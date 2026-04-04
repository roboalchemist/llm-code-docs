# Source: https://docs.snyk.io/snyk-api/oauth2-api.md

# OAuth2 API

Snyk provides an OAuth2 API, primarily for use with [Snyk Apps](https://docs.snyk.io/snyk-api/using-specific-snyk-apis/snyk-apps-apis). It complies with RFC 6749.

Most endpoints are served from the Snyk API subdomain (for example, <https://api.snyk.io>), with the one exception being `/oauth2/authorize` which is served on the main app subdomain (for example, <https://app.snyk.io>).

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c5deed075973ba16e5ec51bb7e894d02107164ff%2Foauth-app-spec.yaml?alt=media>" path="/oauth2/authorize" method="get" %}
[oauth-app-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c5deed075973ba16e5ec51bb7e894d02107164ff%2Foauth-app-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-688a641e25b6bd8b33a94ac151f6adba5ecd370f%2Foauth-api-spec.yaml?alt=media&token=ca861067-361e-4cb6-9ced-ac5551c0bb14>" path="/token" method="post" %}
[oauth-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-688a641e25b6bd8b33a94ac151f6adba5ecd370f%2Foauth-api-spec.yaml?alt=media\&token=ca861067-361e-4cb6-9ced-ac5551c0bb14)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-688a641e25b6bd8b33a94ac151f6adba5ecd370f%2Foauth-api-spec.yaml?alt=media&token=ca861067-361e-4cb6-9ced-ac5551c0bb14>" path="/revoke" method="post" %}
[oauth-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-688a641e25b6bd8b33a94ac151f6adba5ecd370f%2Foauth-api-spec.yaml?alt=media\&token=ca861067-361e-4cb6-9ced-ac5551c0bb14)
{% endopenapi %}
