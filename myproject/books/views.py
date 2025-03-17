from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify
from .models import Book
from .forms import BookForm

def books_list(request):
    books = Book.objects.all().order_by('-date')
    return render(request, 'books/books_list.html', {'books': books})

def book_page(request, slug):
    book = get_object_or_404(Book, slug=slug)
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

def books_list_filtered(request):
    title = request.GET.get('title', '')
    if title:
        books = Book.objects.filter(title__icontains=title).order_by('-date')
    else:
        books = Book.objects.all().order_by('-date')
    return render(request, 'books/books_list_filtered.html', {'books': books, 'title': title})