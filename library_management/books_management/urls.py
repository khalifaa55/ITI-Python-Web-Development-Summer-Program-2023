from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('add_book', views.add_book, name="add_book"),
    path('edit_book/<int:isbn>/', views.edit_book, name="edit_book"),
    path('delete_book/<int:isbn>/', views.delete_book, name="delete_book"),
    path('get_all', views.get_all, name="get_all"),
    path('get_book/<int:isbn>/', views.get_book, name="get_book"),
    path('api/get_all_books',views.get_all_books_api, name="get_all_books_api"),
    path('api/add_book',views.add_book_api, name="add_book_api"),
    path('api/edit_book/<int:isbn>/',views.edit_book_api, name="edit_book_api"),
    path('api/delete_book/<int:isbn>/',views.delete_book_api, name="delete_book_api")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)