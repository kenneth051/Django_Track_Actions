# Third-Party Imports
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from Actions.views import UserView, LoginView, TodoView, HistoryView

router = SimpleRouter()
router.register("users", UserView, "users")
router.register("todo", TodoView, "todo")
router.register("history", HistoryView, "history")

urlpatterns = [path("users/login/", LoginView.as_view())]

urlpatterns += router.urls
