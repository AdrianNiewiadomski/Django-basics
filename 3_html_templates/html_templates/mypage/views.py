from django.shortcuts import render


def display_index(request):
    # To display an HTML template instead of a string, use a method called render.
    # Some of the method's arguments are a request, template name, and an optional argument called context.
    # The context is a dictionary with arguments.
    return render(request, 'mypage/template.html', context={'arg': 'index'})


def display_about(request):
    return render(request, 'mypage/template.html', {'arg': 'about'})


def display_contact(request):
    return render(request, 'mypage/template.html', {'arg': 'contact'})
