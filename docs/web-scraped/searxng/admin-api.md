# Source: https://docs.searxng.org/admin/api.html

[]

# Administration API[¶](#administration-api "Link to this heading")

## Get configuration data[¶](#get-configuration-data "Link to this heading")

    GET /config  HTTP/1.1

### Sample response[¶](#sample-response "Link to this heading")

    ,
        ,
        ,
        ,
      ],
      "instance_name": "SearXNG",
      "locales": ,
      "plugins": [
        
      ],
      "safe_search": 0
    }

## Embed search bar[¶](#embed-search-bar "Link to this heading")

The search bar can be embedded into websites. Just paste the example into the HTML of the site. URL of the SearXNG instance and values are customizable.

    <form method="post" action="https://example.org/">
      <!-- search      --> <input type="text" name="q">
      <!-- categories  --> <input type="hidden" name="categories" value="general,social media">
      <!-- language    --> <input type="hidden" name="lang" value="all">
      <!-- locale      --> <input type="hidden" name="locale" value="en">
      <!-- date filter --> <input type="hidden" name="time_range" value="month">
    </form>