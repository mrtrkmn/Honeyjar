	var homeGrey = "icons/grey/Home.png";
	var testGrey = "icons/grey/Test.png";
	var securityGrey = "icons/grey/Security.png";
	var settingsGrey = "icons/grey/Settings.png";
	var logGrey = "icons/grey/Log.png";
	var homeOrange = "icons/orange/Home.png";
	var testOrange = "icons/orange/Test.png";
	var securityOrange = "icons/orange/Security.png";
	var settingsOrange = "icons/orange/Settings.png";
	var logOrange = "icons/orange/Log.png";

function changeImageHome(src){
	document.getElementById("home").src = src;
}
function changeImageTest(src){
	document.getElementById("test").src = src;
}
function changeImageSecurity(src){
	document.getElementById("security").src = src;
}
function changeImageSettings(src){
	document.getElementById("settings").src = src;
}
function changeImageLog(src){
	document.getElementById("log").src = src;
}
function tabOpen(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}