from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, DetailView
from .models import Topic
from django.conf import settings
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from user.models import CustomUser
from .scripts import crawler
from django.contrib.auth.mixins import UserPassesTestMixin


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.username == self.kwargs['username'] or user.is_superuser

class TopView(TemplateView):
    template_name = "top.html"

class HomeView(OnlyYouMixin, DetailView):
    template_name = "home.html"
    slug_field = "username"
    slug_url_kwarg = "username"
    model = CustomUser

    def get_object(self):
        object = get_object_or_404(CustomUser, username=self.kwargs.get("username"))
        if self.request.user.username == object.username:
            return object
        else:
            return HttpResponseRedirect(reverse('picker:top'))

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["topics_list"] = Topic.objects.filter(user=user)
        return context
    
