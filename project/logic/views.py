from django.shortcuts import render
from .models import Users
from .models import Systems, FullTable,Priority,Time
import json
from django.shortcuts import redirect
import email
from django.conf import settings
from django.http import HttpResponse
import os
# Create your views here.

def mainView(request):
	users = Users.objects.all()
	allSystems = Systems.objects.all()
	allPriority = Priority.objects.all()
	allTime = Time.objects.all()
	return render(request, 'logic/main.html', {'users': users,'allSystems':allSystems,'allPriority':allPriority,'allTime':allTime})
	
def setupUser(request,pk):
	users = Users.objects.all()
	userMatch = Users.objects.get(fio=pk)
	fulltable = FullTable.objects.filter(user = userMatch)
	#userSystems = fulltable.system.all()
	allSystems = Systems.objects.all()
	allPriority = Priority.objects.all()
	allTime = Time.objects.all()
	userSystems = set()
	for rows in fulltable:
		userSystems.add(rows.system)
		
	return render(request, 'logic/user_setup.html', {'users':users,'user':userMatch ,'userSystems':userSystems,'allSystems':allSystems,'allPriority':allPriority,'allTime':allTime,'fulltable':fulltable})
	
def setupUserNull(request):
	users = Users.objects.all()
	userMatch = users.first()
	fulltable = FullTable.objects.filter(user = userMatch)
	#userSystems = fulltable.system.all()
	allSystems = Systems.objects.all()
	allPriority = Priority.objects.all()
	allTime = Time.objects.all()
	userSystems = set()
	for rows in fulltable:
		userSystems.add(rows.system)
	return render(request, 'logic/user_setup.html', {'users':users,'user':userMatch ,'userSystems':userSystems,'allSystems':allSystems,'allPriority':allPriority,'allTime':allTime,'fulltable':fulltable})

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
	
def addSituation(request,system,priority,time):
	chooseSystem = Systems.objects.get(name = system)
	choosePrior = Priority.objects.get(name = priority)
	chooseTime = Time.objects.get(description = time)
	if (time == "Рабочее время"):
		a = FullTable.objects.filter(system = chooseSystem,priotiry = choosePrior)
	if (time == "Круглосуточно"):
		a = FullTable.objects.filter(system = chooseSystem,priotiry = choosePrior,time = chooseTime)
	
	stringTel = ''
	for us in a:
		stringTel = stringTel+us.user.phone+' '
	msg = email.mime.text.MIMEText(stringTel)
	msg['Subject'] = 'SMS Sent'
	msg['From'] = 'from-email@sbt.ru'
	msg['To'] = 'sms-server@sbt.ru'
	
	# open a file and save mail to it
	with open('filename.msg', 'w') as out:
	    gen = email.generator.Generator(out)
	    gen.flatten(msg)
	    
	return render(request, 'logic/add_situation.html', {'fulltable':a})
	
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
	