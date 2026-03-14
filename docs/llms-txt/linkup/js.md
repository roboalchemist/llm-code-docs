# Source: https://docs.linkup.so/pages/sdk/js/js.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Typescript SDK

> How to use Linkup Javascript SDK natively in your apps.

## Introduction

The Typescript SDK allows for easy interaction with the Linkup API, offering the full range of our search functionality. Easily integrate smart search capabilities into your applications, harnessing Linkup’s powerful search features.
You can use our [playground](https://app.linkup.so/playground) to have interactive examples and see how to implement them with the SDK.

<CardGroup cols={2}>
  <Card title="Github" icon="github" href="https://github.com/LinkupPlatform/linkup-js-sdk">
    Repository (feel free to contribute)
  </Card>

  <Card title="NPM" icon="npm" href="https://www.npmjs.com/package/linkup-sdk">
    NPM page
  </Card>
</CardGroup>

## Quickstart

Get started with our Typescript SDK in less than 5 minutes!

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

## Installation

You can install the Linkup Typescript SDK using the following:

```shell  theme={null}
npm i linkup-sdk
```

## Usage

Here is a basic usage showing how to use the Linkup SDK:

```typescript  theme={null}
import { LinkupClient } from "linkup-sdk";

const client = new LinkupClient({
	apiKey: "<YOUR API KEY>",
});

const askLinkup = async () => {
	return await client.search({
		query: "Can you tell me which women were awarded the Physics Nobel Prize",
		depth: "standard",
		outputType: "sourcedAnswer",
	});
};

askLinkup().then(console.log);
```

## Input Parameters

| Parameter              | Type      | Description                                                                                        | Default   |
| ---------------------- | --------- | -------------------------------------------------------------------------------------------------- | --------- |
| query                  | str       | The input query string                                                                             | Required  |
| depth                  | string    | Type of search to perform "standard" or "deep"                                                     | Required  |
| outputType             | string    | Linkup response type, can be "sourcedAnswer", "searchResults", "structuredOutput"                  | Required  |
| structuredOutputSchema | string    | The returned schema from the Linkup API. It should be used only if the outputType is 'structured'. | undefined |
| includeImages          | boolean   | To also return images                                                                              | undefined |
| fromDate               | date      | From date to search                                                                                | undefined |
| toDate                 | date      | To date to search                                                                                  | undefined |
| includeDomains         | string\[] | To include domain(s)                                                                               | undefined |
| excludeDomains         | string\[] | To exclude domain(s)                                                                               | undefined |
| includeInlineCitations | boolean   | To include inline citations in the answer, if `outputType` is `sourcedAnswer`                      | undefined |
| includeSources         | boolean   | To include the sources, if `outputType` is `structured` (modifies the schema of the output)        | undefined |
| maxResults             | number    | Maximum number of results to return                                                                | undefined |

### Query

The `query` parameter is the core input string that defines your search intent. It represents the question or information request that you want Linkup to answer. How you formulate this query significantly impacts the quality and relevance of results.

Effective queries should be:

* **Clear and specific**: "What were the key findings of NASA's James Webb telescope in 2023?" provides better results than "Tell me about space discoveries"
* **Contextually rich**: Include relevant context when needed ("What are the environmental impacts of lithium mining for EV batteries?")
* **Naturally phrased**: Write as you would ask a knowledgeable person, not with keywords

For optimal results, consider reviewing our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide), which provides detailed strategies for crafting effective queries.

### Depth

The `depth` field is used to select the type of search you want to perform:

* **standard**: the search will be straightforward and fast, suited for relatively simple queries (e.g. "What's the weather in Paris today?")
* **depth**: the search will use an agentic workflow, which makes it in general slower, but it will be able to solve more complex queries (e.g. "What is the company profile of LangChain accross the last few years, and how does it compare to its concurrents?")

### Output type

The type of output which is expected:

