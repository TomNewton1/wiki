from django.shortcuts import render
from django.shortcuts import redirect
import random

import re

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

        if form_title in util.list_entries():

            return render(request, "encyclopedia/errorpage_existing_entry.html")

        else: 

            complete_entry = f"# {form_title}\n\n{form_entry}"

            util.save_entry(form_title,complete_entry) # Calls the save entry function

            return redirect ("entries", title=form_title)



def edit(request):

    if request.method == "GET":

        # Pass all required info into the form input fields and allow user to edit form. 

        entry_contents = request.GET['hidden_entry']

        print("The entry contents are:", entry_contents)

        entry_contents_parsed = re.findall(r'<h1>(.+?)</h1>', entry_contents)

        entry_contents_parsed_filtered = entry_contents_parsed[0].replace('+',' ')

        title = entry_contents_parsed_filtered

        contents = util.get_entry(entry_contents_parsed_filtered)

        # Edit the contents to remove the title from the main contents 

        print("The title I want to replace is: ", title)

        updated_contents = contents.replace((f"# {title}" or f"#{title})") ,'')


        return render(request, "encyclopedia/editpage.html", {
            "title": title, "contents": updated_contents })
    
    elif request.method == "POST":

        # If the user is posting info then we need to update the form. 

        form_title = request.POST['entry_title']
        form_entry = request.POST["entry_contents"]

        complete_entry = f"# {form_title}{form_entry}"

        util.save_entry(form_title,complete_entry) # Calls the save entry function

        return redirect ("entries", title=form_title)


def random_page(request):

    form_title = random.choice(util.list_entries())

    print("The random entry is:", form_title)

    return redirect ("entries", title=form_title)
