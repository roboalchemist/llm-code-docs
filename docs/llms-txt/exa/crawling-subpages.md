# Source: https://docs.exa.ai/reference/crawling-subpages.md

# Crawling Subpages

***

When searching websites, you often need to explore beyond the main page to find relevant information. Exa's subpage crawling feature allows you to automatically discover and search through linked pages within a website.

## Using Subpage Crawling

Here's how to use Exa's subpage crawling feature:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://example.com"],
      "subpages": 5,
      "subpageTarget": ["about", "products"]
    }'
  ```

  ```python Python theme={null}
  results = exa.get_contents(
      ["https://example.com"], 
      subpages=5, 
      subpage_target=["about", "products"]
  )
  ```

  ```typescript TypeScript theme={null}
  const results = await exa.getContents(
      ["https://example.com"], 
      {
          subpages: 5,
          subpageTarget: ["about", "products"]
      }
  );
  ```
</CodeGroup>

This will search through up to 5 subpages of the given website, and prioritize pages that contain the terms "about" or "products" in their contents.

## Parameters

* `subpages`: Maximum number of subpages to crawl (integer)
* `subpage_target`: List of query terms to target (e.g., \["about", "products", "news"])

## Best Practices

1. **Limit Depth**: Start with a smaller `subpages` value (5-10) and increase if needed
2. **Consider Caching**: Use `livecrawl='always'` only when you need the most recent content
3. **Target Specific Sections**: Use `subpage_target` to focus on relevant sections rather than crawling the entire site

## Combining with LiveCrawl

For the most up-to-date and comprehensive results, combine subpage crawling with livecrawl:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://www.apple.com/"],
      "livecrawl": "always",
      "subpageTarget": ["news", "product"],
      "subpages": 10
    }'
  ```

  ```python Python theme={null}
  result = exa.get_contents(
      ["https://www.apple.com/"],
      livecrawl="always",
      subpage_target=["news", "product"],
      subpages=10
  )
  ```

  ```typescript TypeScript theme={null}
  const result = await exa.getContents(
      ["https://www.apple.com/"],
      {
          livecrawl: "always",
          subpageTarget: ["news", "product"],
          subpages: 10
      }
  );
  ```
</CodeGroup>

This ensures you get fresh content from all discovered subpages.

Note that regarding usage, additional subpages count as an additional piece of content retrieval for each type you specify.

## Examples

### Product Documentation

Search through documentation pages:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://exa.ai"],
      "subpages": 9,
      "subpageTarget": ["docs", "tutorial"]
    }'
  ```

  ```python Python theme={null}
  result = exa.get_contents(
      ["https://exa.ai"],
      subpages=9,
      subpage_target=["docs", "tutorial"]
  )
  ```

  ```typescript TypeScript theme={null}
  const result = await exa.getContents(
      ["https://exa.ai"],
      {
          subpages: 9,
          subpageTarget: ["docs", "tutorial"]
      }
  );
  ```
</CodeGroup>

This example crawls up to 9 subpages from the main site, prioritizing pages that contain "docs" or "tutorial" in their content.

```Shell Shell theme={null}
{
  "results": [
    {
      "id": "https://exa.ai",
      "url": "https://exa.ai/",
      "title": "Exa API",
      "author": "exa",
      "text": "AIs need powerful access to knowledge. But search engines haven't improved since 1998...",
      "image": "https://exa.imgix.net/og-image.png",
      "subpages": [
        {
          "id": "https://docs.exa.ai/reference/getting-started",
          "url": "https://docs.exa.ai/reference/getting-started",
          "title": "Getting Started",
          "author": "",
          "text": "Exa provides search for AI. Exa is a knowledge API for LLMs..."
        },
        {
          "id": "https://docs.exa.ai/reference/recent-news-summarizer",
          "url": "https://docs.exa.ai/reference/recent-news-summarizer",
          "title": "Recent News Summarizer",
          "author": null,
          "publishedDate": "2024-03-02T11:36:31.000Z",
          "text": "In this example, we will build a LLM-based news summarizer app..."
        },
        {
          "id": "https://docs.exa.ai/reference/company-analyst",
          "url": "https://docs.exa.ai/reference/company-analyst",
          "title": "Company Analyst",
          "author": null,
          "publishedDate": "2024-03-02T11:36:42.000Z",
          "text": "n this example, we&#39;ll build a company analyst tool that..."
        },
        {
          "id": "https://docs.exa.ai/reference/exa-researcher",
          "url": "https://docs.exa.ai/reference/exa-researcher",
          "title": "Exa Researcher",
          "author": null,
          "publishedDate": "2024-03-02T11:36:30.000Z",
          "text": "In this example, we will build Exa Researcher, a Javascript..."
        },
        {
          "id": "https://docs.exa.ai/reference/exa-rag",
          "url": "https://docs.exa.ai/reference/exa-rag",
          "title": "Exa RAG",
          "author": null,
          "publishedDate": "2024-03-02T11:36:43.000Z",
          "text": "LLMs are powerful because they compress large amounts of data..."
        },
        {
          "id": "https://docs.exa.ai/",
          "url": "https://docs.exa.ai/",
          "title": "Introduction",
          "author": "",
          "publishedDate": "2023-03-03T23:47:48.000Z",
          "text": "Exa is a search engine made for AIs.  \n Exa has three core..."
        },
        {
          "id": "https://exa.ai/blog/announcing-exa",
          "url": "https://exa.ai/blog/announcing-exa",
          "title": "Exa API",
          "author": "exa",
          "text": "Steps toward the mission Today, we're excited to announce...",
          "image": "https://exa.imgix.net/og-image.png"
        },
        {
          "id": "https://dashboard.exa.ai/",
          "url": "https://dashboard.exa.ai/",
          "title": "Exa API Dashboard",
          "author": "Exa",
          "publishedDate": "2012-01-06T00:00:00.000Z",
          "text": "Get started with Exa No credit card required. If you are..."
        }
      ]
    }
  ]
}
```

### News Archives

Crawl through a company's news section:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://www.apple.com/"],
      "livecrawl": "always",
      "subpageTarget": ["news", "product"],
      "subpages": 10
    }'
  ```

  ```python Python theme={null}
  result = exa.get_contents(
      ["https://www.apple.com/"],
      livecrawl="always",
      subpage_target=["news", "product"],
      subpages=10
  )
  ```

  ```typescript TypeScript theme={null}
  const result = await exa.getContents(
      ["https://www.apple.com/"],
      {
          livecrawl: "always",
          subpageTarget: ["news", "product"],
          subpages: 10
      }
  );
  ```
