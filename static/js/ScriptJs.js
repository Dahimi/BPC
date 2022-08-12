let editor;
var processingInstance;
window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    changeLanguage();
}

function changeLanguage() {

    let language = $("#languages").val();

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'php')editor.session.setMode("ace/mode/php");
    else if(language == 'py')editor.session.setMode("ace/mode/python");
    else if(language == 'node')editor.session.setMode("ace/mode/javascript");
    else if(language == 'java')editor.session.setMode("ace/mode/java");
}

function LunchTests(){
    var code = editor.getSession().getValue();
    var language = $("#languages").val();
    $.ajax({
       type: "POST",
       url: 'my-ajax-test/',
       data: { csrfmiddlewaretoken: '{{ csrf_token }}', code: code, language:language},
       success: function callback(response){
                   var myArray = response.split("&");
                   var      Data = myArray[2].split(" ");
                   var results = myArray[0].split(" ");
                   var total = myArray[1].split(" ");
                   for (let i = 0; i < Data.length; i++) {
                           var test_data = Data[i];
                           var info = results[i];
                           Update(info, i);
                           StartSimulation(test_data);
                   }
                   UpdateTotal(total);
       }
    });

}

function UpdateTotal(list){
    document.getElementById("score total").style.color = list[2];
    document.getElementById("pourcentage total").style.color = list[2];
    document.getElementById("score total").innerHTML = "SCORE TOTAL:"+list[0];
    document.getElementById("pourcentage total").innerHTML = "POURCENTAGE:"+list[1]+"%";
}
function Update(string, i){
    var list = string.split(",");
    document.getElementById("test"+list[0]).style.color = list[3];
    document.getElementById("score"+list[0]).style.color = list[3];
    document.getElementById("pourcentage"+list[0]).style.color = list[3];
    document.getElementById("score"+list[0]).innerHTML = list[1];
    document.getElementById("pourcentage"+list[0]).innerHTML = list[2];
}

function StartSimulation(string){

        processingInstance = Processing.getInstanceById('sketch');
        processingInstance.StartSimulation(string);

}