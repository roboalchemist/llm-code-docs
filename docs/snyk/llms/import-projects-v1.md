# Source: https://docs.snyk.io/snyk-api/reference/import-projects-v1.md

# Import Projects (v1)

{% hint style="info" %}
This document uses the v1 API, which will eventually be deprecated, as further Snyk developments are now focused on the REST API. For more details, see the [v1 API](https://docs.snyk.io/snyk-api/v1-api).
{% endhint %}

You can use this API to import projects into Snyk. Projects imported can be Git repositories, Docker images, containers, configuration files, and much more. See the [Projects and Targets documentation](https://docs.snyk.io/snyk-platform-administration/snyk-projects#target) for more information. A typical import would start with requesting a target to be processed and then polling the Import Job API for more details on completion of an import and the resulting Snyk Projects.

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/integrations/{integrationId}/import" method="post" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}

{% openapi src="<https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media>" path="/org/{orgId}/integrations/{integrationId}/import/{jobId}" method="get" %}
[v1-api-spec.yaml](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1ca788fc7f0344e1e28fe2e1af146295141d1653%2Fv1-api-spec.yaml?alt=media)
{% endopenapi %}
