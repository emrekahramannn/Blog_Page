from django.shortcuts import render
from django.http import Http404
from .fake_db.pages import FAKE_DB_PAGES

TRENDS_IMG = [
    f"img/{id}.jpeg" for id in range(1,8)
]

def home(request):
    context = dict(
        page_title="Home",
    )
    return render(request, "page/home.html", context)

def page(request, slug):
    result = list(filter(lambda x: (x["url"] == slug), FAKE_DB_PAGES))
    if result:
        context = dict(
                        page_title = result[0]["title"],
                        content = result[0]["content"],
                        TRENDS_IMG = TRENDS_IMG,
                    )
        return render(request, "page/page_temp.html", context)