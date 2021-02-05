from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm


def signup(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            print("User Name =====", username)
            password = form.cleaned_data.get("password1")
            print("Password 1 =====", password)

            user = authenticate(username=username, password=password,)
            print("User ====== ", user)

            print("Result = ", form.cleaned_data)

            login(request, user)
            return redirect("pybo:index")

            #  이 코드는 존재하지 않는 암호를 얻으려고 했기 때문에 인증에 실패하게 되므로
            # 사용자가 없음으로 반환함
            # password2 = form.cleaned_data.get("password2")
            # print("Password 2 =====", password2)
            # https://stackoverflow.com/questions/46284664/django-anonymoususer-object-has-no-attribute-meta

    else:
        form = CreateUserForm()
    return render(request, "common/signup.html", {"form": form})

