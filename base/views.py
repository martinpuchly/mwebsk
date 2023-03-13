from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from pages.models import QuickNew, Post
from datetime import datetime
from django.db.models import Q


def home_view(request):
    return render(request, "home.html", {
        'qicknews': QuickNew.objects.all()[:5],
        'posts': Post.objects.order_by('-created_at').filter(Q(publised__exact=1) | Q(publised_at__lte=datetime.now())).all()[:3]
    })



