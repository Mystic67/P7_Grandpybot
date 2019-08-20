// Chat content element
let chatContentElt = document.getElementById('chat_content');
// function scroll to last message
function scrollToLastMessage(){
    chatContentElt.scrollTop = chatContentElt.scrollHeight;
}
// init instance id from google map
let mapId = 0;
// display google maps with args lattitude and longitude
function displayGoogleMapsElt(lat, lng){
    //let chatContentElt =  document.getElementById('chat_content');
    let googleMapsElt = document.createElement("div");
    googleMapsElt.id = "map"+mapId
    googleMapsElt.className = "col-10 offset-1 text_center";
    chatContentElt.appendChild(googleMapsElt);
    myMap = initMap(lat, lng, mapId);
    google.maps.event.addDomListener(window, "load", myMap);
    mapId++;
}

// function to init google maps
function initMap(latitude,longitude, id){
    let location = {lat: latitude, lng: longitude};
    let map = new google.maps.Map(document.getElementById("map"+mapId),{
        zoom: 18,
        center: location,
        zoomControl: true,
        gestureHandling: 'none',
        zoomControlOptions: {
            position: google.maps.ControlPosition.RIGHT_CENTER,
        }
    });
    let marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

// fonction create and display question or answer chat bubble element
function displayChatBubbleElt(typeBubble = "q", textBubble){
    let row = document.createElement('div');
    row.className="row col-12";
    let chatBubbleElt = document.createElement("p");
    chatBubbleElt.textContent = textBubble;
    if (typeBubble =='q'){
        chatBubbleElt.className = "answer-bubble col-6 offset-6 float-left";
    }
    else {
        chatBubbleElt.className = "question-bubble col-6 float-left";
    }
    row.appendChild(chatBubbleElt);
    chatContentElt.appendChild(row);
    scrollToLastMessage();
}

let searchFormElt = document.querySelector('form');
let inputFormElt = searchFormElt.elements["search"]

searchFormElt.addEventListener("submit",function(e){
    e.preventDefault();
    displayChatBubbleElt('q',searchFormElt.elements["search"].value);
    inputFormElt.value = "";
    inputFormElt.focus();

});

//###################### Test ############################################ 
text = "Salut ! Je suis GrandPy, demande moi, un lieu, une adresse et je te compterai son histoire";
autreText = "Je fais un petit test";

displayChatBubbleElt('a',text);
displayChatBubbleElt('q',autreText);

displayGoogleMapsElt(48.8748465,2.3504873);
//displayGoogleMapsElt(48.693802,6.183263);
//displayGoogleMapsElt(48.704502,6.183263);
//displayGoogleMapsElt(48.704502,6.185563);
