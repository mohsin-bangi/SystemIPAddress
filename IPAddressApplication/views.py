from django.shortcuts import render,redirect
import socket
# Create your views here.


def function(request):
    return render(request,"homePage.html")

def openLink(request):
    return redirect('getIPAddress')

def getIPAddress(request):
    machineName = socket.gethostname()
    machineIPAddress = socket.gethostbyname(machineName)
    return render(request,"ApplicationPage.html",{"dictionary":{"machineName": machineName,"machineIPAddress": machineIPAddress}})
