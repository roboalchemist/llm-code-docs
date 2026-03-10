# Source: https://developers.webflow.com/data/v1.0.0/reference/site_publish.mdx

***

title: Site Publish
slug: data/reference/site\_publish
description: The information about the site(s) published
hidden: false
-------------

## Trigger Type

`site_publish `

## Properties

| Field               | Type      | Description                                        |
| :------------------ | :-------- | :------------------------------------------------- |
| `site`              | string    | The site id that was published                     |
| `publishTime `      | string    | The timestamp of the publish event                 |
| `domains `          | \[string] | The domains that were published                    |
| `publishedBy `      | object    | The name and id of the user who published the site |
| `publishedBy.name`  | string    | The full name of the person who published the site |
| `publishedBy.email` | string    | The email of the person who published the site     |

## Example

```json
{
    "site": "62749158efef318abc8d5a0f",
    "publishTime": 1653619272801,
    "domains": [
        "my-website.webflow.io"
    ],
    "publishedBy": {
        "name": "Some One",
        "id": "123460a7b6c16def4527122d"
    }
}
```
