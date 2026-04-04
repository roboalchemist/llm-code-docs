# Source: https://crawlee.dev/blog/linkedin-job-scraper-python.md

# How to create a LinkedIn job scraper in Python with Crawlee

October 14, 2024 ·

<!-- -->

7 min read

[![Arindam Majumder](https://avatars.githubusercontent.com/u/109217591?v=4)](https://github.com/Arindam200)

[Arindam Majumder](https://github.com/Arindam200)

Community Member of Crawlee

## Introduction[​](#introduction "Direct link to Introduction")

In this article, we will build a web application that scrapes LinkedIn for job postings using Crawlee and Streamlit.

We will create a LinkedIn job scraper in Python using Crawlee for Python to extract the company name, job title, time of posting, and link to the job posting from dynamically received user input through the web application.

note

One of our community members wrote this blog as a contribution to Crawlee Blog. If you want to contribute blogs like these to Crawlee Blog, please reach out to us on our [discord channel](https://apify.com/discord).

By the end of this tutorial, you’ll have a fully functional web application that you can use to scrape job postings from LinkedIn.

![Linkedin Job Scraper](data:image/webp;base64,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nYwyZMmTJkyZMmTJkyZMmTJkyZMocqXLly5cuXLly5cuXSPHjx48ePHjx48eO0d82+2TRbe4zjoOiFHqLt/hCj1F2/whR6i7f4Qo9Rdv8IUeou3+EKOf+PTb4Hxw4cOHDhw4cOHDmQiRIkSJEiRIkSJEVuc9x5l7TVdAzwpeAZ4UvAM8KXgGeFLwDPCl4BnhS8AzuuQgQIECBAgQIECBAjOCxYsWLFixYsWLFaZan17VjsKGW4mfhbr4uDWNmMlU5/DYpzUFDKudkJXnBM87dLMZhwLuBdANKzlFVJjrxPyBw4cOHDhw4cOHDhw4cOHDiwPjhw4cOHDhw4cOHMhEiRIkSJEiRIkSIrc31ectMWdFKFIYDAYDAYDAYDAYDAYDAYDAX9HO5dz+vXr169evXr169ews1atWrVq1atWrVqxlcxua1atWrVq1atWrVq1atWrVq1at7J4cOHDhw4cOHDhw4sD44cOHDhw4cOHDhELGz8ho0ggQIECBAgQIECBAgQIECBAgQFB2mEOa1atWrVq1atWrVq3lsmTJkyZMmTJkyZGeus1CmLLs9Rdv8IUeou3+EKPUXb/CFHqLt/hCj1F2/whR6i7f4QlQUougsWLFixYsWLFixZ4PHjx48ePHjx48eLwut/K2BZaHwJ/1E7OH/169evXr169evXr169evXsLNWrVq1atWrVq1atZvJkyZMmTJkyZMmTA5vfI1UIFuBXQxuyTahDxzn+3naEaFCUHjKr7Z0cAY25W4DZ4BCiMzT8bgjHr169evXr169evXr169evfNatWrVq1atWrVq1by2TJkyZMmTJkyZMjPXBCbVB4EhjESWdcDRjdynfp2vU3Lp06dOnTp06dOnTp06dOnWFEiRIkSJEiRIkSJE4Z8+fPnz58+fPnz4+R9TGVTFByOR1er1er1er1er1er1er1er1er1erzzKO2I2gcOHDhw4cOHDhw4cWB8cOHDhw4cOHDhw6SHDhw4cOHDhw4cOHDhw4cOHDhw4cOHDhw4cOHDhw4cOZCJEiRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIkSJEiRIkSJFzmvXr169evXr169evXr169evXr169evXr169evXr169evXr169evXr169evde5cuXLly5cuXLly5cuXLly5cuXLly5cuXLly5cuXLly5c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)

Let's begin.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Let's start by creating a new Crawlee for Python project with this command:

```
pipx run crawlee create linkedin-scraper
```

Select `PlaywrightCrawler` in the terminal when Crawlee asks for it.

After installation, Crawlee for Python will create boilerplate code for you. You can change the directory(`cd`) to the project folder and run this command to install dependencies.

```
poetry install
```

We are going to begin editing the files provided to us by Crawlee so we can build our scraper.

note

Before going ahead if you like reading this blog, we would be really happy if you gave [Crawlee for Python a star on GitHub](https://github.com/apify/crawlee-python/)!

## Building the LinkedIn job Scraper in Python with Crawlee[​](#building-the-linkedin-job-scraper-in-python-with-crawlee "Direct link to Building the LinkedIn job Scraper in Python with Crawlee")

In this section, we will be building the scraper using the Crawlee for Python package. To learn more about Crawlee, check out their [documentation](https://www.crawlee.dev/python/docs/quick-start).

### 1. Inspecting the LinkedIn job Search Page[​](#1-inspecting-the-linkedin-job-search-page "Direct link to 1. Inspecting the LinkedIn job Search Page")

Open LinkedIn in your web browser and sign out from the website (if you already have an account logged in). You should see an interface like this.

![LinkedIn Homepage](/assets/images/linkedin-homepage-8bec2b6a9ae97a18a7e49d4275c14cee.webp)

Navigate to the jobs section, search for a job and location of your choice, and copy the URL.

![LinkedIn Jobs Page](/assets/images/linkedin-jobs-44e352d2233de5adb7af9838b75b9895.webp)

You should have something like this:

`https://www.linkedin.com/jobs/search?keywords=Backend%20Developer&location=Canada&geoId=101174742&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0`

We're going to focus on the search parameters, which is the part that goes after '?'. The keyword and location parameters are the most important ones for us.

The job title the user supplies will be input to the keyword parameter, while the location the user supplies will go into the location parameter. Lastly, the `geoId` parameter will be removed while we keep the other parameters constant.

We are going to be making changes to our `main.py` file. Copy and paste the code below in your `main.py` file.

```
from crawlee.playwright_crawler import PlaywrightCrawler
from .routes import router
import urllib.parse

async def main(title: str, location: str, data_name: str) -> None:
    base_url = "https://www.linkedin.com/jobs/search"

    # URL encode the parameters
    params = {
        "keywords": title,
        "location": location,
        "trk": "public_jobs_jobs-search-bar_search-submit",
        "position": "1",
        "pageNum": "0"
    }

    encoded_params = urlencode(params)

    # Encode parameters into a query string
    query_string = '?' + encoded_params

    # Combine base URL with the encoded query string
    encoded_url = urljoin(base_url, "") + query_string

    # Initialize the crawler
    crawler = PlaywrightCrawler(
        request_handler=router,
    )

    # Run the crawler with the initial list of URLs
    await crawler.run([encoded_url])

    # Save the data in a CSV file
    output_file = f"{data_name}.csv"
    await crawler.export_data(output_file)
```

Now that we have encoded the URL, the next step for us is to adjust the generated router to handle LinkedIn job postings.

### 2. Routing your crawler[​](#2-routing-your-crawler "Direct link to 2. Routing your crawler")

We will be making use of two handlers for your application:

* **Default handler**

The `default_handler` handles the start URL

* **Job listing**

The `job_listing` handler extracts the individual job details.

Playwright crawler is going to crawl through the job posting page and extract the links to all job postings on the page.

![Identifying elements](/assets/images/elements-a634b50a7ad31ae15db61e1a06f5125e.webp)

When you examine the job postings, you will discover that the job posting links are inside an ordered list with a class named `jobs-search__results-list`. We will then extract the links using the Playwright locator object and add them to the `job_listing` route for processing.

```
router = Router[PlaywrightCrawlingContext]()

@router.default_handler
async def default_handler(context: PlaywrightCrawlingContext) -> None:
    """Default request handler."""

    #select all the links for the job posting on the page
    hrefs = await context.page.locator('ul.jobs-search__results-list a').evaluate_all("links => links.map(link => link.href)")

    #add all the links to the job listing route
    await context.add_requests(
            [Request.from_url(rec, label='job_listing') for rec in hrefs]
        )
```

Now that we have the job listings, the next step is to scrape their details.

We'll extract each job’s title, company's name, time of posting, and the link to the job post. Open your dev tools to extract each element using its CSS selector.

![Inspecting elements](/assets/images/inspect-90f77b162804bd1163b16bb23b315ed8.webp)

After scraping each of the listings, we'll remove special characters from the text to make it clean and push the data to local storage using the `context.push_data` function.

```
@router.handler('job_listing')
async def listing_handler(context: PlaywrightCrawlingContext) -> None:
    """Handler for job listings."""

    await context.page.wait_for_load_state('load')

    job_title = await context.page.locator('div.top-card-layout__entity-info h1.top-card-layout__title').text_content()

    company_name  = await context.page.locator('span.topcard__flavor a').text_content()

    time_of_posting= await context.page.locator('div.topcard__flavor-row span.posted-time-ago__text').text_content()


    await context.push_data(
        {
            # we are making use of regex to remove special characters for the extracted texts

            'title': re.sub(r'[\s\n]+', '', job_title),
            'Company name': re.sub(r'[\s\n]+', '', company_name),
            'Time of posting': re.sub(r'[\s\n]+', '', time_of_posting),
            'url': context.request.loaded_url,
        }
    )
```

## 3. Creating your application[​](#3-creating-your-application "Direct link to 3. Creating your application")

For this project, we will be using Streamlit for the web application. Before we proceed, we are going to create a new file named `app.py` in your project directory. In addition, ensure you have [Streamlit](https://docs.streamlit.io/get-started/installation) installed in your global Python environment before proceeding with this section.

```
import streamlit as st
import subprocess

# Streamlit form for inputs
st.title("LinkedIn Job Scraper")

with st.form("scraper_form"):
    title = st.text_input("Job Title", value="backend developer")
    location = st.text_input("Job Location", value="newyork")
    data_name = st.text_input("Output File Name", value="backend_jobs")

    submit_button = st.form_submit_button("Run Scraper")

if submit_button:

    # Run the scraping script with the form inputs
    command = f"""poetry run python -m linkedin-scraper --title "{title}"  --location "{location}" --data_name "{data_name}" """

    with st.spinner("Crawling in progress..."):
         # Execute the command and display the results
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        st.write("Script Output:")
        st.text(result.stdout)

        if result.returncode == 0:
            st.success(f"Data successfully saved in {data_name}.csv")
        else:
            st.error(f"Error: {result.stderr}")
```

The Streamlit web application takes in the user's input and uses the Python Subprocess package to run the Crawlee scraping script.

## 4. Testing your app[​](#4-testing-your-app "Direct link to 4. Testing your app")

Before we test the application, we need to make a little modification to the `__main__` file in order for it to accommodate the command line arguments.

```
import asyncio
import argparse

from .main import main

def get_args():
    # ArgumentParser object to capture command-line arguments
    parser = argparse.ArgumentParser(description="Crawl LinkedIn job listings")


    # Define the arguments
    parser.add_argument("--title", type=str, required=True, help="Job title")
    parser.add_argument("--location", type=str, required=True, help="Job location")
    parser.add_argument("--data_name", type=str, required=True, help="Name for the output CSV file")


    # Parse the arguments
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    # Run the main function with the parsed command-line arguments
    asyncio.run(main(args.title, args.location, args.data_name))
```

We will start the Streamlit application by running this code in the terminal:

```
streamlit run app.py
```

This is what your application what the application should look like on the browser:

![Running scraper](/assets/images/running-555ab15f009be751f516aabd99e6c574.webp)

You will get this interface showing you that the scraping has been completed:

![Filling input form](/assets/images/form-774ee8d03c87acfc38d3012d38a9c4ce.webp)

To access the scraped data, go over to your project directory and open the CSV file.

![CSV file with all scraped LinkedIn jobs](/assets/images/excel-23850449d4d74099a1264cd93ca8565b.webp)

You should have something like this as the output of your CSV file.

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this tutorial, we have learned how to build an application that can scrape job posting data from LinkedIn using Crawlee. Have fun building great scraping applications with Crawlee.

You can find the complete working Crawler code here on the [GitHub repository.](https://github.com/Arindam200/LinkedIn_Scraping)
