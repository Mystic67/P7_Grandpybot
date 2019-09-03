// Chat content element
let chatContentElt = document.getElementById('chat_content');
// function scroll to last message
function scrollToLastMessage(){
    chatContentElt.scrollTop = (chatContentElt.scrollHeight);
}
// init instance id from google map
let mapId = 0;
//########## google maps with args lattitude and longitude
function displayGoogleMapsElt(location){
    //let chatContentElt =  document.getElementById('chat_content');
    let googleMapsElt = document.createElement("div");
    googleMapsElt.id = "map"+mapId
    googleMapsElt.className = "col-10 offset-1 text_center";
    chatContentElt.appendChild(googleMapsElt);
    myMap = initMap(location);
    google.maps.event.addDomListener(window, "load", myMap);
    mapId++;
}

//################## function to init google maps ##############################
function initMap(mapLocation){
    let location = mapLocation;
    let map = new google.maps.Map(document.getElementById("map"+mapId),{
        zoom: 18,
        center: location,
        zoomControl: true,
        gestureHandling: 'none',
        zoomControlOptions: {
            position: google.maps.ControlPosition.RIGHT_CENTER,
        },
        styles: [
            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'geometry',
              stylers: [{color: '#263c3f'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'labels.text.fill',
              stylers: [{color: '#6b9a76'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: '#38414e'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              elementType: 'geometry',
              stylers: [{color: '#2f3948'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#17263c'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
          ]
    });
    let marker = new google.maps.Marker({
        position: location,
        map: map
    });
}

//###### fonction create and display question or answer chat bubble element ####
function displayChatBubbleElt(typeBubble = "q", textBubble, scroll){
    let row = document.createElement('div');
    row.className="row col-12";
    let chatBubbleElt = document.createElement("p");
    chatBubbleElt.textContent = textBubble;
    if (typeBubble =='q'){
        chatBubbleElt.className = "question-bubble col-6 offset-6 float-left";
    }
    else {
        chatBubbleElt.className = "answer-bubble col-6 float-left";
    }
    row.appendChild(chatBubbleElt);
    chatContentElt.appendChild(row);
    if (scroll == true){
        scrollToLastMessage();
    }
}

let searchFormElt = document.querySelector('form');
let inputFormElt = document.querySelector('input');
let submitButtonElt = document.getElementById('btn');

//################### AJAXPOST function() ######################################
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Appelle la fonction callback en lui passant la réponse de la requête
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    if (isJson) {
        // Définit le contenu de la requête comme étant du JSON
        req.setRequestHeader("Content-Type", "application/json");
        // converti  l'objet javascript au format JSON
        data = JSON.stringify(data);
    }
    req.send(data);
}

//################## Button Submit Event using AJAXPOST ########################
searchFormElt.addEventListener("submit", function(e){
    e.preventDefault();
    let userMessage = searchFormElt.elements['search'].value
    let data = [{ userMessage : userMessage}]
    this.focus();
    this.value = ""
    //data = {userMessage : userMessage}
    //console.log(userMessage)
    displayChatBubbleElt('q',userMessage, true);
    //post_resquest_to_server(userMessage);
    ajaxPost('/search', data, function(response){
        // Call function traitementResponse()
        traitementResponse(response);
        },
        true
    );
    inputFormElt.value = "";
    inputFormElt.focus()
    //submitButtonElt.disabled = true;
});
//########### Response traitement with data returned by AJAXPOST ###############
function traitementResponse(dataResponse){
    // convert JSON to Javascript object
    dataResponse = JSON.parse(dataResponse);
    console.log("La requête a été envoyée !");
    //console.log(dataResponse);

    // Init the response values
    mapsStatus = dataResponse['maps_infos']['status'];
    //console.log(mapsStatus);
    mapsBotMessage = dataResponse['maps_bot_message'];
    //console.log(mapsBotMessage);
    adress = dataResponse['maps_infos']['adress'];
    //console.log(adress);
    mapLocation = dataResponse['maps_infos']['location'];
    //console.log(mapLocation);
    wikiStatus = dataResponse['wikiInfos']['status'];
    console.log(wikiStatus);
    wikiBotMessage = dataResponse['wiki_bot_message']
    console.log(wikiBotMessage);
    wikiText = dataResponse['wikiInfos']['text'];
    console.log(wikiText);

    //################ Display the response bubbles ############################
    if (mapsStatus == "OK"){
        displayChatBubbleElt('a',mapsBotMessage + "   " + adress);
        setTimeout(function(){ displayGoogleMapsElt(mapLocation) } ,3000);
        setTimeout(function(){ displayChatBubbleElt('a',wikiBotMessage,true)} ,5000);
        if (wikiStatus == "OK"){
            setTimeout(function(){ displayChatBubbleElt('a',wikiText)} ,10000);
        }
    }
    else{
        displayChatBubbleElt('a',mapsBotMessage);
        setTimeout(function(){ displayChatBubbleElt('a',wikiBotMessage)} ,5000);
        if (wikiStatus == "OK"){
            setTimeout(function(){ displayChatBubbleElt('a',wikiText)} ,10000);
        }
    }

}

//###################### Display the welcome Bubble ###########################
let text = "Salut ! Je suis GrandPy, demande moi, un lieu, une adresse et je te compterai son histoire";

displayChatBubbleElt('a',text);
