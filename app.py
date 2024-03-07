import requests
import re
import json

def get_latest_time_stories():
    url = "https://time.com"
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        latest_stories = []
        
        # Extracting titles and links using regex
        titles = re.findall(r'<h3 class="headline">(.*?)<\/h3>', html_content)[:6]
        links = re.findall(r'<a href="(.*?)">', html_content)[:6]

        # Cleaning up titles and links
        titles = [re.sub(r'<.*?>', '', title) for title in titles]
        links = ['https://time.com' + link if link.startswith('/') else link for link in links]

        # Creating JSON object array
        for title, link in zip(titles, links):
            latest_stories.append({'title': title.strip(), 'link': link.strip()})
        
        return json.dumps(latest_stories)
    else:
        print("Failed to fetch page:", response.status_code)

if _name_ == "_main_":
    latest_stories_json = get_latest_time_stories()
    print(latest_stories_json)