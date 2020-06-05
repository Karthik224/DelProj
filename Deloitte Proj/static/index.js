let code = ""
jqueryElem = $("#clickMe")
var singleClickTimer = 0;
jqueryElem.click(function(e){
    if (e.detail == 1) {
        singleClickTimer = setTimeout(function(){
            code+='.'
            $("input.clicked").val(code);
        },250);
    }
});
jqueryElem.dblclick(function(e){
    clearTimeout(singleClickTimer);
    code+='-'
    $("input.clicked").val(code);
});
jqueryElem.mouseup(function(e){
    e.preventDefault();
    if (e.which == 3){
        code+=' '
        $("input.clicked").val(code+'|');
    }
});
$("input[type=submit]").click(function (e){
    e.preventDefault();
    $("input.clicked").val("")
    axios.post('/api/get', {"braille": code}).then((response)=>{
        $('.cont').html(response["data"]);
    }, (error)=>{
        $('.cont').html("Nothing exists for such braille");
    });
    code = ""
});
