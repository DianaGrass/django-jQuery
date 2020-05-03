$("document").ready(function () {
    let id;
    console.log('hello');
    $(".like_tag").on("click", function() {
        console.log("on_click")
        id = $(this).attr('id');
        console.log(id)
        $.ajax({'url': "/add_like/",
            "data": {'id': id},
            "success": function(data) {
                console.log(data);
                $("#" + id).html("Likes " + data)
            }
        })
    })
})