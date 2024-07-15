from django.shortcuts import render
from django.http import Http404
from .fake_db.blogs import FAKE_DB_BLOGS


def blog_list(request):
    context = dict(
        FAKE_DB_BLOGS = FAKE_DB_BLOGS,
        page_title = "Blogs",
    )
    return render(request, "blog/blogs.html", context)

def blog_detail(request, id):
    result = list(filter(lambda x: (x["id"] == id), FAKE_DB_BLOGS))
    if result:
        context = dict(
            page_title = result[0]["title"],
            FAKE_DB_BLOGS = FAKE_DB_BLOGS,
            blog_title = result[0]["title"],
            id = result[0]["id"],
            blog_content = result[0]["content"],
        )
        return render(request, "blog/blog_detail.html", context)