from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(View):
    template_name = "notebook/base_view.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)