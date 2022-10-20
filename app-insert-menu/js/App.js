$(document).ready(function () {
    getMenuBiru();  
});

function getMenuBiru() {
    var settings = {
        "url": './php/getMenuBiru.php',
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "async": false
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
        if (response.success) {
            console.log(response)
            // $("#table_menu").append(respon);
        }
    });
};