from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),

    path('post/',views.CreatePhotoView.as_view(), name='post'),

    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),

    #カテゴリ一覧ページ
    #photos/<Categorysテーブルのid値>にマッチング
    #<int:category>は辞書{category: id値(int)}としてCategoryViewに渡される
    path('photos/<int:category>',
    views.CategoryView.as_view(),
    name = 'photos_cat'
    ),
]