* **sourcedAnswer**: Provides a comprehensive natural language answer to the query along with citations to the source material. Ideal for when you need well-formed responses with verifiable information and transparent sourcing.
* **searchResults**: Returns the raw search context data without synthesis, giving you direct access to the underlying information. Useful for custom processing, or when you need to implement your own answer generation logic.
* **structured**: Allows you to receive responses in a custom format based on the format provided in
  `structuredOutputSchema`. If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

### Structured output schema

Linkup’s structured output feature allows you to receive responses in a custom format that you define. This is particularly useful when you need to integrate Linkup’s responses directly into your application’s data structure or when you want to ensure consistency in the response format.
To do that, you have to use the `structuredOutputSchema` field.
If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

### Include images

The `includeImages` parameter allows you to receive image results alongside text results in your search responses. When set to `true`, Linkup will return relevant images related to your query, each with a URL and metadata. This is particularly useful for:

* Creating visual search experiences
* Building content that combines text and images
* Researching topics where visual information is important

Image results are returned with the same structure as text results but with `type: "image"`.

### fromDate

The `fromDate` parameter filters search results to only include content published after the specified date. This helps you:

* Focus on recent information
* Exclude outdated content

The date should be a Date type, for example: `new Date("2024-01-01")`.

### toDate

The `toDate` parameter complements `fromDate` by restricting search results to only include content published or updated before the specified date. This is useful for:

* Historical research on specific time periods
* Analyzing content published within a specific date range
* Avoiding more recent information that might skew results

Like `fromDate`, the date should be a Date type, for example: `new Date("2024-12-31")`.

When used together, `fromDate` and `toDate` create a date range filter for your search results.

### includeDomains

The `includeDomains` parameter allows you to specify a list of domains that must be included in the search results. This is useful for:

* focus on specific sources
* ensure that results come from trusted domains.

### excludeDomains

The `excludeDomains` parameter allows you to specify a list of domains that should be excluded from the search results. This is useful for:

* Filtering out unwanted sources
* Avoiding results from specific domains that may not be relevant or trustworthy.

### includeInlineCitations

The `includeInlineCitations` parameter is specifically designed for use with the `sourcedAnswer` output type. When enabled, it embeds citations directly within the answer text, making it easier to identify which parts of the response correspond to specific sources. This is particularly useful for:

* Academic or research applications where source attribution is critical
* Creating content that needs verifiable claims with clear sourcing
* Building applications where users need to quickly verify information

When `includeInlineCitations` is set to `true`, the answer will contain inline references like \[1], \[2] that correspond to the sources in the response.

### includeSources

The `includeSources` parameter is specifically designed for use with the `structured` output type. When enabled, it modifies the schema of the structured response to include source information alongside your custom data structure. This is particularly useful for:

* Applications that need both structured data and source attribution
* Building systems that require traceability of information
* Creating responses where you want to maintain both custom format and source verification

When `includeSources` is set to `true`, the response will have a `data` property and a `sources` property.

### maxResults

The `maxResults` parameter allows you to specify the maximum number of results to return. This is useful for:

* Limiting the number of results returned
* Reducing the context size

## Examples

