# Create an app

If you've made it this far, chances are you've [installed Streamlit](/get-started/installation) and run through the basics in [Basic concepts](/get-started/fundamentals/main-concepts) and [Advanced concepts](/get-started/fundamentals/advanced-concepts). If not, now is a good time to take a look.

The easiest way to learn how to use Streamlit is to try things out yourself. As you read through this guide, test each method. As long as your app is running, every time you add a new element to your script and save, Streamlit's UI will ask if you'd like to rerun the app and view the changes. This allows you to work in a fast interactive loop: you write some code, save it, review the output, write some more, and so on, until you're happy with the results. The goal is to use Streamlit to create an interactive app for your data or model and along the way to use Streamlit to review, debug, perfect, and share your code.

In this guide, you're going to use Streamlit's core features to create an interactive app; exploring a public Uber dataset for pickups and drop-offs in New York City. When you're finished, you'll know how to fetch and cache data, draw charts, plot information on a map, and use interactive widgets, like a slider, to filter results.

## Let's put it all together

That's it, you've made it to the end. Here's the complete script for our interactive app.

```python
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/' 'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data...done!')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
```

## Share your app

After you’ve built a Streamlit app, it's time to share it! To show it off to the world you can use **Streamlit Community Cloud** to deploy, manage, and share your app for free.

It works in 3 simple steps:

1. Put your app in a public GitHub repo (and make sure it has a requirements.txt!)
2. Sign into [share.streamlit.io](https://share.streamlit.io/)
3. Click 'Deploy an app' and then paste in your GitHub URL

That's it! 🎈 You now have a publicly deployed app that you can share with the world. Click to learn more about [how to use Streamlit Community Cloud](/deploy/streamlit-community-cloud).

## Get help

That's it for getting started, now you can go and build your own apps! If you run into difficulties here are a few things you can do.

- Check out our [community forum](https://discuss.streamlit.io/) and post a question
- Quick help from command line with `streamlit help`
- Go through our [Knowledge Base](/knowledge-base) for tips, step-by-step tutorials, and articles that answer your questions about creating and deploying Streamlit apps.
- Read more documentation! Check out:

  - [Concepts](/develop/concepts) for things like caching, theming, and adding statefulness to apps.
  - [API reference](/develop/api-reference) for examples of every Streamlit command.