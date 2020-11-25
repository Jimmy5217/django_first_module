from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    api_request = requests.get("https://api.github.com/users?since=0")
    api = json.loads(api_request.content)
    return render(request, 'home.html', {"api": api})

def user(request):
    if request.method == "POST":
        import requests
        import json
        user = request.POST['user']
        user_request = requests.get("https://api.github.com/users/" + user)
        userData = json.loads(user_request.content)
        return render(request, 'user.html', {"user": user, "userData": userData})
    else:
        notfound = "Please input the user name you want to query in box"
        return render(request, 'user.html', {'notfound': notfound})