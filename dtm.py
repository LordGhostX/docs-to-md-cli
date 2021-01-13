import os
import sys
import codecs
import secrets
import wget
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


def show_help():
    print("python dtm.py <docs URL>")
    print("python dtm.py <docs URL> <local|docs>")


def get_title(soup):
    r_title = soup.find("title").text.strip()
    title = "".join([i if i.isalnum() else "-" for i in r_title.lower()])
    try:
        os.mkdir(title)
    except:
        pass
    return r_title, title


def clean_href(html):
    def parse_href(href):
        return href.split("?q=")[1].split("&sa")[0]

    for i in html.find_all("a"):
        html = BeautifulSoup(str(html).replace(i["href"].replace(
            "&", "&amp;"), parse_href(i["href"])), "html.parser")

    return str(html)


def download_images(title, html):
    html = BeautifulSoup(html, "html.parser")
    for i in html.find_all("img"):
        image_name = secrets.token_urlsafe(15).lower() + ".png"
        image_path = os.path.join(title, image_name)
        wget.download(i["src"], image_path)
        html = str(html).replace(i["src"], image_name)
    return str(html)


def main(docs_url, method):
    r = requests.get(docs_url)

    soup = BeautifulSoup(r.text, "html.parser")
    r_title, title = get_title(soup)
    html = soup.find("div", {"id": "contents"}).find("div")

    html = clean_href(html)
    if method == "local":
        html = download_images(title, html)

    markdown = markdownify(html, heading_style="ATX").replace("\_", "_")
    with codecs.open(os.path.join(title, "index.md"), "w") as md:
        md.write(markdown)

    print(f"Successfully converted '{r_title}' from Docs to MarkDown")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
        exit()
    else:
        if len(sys.argv) == 2:
            method = "local"
        else:
            method = sys.argv[2].lower()
        if method in ["local", "docs"]:
            main(sys.argv[1], method)
        else:
            show_help()
