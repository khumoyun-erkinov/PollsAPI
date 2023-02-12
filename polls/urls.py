from django.urls import path, include
from .views import *
from .apiviews import *
from rest_framework.routers import DefaultRouter
from .apiviews import PollVewSet,UserCreate


# APIVIEW
# urlpatterns = [
#     path("polls/", polls_list, name="polls_list"),
#     path("polls/<int:pk>/", polls_detail, name="polls_detail")
# ]


# generic and APIVIEWW
# urlpatterns = [
#     # path("polls/", PollList.as_view(), name="polls_list"),
#     # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
#     # path("choices/", ChoiceList.as_view(), name='choice_list'),
#     # path("vote/", CreateVote.as_view(), name='create_vote'),
#     # path("polls/<int:pk>/choices", ChoiceList.as_view(), name='choice_list'),
#     # path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name='created_vote'),
#     path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
#
# ]

# ViewSet
router = DefaultRouter()
router.register('polls', PollVewSet, basename='polls')

urlpatterns = [
    path('users/', UserCreate.as_view(), name="user_create"),

]
urlpatterns += router.urls
