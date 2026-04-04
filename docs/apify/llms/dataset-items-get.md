# Source: https://docs.apify.com/api/v2/dataset-items-get.md

# Get dataset items


```
GET 
https://api.apify.com/v2/datasets/:datasetId/items
```


Returns data stored in the dataset in a desired format.

### Response format

The format of the response depends on `format` query parameter.

The `format` parameter can have one of the following values: `json`, `jsonl`, `xml`, `html`, `csv`, `xlsx` and `rss`.

The following table describes how each format is treated.

| Format  | Items                                                                                                                                       |   |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- | - |
| `json`  | The response is a JSON, JSONL or XML array of raw item objects.                                                                             |   |
| `jsonl` |                                                                                                                                             |   |
| `xml`   |                                                                                                                                             |   |
| `html`  | The response is a HTML, CSV or XLSX table, where columns correspond to the properties of the item and rows correspond to each dataset item. |   |
| `csv`   |                                                                                                                                             |   |
| `xlsx`  |                                                                                                                                             |   |
| `rss`   | The response is a RSS file. Each item is displayed as child elements of one `<item>`.                                                       |   |

Note that CSV, XLSX and HTML tables are limited to 2000 columns and the column names cannot be longer than 200 characters. JSON, XML and RSS formats do not have such restrictions.

### Hidden fields

The top-level fields starting with the `#` character are considered hidden. These are useful to store debugging information and can be omitted from the output by providing the `skipHidden=1` or `clean=1` query parameters. For example, if you store the following object to the dataset:


```
{
    productName: "iPhone Xs",
    description: "Welcome to the big screens."
    #debug: {
        url: "https://www.apple.com/lae/iphone-xs/",
        crawledAt: "2019-01-21T16:06:03.683Z"
    }
}
```


The `#debug` field will be considered as hidden and can be omitted from the results. This is useful to provide nice cleaned data to end users, while keeping debugging info available if needed. The Dataset object returned by the API contains the number of such clean items in the`dataset.cleanItemCount` property.

### XML format extension

When exporting results to XML or RSS formats, the names of object properties become XML tags and the corresponding values become tag's children. For example, the following JavaScript object:


```
{
    name: "Paul Newman",
    address: [
        { type: "home", street: "21st", city: "Chicago" },
        { type: "office", street: null, city: null }
    ]
}
```


will be transformed to the following XML snippet:


```
<name>Paul Newman</name>
<address>
  <type>home</type>
  <street>21st</street>
  <city>Chicago</city>
</address>
<address>
  <type>office</type>
  <street/>
  <city/>
</address>
```


If the JavaScript object contains a property named `@` then its sub-properties are exported as attributes of the parent XML element. If the parent XML element does not have any child elements then its value is taken from a JavaScript object property named `#`.

For example, the following JavaScript object:


```
{
  "address": [{
    "@": {
      "type": "home"
    },
    "street": "21st",
    "city": "Chicago"
  },
  {
    "@": {
      "type": "office"
    },
    "#": 'unknown'
  }]
}
```


will be transformed to the following XML snippet:


```
<address type="home">
  <street>21st</street>
  <city>Chicago</city>
</address>
<address type="office">unknown</address>
```


This feature is also useful to customize your RSS feeds generated for various websites.

By default the whole result is wrapped in a `<items>` element and each page object is wrapped in a `<item>` element. You can change this using `xmlRoot` and `xmlRow` url parameters.

### Pagination

The generated response supports . The pagination is always performed with the granularity of a single item, regardless whether `unwind` parameter was provided. By default, the **Items** in the response are sorted by the time they were stored to the database, therefore you can use pagination to incrementally fetch the items as they are being added. No limit exists to how many items can be returned in one response.

If you specify `desc=1` query parameter, the results are returned in the reverse order than they were stored (i.e. from newest to oldest items). Note that only the order of **Items** is reversed, but not the order of the `unwind` array elements.

## Request

## Responses

* 200
* 400

**Response Headers**

* **X-Apify-Pagination-Offset**

  **X-Apify-Pagination-Limit**

  **X-Apify-Pagination-Count**

  **X-Apify-Pagination-Total**

Bad request - invalid input parameters or request body.
