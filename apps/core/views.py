"""
Phase 1: only the custom 404 handler lives here. This renders the Stitch
"PHINOX // 404 CONVERGENCE FAILED" screen verbatim (see
templates/core/404.html and IMPLEMENTATION_PLAN.md §2.2).

Django's error handlers receive a minimal context (no guarantee that normal
context processors like cart/session state have run cleanly, since a 404 can
happen mid-failure) so this view deliberately renders with base_standard.html
only, no dependency on catalog/cart context.
"""
from django.http import HttpResponseNotFound
from django.template import loader


def custom_404(request, exception=None):
    template = loader.get_template("core/404.html")
    return HttpResponseNotFound(template.render({}, request))
