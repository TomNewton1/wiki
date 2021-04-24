from django.shortcuts import render

from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def md_to_html(request, title):

    if util.get_entry(title) is None: 

        return render(request, "encyclopedia/errorpage.html")

    else: 

        entry_name = util.get_entry(title) 

        markdowner = Markdown()

        md_variable = markdowner.convert(entry_name)

        return render(request, "encyclopedia/entries.html", {
            "md_variable": md_variable})

