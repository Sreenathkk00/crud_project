from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import DetailsModel
from .forms import DetailForm
import os
from django.urls import reverse_lazy
# Create your views here.

# list the details 
class DetailListview(ListView):
    model = DetailsModel
    queryset = DetailsModel.objects.filter().all().order_by('-pub_date') 
        
    template_name = 'index.html'
    context_object_name = 'Details_List'
    

# creat the details
class FormView(CreateView):
    model = DetailsModel
    form_class = DetailForm
    template_name = 'form.html'
    success_url ='/' 


# update_view will display the update.html page
class Update_View(ListView):
    model = DetailsModel
    template_name = 'update.html'
    context_object_name = 'update_view'

# update the details with selected profile (class based view)
class EditView(UpdateView):
    model= DetailsModel
    form_class = DetailForm
    pk_url_kwarg = 'pk'
    template_name = 'edit.html'
    success_url = reverse_lazy('update_view')  # Adjust the URL name
                                              # reverse_lazy: This is a function provided by Django that reverses a URL pattern based on its name.

    def form_valid(self, form):
        # Get the current instance
        self.object = self.get_object()

        # Handle image update
        if form.has_changed():
            # Handle image update
            new_image = form.cleaned_data.get('images')

            # Check if a new image is provided
            if new_image:
                # Delete the old image if it exists
                if self.object.images and self.object.images.path:
                    old_image_path = self.object.images.path
                    if os.path.exists(old_image_path):
                        os.remove(old_image_path)

                # Update the images field of the DetailsModel instance with the new image
                self.object.images = new_image

        # Save the updated instance
        self.object.save()
        
        return super().form_valid(form)
    
# update_view will display the update.html page
class Update_View(ListView):
    model = DetailsModel
    template_name = 'update.html'
    context_object_name = 'update_view'

# Delete profile
class Delete_View(DeleteView):
    model = DetailsModel
    pk_url_kwarg ='pk'
    template_name = 'delete.html'   
    success_url = '/'




