# Source: https://docs.crewai.com/en/tools/web-scraping/scrapewebsitetool.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.crewai.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Scrape Website

> The `ScrapeWebsiteTool` is designed to extract and read the content of a specified website.

# `ScrapeWebsiteTool`

<Note>
  We are still working on improving tools, so there might be unexpected behavior or changes in the future.
</Note>

## Description

A tool designed to extract and read the content of a specified website. It is capable of handling various types of web pages by making HTTP requests and parsing the received HTML content.
This tool can be particularly useful for web scraping tasks, data collection, or extracting specific information from websites.

## Installation

Install the crewai\_tools package

```shell  theme={null}
pip install 'crewai[tools]'
```

## Example

```python  theme={null}
from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()

# Initialize the tool with the website URL, 
# so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://www.example.com')

# Extract the text from the site
text = tool.run()
print(text)
```

## Arguments

| Argument         | Type     | Description                                                                                                                                        |
| :--------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **website\_url** | `string` | **Mandatory** website URL to read the file. This is the primary input for the tool, specifying which website's content should be scraped and read. |
