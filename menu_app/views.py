from django.views.generic import TemplateView
from django.http import Http404
from menu_app.models import MenuItem

class MenuView(TemplateView):
    template_name = "index.html"

    def get(self, request, path=""):
        path = f"/{path}" if path else "/"
        if MenuItem.objects.filter(url=path).exists():
            return super().get(request, path)
        raise Http404("Page not found")
