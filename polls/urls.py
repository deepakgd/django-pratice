from django.urls import path
from . import views

# adding app_name becuase someother app may have same name like index or details or results or vote
app_name = 'polls'

urlpatterns = [
    # /polls
    path('', views.index, name='index'),
    # /polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/v2/5
    path('v2/<str:text>/', views.detailv2, name='detailv2'),
    # polls/5/results
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote')
]