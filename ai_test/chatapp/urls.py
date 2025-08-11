from django.urls import path
from .views import RegisterView,LoginView,ChatView,TokenBalanceView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',LoginView.as_view()),
    path('chat/',ChatView.as_view()),
    path('tokens/',TokenBalanceView.as_view()),
]


