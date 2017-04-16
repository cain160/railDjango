/**
 * Created by jojo on 3/6/17.
 */

var map;
var devices = [];
var pathToDraw;

/*class Coord{
 long;
 lat;
 deviceID;
 constructor(lat,long,deviceID){
 this.long = long;
 this.lat = lat;
 this.deviceID = deviceID;
 }
 getlat(){
 return this.lat;
 }
 getlong(){
 return this.long;
 }
 getdeviceID(){
 return this.deviceID;
 }
 }*/

function updateDevices(lat, long, vehiculeID) {
    devices.push([lat, long, vehiculeID]);
//alert(devices);
}


function corMap() {
    var x = document.getElementById("myLat").value;
    var y = document.getElementById("myLon").value;
}
function drawMarker(lat, lon, vehiculeID) {

    //var uluru = {lat: -25.363, lng: 131.044};
    //N = Positive
    //S = Negative
    //W = Negative
    //E = Positive
    //var x = document.getElementById("myLat").value;
    //var y = document.getElementById("myLon").value;
    //Vehicle 1 Coordinates


    var myCenter = {lat: lat, lng: lon};


    var mapCanvas = document.getElementById("map");


    //var mapOptions = {center: myCenter, zoom: 4};


    // map = new google.maps.Map(mapCanvas, mapOptions);


    var marker = new google.maps.Marker({position: myCenter, animation: google.maps.Animation.BOUNCE});


    marker.setMap(map);

    var infowindow = new google.maps.InfoWindow({
        content: vehiculeID
    });

    // Zoom to 9 when clicking on marker
    google.maps.event.addListener(marker, 'click', function () {
        map.setZoom(9);
        map.setCenter(marker.getPosition());
    });

    infowindow.open(map, marker);

}

function updatePath(path) {
    pathToDraw = [];
    pathToDraw = path;

}
function drawPath() {
    var kennesaw = new google.maps.LatLng(33.9397, -84.5197);
    var bigChicken = new google.maps.LatLng(33.9514, -84.5204);
    //Johnnie Maccracken's
    var theBar = new google.maps.LatLng(33.9519, -84.5488);

    var flightPath = new google.maps.Polyline({
        //Start, Dest 1, Dest 2
        path: [kennesaw, bigChicken, theBar],
        strokeColor: "#0000FF",
        strokeOpacity: 0.8,
        strokeWeight: 2
    });
    flightPath.setMap(map);

}
function initMap() {

    markers = [];
    centers = [];
    var x = document.getElementById("myLat").value;
    var y = document.getElementById("myLon").value;

    var x = 33.9397;
    var y = -84.5197;
    //var uluru = {lat: 33.9397, lng: -84.5197};

    // create Centers For each position given by the database.
    var myCenter = {lat: x, lng: y};
    for (device in devices) {
        //alert(devices.length);
        x = devices[device][0];
        y = devices[device][1];
        centers.push({lat: x, lng: y})
    }

    var mapCanvas = document.getElementById("map");
    var mapOptions = {center: myCenter, zoom: 4};
    map = new google.maps.Map(mapCanvas, mapOptions);
    var marker = new google.maps.Marker({position: myCenter, animation: google.maps.Animation.BOUNCE});

    //create markers for each position given by the Database.
    for (var i = 0; i < devices.length; i++) {
        markers.push(new google.maps.Marker({position: centers[i], animation: google.maps.Animation.BOUNCE}))
    }
    marker.setMap(map);


    for (var i = 0; i < devices.length; i++) {
        markers[i].setMap(map);
    }
    // Zoom to 9 when clicking on marker
    google.maps.event.addListener(marker, 'click', function () {
        map.setZoom(9);
        map.setCenter(marker.getPosition());
    });

}
