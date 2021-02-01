from django.shortcuts import render

def index(request):
	return render(request,"Guest/guest.html")

def resume(request):
	return render(request,'Guest/resume.html')

def blog(request):
	return render(request,'Guest/blog.html')

def gallery(request):
	return render(request,'Guest/gallery.html')
