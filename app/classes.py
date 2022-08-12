import http.client
import json
from .models import *


def get_output(code, language, Input):
    language = "python3"

    conn = http.client.HTTPSConnection("api.jdoodle.com")
    payload = json.dumps({
        "script": code,
        "language": language,
        "stdin": Input,
        "versionIndex": "0",
        "clientId": "126c5a1a760ac38356541c8fc221c342",
        "clientSecret": "61503581d612fb562b0955798fa707e163e5b92d7c8e57c202dc5a961520ea87"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/execute", payload, headers)
    res = conn.getresponse()
    data = res.read()
    string_output = data.decode("utf-8")
    dictionary_output = json.loads(string_output)
    print(dictionary_output)
    return dictionary_output['output'].rstrip("\n")

class Game1:
    def __init__(self):
        self.ID = 1
        self.Game = Game.objects.get(id=self.ID)
        self.tests = Test.objects.filter(Game_Id=self.ID)

    def collect_data(self, code, language):
        Positions_Of_All_Tests = []
        results = []
        Total_Score = 0
        for test in self.tests:
            positions, result, Score = self.get_positions_result_score(test, code, language)
            results.append(result)
            Positions_Of_All_Tests.append(positions)
            Total_Score += Score

        Positions_Of_All_Tests = " ".join(Positions_Of_All_Tests)
        results = " ".join(results)
        Total = "{} {} {}".format(Total_Score, round(100*Total_Score/self.Game.Score), self.get_color(self.Game, Total_Score))
        return results, Total, Positions_Of_All_Tests

    def get_positions_result_score(self, test, code, language):
        positions = []
        Input = list(map(int, test.Input.split()))
        x, y = Input[0], Input[1]
        output = get_output(code, language, test.Input)
        directions = output.split()
        for direction in directions:
            if direction == "a":
                y -= 20
            elif direction == "b":
                x += 20
            elif direction == "c":
                y += 20
            elif direction == "d":
                x -= 20
            String = "{},{}".format(x, y)
            positions.append(String)
        positions = "-".join(positions)
        if x == Input[2] and y == Input[3]:
            Score = test.Score
        else:
            Score = 0
        result = "{},{},{}%,{}".format(test.Test_Id, Score, round(100*Score/test.Score), self.get_color(test, Score))
        return positions, result, Score

    def get_color(self, object, score):
        percentage = round(100*score/object.Score)
        if percentage < 50:
            color = "red"
        elif percentage > 50 and percentage < 70:
            color = "orange"
        else:
            color = "green"
        return color
