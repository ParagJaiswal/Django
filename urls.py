from django.urls import path
from. import views

urlpatterns=[
	path('',views.index,name='index'),
	path('next',views.resume, name='resume'),
	path('blog',views.blog, name='blog'),
	path('gallery',views.gallery,name='gallery')
]