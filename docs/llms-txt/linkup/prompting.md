# Source: https://docs.linkup.so/pages/documentation/tutorials/prompting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompting

> Learn how to best prompt Linkup search with - tips, templates, and best practices

Linkup is a precise engine designed to follow **detailed instructions** like a research assistant. The more guidance you give, the better the result. This guide explains how Linkup works, provides practical prompting techniques, and offers templates to get you started.

***

## 1. How the Search API Works

Linkup uses agentic search powered by AI to return content that is as precise and accurate as possible for a given query.

For each request, Linkup:

* Interprets the query and the user's instructions
* Determines how to execute retrieval steps using the available retrieval mechanisms
* Executes those steps according to the selected search depth

Linkup is aware of its internal search and extraction tools and can be explicitly instructed to use them in a certain way through prompting (e.g., run several searches, scrape specific URLs, execute steps sequentially).

**Key implication:** Agentic search follows instructions literally. Clear and detailed prompts lead to more precise retrieval behavior, especially in `deep` search.

***

## 2. Search Depth: Standard vs. Deep

Linkup supports two search depths. You select the depth for each request, and it defines how retrieval steps are executed.

### Standard search (`depth="standard"`)

**Behavior:**

* Executes a single iteration of retrieval
* Does not reuse outputs from one step in another (e.g., an extracted URL cannot be used in a follow-up step)
* Optimizes for latency by minimizing retrieval operations
* May split a query into sub-searches only if explicitly instructed or required to answer correctly

**Best suited for:**

* Simple or direct questions
* High-volume or low-latency use cases
* Queries where the answer is likely found quickly

### Deep search (`depth="deep"`)

**Behavior:**

* Executes up to 10 iterations of retrieval (iterates until the context sufficiently answers the query)
* Each iteration is aware of the context produced by previous iterations
* If required information is missing, additional iterations may be launched with refined or adjacent queries
* Supports sequential instructions, where outputs from one step are used in the next (e.g., search first, then scrape a discovered URL)

**Best suited for:**

* Complex or multi-step queries
* Company or market research
* Cases where information is not reliably found in a single pass
* Prompts that explicitly require several searches or sequential actions

> **Rule of thumb:**
>
> * If you could answer the question with one Google search → use `standard`
> * If a human would open multiple tabs → use `deep`

### When Simple Prompts Are Enough

Not every query needs a structured prompt. If your goal is **breadth** (source coverage) rather than **precision** (specific data extraction), keep it simple.

**Research and news queries** are a good example. Users typically want search results and will handle synthesis on their end. For these, you don't need roles, extraction steps, or output formatting.

| Use case | Simple prompt                                                                                       |
| -------- | --------------------------------------------------------------------------------------------------- |
| Research | Find the latest significant research on consciousness. Run several searches with adjacent keywords. |
| News     | Find recent news about OpenAI. Run several searches with adjacent keywords.                         |
| Trends   | What are people saying about AI agents on Twitter and Reddit? Run several searches.                 |

**When to keep it simple:**

* You want many sources, not one precise answer
* You'll process/filter the results yourself
* The topic is broad or exploratory

**When to add structure:**

* You need specific data points (prices, names, dates)
* You want Linkup to scrape and extract from pages
* The output needs a defined format

### Bad vs. Good Prompts

