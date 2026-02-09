# Source: https://docs.pinecone.io/reference/api/versioning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# API versioning

Pinecone's APIs are versioned to ensure that your applications continue to work as expected as the platform evolves. Versions are named by release date in the format `YYYY-MM`, for example, `2025-10`.

## Release schedule

On a quarterly basis, Pinecone releases a new **stable** API version as well as a **release candidate** of the next stable version.

* **Stable:** Each stable version remains unchanged and supported for a minimum of 12 months. Since stable versions are released every 3 months, this means you have at least 9 months to test and migrate your app to the newest stable version before support for the previous version is removed.

* **Release candidate:** The release candidate gives you insight into the upcoming changes in the next stable version. It is available for approximately 3 months before the release of the stable version and can include new features, improvements, and [breaking changes](#breaking-changes).

Below is an example of Pinecone's release schedule:

<img className="block max-w-full dark:hidden" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=be4366853edee83e003c3863e31fa1ce" data-og-width="2120" width="2120" data-og-height="960" height="960" data-path="images/api-versioning.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=66d593bf5bc7c842b28392daebb93c4a 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=c241a0f2c0e6e3ec3b1415e10a8516c8 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=0b88fe499a3c01dbd424ee943e9ab0c9 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=fcdffc7f6d2b907681018e42cdbe0920 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=bc180b4a9a96edc502c5b49470ca3881 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=70bbd09f29afc200f6c9111495cd5f05 2500w" />

<img className="hidden max-w-full dark:block" noZoom src="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=47a32d4f515a118a7500a0e2aec3beed" data-og-width="2120" width="2120" data-og-height="960" height="960" data-path="images/api-versioning-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=280&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=deb21035b92a663a67b5cfe9420d999d 280w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=560&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=8519ab97f6f889abeaab6105ea681e31 560w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=840&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=dd4ef1e1e99cb42da31c83a7cd0d5e5d 840w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=1100&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=927c7d86e73e85f417c832a96e98fdbb 1100w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=1650&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=eb0c5f538f0b3422c475280f09476a62 1650w, https://mintcdn.com/pinecone/9qvQp5nU6duJvusQ/images/api-versioning-dark.png?w=2500&fit=max&auto=format&n=9qvQp5nU6duJvusQ&q=85&s=eacb669a6469064133034bdc1e30add1 2500w" />

## Specify an API version

<Warning>
  When using the API directly, it is important to specify an API version in your requests. If you don't, requests default to the oldest supported stable version. Once support for that version ends, your requests will default to the next oldest stable version, which could include breaking changes that require you to update your integration.
</Warning>

To specify an API version, set the `X-Pinecone-Api-Version` header to the version name.

For example, based on the version support diagram above, if it is currently October 2025 and you want to use the latest stable version to describe an index, you would set `"X-Pinecone-Api-Version: 2025-10"`:

```shell curl theme={null}
PINECONE_API_KEY="YOUR_API_KEY"

curl -i -X GET "https://api.pinecone.io/indexes/movie-recommendations" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
```

To use an older version, specify that version instead.

## SDK versions

Official [Pinecone SDKs](/reference/pinecone-sdks) provide convenient access to Pinecone APIs. SDK versions are pinned to specific API versions. When a new API version is released, a new version of the SDK is also released.

For the mapping between SDK and API versions, see [SDK versions](/reference/pinecone-sdks#sdk-versions).

## Breaking changes

Breaking changes are changes that can potentially break your integration with a Pinecone API. Breaking changes include:

* Removing an entire operation
* Removing or renaming a parameter
* Removing or renaming a response field
* Adding a new required parameter
* Making a previously optional parameter required
* Changing the type of a parameter or response field
* Removing enum values
* Adding a new validation rule to an existing parameter
* Changing authentication or authorization requirements

## Non-breaking changes

Non-breaking changes are additive and should not break your integration. Additive changes include:

* Adding an operation
* Adding an optional parameter
* Adding an optional request header
* Adding a response field
* Adding a response header
* Adding enum values

## Get updates

To ensure you always know about upcoming API changes, follow the [Release notes](/release-notes/).
