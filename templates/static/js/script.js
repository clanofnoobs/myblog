$(function myFunction (){
 $("#admin2").click(function (){
 	
 	
 	$("#loginModal").fadeIn();
 	$("#headframe").fadeIn();
 	$("#overlay").fadeIn();
 });
 
 $("#overlay").click(function(){
	$("#loginModal").fadeOut(250);
 	$("#headframe").fadeOut(250);
 	$("#overlay").fadeOut(950);
 });
 


});

$(function (){
 $("#menub").hover(function (){
 
 $("#menu").stop().fadeToggle(250);
 });

});
