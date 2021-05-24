from django.http import HttpResponse
from django.shortcuts import render,redirect
from movieapp.models import Movie
from movieapp.forms import MovieForm
# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie': movie,
    }
    return render (request,'movieapp/index.html',context)
def details(request,movie_id):
    ob = Movie.objects.get(id=movie_id)
    return render(request,'movieapp/details.html',{'ob':ob})
def add_movie(request):
    if request.method=='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie = Movie(name=name,desc=desc,year=year,img=img)
        movie.save()
    return render(request,'movieapp/add.html')

def update(request,movie_id):
    movie = Movie.objects.get(id=movie_id)

    form = MovieForm(instance=movie)
    if request.method=='POST':
        form = MovieForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'movieapp/update.html',{'form':form})

def delete(request,m_id):
    movie = Movie.objects.get(id=m_id)
    if request.method=='POST':

        movie.delete()
        return redirect('/')
    return render(request,'movieapp/delete.html',{'movie':movie})
