from flask import Flask, redirect

app = Flask(__name__)

# Add this search engine to your browser: http://localhost:5000/%s

# Use full URL
go_links = {
    "maps": "https://maps.google.com",
    "gh": "https://github.com",
    "mail": "https://mail.google.com",
    "news": "https://lite.cnn.com"
}

@app.route("/<path:key>")
def go(key):
	# Change this to any search engine as fallback
    url = go_links.get(key, f"https://duckduckgo.com/?q={key}")
    return redirect(url)

if __name__ == "__main__":
	# Debug is true so that editing this file will auto update the keyword index
    app.run(port=5000, debug=True)
