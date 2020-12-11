from django.conf.urls import url
from django.urls import path, include

from app import views
from app.views import BookCreateView, BookUpdateView, BookListView, BookDetailView, BookDeleteView, StudentCreateView, \
    StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView, OrderCreateView, OrderListView, \
    OrderDetailView, OrderUpdateView, SearchResultsView, dashboardView

urlpatterns = [
    path('register', views.registerPage, name='register'),
    path('', dashboardView.as_view(), name='index'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('book/create/', BookCreateView.as_view(), name='book-create'),
    path('book/list', BookListView.as_view(), name='book-list'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/detail', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    path('student/create', StudentCreateView.as_view(), name='student-create'),
    path('student/list', StudentListView.as_view(), name='student-list'),
    path('student/<int:pk>/detail', StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/update', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('order/create/', OrderCreateView.as_view(), name='order-create'),
    path('order/list', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/detail', OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order-update'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]