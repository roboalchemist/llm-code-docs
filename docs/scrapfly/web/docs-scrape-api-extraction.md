# Source: https://scrapfly.io/docs/scrape-api/extraction

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/extraction

Markdown Content:
Data Extraction
---------------

Scrapfly provides a powerful data extraction API which can extract structured data from any web page using AI, LLMs and predefined JSON instructions.

The Web Scraping API integrates [Extraction API](https://scrapfly.io/docs/extraction-api/getting-started) to extract data from web pages using 3 different methods:

For convenience, these 3 extraction API methods are directly accessible in the Web Scraping API requests through [extraction_model](https://scrapfly.io/docs/scrape-api/getting-started#api_param_extraction_model), [extraction_prompt](https://scrapfly.io/docs/scrape-api/getting-started#api_param_extraction_prompt) and [extraction_template](https://scrapfly.io/docs/scrape-api/getting-started#api_param_extraction_template) parameters. This means you can scrape and extract data with a single API call.

* * *

> Combined with cache feature, we cache the raw data from the website, allowing you to **re-extract the data with multiple extraction passes**at a **much faster speed**and **lower cost**. This applies to the following extraction types: 
> *   [Extraction Template](https://scrapfly.io/docs/extraction-api/rules-and-template)
> *   [Extraction Model](https://scrapfly.io/docs/extraction-api/automatic-ai)
> *   [LLM Extraction](https://scrapfly.io/docs/extraction-api/llm-prompt)
> 
> 
> 
> ##### Learn more about cache feature
> 
> 
> *   [Cache feature](https://scrapfly.io/docs/scrape-api/cache)
> *   [API Specification](https://scrapfly.io/docs/scrape-api/getting-started)

If your scrape is not reliable due to **heavy anti-bot protection or long load times**, you can scrape without extraction and then submit your content to the [dedicated Extraction API](https://scrapfly.io/docs/extraction-api/getting-started).

The extraction template allows you to define custom extraction rules in JSON format. By using these templates, you can extract structured data from HTML, JSON, or XML content with exact precision using industry standard parsing rules like CSS selectors, XPath, and regex.

#### Key Features:

*   **Customizable Rules:** Define your own extraction rules to tailor data extraction according to your needs.
*   **Versatile Data Sources:** Extract data from various content types including HTML, JSON, and XML.
*   **Structured Output:** Retrieve well-structured data in JSON format, making it easier to process and analyze.

> You will find the template and extraction rules in the [extraction API section](https://scrapfly.io/docs/extraction-api/rules-and-template)

To use the extraction template with the Web Scraping API, pass the following parameter `extraction_template=ephemeral:<YOUR BASE64 ENCODED TEMPLATE>`

For template encoding you can use [our base64 tool](https://scrapfly.io/web-scraping-tools/base64)

### [Example](https://scrapfly.io/docs/scrape-api/extraction#template_example)

Extraction Template

```
{
    "source": "html",
    "selectors": [
        {
            "name": "description",
            "query": "p.product-description::text",
            "type": "css"
        },
        {
            "name": "price_block",
            "nested": [
                {
                    "extractor": {
                        "name": "price"
                    },
                    "formatters": [
                        {
                            "args": {
                                "key": "currency"
                            },
                            "name": "pick"
                        }
                    ],
                    "name": "price_regex",
                    "options": {
                        "content": "text",
                        "dotall": true,
                        "ignorecase": true,
                        "multiline": false
                    },
                    "query": "(\\$\\d{2}\\.\\d{2})",
                    "type": "regex"
                }
            ],
            "query": ".product-data div.price",
            "type": "css"
        },
        {
            "name": "price_from_html",
            "nested": [
                {
                    "formatters": [
                        {
                            "name": "uppercase"
                        },
                        {
                            "name": "remove_html"
                        }
                    ],
                    "name": "price_html_regex",
                    "nested": [
                        {
                            "multiple": true,
                            "name": "price regex",
                            "query": ".+",
                            "type": "regex"
                        }
                    ],
                    "query": ".+",
                    "type": "regex"
                }
            ],
            "query": ".product-data div.price",
            "type": "css"
        },
        {
            "extractor": {
                "name": "price"
            },
            "name": "price",
            "query": "span.product-price::text",
            "type": "css"
        },
        {
            "formatters": [
                {
                    "name": "absolute_url"
                },
                {
                    "name": "unique"
                }
            ],
            "multiple": true,
            "name": "page_links",
            "query": "\/\/a\/@href",
            "type": "xpath"
        },
        {
            "formatters": [
                {
                    "name": "absolute_url"
                },
                {
                    "name": "unique"
                }
            ],
            "multiple": true,
            "name": "page_images",
            "query": "\/\/img\/@src",
            "type": "xpath"
        },
        {
            "name": "reviews",
            "nested": [
                {
                    "cast": "float",
                    "name": "rating",
                    "query": "count(\/\/svg)",
                    "type": "xpath"
                },
                {
                    "formatters": [
                        {
                            "args": {
                                "format": "%d\/%m\/%Y"
                            },
                            "name": "datetime"
                        }
                    ],
                    "name": "date",
                    "query": "\/\/span[1]\/text()",
                    "type": "xpath"
                },
                {
                    "name": "text",
                    "query": "\/\/p[1]\/text()",
                    "type": "xpath"
                }
            ],
            "query": "#reviews > div.review",
            "type": "css"
        }
    ]
}
```

Extracted Data

```
{
    "description": "Indulge your sweet tooth with our Box of Chocolate Candy. Each box contains an assortment of rich, flavorful chocolates with a smooth, creamy filling. Choose from a variety of flavors including zesty orange and sweet cherry. Whether you're looking for the perfect gift or just want to treat yourself, our Box of Chocolate Candy is sure to satisfy.",
    "page_images": [
        "https://web-scraping.dev/assets/products/orange-chocolate-box-small-1.webp",
        "https://web-scraping.dev/assets/products/orange-chocolate-box-small-2.webp",
        "https://web-scraping.dev/assets/products/orange-chocolate-box-small-3.webp",
        "https://web-scraping.dev/assets/products/orange-chocolate-box-small-4.webp",
        "https://web-scraping.dev/assets/products/kids-light-up-sneakers-red-1.webp",
        "https://web-scraping.dev/assets/products/blue-potion.webp",
        "https://web-scraping.dev/assets/products/cat-ear-beanie-grey.webp",
        "https://web-scraping.dev/assets/products/orange-chocolate-box-medium-1.webp"
    ],
    "page_links": [
        "https://web-scraping.dev/",
        "https://web-scraping.dev",
        "https://web-scraping.dev/docs",
        "https://web-scraping.dev/api/graphql",
        "https://web-scraping.dev/products",
        "https://web-scraping.dev/reviews",
        "https://web-scraping.dev/testimonials",
        "https://web-scraping.dev/login",
        "https://web-scraping.dev/cart",
        "https://web-scraping.dev/",
        "https://web-scraping.dev/products",
        "https://web-scraping.dev/product/1?variant=orange-small",
        "https://web-scraping.dev/product/1?variant=orange-medium",
        "https://web-scraping.dev/product/1?variant=orange-large",
        "https://web-scraping.dev/product/1?variant=cherry-small",
        "https://web-scraping.dev/product/1?variant=cherry-medium",
        "https://web-scraping.dev/product/1?variant=cherry-large",
        "https://web-scraping.dev/product/10",
        "https://web-scraping.dev/product/5",
        "https://web-scraping.dev/product/24",
        "https://web-scraping.dev/product/1",
        "https://scrapfly.io/academy",
        "https://web-scraping.dev/"
    ],
    "price": {
        "amount": "9.99",
        "currency": "USD",
        "original": "$9.99 ",
        "symbol": "$"
    },
    "price_block": [
        {
            "price_regex": "USD"
        }
    ],
    "price_from_html": [
        {
            "price_html_regex": [
                {
                    "price regex": [
                        "\n            \n            $9.99 \n            FROM $12.99\n            \n          "
                    ]
                }
            ]
        }
    ],
    "reviews": [
        {
            "date": "22/07/2022",
            "rating": 5,
            "text": "Absolutely delicious! The orange flavor is my favorite."
        },
        {
            "date": "16/08/2022",
            "rating": 4,
            "text": "I bought these as a gift, and they were well received. Will definitely purchase again."
        },
        {
            "date": "10/09/2022",
            "rating": 5,
            "text": "Nice variety of flavors. The chocolate is rich and smooth."
        },
        {
            "date": "02/10/2022",
            "rating": 5,
            "text": "The cherry flavor is amazing. Will be buying more."
        },
        {
            "date": "05/11/2022",
            "rating": 4,
            "text": "A bit pricey, but the quality of the chocolate is worth it."
        }
    ]
}
```

* * *

#### Web Scraping API Usage

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "tags=player,project:default" \
--data-urlencode "extraction_template=ephemeral:eyJzZWxlY3RvcnMiOlt7Im5hbWUiOiJkZXNjcmlwdGlvbiIsInF1ZXJ5IjoicC5wcm9kdWN0LWRlc2NyaXB0aW9uOjp0ZXh0IiwidHlwZSI6ImNzcyJ9LHsibmFtZSI6InByaWNlX2Jsb2NrIiwibmVzdGVkIjpbeyJleHRyYWN0b3IiOnsibmFtZSI6InByaWNlIn0sImZvcm1hdHRlcnMiOlt7ImFyZ3MiOnsia2V5IjoiY3VycmVuY3kifSwibmFtZSI6InBpY2sifV0sIm5hbWUiOiJwcmljZV9yZWdleCIsIm9wdGlvbnMiOnsiY29udGVudCI6InRleHQiLCJkb3RhbGwiOnRydWUsImlnbm9yZWNhc2UiOnRydWUsIm11bHRpbGluZSI6ZmFsc2V9LCJxdWVyeSI6IihcXCRcXGR7Mn1cXC5cXGR7Mn0pIiwidHlwZSI6InJlZ2V4In1dLCJxdWVyeSI6Ii5wcm9kdWN0LWRhdGEgZGl2LnByaWNlIiwidHlwZSI6ImNzcyJ9LHsibmFtZSI6InByaWNlX2Zyb21faHRtbCIsIm5lc3RlZCI6W3siZm9ybWF0dGVycyI6W3sibmFtZSI6InVwcGVyY2FzZSJ9LHsibmFtZSI6InJlbW92ZV9odG1sIn1dLCJuYW1lIjoicHJpY2VfaHRtbF9yZWdleCIsIm5lc3RlZCI6W3sibXVsdGlwbGUiOnRydWUsIm5hbWUiOiJwcmljZSByZWdleCIsInF1ZXJ5IjoiLisiLCJ0eXBlIjoicmVnZXgifV0sInF1ZXJ5IjoiLisiLCJ0eXBlIjoicmVnZXgifV0sInF1ZXJ5IjoiLnByb2R1Y3QtZGF0YSBkaXYucHJpY2UiLCJ0eXBlIjoiY3NzIn0seyJleHRyYWN0b3IiOnsibmFtZSI6InByaWNlIn0sIm5hbWUiOiJwcmljZSIsInF1ZXJ5Ijoic3Bhbi5wcm9kdWN0LXByaWNlOjp0ZXh0IiwidHlwZSI6ImNzcyJ9LHsiZm9ybWF0dGVycyI6W3sibmFtZSI6ImFic29sdXRlX3VybCJ9LHsibmFtZSI6InVuaXF1ZSJ9XSwibXVsdGlwbGUiOnRydWUsIm5hbWUiOiJwYWdlX2xpbmtzIiwicXVlcnkiOiJcL1wvYVwvQGhyZWYiLCJ0eXBlIjoieHBhdGgifSx7ImZvcm1hdHRlcnMiOlt7Im5hbWUiOiJhYnNvbHV0ZV91cmwifSx7Im5hbWUiOiJ1bmlxdWUifV0sIm11bHRpcGxlIjp0cnVlLCJuYW1lIjoicGFnZV9pbWFnZXMiLCJxdWVyeSI6IlwvXC9pbWdcL0BzcmMiLCJ0eXBlIjoieHBhdGgifSx7Im5hbWUiOiJyZXZpZXdzIiwibmVzdGVkIjpbeyJjYXN0IjoiZmxvYXQiLCJuYW1lIjoicmF0aW5nIiwicXVlcnkiOiJjb3VudChcL1wvc3ZnKSIsInR5cGUiOiJ4cGF0aCJ9LHsiZm9ybWF0dGVycyI6W3siYXJncyI6eyJmb3JtYXQiOiIlZFwvJW1cLyVZIn0sIm5hbWUiOiJkYXRldGltZSJ9XSwibmFtZSI6ImRhdGUiLCJxdWVyeSI6IlwvXC9zcGFuWzFdXC90ZXh0KCkiLCJ0eXBlIjoieHBhdGgifSx7Im5hbWUiOiJ0ZXh0IiwicXVlcnkiOiJcL1wvcFsxXVwvdGV4dCgpIiwidHlwZSI6InhwYXRoIn1dLCJxdWVyeSI6IiNyZXZpZXdzID4gZGl2LnJldmlldyIsInR5cGUiOiJjc3MifV0sInNvdXJjZSI6Imh0bWwifQ" \
--data-urlencode "cache=true" \
--data-urlencode "asp=true" \
--data-urlencode "render_js=true" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/product/1"
```

`https://api.scrapfly.io/scrape?tags=player%2Cproject%3Adefault&extraction_template=ephemeral%3AeyJzZWxlY3RvcnMiOlt7Im5hbWUiOiJkZXNjcmlwdGlvbiIsInF1ZXJ5IjoicC5wcm9kdWN0LWRlc2NyaXB0aW9uOjp0ZXh0IiwidHlwZSI6ImNzcyJ9LHsibmFtZSI6InByaWNlX2Jsb2NrIiwibmVzdGVkIjpbeyJleHRyYWN0b3IiOnsibmFtZSI6InByaWNlIn0sImZvcm1hdHRlcnMiOlt7ImFyZ3MiOnsia2V5IjoiY3VycmVuY3kifSwibmFtZSI6InBpY2sifV0sIm5hbWUiOiJwcmljZV9yZWdleCIsIm9wdGlvbnMiOnsiY29udGVudCI6InRleHQiLCJkb3RhbGwiOnRydWUsImlnbm9yZWNhc2UiOnRydWUsIm11bHRpbGluZSI6ZmFsc2V9LCJxdWVyeSI6IihcXCRcXGR7Mn1cXC5cXGR7Mn0pIiwidHlwZSI6InJlZ2V4In1dLCJxdWVyeSI6Ii5wcm9kdWN0LWRhdGEgZGl2LnByaWNlIiwidHlwZSI6ImNzcyJ9LHsibmFtZSI6InByaWNlX2Zyb21faHRtbCIsIm5lc3RlZCI6W3siZm9ybWF0dGVycyI6W3sibmFtZSI6InVwcGVyY2FzZSJ9LHsibmFtZSI6InJlbW92ZV9odG1sIn1dLCJuYW1lIjoicHJpY2VfaHRtbF9yZWdleCIsIm5lc3RlZCI6W3sibXVsdGlwbGUiOnRydWUsIm5hbWUiOiJwcmljZSByZWdleCIsInF1ZXJ5IjoiLisiLCJ0eXBlIjoicmVnZXgifV0sInF1ZXJ5IjoiLisiLCJ0eXBlIjoicmVnZXgifV0sInF1ZXJ5IjoiLnByb2R1Y3QtZGF0YSBkaXYucHJpY2UiLCJ0eXBlIjoiY3NzIn0seyJleHRyYWN0b3IiOnsibmFtZSI6InByaWNlIn0sIm5hbWUiOiJwcmljZSIsInF1ZXJ5Ijoic3Bhbi5wcm9kdWN0LXByaWNlOjp0ZXh0IiwidHlwZSI6ImNzcyJ9LHsiZm9ybWF0dGVycyI6W3sibmFtZSI6ImFic29sdXRlX3VybCJ9LHsibmFtZSI6InVuaXF1ZSJ9XSwibXVsdGlwbGUiOnRydWUsIm5hbWUiOiJwYWdlX2xpbmtzIiwicXVlcnkiOiJcL1wvYVwvQGhyZWYiLCJ0eXBlIjoieHBhdGgifSx7ImZvcm1hdHRlcnMiOlt7Im5hbWUiOiJhYnNvbHV0ZV91cmwifSx7Im5hbWUiOiJ1bmlxdWUifV0sIm11bHRpcGxlIjp0cnVlLCJuYW1lIjoicGFnZV9pbWFnZXMiLCJxdWVyeSI6IlwvXC9pbWdcL0BzcmMiLCJ0eXBlIjoieHBhdGgifSx7Im5hbWUiOiJyZXZpZXdzIiwibmVzdGVkIjpbeyJjYXN0IjoiZmxvYXQiLCJuYW1lIjoicmF0aW5nIiwicXVlcnkiOiJjb3VudChcL1wvc3ZnKSIsInR5cGUiOiJ4cGF0aCJ9LHsiZm9ybWF0dGVycyI6W3siYXJncyI6eyJmb3JtYXQiOiIlZFwvJW1cLyVZIn0sIm5hbWUiOiJkYXRldGltZSJ9XSwibmFtZSI6ImRhdGUiLCJxdWVyeSI6IlwvXC9zcGFuWzFdXC90ZXh0KCkiLCJ0eXBlIjoieHBhdGgifSx7Im5hbWUiOiJ0ZXh0IiwicXVlcnkiOiJcL1wvcFsxXVwvdGV4dCgpIiwidHlwZSI6InhwYXRoIn1dLCJxdWVyeSI6IiNyZXZpZXdzID4gZGl2LnJldmlldyIsInR5cGUiOiJjc3MifV0sInNvdXJjZSI6Imh0bWwifQ&cache=true&asp=true&render_js=true&key=&url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1`

Large Language Model extraction allows you to extract data from web pages using natural language instructions. You can describe the data you want to extract in plain English, and our models will handle the rest. This extraction method is very accessible and very powerful.

For example, you can ask the LLM to perform intelligent tasks like sentiment analysis or content summary or perform direct extract tasks like extracting data based on provided schema or output definitions.

#### Benefits

*   Ease of Use: No need to worry about technical details; our models manage everything for you.
*   Versatile Content Types: Supports various text content types including `text/plain, html, xml, markdown, application/json, rss`. We plan to support additional content types like `application/pdf` in the future.

#### How It works

1.   Provide Natural Language Instructions with API Parameter and describe the data you want to extract. `extraction_prompt=my prompt`
2.   Get Structured Data: Receive well-organized data based on your specifications in `result.extracted_data.data`. You also have the content type available `result.extracted_data.content_type` - JSON is not re encoded (JSON in JSON) for simplicity, so you can directly access your data. 

> You will find the template and extraction rules in the [Extraction API - LLM Extraction](https://scrapfly.io/docs/extraction-api/llm-prompt)

### [Example](https://scrapfly.io/docs/scrape-api/extraction#llm_example)

Prompt:

`In this document, what is the general sentiment about the product`

Result:

```
{
    "config" : {
        ...
    },
    "context": {
        ...
    },
    "result": {
        ...
        "content": ".... html content ... too long for the example",
        "content_encoding": "utf-8",
        "content_format": "raw",
        "content_type": "text/html; charset=utf-8",
        "duration": 3.7,
        "error": null,
        "extracted_data": {
            "content_type": "text/plain",
            "data": "In this document, what is the general sentiment about the product"
        },
        "format": "text",
        "reason": "OK",
        "request_headers": [],
        "response_headers": {
            ...
        },
        "status": "DONE",
        "status_code": 200,
        "success": true,
        "url": "https://web-scraping.dev/product/1"
    }
}
```

Try yourself:

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "tags=player,project:default" \
--data-urlencode "extraction_prompt=In this document, what is the general sentiment about the product" \
--data-urlencode "asp=true" \
--data-urlencode "render_js=true" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/reviews"
```

`https://api.scrapfly.io/scrape?tags=player%2Cproject%3Adefault&extraction_prompt=In+this+document%2C+what+is+the+general+sentiment+about+the+product&asp=true&render_js=true&key=&url=https%3A%2F%2Fweb-scraping.dev%2Freviews`

Choose one of pre-defined AI data models to extract common web page structures like products, reviews, item listings etc. automatically without any additional context. Scrapfly's extraction engine will find all relevant fields to the selected extraction model.

Our AI models are trained to extract specific object data from many different content types like HTML, JSON, XML, and more.

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "tags=player,project:default" \
--data-urlencode "extraction_model=product" \
--data-urlencode "asp=true" \
--data-urlencode "render_js=true" \
--data-urlencode "auto_scroll=true" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://web-scraping.dev/product/1"
```

`https://api.scrapfly.io/scrape?tags=player%2Cproject%3Adefault&extraction_model=product&asp=true&render_js=true&auto_scroll=true&key=&url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1`

All related errors are listed below. You can see full description and example of error response on the [Errors section](https://scrapfly.io/docs/extraction-api/errors).

*   [ERR::EXTRACTION::CONFIG_ERROR](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::CONFIG_ERROR) - Parameters sent to the API are not valid
*   [ERR::EXTRACTION::CONTENT_TYPE_NOT_SUPPORTED](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::CONTENT_TYPE_NOT_SUPPORTED) - The content type of the response is not supported for extraction.
*   [ERR::EXTRACTION::DATA_ERROR](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::DATA_ERROR) - Extracted data is invalid or have an issue
*   [ERR::EXTRACTION::INVALID_RULE](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::INVALID_RULE) - The extraction rule is invalid
*   [ERR::EXTRACTION::INVALID_TEMPLATE](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::INVALID_TEMPLATE) - The template used for extraction is invalid
*   [ERR::EXTRACTION::NO_CONTENT](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::NO_CONTENT) - Target response is empty
*   [ERR::EXTRACTION::OPERATION_TIMEOUT](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::OPERATION_TIMEOUT) - Extraction Operation Timeout
*   [ERR::EXTRACTION::OUT_OF_CAPACITY](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::OUT_OF_CAPACITY) - Not able to extract more data, backend are out of capacity, retry later.
*   [ERR::EXTRACTION::TEMPLATE_NOT_FOUND](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::TEMPLATE_NOT_FOUND) - The provided template do not exist
*   [ERR::EXTRACTION::TIMEOUT](https://scrapfly.io/docs/extraction-api/error/ERR::EXTRACTION::TIMEOUT) - The extraction was too long or did not had enough time to complete

[Pricing](https://scrapfly.io/docs/scrape-api/extraction#pricing)
-----------------------------------------------------------------

The Scrapfly Extraction API is billed as follows:

*   Extraction Template: **1 API Credits**
*   Extraction Prompt: **5 API Credits**
*   Extraction Model: **5 API Credits**

Each API request returns billing information about the used API credits. The `X-Scrapfly-Api-Cost` header contains the **total** amount of API credits used for this request.
