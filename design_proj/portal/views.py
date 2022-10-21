from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def index(request):
    return render(request, 'index.html')


def other_page(request, page):
    try:
        template = get_template('portal/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


class BBLoginView(LoginView):
    template_name = 'portal/login.html'


@login_required
def profile(request):
    return render(request, 'portal/profile.html')
