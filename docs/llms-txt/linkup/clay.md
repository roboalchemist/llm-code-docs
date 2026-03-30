# Source: https://docs.linkup.so/pages/integrations/clay/clay.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Clay

> Enrich Companies in Clay using Linkup Web Search

## Overview

You can connect a [Clay](https://clay.com) table to web search through Linkup, which can be used as an enrichment provider to get contextual information from the internet for your prospects and leads.

Below is a short Youtube Tutorial:

<iframe width="100%" height="400" style={{ maxWidth: '1072px', width: '100%', display: 'block', margin: '0 auto', borderRadius: '12px' }} src="https://www.youtube.com/embed/NbLsyvJ8rVY?si=ddvKnRuO2raek2Ti" title="Install Linkup on Google Sheets" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />

## Installation

### 1. Open Clay

Go to your Clay account and navigate to the table you would like to enrich.

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay1.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=b563c7a998989d841d530b073db8d008" alt="Clay" width="3024" height="1656" data-path="pages/integrations/clay/assets/clay1.png" />

### 2. Add HTTP API Enrichment

Click on "Add enrichment" and search for HTTP API.

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay2.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=7134770ff484fa699ba108c84ddde5a7" alt="Clay" width="3024" height="1648" data-path="pages/integrations/clay/assets/clay2.png" />
<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay3.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=18bb6349d74d47ca4bb5ae685bb212d7" alt="Clay" width="3024" height="1646" data-path="pages/integrations/clay/assets/clay3.png" />

### 3. Configure the HTTP API to call the Linkup API

After clicking on HTTP API, you will see the configuration sidebar opening.

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay4.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=089719cfc89b2e758e5ce4c83a5ac915" alt="Clay" width="3024" height="1648" data-path="pages/integrations/clay/assets/clay4.png" />

There are a few things we'll need to configure:

* **Endpoint & Header** (think of it as the address and name you would put on an envelope)
* **Body** (the actual content of the letter)

Let's first configure the *HTTP API (Headers) account* - this is how Linkup will authenticate you. In the *Account* section, select "Add account". You will see a box popping up, where you need to add two key/value pairs:

* `Authorization` / `Bearer {your API key}`
* `Content-Type` / `application/json`

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay5.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=d3d3f6f1dee70a40801a0d598831b988" alt="Clay" width="1182" height="950" data-path="pages/integrations/clay/assets/clay5.png" />

Once this is done, we'll configure the Method, Endpoint and Body.

To find the endpoint, head over to the [API Reference](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-search). You'll see the endpoint url is `https://api.linkup.so/v1/search`, using a the *POST* Method.

Then for the Body, you need to send the query parameters of the API (see the [API Reference](https://docs.linkup.so/pages/documentation/api-reference/endpoint/post-search) for more details on output type, filters, and depth).

You can copy the configuration below, replacing "q" with your actual query:

```json  theme={null}
{
  "q": "your search query here",
  "outputType": "sourcedAnswer",
  "depth": "standard"
}
```

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay6.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=28c114a6c229970be2b7fc45374703d7" alt="Clay" width="994" height="1574" data-path="pages/integrations/clay/assets/clay6.png" />

### 4. Call the API and create a new column for the results

You can then save and run the column directly from the table.

**Important**: This column will not get you the enriched data directly, but shows the API response. You need to open the API response and create a new column based on the field "answer", which is included in the response.

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay9.1.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=8074f6bad3e3bd6bf0888c8f14abec6d" alt="Clay" width="3024" height="1244" data-path="pages/integrations/clay/assets/clay9.1.png" />

You now have your enrichment working!

### 5. Save the enrichment as a template and reuse it with different queries

If you open the configuration panel of the HTTP API call, you can save the parameters as a new template, and then re-use this template in new columns. All you will have to change is your query.

<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay10.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=56bb571f71bca9cedd82dd1bf73caebe" alt="Clay" width="3024" height="1646" data-path="pages/integrations/clay/assets/clay10.png" />\
<img src="https://mintcdn.com/linkup-8b5c238e/eJ8cJjJOf3NSdL-t/pages/integrations/clay/assets/clay11.png?fit=max&auto=format&n=eJ8cJjJOf3NSdL-t&q=85&s=f7efa5db37f7e16d622fd60dad82c1a3" alt="Clay" width="3024" height="1644" data-path="pages/integrations/clay/assets/clay11.png" />

## Use Cases

**Company Intelligence & Research**

* Research any company based on its website or public information
* Find detailed information about customers, job positions, office locations
* Discover funding stages, technology stacks, and SOC-II compliance status
* Analyze competitive landscape and market positioning

**Lead Qualification & Scoring**

* Automate the research process to identify highly-qualified leads
* Gather contextual information that helps prioritize prospects
* Filter leads based on your ideal customer profile (ICP) criteria

**Sales Intelligence & Pre-call Research**

* Automatically gather facts about companies and contacts before sales calls
* Replace manual Googling with automated research
* Create more confident, relevant conversations with prospects

**Account-Based Marketing (ABM) Research**

* Find companies of particular sizes that use specific technologies
* Identify prospects that aren't in your CRM yet
* Expand your total addressable market (TAM) with targeted research

**Contact & Email Discovery**

* Obtain valid email addresses and contact information
* Research across various platforms and public sources
* Automate contact discovery in one streamlined process

**Competitor Analysis & Market Research**

* Analyze competitors and their market positioning
* Research industry trends and market opportunities
* Gather intelligence to inform your sales strategy

**Signal & Trigger Detection**

* Track key customer events and buying signals
* Monitor company changes like hiring sprees or funding announcements
* Identify technology adoptions that indicate sales opportunities

**Customer Success & Expansion Research**

* Research existing customers to identify expansion opportunities
* Analyze renewal risks and success patterns
* Monitor public activities and business changes for upsell signals

You are all set to use Linkup in your Clay workflows! Visit the [Concepts](/pages/documentation/get-started/concepts) page to learn more about the different Linkup parameters.

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).