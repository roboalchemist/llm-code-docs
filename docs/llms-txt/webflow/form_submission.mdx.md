# Source: https://developers.webflow.com/data/v1.0.0/reference/form_submission.mdx

***

title: Form Submission
slug: data/reference/form\_submission
description: The form data submitted
hidden: false
-------------

## Trigger Type

`form_submission`

## Properties

| Field  | Type   | Description                                         |
| :----- | :----- | :-------------------------------------------------- |
| `name` | string | The name of the form                                |
| `site` | string | The id of the site that the form was submitted from |
| `data` | object | The data submitted in the form                      |
| `d`    | string | The timestamp the form was submitted                |
| `_id`  | string | The id of the form submission                       |

## Example

```json
{
    "name": "Sample Form",
    "site": "62749158efef318abc8d5a0f",
    "data": {
        "name": "Some One",
        "email": "some.one@home.com"
    },
    "d": "2022-09-14T12:35:16.117Z",
    "_id": "6321ca84df3949bfc6752327"
}
```
