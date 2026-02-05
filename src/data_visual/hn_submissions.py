from operator import itemgetter

import requests

# Make an API call to Hacker News to get the top stories
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process the top stories
submission_ids = r.json()
submissions = []
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()
    submissions.append(
        {
            "title": response_dict.get("title"),
            "link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict.get("descendants", 0),
        }
    )

# Sort the submissions by number of comments
submissions = sorted(submissions, key=itemgetter("comments"), reverse=True)

# Print the top submissions
for submission in submissions:
    print(f"{submission['title']} ({submission['comments']} comments)")
    print(f"Link: {submission['link']}\n")