<AccordionGroup>
  <Accordion title="Last Formula 1 race" description="Standard example" icon="flag">
    <p>This example show you how to combine the standard search with a sourced answer</p>

    ```typescript  theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getRaceResume = async () => {
      return await client.search({
        query:"Can you resume me the last Formula 1 race ?",
        depth:"standard",
        outputType:"sourcedAnswer",
      });
    };

    getRaceResume().then(console.log);
    ```

    Example response:

    ```json  theme={null}
    {
      "answer": "Lando Norris won the 2025 Australian Grand Prix, the season opener, in challenging wet conditions. The race saw multiple incidents, including crashes on the first lap, leading to six drivers not finishing. Notably, Lewis Hamilton finished in 10th place. The race was marked by dramatic weather changes that affected many competitors. For more details, you can read the full results [here](https://www.motorsportweek.com/2025/03/16/f1-2025-australian-grand-prix-race-results/).",
      "sources": [
        {
          "name": "F1 2025 Australian Grand Prix – Race Results",
          "url": "https://www.motorsportweek.com/2025/03/16/f1-2025-australian-grand-prix-race-results/",
          "snippet": "McLaren's Lando Norris has won the Formula 1 season-opening Australian Grand Prix in a mixed conditions thriller at the Albert",
          "favicon": "https://www.motorsportweek.com/wp-content/uploads/2020/04/cropped-favicon-32x32.png"
        },
        {
          "name": "McLaren’s Lando Norris wins wet and wild Australian Grand Prix. Hamilton finishes 10th",
          "url": "https://www.msn.com/en-us/sports/other/mclarens-lando-norris-wins-wet-and-wild-australian-grand-prix-hamilton-finishes-10th/ar-AA1B0kIf",
          "snippet": "The Melbourne race had a thrilling start with Racing Bull’s Isack Hadjar out on the formation lap, and Alpine’s Jack Doohan and Williams’ Carlos Sainz crashing out on the opening lap.",
          "favicon": "https://static.msn.com/en-us/entertainment/favicon.ico"
        },
        {
          "name": "F1 Australian Grand Prix 2025 results: Norris wins, rookies spin out in the rain",
          "url": "https://www.msn.com/en-us/sports/other/f1-australian-grand-prix-2025-results-norris-wins-rookies-spin-out-in-the-rain/ar-AA1B4irD",
          "snippet": "If you like drama in racing, the 2025 F1 Australian Grand Prix didn’t disappoint. Intermittent rain caused havoc on the track, and six drivers didn’t complete the 57 laps, including four of this year’s full-season rookies.",
          "favicon": "https://static.msn.com/en-us/entertainment/favicon.ico"
        },
        ...
      ]
    }
    ```
  </Accordion>

  <Accordion title="Company Revenue" description="Deep + structured output" icon="building">
    <p>This example shows you how to use the deep with a relative complexe structured output:</p>

    ```typescript  theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const schema = {
      "type": "object",
      "properties": {
        "companyName": {
          "type": "string",
          "description": "The name of the company"
        },
        "revenueAmount": {
          "type": "number",
          "description": "The revenue amount"
        },
        "fiscalYear": {
          "type": "string",
          "description": "The fiscal year for this revenue"
        }
      }
    };

    const getCompanyRevenue = async () => {
      return await client.search({
        query: "What is Microsoft's 2024 revenue?",
        depth: 'deep',
        outputType: 'structured',
        structuredOutputSchema: schema
      });
    };

    getCompanyRevenue().then(console.log);
    ```

    Example response:

    ```json  theme={null}
    {
        "companyName": "Microsoft",
        "revenueAmount": 245100000000,
        "fiscalYear": "2024"
    }
    ```
  </Accordion>

  <Accordion title="Latest politic news" description="Search results as outputType" icon="newspaper">
    <p>This example shows you how to use the standard with a search results:</p>

    ```typescript  theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getNews = async () => {
      return await client.search({
        query: "Latest politic news",
        depth: 'standard',
        outputType: 'searchResults'
      });
    };

    getNews().then(console.log);
    ```

    Example response:

    ```json  theme={null}
    {
      "results": [
        {
          "type": "text",
          "name": "‘I’m Still Here’ invites reflection on world politics, history",
          "url": "https://www.thepostathens.com/article/2025/03/im-still-here-movie-review",
          "content": "For “I’m Still Here,” viewers do not walk away with the same feeling. It begins with excitement and energy but ends feeling empty and reflective. It is a movie about memory and the ability to keep the ones we’ve lost alive in our psyches.",
          "favicon": "https://www.thepostathens.com/favicon.ico"
        },
        {
          "type": "text",
          "name": "Local Politics",
          "url": "https://www.seattletimes.com/seattle-news/politics/",
          "content": "House Bill 1175 would have required cities across Washington to allow cafes and stores in all residential areas, superseding any local zoning restrictions. Initiative 2081, signed by over 448,000 ...",
          "favicon": "https://www.seattletimes.com/favicon.ico"
        },
        {
          "type": "text",
          "name": "Spruce Creeker allegedly points gun at fellow resident over politics",
          "url": "https://www.villages-news.com/2025/03/17/spruce-creeker-allegedly-points-gun-at-fellow-resident-over-politics/",
          "content": "A resident of the Spruce Creek Del Webb community in Summerfield was arrested after he allegedly pointed a gun at a fellow resident over politics.",
          "favicon": "https://www.villages-news.com/wp-content/uploads/2019/06/cropped-villages-news-favicon-32x32.png"
        },
        ...
      ]
    }
    ```
  </Accordion>

  <Accordion title="Amazon deforestation" description="IncludeImages filter" icon="trees">
    <p>This example return text and images sources</p>

    ```typescript  theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getData = async () => {
      return await client.search({
        query: "Amazon deforestation",
        depth: 'standard',
        outputType: 'searchResults',
        includeImages: true
      });
    };

    getData().then(console.log);
    ```

    Exemple response

    ```json  theme={null}
    {
      "results":
        [
          {"type":"text","name":"The rough road to sustainable farming in an Amazon deforestation hotspot","url":"https://www.msn.com/en-us/society-culture-and-history/social-issues/the-rough-road-to-sustainable-farming-in-an-amazon-deforestation-hotspot/ar-AA1B64yY","content":"Bartolomeu Moraes, better known as Brasília, was a peasant leader and trade unionist in Brazil involved in a long, bloody land war. In 2002, he was killed after years of opposing powerful local ranchers along the BR-163 highway area,", "favicon":"https://static.msn.com/en-us/entertainment/favicon.ico"},
          {"type":"text","name":"Forest management ambitions in Brazilian Amazon aim to make up for lost time","url":"https://www.msn.com/en-us/news/world/forest-management-ambitions-in-brazilian-amazon-aim-to-make-up-for-lost-time/ar-AA1ALyxz","content":"In the early 2000s, deforestation levels in the Brazilian Amazon rose so tremendously that, faced with both national and international pressure, the federal government decided to implement forest timber management as a way to curb the destruction.", "favicon":"https://static.msn.com/en-us/entertainment/favicon.ico"},
          {"type":"text","name":"Race to save the rainforest: Why replacing cocaine barons with cattle ranchers is destroying the Amazon","url":"https://www.telegraph.co.uk/news/amazon-deforestation-in-colombia/","content":"Though the Amazon rainforest proved a useful screen ... Should the recent rates of deforestation continue, experts warn, the implications will prove devastating for us all. Marisela Silva Parra ...", "favicon":"https://www.telegraph.co.uk/favicon.ico"},
          ...
          {"type":"image","name":"Deforestation: Primary Forest Losses Impact Climate Change — Carmen ...","url":"https://images.squarespace-cdn.com/content/v1/584738ff20099e6c2da92f74/1556207140784-08HFC1PNAYWX368IJGXM/ke17ZwdGBToddI8pDm48kNvT88LknE-K9M4pGNO0Iqd7gQa3H78H3Y0txjaiv_0fDoOvxcdMmMKkDsyUqMSsMWxHk725yiiHCCLfrh8O1z5QPOohDIaIeljMHgDF5CVlOqpeNLcJ80NK65_fV7S1USOFn4xF8vTWDNAUBm5ducQhX-V3oVjSmr829Rco4W2Uo49ZdOtO_QXox0_W7i2zEA/Deforestation+in+Brazil"},
          {"type":"image","name":"Amazon Rainforest Deforestation Before And After","url":"https://media.wired.com/photos/59372bbfd80dd005b42b626f/master/w_2560%2Cc_limit/AP4997094644081.jpg"},
          {"type":"image","name":"11 Amazon Rainforest Deforestation Facts to Know About | Earth.Org","url":"https://u4d2z7k9.rocketcdn.me/wp-content/uploads/2021/11/Untitled-design-88.jpg"},
          ...
        ]
    }
    ```
  </Accordion>

  <Accordion title="AI Avancements" description="Dates filtering" icon="calendar">
    <p>This example shows you how to use the dates filter:</p>

    ```typescript  theme={null}
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: 'YOUR_API_KEY',
    });

    const getNews = async () => {
      return await client.search({
        query: "What are the recent advancements in artificial intelligence technology",
        "depth": "standard",
        "outputType": "sourcedAnswer",
        "fromDate": new Date("2025-03-01"),
        "toDate": new Date("2025-03-05"),
      });
    };

    getNews().then(console.log);
    ```

    Example response:

    ```json  theme={null}
    {
      "answer":"1. **MBZUAI Launches AI Undergraduate Program**: The Mohamed bin Zayed University of Artificial Intelligence has introduced a pioneering undergraduate program aimed at shaping future AI leaders. [Read more](https://www.finanznachrichten.de/nachrichten-2025-03/64714165-mbzuai-unveils-first-of-its-kind-undergraduate-program-in-artificial-intelligence-designed-to-empower-future-ai-leaders-200.htm)\n\n2. **DeepSeek AI Chatbot Raises Cybersecurity Concerns**: The release of DeepSeek, an AI chatbot, has sparked discussions about new cybersecurity challenges associated with rapidly advancing AI technologies. [Read more](https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/)\n\n3. **AI's Impact on Business Innovation**: The integration of AI and other technologies is becoming essential for business success, driving innovation and growth. [Read more](https://www.independent.com.mt/articles/2025-03-02/newspaper-opinions/The-intersection-of-technology-and-business-Paving-the-way-for-innovation-and-growth-6736268254)\n\n4. **Research on Achieving Human-Level AI**: Experts are calling for a change in approach to develop AI systems capable of human-level reasoning, indicating current methods may not suffice. [Read more](https://www.nature.com/articles/d41586-025-00649-4)",
      "sources":
        [
          {
            "name":"MBZUAI Unveils First-of-its-Kind Undergraduate Program in Artificial Intelligence Designed to Empower Future AI Leaders",
            "url":"https://www.finanznachrichten.de/nachrichten-2025-03/64714165-mbzuai-unveils-first-of-its-kind-undergraduate-program-in-artificial-intelligence-designed-to-empower-future-ai-leaders-200.htm",
            "snippet":"ABU DHABI, AE / ACCESS Newswire / March 3, 2025 / The Mohamed bin Zayed University of Artificial Intelligence (MBZUAI) is disrupting the AI education landscape with the launch of its first-ever underg",
            "favicon":"https://www.finanznachrichten.de/favicon.ico"
          },
          {
            "name":"The intersection of technology and business: Paving the way for innovation and growth",
            "url":"https://www.independent.com.mt/articles/2025-03-02/newspaper-opinions/The-intersection-of-technology-and-business-Paving-the-way-for-innovation-and-growth-6736268254",
            "snippet":"In the fast-paced world of business, the integration of innovative technologies has become a crucial driver of success. As an advocate for Artificial Intelligence (AI), Blockchain, Data Analytics, and",
            "favicon":"https://www.independent.com.mt/favicon.ico"
          },
          {
            "name":"DeepSeek Sparks New Cyber Challenges In the AI Chatbot Era",
            "url":"https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/",
            "snippet":"This article discusses DeepSeek, an artificial intelligence chatbot that was released in January of this year, and the concerns it raises around security and rapidly advancing technology.",
            "favicon":"https://www.law.com/favicon.ico"
          },
          ...
      ]
    }
    ```
  </Accordion>
</AccordionGroup>

## Additional ressources

### Prompting guide

We strongly recommend you to read our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide) to best prompt the Linkup API and get optimal results. Even small improvements in how you structure your prompts can dramatically enhance the quality of responses and the overall user experience.

### Structured output guide

We strongly recommend you to read our [structured output guide](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide) to ensure consistency in the response format. Mastering structured outputs allows you to fully leverage Linkup's capabilities while maintaining complete control over how the information is presented and processed in your application.

### Tutorials

Don't hesitate to [check our tutorials](https://docs.linkup.so/pages/documentation/tutorials/signup-radar) for other ideas of what to build with Linkup!

And voilà ! You're now ready to implement the Linkup SDK inside your fabulous project ! 🚀

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).