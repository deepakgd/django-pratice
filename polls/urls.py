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
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # method 2 - same above - using generic view - note prefix with gv
    path('gv', views.IndexView.as_view(), name='gvindex'),
    path('gv/<int:pk>/', views.DetailView.as_view(), name='gvdetail'),
    path('gv/<int:pk>/results/', views.ResultsView.as_view(), name='gvresults'),
]