from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import BookForm
from .models import Book, publishing_house
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer, publishing_houseSerializer


# Create your views here.
def index(request):
    header = "Hi, from library"
    context = {
        "header": header
    }
    return render(request, 'books_management/index.html', context)

def add_book(request):
    book_form = BookForm()
    try: 
        if request.method == "POST":
            book_form = BookForm(request.POST, request.FILES)
            if book_form.is_valid():
                book_form.save()
                return HttpResponse('/')
    except Exception as e:
        print("exception in add_book ", e)
    return render(request, 'books_management/add_book.html',{'book_form':book_form})


def edit_book(request, isbn):
    try:
        book = get_object_or_404(Book, isbn=isbn)
        if request.method == "POST":
            book_form = BookForm(request.POST, instance=book)
            if book_form.is_valid():
                book_form.save()
                return HttpResponse('/')
        else:
            # Initialize the form with the existing book instance data
            book_form = BookForm(instance=book)
    except Exception as e:
        print("exception in edit_book ", e)
        book_form = BookForm()  # Initialize an empty form

    return render(request, 'books_management/add_book.html', {'book_form': book_form})


def delete_book(request, isbn):
    try:
        obj = Book.objects.get(isbn = isbn)
        obj.delete()
    except Exception as e:
        print("exception in delete_book ", e)
    return HttpResponse('/')

from django.shortcuts import render, HttpResponse
from .models import Book

def get_all(request):
    try:
        all_books = Book.objects.all()
        context = {'books': all_books}
    except Exception as e:
        print("exception at get_all ", e)
        context = {'books': []}  # Provide an empty list of books in case of exception

    return render(request, 'books_management/get_all.html', context)

def get_book(request, isbn):
    try:
        book = get_object_or_404(Book, isbn=isbn)
        context = {'book': book}
    except Exception as e:
        print("exception at get_book ", e)
        context = {'book': None}  # Provide an empty list of books in case of exception

    return render(request, 'books_management/get_book.html', context)

#-------------------------------------------Rest Framework Api-----------------------------------------------

@api_view(['GET'])
def get_all_books_api(request):
    ret_obj = {}
    serialized_book = {}
    http_status = status.HTTP_200_OK
    try:
        all_books = Book.objects.all()
        if all_books:
            serialized_books = BookSerializer(all_books, many=True)
            ret_obj['success'] = True
            ret_obj['data'] = serialized_books.data
            ret_obj['error'] = None
    except Exception as e:
        print("error in get_all_books_api ", e)
        ret_obj['success'] = False
        ret_obj['data'] = None
        ret_obj['error'] = f'{e}'
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=ret_obj, status=http_status)

@api_view(['POST'])
def add_book_api(request):
    ret_obj = {}
    serialized_book = {}
    http_status = status.HTTP_200_OK
    try:
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
        ret_obj['success'] = True
        ret_obj['data'] = book.data
        ret_obj['error'] = None
    except Exception as e:
        print("error in add_book_api ", e)
        ret_obj['success'] = False
        ret_obj['data'] = None
        ret_obj['error'] = f'{e}'
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=ret_obj, status=http_status)

@api_view(['PUT'])
def edit_book_api(request, isbn):
    ret_obj = {}
    http_status = status.HTTP_200_OK
    
    try:
        book = get_object_or_404(Book, isbn=isbn)
        book = BookSerializer(instance=book, data=request.data)
        if book.is_valid():
            book.save()
            ret_obj['success'] = True
            ret_obj['data'] = book.data
            ret_obj['error'] = None
    except Exception as e:
        print("error in edit_book_api ", e)
        ret_obj['success'] = False
        ret_obj['data'] = None
        ret_obj['error'] = f'{e}'
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=ret_obj, status=http_status)

@api_view(['DELETE'])
def delete_book_api(request, isbn):
    ret_obj = {}
    http_status = status.HTTP_200_OK
    
    try:
        book = get_object_or_404(Book, isbn=isbn)
        book.delete()
        book.save()
        ret_obj['success'] = True
        ret_obj['data'] = {}
        ret_obj['error'] = None
    except Exception as e:
        print("error in edit_book_api ", e)
        ret_obj['success'] = False
        ret_obj['data'] = None
        ret_obj['error'] = f'{e}'
        http_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    return Response(data=ret_obj, status=http_status)