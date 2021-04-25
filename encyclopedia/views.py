from django.shortcuts import render
from django.shortcuts import redirect
import re

from . import util
from markdown2 import Markdown


# Set regex to search 

r = re.compile('.*search.*')

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



def get_search(request):

    if request.method == "POST":

        form_input = request.POST["q"]

         # Check if form input is within entries 

        if form_input in util.list_entries():

            entry_name = util.get_entry(form_input)
            
            markdowner = Markdown()

            md_variable = markdowner.convert(entry_name)

            return render(request, "encyclopedia/entries.html", {
                "md_variable": md_variable})


        elif any(form_input in entry for entry in util.list_entries()):

            # Check substring to see if it is list entries. If it is then produce a list of all possible entries. 

            entry_name = [entry for entry in util.list_entries() if form_input in entry]

            print("Did you mean: ", entry_name)


            print(f"Your input {form_input} was in the entries list!")


            return render(request, "encyclopedia/subsearch.html", {
                "entry_name": entry_name, "entries": util.list_entries()
            })


        else: 

            return render(request, "encyclopedia/errorpage.html")


    else: 

        print("form not posting")
        
    