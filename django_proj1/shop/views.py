from django.shortcuts import render
from shop.models import Item, Review
from django.http import HttpRequest


def index(request: HttpRequest):
    qs = Item.objects.all()  # QuerySet : 데이터베이스로의 쿼리를 생성/실행
    return render(
        request,
        "shop/item_list.html",
        {
            "item_list": qs,
        },
    )


def item_detail(request: HttpRequest, pk: int):
    item = Item.objects.get(pk=pk)
    return render(
        request,
        "shop/item_detail.html",
        {
            "item": item,
        },
    )
