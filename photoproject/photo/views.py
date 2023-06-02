from django.shortcuts import render
#django.views.genericからTemplateView、ListViewをインポート
from django.views.generic import TemplateView,ListView

from django.views.generic import TemplateView
#django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
#django.urlsからreverse_lazyをインポート
from django.urls import reverse, reverse_lazy

from photoproject.photo.admin import PhotoPostAdmin 
#fromsモジュールからPhotoPostFormをインポート
from .forms import PhotoPostForm
#method_decoratorをインポート
from django.utils.decorators import method_decorator
#login_requiredをインポート
from django.contrib.auth.decorators import login_required
#modelsモジュールからモデルPhotoPostをインポート
from .models import photoPost

class IndexView(ListView):

 class IndexView(TemplateView):
    template_name ='index.html'
    #モデルBlogPostのオブジェクトにorder_by()を適用して
    #投稿日時の降順で並べ替える
    queryset = PhotoPostAdmin.objacts.order_by('-posted_at')
    #1ページに表示するレコードの件数
    paginate_by = 9

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
