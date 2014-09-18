from django.conf.urls import patterns
from django.conf.urls import url

from . import views

urlpatterns = patterns('',
    url(r'^types/', view=views.typesview, name='list_types'),
    url(r'^deliverytype/', view=views.DeliverytypeListView.as_view(), name='deliverytypeList'),
    url(r'^add', view=views.deliverytypeAddView, name='deliverytypeAdd'),
    url(
        regex=r'^(?P<code>[\w.@+-]+)/$',
        view=views.DeliverytypeUpdateView.as_view(),
        name='deliverytypeDetail'
    ),
)
