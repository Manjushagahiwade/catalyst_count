from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator
from account.forms import CustomUserCreationForm
from account.models import CustomUser
from django.urls import reverse_lazy

success_url = reverse_lazy('user-list')


class UserCreateView(generic.CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user/user_create.html'  # Define the template for the form
    success_url = reverse_lazy('user-list')


class UserListView(generic.ListView):
    model = CustomUser
    template_name = "user/user_list.html"
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self):
        return CustomUser.objects.all()




class UserDeleteView(generic.DeleteView):
    model = CustomUser

    # Specify the URL name to redirect to upon successful deletion
    success_url = reverse_lazy('user-list')

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        print('id')
        user = CustomUser.objects.filter(id=id).delete()
        print(user)

        return HttpResponseRedirect(success_url)


# Create your views here.
class LoginGenericView(generic.View):
    def post(self, request, *args, **kwargs):
        pass
