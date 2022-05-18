from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from accounts.forms import UserCreateForm


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html', {
            'next': request.GET.get('next')
        })

    def post(self, request, *args, **kwargs):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            next = request.GET.get('next')
            login(request, user)
            if next:
                return redirect(next)
            return redirect('main')
        else:
            context['has_error'] = True
        return render(request, 'accounts/login.html', context=context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class RegisterView(View):
    template_name = 'accounts/register.html'

    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, self.template_name, context={'form': form})

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, self.template_name, context={'form': form})


class ProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'accounts/profile.html'
    context_object_name = 'user_obj'
    extra_context = {
        'title': 'Личный кабинет'
    }
