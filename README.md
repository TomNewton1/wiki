# Wiki
### Web application with Wikipedia like functionality.


![](encyclopedia/static/encyclopedia/wiki_video.gif)


## Description

Wiki is a wikipedia like web application built in Django. The site allows users to view, create and edit entries. The site is made up of the following features: 

**Entry Page:** Each entry is stored locally in a Markdown file. 

**Index Page:** Show a list of all entries in the encyclopdia. 

**Search:** Allows users to search for entries in the encyclopedia. This can be done using the url or search input field, redirecting users to the entry. If the search query is a substring of any entry, a list will be created of all possible entries. 

**New Page:**: Allows users to create a new entry using Markdown formating.

**Edit Page:** Users are able to edit entries.

**Random Page:** Will redirect the user to a random page from the list of encyclopedia entries. 

**Markdown to HTML conversion:** When the user requests an entry the entries Markdown file is converted to HTML using the 'markdown2' library.



