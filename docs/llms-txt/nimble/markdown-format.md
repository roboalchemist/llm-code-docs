# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/data-parsing/markdown-format.md

# Markdown Format

##

## Markdown Support&#x20;

Extract clean, formatted content from any webpage as markdown - perfect for AI applications, content analysis, and text processing pipelines.

The Web API now supports markdown extraction, providing clean, structured text content without HTML tags or formatting noise. This feature is available in two modes depending on your use case:

1. **Pure Markdown Response** - Returns only markdown content
2. **Markdown with Structured Data** - Returns markdown alongside HTML and parsed data

### **Benefits**

* **Clean Content for LLMs**: Markdown provides optimal formatting for language models and AI applications
* **Simplified Processing**: No need to parse HTML - get readable content directly
* **Flexible Output Options**: Choose between pure markdown or markdown alongside structured data
* **Reduced Payload Size**: Markdown responses are 60-80% smaller than HTML

## Request Options

<table><thead><tr><th width="189">Parameter</th><th width="265">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>foramt</code></td><td>Optional (default = <code>JSON</code>)</td><td>Enum: <code>JSON</code> | <code>HTML</code> | <code>JSON-LINES</code> | <code>RAW</code> | <code>MARKDOWN</code> -  Set to <code>MARKDOWN</code> to receive pure markdown response (cannot be used with other parsing options)</td></tr><tr><td><code>markdown</code></td><td>Optional (default = <code>false</code>)</td><td>Boolean | Set to <code>true</code> to include markdown field in standard JSON response alongside HTML and parsed data</td></tr></tbody></table>

### Usage Notes

* Use `format=markdown` for text-only workflows where you need just the content
* Use `markdown=true` when you need both markdown and other response data, html and parsed data,
* JavaScript-rendered content requires `render=true` for accurate markdown extraction

#### Example Request - Pure Markdown

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location 'https://api.webit.live/api/v1/realtime/web' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
    "url": "https://docs.nimbleway.com/nimble-sdk/search-api",
    "locale": "en",
    "country": "US"
    "format":"MARKDOWN"
}'
```

{% endtab %}
{% endtabs %}

<details>

<summary>Pure Markdown Response</summary>

````markdown
1.  [Nimble SDK](/nimble-sdk)

## Search API

Execute a search queries using Nimble Search

Execute web searches and retrieve clean, parsed content from top results in two modes:

*   **Fast Mode** — Quickly discovers high-value URLs or generates fast web answers for your agents It’s ideal for lightweight discovery or pairing with /extract when you want to selectively fetch full content only from the URLs you choose. Costs 1 credit per search.
    
*   **Deep Search** — Performs real-time webpage extraction for full, rich context, automatically calling /extract to retrieve complete webpage content for deeper research tasks. Deep Search costs 1 credit per search, plus 1 additional credit for each webpage extracted.
    

Both Fast Mode and Deep Search support [advanced search filtering](about:/nimble-sdk/search-api#request-body-parameters), location targeting, max result limits, and additional web-search refinement tools.

```
curl -X POST https://nimble-retriever.webit.live/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI trends 2025",
    "num_results": 10,
    "deep_search": false,
    "country": "US",
    "locale": "en"
  }'