</CodeGroup>

Output:

```Shell Shell theme={null}
{
  "results": [
    {
      "id": "https://www.apple.com/",
      "url": "https://www.apple.com/",
      "title": "Apple",
      "author": "",
      "publishedDate": "2024-10-30T16:54:13.000Z",
      "text": "Apple Intelligence is here.\nExperience it now on the latest iPhone...",
      "image": "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202110180743",
      "subpages": [
        {
          "id": "https://www.apple.com/apple-news/",
          "url": "https://www.apple.com/apple-news/",
          "title": "Apple News+",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "Get 3 months of Apple News+ free with a new iPhone, iPad, or...",
          "image": "https://www.apple.com/v/apple-news/l/images/shared/apple-news__6xg2yiktruqy_og.png?202401091100"
        },
        {
          "id": "https://www.apple.com/us/shop/goto/store",
          "url": "https://www.apple.com/us/shop/goto/store",
          "title": "Apple Store Online",
          "author": "",
          "publishedDate": "2024-06-18T09:56:09.000Z",
          "text": "Apple Intelligence is available in beta on all iPhone 16 models...",
          "image": "https://as-images.apple.com/is/og-default?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1525370171638"
        },
        {
          "id": "https://www.apple.com/mac/",
          "url": "https://www.apple.com/mac/",
          "title": "Mac",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "Answer calls or messages from your iPhone directly on your Mac...",
          "image": "https://www.apple.com/v/mac/home/cb/images/meta/mac__c3zv0c86zu0y_og.png?202410291046"
        },
        {
          "id": "https://www.apple.com/ipad/",
          "url": "https://www.apple.com/ipad/",
          "title": "iPad",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "Get 3% Daily Cash back with Apple Card. And pay for your new iPad...",
          "image": "https://www.apple.com/v/ipad/home/cm/images/meta/ipad__f350v51yy3am_og.png?202410241440"
        },
        {
          "id": "https://www.apple.com/iphone/",
          "url": "https://www.apple.com/iphone/",
          "title": "iPhone",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "Get credit toward iPhone 16 or iPhone 16 Pro when you trade...",
          "image": "https://www.apple.com/v/iphone/home/bx/images/meta/iphone__kqge21l9n26q_og.png?202410241440"
        },
        {
          "id": "https://www.apple.com/watch/",
          "url": "https://www.apple.com/watch/",
          "title": "Apple Watch",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "Combining Apple Watch and iPhone opens up a world of features...",
          "image": "https://www.apple.com/v/watch/bo/images/meta/apple-watch__f6h72tjlgx26_og.png?202410031527"
        },
        {
          "id": "https://www.apple.com/apple-vision-pro/",
          "url": "https://www.apple.com/apple-vision-pro/",
          "title": "Apple Vision Pro",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "Apple Vision Pro seamlessly blends digital content with your...",
          "image": "https://www.apple.com/v/apple-vision-pro/e/images/meta/apple-vision-pro-us__f28gp8ey4vam_og.png?202409261242"
        },
        {
          "id": "https://www.apple.com/airpods/",
          "url": "https://www.apple.com/airpods/",
          "title": "AirPods",
          "author": "",
          "publishedDate": "2024-09-27T17:22:17.000Z",
          "text": "AirPods Pro 2 now feature a scientifically validated Hearing...",
          "image": "https://www.apple.com/v/airpods/x/images/meta/airpods__dh7xkbort402_og.png?202410241631"
        },
        {
          "id": "https://www.apple.com/tv-home/",
          "url": "https://www.apple.com/tv-home/",
          "title": "TV & Home",
          "author": "",
          "publishedDate": "2024-05-07T20:24:00.000Z",
          "text": "The future hits home.\nSimply connect your favorite devices...",
          "image": "https://www.apple.com/v/tv-home/n/images/meta/tv-home__fedwm0ly3mqi_og.png?202409151638"
        }
      ]
    }
  ],
  "requestId": "17e8a79ff11bcb73115ef3efcb8e0457"
}
```

