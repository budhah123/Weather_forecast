from django.shortcuts import render
import requests
# Create your views here.
def home_view(request):
    context = {}
    city_name = ""
  
    if request.method == "POST":
         city_name = request.POST.get('city_name')

         
         url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=4a6e825b478364d3fb67db3ce6a08146'
         data = requests.get(url).json()
         payload = {
              'city_name': data['name'], 'weather': data['weather'][0]['main'], 'icon': data['weather'][0]['icon'],
              'Humidity': data['main']['humidity'], 'Kelvin_Temperature':data['main']['temp'],
              'Celsius_temperature': int(data['main']['temp']- 273),
              'Wind': data['wind']['speed'], 'Pressure':data['main']['pressure'],'Description':data['weather'][0]['description'],'feels_like':int(data['main']['feels_like'] - 273)

         }
         context = {'data':payload}
         
    return render(request,'home.html', context)

