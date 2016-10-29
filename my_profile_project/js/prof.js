$(document).ready(function(){

  $('#right-button').click(function() {
      event.preventDefault();
      $('#content').animate({
        marginLeft: "-=200px"
      }, "fast");
   });



$('#left-button').click(function() {
      event.preventDefault();
      $('#content').animate({
        marginLeft: "+=200px"
      }, "fast");
   });
});

console.log("Hello");

/*function backgroundImage() {
  $("#walk").css({
    'background-image': 'url(http://media1.santabanta.com/full5/Animals/Cats/cats-)'
    'width':'1000px',
    'height': '1000px'
  })
}

.append
*/
