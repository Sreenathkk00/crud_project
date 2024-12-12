from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import DetailsModel
from .forms import DetailForm
from django.urls import reverse_lazy

# list the details 
class ListView(ListView):
    model = DetailsModel
    queryset = DetailsModel.objects.filter().all().order_by('-pub_date') 
    form_class = DetailForm
    template_name = 'home.html'
    context_object_name = 'Details_List'
    success_url ='/' 
    # add the form
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context
    
# creat the details
class CreateView(CreateView):
    model = DetailsModel
    form_class = DetailForm
    template_name = 'create_new.html'
    success_url = reverse_lazy('home')

# update the details with selected profile (class based view)
class EditView(UpdateView):
    model= DetailsModel
    form_class = DetailForm
    pk_url_kwarg = 'pk'
    template_name = 'edit.html'
    success_url = reverse_lazy('update_view')

# update_view will display the update_success.html page
class UpdateView(ListView):
    model = DetailsModel
    template_name = 'update_success.html'
    context_object_name = 'update_view'

# Delete profile
class DeleteView(DeleteView):
    model = DetailsModel
    pk_url_kwarg ='pk'
    template_name = 'delete_confirm.html'   
    success_url = '/'




