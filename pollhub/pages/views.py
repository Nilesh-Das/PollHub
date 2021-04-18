from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
def index(request):
	# return HttpResponse("Welcome to poll's index!")
	return render(request, 'pages/index.html')