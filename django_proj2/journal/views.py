from django.shortcuts import render
from journal.models import Journalist, Post
from django.http import HttpRequest


def index(request: HttpRequest):
    qs = Journalist.objects.all()  # QuerySet : 데이터베이스로의 쿼리를 생성/실행
    return render(
        request,
        "journal/post_list.html",
        {
            "post_list": qs,
        },
    )


def post_detail(request: HttpRequest, pk: int):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        "journal/post_detail.html",
        {
            "post": post,
        },
    )
