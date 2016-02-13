from django.conf.urls import url
from django.views.generic import DetailView
from . import views, models

urlpatterns = [
    url(r'^error-flash/$', views.ItemErrorFlashView.as_view(), name='item-error-flash'),
    url(r'^remove-flash/$', views.ItemFlashRemoveView.as_view(), name='item-remove-flash'),
    url(r'^reuse-flash/$', views.ItemFlashReuseView.as_view(), name='item-reuse-flash'),
    url(r'^mixin-flash/$', views.ItemFlashMixinView.as_view(), name='item-mixin-flash'),
    # Djangoで用意されているDetailViewをそのまま使うので、views.pyでなくurls.pyに書いておく
    url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(model=models.Item), name='item-detail'),
]
