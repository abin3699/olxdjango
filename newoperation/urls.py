from django.urls import path
from newoperation.views import SignUpView,SigninView,IndexView,\
    OlxCreateView,OlxNewListView,OlxNewDetailView,\
        OlxNewUpdateView,remove_vehicle,signout


urlpatterns=[
    path("reg/",SignUpView.as_view(),name="reg-olx"),
    path("sign",SigninView.as_view(),name="signin-olx"),
    path("index",IndexView.as_view(),name="index"),
    path("add/",OlxCreateView.as_view(),name="add-olx"),
    path("all/",OlxNewListView.as_view(),name="list-olx"),
    path("<int:pk>",OlxNewDetailView.as_view(),name="view-olx"),
    path("<int:pk>/change",OlxNewUpdateView.as_view(),name="change-olx"),
    path("<int:pk>/remove",remove_vehicle,name="remove-olx"),
    path("signout",signout,name="signout")

]