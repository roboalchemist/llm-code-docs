# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/mapping-reddit-comments-with-atlas

In this cookbook, we show how to automate the extraction, processing, and mapping of Reddit comments using Python and Nomic Atlas. You can also view this cookbook on our github.

We'll use the Reddit API to fetch comments from this Reddit post URL, store the data in Nomic Atlas and create an Atlas map on the dataset to produce this visualization:

## Getting Started​

### Prerequisites​

Before we begin, make sure you have:

- Python (3.6 or higher) installed on your machine.
- Reddit API credentials (client ID, client secret, user agent). You can obtain these from your Reddit developer account.
- Nomic API key to access Nomic Atlas.
### Install Required Libraries​

Install the necessary Python libraries:

```
pip install pandas pyarrow praw nomic
```

### Setting Up Environment Variables for Reddit and Nomic API Keys​

To securely manage your Reddit API credentials and Nomic API key, follow these steps to set them up as environment variables:

- Reddit API Credentials:

Open your terminal or command prompt.
Set your Reddit client ID, client secret, and user agent as environment variables. Replace <your_client_id>, <your_client_secret>, and <your_user_agent> with your actual Reddit API credentials.

export REDDIT_CLIENT_ID=<your_client_id>export REDDIT_CLIENT_SECRET=<your_client_secret>export REDDIT_USER_AGENT=<your_user_agent>

Alternatively, you can add these lines to your shell configuration file (e.g., .bashrc, .zshrc) to persist them across sessions.
Reddit API Credentials:

- Open your terminal or command prompt.
- Set your Reddit client ID, client secret, and user agent as environment variables. Replace <your_client_id>, <your_client_secret>, and <your_user_agent> with your actual Reddit API credentials.
```
<your_client_id>
```

```
<your_client_secret>
```

```
<your_user_agent>
```

```
export REDDIT_CLIENT_ID=<your_client_id>export REDDIT_CLIENT_SECRET=<your_client_secret>export REDDIT_USER_AGENT=<your_user_agent>
```

- Alternatively, you can add these lines to your shell configuration file (e.g., .bashrc, .zshrc) to persist them across sessions.
```
.bashrc
```

```
.zshrc
```

- Nomic API Key:

Similarly, set your Nomic API key as an environment variable. Replace <your_nomic_api_key> with your actual Nomic API key.

export NOMIC_API_KEY=<your_nomic_api_key>

Add this line to your shell configuration file to keep it persistent.
Nomic API Key:

- Similarly, set your Nomic API key as an environment variable. Replace <your_nomic_api_key> with your actual Nomic API key.
```
<your_nomic_api_key>
```

```
export NOMIC_API_KEY=<your_nomic_api_key>
```

- Add this line to your shell configuration file to keep it persistent.
- Using the Environment Variables:

In your Python script, access these environment variables using os.getenv() function. For example:

import osclient_id = os.getenv('REDDIT_CLIENT_ID')client_secret = os.getenv('REDDIT_CLIENT_SECRET')user_agent = os.getenv('REDDIT_USER_AGENT')nomic_api_key = os.getenv('NOMIC_API_KEY')

This ensures your API credentials are securely managed without hardcoding them in your scripts.
Using the Environment Variables:

- In your Python script, access these environment variables using os.getenv() function. For example:
```
os.getenv()
```

```
import osclient_id = os.getenv('REDDIT_CLIENT_ID')client_secret = os.getenv('REDDIT_CLIENT_SECRET')user_agent = os.getenv('REDDIT_USER_AGENT')nomic_api_key = os.getenv('NOMIC_API_KEY')
```

- This ensures your API credentials are securely managed without hardcoding them in your scripts.
### Import Libraries​

Next, let's include the required libraries at the top of your Python script:

```
import pandas as pdimport pyarrow as pafrom nomic import AtlasDatasetfrom prawcore.exceptions import PrawcoreExceptionimport prawimport os
```

## Helper Functions​

### Fetching Comments and Replies​

Now, we'll define functions to fetch Reddit comments and their replies:

