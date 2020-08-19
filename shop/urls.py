from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns =[
    path('', product_in_category, name='product_all'), # 카테고리 선택없이 전체 제품을 노출하는 경우
    path('<slug:category_slug>/', product_in_category, name='product_in_category'), # 카테고리 선택이 있는 경우
    path('<int:id>/<product_slug>', product_detail, name='product_detail'), # 제품 상세
]