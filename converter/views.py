from django.shortcuts import render

def index(request):
	word = 'hello!'
	context = {'word': word}
	return render(request, 'converter/index.html', context)
