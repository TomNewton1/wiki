from django.shortcuts import render

from . import util
from markdown2 import Markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request):
    markdowner = Markdown()

    f = open('entries/CSS.md', 'r')

    md_variable = markdowner.convert(f.read())

    print(md_variable)


    return render(request, "encyclopedia/entries.html", {
		"md_variable": md_variable})