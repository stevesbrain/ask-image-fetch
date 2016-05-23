# Import ingredients to make soup
from bs4 import BeautifulSoup

# Generic URL parsing goodies
import urllib.request
import http.client

# Some arguments for the command line
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", dest="user_url", help="The URL for parsing", type=str)

args = parser.parse_args()

# URL from the arguments; assign to variable and fetch

web_url = args.user_url

page = urllib.request.urlopen(web_url)

# Parse the HTML with lxml

soup = BeautifulSoup(page, 'lxml')

# Assign all <img> tags to tag types

tag = soup.img

# Finding data-poll-url; using find instead of findAll
# as findAll returns "results set" and not tag

data_tag = soup.find('a', id="newItemsReady")

print(data_tag['data-poll-url'])


# Look for <img> that has both src and onerror - other images in page
# that were extraneous did not have these attributes

def has_img_and_onerror(tag):
    return tag.has_attr('onerror') and tag.has_attr('src')

# Get just the src attributes of these tags

for images in soup.findAll(has_img_and_onerror):
    print(images.get('src'))