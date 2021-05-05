from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from merchantUI.forms import *
from api.models import Item

def merchantLandingPage(request):
    if request.method == 'GET':
        # If user is already logged in, redirect to item upload page.
        if request.user.is_authenticated:
            return redirect(reverse('itemUpload'))

        return render(request, 'merchantUI/loginOrRegister.html',
                      {'loginForm': LoginForm(), 'registerForm': RegisterForm()})


def registerMerchantAction(request):
    if request.method == 'GET':
        return render(request, 'merchantUI/loginOrRegister.html',
                      {'loginForm': LoginForm(), 'registerForm': RegisterForm()})

    if request.method == 'POST':
        # Received register form. Validate and create new user.
        registerForm = RegisterForm(request.POST)
        if not registerForm.is_valid():
            return render(request, 'merchantUI/loginOrRegister.html',
                          {'loginForm': LoginForm(), 'registerForm': registerForm})

        print("Valid register POST request received: ", request.POST)
        newUser = User.objects.create_user(
            username=registerForm.cleaned_data['username'],
            password=registerForm.cleaned_data['password'])
        newUser.save()
        print("New user created:", newUser)

        # After registering users, automatically log them in.
        authUser = authenticate(username=registerForm.cleaned_data['username'],
                                password=registerForm.cleaned_data['password'])
        # authUser should never be None since we're using the correct username/password
        print("Logging new user in automatically...", newUser.username)
        login(request, authUser)

        # After logging user in, redirect them to the item upload portal.
        return redirect(reverse('itemUpload'))


def loginMerchantAction(request):
    if request.method == 'GET':
        return render(request, 'merchantUI/loginOrRegister.html',
                      {'loginForm': LoginForm(), 'registerForm': RegisterForm()})

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'merchantUI/loginOrRegister.html',
                          {'loginForm': form, 'registerForm': RegisterForm()})

        user = authenticate(username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        print("User logged in:", form.cleaned_data['username'])
        login(request, user)
        return redirect(reverse('itemUpload'))

@login_required
def itemUploadPage(request):
    if request.method == 'GET':
        return render(request, 'merchantUI/itemUpload.html', {'form': ItemUploadForm()})

    form = ItemUploadForm(request.POST)
    if not form.is_valid():
        return render(request, 'merchantUI/itemUpload.html', {'form': form})

    newItem = Item(
        seller=request.user,
        name=form.cleaned_data['name'],
        nominal_price=form.cleaned_data['nominalPrice'],
        lowest_price=form.cleaned_data['lowestPrice'],
        item_url=form.cleaned_data['itemUrl']
    )

    # TODO(@carlos): The line below fails with the message "table api_item has no column named seller_id", any ideas why?
    newItem.save()
    return redirect(reverse('itemUpload'))

@login_required
def logoutAction(request):
    print("Logging user out...")
    logout(request)
    return render(request, 'merchantUI/loginOrRegister.html',
                  {'loginForm': LoginForm(), 'registerForm': RegisterForm()})
