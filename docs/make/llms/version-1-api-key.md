# Source: https://developers.make.com/custom-apps-development-training/version-1-api-key.md

# Version 1 (API key)

## Authentication

The App Academy API version 1 uses the API Key authorization. You need the `x-api-key` which you can obtain in this [form](https://airtable.com/apptuF9ohhm4eho3M/shrXXIuflEJFXaUPP).

## Pagination

Since the App Academy API was built for educational purposes, the following types of pagination were used:

* **offset** based
* **page** based
* **has more items** based

## Endpoints

### About

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/about" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### Movies

Each user is granted access to 6 default records that cannot be updated or deleted.

Each user can create up to 14 records, resulting in a total of 20 retrievable records.

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/movies" method="post" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/movies" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/movies/{id}" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/movies/{id}" method="put" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/movies/{id}" method="patch" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/movies/{id}" method="delete" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### People

The query (parameter `q` ) has to be written in this format:

* all the conditions can be grouped by operator `AND`
* the value in each condition has to be enclosed in quotation marks
* supported conditions:
  * `contains`
  * `startsWith`
  * `endsWith`
  * `equal`
* multiple conditions can be used multiple times within one query

example:

```
contains= "Rob" AND startsWith = "Rob" AND endsWith = "Jr."
```

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/people" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### Organizations

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/organizations" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### Genres

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/genres" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### Awards

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/awards/{movieId}" method="get" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### Webhooks

Each user can create 1 webhook.

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/webhooks" method="post" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f>" path="/webhooks/{id}" method="delete" %}
[make-custom\_app\_academy\_api-v1.json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FjdhKa2tPyJM2t28x3ysa%2Fmake-custom_app_academy_api-v1.json?alt=media\&token=d2f10311-cb4e-4115-bc3e-7a01edc5765f)
{% endopenapi %}

### Files

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20(1).json?alt=media&token=8198775f-c7a6-47a8-bf85-aef4aceda10f>" path="/files" method="get" %}
[TKLOBOUCKOVA-custom-academy-1.0.0-resolved (1).json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20\(1\).json?alt=media\&token=8198775f-c7a6-47a8-bf85-aef4aceda10f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20(1).json?alt=media&token=8198775f-c7a6-47a8-bf85-aef4aceda10f>" path="/files/{id}/export" method="get" %}
[TKLOBOUCKOVA-custom-academy-1.0.0-resolved (1).json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20\(1\).json?alt=media\&token=8198775f-c7a6-47a8-bf85-aef4aceda10f)
{% endopenapi %}

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20(1).json?alt=media&token=8198775f-c7a6-47a8-bf85-aef4aceda10f>" path="/files/import" method="post" %}
[TKLOBOUCKOVA-custom-academy-1.0.0-resolved (1).json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20\(1\).json?alt=media\&token=8198775f-c7a6-47a8-bf85-aef4aceda10f)
{% endopenapi %}

{% hint style="info" %}
Please note that the **Import** endpoint does not upload or store any data. Therefore, the file

you provide will not be returned or stored in the **Files** endpoint.
{% endhint %}

### Custom Fields (movie)

{% openapi src="<https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20(1).json?alt=media&token=8198775f-c7a6-47a8-bf85-aef4aceda10f>" path="/custom-fields" method="get" %}
[TKLOBOUCKOVA-custom-academy-1.0.0-resolved (1).json](https://3114796191-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FgNTg64InL2Ea6QArLuAq%2Fuploads%2FLuPLiJsZjtSTYKS1F6Sg%2FTKLOBOUCKOVA-custom-academy-1.0.0-resolved%20\(1\).json?alt=media\&token=8198775f-c7a6-47a8-bf85-aef4aceda10f)
{% endopenapi %}

{% hint style="info" %}
Please note that values in custom fields are not stored in movie records. Therefore, the

values you provide will not be returned or stored in the **Movies** endpoints.
{% endhint %}
