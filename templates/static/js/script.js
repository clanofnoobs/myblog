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
$("#portfolio img").click(function(){
        var src = $(this).attr("src");
        $("#frame img").attr("src", src); 
        $("#frame").fadeIn();
        $("#overlay").fadeIn();
});
$("#overlay").click(function(){
        $("#frame").fadeOut();
        $("#overplay").fadeOut();
});
        
});

$(function (){
 $("#menub").hover(function (){
 
 $("#menu").stop().fadeToggle(250);
 });

});
