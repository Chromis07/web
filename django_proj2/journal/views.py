from django.shortcuts import render
from journal.models import Journalist
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