```

**Response**

```
{
  "message": "Request processed successfully",
  "body": [
    {
      "page_content": "",
      "metadata": {
        "title": "Latest GenAI Trends: 5 Key Developments to Watch",
        "snippet": "Explore the top trends in generative AI including agentic AI, retrieval-augmented generation, self-training models, and ethical AI implementations.",
        "url": "https://example.com/genai-trends-2025",
        "position": 1,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    },
    {
      "page_content": "",
      "metadata": {
        "title": "GenAI Investment and Market Analysis 2025",
        "snippet": "Despite challenges, investment in generative AI continues to grow. Analysis of market trends, adoption rates, and future projections for enterprise AI.",
        "url": "https://example.com/genai-investment-analysis",
        "position": 2,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    },
    {
      "page_content": "",
      "metadata": {
        "title": "Emerging Technologies: AI and Data Trends",
        "snippet": "Comprehensive overview of agent-ready data, AI for data engineering, data provenance, compliance changes, and the rise of agentic edge computing.",
        "url": "https://example.com/emerging-tech-trends",
        "position": 3,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    }
  ]
}
```

### 

Fast Mode with - `Include Answer`

Optional AI-generated answer summaries that provide quick insights from search results without reading full content. _This costs 1 additional credit per request._

**Response**

* * *

The search query to execute

Number of search results to return (max: 100)

enum\["general", "news", "location"\]

The search topic type. `news` returns real-time news articles with publication dates. `location` returns places with ratings, addresses, and reviews (restaurants, businesses, venues). `general` (default) returns standard web search results across all sources.

When `true`, fetches and parses full page content. When `false`, return only meta\_data.

Output format. Options: `plain_text`, `markdown`, `simplified_html`

Locale for search results (e.g., `en`, `fr`, `de`)

Country code for search results (e.g., `US`, `FR`, `GB`)

Generate LLM answer summary (only available when deep\_search=False)

List of domains to include in search results. Maximum 50 domains.

List of domains to exclude from search results. Maximum 50 domains.

Filter results after this date (format: YYYY-MM-DD or YYYY)

Filter results before this date (format: YYYY-MM-DD or YYYY)

* * *

*   [Basic Usage](#basic-usage)
*   [Fast Mode with - Include Answer](#fast-mode-with-include-answer)
*   [Deep Search](#deep-search)
*   [Request Body Parameters](#request-body-parameters)

```
curl -X POST https://nimble-retriever.webit.live/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest developments in quantum computing",
    "num_results": 5,
    "deep_search": false,
    "include_answer": true
  }'
```

```
{
  "message": "Request processed successfully",
  "answer": "Recent developments in quantum computing include significant advances in error correction, with researchers achieving quantum advantage in specific computational tasks. Major tech companies have announced new quantum processors with increased qubit counts and improved coherence times, moving closer to practical quantum applications in cryptography and drug discovery.",
  "body": [...]
}
```

```
curl -X POST https://nimble-retriever.webit.live/search \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI trends 2025",
    "num_results": 5,
    "parsing_type": "markdown",
    "country": "US",
    "locale": "en"
  }'
```

```
{
  "message": "Request processed successfully",
  "body": [
    {
      "page_content": "# Latest AI Trends in 2025\n\nThe artificial intelligence landscape has evolved dramatically...",
      "metadata": {
        "title": "Top AI Trends Shaping 2025 - Tech Insights",
        "snippet": "Explore the latest artificial intelligence trends transforming industries in 2025...",
        "url": "https://example.com/ai-trends-2025",
        "position": 1,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    },
    {
      "page_content": "...",
      "metadata": {
        "title": "AI Revolution: What to Expect in 2025",
        "snippet": "From generative AI to autonomous systems...",
        "url": "https://example.com/ai-revolution",
        "position": 2,
        "entity_type": "OrganicResult",
        "country": "US",
        "locale": "en"
      }
    }
  ]
}
```
````

</details>

#### Example Request - Markdown with Structured Data

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location 'https://api.webit.live/api/v1/realtime/web' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
    "url": "https://www.amazon.com/s?k=iphone+17",
    "locale": "en",
    "country": "US"
    "markdown":true,
    "parse":true
}'
```

{% endtab %}
{% endtabs %}

<details>

<summary>Markdown with Structured Data Response</summary>

```json
{
    "url": "https://www.amazon.com/s?k=iphone+17",
    "task_id": "e94316f6-2123-4505-a187-89e0606834c5",
    "status": "success",
    "query_time": "2025-12-15T14:08:26.079Z",
    "html_content": "...HTML...",
    "status_code": 200,
    "headers": {...},
    "parsing": {...},
    "input_url": "https://www.amazon.com/s?k=iphone+17",
    "markdown": "[![iPhone Accessories](https://m.media-amazon.com/images/S/al-na-9d5791cf-3faf/b8a1618b-413f-4e75-8976-51c843b465f5._CR0,0,400,400_AC_SX130_SY60_CB1169409_QL70_.png)](https://aax-events-cell01-cf.us-east.ono.axp.amazon-adsystem.com/x/c/JNH6MLOgIAHG5qIY8mXPW5MAAAGbIldTiQEAAAH2AQBvbm9fdHhuX2JpZDQgICBvbm9fdHhuX2ltcDEgICAdTIMU/clv1_CEuOPUxokZA0iHrVd9cPwXrqRHdiV7c0q6wiqSaG9MMk138D2kKiJ_018nHz9hvWjq0yzpNb3XTPsunP6WEceRBtMD6KSOP8OkoHY0ZxSUqTF9d2viAOLZEdHEepxYGmXJOUI0W78tANGk5hgFv_ak5TLFFOGshzBElqUqEnHhGU36Ta0Ek8SAz5MJbld7QzBH9acdHMzpkFUDVhJ9oQXuEFlsWsnsI6KjDhFKorgxcWp4FvlLz2S1sKgEji6npOAE_zFP7W4zho-hUrANRvXRGwenKzslPpBOrh0YngUq87NF-Cy7yFyCnOZALHHJaq9-sczsxsTvDakJr8IcuqBZ5Sj9hJUhMD9YwF0I5pCZdi8G1fMWu-4hWR5rIBU0KHcCRtq0SmgkUgiWzSCoLRfHV2BrP6s8pDZfIZM3hCrgUANL9bkxVaLztUwaVWXQoMHaeUao3xp-WQHS8cbA2SvJ4-Q2qPp1y_TBdOTLAmp_2qFGp75LHc-AHMbHhxNK2CqqpS0ANBBJckvBiPqG6J_QDbShZBIlAiKhHYaBTXJr2tTyesYBV04HgFDGfLZXTbcOg1kdlQdgfD0O5fltwGIA3fMTRdiCxa_eAfgriSoXM6mpyp-PsPXWjG5SaBd6WbC0ktbP4TMDxL1ep0br5KnSc94ZT2HU1ODkdditRAwLwpHEwEUCKmpDUnohTxYblp7jd48WRPnu44yrUGIH_rN245p5HfH_zQ4aHEAk8EGzDBsUjWHfB08gVt-ugCa8OiqYF-ExyZ93TMqhrRAV7uASt-rzfJI2B1rtFpW_0oZC-ix1wiYtRNgAVtpbS2VWm8cdW_TQhChzrcu-dgdcAXm6Dz23pDtt68P7apoeukh2Oxz27r7lcOyDzoj22unTzLuNkmnvMYiBOaGt0STPodHfW53cPgrwhVMjkxLynXqSHjomlFV20hUWZ0XhvW5XqunQ2Deevu4b6cj7nSyRaVZaliGduRZ7nv13mRZnVRLs4bbQ5NEBV1RIr03D_9ZH4RHTiG0pZL3jAIXpQP3p26_DFCmQRtC-iTng56xoVfrRJ3eF60DL61ORn7aKd8GohjRW2hSo70SgE3NOWxbbuElO_iWBP05NtnScNRJitgIpK0LSuGK8dxl3JhBJWS5PXZg8oeQfvmmQMsPrVvs3MZRX0IQ-z4J2j4PqBSlJ_R9aix9hyQ03L11YlckBpUIpIdPljpC3__wVKpYT4IoGfZG9jE6chwmal7oGu17bJmO2PcFFMNfmOOyzOHlhhweKzZerc-tPutZXD5EPpRbrkKmFY5-qtPj6yzijCxnHSaYd3NS85nTP_HyPgCrjSDzY8YFawgWQG4zUiSiuIgUmYk34_77O1_xmJobJwNAr9gvIoXtX2lKWy8ndSvCkytbqVTKA_bdHSOei_OcBoVaYenV9nElhSEDTN-6pcD5v7IvUJscw5LwqxAHOgADD74BRyQ2g9cMB_lv7OpzDX1KTj0fHTtqwCdYdA4ys0W-YgY7kgOtVD9NX77OWVY2IVWvdijjGb7Zy13VP5rCL3gLNIbPgj-vffoM0OlFXODIYsmosu618ma0ZqLaNlbAvQAqPBeQtftBUn8ybT4S-bSAmERVXRp6e-I9Zkk26Pzwwnl0da5f3zaBTGpoD1z5VFGZd6PSTjIPGTJw7YTbSa9pwBM9fceRiGxUEYHPK1ug-MgVMOoB94Wi7X-dlYJn_eTgvyNl9pxVpKJqSlYhnuWlZMNHBy30yxgniGvl95IODelwlSAj7Pp_bgPXaZz33fjTsIHiq4Txw6GspBPBPNpRtwa72IJAPivkk7fVsu7LSbJr7O1CZuOt4In7sw3ec_zq9hKkR0kfPFnMqcageb9P0udA-mwqI95TMqde-1BYkVR3BZAgdHlb4mVj1U4e4uE4ooBrf-CVgZ_oPiQ3VdBZyKpHZOdyhVuoe4ORpySvZ8Zr3oMEBRN57bPaP4LwzymNjZ6-qHHb1U_PfOKk8yhVL2eEHLf3eNCMDinT5FnKS7wRcjjAQ4gT_q8ZZ3cmTungTMCG_prWCJoTYEkiVZbvqXoifffitJsIe2cfNgZQaZTdZ87p7V0EXQgWNAa83snO5WZ-lMAYVheIMb7GGaDFRn4E2k1A42ZgMjUF5lW-k4EE8aDIMN9UxnTeJYQn5QsnUWvdwAxpiULCEVvUkuefSze0nWJS6Lj7TA9qxOLFMMws0_azAt4nldCbpDr7uWS9N0F1l4InistUL2MdUqS5YunqO7mnMpI2V5-o62kcAofm6BSPJADJXD-3of1cvzml_wtG2mCWba5onPv1hRrDfMXUa7pIO24-QZSTLGHS5xBb0Cx6dYmbXE7aGXT5K3HHcgsmD3bwPZaymvUiyT_dPndE9APqJFbnQfkNupFM7klHFwTVEyuDqn8KLBdUIogAVVmiIblgvD5mvcDyks1JkUHeT5tp8Pvj_R5aAMEDUyYu2Fu5KPHcCRrdONQsxC9gItMfI_1XS_QpmT8-wP4d2wRVJV6EhnZfroOBydDjU-mThUdxcff6Iv0AlU/https://www.amazon.com/stores/page/7FF33670-28E4-48AA-9D38-3B9010BB6947/?_encoding=UTF8&store_ref=SB_A0482791CH6VY6ORQAYO-A0114665WRNDA66B71FG&pd_rd_plhdr=t&aaxitk=776a9a9110219475e62ccc42eb74ba18&hsa_cr_id=0&lp_asins=B0FQFH75KL%2CB0FQFPN3WR%2CB0DCH8VDXF&lp_query=iphone%2017&lp_slot=auto-sparkle-hsa-tetris&ref_=sbx_be_s_sparkle_dlcd_logo&pd_rd_w=YhaKT&content-id=amzn1.sym.9f2b2b9e-47e9-4764-a4dc-2be2f6fca36d%3Aamzn1.sym.9f2b2b9e-47e9-4764-a4dc-2be2f6fca36d&pf_rd_p=9f2b2b9e-47e9-4764-a4dc-2be2f6fca36d&pf_rd_r=74STAMEGSA8T1AB6AKC0&pd_rd_wg=Xl4Ve&pd_rd_r=f19536fd-4b0e-4af2-8cca-7cf7e2d613a5)\n\n![](//aax-events-cell01-cf.us-east.ono.axp.amazon-adsystem.com/e/is/D8A8F2B64B75DAA625F6833085AA5FF3/impb?b=JNH6MLOgIAHG5qIY8mXPW5MAAAGbIldTiQEAAAH2AQBvbm9fdHhuX2JpZDQgICBvbm9fdHhuX2ltcDEgICAdTIMU&w=0&bi=CjHynn2XAR.q.9HreKdsMhzhNyTg0vcotIYcrsP788hJzDGU52H.vSGi0F3Oi8yOUEVgomDlbvoLiStewJ20R4R3gU98IwK3Jvs6Hf5BNvE1wj9Gf5N2gXFu1qh83ZcL3wKJpmxvmS64C2c3iJe05vwNFDfyEZtvhHb5Ci4BKk6dHdDbDgwNoK.18tksWH6JYvcY5haZ5GurH8IULIFQ2w9KnaTb3g1ISE2IKYvjxMVizichIxo9cT3XJTqKPRdG8CsPKdPLkYfnAr0skVcSVM3smv6DkGwmDVvWl.e8GqwKEWF3tgEkfo0D9pTQ3giDGoM1fIW0VIPaVJ-.xs1lFqaWs.Z-4nK9CpxCE595R6wMV3XSXOf84iQyBEq60O0ubfIjXvqI2hRF.QpbKUiwMohndemQoNgsnyc-Z8kc9c-izmycb2LU1kFe-avqi0i7Izqln77AKRBaDzvPXZXNWZ9tQEn4Ky4go3Txu3NGUjO7HeCMb5kRxAhTyy3ONByy)\n\n## Results\n\nCheck each product page for other buying options.\n\nFREE delivery Sat, Dec 20\n\nOr fastest delivery Thu, Dec 18\n\nArrives before Christmas\n\n## More results\n\n## More results\n\n## Recently bought and rated\n\n[Sponsored](#)| 4+ stars and rising in past 90 days\n\n1.  Best Sellerin Cell Phone Battery Charger Cases\n    \n\n## More results\n\n$5.00 off coupon appliedSave $5.00 with coupon\n\nFREE delivery Sat, Dec 20\n\nOr fastest delivery Thu, Dec 18\n\nArrives before Christmas\n\nShop products from small business brands sold in Amazon’s store. Discover more about the small businesses partnering with Amazon and Amazon’s commitment to empowering them. [Learn more](https://www.amazon.com/b/ref=s9_acss_bw_cg_sbp22c_1e1_w/ref=SBE_navbar_5?pf_rd_r=6W5X52VNZRB7GK1E1VX2&pf_rd_p=56621c3d-cff4-45e1-9bf4-79bbeb8006fc&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-top-3&pf_rd_t=30901&pf_rd_i=17879387011&node=18018208011)\n\nFREE delivery Sat, Dec 20 on $35 of items shipped by Amazon\n\nOr fastest delivery Thu, Dec 18\n\nArrives before Christmas\n\n10K+ bought in past month\n\nFREE delivery Sat, Dec 20 on $35 of items shipped by Amazon\n\nOr fastest delivery Thu, Dec 18\n\nArrives before Christmas\n\nThis product has sustainability features recognized by trusted certifications.\n\n## Picks from Amazon Influencers\n\n[Sponsored](#)| From Amazon Influencer storefronts\n\n2.  Best Sellerin Cell Phone Battery Charger Cases\n    \n\n## Related searches\n\n*   Previous\n*   1\n*   [2](/s?k=iphone+17&page=2&xpid=NWM23dMgPHaJU&qid=1765807706&ref=sr_pg_2)\n*   [3](/s?k=iphone+17&page=3&xpid=NWM23dMgPHaJU&qid=1765807706&ref=sr_pg_3)\n20*   [Next](/s?k=iphone+17&page=2&xpid=NWM23dMgPHaJU&qid=1765807706&ref=sr_pg_1)\n\n## Need help?",
    "driver": "vx6"
}
```

</details>
