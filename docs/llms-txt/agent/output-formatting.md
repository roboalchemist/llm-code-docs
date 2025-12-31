# Source: https://docs.agent.ai/output-formatting.md

# How to Format Output for Better Readability

When working with data in [Agent.ai](http://Agent.ai), you might find that the default output format isn't always easy to read or interpret. This is especially true when dealing with structured data like tweets, JSON, or other complex information. In this guide, we'll show you simple but powerful techniques to transform messy output into beautifully formatted, readable content.

## Create Better Formatting Prompts

<iframe width="560" height="315" src="https://www.youtube.com/embed/yJmF7c0N4Vg?si=oISTh9cgo7pxkAkZ" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### Step 1: Identify the Formatting Issue

First, recognize when your [Agent.ai](http://Agent.ai) output needs better formatting. If you're looking at data that's hard to read or doesn't have clear visual organization, it's time to improve the formatting.

### Step 2: Ask ChatGPT to Generate a Better Prompt

Take your unformatted output to ChatGPT and ask it to create a prompt specifically designed for better formatting. For example:

"I have a list of tweets with data about the tweets, etc. It's in a raw, non-human readable format. I'd like you to generate a prompt that'll do two things:

1. Generate a summary of the tweets
2. Return each tweet in a readable form"

Then paste your unformatted output so ChatGPT can see what you're working with.

### Step 3: Use the New Prompt in [Agent.ai](http://Agent.ai)

ChatGPT will provide you with a more detailed prompt that includes specific formatting instructions. It might look something like:

"I have a dataset of tweets in JSON format. Perform the following tasks:

1. Generate a summary of the tweets
2. For each tweet, reformat it so it looks like this: \[Example of nicely formatted output]"

Copy this entire prompt and paste it into your [Agent.ai](http://Agent.ai) editor, replacing your original prompt.

### Step 4: Run Your Agent with the New Prompt

When you run your agent with the improved prompt, you'll get much more readable output. For example, instead of jumbled text about tweets, you might get:

Summary of tweets: \[Clear summary of main topics]

Most notable tweet: \[Highlighted important tweet]

Tweet Details: Date: \[Date] Content: \[Tweet content] Retweets: \[Number] Impressions: \[Number]

## Create Markdown Tables

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZHsrNv82B6U?si=sZ97MKlX8CjdMOLL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Step 1: Set Up Your Agent's Data Collection

First, create an agent that collects the data you want to display. For example, you could create a news agent that:

* Takes a topic as input
* Uses an API (like Google News) to fetch relevant articles
* Stores the results in a variable

### Step 2: Add a Formatting Action

After collecting your data, add a new action that will format the results into a markdown table:

1. Create a new action in your agent workflow
2. Use the following prompt structure to instruct the AI to create a markdown table: Format the following \[data type] into a markdown table. The table should include the following columns: \[list your columns] Ensure the output is properly formatted for markdown rendering and all links are properly formatted using markdown syntax.

For example, if you're creating a news agent, your prompt might look like:

> Format the following JSON list into a markdown table. The table should include the following columns: Title, Source, and Link Ensure the output is properly formatted for markdown rendering and all links are properly formatted using markdown syntax.

### Step 3: Configure the Output Format

When setting up your final response:

1. Pass the formatted markdown table to your output
2. In the output settings, select "Format as Markdown" to ensure proper rendering

This will ensure that your table displays correctly with proper columns, rows, and formatting.

## Create Interactive HTML Output

<iframe width="560" height="315" src="https://www.youtube.com/embed/-3FHfdikyf8?si=0ZNsXsecJ7uKA2Xc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Structuring Your Content

When designing an agent that outputs HTML, it's important to define a consistent structure.

Common sections for informational agents might include:

* Overview
* Financials
* Products
* Competitors
* News
* Additional Resources

You can also include a Table of Contents at the top of the page that links to each section. Passing structured variables makes it easier for the agent to organize the final output.

### Engineering the HTML Prompt

To generate HTML, add a final instruction asking the agent to format the response accordingly.

Example prompt:

> "Format the response as a complete HTML document. Include a Table of Contents linking to each section (Overview, Financials, Products, Competitors, News, Additional Resources). Organize the information with clear headings, bullet points, and tables where appropriate."

You can instruct the agent to create anchor links for navigation and use lightweight formatting for better readability. At the end of the prompt, add:

> "Format the response as HTML."

This tells [Agent.ai](http://Agent.ai) to render the final output as HTML rather than plain text.

### Best Practices

* Use section headers (\<h2>, \<h3>) to organize information.
* Add anchor links (\<a href="#section-id">) for easier navigation.
* Use tables for structured data like financials or product comparisons.
* Keep formatting lightweight and focused on clarity.

Formatting agent responses as HTML allows you to create more structured, interactive outputs without custom development.
By defining your content flow, gathering the right inputs, and prompting clearly, you can design richer user experiences directly inside Agent.ai.

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).
