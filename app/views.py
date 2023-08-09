from django.contrib.sites import requests
import requests
from django.shortcuts import render
import json


def index(request):
    return render(request, "index.html")


def getsettings(request):
    id_instance = request.GET.get('idInstance')
    api_token_instance = request.GET.get('apiTokenInstance')
    url_template = f"https://api.green-api.com/waInstance{id_instance}/getSettings/{api_token_instance}"
    payload = ''
    headers = {}
    response = requests.get(url=url_template, headers=headers, data=payload)
    response_data = response.json()
    return render(request, "index.html", {"get_settings": response_data,
                                          "id_instance": id_instance,
                                          "api_token_instance": api_token_instance})


def getstateinstance(request):
    id_instance = request.GET.get('idInstance')
    api_token_instance = request.GET.get('apiTokenInstance')
    url_template = f"https://api.green-api.com/waInstance{id_instance}/getStateInstance/{api_token_instance}"
    payload = ''
    headers = {}
    response = requests.get(url=url_template, headers=headers, data=payload)
    response_data = response.json()
    return render(request, "index.html", {"get_settings": response_data,
                                          "id_instance": id_instance,
                                          "api_token_instance": api_token_instance})


def sendmessage(request):
    id_instance = request.POST['idInstance']
    api_token_instance = request.POST['apiTokenInstance']
    url_template = f"https://api.green-api.com/waInstance{id_instance}/sendMessage/{api_token_instance}"
    chatId = request.POST['chatId']
    message = request.POST['message']
    payload = json.dumps({
        "chatId": f"{chatId}",
        "message": f"{message}",
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url_template, headers=headers, data=payload)
    response_data = response.text
    return render(request, "index.html", {"get_settings": response_data,
                                          "id_instance": id_instance,
                                          "api_token_instance": api_token_instance})


def sendfilebyurl(request):
    id_instance = request.POST['idInstance']
    api_token_instance = request.POST['apiTokenInstance']
    url_template = f"https://api.green-api.com/waInstance{id_instance}/sendFileByUrl/{api_token_instance}"
    chatId = request.POST.get("chatId")
    urlFile = request.POST.get("urlFile")
    payload = json.dumps({
        "chatId": f"{chatId}",
        "urlFile": f"{urlFile}",
        "fileName": "test.png",
        "caption": "test",
    })
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url=url_template, headers=headers, data=payload)
    response_data = response.text
    return render(request, "index.html",  {"get_settings": response_data,
                                           "id_instance": id_instance,
                                           "api_token_instance": api_token_instance})
