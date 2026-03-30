# Source: https://exa.ai/docs/changelog/sdk-major-version-changes.md

> ## Documentation Index

> Fetch the complete documentation index at: https://exa.ai/docs/llms.txt

> Use this file to discover all available pages before exploring further.

# SDK changes: highlights removed and contents returned by default

> Major SDK update with contents included by default in search, highlights feature removed from SDKs, and use_autoprompt field deprecated in all API responses.

***

**Date: October 28, 2025**

We're releasing a major version update to our SDKs along with changes to API responses. This update makes content retrieval more convenient while removing deprecated features.

### 1. Contents Included by Default in SDKs

Search operations in the SDKs now include page contents by default, eliminating the need for a separate contents call in most workflows. You can opt out if you need faster searches without content.

### 2. Highlights Feature Removed from SDKs

The highlights feature has been completely removed from all SDKs. This feature was previously deprecated and is no longer available in the SDK packages.

> *Update (November 2025): Highlights have been reintroduced in the JavaScript SDK as of `exa-js` v2.0.11. See [JS SDK: highlights restored](/changelog/highlights-restored-js-sdk) for details.*

**Migration Options:**

* **Option 1**: Do not upgrade to the new major version if you still need highlights
* **Option 2**: Use the API directly to access highlights functionality
* **Option 3**: Use "AI Summary" to get the main summary of "text"

### 3. use\_autoprompt Deprecated in All API Responses

The `use_autoprompt` field has been deprecated and removed from all API responses across the entire platform. This field is no longer needed with current search improvements.

## Need Help?

If you have questions about upgrading or need help with migration, please reach out to [hello@exa.ai](mailto:hello@exa.ai). We're here to help ensure a smooth transition to the new major version.
