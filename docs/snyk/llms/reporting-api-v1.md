# Source: https://docs.snyk.io/snyk-api/reference/reporting-api-v1.md

# Reporting API (v1)

{% hint style="info" %}
This document uses the v1 API, which will eventually be deprecated, as further Snyk developments are now focused on the REST API. For more details, see the [v1 API](https://docs.snyk.io/snyk-api/v1-api).
{% endhint %}

{% hint style="warning" %}
The endpoints in this category support only Snyk legacy reporting, not the latest release. They are not available in regions such as single-tenant or multi-tenant US02, EU, and AU; instead use the [Issues REST API](https://docs.snyk.io/snyk-api/reference/issues).
{% endhint %}

Using the Reporting API, you can find answers to questions like how many issues your Organization has, or how many tests have been conducted in a given time period.

The rate limit is up to **70 requests per minute, per user**. All requests above the limit will get a response with the status code `429 - Too many requests` until requests stop for the duration of the rate-limiting interval (one minute).

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/issues" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/issues/latest" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/counts/tests" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/counts/projects" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/counts/projects/latest" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/counts/issues" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/reporting/counts/issues/latest" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}
