from django.shortcuts import render, redirect
from .models import Book
from .forms import CreateBookForm
from django.contrib import messages

def index(request):
    return render(request, 'trial_app/index.html')

def home(request):
    book_list = {
        'books':Book.objects.all()
    }
    return render(request, 'trial_app/home.html', book_list)
    
def subpage(request):
    return HttpResponse('Hello World')

def addBooks(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():

            t = form.cleaned_data['title']
            a = form.cleaned_data['author']
            s = form.cleaned_data['summary']
            ye = form.cleaned_data['your_email']

            newBook = Book(title = t, author = a, summary = s, your_email=ye)
            newBook.save()

            title = form.cleaned_data.get('title')

            messages.success(request, f'{title} has been added!')           
            return redirect('list')
        else:
            messages.error(request, 'Submission Failed. Try again.')
    else:
        form = CreateBookForm()
    return render(request, 'trial_app/addBookForm.html', {'form': form})

