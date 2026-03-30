# Source: https://scrapfly.io/docs/mcp/integrations/chatgpt

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/mcp/integrations/chatgpt

Markdown Content:
1.   [MCP Documentation](https://scrapfly.io/docs/mcp)
2.   [Integrations](https://scrapfly.io/docs/mcp/integrations)
3.   ChatGPT

[Prerequisites](https://scrapfly.io/docs/mcp/integrations/chatgpt#prerequisites)
--------------------------------------------------------------------------------

Before getting started, make sure you have the following:

*   [ChatGPT Plus or Team subscription](https://chat.openai.com/)
*   An active [Scrapfly account](https://scrapfly.io/register)
*   Your Scrapfly API key (from your [Dashboard](https://scrapfly.io/dashboard))

[Getting Started](https://scrapfly.io/docs/mcp/integrations/chatgpt#getting-started)
------------------------------------------------------------------------------------

Watch this quick video tutorial to get up and running with Scrapfly MCP on ChatGPT:

[Setup via MCP (Developer Mode)](https://scrapfly.io/docs/mcp/integrations/chatgpt#setup)
-----------------------------------------------------------------------------------------

Connect Scrapfly MCP directly to ChatGPT using Developer Mode. This gives you full access to all Scrapfly scraping tools with your own API key.

1.   **Navigate to App Settings**
In ChatGPT, click your **profile icon** in the bottom-left corner and select **Settings**. In the left-hand menu, click on **Apps**, then select **Advanced settings**.

2.   **Enable Developer Mode**
Toggle **Developer mode** to the ON position, then click the **"Create app"** button at the top right of the window.

3.   **Connect Scrapfly MCP**
Fill in the following details in the configuration window:

    *   **Name:**`Scrapfly`
    *   **MCP Server URL:**

`https://mcp.scrapfly.io/mcp?key=`

    *   **Authentication:** Select `No Auth` (authentication is handled securely via the API key in the URL)
    *   **Mandatory:** Check the box _"I understand and want to continue"_ to acknowledge the use of a custom MCP server

Click **"Create"**.

4.   **Start scraping!**
You are all set! Simply ask ChatGPT to scrape a webpage in your normal chat window. ChatGPT will automatically trigger the Scrapfly tool when needed to retrieve real-time data.

**Note:** The first time you prompt a scrape, ChatGPT will ask you to click **"Allow"** to grant Scrapfly access.

[Alternative: CustomGPT](https://scrapfly.io/docs/mcp/integrations/chatgpt#customgpt)
-------------------------------------------------------------------------------------

Scrapfly also provides a CustomGPT that integrates web scraping capabilities directly into ChatGPT. This enables conversational, AI-powered data collection where you simply describe what data you need, and ChatGPT handles the technical scraping details.

[What You Can Do](https://scrapfly.io/docs/mcp/integrations/chatgpt#use-cases)
------------------------------------------------------------------------------

The Scrapfly CustomGPT enables a wide range of conversational web scraping use cases:

##### Research & Analysis

*   Market research and competitor analysis
*   Industry trend monitoring
*   Academic and scientific research
*   News and media monitoring

##### Content Extraction

*   Article and blog post scraping
*   Product information extraction
*   Review and rating collection
*   Technical documentation mining

##### Data Monitoring

*   Price tracking and comparison
*   Availability checking
*   Change detection
*   Alert generation

##### Visual Capture

*   Full-page screenshots
*   Multi-viewport captures
*   Element-specific screenshots
*   Responsive design testing

[How It Works](https://scrapfly.io/docs/mcp/integrations/chatgpt#how-it-works)
------------------------------------------------------------------------------

The CustomGPT uses OpenAI's function calling to access Scrapfly's web scraping infrastructure. When you ask for data from a website:

1.   **You describe what you need**
Use natural language to explain what data you want to extract from which website.

2.   **ChatGPT calls Scrapfly's API**
The CustomGPT automatically invokes the appropriate Scrapfly scraping functions with optimal parameters.

3.   **Data is extracted and formatted**
Scrapfly scrapes the website, bypassing anti-bot protections, and returns clean data.

4.   **ChatGPT presents results**
The AI analyzes, formats, and presents the data according to your request - tables, summaries, insights, etc.

**No coding required:** The CustomGPT handles all technical details - selectors, parsing, error handling, and anti-bot bypass. You just describe what you need!

[Example Conversations](https://scrapfly.io/docs/mcp/integrations/chatgpt#examples)
-----------------------------------------------------------------------------------

Here are real-world examples of conversational scraping with the Scrapfly CustomGPT:

### Research & Analysis

###### Market Research

Compare the pricing of the top 3 web scraping services and create a detailed comparison table

###### Competitor Intelligence

Analyze competitor.com blog, extract all article titles from the last 6 months, and identify trending topics

###### Industry News

Scrape Hacker News front page, filter for AI-related stories, and summarize the top discussions

### Content Extraction

###### Article Scraping

Extract the full text, author, and publish date from this Medium article and format as markdown

###### Product Data

Scrape this Amazon product page and extract the price, rating, review count, and top 5 customer reviews

###### Documentation Mining

Extract all API endpoint names and descriptions from stripe.com/docs/api and create a reference table

### Data Monitoring

###### Price Comparison

Check the current price of iPhone 15 on Apple.com, Amazon, and Best Buy, then create a comparison

###### Availability Tracking

Check if the Nintendo Switch is in stock at these 5 retailer URLs and report availability status

###### Change Detection

Compare the current pricing page of competitor.com with the version from last month and highlight changes

### Screenshots & Visual Analysis

###### Full Page Screenshot

Take a full-page screenshot of scrapfly.io homepage and analyze the design layout

###### Responsive Design

Capture screenshots of this landing page in mobile, tablet, and desktop viewports and compare layouts

###### Visual Comparison

Screenshot the pricing sections of Scrapfly, ScrapingBee, and Zyte, then compare their design approaches

### Multi-Step Workflows

###### News Aggregation

Find the top 5 AI-related posts on Hacker News, scrape each article, and create a summary digest with key points

###### Product Research

Get today's top 3 products from Product Hunt, scrape their websites, and analyze their value propositions and pricing strategies

###### SEO Analysis

Scrape the top 10 Google results for "web scraping API", extract titles and meta descriptions, and analyze SEO patterns

[Limitations & Best Practices](https://scrapfly.io/docs/mcp/integrations/chatgpt#limitations)
---------------------------------------------------------------------------------------------

### Current Limitations

*   **Authentication:** The CustomGPT works without Scrapfly credentials for most public websites, but authenticated scraping requires your own API key
*   **Rate Limits:** Free usage has rate limits; for high-volume scraping, use your own Scrapfly API key
*   **Complex Scraping:** For advanced scenarios (JavaScript rendering, CAPTCHA solving, session management), direct API access via [Claude Desktop](https://scrapfly.io/docs/mcp/integrations/claude-desktop) or [OpenAI API](https://scrapfly.io/docs/mcp/integrations/openai) is recommended

### Best Practices

*   **Be Specific:** Clearly describe what data you need and in what format
*   **Provide URLs:** Include full URLs for the pages you want to scrape
*   **Iterate:** If results aren't perfect, refine your request with additional details
*   **Respect Limits:** For high-volume scraping, use the official API with your own credentials

[More Powerful Alternatives](https://scrapfly.io/docs/mcp/integrations/chatgpt#alternatives)
--------------------------------------------------------------------------------------------

For advanced scraping needs, consider these alternatives with full MCP support:

##### ![Image 1: Claude](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/claude-icon.svg?version=0.1.176)[Claude Desktop](https://scrapfly.io/docs/mcp/integrations/claude-desktop)

Full MCP integration with OAuth2 authentication and unlimited scraping capabilities.

*   Native MCP protocol support
*   OAuth2 + API key authentication
*   Unlimited scraping with your credits
*   Advanced JavaScript rendering support

##### ![Image 2: OpenAI](https://cdn.scrapfly.io/0.1.176/www/public/svg/integrations/openai-icon.svg?version=0.1.176)[OpenAI API](https://scrapfly.io/docs/mcp/integrations/openai)

Programmatic access with function calling for custom AI applications.

*   Full API control and customization
*   Function calling integration
*   Build custom assistants and chatbots
*   Production-ready scalability

[Troubleshooting](https://scrapfly.io/docs/mcp/integrations/chatgpt#troubleshooting)
------------------------------------------------------------------------------------

**Cause:** CustomGPTs require ChatGPT Plus or Team subscription

**Solution:**

*   Verify you have a ChatGPT Plus or Team subscription
*   Check the CustomGPT link is not broken (click the link above)
*   Try accessing from https://chat.openai.com/gpts/discovery
*   If unavailable, use [Claude Desktop](https://scrapfly.io/docs/mcp/integrations/claude-desktop) or [OpenAI API](https://scrapfly.io/docs/mcp/integrations/openai) as alternatives

**Cause:** Rate limits, invalid URL, or website blocking

**Solution:**

*   Verify the URL is correct and publicly accessible
*   Check if you've hit rate limits (wait and retry)
*   For high-volume scraping, use your own Scrapfly API key
*   Some websites may require JavaScript rendering - specify this in your request
*   For protected sites, consider [Claude Desktop](https://scrapfly.io/docs/mcp/integrations/claude-desktop) with full MCP support

**Cause:** Ambiguous request or complex page structure

**Solution:**

*   Be more specific about what data you want to extract
*   Provide examples of the expected output format
*   Try breaking complex requests into smaller steps
*   If extraction fails repeatedly, check the page source manually
*   For dynamic content, specify that JavaScript rendering is needed

**Cause:** Large pages, slow target websites, or heavy processing

**Solution:**

*   Request smaller chunks of data instead of entire pages
*   Avoid scraping multiple pages in a single request
*   For batch operations, break into separate conversations
*   For time-sensitive scraping, use direct API access instead

[Next Steps](https://scrapfly.io/docs/mcp/integrations/chatgpt#next-steps)
--------------------------------------------------------------------------

*   [Explore available MCP tools](https://scrapfly.io/docs/mcp/tools) and their capabilities
*   [See real-world examples](https://scrapfly.io/docs/mcp/examples) of what you can build
*   [Learn about authentication methods](https://scrapfly.io/docs/mcp/authentication) in detail
*   [Read the FAQ](https://scrapfly.io/docs/mcp/faq) for common questions
