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

            # Loop through the list and append all the items that have the form input substring. 

            suggested_entries = []

            for entry in util.list_entries():
                if form_input in entry:
                    suggested_entries.append(entry)

            return render(request, "encyclopedia/subsearch.html", {
                "suggested_entries": suggested_entries
            })

        else: 

            return render(request, "encyclopedia/errorpage.html")


        
def newpage(request): 
    
    if request.method == "GET": 
        
        return render(request, "encyclopedia/newpage.html")

    elif request.method =="POST":

        form_title = request.POST['entry_title']
        form_entry = request.POST["entry_contents"]

        complete_entry = f"#{form_title}\n{form_entry}"

        util.save_entry(form_title,complete_entry) # Calls the save entry function

        # Convert md to html 

        markdowner = Markdown()

        #md_title= markdowner.convert(f"# {form_title}")
        #md_contents= markdowner.convert(form_entry)
        md_contents= markdowner.convert(complete_entry)

        return render(request, "encyclopedia/entries.html", {
            "md_variable": md_contents })


def edit(request):

    if request.method == "GET":

        # Show a page

        print("you reached the edit page")

        return render(request, "encyclopedia/errorpage.html")
