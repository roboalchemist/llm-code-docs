# Source: https://redocly.com/blog/updates-2025-02.md

# February 2025 updates ð

February was a **big month at Redocly** as we launched **two new products**: [**Respect**](/respect-cli) and [**Respect Monitoring**](/respect).

We also made **AI-powered search** and **Typesense search** available, enhancing documentation navigation with **faster, smarter** search capabilities.
Another **major milestone**â**theme component ejection** from **Reunite** is now **generally available**, offering even greater customization.

Beyond these key launches, weâve **continued our commitment to stability**, fixing bugs and optimizing platform performance.

Hereâs whatâs new:

## **ð AI Search**

AI search is now generally available for **Enterprise** and **Enterprise Plus** plans. This feature **enhances documentation search capabilities** by:

â Understanding **natural language queries**
â Delivering **more relevant results** in less time
â **Reducing friction** in API discovery

AI search is designed to **help developers and technical teams** find the right answers **faster**, cutting down on time spent searching through documentation.

**Want to customize AI search settings?**
You can [add your own custom prompt](/docs/realm/config/search).

Don't want it?
You can also **turn AI search off** in your `redocly.yaml` configuration:


```yaml
search:
  ai:
    hide: true
```

## â¡ Typesense Search

Weâve also introduced **Typesense search**âan alternative search engine that provides:

â Ultra-fast API documentation search
â Advanced filtering and facets
â Improved relevancy ranking

This feature is available for Enterprise and Enterprise Plus plans.

To enable it, add the following to your `redocly.yaml` file:


```yaml
search:
  engine: typesense
```

Typesense **enhances search performance** while giving teams more **control over indexing and results**.

## ð¨ Eject Components from Within Reunite

Reunite now allows users to eject theme components, enabling even deeper customization of your documentation.

Eject preview
With component ejection, you can:

- Modify UI elements without affecting core functionality
- Customize styling, layouts, and interactions
- Maintain flexibility while leveraging Redoclyâs framework


This gives teams the best of both worlds:

ð¹ The power of pre-built themes with the flexibility of custom development.

## ð® Roadmap Sneak Peek

### ð Coming this month: **Code Walkthroughs**

One of the most anticipated features is Code Walkthroughsâdesigned to help users:

â Navigate complex API integrations step by step
â Understand key implementation details with interactive guides
â Reduce friction for first-time adopters

ð Interested in early access? [Contact us](https://redocly.com/contact-us) to learn more.

### ð¯ Ready for Early Access: **API Functions and Server-Side Props**

Weâre rolling out API Functions and Server-Side Props, allowing teams to:

â Extend documentation dynamically
â Improve API-driven workflows
â Customize data retrieval strategies

Interested in trying these out? [Request access](https://redocly.com/contact-us).

### ð® Upcoming Features

- Performance enhancements â Faster response times and improved stability
- Information architecture updates â Optimized docs structure for better discoverability
- Visual API workflows builder â A new way to model API interactions


## ð Build Redocly with Us!

Weâre hiring software engineers to help shape the future of API documentation.

â Passionate about APIs?
â Excited by cutting-edge developer tools?

Join our team and be part of something big.

[Apply now â](https://redocly.com/careers#software-engineer)