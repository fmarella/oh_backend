# -*- coding: utf-8 -*-
from django import forms


from .models import Deliverytype

class DeliverytypeForm(forms.ModelForm):

    class Meta:
        model = Deliverytype
        
        fields = ('dlt_id_a', 'dlt_desc')
    
    
