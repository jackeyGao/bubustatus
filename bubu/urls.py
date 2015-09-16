from django.conf.urls import include, url
from django.contrib import admin

from bubustatus.views import labels
from bubustatus.views import step
from bubustatus.views import StepListView
from bubustatus import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'label', api.LabelViewSet)
router.register(r'step', api.StepViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'bubu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', StepListView.as_view()),
    url(r'^labels$', labels),
    url(r'^step/(?P<label>.*)/(?P<name>.*)$', step),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls))
]
