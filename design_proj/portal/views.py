from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Request
from django.views import generic


def index(request):
    num_request = Request.objects.filter(status__exact='c')[:4]
    num_status = Request.objects.filter(status__exact='a').count()
    return render(
        request,
        'index.html',
        context={'num_order': num_request, 'num_status': num_status},
    )


def detail(request, pk):
    req = get_object_or_404(Request, pk=pk)
    context = {'req': req}
    return render(request, 'detail.html', context)


class RequestDetailView(generic.DetailView):
    model = Request


class BBLoginView(LoginView):
    template_name = 'login.html'


@login_required
def profile(request):
    reqs = Request.objects.filter(author=request.user.pk)
    context = {'reqs': reqs}
    return render(request, 'profile.html', context)


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'

# class OrderCreate(CreateView):
#     model = Request
#     fields = ['name', 'summary', 'category', 'img']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         form.instance.day_add = datetime.date.today()
#         return super().form_valid(form)