### Blog Content

Gather recent blog posts:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://medium.com"],
      "subpages": 5,
      "subpageTarget": ["blog", "articles"],
      "livecrawl": "always"
    }'
  ```

  ```python Python theme={null}
  results = exa.get_contents(
      ["https://medium.com"],
      subpages=5,
      subpage_target=["blog", "articles"],
      livecrawl='always'
  )
  ```

  ```typescript TypeScript theme={null}
  const results = await exa.getContents(
      ["https://medium.com"],
      {
          subpages: 5,
          subpageTarget: ["blog", "articles"],
          livecrawl: "always"
      }
  );
  ```
</CodeGroup>

Output:

```Shell Shell theme={null}
{
	"results": [
		{
			"id": "https://medium.com",
			"title": "Medium: Read and write stories.",
			"url": "https://medium.com",
			"publishedDate": "2025-08-12T20:25:00.000Z",
			"author": "",
			"text": "[Sitemap](https://medium.com/sitemap/sitemap.xml)\n\n[Medium Logo](https://medium.com/)...",
			"image": "https://miro.medium.com/v2/da:true/167cff2a3d17ac1e64d0762539978f2d54c0058886e8b3c8a03a725a83012ec0",
			"favicon": "https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19",
			"subpages": [
				{
					"id": "https://blog.medium.com",
					"title": "The Medium Blog",
					"url": "https://blog.medium.com",
					"publishedDate": "2025-08-12T20:25:00.000Z",
					"author": "",
					"text": "[Sitemap](https://blog.medium.com/sitemap/sitemap.xml)...",
					"image": "https://miro.medium.com/v2/resize:fit:1024/1*7eq6Xl7nRYU77U7IPYvoDg.jpeg",
					"favicon": "https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19"
				},
				{
					"id": "https://medium.com/",
					"title": "Medium: Read and write stories.",
					"url": "https://medium.com/",
					"publishedDate": "2025-08-12T20:25:00.000Z",
					"author": "",
					"text": "[Sitemap](https://medium.com/sitemap/sitemap.xml)...",
					"image": "https://miro.medium.com/v2/da:true/167cff2a3d17ac1e64d0762539978f2d54c0058886e8b3c8a03a725a83012ec0",
					"favicon": "https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19"
				},
				{
					"id": "https://medium.com/about?autoplay=1",
					"title": "About Medium",
					"url": "https://medium.com/about?autoplay=1",
					"publishedDate": "2025-08-12T20:25:00.000Z",
					"author": "",
					"text": "[Sitemap](https://medium.com/sitemap/sitemap.xml)...",
					"image": "https://miro.medium.com/v2/da:true/167cff2a3d17ac1e64d0762539978f2d54c0058886e8b3c8a03a725a83012ec0",
					"favicon": "https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19"
				},
				{
					"id": "https://medium.com/membership",
					"title": "Medium Membership",
					"url": "https://medium.com/membership",
					"publishedDate": "2025-08-12T20:25:00.000Z",
					"author": "",
					"text": "[Sitemap](https://medium.com/sitemap/sitemap.xml)...",
					"image": "https://miro.medium.com/v2/da:true/167cff2a3d17ac1e64d0762539978f2d54c0058886e8b3c8a03a725a83012ec0",
					"favicon": "https://miro.medium.com/v2/5d8de952517e8160e40ef9841c781cdc14a5db313057fa3c3de41c6f5b494b19"
				}
			]
		}
	],
  "requestId": "20163fc78142a5ff69c6959167417f1f"
}
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt