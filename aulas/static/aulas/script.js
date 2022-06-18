$('.card').owlCarousel({
            margin:20,
            loop:true,
            autoplayTimeOut:2000,
            autoplayHoverPauser:true,
            responsive:{
                0:{
                    items:1,
                    nav:false
                },
                500:{
                    items:2,
                    nav:false
                },
                1440:{
                    items:3,
                    nav:false
                }
            }
        })

$('.btn').click(function(){
    $('.menu-mobile').slideToggle('show')
})

document.getElementById("aulas").onload = function() {verifyButton()};

function  selectAula(evt, itemId) {
    // declare variables
    var i, count,  buttons, test;
    buttons = document.querySelectorAll(".checkboxaula");
    console.log(itemId);
    console.log(buttons);

    // verify if the button was clicked
    for (i=0; i < buttons.length; i++) {

        if (buttons[i].value === itemId) {
            const max = buttons[i].querySelector("input#max_alunos").value;
            const numero = buttons[i].querySelector("input#numero_alunos").value;
            console.log("Checking the max_alunos");
            console.log(max);
            console.log("Checking the numero_alunos");
            console.log(numero);
            if (max === numero) {
                console.log("Máxima capacidade"); 
                checkboxes = document.querySelectorAll(".form-check-input");
                for (i=0; i < checkboxes.length; i++) {
                    if (checkboxes[i].value === itemId) {
                        checkboxes[i].disabled = "True";
                    }
                }
            }
        }
    }

}

function  verifyButton() {
    // declare variables
    var i, j, buttons;
    buttons = document.querySelectorAll(".form-check");
    console.log(buttons);
    console.log("Load");

    // verify if the checkbox need to be disabled
    for (i=0; i < buttons.length; i++) {
        const max = buttons[i].querySelector("input#max_alunos").value;
        const numero = buttons[i].querySelector("input#numero_alunos").value;
        console.log("Checking the max_alunos");
        console.log(max);
        console.log("Checking the numero_alunos");
        console.log(numero);
        if (max === numero) {
            console.log("Máxima capacidade"); 
            checkboxes = buttons[i].querySelector(".form-check-input");
            checkboxes.disabled = "True";
            checkboxes.style.backgroundColor = "Red";
        }
    }

}
