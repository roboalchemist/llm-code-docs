# Source: https://docs.enate.net/enate-help/integrations/enate-integrations/apis/api-changes.md

# API Changes

This section gives a list of changes to Enate's APIs from version 2024.1 and above.

## What is a breaking change?

With each release of Enate (both major and minor), the changes to Enate's APIs may also include breaking changes. Examples of breaking changes are:

* Changes to the URL or fundamental request/response associated with a resource
* Removal, rename, or change to the type of a declared property
* Removal or rename of APIs or API parameters
* Addition of a required request header
* Addition of a required API parameter

Examples of changes which are NOT considered breaking changes and are outside the scope of this document are:

* Addition of properties that are nullable or have a default value
* Addition of an optional API parameter
* Addition of a member to an enumeration
* Removal, rename, or change to the type of an open extension
* Removal, rename, or change to the type of an annotation
* Introduction of paging to existing collections
* Changes to error codes
* Changes to the order of properties
* Changes to the length or format of opaque strings, such as resource IDs

## API Changes Documents

See the following documents for details of all the API changes, including breaking API changes.

#### November 2025 Feature Wave

#### Version 1 Configurational API

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2F5aORsLKIF9JNmA77nvss%2FVersion%201%20Configuration%20API%20Changes.pdf?alt=media&token=cbcc9c5c-c849-4d02-af30-935eb406552e>" %}

#### Version 1 Operational API

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FBfqIEXhliMm2YsVSJU1n%2FVersion%201%20Operational%20API%20Changes.pdf?alt=media&token=463ad4f9-b1f0-4521-986d-6c3cf7c5c4c7>" %}

#### 2024.1 Legacy API

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FdgxFhacI0vLXdNceglAR%2F2024.1.1.43%20-%20Version%201%20WebApi%20API%20Changes.pdf?alt=media&token=b74e9516-a258-43ae-99d9-e74145aa66e1>" %}

#### v2024.1

{% file src="<https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FZdal8s9VJdghpHgLHCzC%2F2023.5.0%20-%202024.1.0%20API%20Changes.pdf?alt=media&token=6986e79d-5961-4e4b-a697-5ceb1027815b>" %}

## How to use the API Changes document

Recommendations for how best to use the breaking changes document information to highlight where you may need to make changes to your code which involves Enate APIs.&#x20;

Recommendation for best use of API breaking changes documentation is as follows:&#x20;

* Read through the breaking changes information for APIs.
* Upon finding reference to an API which you currently use and which has changed, go to your Swagger environment for the quickest way to view the overall impact and new API content definition. Your Swagger environment should always be your go-to place for the definitive explanation of the current API structure.\
  See the [Swagger explanation section](https://docs.enate.net/enate-help/integrations/enate-integrations/apis#swagger-enates-interactive-api-documentation) for more info.
