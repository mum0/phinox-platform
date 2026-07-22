"""
Phase 1: bare-minimum views so the URL/template scaffolding is provable
end-to-end. `contact` renders the ported Stitch page verbatim (GET only —
form POST handling + ContactMessage model are out of scope until a later
phase per IMPLEMENTATION_PLAN.md §2.3). `home` is a placeholder — no Home
screen has been supplied by the Stitch project yet (see plan §5, open
question #4), so it renders an empty shell on base_standard.html rather than
inventing page content.
"""
from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def contact(request):
    return render(request, "pages/contact.html")
