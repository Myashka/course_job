from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt

def aboutCinemas(request):
	request.session["role"] = None
	with open('data.json', 'r', encoding='utf-8') as file:
		data = json.load(file)
	a = {}
	conteiner = []
	for i in data["cinemas"]:
		conteiner.append(i)
		a = {"cinemas": conteiner}
	return render(request, "base.html", a)

def aboutCinema(request, id):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    a = {}
    for i in data["cinemas"]:
        if i["id"] == id:
            a = i
            break
    return render(request, 'about_cinema.html', {'a': a})

def aboutFilm(request, id):
    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    a = {}
    for i in range(len(data["cinemas"])):
        for j in data["cinemas"][i]["films"]:
            if j["id"] == id:
                a = j
                break
    return render(request, 'about_film.html', {'a': a})

@csrf_exempt
def login(request):
    with open('users.json', 'r', encoding='utf-8') as file:
        users = json.load(file)
    request.session["role"] = None
    req = request.POST
    request.session["login"] = req.get("login")
    request.session["password"] = req.get("password")
    page = "login.html"
    for i in users["data"]:
        if i["login"] == request.session["login"] and i["password"] == request.session["password"]:
            request.session["role"] = i["role"]
            break
    if request.session["role"] == "superuser":
        page = "superuser.html"
        return render(request, page)
    elif request.session["role"] == "moderator":
        page = "moderator.html"
        return render(request, page)
    else:
        return render(request, page)