| Bad                                                      | Good (standard)                                                                                                                                                                                                                                                       | Good (deep)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Generate a business description of linkup.so             | You are an expert company researcher. Run a web search to find what the company {company_domain} does. Then, scrape the page: {company_domain}. Only return a 3-sentence description of the company: what it does, who it serves, and its main differentiator.        | You are an expert business analyst. Your role is to generate a detailed description of the company {company_domain}. To do so you must consult: its homepage, product page, about us page, and LinkedIn profile. First, find these page URLs, then scrape each URL. Do not stop until you have scraped each URL. Return a structured company overview including: what the company does, products/services, target customers, value proposition, and founding story.                                      |
| Analyze the company website to determine its GTM motion. | You are an expert GTM analyst. Run a web search to find if {company_domain} uses self-service signup, free trials, or sales demos. Then, scrape the page: {company_domain}. Only return whether the company is PLG or SLG, with the evidence found, and nothing else. | You are an expert GTM analyst. Your objective is to determine if {company_domain} follows Product-Led Growth (PLG) or Sales-Led Growth (SLG). First, find and scrape the company's homepage, pricing page, and sign-up flow. For each page, extract evidence of: self-service signup options, free trial availability, demo request CTAs, sales contact requirements, pricing transparency. Then, based on the data collected, determine whether the company is PLG or SLG with a 3-sentence conclusion. |
| Latest research on consciousness                         | Find the latest significant research on consciousness. Run several searches with adjacent keywords.                                                                                                                                                                   | Find the latest significant research on consciousness. For each topic below, run several searches with adjacent keywords: - neuroscience of consciousness - integrated information theory - global workspace theory - AI and machine consciousness. For each publicly-available result, scrape the page to extract the full abstract or article summary.                                                                                                                                                 |

***

## 3. Anatomy of a Good Prompt

### Core Principle: Focus on Data Retrieval

If you're using Linkup, you're most likely looking for data — this is what your prompt should focus on. Answer generation should not be the objective of your prompt.

| Bad                                                          | Good                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| How to estimate the annual IT costs of the company Total SA? | You are an expert information systems consultant. Your objective is to find data that can be used to estimate the total cost of ownership (TCO) of Total SA's intranet. First, search for data that can support this estimation. Then, produce an estimate. If no information allows for a precise estimation, still produce an estimate based on the data you were able to find. |

The first prompt asks for an answer directly. The second prompt focuses on finding the data first, then using it to produce an estimate.

### The Four Components

A strong prompt usually includes:

| Component                                            | Description                                                            | Example                                                                                                                       |
| ---------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Goal**                                             | What do you want to find or understand?                                | "You are an expert business analyst. Your goal is find context to generate a detailed business description of {company_name}" |
| **Scope**                                            | Where should the system look?                                          | "The company domain is linkup.so. Analyze the homepage, about us page, and blog section."                                     |
| **Criteria / Method**                                | What type of information and analytical depth should the system apply? | "Include products, business model, target market, and value chain positioning"                                                |
| **Format (when using sourcedAnswer and Structured)** | How should the response be structured or returned?                     | "Be sharp and business oriented in your answer."                                                                              |

**Tip**: If you want us to look into specific sources, tell us! Examples include: company domains, news articles, LinkedIn URLs, etc.

### Common Mistakes

Weak prompts often:

* Are vague: "Tell me about the company" → What exactly? Revenue? Product strategy?
* Lack instructions: "Summarize this page" → How? As a bullet list? As a paragraph?
* Are unstructured: "Give me pricing, hiring plans, GTM strategy, and roadmap" → No sequence, no sources, no extraction steps. Instead, specify which pages to scrape and what data to extract from each.

***

## 4. Advanced Prompting Techniques

### Leverage the Scraper (standard and deep)

Since Linkup has a scraper as a tool, you can provide a URL and query the page in natural language. Even in `standard`, you can both scrape a page and force a web search in parallel.

**Example:**

```
Scrape the website linkup.so.
Also run a search to find articles, news, and posts mentioning linkup.so clients.
Based on the content from the website and from the search, return a list of clients that use Linkup, as well as the source of the information.
```

### Run Multiple Searches for Better Coverage (standard and deep)

If you want to optimize for source coverage (e.g., for research or news use cases), add to your prompt: "run several searches with adjacent keywords."

If you want to find several pieces of information that would be handled through separate searches, be explicit about it. Linkup can execute multiple searches even in `standard` mode.

### Use Sequential Search with LinkedIn

LinkedIn content often requires a two-step approach:

```
First find LinkedIn posts on context engineering.
Then, for each URL, extract the LinkedIn comments.
Then, return the LinkedIn profile URL of the commenters.
```

