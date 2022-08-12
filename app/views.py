from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .classes import *


def get_participant(request):
    current_user = request.user
    participant = Participant.objects.get(Username=current_user.username)
    return participant


def get_advancement(game, participant):
    try:
        advancement = Advancement.objects.get(Game_Id=game.id, Participant_Id=participant.id)
    except:
        List = ["{},0,0%,black".format(i+1, i+1) for i in range(game.Number_Of_Tests)]
        advancement = Advancement(Game_Id=game.id, Participant_Id=participant.id,
                                  Wrote_Code=game.Default_Python_Code, Used_Language="Python",
                                  Results=" ".join(List))
        advancement.save()
    results = advancement.Results.split(" ")
    results = [ele.split(",") for ele in results]
    return advancement, results


@login_required(login_url='login')
def Play(request, id):
    values = ["c", "cpp", "py", "node", "php", "java"]
    languages = ["C", "C++", "Python3", "Node JS", "PHP", "Java"]
    options = list(zip(values, languages))
    game = Game.objects.get(id=id)
    participant = get_participant(request)
    advancement, results = get_advancement(game, participant)
    context = {'game':game, 'advancement':advancement, 'results':results, 'options':options}
    return render(request, "Game.html", context)


@login_required(login_url='login')
def Home(request):
    games = Game.objects.all()
    participant = get_participant(request)
    context = {'games':games, 'participant':participant}
    return render(request, 'Home.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Le nom d'utilisateur ou le mot de passe est incorrect")
    return render(request, 'LoginPage.html')


def Logout(request):
    logout(request)
    return redirect('login')


def CollectData(code, language, id):
    ClassName = "Game{}()".format(id)
    Object = eval(ClassName)
    data = Object.collect_data(code, language)
    return data


def Update_Advancement(request, game_id, language, code, Total, results):
    game = Game.objects.get(id=game_id)
    participant = get_participant(request)
    advancement = Advancement.objects.get(Game_Id=game.id, Participant_Id=participant.id)
    advancement.Wrote_Code = code
    advancement.Used_Language = language
    advancement.Score = int(Total.split(" ")[0])
    advancement.Percentage = int(Total.split(" ")[1])
    advancement.Color = Total.split(" ")[2]
    advancement.Results = results
    advancement.Number_Of_Tests += 1
    advancement.save()


def Update_Score(request):
    participant = get_participant(request)
    advancements = Advancement.objects.filter(Participant_Id=participant.id)
    participant.Score = sum([advancement.Score for advancement in advancements])
    participant.Number_Of_Tests = sum([advancement.Number_Of_Tests for advancement in advancements])
    participant.save()


@login_required(login_url='login')
def Ranking(request):
    participants = Participant.objects.all().order_by('Score').reverse()
    context = {'participants':participants, 'pass':5}
    return render(request, "Ranking.html", context)


@csrf_exempt
def Lunch_Tests(request, id):
    code = request.POST["code"]
    language = request.POST["language"]
    results, Total, Positions_Of_All_Tests = CollectData(code, language, id)
    Update_Advancement(request, id, language, code, Total, results)
    Update_Score(request)
    data = "{}&{}&{}".format(results, Total, Positions_Of_All_Tests)
    return HttpResponse(data)


