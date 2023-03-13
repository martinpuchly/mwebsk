from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from pages.models import QuickNew, Post

def home_view(request):
    return render(request, "home.html", {
        'qicknews': QuickNew.objects.all()[:5],
        'posts': Post.objects.order_by('-created_at').all()[:3]
    })



