

var lat = document.getElementById("latitude");
var long = document.getElementById("longitude");
function getUserLocation() 
{
    if (navigator.geolocation) 
    {
        navigator.geolocation.getCurrentPosition(showuserPosition);
    } 
    else 
    { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showuserPosition(position) {
    lat.value = position.coords.latitude;
    long.value = position.coords.longitude;
}

function formValidation() {
  var flag = 0;
    
  if(document.getElementById("reviewText").value=="")
  {
    $("#reviewText").addClass("errorHighlighter");
    flag++;
  }else
  {
    $("#reviewText").removeClass("errorHighlighter");
  }

  if (document.getElementById("name").value == "") {
        $("#name").addClass("errorHighlighter");
        flag++;
    }
    else
    {
      $("#name").removeClass("errorHighlighter");
    }

    if(flag>0)
    {
      return false;
    }
  
}


function formValidation1() {
  var flag = 0;
    
  if(document.getElementById("rname").value=="")
  {
    $("#rname").addClass("errorHighlighter");
    flag++;
  }else
  {
    $("#rname").removeClass("errorHighlighter");
  }


    if(flag>0)
    {
      return false;
    }
  
}

function getRestaurant(restName,my_prediction) {

  $.getJSON('/static/src/js/restaurant-deatils.json', function(data) {
    var items = [];
    $.each(data, function(i, item) {
        if(restName == item.name)
        {
          $("#restAddress").text(item.address);
        }
    });
  });
  for(var i = 1; i <= my_prediction ; i++)
  {
    $("#starHighlighter").append('<span>★</span>');
  }

}