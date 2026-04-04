# Source: https://scrapfly.io/docs/extraction-api/automatic-ai

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/extraction-api/automatic-ai

Markdown Content:
AI Powered Data Extraction
--------------------------

Scrapfly's AI-powered automatic parser effortlessly converts unstructured HTML data into predefined, structured models. Experience precise and efficient data extraction with our advanced technology. It can ingest any text format like `HTML`, `text`, `Markdown`, `json`

Minimal API call is a `POST` request with `key` and `extraction_model` parameters:

`https://api.scrapfly.io/extraction?key=&extraction_model=`

[Usage](https://scrapfly.io/docs/extraction-api/automatic-ai#usage)
-------------------------------------------------------------------

1.    We will use [https://web-scraping.dev/product/1](https://web-scraping.dev/product/1) page as example and save its content to the current directory where you will run the curl command below as `product.html`
2.    We will use the [product](https://scrapfly.io/docs/extraction-api/automatic-ai/models/product) model to extract product information 
3.    Call the extraction API ```
curl -X POST \
-H "content-type: text/html" \
"https://api.scrapfly.io/extraction?key=&url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1&extraction_model=product" \
-d @product.html
``` 
> If you have `jq`available on your machine, you can pretty print the output JSON by appending it to the command like `-d @product.html | jq`.

Command Explanation
    *   **`curl -X POST`**: 
        *   `curl` is a command-line tool for transferring data with URLs.
        *   `-X POST` specifies the HTTP method to be used, which is POST in this case.

    *   **`-H "content-type: text/html"`**: 
        *   `-H` is used to specify an HTTP header for the request.
        *   `"content-type: text/html"` sets the Content-Type header to `text/html`, indicating that the data being sent is HTML.

    *   **URL**: 
        *   The URL of the API endpoint being accessed, including query parameters for authentication and specifying the target URL and extraction prompt.
        *   [`key`:](https://scrapfly.io/docs/extraction-api/getting-started#api_param_key) An API key for authentication. 
        *   [`url`:](https://scrapfly.io/docs/extraction-api/getting-started#api_param_url) The URL of the web page to be scraped, URL-encoded. 
        *   [`extraction_model`:](https://scrapfly.io/docs/extraction-api/getting-started#api_param_extraction_model) The AI model to use for extraction.

    *   **`-d @product.html`**: 
        *   `-d` is used to specify the data to be sent in the POST request body.
        *   `@product.html` indicates that the data should be read from a file named `product.html`.

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
            "content_type": "application/json",
            "data": {
                "additional_property": [],
                "aggregate_rating": null,
                "brand": "ChocoDelight",
                "breadcrumbs": null,
                "canonical_url": null,
                "color": null,
                "description": "Indulge your sweet tooth with our Box of Chocolate Candy. Each box contains an assortment of rich, flavorful chocolates with a smooth, creamy filling. Choose from a variety of flavors including zesty orange and sweet cherry. Whether you're looking for the perfect gift or just want to treat yourself, our Box of Chocolate Candy is sure to satisfy.",
                "identifiers": {
                    "ean13": null,
                    "gtin14": null,
                    "gtin8": null,
                    "isbn10": null,
                    "isbn13": null,
                    "ismn": null,
                    "issn": null,
                    "mpn": null,
                    "sku": null,
                    "upc": null
                },
                "images": [],
                "main_category": "Products",
                "main_image": null,
                "name": "Box of Chocolate Candy",
                "offers": [
                    {
                        "availability": "available",
                        "currency": "$",
                        "price": 9.99,
                        "regular_price": 12.99
                    }
                ],
                "related_products": [
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/red-potion.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/28",
                        "name": "Red Energy Potion",
                        "price": {
                            "amount": 4.99,
                            "currency": null,
                            "raw": "4.99"
                        }
                    },
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/darkred-potion.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/2",
                        "name": "Dark Red Energy Potion",
                        "price": {
                            "amount": 4.99,
                            "currency": null,
                            "raw": "4.99"
                        }
                    },
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/women-sandals-beige-1.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/8",
                        "name": "Women's High Heel Sandals",
                        "price": {
                            "amount": 59.99,
                            "currency": null,
                            "raw": "59.99"
                        }
                    },
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/red-potion.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/4",
                        "name": "Red Energy Potion",
                        "price": {
                            "amount": 4.99,
                            "currency": null,
                            "raw": "4.99"
                        }
                    }
                ],
                "secondary_category": null,
                "size": null,
                "specifications": [
                    {
                        "name": "material",
                        "value": "Premium quality chocolate"
                    },
                    {
                        "name": "flavors",
                        "value": "Available in Orange and Cherry flavors"
                    },
                    {
                        "name": "sizes",
                        "value": "Available in small, medium, and large boxes"
                    },
                    {
                        "name": "brand",
                        "value": "ChocoDelight"
                    },
                    {
                        "name": "care instructions",
                        "value": "Store in a cool, dry place"
                    },
                    {
                        "name": "purpose",
                        "value": "Ideal for gifting or self-indulgence"
                    }
                ],
                "style": null,
                "url": "https://web-scraping.dev/",
                "variants": [
                    {
                        "color": "orange",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=orange-small"
                    },
                    {
                        "color": "orange",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=orange-medium"
                    },
                    {
                        "color": "orange",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=orange-large"
                    },
                    {
                        "color": "cherry",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=cherry-small"
                    },
                    {
                        "color": "cherry",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=cherry-medium"
                    },
                    {
                        "color": "cherry",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=cherry-large"
                    }
                ]
            },
            "data_quality": {
                "errors": [
                    "identifiers.sku: Input should be a valid string"
                ],
                "fulfilled": false,
                "fulfillment_percent": 45
            }
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

[Models](https://scrapfly.io/docs/extraction-api/automatic-ai#models)
---------------------------------------------------------------------

> These models have been tailored based on customer feedback and usage. If you need a specific general model, you can contact us through the support link below. In addition, if the existing models are missing some important fields you can also request them to be added. 
> [Contact us](https://scrapfly.io/docs/support)

For automatic structured data extraction, choose a model from below and the AI will try to fulfill it from the scrape web page you provide

| Name | API name [`&extraction_model={model-name}`](https://scrapfly.io/docs/extraction-api/getting-started#api_param_extraction_model) |
| --- | --- |
| [Article](https://scrapfly.io/docs/extraction-api/automatic-ai/models/article) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`article` |
| [Event](https://scrapfly.io/docs/extraction-api/automatic-ai/models/event) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`event` |
| [Food Recipe](https://scrapfly.io/docs/extraction-api/automatic-ai/models/food_recipe) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`food_recipe` |
| [Hotel](https://scrapfly.io/docs/extraction-api/automatic-ai/models/hotel) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`hotel` |
| [Hotel Listing](https://scrapfly.io/docs/extraction-api/automatic-ai/models/hotel_listing) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`hotel_listing` |
| [Job Listing](https://scrapfly.io/docs/extraction-api/automatic-ai/models/job_listing) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`job_listing` |
| [Job Posting](https://scrapfly.io/docs/extraction-api/automatic-ai/models/job_posting) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`job_posting` |
| [Organization](https://scrapfly.io/docs/extraction-api/automatic-ai/models/organization) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`organization` |
| [Product](https://scrapfly.io/docs/extraction-api/automatic-ai/models/product) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`product` |
| [Product Listing](https://scrapfly.io/docs/extraction-api/automatic-ai/models/product_listing) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`product_listing` |
| [Real Estate Property](https://scrapfly.io/docs/extraction-api/automatic-ai/models/real_estate_property) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`real_estate_property` |
| [Real Estate Property Listing](https://scrapfly.io/docs/extraction-api/automatic-ai/models/real_estate_property_listing) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`real_estate_property_listing` |
| [Review List](https://scrapfly.io/docs/extraction-api/automatic-ai/models/review_list) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`review_list` |
| [Search Engine Results](https://scrapfly.io/docs/extraction-api/automatic-ai/models/search_engine_results) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`search_engine_results` |
| [Social Media Post](https://scrapfly.io/docs/extraction-api/automatic-ai/models/social_media_post) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`social_media_post` |
| [Software](https://scrapfly.io/docs/extraction-api/automatic-ai/models/software) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`software` |
| [Stock](https://scrapfly.io/docs/extraction-api/automatic-ai/models/stock) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`stock` |
| [Vehicle Ad](https://scrapfly.io/docs/extraction-api/automatic-ai/models/vehicle_ad) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`vehicle_ad` |
| [Vehicle Ad Listing](https://scrapfly.io/docs/extraction-api/automatic-ai/models/vehicle_ad_listing) | [](https://scrapfly.io/docs/extraction-api/automatic-ai# "Copy to clipboard")`vehicle_ad_listing` |

[Web Scraping API](https://scrapfly.io/docs/extraction-api/automatic-ai#web_scraping_api)
-----------------------------------------------------------------------------------------

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

#### API Response

You will retrieve the following information from the API response `result.extracted_data`

*   `result.extracted_data.content_type`: Always be JSON
*   `result.extracted_data.data`: Structured extracted data
*   `result.extracted_data.data_quality`
    *   **errors** Will give the list of data violations that do not follow the validation schema
    *   **fulfilled** A boolean indicating whether the schema is fully satisfied.
    *   **fulfillment_percent** The percentage of fulfillment, where 0 indicates empty and 100 indicates perfect.

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
            "content_type": "application/json",
            "data": {
                "additional_property": [],
                "aggregate_rating": null,
                "brand": "ChocoDelight",
                "breadcrumbs": null,
                "canonical_url": null,
                "color": null,
                "description": "Indulge your sweet tooth with our Box of Chocolate Candy. Each box contains an assortment of rich, flavorful chocolates with a smooth, creamy filling. Choose from a variety of flavors including zesty orange and sweet cherry. Whether you're looking for the perfect gift or just want to treat yourself, our Box of Chocolate Candy is sure to satisfy.",
                "identifiers": {
                    "ean13": null,
                    "gtin14": null,
                    "gtin8": null,
                    "isbn10": null,
                    "isbn13": null,
                    "ismn": null,
                    "issn": null,
                    "mpn": null,
                    "sku": null,
                    "upc": null
                },
                "images": [],
                "main_category": "Products",
                "main_image": null,
                "name": "Box of Chocolate Candy",
                "offers": [
                    {
                        "availability": "available",
                        "currency": "$",
                        "price": 9.99,
                        "regular_price": 12.99
                    }
                ],
                "related_products": [
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/red-potion.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/28",
                        "name": "Red Energy Potion",
                        "price": {
                            "amount": 4.99,
                            "currency": null,
                            "raw": "4.99"
                        }
                    },
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/darkred-potion.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/2",
                        "name": "Dark Red Energy Potion",
                        "price": {
                            "amount": 4.99,
                            "currency": null,
                            "raw": "4.99"
                        }
                    },
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/women-sandals-beige-1.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/8",
                        "name": "Women's High Heel Sandals",
                        "price": {
                            "amount": 59.99,
                            "currency": null,
                            "raw": "59.99"
                        }
                    },
                    {
                        "availability": "available",
                        "description": null,
                        "images": [
                            {
                                "url": "https://web-scraping.dev/assets/products/red-potion.webp"
                            }
                        ],
                        "link": "https://web-scraping.dev/product/4",
                        "name": "Red Energy Potion",
                        "price": {
                            "amount": 4.99,
                            "currency": null,
                            "raw": "4.99"
                        }
                    }
                ],
                "secondary_category": null,
                "size": null,
                "specifications": [
                    {
                        "name": "material",
                        "value": "Premium quality chocolate"
                    },
                    {
                        "name": "flavors",
                        "value": "Available in Orange and Cherry flavors"
                    },
                    {
                        "name": "sizes",
                        "value": "Available in small, medium, and large boxes"
                    },
                    {
                        "name": "brand",
                        "value": "ChocoDelight"
                    },
                    {
                        "name": "care instructions",
                        "value": "Store in a cool, dry place"
                    },
                    {
                        "name": "purpose",
                        "value": "Ideal for gifting or self-indulgence"
                    }
                ],
                "style": null,
                "url": "https://web-scraping.dev/",
                "variants": [
                    {
                        "color": "orange",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=orange-small"
                    },
                    {
                        "color": "orange",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=orange-medium"
                    },
                    {
                        "color": "orange",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=orange-large"
                    },
                    {
                        "color": "cherry",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=cherry-small"
                    },
                    {
                        "color": "cherry",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=cherry-medium"
                    },
                    {
                        "color": "cherry",
                        "offers": [
                            {
                                "availability": "available",
                                "price": {
                                    "amount": null,
                                    "currency": null,
                                    "raw": null
                                }
                            }
                        ],
                        "sku": "https://web-scraping.dev/product/1?variant=cherry-large"
                    }
                ]
            },
            "data_quality": {
                "errors": [
                    "identifiers.sku: Input should be a valid string"
                ],
                "fulfilled": false,
                "fulfillment_percent": 45
            }
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

[Pricing](https://scrapfly.io/docs/extraction-api/automatic-ai#pricing)
-----------------------------------------------------------------------

Extraction model is billed **5 API Credits**.

For more information about the pricing you can [learn more on the dedicated section](https://scrapfly.io/docs/extraction-api/billing)
