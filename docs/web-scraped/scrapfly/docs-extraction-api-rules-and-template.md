# Source: https://scrapfly.io/docs/extraction-api/rules-and-template

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/extraction-api/rules-and-template

Markdown Content:
Extraction Rules and Template
-----------------------------

The extraction templates allow defining custom extraction JSON rules for parsing data from HTML, XML and JSON documents and generate structured JSON output. In other words, using JSON definition we can tell the API where to find data, how to extract it and format it.

This tool is a great service for developers who are familiar with data parsing tools like CSS selectors, XPath or JMESPath as it provides full control over the extraction but still saves a lot of time by handling the most complex parts of data parsing.

Minimal API call is a `POST` request with `key` and `extraction_template` parameters:

`https://api.scrapfly.io/extraction?key=&extraction_template=ephemeral:{template_base64}`

#### Key Features:

*   **Customizable Rules:** Define your own extraction rules to tailor data extraction according to your needs.
*   **Versatile Data Sources:** Extract data from various content types including HTML, JSON, and XML.
*   **Structured Output:** Retrieve well-structured data in JSON format, making it easier to process and analyze.

Template Specification
----------------------

 Structure of the extraction template 

*   **source** string 
The source of the expected data, either 'html' or 'json'.

_Default Value: html_
*   **name** string 
Name of the template - only used for persistent templates.

_Default Value: ephemeral_
*   **version** string 
The version of the document - only used for persistent templates.

_Default Value: @latest_
*   **match** object 
Match the template for the given URL.

    *   **domain** string 
Match against the current domain

    *   **path** string 
Match against the current path

*   **selectors** array 

###### Items  object

    *   **name** string 
The name of the data field to extract.

    *   **type** string 
The type of selector to use.

    *   **options** object 
selector options

    *   **cast** string 
Cast the value in the given type.

    *   **multiple** boolean 
When multiple is true, capture all matched content.

    *   **query** string 
The query string for the selector.

    *   **formatters** array 

###### Items  object

        *   **name** string 
The type of formatter to apply.

        *   **args** object 
Optional arguments for the formatter.

    *   **extractor** object 

        *   **name** string 
The extractor to apply - Extractor are executed before formatters.

        *   **args** object 
Optional arguments for the extractor.

    *   **nested** array 
Nested selectors for each item in the list.

###### Items #/properties/selectors/items (Recursion) 

 JSON schema Validation 

```
{
    "type": "object",
    "properties": {
        "source": {
            "type": "string",
            "description": "The source of the expected data, either 'html' or 'json'.",
            "default": "html"
        },
        "name": {
            "type": "string",
            "description": "Name of the template - only used for persistent templates.",
            "default": "ephemeral"
        },
        "version": {
            "type": "string",
            "description": "The version of the document - only used for persistent templates.",
            "default": "@latest"
        },
        "match": {
            "type": "object",
            "description": "Match the template for the given URL.",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Match against the current domain"
                },
                "path": {
                    "type": "string",
                    "description": "Match against the current path"
                }
            }
        },
        "selectors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "The name of the data field to extract."
                    },
                    "type": {
                        "type": "string",
                        "enum": [
                            "css",
                            "xpath",
                            "jmespath",
                            "regex"
                        ],
                        "description": "The type of selector to use."
                    },
                    "options": {
                        "type": "object",
                        "description": "selector options"
                    },
                    "cast": {
                        "type": "string",
                        "enum": [
                            "int",
                            "float",
                            "bool"
                        ],
                        "description": "Cast the value in the given type."
                    },
                    "multiple": {
                        "type": "boolean",
                        "description": "When multiple is true, capture all matched content."
                    },
                    "query": {
                        "type": "string",
                        "description": "The query string for the selector."
                    },
                    "formatters": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "enum": [
                                        "pick",
                                        "trim",
                                        "unquote",
                                        "unique",
                                        "lowercase",
                                        "uppercase",
                                        "datetime",
                                        "titleize",
                                        "capitalize",
                                        "slugify",
                                        "replace",
                                        "split",
                                        "join",
                                        "json_decode",
                                        "url_encode",
                                        "url_decode",
                                        "base64_encode",
                                        "base64_decode",
                                        "remove_html",
                                        "absolute_url"
                                    ],
                                    "description": "The type of formatter to apply."
                                },
                                "args": {
                                    "type": "object",
                                    "description": "Optional arguments for the formatter."
                                }
                            },
                            "required": [
                                "name"
                            ]
                        }
                    },
                    "extractor": {
                        "type": "object",
                        "properties": {
                            "name": {
                                "type": "string",
                                "enum": [
                                    "price",
                                    "image",
                                    "links",
                                    "emails"
                                ],
                                "description": "The extractor to apply - Extractor are executed before formatters."
                            },
                            "args": {
                                "type": "object",
                                "description": "Optional arguments for the extractor."
                            }
                        },
                        "required": [
                            "name"
                        ]
                    },
                    "nested": {
                        "type": "array",
                        "description": "Nested selectors for each item in the list.",
                        "items": {
                            "$ref": "#/properties/selectors/items"
                        }
                    }
                },
                "required": [
                    "name",
                    "type",
                    "query"
                ]
            }
        }
    },
    "required": [
        "source",
        "selectors"
    ]
}
```

