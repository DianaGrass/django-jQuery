$("document").ready(function () {
    let id;
    $.ajax({'url': "/add_like/",
    "data": {'id': id},
    "success": function(data){
    $("#" + id).html("Likes " + data)}
    })
    }