"""
Root URLconf.

Phase 1 scope: wires up the app namespace skeleton, static/media serving in
dev, Django Admin, and the custom 404 handler required to render
core/404.html (see IMPLEMENTATION_PLAN.md §2.2 / §4.2). No business-logic
routes (cart, checkout, orders, payments, auth) are included yet — those land
with their respective apps in later phases.
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    try:
        import debug_toolbar

        urlpatterns += [path("__debug__/", include(debug_toolbar.urls))]
    except ImportError:
        pass

# Custom error handlers — 404 template ported verbatim from the Stitch export
# (code.html "PHINOX // 404 CONVERGENCE FAILED"). See apps/core/views.py.
handler404 = "apps.core.views.custom_404"
