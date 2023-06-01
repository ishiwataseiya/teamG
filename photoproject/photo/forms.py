from django.forms import ModelForm

from photoproject.photo.admin import PhotoPostAdmin
from .models import photoPost

class PhotoPostForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
         model: モデルのクラス
         fields: フォームで使用するモデルのフィールドを指定
        '''
        model = PhotoPostAdmin
        fields = ['category','title','comment','image1','image2']