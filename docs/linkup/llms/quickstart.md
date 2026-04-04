# Source: https://docs.linkup.so/pages/documentation/get-started/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Quickstart

> Integrate with Linkup in 5 minutes

The Linkup API can be used in AI workflows to find and access high quality content from the internet. You can follow the steps below to integrate Linkup easily.

1. Get your API key for free

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

2. Install the Linkup SDK

<CodeGroup>
  ```python python theme={null}
  pip install linkup-sdk
  ```

  ```js js theme={null}
  npm i linkup-sdk
  ```
</CodeGroup>

3. Call the Search API to retrieve context. This enables you to RAG the internet. Linkup will return the context you need to ground your LLM's answer.

<CodeGroup>
  ```python python theme={null}
  from linkup import LinkupClient

  client = LinkupClient(api_key="<YOUR_LINKUP_API_KEY>")

  response = client.search(
      query="What is Microsoft's 2024 revenue?",
      depth="deep",
      output_type="sourcedAnswer"
  )

  print(response)
  ```

  ```js js theme={null}
  import { LinkupClient } from 'linkup-sdk';

  const client = new LinkupClient({
    apiKey: '<YOUR API KEY>',
  });

  const askLinkup = async () => {
    return await client.search({
      query: "What is Microsoft's 2024 revenue?",
      depth: 'deep',
      outputType: 'sourcedAnswer',
    });
  };

  askLinkup().then(console.log);
  ```

  ```shell curl theme={null}
  curl "https://api.linkup.so/v1/search" \
      -G \
      -H "Authorization: Bearer $LINKUP_API_KEY" \
      --data-urlencode "q=What is Microsoft's 2024 revenue?" \
      --data-urlencode "depth=deep" \
      --data-urlencode "outputType=sourcedAnswer"
  ```
</CodeGroup>

Response:

<CodeGroup>
  ```json 200 [expandable] theme={null}
  {
      "answer": "Microsoft's revenue for fiscal year 2024 was $245.1 billion, reflecting a 16% increase from the previous year.",
      "sources": [
          {
              "name": "Microsoft 2024 Annual Report",
              "url": "https://www.microsoft.com/investor/reports/ar24/index.html",
              "snippet": "Highlights from fiscal year 2024 compared with fiscal year 2023 included: Microsoft Cloud revenue increased 23% to $137.4 billion.\nMore broadly, we continued to see sustained revenue growth from migrations as customers turn to Azure. Azure Arc is helping customers streamline their transition, as they secure, develop, and operate workloads with Azure services anywhere. We have 36,000 Arc customers, up 90 percent year-over-year.\nWith our acquisition of Activision Blizzard King, which closed October 2023, we’ve added hundreds of millions of players to our ecosystem. We now have 20 franchises that have generated over $1 billion in lifetime revenue—from Candy Crush, Diablo, and Halo, to Warcraft, Elder Scrolls, and Gears of War.\nGrowth depends on our ability to reach new users in new markets such as frontline workers, small and medium businesses, and growth markets, as well as add value to our core product and service offerings to span AI and productivity categories such as communication, collaboration, analytics, security, and compliance. Office Commercial revenue is mainly affected by a combination of continued installed base growth and average revenue per user expansion, as well as the continued shift from Office licensed on-premises to Office 365.\nGrowth depends on our ability to reach new users, add value to our core product set with new features including AI tools, and continue to expand our product and service offerings into new markets. Office Consumer revenue is mainly affected by the percentage of customers that buy Office with their new devices and the continued shift from Office licensed on-premises to Microsoft 365 Consumer subscriptions.",
              "favicon": "https://www.microsoft.com/favicon.ico"
          },
          {
              "name": "Microsoft's Financial Results in FY24 Q4 – AGOLUTION",
              "url": "https://agolution.com/en/microsoft/financial-reporting/2024-q4/",
              "snippet": "What did the other quarterly figures look like and how did Microsoft fare in fiscal year 2024 as a whole? Microsoft’s revenue amounted to $64.7 billion - and increased by 15%.\nWhat did the other quarterly figures look like and how did Microsoft fare in fiscal year 2024 as a whole? Microsoft’s revenue amounted to $64.7 billion - and increased by 15%.\nThe Xbox and Gaming segment recorded a remarkable jump in revenue of 61%, with the majority of this increase being due to the acquisition of Activision Blizzard King by Microsoft at the end of last year. Since then, Microsoft has owned popular video games such as “Call of Duty”, “Overwatch” and “Candy Crush”. The results for Microsoft’s fiscal year 2024 as compared to fiscal year 2023 were as follows.\nMicrosoft achieved total revenue of $245.1 billion, an increase of 16%. The operating income amounted to $109.4 billion and increased by 24%. Total net income amounted to $88.1 billion and increased by 22%. Earnings per share amounted to $11.8 - here too there was an increase of 22%. Solid fiscal year 2024: Microsoft remains one of the market leaders in the era of AI.\nThe third quarter of Microsoft’s 2024 fiscal year was again characterized by strong cloud results.",
              "favicon": "https://agolution.com/favicon.ico"
          },
          {
              "name": "Microsoft Revenue 2010-2024 | MSFT | MacroTrends",
              "url": "https://www.macrotrends.net/stocks/charts/MSFT/microsoft/revenue",
              "snippet": "Microsoft revenue for the quarter ending December 31, 2024 was $69.632B, a 12.27% increase year-over-year.\nMicrosoft annual/quarterly revenue history and growth rate from 2010 to 2024. Revenue can be defined as the amount of money a company receives from its customers in exchange for the sales of goods or services. Revenue is the top line item on an income statement from which all costs and expenses are subtracted to arrive at net income.\nMicrosoft revenue for the quarter ending December 31, 2024 was $69.632B, a 12.27% increase year-over-year.\nMicrosoft annual revenue for 2023 was $211.915B, a 6.88% increase from 2022. Microsoft annual revenue for 2022 was $198.27B, a 17.96% increase from 2021.",
              "favicon": "https://www.macrotrends.net/favicon.ico"
          },
          ...
      ]
  }
  ```
</CodeGroup>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>

<Card title="Best Practice" icon="link" href="https://docs.linkup.so/pages/documentation/tutorials/prompting" cta="Read our Prompting Guide here">
  The more precise and detailed your prompts, the better the results.
</Card>


Built with [Mintlify](https://mintlify.com).