_To learn about [JSON schema](https://json-schema.org/)_

### [Template Example and Output](https://scrapfly.io/docs/extraction-api/rules-and-template#learn_by_example)

This example template will extract various data to illustrate all available features from the playground website `https://web-scraping.dev/product/1`

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

[Usage](https://scrapfly.io/docs/extraction-api/rules-and-template#usage)
-------------------------------------------------------------------------

1.   **Prepare your content**
For the examples below we will use HTML data from [https://web-scraping.dev/product/1](https://web-scraping.dev/product/1). To follow along save its contents to the current directory under `product.html`

`curl https://web-scraping.dev/product/1 -o product.html` 
2.   **Create your extraction template**
The template consists of 2 primary root keys: `source` which indicates parsed content type (usually `html`) and `selectors` which is an array defining all of the extraction instructions. Here's an example:

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
Then we will send this template in `base64` format. To send base64 url-encoded data, you can take a look on [our base64 tool](https://scrapfly.io/web-scraping-tools/base64)

3.   **Call the API**
Call the extraction endpoint with `extraction_template` parameter set to the base64 encoded template with `ephemeral:` prefix:

```
curl -X POST \
-H "content-type: text/html" \
"https://api.scrapfly.io/extraction?key=&url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1&extraction_template=ephemeral:ewogICAgInNvdXJjZSI6ICJodG1sIiwKICAgICJzZWxlY3RvcnMiOiBbCiAgICAgICAgewogICAgICAgICAgICAibmFtZSI6ICJkZXNjcmlwdGlvbiIsCiAgICAgICAgICAgICJxdWVyeSI6ICJwLnByb2R1Y3QtZGVzY3JpcHRpb246OnRleHQiLAogICAgICAgICAgICAidHlwZSI6ICJjc3MiCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJuYW1lIjogInByaWNlX2Jsb2NrIiwKICAgICAgICAgICAgIm5lc3RlZCI6IFsKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAiZXh0cmFjdG9yIjogewogICAgICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJwcmljZSIKICAgICAgICAgICAgICAgICAgICB9LAogICAgICAgICAgICAgICAgICAgICJmb3JtYXR0ZXJzIjogWwogICAgICAgICAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAiYXJncyI6IHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAia2V5IjogImN1cnJlbmN5IgogICAgICAgICAgICAgICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJuYW1lIjogInBpY2siCiAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICBdLAogICAgICAgICAgICAgICAgICAgICJuYW1lIjogInByaWNlX3JlZ2V4IiwKICAgICAgICAgICAgICAgICAgICAib3B0aW9ucyI6IHsKICAgICAgICAgICAgICAgICAgICAgICAgImNvbnRlbnQiOiAidGV4dCIsCiAgICAgICAgICAgICAgICAgICAgICAgICJkb3RhbGwiOiB0cnVlLAogICAgICAgICAgICAgICAgICAgICAgICAiaWdub3JlY2FzZSI6IHRydWUsCiAgICAgICAgICAgICAgICAgICAgICAgICJtdWx0aWxpbmUiOiBmYWxzZQogICAgICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICAgICAgInF1ZXJ5IjogIihcXCRcXGR7Mn1cXC5cXGR7Mn0pIiwKICAgICAgICAgICAgICAgICAgICAidHlwZSI6ICJyZWdleCIKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgXSwKICAgICAgICAgICAgInF1ZXJ5IjogIi5wcm9kdWN0LWRhdGEgZGl2LnByaWNlIiwKICAgICAgICAgICAgInR5cGUiOiAiY3NzIgogICAgICAgIH0sCiAgICAgICAgewogICAgICAgICAgICAibmFtZSI6ICJwcmljZV9mcm9tX2h0bWwiLAogICAgICAgICAgICAibmVzdGVkIjogWwogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICJmb3JtYXR0ZXJzIjogWwogICAgICAgICAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJ1cHBlcmNhc2UiCiAgICAgICAgICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJuYW1lIjogInJlbW92ZV9odG1sIgogICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgXSwKICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJwcmljZV9odG1sX3JlZ2V4IiwKICAgICAgICAgICAgICAgICAgICAibmVzdGVkIjogWwogICAgICAgICAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAibXVsdGlwbGUiOiB0cnVlLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAicHJpY2UgcmVnZXgiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgInF1ZXJ5IjogIi4rIiwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJ0eXBlIjogInJlZ2V4IgogICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgXSwKICAgICAgICAgICAgICAgICAgICAicXVlcnkiOiAiLisiLAogICAgICAgICAgICAgICAgICAgICJ0eXBlIjogInJlZ2V4IgogICAgICAgICAgICAgICAgfQogICAgICAgICAgICBdLAogICAgICAgICAgICAicXVlcnkiOiAiLnByb2R1Y3QtZGF0YSBkaXYucHJpY2UiLAogICAgICAgICAgICAidHlwZSI6ICJjc3MiCiAgICAgICAgfSwKICAgICAgICB7CiAgICAgICAgICAgICJleHRyYWN0b3IiOiB7CiAgICAgICAgICAgICAgICAibmFtZSI6ICJwcmljZSIKICAgICAgICAgICAgfSwKICAgICAgICAgICAgIm5hbWUiOiAicHJpY2UiLAogICAgICAgICAgICAicXVlcnkiOiAic3Bhbi5wcm9kdWN0LXByaWNlOjp0ZXh0IiwKICAgICAgICAgICAgInR5cGUiOiAiY3NzIgogICAgICAgIH0sCiAgICAgICAgewogICAgICAgICAgICAiZm9ybWF0dGVycyI6IFsKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJhYnNvbHV0ZV91cmwiCiAgICAgICAgICAgICAgICB9LAogICAgICAgICAgICAgICAgewogICAgICAgICAgICAgICAgICAgICJuYW1lIjogInVuaXF1ZSIKICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgXSwKICAgICAgICAgICAgIm11bHRpcGxlIjogdHJ1ZSwKICAgICAgICAgICAgIm5hbWUiOiAicGFnZV9saW5rcyIsCiAgICAgICAgICAgICJxdWVyeSI6ICJcL1wvYVwvQGhyZWYiLAogICAgICAgICAgICAidHlwZSI6ICJ4cGF0aCIKICAgICAgICB9LAogICAgICAgIHsKICAgICAgICAgICAgImZvcm1hdHRlcnMiOiBbCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAiYWJzb2x1dGVfdXJsIgogICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJ1bmlxdWUiCiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIF0sCiAgICAgICAgICAgICJtdWx0aXBsZSI6IHRydWUsCiAgICAgICAgICAgICJuYW1lIjogInBhZ2VfaW1hZ2VzIiwKICAgICAgICAgICAgInF1ZXJ5IjogIlwvXC9pbWdcL0BzcmMiLAogICAgICAgICAgICAidHlwZSI6ICJ4cGF0aCIKICAgICAgICB9LAogICAgICAgIHsKICAgICAgICAgICAgIm5hbWUiOiAicmV2aWV3cyIsCiAgICAgICAgICAgICJuZXN0ZWQiOiBbCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgImNhc3QiOiAiZmxvYXQiLAogICAgICAgICAgICAgICAgICAgICJuYW1lIjogInJhdGluZyIsCiAgICAgICAgICAgICAgICAgICAgInF1ZXJ5IjogImNvdW50KFwvXC9zdmcpIiwKICAgICAgICAgICAgICAgICAgICAidHlwZSI6ICJ4cGF0aCIKICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAgICAgImZvcm1hdHRlcnMiOiBbCiAgICAgICAgICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICJhcmdzIjogewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICJmb3JtYXQiOiAiJWRcLyVtXC8lWSIKICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0sCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJkYXRldGltZSIKICAgICAgICAgICAgICAgICAgICAgICAgfQogICAgICAgICAgICAgICAgICAgIF0sCiAgICAgICAgICAgICAgICAgICAgIm5hbWUiOiAiZGF0ZSIsCiAgICAgICAgICAgICAgICAgICAgInF1ZXJ5IjogIlwvXC9zcGFuWzFdXC90ZXh0KCkiLAogICAgICAgICAgICAgICAgICAgICJ0eXBlIjogInhwYXRoIgogICAgICAgICAgICAgICAgfSwKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAibmFtZSI6ICJ0ZXh0IiwKICAgICAgICAgICAgICAgICAgICAicXVlcnkiOiAiXC9cL3BbMV1cL3RleHQoKSIsCiAgICAgICAgICAgICAgICAgICAgInR5cGUiOiAieHBhdGgiCiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIF0sCiAgICAgICAgICAgICJxdWVyeSI6ICIjcmV2aWV3cyA-IGRpdi5yZXZpZXciLAogICAgICAgICAgICAidHlwZSI6ICJjc3MiCiAgICAgICAgfQogICAgXQp9" \
-d @product.html
``` 

Command Explanation
This command uses `curl` to send a POST request to an API endpoint with specified headers and data.

##### Components

    *   **`curl -X POST`**: 
        *   `curl` is a command-line tool for transferring data with URLs.
        *   `-X POST` specifies the HTTP method to be used, which is POST in this case.

    *   **`-H "content-type: text/html"`**: 
        *   `-H` is used to specify an HTTP header for the request.
        *   `"content-type: text/html"` sets the Content-Type header to `text/html`, indicating that the data being sent is HTML.

    *   **URL**: 
        *   The URL of the API endpoint being accessed, including query parameters for authentication and specifying the target URL and extraction template.
        *   [`key`](https://scrapfly.io/docs/extraction-api/getting-started#api_param_key): An API key for authentication.
        *   [`url`](https://scrapfly.io/docs/extraction-api/getting-started#api_param_url): The URL of the web page to be scraped, URL-encoded.
        *   [`extraction_template`](https://scrapfly.io/docs/extraction-api/getting-started#api_param_extraction_template): A base64-encoded string representing the extraction template.

    *   **`-d @product.html`**: 
        *   `-d` is used to specify the data to be sent in the POST request body.
        *   `@product.html` indicates that the data should be read from a file named `product.html`.

4.   **Retrieve the Results**
The API will return the extracted data in JSON format. For example:

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

### [Web Scraping API](https://scrapfly.io/docs/extraction-api/rules-and-template#web_scraping_api)

[Consult the full documentation about extraction with the Web Scraping API](https://scrapfly.io/docs/scrape-api/getting-started#api_param_extraction_template)

When using extraction through the Web Scraping API, you will scrape the content, and then extract the data from it:

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

> To extract directly the data while using the [Web Scraping API](https://scrapfly.io/docs/scrape-api/extraction), you must pass the template like `extraction_template=ephemeral:base64(template)`when you pass the template on the fly, or use a template saved from your dashboard `extraction_template=my-template`. 
> 
> _(Saved template are coming soon)_

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

[Extraction Rules](https://scrapfly.io/docs/extraction-api/rules-and-template#rules)
------------------------------------------------------------------------------------

Extraction rules will instruct what to retrieve and how. By default it returns the first matched element, you can set `multiple: true` to retrieve all matched elements

### [CSS Selector](https://scrapfly.io/docs/extraction-api/rules-and-template#css_selector)

Extracts data using CSS selectors with some extra features:

*   `::attr(attribute_name)` retrieve the attribute values
*   `::text` retrieve the text node

```
{
    "selectors": [
        {
            "name": "description",
            "query": "p.product-description::text",
            "type": "css"
        }
    ]
}
```

```
{
    "description": "Indulge your sweet tooth with our Box of Chocolate Candy. Each box contains an assortment of rich, flavorful chocolates with a smooth, creamy filling. Choose from a variety of flavors including zesty orange and sweet cherry. Whether you're looking for the perfect gift or just want to treat yourself, our Box of Chocolate Candy is sure to satisfy."
}
```

### [XPath Selector](https://scrapfly.io/docs/extraction-api/rules-and-template#xpath_selector)

Extracts data using XPath expressions.

```
{
    "selectors": [
        {
            "name": "page_links",
            "query": "//a/@href",
            "type": "xpath",
            "multiple": true // Capture all matched content, by default return the first element
        }
    ]
}
```

```
{
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
        ...
    ]
}
```

### [JMESPath Selector](https://scrapfly.io/docs/extraction-api/rules-and-template#jmespath_selector)

Extracts data from JSON using JMESPath expressions.

```
{
    "selectors": [
        {
            "name": "price",
            "query": "items[?name=='price'].value",
            "type": "jmespath"
        }
    ]
}
```
`$9.99`
### [Regex Selector](https://scrapfly.io/docs/extraction-api/rules-and-template#regex_selector)

Extracts data using regular expressions.

```
{
    "selectors": [
        {
            "name": "price",
            "query": "(\\$\\d{2}\\.\\d{2})",
            "type": "regex"
        }
    ]
}
```

```
{
    "price regex": "USD"
}
```

### [Nested Selectors](https://scrapfly.io/docs/extraction-api/rules-and-template#nested_selectors)

You can structure your schema by using nested selector, it also simplify the query. All available selectors can be used

**Example:**

```
{
    "selectors": [
        {
            "name": "reviews",
          	"query": "div.product-reviews",
            "type": "css",
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

```
{
    "price html block": [
        {
            "product": [
                {
                    "name": "description",
                    "query": "p.product-description::text",
                    "type": "css"
                },
            ]
        }
    ]
}
```

Extractors are applied before formatters and are used to extract specific types of data. It helps a lot to convert specific type of data into a structured and normalized format

Extracts price information.

```
{
    "extractor": {
        "name": "price"
    },
    "name": "price",
    "query": ".price::text",
    "type": "css"
}
```

Extracts image URLs.

```
{
    "extractor": {
        "name": "image"
    },
    "name": "product_images",
    "query": "//img/@src",
    "type": "xpath"
}
```

Extracts hyperlinks.

```
{
    "extractor": {
        "name": "links"
    },
    "name": "page_links",
    "query": "//a/@href",
    "type": "xpath"
}
```

Extracts email addresses.

```
{
    "extractor": {
        "name": "emails"
    },
    "name": "contact_emails",
    "query": "//body",
    "type": "xpath"
}
```

[Formatters](https://scrapfly.io/docs/extraction-api/rules-and-template#formatters)
-----------------------------------------------------------------------------------

Formatters are applied in the order they are specified and are used to transform the extracted data.

Example of formater usage
```
{
    "selectors": [
      {
        "name": "title",
        "type": "css",
        "query": "title::text",
        "formatters": [{"name": "trim"}]
      },
      {
        "name": "links",
        "type": "xpath",
        "multiple": true,
        "query": "//a/@href",
        "formatters": [
          {"name": "absolute_url"},
          {"name": "unique"}
        ]
      }
    ]
}
```

### [trim](https://scrapfly.io/docs/extraction-api/rules-and-template#trim)

*   **Description:** Trims whitespace from the extracted data.

### [pick](https://scrapfly.io/docs/extraction-api/rules-and-template#pick)

*   **Description:** Picks a specific key from a dictionary.
*   **Arguments:**
*       *   `key`: The key to pick from the dictionary. Required and case-sensitive

If the key do not exist, return null

### [unique](https://scrapfly.io/docs/extraction-api/rules-and-template#unique)

*   **Description:** Ensures the extracted data contains unique values.

### [unquote](https://scrapfly.io/docs/extraction-api/rules-and-template#unquote)

*   **Description:** Decodes a URL-encoded string.

### [lowercase](https://scrapfly.io/docs/extraction-api/rules-and-template#lowercase)

*   **Description:** Converts the extracted data to lowercase.

### [uppercase](https://scrapfly.io/docs/extraction-api/rules-and-template#uppercase)

*   **Description:** Converts the extracted data to uppercase.

### [datetime](https://scrapfly.io/docs/extraction-api/rules-and-template#datetime)

*   **Description:** Formats date strings.
*   **Arguments:**
*       *   `format`: The format to convert the date string into. Default is `%Y-%m-%d`. 

### [titleize](https://scrapfly.io/docs/extraction-api/rules-and-template#titleize)

*   **Description:** Converts the extracted data to title case.

### [capitalize](https://scrapfly.io/docs/extraction-api/rules-and-template#capitalize)

*   **Description:** Capitalizes the first letter of the extracted data.

### [slugify](https://scrapfly.io/docs/extraction-api/rules-and-template#slugify)

*   **Description:** Converts the extracted data into a URL slug.
*   **Arguments:**
*       *   `separator`: The separator to use for the slug. Default is `-`.

### [replace](https://scrapfly.io/docs/extraction-api/rules-and-template#replace)

*   **Description:** Replaces occurrences of a string with another string.
*   **Arguments:**
*       *   `search`: The string to search for. (Required)
    *   `replace`: The string to replace with. (Required)

### [split](https://scrapfly.io/docs/extraction-api/rules-and-template#split)

*   **Description:** Splits the extracted data by a delimiter.
*   **Arguments:**
*       *   `delimiter`: The delimiter to split the string by. (Required)

### [join](https://scrapfly.io/docs/extraction-api/rules-and-template#join)

*   **Description:** Joins an iterable of strings into a single string with a delimiter. 
*   **Arguments:**
*       *   `delimiter`: The delimiter to join the strings with. (Required)

### [json_decode](https://scrapfly.io/docs/extraction-api/rules-and-template#json_decode)

*   **Description:** Decodes a JSON string into a Python object.
*   **Arguments:**
*       *   `fail_silently`: Whether to fail silently if decoding fails. Default is `false`. 

### [url_encode](https://scrapfly.io/docs/extraction-api/rules-and-template#url_encode)

*   **Description:** Encodes a string into URL format.

### [url_decode](https://scrapfly.io/docs/extraction-api/rules-and-template#url_decode)

*   **Description:** Decodes a URL-encoded string.

### [base64_encode](https://scrapfly.io/docs/extraction-api/rules-and-template#base64_encode)

*   **Description:** Encodes a string into Base64 format.

### [base64_decode](https://scrapfly.io/docs/extraction-api/rules-and-template#base64_decode)

*   **Description:** Decodes a Base64-encoded string.

### [remove_html](https://scrapfly.io/docs/extraction-api/rules-and-template#remove_html)

*   **Description:** Removes HTML tags from the extracted data.

### [absolute_url](https://scrapfly.io/docs/extraction-api/rules-and-template#absolute_url)

*   **Description:** Converts a relative URL to an absolute URL based on the base URL.

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

[Pricing](https://scrapfly.io/docs/extraction-api/rules-and-template#pricing)
-----------------------------------------------------------------------------

Template extraction is billed **1 API Credits**.

For more information about the pricing you can [learn more on the dedicated section](https://scrapfly.io/docs/extraction-api/billing)
