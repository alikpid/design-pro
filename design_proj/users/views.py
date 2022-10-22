from django.shortcuts import render
from .forms import RegisterUserForm


def register(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterUserForm()
    return render(request, 'register.html', {'user_form': user_form})

