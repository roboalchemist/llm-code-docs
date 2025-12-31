# Source: https://docs.warp.dev/university/mcp-servers/puppeteer-mcp-scraping-amazon-web-reviews.md

# Puppeteer MCP: Scraping Amazon Web Reviews&#x20;

{% hint style="info" %}
This tutorial demonstrates how to configure and use the **Puppeteer MCP server** inside Warp to scrape Amazon web reviews.
{% endhint %}

{% embed url="<https://youtu.be/rrxfS9u1XRA?si=Bzaxm6Qb00okv03t&t=134>" %}

***

### 🧠 Overview

**Puppeteer MCP** integrates Warp’s agents with the browser, letting you automate tasks such as navigation, form filling, screenshotting, and scraping content.\
\
Once configured, Warp can issue Puppeteer commands directly from prompts, enabling full **browser automation** without manual scripting.

You’ll learn how to:

* Set up the Puppeteer MCP server.
* Use Warp’s voice input and AI to describe automation tasks.
* Execute browser workflows hands-free.
* Capture, scrape, and analyze web data programmatically.

***

{% stepper %}
{% step %}

### Configure the Puppeteer MCP Server

Open the MCP panel in Warp:

* Press **Cmd + Shift + P** (Mac) or **Ctrl + Shift + P** (Windows/Linux) to open the **Command Palette**.
* Search for `MCP` and open the **MCP Panel**.

Add the Puppeteer MCP config:

* Click **Add**, then paste in the provided JSON configuration for Puppeteer:

{% code title="puppeteer-mcp-config.json" %}

```json
{
  "puppeteer": {
    "command": "npx",
    "args": [
      "-y",
      "@modelcontextprotocol/server-puppeteer"
    ],
    "env": {},
    "working_directory": null
  }
}
```

{% endcode %}

Save your configuration. Available endpoints will include:

* `puppeteer.navigate`
* `puppeteer.fill`
* `puppeteer.screenshot`
* `puppeteer.evaluate`

&#x20;These represent actions Warp can call automatically through its AI agent.
{% endstep %}

{% step %}

### Use Voice Input to Trigger Automation

Enable **voice input** by clicking the microphone icon in Warp. Then speak your automation prompt naturally.

```
Can you go to Amazon search for "white t-short women?"

Scrape the results so the titles, prices, and links are extracted.
Then open each product link and summarize the product reviews.
Finally, give me a recommendation for which shirt to buy based on the combination of the pricing and review quality.
```

### Watch Puppeteer Automate the Workflow

Behind the scenes, Puppeteer:

* Navigates to Amazon.
* Fills the search bar with “white t-shirt woman.”
* Scrapes the product results — capturing titles, prices, and product links.
* Clicks into each product and extracts review data using JavaScript selectors.
* Takes screenshots of the pages for reference.

You can see the browser (Amazon) and Warp side-by-side as Puppeteer performs these steps autonomously.

{% hint style="info" %}
Puppeteer runs fully headless or in visible browser mode — you don’t need to touch your mouse or keyboard.
{% endhint %}

### Analyze and Summarize Results

Once the scrape is complete, Warp compiles the data and provides a ranked list of products. Example output (from transcript):

| Product          | Price | Rating | Summary               |
| ---------------- | ----- | ------ | --------------------- |
| Cozy T-Shirt     | $8    | ⭐ 4.5  | Soft fabric, good fit |
| Comfy Cotton Tee | $10   | ⭐ 4.2  | Slightly looser fit   |
| Basic White Top  | $6    | ⭐ 3.8  | Mixed quality reviews |

Warp’s recommendation:

> “The Cozy T‑Shirt — $8, 4.5 stars, good fit, and soft fabric.”

### Apply Puppeteer MCP to Other Scenarios

The same setup works for:

* Product research – Compare reviews or specs across multiple sites.
* Competitive analysis – Scrape competitors’ pricing or product data.
* Web testing – Automate user flows like login or checkout.
* Repetitive data tasks – Periodic scraping or screenshot capture.

{% hint style="success" %}
Puppeteer MCP lets Warp act like your hands in the browser — navigating, scraping, and summarizing data while you focus on analysis.
{% endhint %}
{% endstep %}
{% endstepper %}
