"""
Created to allow me to convert my Medium bookmarks to a CSV file.
I had already combined all my bookmarks into a single HTML file ready for this.
"""

import csv
from bs4 import BeautifulSoup
from datetime import datetime

def convert_html_to_csv(html_file, csv_file):
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
        
            bookmarks.append([title, url, '', '', created])
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'URL', 'Excerpt', 'Tags', 'Created'])
        writer.writerows(bookmarks)

# Replace with your file paths
html_file = 'combined.html'
csv_file = 'output_csv_file.csv'

convert_html_to_csv(html_file, csv_file)
