# Source: https://docs.snyk.io/snyk-api/reference/webhooks-v1.md

# Webhooks (v1)

{% hint style="info" %}
This document uses the v1 API, which will eventually be deprecated, as further Snyk developments are now focused on the REST API. For more details, see the [v1 API](https://docs.snyk.io/snyk-api/v1-api).
{% endhint %}

{% hint style="warning" %}
The Webhooks API is in beta. While the API is in beta, Snyk may change the API and the structure of webhook payloads at any time, without notice. During this beta, Webhooks are available only in the Snyk US-01, US-02, EU-01, and AU-01 regions.
{% endhint %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/webhooks" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/webhooks" method="get" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/webhooks/{webhookId}" method="get" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/webhooks/{webhookId}" method="delete" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/webhooks/{webhookId}/ping" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}
