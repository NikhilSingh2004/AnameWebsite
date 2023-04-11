from django.contrib import admin
from django.urls import path 
from home import views
from django.conf import settings
from django.conf.urls.static import static 
from django.views.static import serve 
from django.conf.urls import url


urlpatterns = [
    path("/",views.home,name="Home"),
    path("about/",views.about,name="about"),
    path("new_genart/",views.new_genart,name="new_genart"),
    path("new_candels/",views.new_candels,name="new_candels"),
    path("contact/",views.contact,name="contact"),
    path("candleDetails/<id>",views.candleDetails,name="candleDetails"),
    path("resinArtDetails/<id>",views.resinArtDetails,name="resinArtDetails"),
    path("payment/",views.payment,name="payment"),
    path("billingaddress/<id>",views.billingAddress,name="billingaddress"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

] 

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)