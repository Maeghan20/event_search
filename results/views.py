from django.shortcuts import render
import requests

def index(request):
    if request.method == 'POST':
        Event_ID = request.POST.get("Event_ID")
        doe = request.POST.get("DOE")
        api_url = f'http://127.0.0.1:8000/events/{Event_ID}/{doe}'  # Replace with your API endpoint URL
        response = requests.get(api_url)
        event_data = response.json()
        if response.status_code == 200:
            event_data = response.json()
            return render(request, 'results.html', {'event_data': event_data})
        else:
            return render(request, 'index.html', {'message': 'Failed to fetch event results. Check Again!'})
    
        
    return render(request, 'index.html')












