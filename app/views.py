from itertools import chain

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, query
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView, TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# from app.forms import CreateBookForm
from app.forms import CreateUserForm
from app.models import Book, Student, PurchasedBook



class dashboardView(TemplateView):
    model = PurchasedBook
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(dashboardView, self).get_context_data(**kwargs)
        context['object_list'] = PurchasedBook.objects.all()
        return context




class BookCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book
    fields = '__all__'

    def get_success_url(self):
        return reverse('book-list')


class BookUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book
    fields = ["name", "full_name_of_author", "status"]
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('book-list')


class BookListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book
    paginate_by = 15  # if pagination is desired



    def get_queryset(self, *args, **kwargs):
        qs = super(BookListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


class BookDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BookDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Book
    success_url = reverse_lazy('book-list')
    template_name_suffix = '_delete'


class StudentCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Student
    fields = '__all__'

    def get_success_url(self):
        return reverse('order-create')


class StudentListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Student
    paginate_by = 15  # if pagination is desired



    def get_queryset(self, *args, **kwargs):
        qs = super(StudentListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs


    def get_success_url(self):
        return reverse('student-list')


class StudentDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Student
    fields = ["full_name", "email", "phone"]
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('student-list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = Student
    success_url = reverse_lazy('student-list')
    template_name_suffix = '_delete'


class OrderCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = PurchasedBook
    fields = '__all__'



    def get_success_url(self):
        return reverse('order-list')


    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['form'].fields['book'].queryset = Book.objects.filter(status=True)
        return context




class OrderListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = PurchasedBook
    paginate_by = 15  # if pagination is desired



    def get_queryset(self, *args, **kwargs):
        qs = super(OrderListView, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-id")
        return qs

    def get_success_url(self):
        return reverse('order-detail')


class OrderDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = PurchasedBook

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = PurchasedBook
    fields = '__all__'
    template_name_suffix = '_update'

    def get_success_url(self):
        return reverse('order-list')



class SearchResultsView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    model = PurchasedBook
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q','')
        if query:
            object_list = self.model.objects.filter(Q(student__full_name__icontains=query)| Q(book__name__icontains=query))

        else:
            object_list = self.model.objects.none()


        return object_list


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form': form}
        return render(request, 'app/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                 messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'app/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')




