# keyword-search
Using a browser keyword, instantly jump to a webpage in your browser
This way for example with the keyword "in" you can instantly jump to your mail box by typing "in mail" in your search bar.

## Setup

- Go to your browser, add a search engine
- Give it a name
- Give it a keyword (optional, you could also make it without and set it as default) (e.g. "in")
- Set the url search term to 
```
http://localhost:5000/%s
```
- search with "in <key>"

The .pyw ending means it should run in the background by default, and Flask debug mode means that it will auto update, so to add more keywords simply edit the file and add to the dictionary, then save the file.

## Requirements
- Python 3.6+
- Flask 
