$(function myFunction (){
 $("#admin2").click(function (){
 	
 	
 	$("#loginModal").fadeIn();
 	$("#headframe").fadeIn();
 	$("#overlay").fadeIn();
 });
 
 $("#overlay").click(function(){
	$("#loginModal").fadeOut(250);
 	$("#headframe").fadeOut(250);
 	$("#overlay").fadeOut(650);
 });

});
$(document).ready(function (){
$("#portfolio li img").click(function(e){
        var src = $(this).attr("src");
        var des = $(this).next("p").clone();
        $("#description p").html(des);
        $("#frame img").attr("src", src); 
        $("#frame").fadeIn();
        $("#overlay").fadeIn();
});
$("#overlay").click(function(){
        $("#frame").fadeOut();
        $("#overplay").fadeOut();
});
$("#arrowright").click(function(){
    closest("#portfolio").next().find('img').trigger('click');
});
        
});

$(function (){
 $("#menub").hover(function (){
 
 $("#menu").stop().fadeToggle(250);
 });

});

$(function (){
 $("#frame").hover(function (){
 var topx = $("#frame img").height()/2;
 $("#arrowleft,#arrowright").fadeIn(200);
 $("#arrowleft,#arrowright").css({"top":topx});
 $("#description").fadeIn(200);
 }
 ,
 function(){
 //$("#description").css({"display":"none"});
 $("#description").stop().fadeOut(200);
 //$("#arrowleft,#arrowright").css({"display":"none"});
 $("#arrowleft,#arrowright").stop().fadeOut(200);
     
 });

});