```
def scrape_reddit_comments(reddit: praw.Reddit, submission: praw.models.reddit.submission.Submission) -> list:    # Function to scrape Reddit comments    max_attempts = 5      current_attempt = 0    while current_attempt < max_attempts:        try:            submission.comments.replace_more(limit=None)            time.sleep(1)  # Add a delay between replace_more() calls            comments = fetch_all_comments(submission)            print(f"Number of comments fetched: {len(comments)}")            return comments        except PrawcoreException as e:            if e.response and e.response.status_code == 429:                delay = 2 ** current_attempt                  print(f"Rate limit exceeded. Retrying in {delay} seconds...")                time.sleep(delay)                current_attempt += 1            else:                print(f"Error scraping comments: {e}")                return []    print("Max retry attempts reached. Could not fetch comments.")    return []def fetch_all_comments(submission: praw.models.reddit.submission.Submission) -> list:    # Function to fetch all comments from a Reddit submission    comments = []    submission.comments.replace_more(limit=None)    time.sleep(1)    for comment in submission.comments.list():        comment_data = {            'text': comment.body,            'author': comment.author.name if comment.author else '[deleted]',            'score': comment.score,            'depth': comment.depth,            'created_utc': comment.created_utc        }        comments.append(comment_data)        comments.extend(fetch_replies(comment))    return commentsdef fetch_replies(comment: praw.models.reddit.comment.Comment) -> list:    # Function to fetch replies to a Reddit comment    replies = []    if isinstance(comment, praw.models.reddit.comment.Comment):        if hasattr(comment, 'replies') and isinstance(comment.replies, praw.models.comment_forest.CommentForest):            comment.replies.replace_more(limit=None)            time.sleep(1)            for reply in comment.replies.list():                reply_data = {                    'text': reply.body,                    'author': reply.author.name if reply.author else '[deleted]',                    'score': reply.score,                    'depth': reply.depth,                    'created_utc': reply.created_utc                }                replies.append(reply_data)                replies.extend(fetch_replies(reply))    return repliesdef comments_to_arrow_table(comments: list) -> pa.Table:    # Function to convert comments into an Arrow Table for efficient data handling    df = pd.DataFrame(comments)    arrow_table = pa.Table.from_pandas(df)    return arrow_table
```

## Main Function​

Now, let's walk through the main function that orchestrates the entire process:

```
def main():    # Function to automate Reddit comment mapping with Nomic Atlas    # Retrieve Reddit API credentials and Nomic API key from environment variables    client_id = os.getenv('REDDIT_CLIENT_ID')    client_secret = os.getenv('REDDIT_CLIENT_SECRET')    user_agent = os.getenv('REDDIT_USER_AGENT')    reddit_url = input("Enter Reddit post URL: ")    nomic_api_key = os.getenv('NOMIC_API_KEY')    # Initialize Reddit instance    reddit = get_reddit_instance(client_id, client_secret, user_agent)    submission = reddit.submission(url=reddit_url)    # Scrape Reddit comments    comments = scrape_reddit_comments(reddit, submission)    arrow_table = comments_to_arrow_table(comments)    try:        map_name = f"[Reddit Comment Thread] {submission.title}"          dataset = AtlasDataset(            map_name,            description='Reddit comments mapped via automation.'        )        dataset.add_data(arrow_table)        atlas_map = dataset.create_index(            indexed_field='text',        )                if atlas_map:            print("Map created on Atlas with ID:", dataset.id)            print("All done! Visit the map link to see the status of your map build.")        else:            print("Map creation failed.")    except Exception as e:        print(f"An error occurred while building map on Atlas: {e}")def get_reddit_instance(client_id: str, client_secret: str, user_agent: str) -> praw.Reddit:    # Function to create a Reddit instance    reddit = praw.Reddit(        client_id=client_id,        client_secret=client_secret,        user_agent=user_agent    )    return redditif __name__ == "__main__":    main()
```

Now run the script and see your data come to life!

- Getting StartedPrerequisitesInstall Required LibrariesSetting Up Environment Variables for Reddit and Nomic API KeysImport Libraries
- Prerequisites
- Install Required Libraries
- Setting Up Environment Variables for Reddit and Nomic API Keys
- Import Libraries
- Helper FunctionsFetching Comments and Replies
- Fetching Comments and Replies
- Main Function