@csrf_exempt
def addCinema(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    id = req.get('id')
	    name = req.get('name')
	    image = req.get('image')
	    location = req.get('location')
	    phone = req.get('phone')
	    if id != None and id != "" and name != "" and location != "":
	        k = 0
	        for i in data['cinemas']:
	            if id == i['id']:
	                k = 1
	                break
	        if k == 0:
	            a = {
	                "id": id,
	                "name": name,
	                "image": image,
	                "location": location,
	                "phone": phone,
	                "films":[]
	            }
	            data['cinemas'].append(a)
	            with open('data.json', 'w', encoding='utf-8') as file:
	                file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	            if request.session["role"] == "superuser":
	            	return render(request, "superuser.html")
	            elif request.session["role"] == "moderator":
	            	return render(request, "moderator.html")
	        else:
	            return render(request, 'add_cinema.html', {})
	    else:
	        return render(request, 'add_cinema.html', {})
	else:
		return login(request)

@csrf_exempt
def addFilm(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    id = req.get('id')
	    name = req.get('name')
	    cinemas = req.get('cinemas')
	    genre = req.get('genre')
	    description = req.get('description')
	    image = req.get('image')
	    duration = req.get('duration')
	    agerating = req.get('agerating')
	    if id != None and id != "" and name != "" and cinemas != "" and genre != ""\
	        and description != "" and image != "" and duration != "" and agerating != "":
	        k = 0
	        for i in range(len(data['cinemas'])):
	            for j in data['cinemas'][i]['films']:
	                if id == j['id']:
	                    k = 1
	                    break
	        if k == 0:
	            a = {
	                "id": id,
	                "name": name,
	                "genre": genre,
	                "description": description,
	                "image": image,
	                "duration": duration,
	                "agerating": agerating,
	                "director": [],
	                "actors": [],
	                "sessions": []
	            }
	            for i in data['cinemas']:
	                if i['name'] == cinemas:
	                    i["films"].append(a)
	                    break
	            with open('data.json', 'w', encoding='utf-8') as file:
	                file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	            if request.session["role"] == "superuser":
	            	return render(request, "superuser.html")
	            elif request.session["role"] == "moderator":
	            	return render(request, "moderator.html")
	        else:
	            return render(request, 'add_film.html', {})
	    else:
	        return render(request, 'add_film.html', {})
	else:
		return login(request)
	

@csrf_exempt
def addDir(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    full_name = req.get('full_name')
	    image = req.get('image')
	    films = req.get('films')
	    if full_name != None and full_name != "" and image != "" and films != "":
	        k = 0
	        for i in range(len(data["cinemas"])):
	            for j in range(len(data["cinemas"][i]["films"])):
	                for n in data["cinemas"][i]["films"][j]["director"]:
	                    if full_name == n["full_name"]:
	                        k = 1
	                        break
	        if k == 0:
	            a = {
	                "full_name": full_name,
	                "image": image
	            }
	            for i in range(len(data["cinemas"])):
	                for j in data["cinemas"][i]["films"]:
	                    if j["name"] == films:
	                        j["director"].append(a)
	                        break
	            with open('data.json', 'w', encoding='utf-8') as file:
	                file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	            if request.session["role"] == "superuser":
	            	return render(request, "superuser.html")
	            elif request.session["role"] == "moderator":
	            	return render(request, "moderator.html")
	        else:
	            return render(request, 'add_dir.html', {})
	    else:
	        return render(request, 'add_dir.html', {})
	else:
		return login(request)

@csrf_exempt
def addActs(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    full_name = req.get('full_name')
	    image = req.get('image')
	    films = req.get('films')
	    if full_name != None and full_name != "" and image != "" and films != "":
	        k = 0
	        for i in range(len(data["cinemas"])):
	            for j in range(len(data["cinemas"][i]["films"])):
	                for n in data["cinemas"][i]["films"][j]["actors"]:
	                    if full_name == n["full_name"]:
	                        k = 1
	                        break
	        if k == 0:
	            a = {
	                "full_name": full_name,
	                "image": image
	            }
	            for i in range(len(data["cinemas"])):
	                for j in data["cinemas"][i]["films"]:
	                    if j["name"] == films:
	                        j["actors"].append(a)
	                        break
	            with open('data.json', 'w', encoding='utf-8') as file:
	                file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	            if request.session["role"] == "superuser":
	            	return render(request, "superuser.html")
	            elif request.session["role"] == "moderator":
	            	return render(request, "moderator.html")
	        else:
	            return render(request, 'add_acts.html', {})
	    else:
	        return render(request, 'add_acts.html', {})
	else:
		return login(request)
@csrf_exempt
def addSessions(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    ses_id = req.get('ses_id')
	    cost = req.get('cost')
	    cinemaName = req.get('cinemaName')
	    films = req.get('films')
	    begin_end = req.get('begin_end')
	    if ses_id != None and ses_id != "" and cost != "" and cinemaName != "" and films != "" and begin_end != "":
	        k = 0
	        for i in range(len(data["cinemas"])):
	            for j in range(len(data["cinemas"][i]["films"])):
	                for n in data["cinemas"][i]["films"][j]["sessions"]:
	                    if ses_id == n["ses_id"]:
	                        k = 1
	                        break
	        if k == 0:
	            a = {
	                "ses_id": ses_id,
	                "cost": cost,
	                "begin_end": begin_end
	            }
	            for i in range(len(data["cinemas"])):
	                for j in data["cinemas"][i]["films"]:
	                    if j["name"] == films and data['cinemas'][i]['name'] == cinemaName:
	                        j["sessions"].append(a)
	                        break
	            with open('data.json', 'w', encoding='utf-8') as file:
	                file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	            if request.session["role"] == "superuser":
	            	return render(request, "superuser.html")
	            elif request.session["role"] == "moderator":
	            	return render(request, "moderator.html")
	        else:
	            return render(request, 'add_session.html', {})
	    else:
	        return render(request, 'add_session.html', {})
	else:
		return login(request)
@csrf_exempt
def addModer(request):
	if request.session["role"] == "superuser":
	    with open('users.json', 'r', encoding='utf-8') as file:
	        users = json.load(file)
	    req = request.POST
	    login = req.get('login')
	    password = req.get('password')
	    if login != None and id != "" and password != "":
	        k = 0
	        for i in users["data"]:
	            if login == i["login"]:
	                k = 1
	                break
	        if k == 0:
	            a = {
	                "login": login,
	                "password": password,
	                "role": "moderator"
	            }
	            users["data"].append(a)
	            with open('users.json', 'w', encoding='utf-8') as file:
	                file.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))
	            if request.session["role"] == "superuser":
	            	return render(request, "superuser.html")
	        else:
	            return render(request, 'add_moderator.html', {})
	    else:
	        return render(request, 'add_moderator.html', {})
	else:
		return login(request)

@csrf_exempt
def delCinema(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    name = req.get('name')
	    if name != None and name != "":
	        a = {}
	        for i in range(len(data['cinemas'])):
	            if data['cinemas'][i]['name'] == name:
	                data['cinemas'].pop(i)
	                break
	        with open('data.json', 'w', encoding='utf-8') as file:
	            file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	        if request.session["role"] == "superuser":
	           	return render(request, "superuser.html")
	        elif request.session["role"] == "moderator":
	           	return render(request, "moderator.html")
	    else:
	        return render(request, 'del_cinema.html', {})
	else:
		return login(request)
@csrf_exempt
def delFilm(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    name = req.get('name')
	    cinemaName = req.get('cinemaName')
	    if name != None and name != "" and cinemaName != "":
	        a = {}
	        for i in range(len(data['cinemas'])):
	            for j in range(len(data['cinemas'][i]['films'])):
	                if data['cinemas'][i]['films'][j]['name'] == name and data['cinemas'][i]['name'] == cinemaName:
	                    data['cinemas'][i]['films'].pop(j)
	                    break
	        with open('data.json', 'w', encoding='utf-8') as file:
	            file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	        if request.session["role"] == "superuser":
	           	return render(request, "superuser.html")
	        elif request.session["role"] == "moderator":
	           	return render(request, "moderator.html")
	    else:
	        return render(request, 'del_film.html', {})
	else:
		return login(request)

@csrf_exempt
def delDir(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    full_name = req.get('full_name')
	    cinemaName = req.get('cinemaName')
	    filmName = req.get('filmName')
	    if full_name != None and full_name != "" and cinemaName != "" and filmName != "":
	        a = {}
	        for i in range(len(data['cinemas'])):
	            for j in range(len(data['cinemas'][i]['films'])):
	                for n in range(len(data['cinemas'][i]['films'][j]['director'])):
	                    if data['cinemas'][i]['films'][j]['director'][n]['full_name'] == full_name \
	                        and data['cinemas'][i]['name'] == cinemaName and data['cinemas'][i]['films'][j]['name'] == filmName:
	                        data['cinemas'][i]['films'][j]['director'].pop(n)
	                        break
	        with open('data.json', 'w', encoding='utf-8') as file:
	            file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	        if request.session["role"] == "superuser":
	           	return render(request, "superuser.html")
	        elif request.session["role"] == "moderator":
	           	return render(request, "moderator.html")
	    else:
	        return render(request, 'del_dir.html', {})
	else:
		return login(request)

@csrf_exempt
def delActor(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    full_name = req.get('full_name')
	    cinemaName = req.get('cinemaName')
	    filmName = req.get('filmName')
	    if full_name != None and full_name != "" and cinemaName != "" and filmName != "":
	        a = {}
	        for i in range(len(data['cinemas'])):
	            for j in range(len(data['cinemas'][i]['films'])):
	                for n in range(len(data['cinemas'][i]['films'][j]['actors'])):
	                    if data['cinemas'][i]['films'][j]['actors'][n]['full_name'] == full_name \
	                        and data['cinemas'][i]['name'] == cinemaName and data['cinemas'][i]['films'][j]['name'] == filmName:
	                        data['cinemas'][i]['films'][j]['actors'].pop(n)
	                        break
	        with open('data.json', 'w', encoding='utf-8') as file:
	            file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	        if request.session["role"] == "superuser":
	           	return render(request, "superuser.html")
	        elif request.session["role"] == "moderator":
	           	return render(request, "moderator.html")
	    else:
	        return render(request, 'del_act.html', {})
	else:
		return login(request)

@csrf_exempt
def delSession(request):
	if request.session["role"] != None:
	    with open('data.json', 'r', encoding='utf-8') as file:
	        data = json.load(file)
	    req = request.POST
	    ses_id = req.get('ses_id')
	    cinemaName = req.get('cinemaName')
	    filmName = req.get('filmName')
	    if ses_id != None and ses_id != "" and cinemaName != "" and filmName != "":
	        a = {}
	        for i in range(len(data['cinemas'])):
	            for j in range(len(data['cinemas'][i]['films'])):
	                for n in range(len(data['cinemas'][i]['films'][j]['sessions'])):
	                    if data['cinemas'][i]['films'][j]['sessions'][n]['ses_id'] == ses_id \
	                        and data['cinemas'][i]['name'] == cinemaName and data['cinemas'][i]['films'][j]['name'] == filmName:
	                        data['cinemas'][i]['films'][j]['sessions'].pop(n)
	                        break
	        with open('data.json', 'w', encoding='utf-8') as file:
	            file.write(json.dumps(data, ensure_ascii=False, separators=(',', ': '), indent=2))
	        if request.session["role"] == "superuser":
	           	return render(request, "superuser.html")
	        elif request.session["role"] == "moderator":
	           	return render(request, "moderator.html")
	    else:
	        return render(request, 'del_session.html', {})
	else:
		return login(request)
			

@csrf_exempt
def delModer(request):
	if request.session["role"] == "superuser":
	    with open('users.json', 'r', encoding='utf-8') as file:
	        users = json.load(file)
	    req = request.POST
	    login = req.get('login')
	    if login != None and login != "" and login != "superuser":
	        a = {}
	        for i in range(len(users['data'])):
	            if users['data'][i]['login'] == login:
	                users['data'].pop(i)
	                break
	        with open('users.json', 'w', encoding='utf-8') as file:
	            file.write(json.dumps(users, ensure_ascii=False, separators=(',', ': '), indent=2))
	        if request.session["role"] == "superuser":
	           	return render(request, "superuser.html")
	    else:
	        return render(request, 'del_moderator.html', {})
	else:
		return login(request)