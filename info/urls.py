from django.urls import include, path
from .views import infoCreate, infoList, infoDetail, infoUpdate,infoDelete

urlpatterns = [
    path('create/', infoCreate.as_view()),
    path('', infoList.as_view()),
    path('<int:pk>/', infoDetail.as_view()),
    path('update/<int:pk>', infoUpdate.as_view()),
    path('delete/<int:pk>', infoDelete.as_view()),
]