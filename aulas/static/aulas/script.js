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

function  selectAula(evt, itemId) {
    // declare variables
    var i, count,  buttons, test;
    buttons = document.getElementById("aulas").querySelectorAll(".aula");
    console.log(itemId);
    console.log(buttons);
    test = document.getElementById("aulas");
    console.log(test);
    const test1 = document.querySelectorAll(".aula");
    console.log(test1);
    const test2 = document.querySelectorAll(".buttonaula");
    console.log(test2);

    // verify if the button was clicked



}