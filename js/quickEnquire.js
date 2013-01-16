// JavaScript Document

function clearValue(id)
{
	id.setAttribute("value"," ");
}

function validateC()
{
	var k=0;
	var ele=document.getElementById("contactno");
	if(ele.value.length<8)
	{
		var mobno=/^[0-9]+$/; 
		var emailexp=/^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-Z0-9\.\-]{2,4}$/;
		if(!ele.value.match(emailexp)||!ele.value.match(mobno))
			ele.setAttribute("value","Wrong Entry !");
			ele.focus() 
	}
}