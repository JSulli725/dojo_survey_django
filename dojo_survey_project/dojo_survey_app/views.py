from django.shortcuts import render, redirect

def user_form(request):
    return render(request, "form.html")

def user_form_post(request):
    request.session["user_name"] = request.POST['user_name']
    request.session["dojo_location"] = request.POST["dojo_location"]
    request.session["favorite_language"] = request.POST["favorite_language"]
    request.session["comments"] = request.POST["comments"]
    return redirect("/result")

def survey_result(request):
    # context = {
    #     'user_name': request.session['user_name'],
    #     'dojo_location': request.session['dojo_location'],
    #     'favorite_language': request.session['favorite_language'],
    #     'comments': request.session['comments']
    # }
    return render(request, 'results.html')

def homeButton(request):
    return redirect("/")