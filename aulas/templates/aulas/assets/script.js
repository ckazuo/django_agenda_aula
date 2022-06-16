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