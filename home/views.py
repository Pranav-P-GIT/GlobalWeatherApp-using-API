from django.shortcuts import render
import requests


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city_name=city
        api =requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=<token>').json()
        city_coord = api.get('coord')
        if city_coord is None:
            msg = "Could not get weather details for the specified place"
            return render(request, "index.html", {"msg":msg})
        else:
            context = {"coordinate": str(api['coord']['lon']) + ', '
                + str(api['coord']['lat']),
                "temp": str(api['main']['temp']) + ' °C',
                "pressure": str(api['main']['pressure']),
                "humidity": str(api['main']['humidity']),
                'main': str(api['weather'][0]['main']),
                'description': str(api['weather'][0]['description']),
                'icon': api['weather'][0]['icon'],"city_name": city_name}      
    else:
        context = {}
    return render(request, "index.html", context)



    
