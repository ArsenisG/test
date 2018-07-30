from django.urls import path 
from . import views


urlpatterns=[
	path('', views.question_values, name='questionvalues'),
	path('process', views.create_survey),
	path('result', views.create_survey),
	path('final',views.python_code),
	path('download',views.generate_view),
]
