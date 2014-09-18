from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from widgy_demo.site import site as widgy_site

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'widgy_demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # widgy admin
    url(r'^admin/widgy/', include(widgy_site.urls)),
    # widgy frontend
    url(r'^widgy/', include('widgy.contrib.widgy_mezzanine.urls')),
    url(r'^$', 'mezzanine.pages.views.page', {'slug': '/'}, name='home'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )

    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )

urlpatterns += patterns('',
    url(r'^', include('mezzanine.urls')),
)
