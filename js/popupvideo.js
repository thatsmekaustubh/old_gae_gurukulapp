// JavaScript Document
function playVideo()
{
	var divpop=document.createElement("div");
	divpop.setAttribute("id","popupvideo");
	divpop.setAttribute("style","width:100%;height:100%;background-color:#000;opacity:0.6;top:0px;position:fixed;");
	divpop.setAttribute("onclick","poppoof()");
	var mainEle=document.body;
	mainEle.appendChild(divpop);

    var styleCon="margin-top:10%;height:60%;margin-left:20%;width:60%;background-color:#FFF;top:0px;position:fixed;";
	var divpop=document.createElement("div");
	divpop.setAttribute("id","container");
	divpop.setAttribute("style",styleCon);
	divpop.innerHTML="Hello world";
	var mainEle=document.body;
	mainEle.appendChild(divpop);
	
	var playerDiv = document.getElementById("container");
	playerDiv.innerHTML="<img src='images/map.png'/>";

}

function poppoof()
{
	var mainEle=document.body;
	var popDiv=document.getElementById("popupvideo");
	var popContainer=document.getElementById("container");
	
	mainEle.removeChild(popDiv);
	mainEle.removeChild(popContainer);
}