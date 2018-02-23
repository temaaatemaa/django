from django.shortcuts import render
from .models import Users
from .models import Systems, FullTable,Priority,Time
import json
from django.shortcuts import redirect
# Create your views here.

def mainView(request):
	users = Users.objects.all()
	allSystems = Systems.objects.all()
	allPriority = Priority.objects.all()
	allTime = Time.objects.all()
	return render(request, 'logic/main.html', {'users': users,'allSystems':allSystems,'allPriority':allPriority,'allTime':allTime})
	
def setupUser(request,pk):
	userMatch = Users.objects.get(fio=pk)
	fulltable = FullTable.objects.filter(user = userMatch)
	#userSystems = fulltable.system.all()
	allSystems = Systems.objects.all()
	allPriority = Priority.objects.all()
	allTime = Time.objects.all()
	userSystems = set()
	for rows in fulltable:
		userSystems.add(rows.system)
		
	
	return render(request, 'logic/user_setup.html', {'user':userMatch ,'userSystems':userSystems,'allSystems':allSystems,'allPriority':allPriority,'allTime':allTime,'fulltable':fulltable})
	
def addRow(request,fio,system,priority,time):
	user = Users.objects.get(fio = fio)
	chooseSystem = Systems.objects.get(name = system)
	choosePrior = Priority.objects.get(name = priority)
	chooseTime = Time.objects.get(description = time)
	a = FullTable.objects.filter(user=user,system = chooseSystem,priotiry = choosePrior,time = chooseTime).first()
	if not a:
		FullTable.objects.create(user=user,system = chooseSystem,priotiry = choosePrior,time = chooseTime)
	return redirect('setupUser',pk = fio)
	#127.0.0.1:8000/add_row/Иванов/Маленькая/Низкая/Утро/
	
def delRow(request,fio,system,priority,time):
	user = Users.objects.get(fio = fio)
	chooseSystem = Systems.objects.get(name = system)
	choosePrior = Priority.objects.get(name = priority)
	chooseTime = Time.objects.get(description = time)
	a = FullTable.objects.filter(user=user,system = chooseSystem,priotiry = choosePrior,time = chooseTime).delete()
	return redirect('setupUser',pk = fio)
	
#def addSituation(request)
#	return H
	#return render(request, 'logic/main.html', {'users': users})
	