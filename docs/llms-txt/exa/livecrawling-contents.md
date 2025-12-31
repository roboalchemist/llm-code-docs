# Source: https://docs.exa.ai/reference/livecrawling-contents.md

# Livecrawling Contents

***

With Exa, we can already search the web using LLMs.

However, by default, we cache all of our links to bias for the fastest response possible. You may be interested in the live version of the page, which our `livecrawl` parameter can help with.

## LiveCrawl Options

Here are all livecrawl options and their behaviors:

| Option        | Crawl Behavior   | Cache Fallback              | Best For                                               |
| ------------- | ---------------- | --------------------------- | ------------------------------------------------------ |
| `"always"`    | Always crawls    | Never falls back            | Real-time data (news, stock prices, live events)       |
| `"preferred"` | Always crawls    | Falls back on crawl failure | Production apps needing fresh content with reliability |
| `"fallback"`  | Only if no cache | Uses cache first            | Balanced speed and freshness                           |
| `"never"`     | Never crawls     | Always uses cache           | Maximum speed, historical/static content               |

## When LiveCrawl Isn't Necessary

Cached data is sufficient for many queries, especially for historical topics like "What were the major causes of World War II?" or educational content such as "How does photosynthesis work?" These subjects rarely change, so reliable cached results can provide accurate information quickly.

## Examples

### Company News

Using `"always"` ensures you get the freshest content. If you're tracking Apple's latest releases, you'll want a live view of their homepage:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://www.apple.com"],
      "livecrawl": "always"
    }'
  ```

  ```python Python theme={null}
  result = exa.get_contents(
      ["https://www.apple.com"],
      livecrawl="always"
  )
  ```

  ```typescript TypeScript theme={null}
  const result = await exa.getContents(
      ["https://www.apple.com"],
      {
          livecrawl: "always"
      }
  );
  ```
</CodeGroup>

Output without LiveCrawl: Results here are slightly dated, mentioning a fall release (later in the year)

```Shell Shell theme={null}
{
  "results": [
    {
      "id": "https://www.apple.com",
      "url": "https://www.apple.com/",
      "title": "Apple",
      "author": "",
      "text": "Apple Footer\n 1. Apple Intelligence will be available in beta on iPhone 15 Pro, iPhone 15 Pro Max, and iPad and Mac with M1 and later, with Siri and device language set to U.S. English, as part of iOS 18, iPadOS 18, and macOS Sequoia this fall.\n 2. Trade-in values will vary based on the condition, year, and configuration of your eligible trade-in device. Not all devices are eligible for credit. You must be at least 18 years old to be eligible to trade in for credit or for an Apple Gift Card. Trade-in value may be applied toward qualifying new device purchase, or added to an Apple Gift Card. Actual value awarded is based on receipt of a qualifying device matching the description provided when estimate was made. Sales tax may be assessed on full value of a new device purchase. In-store trade-in requires presentation of a valid photo ID (local law may require saving this information). Offer may not be available in all stores, and may vary between in-store and online trade-in. Some stores may have additional requirements. Apple or its trade-in partners reserve the right to refuse or limit quantity of any trade-in transaction for any reason. More details are available from Apple's trade-in partner for trade-in and recycling of eligible devices. Restrictions and limitations may apply. \nA subscription is required for Apple TV+.\nAvailable in the U.S. on apple.com, in the Apple Store app, and at Apple Stores.\nTo access and use all Apple Card features and products available only to Apple Card users, you must add Apple Card to Wallet on an iPhone or iPad that supports and has the latest version of iOS or iPadOS. Apple Card is subject to credit approval, available only for qualifying applicants in the United States, and issued by Goldman Sachs Bank USA, Salt Lake City Branch. \nIf you reside in the U.S. territories, please call Goldman Sachs at 877-255-5923 with questions about Apple Card.\nLearn more about how Apple Card applications are evaluated at support.apple.com/kb/HT209218.\n A subscription is required for Apple TV+. \n Major League Baseball trademarks and copyrights are used with permission of MLB Advanced Media, L.P. All rights reserved. \n A subscription is required for Apple Arcade, Apple Fitness+, and Apple Music. \nApple Store\n Find a Store \n Genius Bar \n Today at Apple \n Group Reservations \n Apple Camp \n Apple Store App \n Certified Refurbished \n Apple Trade In \n Financing \n Carrier Deals at Apple \n Order Status \n Shopping Help",
      "image": "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202110180743"
    }
  ],
  "requestId": "f60d0828916fb43401ed90cd3c11dd59"
}
```

Output with LiveCrawl (as at Oct 30 2024): Now we see contents talking about Apple's upcoming specific release on November 11th

```Shell Shell theme={null}
{
  "results": [
    {
      "id": "https://www.apple.com",
      "url": "https://www.apple.com",
      "title": "Apple",
      "author": "",
      "publishedDate": "2024-10-30T16:34:14.000Z",
      "text": "Apple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \nMacBook Pro\nA work of smart.\nAvailable starting 11.8\n Hello, Apple Intelligence. \nApple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \nMac mini\nSize down. Power up.\nAvailable starting 11.8\n Hello, Apple Intelligence. \nApple Intelligence is here.\nExperience it now on the latest iPhone, iPad, and Mac models with a free software update.1 \niMac\nBril l l l l liant.\nAvailable starting 11.8\n Hello, Apple Intelligence. \niPhone 16 Pro\nHello, Apple Intelligence.\niPhone 16\nHello, Apple Intelligence.\nAirPods Pro 2\nHearing Test, Hearing Aid, and Hearing Protection features in a free software update.2\n Apple Intelligence \nAI for the rest of us.\n Apple Trade In \nGet $180-$650 in credit when you trade in iPhone 12 or higher.3 \n Apple Card \nGet up to 3% Daily Cash back with every purchase.\nApple TV+\nFAM Gallery",
      "image": "https://www.apple.com/ac/structured-data/images/open_graph_logo.png?202110180743"
    }
  ],
  "requestId": "fdb7df2ef400b5994b0c5a855875cdce"
}
```

### Production Applications

Using `"preferred"` provides fresh content with fallback reliability. This is ideal for production applications:

<CodeGroup>
  ```bash cURL theme={null}
  curl -X POST 'https://api.exa.ai/contents' \
    -H 'x-api-key: YOUR-EXA-API-KEY' \
    -H 'Content-Type: application/json' \
    -d '{
      "ids": ["https://www.apple.com"],
      "livecrawl": "preferred"
    }'
  ```

  ```python Python theme={null}
  result = exa.get_contents(
      ["https://www.apple.com"],
      livecrawl="preferred"
  )
  ```

  ```typescript TypeScript theme={null}
  const result = await exa.getContents(
      ["https://www.apple.com"],
      {
          livecrawl: "preferred"
      }
  );
  ```
</CodeGroup>

This will try to get the freshest content available, but if live crawling fails (due to website downtime, network issues, etc.), it falls back to cached content instead of failing entirely. This makes it ideal for production applications.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt