"""
This script takes a CSV file exported from Pocket and converts it to a CSV file in Raindrop.io format.
"""
import csv
from datetime import datetime

def convert_csv_to_raindrop(input_csv, output_csv):
    bookmarks = []

    # Read the input CSV file
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            title = row['title']
            url = row['url']
            add_date = row['time_added']

            # Convert the time_added to the ISO 8601 format (UTC)
            created = datetime.utcfromtimestamp(int(add_date)).isoformat()
        
            bookmarks.append([title, url, '', '', created])
    
    # Write the bookmarks to the output CSV file in Raindrop.io format
    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'URL', 'Excerpt', 'Tags', 'Created'])
        writer.writerows(bookmarks)

# Replace with your file paths
input_csv = 'part_000000.csv'
output_csv = 'output_pocket_raindrop_csv_file.csv'

convert_csv_to_raindrop(input_csv, output_csv)
