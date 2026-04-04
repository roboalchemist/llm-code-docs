# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/data-parsing/parsing-templates.md

# Parsing Templates

<mark style="color:purple;">**`Nimble Labs Beta Feature`**</mark>

Parsing templates allow users to accurately extract specific snippets or key data points from a webpage. By using industry-standard CSS selectors, parsing templates can extract data precisely from almost any webpage.

<div data-full-width="true"><figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/DDJbjIouxdvpfD9p42gL/Full.png" alt=""><figcaption></figcaption></figure></div>

Parsing templates also come with a variety of options designed to make data extraction a breeze, such as built-in support for tables, JSON output, and custom objects. They make use of the same framework used by other popular parsing libraries such as Beautiful Soup, making for an easy and familiar experience.

{% hint style="warning" %}
When using parsing templates, it's important to monitor changes in the source webpage structure and its effect on parsing templates. Nimble does not maintain or update custom parsing templates.
{% endhint %}

### Table of contents

* [Quick start examples](#quick-start-examples)
  * [Extracting text](#example-1-extracting-text)
  * [Extracting tables](#example-2-extracting-tables)
  * [Extracting repeating elements](#example-3-extracting-repeating-elements)
  * [Advanced example - Using object-list](#advanced-example-using-object-list)
* [Parsing template syntax](#parsing-template-syntax)
  * [Types](#types)
  * [Extractors](#extractors)
  * [Objects](#objects)
  * [Object lists](#object-lists)
* [Implementing parsing templates](#implementing-parsing-templates)
* [Managing parsing templates](#managing-parsing-templates)

### Quick start examples

In the following examples, we'll be using a single page through, and demonstrate the best way to go about parsing specific snippets in a real-world situation. The page we'll be using is the ESPN NBA page for the Boston Celtics, as it appeared circa June 2023. This page may have changed since the writing of this guide, and should only be used as an example.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/cVM6ZDM6EDQ6xyvyBzyx/Clean.png" alt=""><figcaption></figcaption></figure>

In the following examples, we'll demonstrate how to extract the name of the team, the team standings table, and the titles and link URLs of the articles displayed on the page.

<details>

<summary>Example 1 - extracting text</summary>

We'll start off by parsing out the name of the team, as it appears in the top left of the page. If we examine the HTML surrounding the title, we see the following structure:

```html
<h1 class="ClubhouseHeader__Name ttu flex items-start n2">
    <span class="flex flex-wrap">
        <span class="db pr3 nowrap">Boston</span>
        <span class="db fw-bold">Celtics</span>
    </span>
</h1>
```

The class `ClubhouseHeader__Name` is unique, and appears only once on this page, so we can use it to target the name of the team accurately. Although the H1 container has several `spans` inside, we'll be able to parse out just the contents and get the name of the team.

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/2Ni53MFEqBTqjQzUca6k/Team%20Name.png)

To get the name of the team, we'll use the following request:

<pre class="language-bash"><code class="lang-bash"><strong>curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
</strong>--header 'Authorization: Basic &#x3C;credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics",
    "parse": true,
    "format": "json",
    "render": true,
    "country": "US",
    "parser": {
        "team_name": {
            "type": "item",
            "selectors": [".ClubhouseHeader__Name"],
            "extractor": "text"
        }
    }
}'
</code></pre>

Firstly, notice that we've set `parse` to `true` and `format` to `json` - these are required for parsing templates to work correctly.

Next, let's examine the `parser` setting, where the parsing template itself is defined.&#x20;

On the first line, we've set the name of the first parsing template - `team_name`. This name will also be used in the response we get back, where this name will be attached to the parsing output. Within the team\_name template, we've set three parameters:

* [x] **type** - establishes the type of data we'll be targeting. In this case, we use `item` because we're targeting a single element, and wish to return its contents.
* [x] **selectors** - the CSS selector that identifies the element we are targeting. In this case, we used `.ClubhouseHeader__Name` because it was unique and encapsulated all of the text we wanted.&#x20;
* [x] **extractor** - extractors define what part of a matched element should be returned. In this case, we used text in order to clean all of the HTML and get just the actual name of the team.

The output for this request returned:

```json
{
    "status": "success",
    "query_time": "2023-06-06T14:06:44.986Z",
    "status_code": 200,
    "html_content": "...",
    "headers": {
        ...
    },
    "parsing": {
        "team_name": "BostonCeltics"
    },
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics"
}
```

In this example, we defined the parsing template inline, or within the request body. However, we recommend uploading your parsing templates and simply referring to them in each call for a more smooth experience at scale.

See the [Implementing Parsing Templates](#implementing-parsing-templates) section further down for more information.

</details>

<details>

<summary>Example 2 - extracting tables</summary>

Having parsed the name of the team, we're now interested in parsing additional data. On the right side of the page, we can see the standings table, and wish to add that to our request. When we examine the table, we see the following HTML structure:

<pre class="language-html"><code class="lang-html">&#x3C;section class="Card TeamStandings">
  ...
<strong>  &#x3C;table style="border-collapse:collapse;border-spacing:0" class="Table Table--align-right">
</strong>    &#x3C;colgroup class="Table__Colgroup">
      &#x3C;col class="Table__Column">
      &#x3C;col class="Table__Column">
      &#x3C;col class="Table__Column">
      &#x3C;col class="Table__Column">
      &#x3C;col class="Table__Column">
      &#x3C;col class="Table__Column">
    &#x3C;/colgroup>
    &#x3C;thead class="Table__THEAD">
      &#x3C;tr class="Table__TR Table__even">
        &#x3C;th title="" class="Table__TH">Team&#x3C;/th>
        &#x3C;th title="" class="Table__TH">W&#x3C;/th>
        &#x3C;th title="" class="Table__TH">L&#x3C;/th>
        &#x3C;th title="" class="Table__TH">PCT&#x3C;/th>
        &#x3C;th title="" class="Table__TH">GB&#x3C;/th>
        &#x3C;th title="" class="Table__TH">STRK&#x3C;/th>
      &#x3C;/tr>
    &#x3C;/thead>
    &#x3C;tbody class="Table__TBODY">
      &#x3C;tr class="Table__TR Table__TR--sm Table__even" data-idx="0">
        &#x3C;td class="Table__TD">
          &#x3C;a class="AnchorLink fw-bold" tabindex="0" href="/nba/team/_/name/bos/boston-celtics">Boston&#x3C;/a>
        &#x3C;/td>
        &#x3C;td class="fw-bold clr-gray-01 Table__TD">
          &#x3C;span class="fw-bold clr-gray-01">57&#x3C;/span>
        &#x3C;/td>
        &#x3C;td class="fw-bold clr-gray-01 Table__TD">
          &#x3C;span class="fw-bold clr-gray-01">25&#x3C;/span>
        &#x3C;/td>
        ...
    &#x3C;/tbody>
  &#x3C;/table>
&#x3C;/section>
</code></pre>

To target this table, we'll use two selectors in conjunction. The `.TeamStandings` class is unique, and helps us define a narrow scope, and the `table` selector allows us to directly select the table within the `.TeamStandings` class.

<img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/5MDX1xCuA0ayCV3cfiJk/Table.png" alt="" data-size="original">

To get the standings table and the team name, we'll use the following request:

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics",
    "parse": true,
    "format": "json",
    "render": true,
    "country": "US",
    "parser": {
        "team_name": {
            "type": "item",
            "selectors": [".ClubhouseHeader__Name"],
            "extractor": "text"
        },
        "team_standings": {
            "type": "table",
            "selectors": [".TeamStandings table"],
            "extractor": "text"
        }
    }
}'
```

We can use multiple parsing templates by simply defining each one with a unique name and separating them with a comma. For the team standings parsing template, we've set the following parameters:

* [x] **type** - we've used the `table` type here, which can automatically convert HTML tables into JSON and uses the header row as keys.
* [x] **selector** - we've used the `.TeamStandings table` selector to target the first table within the `TeamStandings` class.
* [x] **extractor** - we've used `text` again, as the data we'd like extracted from the element is its text contents.

This request returned:

```json
{
    "status": "success",
    "query_time": "2023-06-06T14:06:44.986Z",
    "status_code": 200,
    "html_content": "...",
    "headers": {
        ...
    },
    "parsing": {
        "team_name": "BostonCeltics",
        "team_standings": [
            {
                "GB": "-",
                "L": "25",
                "PCT": ".695",
                "STRK": "W3",
                "Team": "Boston",
                "W": "57"
            },
            {
                "GB": "3",
                "L": "28",
                "PCT": ".659",
                "STRK": "W2",
                "Team": "Philadelphia",
                "W": "54"
            },
            {
                "GB": "10",
                "L": "35",
                "PCT": ".573",
                "STRK": "L2",
                "Team": "NY Knicks",
                "W": "47"
            },
            {
                "GB": "12",
                "L": "37",
                "PCT": ".549",
                "STRK": "L1",
                "Team": "Brooklyn",
                "W": "45"
            },
            {
                "GB": "16",
                "L": "41",
                "PCT": ".500",
                "STRK": "W1",
                "Team": "Toronto",
                "W": "41"
            }
        ]
    },
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics"
}
```

In this example, we defined the parsing template inline, or within the request body. However, we recommend uploading your parsing templates and simply referring to them in each call for a more smooth experience at scale.

See the [Implementing Parsing Templates](#implementing-parsing-templates) section further down for more information.

</details>

<details>

<summary>Example 3 - extracting repeating elements</summary>

Our example page contains many articles that are relevant to the Boston Celtics, appearing in the center of the page. We might be interested in parsing out these articles. Doing each one individually would take a lot of time, and would be prone to breaks as new articles are published.

This is where lists come in. Using `list` instead of `item` as our extractor allows us to get not just the first, but all the matched elements that appear for a selector. When we examine the HTML of the page around an article, we see the following structure:

```html
<section>
  <article class="contentItem cf relative overflow-hidden mb3 br-5 overflow-hidden bg-clr-white">
    <header class="contentItem__header" style="border-top-color: rgb(0, 101, 50);">
      ...
    </header>
    <div>
      <div class="ResponsiveWrapper">
        <div class="contentItem__content--layoutLg contentItem__content overflow-hidden contentItem__content--standard hasImage hasVideo contentItem__content--fullWidth flex contentItem__content--media" aria-label="Why JWill and Max want patience with Tatum and Brown" style="height: auto;">
          <div class="contentItem__contentWrapper relative flex flex-column contentWrapper">
            <div class="ColorBorder absolute top-0 left-0 right-0" style="background-color: rgb(165, 166, 167);"></div>
            <ul class="contentItem__meta"></ul>
            <h2 class="contentItem__title">
              <span class="Truncate Truncate--collapsed">
                <span>Why JWill and Max want patience with Tatum and Brown</span>
              </span>
            </h2>
          ...
  </article>
</section>
```

We can see that all of the articles are within a `section` container, and each article is inside an `article` container. Furthermore, the title of the article has a consistent class `contentItem__title` .&#x20;

![](https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/ZcSxvfv95X6kkP7XTf0O/Articles.png)

This structure is consistent across all articles, so we can use a list type to ask for all of the titles of all of the articles:

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics",
    "parse": true,
    "format": "json",
    "render": true,
    "country": "US",
    "parser": {
        "team_name": {
            "type": "item",
            "selectors": [".ClubhouseHeader__Name"],
            "extractor": "text"
        },
        "team_standings": {
            "type": "table",
            "selectors": [".TeamStandings table"],
            "extractor": "text"
        },
        "articles": {
            "type": "list",
            "selectors": ["section > article .contentItem__title"],
            "extractor": "text"
        }
    }
}'
```

The `list` type will now provide us with a list of all the matched elements, and the `text` extractor cleans the HTML out and parses just the contents, providing us with the following result:

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "query_time": "2023-06-06T14:06:44.986Z",
    "status_code": 200,
    "html_content": "...",
    "headers": {
        ...
    },
    "parsing": {
        "team_name": "BostonCeltics",
        "team_standings": [
            {
                "GB": "-",
                "L": "25",
                "PCT": ".695",
                "STRK": "W3",
                "Team": "Boston",
                "W": "57"
            },
            ...
        ],
        "articles": [
            "Why JWill and Max want patience with Tatum and Brown",
            "When did the Heat start to win Game 7 over the Celtics? As soon as Game 6 ended",
            "Star deals, coaching plans and an uncertain summer: What lies ahead for Boston",
            ...
        ]
    },
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics"
}
```

{% endcode %}

Now that we have the article titles, we can parse the article links in a very similar fashion:

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics",
    "parse": true,
    "format": "json",
    "render": true,
    "country": "US",
    "parser": {
        "team_name": {
            "type": "item",
            "selectors": [".ClubhouseHeader__Name"],
            "extractor": "text"
        },
        "team_standings": {
            "type": "table",
            "selectors": [".TeamStandings table"],
            "extractor": "text"
        },
        "articles": {
            "type": "list",
            "selectors": ["section > article .contentItem__title"],
            "extractor": "text"
        },
        "articles_links": {
            "type": "list",
            "selectors": ["section > article a"],
            "extractor": "[href]"
        }
    }
}'
```

We've made some modifications in order to target the links:

* [x] **type** - `list` is still the appropriate type, as we would like a list of article links.
* [x] **selectors** - the `selectors` has been modified to request the `a` , or link, element instead of the title.&#x20;
* [x] **extractor** - instead of using the usual text extractor, we now use the name of the HTML attribute surrounded by square brackets `[href]` to define that we would like the value of the href attribute.

The result of this request returns:

```json
{
    "status": "success",
    "query_time": "2023-06-06T14:06:44.986Z",
    "status_code": 200,
    "html_content": "...",
    "headers": {
        ...
    },
    "parsing": {
        "team_name": "BostonCeltics",
        "team_standings": [
            {
                "GB": "-",
                "L": "25",
                "PCT": ".695",
                "STRK": "W3",
                "Team": "Boston",
                "W": "57"
            },
            ...
        ],
        "articles": [
            "Why JWill and Max want patience with Tatum and Brown",
            "When did the Heat start to win Game 7 over the Celtics? As soon as Game 6 ended",
            "Star deals, coaching plans and an uncertain summer: What lies ahead for Boston",
            ...
        ],
        "articles_links": [
            "/video/clip/_/id/37759456",
            "/nba/story/_/id/37757803/when-did-heat-start-win-game-7-celtics-soon-game-6-ended",
            "/nba/story/_/id/37603481/the-celtics-biggest-issues-came-roaring-back-game-7-now",
            ...
        ],
    },
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics"
}
```

Although parsing out the article titles and links in this way works, it can be a bit cumbersome as more properties are added. What if we wanted the author, publish date, image URL, and more?

This is where objects, and object-lists, comes in. We can use objects to define an article object, with multiple properties defined in the schema of the object. See [Advanced example - using object-list](#advanced-example-using-object-list) to learn more.

In this example, we defined the parsing template inline, or within the request body. However, we recommend uploading your parsing templates and simply referring to them in each call for a more smooth experience at scale.

See the [Implementing Parsing Templates](#implementing-parsing-templates) section further down for more information.

</details>

<details>

<summary>Advanced example - Using object-list</summary>

In the previous example, we used the `list` type to get a list of article titles and article links, but we can achieve the same result more effectively and robustly by using the `object-list` type instead.

Before we get into `object-list`, let's understand what an object is.

An object consists of a single selector that identifies the target element on the webpage and a series of fields. Each field has it's own type, extractor, and selector. This is useful when wanting to extract complex elements from a page that have several relevant attributes. Some examples of use cases for objects include:

* [x] An article object with fields such as title, URL, publish date, author, length, etc.
* [x] A product object with fields such as name, manufacturer, model, price, rating, etc.
* [x] A social media post with fields such as user, media, likes, views, etc.

For a practical example, let's look at how we could use objects to collect the articles from our ESPN Celtics page. In the below example, we create an object-list that collects the title, URL, time elapsed since publish, and author for each article:

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics",
    "format": "json",
    "render": true,
    "country": "GR",
    "parse": true,
    "parser": {
        "articles": {
            "type": "object-list",
            "selectors": [
                "section > article"
            ],
            "fields": {
                "title": {
                    "type": "item",
                    "selectors": [
                        ".contentItem__title"
                    ],
                    "extractor": "text"
                },
                "link": {
                    "type": "item",
                    "selectors": [
                        "a"
                    ],
                    "extractor": "[href]"
                },
                "time_elapsed": {
                    "type": "item",
                    "selectors": [
                        ".time-elapsed"
                    ],
                    "extractor": "text"
                },
                "author": {
                    "type": "item",
                    "selectors": [".author"],
                    "extractor": "text"
                }
            }
        }
    }
}
```

First, we create a parsing template names `articles`.&#x20;

* [x] The `type` is set to `object-list`, which allows us to define our object and to have an object created for all elements that match the selector, and not just the first.
* [x] The `selectors` is set to the main, repeating parent element. Selectors defined later down in the fields are relative to this main parent selector.

Next, we start defining the fields of the object.

* [x] The **title** field uses the `item` type to get a single element, uses the `.contentItem__title`  selector to target the class that contains the title of the article, and uses the `text` extractor to get only the text without any HTML.
* [x] The **link** field uses a different selector to target the link of each article, and uses the html attribute `[href]` to get the value for the href link attribute.
* [x] the **time\_elapsed** and **author** fields work the same as the **title** feed, but use different selectors to target different elements of the article.

The result of the above request is:

```json
{
    "status": "success",
    "query_time": "2023-06-06T14:05:39.129Z",
    "status_code": 200,
    "html_content": "...",
    "headers": {
        ...
    },
    "parsing": {
        "status": "success",
        "articles": [
            {
                "author": "",
                "link": "/video/clip/_/id/37759456",
                "time_elapsed": "1h",
                "title": "Why JWill and Max want patience with Tatum and Brown"
            },
            {
                "author": "Brian Windhorst",
                "link": "nba/story/_/id/37757803/when-did-heat-start-win-game-7-celtics-soon-game-6-ended",
                "time_elapsed": "7h",
                "title": "When did the Heat start to win Game 7 over the Celtics? As soon as Game 6 ended"
            },
            {
                "author": "Tim Bontemps",
                "link": "/nba/story/_/id/37603481/the-celtics-biggest-issues-came-roaring-back-game-7-now",
                "time_elapsed": "8h",
                "title": "Star deals, coaching plans and an uncertain summer: What lies ahead for Boston"
            },
            ...
        ],
        "entity_type": "Dynamic"
    },
    "url": "https://www.espn.com/nba/team/_/name/bos/boston-celtics"
}
```

In this example, we defined the parsing template inline, or within the request body. However, we recommend uploading your parsing templates and simply referring to them in each call for a more smooth experience at scale.

See the [Implementing Parsing Templates](#implementing-parsing-templates) section further down for more information.

</details>

### Parsing template syntax

Introducing new param named `parser`, along side `parser` param which is set to `true`\
At its core, a parsing template is built of three properties:

* **type (required)** - defines the format of the returned data. For example, setting `type` to `json` will instructed the parser to structure the extract data into JSON, and then return the JSON object.
* **selectors (required)** - The CSS selector or selectors of the elements that should be extracted by the parser. Listing more than one selector creates fallback selectors, meaning that if the first selector isn’t found, the parser will look for the second, then the third, etc.
* **extractor** - Once an element has been identified by its selector, the extractor defines what part of the element should be returned.

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/web/' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com/",
    "country": "US",
    "parse": true,
    "parser": {...}
}'
```

{% endtab %}
{% endtabs %}

### Types

Types define the return format of extracted data. Types are a required field, and can have the following values:

| Value          | Description                                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| item (Default) | Returns the contents of the first element matched by the defined CSS selector.                                                                                                                                                  |
| list           | Returns a list of data points from all the matching elements of the CSS selector in a list.                                                                                                                                     |
| json           | Returns the contents of the first element (like item), but formatted into JSON.                                                                                                                                                 |
| table          | Converts an HTML table into JSON, using the headers of the table as keys. Use this type when targeting \<table>\</table> elements.                                                                                              |
| object         | Define a custom object that is populated and returned. The structure/properties of the object are defined using fields (see below). The object will be populated using the first element that matches the defined CSS selector. |
| object-list    | Returns a list of objects, populated by all the elements that match the defined CSS selector. The structure/properties of objects are defined using fields (see below).                                                         |

**Example - list**

```json
    ...
    "parser": {
        "template_name": {
            "type": "list",
            "selectors": ["h1,h2,h3"],
            "extractor": "text"
        }
    }
```

**Example - json**

```json
    ...
    "parser": {
        "template_name": {
            "type": "json",
            "selectors": ["script[type='application/json']"]
        }
    }
```

**Example - table**

```json
    ...
    "parser": {
        "template_name": {
            "type": "table",
            "selectors": [".someTable"]
        }
    }
```

### Extractors

When an element matches the defined CSS selectors, the extractor defines which part of the matched element is extracted and returned. Extractors can have three possible values:

| Name              | Description                                                                          |
| ----------------- | ------------------------------------------------------------------------------------ |
| text (default)    | Extracts the text of the selected element.                                           |
| html              | Extracts the full inner HTML of the selected element.                                |
| \[attribute-name] | Extracts the value of an HTML attribute of the selected element (eg: id, href, etc.) |

Extractors can only be used when `type` is set to one of:

* item
* list
* json

Tables do not use extractors because the structure of the table defines the way the table is parsed. An object, and by extension object-lists, uses “fields” to define the data to be extracted.

**Examples**

Let's assume the page being parsed is made up of the following HTML:

```html
<html>
    <head>
        <title>parsing demo</title>
    </head>
    <body>
        <div class="article">
            <p>
                Lorem ipsum dolor sit amet <span>consectetur adipiscing elit.</span> Duis sapien eros, euismod vel magna sodales,
                porttitor tristique mi. Phasellus vel lobortis mi, 
                <a href=\"https://www.somedomain.com\">nec pharetra risus.</a>
                Sed quis augue in ligula blandit ullamcorper non et elit. 
            </p>
        </div>
    </body>
</html>
```

In the below parsing template example, the first template “link” searches for the first link in the page (an element matching the “a” selector), and then uses the \[attribute-name] extractor to extract the URL to which the link is pointing.

The second template looks for a div with the class “article” and extracts the full html contents.

```json
 ...
 "parser": {
  "link": {
   "selectors": ["a"],
   "extractor": "[href]"
  },
  "article": {
   "selectors": ["div.article"],
   "extractor": "html"
  }
 }
```

The response for this parsing template processing our example HTML would produce the following output:

{% code overflow="wrap" %}

```json
{
 ...
 "link": "https://www.somedomain.com",
 "article": "<p>Lorem ipsum dolor sit amet, <span>consectetur adipiscing elit.</span> Duis sapien eros, euismod vel magna sodales, porttitor tristique mi. Phasellus vel lobortis mi, <a href=\"https://www.somedomain.com\">nec pharetra risus.</a> Sed quis augue in ligula blandit ullamcorper non et elit. </p>"
}
```

{% endcode %}

### Objects

Objects allow users to define a customized return structure that can capture data in a way that is more accessible and better represents the data they are trying to collect. For example, when collecting product data, a “product” object can be created, with fields for price, inventory, color, shipping method, and other contextually relevant factors.

Because objects are fully user-defined, different objects can be created for different sources, purposes, or any other use case!

An object has a `type`, which is always set to `object`, and `selectors`, which define the scope or parent element from which fields (which each have their own selectors) select from.

Fields make up the contents of the object, and each one has a `title` and a `selector`. The `title` defines the name of the field, and the `selector` defines the CSS selector that should be used to populate its value, where that element is a child of the object selector. For example:

```json
    ...
    "product": {
        "type": "object",
        "selectors": [ ".product-card" ],
        "fields": {
            "name": {
                "selectors": [ ".name" ]
            },
            "price": {
                "selectors": [ ".price" ]
            },
            "average_rating": {
                "selectors": [ ".rating" ]
            }
        }
    }
```

In the above example, an object named “product” would be returned. It would have three children, “name”, “price”, and “average\_rating”. The value for name would be extracted from the first element found with the class “name”, where that element is itself a child of the first element found with the class “product-card”.

The above object parsing template would parse this HTML:

```html
<html>
    <head>
        <title>parsing demo</title>
    </head>
    <body>
        <div class="product-card">
            <div class="name">blue jeans</div>
            <div class="price">$50</div>
            <div class="rating">4/5</div>
        </div>
    </body>
</html>
```

into this output:

```json
{
 ...
 "product":{
  "name": "blue jeans",
  "price": "$50",
  "average_rating": "4/5"
 }
}
```

### Object lists

An object list combines objects with lists, allowing users to create custom structures that are populated by multiple matching elements. This can be useful, for example, when collecting product data from a page that has multiple products, or to quickly extract SERP listings.

An object-list uses syntax that is very similar to a regular object, except that `type` is set to `object-list` instead of `object`. For example:

```json
{
    "links": {
        "type": "object-list",
        "selectors": ["a"],
        "fields": {
            "url": {
                "selectors": ["*"],
                "extractor": "[href]"
            },
            "title": {
                "selectors": ["*"],
                "extractor": "text"
            }
        }
        
    }
}
```

The above example would parse out all of the links (all of the elements that have an "a" tag) in a webpage. For the following HTML webpage:

```html
<html>
    <head>
        <title>parsing demo</title>
    </head>
    <body>
        <a href="https://www.somelink.com">Some link</a>
        <a href="https://www.anotherlink.com">Another lin</a>
    </body>
</html>
```

The output of our object-list template would be:

```json
{
 ...
 "links":[
  {
   "url": "https://www.somelink.com",
   "title": "Some link"
  },
  {
   "url": "https://www.anotherlink.com",
   "title": "Another link"
  },
  ...
 ]
}
```

### Implementing parsing templates

Parsing templates can be implemented in one of two ways:

* **Inline** - The parsing template’s rules are defined within the request body. All of the previous examples shown above have been inline implementations.
* **Upload** - Custom parsers can be written separately and uploaded to the WebAPI, and then implemented by passing a `parser` value instead of being written inline.

{% hint style="success" %}
**We highly recommend uploading your parsing template to increase stability and performance. Parsing templates should only be used inline for testing and development purposes.**
{% endhint %}

### Managing parsing templates

Parsing templates can be managed through several API endpoints that allow uploading, viewing, updating, and deleting parsing templates.

## Upload a new parsing template

<mark style="color:green;">`POST`</mark> `https://api.webit.live/api/v1/parsers`

{\
&#x20;   "schema": { "type": "item", "selectors": \[".css-selector"], "extractor": "text" },\
&#x20;   "name": "parsing template name"\
}

#### Request Body

| Name                                     | Type   | Description                                                                                             |
| ---------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| schema<mark style="color:red;">\*</mark> | String | { /\* A valid parser template \*/}                                                                      |
| name<mark style="color:red;">\*</mark>   | String | A name for the parsing template that will later be used to update, delete, or implement it in requests. |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "id": "<parser id>",
    "message": "parser created",
    "success": true
}
```

{% endtab %}
{% endtabs %}

## View a parsing template

<mark style="color:blue;">`GET`</mark> `https://api.webit.live/api/v1/parsers/{parsing-template-name}`

#### Path Parameters

| Name                                                    | Type   | Description                     |
| ------------------------------------------------------- | ------ | ------------------------------- |
| parsing-template-name<mark style="color:red;">\*</mark> | String | The name of the parser to view. |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "id": "<parser id>",
    "name": "My Parser",
    "account": "my_account",
    "schema": { /* The parser's schema */},
    "created_at": "2022-11-16T15:18:24.525Z",
    "created_by": "username@my_account.com",
    "modified_at": "2022-11-16T15:18:24.525Z",
    "modified_by": "username@my_account.com",
}
```

{% endtab %}

{% tab title="404: Not Found " %}

```javascript
{
    "success": false,
    "parser": "<parser name>",
    "message": "parser <parser name> not found"
}
```

{% endtab %}
{% endtabs %}

## List all uploaded parsing templates

<mark style="color:blue;">`GET`</mark> `https://api.webit.live/api/v1/parsers`

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "parsers": [
        {
            "id": "<parser id>",
            "name": "My Parser",
            "account": "my_account",
            "schema": { /* The parser's schema */ },
            "created_at": "2022-11-16T15:18:24.525Z",
     "created_by": "username@my_account.com",
     "modified_at": "2022-11-16T15:18:24.525Z",
     "modified_by": "username@my_account.com",
        },
        {
            "id": "<parser id>",
            "name": "My Second Parser",
            "account": "my_account",
            "schema": { /* The parser's schema */ },
            "created_at": "2022-11-16T15:18:24.525Z",
     "created_by": "username@my_account.com",
     "modified_at": "2022-11-16T18:39:54.015Z",
     "modified_by": "username2@my_account.com",
        }
    ]
}
```

{% endtab %}
{% endtabs %}

## Delete a parsing template

<mark style="color:red;">`DELETE`</mark> `https://api.webit.live/api/v1/parsers/{parsing-template-name}`

#### Path Parameters

| Name                                                    | Type   | Description                     |
| ------------------------------------------------------- | ------ | ------------------------------- |
| parsing-template-name<mark style="color:red;">\*</mark> | String | The parsing template to delete. |

## Update a parsing template

<mark style="color:orange;">`PUT`</mark> `https://api.webit.live/api/v1/parsers`

#### Request Body

| Name                                     | Type   | Description                      |
| ---------------------------------------- | ------ | -------------------------------- |
| schema<mark style="color:red;">\*</mark> | String | { /\* A valid parser schema \*/} |
| name<mark style="color:red;">\*</mark>   | String | The name of the parser to update |

{% tabs %}
{% tab title="200: OK " %}

```javascript
{
    "parser": "<parser name>",
    "message": "parser updated",
    "success": true
}
```

{% endtab %}
{% endtabs %}
