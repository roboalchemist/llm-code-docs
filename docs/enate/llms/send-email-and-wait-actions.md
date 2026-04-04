# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/send-email-and-wait-actions.md

# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/processing-an-action/send-email-and-wait-actions.md

# 'Send Email' and 'Send Email and Wait' Actions

## Overview

'Send Email' Actions involve Enate auto-sending an email and then the Action will immediately close. Work Manager Users should not have to do any work on this type of Action.

'Send Email and Wait' Actions involve Enate auto-sending an email. The Action will then move to a state of Waiting until a response has been received. Once a response has been received, the Action will move to a state of To Do to be processed further.&#x20;

The To address and any CC or BCC addresses on the email are configured in Builder - see this article about how to configure 'Send Email' Actions in Builder:

{% content-ref url="../../../builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab" %}
[email-action-info-tab](https://docs.enate.net/enate-help/builder/builder-2021.1/case-configuration/adding-actions-to-a-case/email-action-info-tab)
{% endcontent-ref %}

Once the email has been sent, an entry will appear in the timeline showing when it was sent, who it sent from and to, any CC or BCC addresses, the email subject and if you click to expand, the email body itself.&#x20;

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC1k6yxkA8RGOKK0huxob%2Fimage.png?alt=media&#x26;token=c5378c66-4216-4eea-a1c3-35847b0aed54" alt=""><figcaption></figcaption></figure>

## Exceptions

If an invalid To, CC or BCC email address is used, the email for the Send Email/Send Email and Wait Action will fail to auto-send and the Action will then be moved back to its Queue.&#x20;

A warning will appear in the timeline:

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2Ft9LYFTaD3Z1TU8mIKeU1%2Fimage.png?alt=media&#x26;token=412e9ad4-9b89-4196-9613-cb625e1e17d0" alt=""><figcaption></figcaption></figure>

The Case owner can then decide if they want to manually send the email and will need to correct the email address and add the email body manually. They should also contact their system administrator to alert them about the issue so that they can correct the email address to prevent future email failure.
