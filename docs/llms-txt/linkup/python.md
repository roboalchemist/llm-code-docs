# Source: https://docs.linkup.so/pages/sdk/python/python.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Python SDK

> How to use Linkup Python SDK natively in your apps.

## Introduction

The Python SDK allows for easy interaction with the Linkup API, offering the full range of our search functionality. Easily integrate smart search capabilities into your applications, harnessing Linkup’s powerful search features.
You can use our [playground](https://app.linkup.so/playground) to have interactive examples and see how to implement them with the SDK.

<CardGroup cols={2}>
  <Card title="Github" icon="github" href="https://github.com/LinkupPlatform/linkup-python-sdk">
    Repository (feel free to contribute)
  </Card>

  <Card title="PyPi" icon="python" href="https://pypi.org/project/linkup-sdk/">
    PyPi page
  </Card>
</CardGroup>

## Quickstart

Get started with our Python SDK in less than 5 minutes!

<Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
  Create a Linkup account for free to get your API key.
</Card>

## Installation

You can install the Linkup Python SDK as any Python package, for instance using `pip`:

```shell  theme={null}
pip install linkup-sdk
```

## Usage

Here is a basic usage example showing how to use the Linkup Python SDK:

```python  theme={null}
from linkup import LinkupClient

client = LinkupClient(
    api_key="<your-api-key>", # Or set the LINKUP_API_KEY environment variable
)

# Perform a search query
search_response = client.search(
    query="What are the 3 major events in the life of Abraham Lincoln?",
    depth="deep",
    output_type="sourcedAnswer",
)
print(search_response)

# Fetch the content of a web page
response = client.fetch(
    url="https://docs.linkup.so",
)
print(response)
```

### Search parameters

| Parameter                  | Type                                                             | Description                                                                                          | Default  |
| -------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------- |
| query                      | `str`                                                            | The input query                                                                                      | Required |
| depth                      | `typing.Literal["standard", "deep"]`                             | The depth of the search                                                                              | Required |
| output\_type               | `typing.Literal["searchResults", "sourcedAnswer", "structured"]` | The desired output type                                                                              | Required |
| structured\_output\_schema | `pydantic.BaseModel`, `str` or `None`                            | The desired schema for the output, if `output_type` is `structured`                                  | `None`   |
| include\_images            | `datetime.bool` or `None`                                        | Whether to include images in the search                                                              | `None`   |
| from\_date                 | `datetime.date` or `None`                                        | The date from which the search results should be considered                                          | `None`   |
| to\_date                   | `datetime.date` or `None`                                        | The date until which the search results should be considered                                         | `None`   |
| exclude\_domains           | `list[str]` or `None`                                            | The domains to exclude from the search                                                               | `None`   |
| include\_domains           | `list[str]` or `None`                                            | The domains to restrict the search with                                                              | `None`   |
| include\_inline\_citations | `bool` or `None`                                                 | Whether to include inline citations in the answer, if `output_type` is `sourcedAnswer`               | `None`   |
| include\_sources           | `bool` or `None`                                                 | Whether to include the sources, if `output_type` is `structured` (modifies the schema of the output) | `None`   |
| max\_results               | `int` or `None`                                                  | Maximum number of results to return                                                                  | `None`   |

#### Query

The `query` parameter is the core input string that defines your search intent. It represents the question or information request that you want Linkup to answer. How you formulate this query significantly impacts the quality and relevance of results.

Effective queries should be:

* **Clear and specific**: "What were the key findings of NASA's James Webb telescope in 2023?" provides better results than "Tell me about space discoveries"
* **Contextually rich**: Include relevant context when needed ("What are the environmental impacts of lithium mining for EV batteries?")
* **Naturally phrased**: Write as you would ask a knowledgeable person, not with keywords

For optimal results, consider reviewing our [prompting guide](https://docs.linkup.so/pages/documentation/tutorials/prompting-guide), which provides detailed strategies for crafting effective queries.

#### Depth

The `depth` field is used to select the type of search you want to perform:

* **standard**: the search will be straightforward and fast, suited for relatively simple queries (e.g. "What's the weather in Paris today?")
* **depth**: the search will use an agentic workflow, which makes it in general slower, but it will be able to solve more complex queries (e.g. "What is the company profile of LangChain accross the last few years, and how does it compare to its concurrents?")

#### Output type

The type of output which is expected:

* **sourcedAnswer**: Provides a comprehensive natural language answer to the query along with citations to the source material. Ideal for when you need well-formed responses with verifiable information and transparent sourcing.
* **searchResults**: Returns the raw search context data without synthesis, giving you direct access to the underlying information. Useful for custom processing, or when you need to implement your own answer generation logic.
* **structured**: Allows you to receive responses in a custom format based on the format provided in
  `structured_output_schema`. If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

#### Structured output schema

Linkup’s structured output feature allows you to receive responses in a custom format that you define. This is particularly useful when you need to integrate Linkup’s responses directly into your application’s data structure or when you want to ensure consistency in the response format.
To do that, you have to use the `structured_output_schema` field. Supported formats are a pydantic.BaseModel or a string representing a valid object JSON schema.
If you want a full guide on how to use it, you check it [here](https://docs.linkup.so/pages/documentation/tutorials/structured-output-guide)

#### Include images

The `include_images` parameter allows you to receive image results alongside text results in your search responses. When set to `True`, Linkup will return relevant images related to your query, each with a URL and metadata. This is particularly useful for:

* Creating visual search experiences
* Building content that combines text and images
* Researching topics where visual information is important

Image results are returned with the same structure as text results but with `type: "image"`.

#### From date

The `from_date` parameter filters search results to only include content published after the specified date. This helps you:

* Focus on recent information
* Exclude outdated content

The date should be a `datetime.date` type, for example: `datetime.date(2025, 3, 1)`.

#### To date

The `to_date` parameter complements `from_date` by restricting search results to only include content published or updated before the specified date. This is useful for:

* Historical research on specific time periods
* Analyzing content published within a specific date range
* Avoiding more recent information that might skew results

Like `from_date`, the date should be a `datetime.date` type, for example: `date(2025, 3, 15)`.

When used together, `from_date` and `to_date` create a date range filter for your search results.

#### Exclude domains

The `exclude_domains` parameter allows you to specify a list of domains that should be excluded from the search results. This is useful for:

* Filtering out unwanted sources
* Avoiding results from specific domains that may not be relevant or trustworthy.

#### Include domains

The `include_domains` parameter allows you to specify a list of domains that must be included in the search results. This is useful for:

* focus on specific sources
* ensure that results come from trusted domains.

#### Include inline citations

The `include_inline_citations` parameter is specifically designed for use with the `sourcedAnswer` output type. When enabled, it embeds citations directly within the answer text, making it easier to identify which parts of the response correspond to specific sources. This is particularly useful for:

* Academic or research applications where source attribution is critical
* Creating content that needs verifiable claims with clear sourcing
* Building applications where users need to quickly verify information

When `include_inline_citations` is set to `True`, the answer will contain inline references like \[1], \[2] that correspond to the sources in the response.

#### Include sources

The `include_sources` parameter is specifically designed for use with the `structured` output type. When enabled, it modifies the schema of the structured response to include source information alongside your custom data structure. This is particularly useful for:

* Applications that need both structured data and source attribution
* Building systems that require traceability of information
* Creating responses where you want to maintain both custom format and source verification

When `include_sources` is set to `True`, the response will be wrapped in a `LinkupSearchStructuredResponse` object containing both your structured data and source information.

### maxResults

The `maxResults` parameter allows you to specify the maximum number of results to return. This is useful for:

* Limiting the number of results returned
* Reducing the context size

### Fetch parameters

| Parameter          | Type             | Description                                          | Default  |
| ------------------ | ---------------- | ---------------------------------------------------- | -------- |
| url                | `str`            | The URL of the web page to fetch                     | Required |
| include\_raw\_html | `bool` or `None` | Whether to include the raw HTML in the response      | `None`   |
| render\_js         | `bool` or `None` | Whether the API should render JavaScript on the page | `None`   |

#### URL

The `url` parameter specifies the web page URL that you want to fetch content from. This should be a fully qualified URL including the protocol (http\:// or https\://). The fetch endpoint will retrieve the page content and return it in a cleaned up mardown, making it easy to process the web page by AI agents or other applications.

#### Include raw HTML

The `include_raw_html` parameter controls whether the raw HTML source code of the web page is included in the response alongside the cleaned up markdown content. This is useful for applications that need to perform custom HTML parsing, preserve specific formatting, or access elements that might be filtered out during the standard content extraction process.

#### Render JS

The `render_js` parameter determines whether JavaScript should be executed when fetching the web page. When set to `True`, the API will render the page in a browser-like environment, executing JavaScript code and waiting for dynamic content to load before extracting the content. This is essential for modern web applications that rely heavily on JavaScript for content generation, such as single-page applications (SPAs) or pages with dynamically loaded content, but induces additional latency.

## Examples

<AccordionGroup>
  <Accordion title="Last Formula 1 race" description="Standard example" icon="flag">
    <p>This example show you how to combine the standard search with a sourced answer</p>

    ```python  theme={null}
    from linkup import LinkupClient

    client = LinkupClient()

    search_response = client.search(
        query="Last Formula 1 race",
        depth="standard",
        output_type="sourcedAnswer",
    )
    print(search_response)
    ```

    Example response:

    ```python  theme={null}
    answer='The last Formula 1 race was the Australian Grand Prix, where Lando Norris won. The race took place recently, and it was marked by intermittent rain causing several challenges on the track. The next race is the Chinese Grand Prix, scheduled for March 21-23, 2025.'
    sources=[
      LinkupSource(name='Formula 1 season begins with dramatic Australian Grand Prix', url='https://www.emorywheel.com/article/2025/03/pivexulgpch8', snippet='The Australian Grand Prix was a thrilling way to start the 2025 F1 season for the many fans eager to have F1 back after the long winter break. The excitement will continue with the Chinese Grand Prix, the first sprint race of the season, in Shanghai on March 21-23.', favicon='https://www.emorywheel.com/wp-content/uploads/2023/09/cropped-Emory-Wheel-Favicon-32x32.png'),
      LinkupSource(name="AUTO RACING: Bell's three-race win streak snapped and Norris takes the F1 season opener", url='https://www.washingtonpost.com/sports/auto-racing/2025/03/18/auto-racing-glance/414c4f32-0419-11f0-941f-6ca83a0bd35b_story.html', snippet='Schedule: Saturday, practice, 1:05 p.m., qualifying, 2:10 p.m.; Sunday, race, 3 p.m. (FS1). Track: Homestead-Miami Speedway. Race distance: 267 laps, 400.5 miles. Last year: Tyler Reddick secured the win from the pole after a last-lap pass of Ryan Blaney.', favicon='https://www.washingtonpost.com/wp-stat/assets/favicon-32x32.png'),
      LinkupSource(name='F1 Australian Grand Prix 2025 results: Norris wins, rookies spin out in the rain', url='https://www.yahoo.com/lifestyle/f1-australian-grand-prix-2025-083408114.html', snippet='Intermittent rain caused havoc on the track before and during the 2025 F1 Australian Grand Prix. The post F1 Australian Grand Prix 2025 results: Norris wins, rookies spin out in the rain appeared first on The Manual.', favicon='https://s.yimg.com/rz/l/favicon.ico'),
      ...
    ]
    ```
  </Accordion>

  <Accordion title="Company Revenue" description="Deep + structured output" icon="building">
    <p>This example shows you how to use the deep with a relative complexe structured output:</p>

    ```python  theme={null}
    from linkup import LinkupClient

    client = LinkupClient(api_key="YOUR_API_KEY")

    schema = """{
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
    }"""

    response = client.search(
        query="What is Microsoft's 2024 revenue?",
        depth="deep",
        output_type="structured",
        structured_output_schema=schema
    )

    print(response)
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

    ```python  theme={null}
    from linkup import LinkupClient

    client = LinkupClient(api_key="YOUR_API_KEY")

    search_response = client.search(
        query="Latest politic news",
        depth="standard",
        output_type="searchResults",
    )

    print(search_response)
    ```

    Example response:

    ```python  theme={null}
    results=[
      LinkupSearchTextResult(type='text', name='CNN host Van Jones shares personal upbringing, reflects on state of American politics', url='https://www.browndailyherald.com/article/2025/03/cnn-host-van-jones-shares-personal-upbringing-reflects-on-state-of-american-politics', content='On Wednesday night, the Watson Institute for International and Public Affairs welcomed CNN Host Van Jones for a conversation on the state of American politics. In his talk, Jones explained increasingly strained ties between Jewish and Black activist communities,', favicon='https://www.browndailyherald.com/wp-content/uploads/2023/09/cropped-BDH-Favicon-32x32.png'),
      LinkupSearchTextResult(type='text', name='Politics latest: Billions being shaved off welfare bill - join our live Q&A on what it means for you', url='https://news.sky.com/story/politics-latest-trump-wants-to-shock-europe-into-action-with-false-ukraine-claims-says-boris-johnson-12593360', content='Work and Pensions Secretary Liz Kendall has announced changes to the welfare system - including merging some benefits and a plan to scrap the work capability assessment used to claim universal credit.', favicon='https://e1.365dm.com/21/03/1600x900/skysports-politics-latest-live_5311164.jpg?20210310123112'),
      LinkupSearchTextResult(type='text', name='Politics', url='https://www.npr.org/sections/politics/', content="March 19, 2025 • The decision offers a venue compromise in the bellwether case, while Khalil's legal team seeks to release him from detention and block his deportation.", favicon='https://media.npr.org/favicon.ico'),
      ...
    ]
    ```
  </Accordion>

  <Accordion title="Amazon deforestation" description="IncludeImages filter" icon="trees">
    <p>This example return text and images sources</p>

    ```python  theme={null}
    from linkup import LinkupClient

    client = LinkupClient(api_key="YOUR_API_KEY")

    search_response = client.search(
        query="Amazon deforestation",
        depth="standard",
        output_type="searchResults",
        include_images=True
    )

    print(search_response)
    ```

    Exemple response

    ```python  theme={null}
    results=[
      LinkupSearchTextResult(type='text', name='How a grassroots financing model is helping Indigenous communities save the Amazon', url='https://www.unep.org/news-and-stories/story/how-grassroots-financing-model-helping-indigenous-communities-save-amazon', content='A United Nations effort is channeling more finance to communities to help them conserve, restore and sustainably manage forests.', favicon='https://www.unep.org/sites/all/themes/custom/unep/favicon.ico'),
      LinkupSearchTextResult(type='text', name='Amazon Rainforest Razed To Build Highway For UN Climate Summit', url='https://ijr.com/amazon-rainforest-razed-to-build-highway-for-un-climate-summit/', content='Ahead of the COP30 climate summit in Belém, Brazil, developers are carving a four-lane highway through protected tracts of the', favicon='https://ijr.com/wp-content/uploads/2021/08/cropped-ijr-favicon-32x32.png'),
      LinkupSearchTextResult(type='text', name='Roads less traveled multiply deforestation in the Amazon and beyond', url='https://www.msn.com/en-us/news/world/roads-less-traveled-multiply-deforestation-in-the-amazon-and-beyond/ar-AA1AGYEe', content='James Cook University-led research has revealed secondary roads branching from major highways in tropical forests linked to extensive deforestation across the Brazilian Amazon, the Congo Basin, and New Guinea.', favicon='https://static.msn.com/favicon.ico'),
      ...
      LinkupSearchImageResult(type='image', name='Amazon Fires and the Horrifying Science of Deforestation | WIRED', url='https://media.wired.com/photos/5d6027925af21f000859fc13/master/w_2000,c_limit/Science_AmazonASAP_1125307709.jpg'),
      LinkupSearchImageResult(type='image', name='Deforestation In The Amazon Rainforest | emr.ac.uk', url='https://en.mercopress.com/data/cache/noticias/73326/0x0/1-88.jpg'),
      LinkupSearchImageResult(type='image', name='Amazon Deforestation WWF - Green Queen', url='https://www.greenqueen.com.hk/wp-content/uploads/2020/06/Amazon-Deforestation-WWF.jpg'),
      ...
    ]
    ```
  </Accordion>

  <Accordion title="AI Avancements" description="Dates filtering" icon="calendar">
    <p>This example shows you how to use the dates filter:</p>

    ```python  theme={null}
    from linkup import LinkupClient
    from datetime import date

    client = LinkupClient(api_key="YOUR_API_KEY")

    search_response = client.search(
        query="What are the recent advancements in artificial intelligence technology",
        depth="standard",
        output_type="sourcedAnswer",
        from_date=date(2025, 3, 1),
        to_date=date(2025, 3, 5),
    )

    print(search_response)
    ```

    Example response:

    ```python  theme={null}
    answer='1. A call for a new approach to achieve human-level reasoning in AI systems has been highlighted by researchers. [Read more](https://www.nature.com/articles/d41586-025-00649-4).\n\n2. The release of DeepSeek, an AI chatbot, has raised new cybersecurity concerns. [Read more](https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/).\n\n3. AI continues to transform everyday life, influencing communication, work, and leisure activities. [Read more](https://signalscv.com/2025/03/how-technology-is-changing-our-everyday-life-from-ai-to-the-internet-of-things/).\n\n4. The integration of AI with other technologies is driving innovation and growth in business sectors. [Read more](https://www.independent.com.mt/articles/2025-03-02/newspaper-opinions/The-intersection-of-technology-and-business-Paving-the-way-for-innovation-and-growth-6736268254).'
    sources=[
      LinkupSource(name='How AI can achieve human-level intelligence: researchers call for change in tack', url='https://www.nature.com/articles/d41586-025-00649-4', snippet='Artificial intelligence (AI) systems with human-level reasoning are unlikely to be achieved through the approach and technology ... Heights, New York, who spearheaded the survey in her role as president of the Association for the Advancement of Artificial ...', favicon='https://media.nature.com/lw1024/magazine-assets/d41586-025-00649-4/d41586-025-00649-4_17996430.png'),
      LinkupSource(name='DeepSeek Sparks New Cyber Challenges In the AI Chatbot Era', url='https://www.law.com/newyorklawjournal/2025/03/04/deepseek-sparks-new-cyber-challenges-in-the-ai-chatbot-era/', snippet='This article discusses DeepSeek, an artificial intelligence chatbot that was released in January of this year, and the concerns it raises around security and rapidly advancing technology.', favicon='https://www.law.com/img/NYLJ/favicon.ico'),
      LinkupSource(name='How Technology is Changing Our Everyday Life: From AI to the Internet of Things', url='https://signalscv.com/2025/03/how-technology-is-changing-our-everyday-life-from-ai-to-the-internet-of-things/', snippet='Technology has revolutionized our lives, transforming how we communicate, work, shop, and even unwind. In a world driven by rapid innovation, technologies like artificial intelligence (AI), the Internet of Things', favicon='https://signalscv.com/wp-content/uploads/2023/01/cropped-Signals-favicon-32x32.png'),
      ...
    ]
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