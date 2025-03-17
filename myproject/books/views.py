from django.shortcuts import render, redirect
from django.utils.text import slugify
from .models import Book
from .forms import BookForm
# Create your views here.

def books_list(request):
    books = Book.objects.all().order_by('-date')
    return render(request, 'books/books_list.html', {'books': books})


def book_page(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_page.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.slug = slugify(book.title)
            book.save()
            return redirect('books:list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})
