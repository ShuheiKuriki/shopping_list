from django.urls import path
from . import views

app_name = 'shoppinglist'

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:sort>', views.ShoppingListView.as_view(), name='list'),
    path('sort', views.sort, name='sort'),
    path('buy/<int:pk>', views.buy, name='buy'),
    path('must_buy/<int:pk>', views.must_buy, name='must_buy'),
    path('create', views.ShoppingCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.ShoppingUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.ShoppingDeleteView.as_view(), name='delete'),
]