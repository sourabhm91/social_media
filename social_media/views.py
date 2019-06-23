from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

from . import forms as loginform


class SignInView(generic.FormView):
    template_name = "index.html"
    form_class = loginform.SignInForm
    success_url = reverse_lazy("twitter:credentials")

    # print "success_url==",success_url

    def form_valid(self, form):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
        else:
            raise forms.ValidationError(['user name or password is incorrect'])
        return super(SignInView, self).form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SignUpView(generic.FormView):
    template_name = "signup.html"
    form_class = loginform.SignUpForm

    # success_url = reverse("")

    def form_valid(self, forms):
        username = self.request.POST['username']
        password = self.request.POST['password']
        email = self.request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        # return super(SignUpView,self).form_valid(form)
        return HttpResponseRedirect("/")

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class LogOutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
