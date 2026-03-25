# Source: https://docs.nimbleway.io/quick-start-tutorials/tutorial-library/track-seo-and-sem-ranking.md

# Track SEO and SEM Ranking

## AI-Powered SEO and SEM Monitoring with the Nimble Platform

In the digital age, businesses strive to maintain a robust online presence. SEO (Search Engine Optimization) and SEM (Search Engine Marketing) play a crucial role in this endeavor. However, monitoring your SEO and SEM strategies can often be a daunting task.

Fear not! We're here to show you how Nimble Data Platform’s [SERP API](http://nimbleway-com-export.s100.upress.link/nimble-api/serp/) can automate your SEO and SEM performance monitoring, providing insightful, data-driven cues for decision-making.

### **Harnessing AI for SEO and SEM Monitoring** <a href="#heading-1" id="heading-1"></a>

Traditional web scraping tools, like Beautiful Soup, can extract data from web pages. Yet, they frequently stumble over complex and dynamic content such as SERPs (Search Engine Results Pages).

This is where AI-powered tools come to the rescue. Nimble's built-in data structuring AI engine can comprehend the structure and content of web pages, making it a breeze to extract valuable information for SEO and SEM monitoring.

### **Step-by-Step Guide to AI-Powered SEO Monitoring** <a href="#heading-2" id="heading-2"></a>

Now, that we’ve discussed the advantages of Nimble’s data platform, let’s see how we can put it into practice with a practical example.

In this guide, we’ll demonstrate how to write a simple script using Python that uses[Nimble’s SERP API](http://nimbleway-com-export.s100.upress.link/nimble-api/serp/) to access, parse, and retrieve SERP data.

Once Nimble has returned the parsed data, we’ll write some simple code to compare previous results with the latest result and inform us of any changes in the rankings of pages.

#### Step 1: Import Required Libraries and Set Up Nimble SERP API

We’ll start off by importing the needed Python libraries:

```javascript
import requests
import base64
import time
```

Next, we’ll define the basic parameters we’ll need to construct the request for Nimble’s SERP API, including our credentials, desired search engine, search query, and more:

```javascript
# Substitute with your Nimble API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'

# Encode credentials
credentials = f"{api_key}:{api_secret}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

# Set up headers
headers = {
    'Authorization': f'Basic {encoded_credentials}',
    'Content-Type': 'application/json'
}

# Set up request parameters
search_engine = 'google_search'
country = 'US'
locale = 'en'
query = 'your_search_query'
```

#### Step 2: Collect SERP Data and Extract Relevant Information

Next, we'll define a Python function to [collect the SERP data](http://nimbleway-com-export.s100.upress.link/nimble-api/serp/) for specified keywords and extract relevant information using Nimble's AI engine. In this example, we’ll extract and store the organic search results.

```javascript
# Function to fetch SERP data
def get_serp_data(query, start=0):
    url = '<https://api.webit.live/api/v1/realtime/serp>'
    data = {
        'search_engine': search_engine,
        'country': country,
        'locale': locale,
        'query': query,
        'parse': true,
        'start': start
    }
    response = requests.post(url, headers=headers, json=data)
    organic_results = response['parsing']['entities']['OrganicResult']
    return organic_results
```

**Step 3: Monitor SEO Performance**

In this step, we will devise a function to monitor SEO performance for specific keywords. By automating this process, you can efficiently track and analyze the performance of your business and its competitors. The function will run at specified intervals to provide timely insights.

```javascript
# Collect initial SERP data
organic_results = get_serp_data(query)

# Monitor page rankings over time
while True:
    print("Monitoring page rankings...")
    time.sleep(86400)  # Wait for 24 hours (86400 seconds)

    # Fetch updated SERP data
    updated_organic_results = get_serp_data(query)

    # Compare initial and updated organic results
    for initial_result, updated_result in zip(organic_results, updated_organic_results):
        initial_position = initial_result['position']
        updated_position = updated_result['position']

        if initial_position != updated_position:
            print(f"URL {initial_result['url']} changed position from {initial_position} to {updated_position}")

    # Update organic_results for the next iteration
    organic_results = updated_organic_results<code class="language-python">
</code>
```

‍

With this approach, businesses can efficiently monitor their SEO performance for multiple keywords, eliminating the need for manual data extraction and analysis. This enables them to optimize their strategies, improve their search engine rankings, and ultimately drive more traffic to their websites.

### **Real-World Use Cases** <a href="#heading-3" id="heading-3"></a>

Search engines today are capable of providing information on virtually any subject, and include sophisticated widgets that make useful information even more accessible.

As a result, the use cases for SERP data collection are virtually limitless. For example:

* **SEO Optimization** - Monitor changes in your website and landing page rankings to establish the true, data-driven impact of adjustments to your website and SEO strategy. Discover new keywords in real-time as competitors add them to organic and paid listings, and integrate them into your marketing strategy.
* **E-commerce** - Discover new products and SEM campaigns created by competitors in real-time. Use the SERP API to discover which keywords your competitors are targeting, and where your products are ranking in relation to theirs.
* **Travel data collection** - Automate the collection of flight information including destinations, take-off and landing times, prices, and more. Search engines such as Google automatically collect and present flight data from a variety of sources - making it accessible to Nimble’s SERP API.

### **Conclusion** <a href="#heading-4" id="heading-4"></a>

Automating SEO and SEM monitoring with the Nimble Data Platform and Nimble's built-in data structuring AI engine can save businesses time and effort while providing valuable insights into their online performance.

By automating the monitoring process and leveraging AI technologies, businesses can make more informed decisions about their SEO and SEM strategies, leading to better search engine rankings and increased website traffic.

Nimble offers a suite of powerful solutions for web data collection, making it the perfect tool for businesses looking to gain a competitive edge in their SEO and SEM efforts. Try Nimble today to see how it can revolutionize your SEO and SEM monitoring process.
