from django.shortcuts import render

from django.views.generic import TemplateView
#django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
#django.urlsからreverse_lazyをインポート
from django.urls import reverse, reverse_lazy 
#fromsモジュールからPhotoPostFormをインポート
from .forms import PhotoPostForm
#method_decoratorをインポート
from django.utils.decorators import method_decorator
#login_requiredをインポート
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name ='index.html'

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):

 class PostSuccessView(TemplateView):
    template_name = 'post_success.html'

    from_class = PhotoPostForm
    template_name = "post_photo.html"
    success_url = reverse_lazy('photo:post_done')

    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)

# Create your views here.
