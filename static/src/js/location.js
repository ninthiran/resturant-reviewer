 function mapPlotter(restname)
 {    

	var geojson = [];
         
         // Creating a map object
		var map = L.map('map').setView([51.505, -0.09], 10);
         
         // Creating a Layer object
        var layer = new L.TileLayer('https://stamen-tiles-{s}.a.ssl.fastly.net/toner/{z}/{x}/{y}.png', { minZoom: 10, maxZoom: 15 });
		map.addLayer(layer);        

		// Adding layer to the map
        var markerOptions = {
            title: "MyLocation",
            clickable: true,
            draggable: true
         }

        // Getting location data saved from corresponding resturant name

        $.getJSON("/static/src/js/"+restname+".json", function (data) {
		var myStyle = {
        radius: 5,
        fillColor: "red",
        weight: 1,
        opacity: 0.7,
        fillOpacity: 0.6,
        stroke: "black"
    	};
	
	    var geojson = L.geoJson(data, {
	        pointToLayer: function (feature, layer) {
	        	content = "<b>Rating</b> - " + feature.properties.star +" star </br><b>Review</b></br> " + feature.properties.text + 
	        			  "<br/><br/><b>Posted at:</b> " + feature.properties.created_at;

	        	switch(feature.properties.star)
	        	{
	        		case '1':
	        		case 1:
		        		myStyle = {
							        radius: 5,
							        fillColor: "red",
							        weight: 1,
							        opacity: 1,
							        fillOpacity: 0.6
							    	};
						break;

					case '2':
					case 2:
		        		myStyle = {
							        radius: 5,
							        fillColor: "red",
							        weight: 1,
							        opacity: 0.5,
							        fillOpacity: 0.6
							    	};
						break;

	        		case '3':
	        		case 3:
		        		myStyle = {
							        radius: 5,
							        fillColor: "yellow",
							        weight: 1,
							        opacity: 1,
							        fillOpacity: 0.6
							    	};
						break;

					case '4':
					case 4:
		        		myStyle = {
							        radius: 5,
							        fillColor: "green",
							        weight: 1,
							        opacity: 0.5,
							        fillOpacity: 0.6
							    	};
						break;

					case '5':
					case 5:
		        		myStyle = {
							        radius: 5,
							        fillColor: "green",
							        weight: 1,
							        opacity: 1,
							        fillOpacity: 0.6
							    	};
						break;

	        	}
	            return L.circleMarker(layer, myStyle).bindPopup(String(content));
	        }
    	});

    	geojson.addTo(map)
    });

}