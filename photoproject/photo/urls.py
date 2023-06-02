from django.urls import path
from django.views import View
from . import views

app_name = 'photo'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),

    path('post/',views.CreatePhotoview.as_view(), name='post'),
    path('post_done/',
          views.PostSuccessView.as_view(),
          name='post_done'),
    #カテゴリ一覧ページ
    #photos/<Categorysテーブルのid値>にマッチング
    #<int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
         View.CategoryView.as_view(),
         name = 'photos_cat'
         ),
]
    

