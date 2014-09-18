from django.shortcuts import render, redirect

from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.core.urlresolvers import reverse

from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin

from .forms import DeliverytypeForm

from .models import (Deliveryresulttype, Deliverytype)


class DeliverytypeListView(LoginRequiredMixin, ListView):
    model = Deliverytype
    #return render(request, "generaldata/deliverytype_list.html",
    #{"object_list": Deliverytype.objects.all()})
    
def typesview(request):
    return render(request, "generaldata/alltypes.html")
    
class DeliverytypeUpdateView(LoginRequiredMixin, UpdateView):

    form_class = DeliverytypeForm
    
    model = Deliverytype
    
    def get_success_url(self):
        return reverse('generaldata:deliverytypeDetail',
                        kwargs={code: self.request.code})
    
    def get_object(self):
        return Deliverytype.objects.get(dlt_id_a=self.request.code)
    
def deliverytypeAddView(request):
    if request.method == "POST":
        code = request.POST.get("code")
        description = request.POST.get("description")
        if code and description:
            d = Deliverytype()
            d.dlt_id_a = code
            d.dlt_desc = description
            d.save()
    return redirect(reverse('generaldata:deliverytypeList'))
