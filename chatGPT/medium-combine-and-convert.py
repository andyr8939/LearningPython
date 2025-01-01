"""
Created to allow me to convert my Medium bookmarks to a CSV file and HTML file.
This combines multiple HTML files from the original export into a single CSV file and HTML file.
"""

import csv
from bs4 import BeautifulSoup
from datetime import datetime

def extract_bookmarks_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    bookmarks = []
    for li in soup.find_all('li'):
        a = li.find('a')
        time = li.find('time')

        if a and time:
            title = a.get_text()
            url = a.get('href')
            add_date = time.get_text()

            # Convert the date to the ISO 8601 format (UTC)
            created = datetime.strptime(add_date, "%Y-%m-%d %I:%M %p").isoformat()
        
            bookmarks.append([title, url, add_date])
    
    return bookmarks

def combine_html_to_csv_and_html(html_files, csv_file, combined_html_file):
    all_bookmarks = []

    for html_file in html_files:
        all_bookmarks.extend(extract_bookmarks_from_html(html_file))
    
    # Write bookmarks to CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'URL', 'Excerpt', 'Tags', 'Created'])
        for bookmark in all_bookmarks:
            writer.writerow([bookmark[0], bookmark[1], '', '', datetime.strptime(bookmark[2], "%Y-%m-%d %I:%M %p").isoformat()])
    
    # Write bookmarks to combined HTML file
    with open(combined_html_file, 'w', encoding='utf-8') as f:
        f.write('<!DOCTYPE html><html><head><title>Combined Bookmarks</title></head><body><ul>\n')
        for bookmark in all_bookmarks:
            f.write(f'<li><a href="{bookmark[1]}">{bookmark[0]}</a> (<time>{bookmark[2]}</time>)</li>\n')
        f.write('</ul></body></html>')

# Replace with your list of HTML file paths
html_files = ['bookmarks-0001.html', 'bookmarks-0002.html','bookmarks-0003.html','bookmarks-0004.html','bookmarks-0005.html',]
csv_file = 'output_combined_csv_file.csv'
combined_html_file = 'output_combined_html_file.html'

combine_html_to_csv_and_html(html_files, csv_file, combined_html_file)
