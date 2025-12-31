# Source: https://docs.avaamo.com/user-guide/recent-releases/release-notes-v8.2.0/fix-patch-releases-v8.2.1.md

# Fix patch releases (v8.2.1)

This fix patch release contains critical bug fixes, performance fixes, and minor bug fixes. The following are some of the key fixes included in this release:

1. [LLaMB: Security for Citation links](#llamb-security-for-citation-links)
2. [LLaMB: Response formatting fixes](#llamb-response-formatting-fixes)

## LLaMB: Security for Citation links

* Citation links now expire 24 hours after generation, restricting access to a specific timeframe.
* Additional checks ensure links are accessible only to authenticated, authorized users.
* The citation link format now includes security tokens for validation, as detailed below:
  * Old Citation Link Format:

    <pre data-overflow="wrap"><code><strong>https://llambx.avaamo.com/answers/external/document-groups/{document-group_id}/documents/{document_uuid}#page={page_no}
    </strong></code></pre>
  * New Citation Link Format:

    <pre data-overflow="wrap"><code>https://cx.avaamo.com/llamb/messages/{message_uuid}/documents/{document_uuid}?lt={base64_encoded_JWT_token}&#x26;page={page_number}
    </code></pre>

{% hint style="danger" %}
**Important**: All existing citation links in the Conversation history, Query insights, and agent conversations will expire 24 hours after patch release 8.2.1. Contact Avaamo support to regain access.
{% endhint %}

See [Citation link](https://docs.avaamo.com/user-guide/llamb/citation-links), for more information.

## LLaMB: Response formatting fixes

* LLaMB responses support markdown formatting with the `Use MD Format` option, enabling rich text elements like bold, italics, and hyperlinks.
* Hyperlinks within the ingested documents are accessible through the LLaMB Responses.

{% hint style="danger" %}
**Important:**

1. The [`Use MD Format`](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration#use-md-format) option is available for [Web](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel), [Custom](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/custom-channel#configure-custom-channel), and, Mobile ([Android](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/android-apps) and [iOS](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/ios-apps)) channels.&#x20;
2. To utilize this option, ensure you re-ingest the document before enabling it.
   {% endhint %}

See [Use MD Format](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/widget-configuration#use-md-format),  for more information.
