from django.views.generic import TemplateView

from core.auth_mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'