### Use Sequential Search: Search → Scrape (deep)

If what you're looking for requires you to 1) find a website URL, then 2) scrape the website, use **`deep`** and explicitly ask to "first find the URL, then scrape the URL."

This is essential for:

* Detailed answers that rely on full pages vs. search snippets
* Returning a list of precise items on a page (product characteristics, PDF links, other URLs, etc.)
* Tasks requiring prices, images, or specifications

**Example:**

```
**Your role is to** map a company's value proposition from its website.

**Inputs:**
- `{company_name}`
- `{company_website}`

**Objective:** Extract the core value proposition communicated on public-facing product pages.

**Instructions:**
- First, find and scrape the homepage and primary product pages.
- From each page, extract: headline claims, customer benefits, differentiator language, and CTAs.
- Then, synthesize the extracted data into a summary of the value proposition.
- Avoid vague marketing fluff. Focus on concrete external value claims.
```

***

## 5. Resources

### Prompt Optimizer

Get the most out of Linkup by optimizing your search prompts. Our prompt optimizer helps you craft better queries that yield more accurate and relevant results.

[**Launch Prompt Optimizer →**](https://prompt.linkup.so)

### Prompt Templates

Access our curated library of proven prompt templates for common business intelligence and research scenarios.

[**Browse Prompt Templates →**](https://prompt.linkup.so/templates)

**Template categories:**

* **Business Intelligence**: Analyze companies, competitors, and market dynamics
* **Research**: Conduct thorough investigations on specific topics
* **Competitive Analysis**: Understand positioning and strategies
* **Market Research**: Gather insights about industries and trends

### Sample Prompts for Business Intelligence

Below is a list of prompts you can leverage to extract intelligence from company websites. We have a full list [here](https://linkup-platform.notion.site/The-100-Prompts-You-Need-to-Leverage-AI-in-Your-GTM-Strategy-1cb161ecef69809593b3d2c51bbee943?pvs=74), or you can access our [Prompting Templates library](https://prompt.linkup.so/templates).

#### Map a Competitor's Value Proposition

**Your role is to** map a company's value proposition from its website.

**Inputs:**

* `{company_name}`
* `{company_website}`

**Objective:** Extract the core value proposition communicated on public-facing product pages.

**Instructions:**

* First, find and scrape the homepage and primary product pages.
* From each page, extract: headline claims, customer benefits, differentiator language, and CTAs.
* Then, synthesize the extracted data into a summary of the value proposition.
* Avoid vague marketing fluff. Focus on concrete external value claims.

#### Identify a Company's ICP

**Your role is to** determine a company's Ideal Customer Profile (ICP).

**Inputs:**

* `{company_name}`
* `{company_website}`

**Objective:** Infer the ICP based on how the company communicates publicly.

**Instructions:**

* First, find and scrape the homepage, use case pages, and 2-3 recent blog posts.
* From each page, extract: industries mentioned, company sizes referenced, job titles targeted, and pain points addressed.
* Also extract any visible customer logos.
* Then, based on the extracted data, infer the ICP (industry, company size, buyer persona, key pain points).

#### Determine if the Company Publishes a Public Roadmap

**Your role is to** check whether the company shares future product features publicly.

**Inputs:**

* `{company_website}`

**Objective:** Evaluate product transparency and customer feedback incorporation.

**Instructions:**

* First, search for "roadmap", "coming soon", or "what's next" pages on {company_website}.
* Also search for any Canny, Trello, or Notion boards linked to the company.
* For each relevant URL found, scrape the page to extract roadmap items.
* Return: roadmap URL (if found), items with their status (planned/in progress/live), and whether the roadmap is public or requires login.

***

## To Go Further

There are many ways to optimize your prompts and results with Linkup. If you'd like to discuss your use case further, please feel free to reach out to our team at [support@linkup.so](mailto:support@linkup.so) or via our Discord.

You can also [book a quick 15-minute call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9).


Built with [Mintlify](https://mintlify.com).