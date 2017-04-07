from django.views.generic import TemplateView
from jt_portfolio.about_me.models import Skills


class Home(TemplateView):

    template_name = 'jt_portfolio/home.html'

    def get_contxt_data(self, **kwargs):
        """
        Override default context data for TemplateView
        """

        context = super(TemplateView, self).get_contxt_data(**kwargs)
        skills_queryset = self.Skills.object.all()
        context['skills'] = skills_queryset
        return context
