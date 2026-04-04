# Source: https://docs.luciq.ai/organization-settings/user-management/scim-provisioning.md

# SCIM Provisioning

{% hint style="warning" %}
To enable SCIM in your company, you must enable [SAML](https://docs.luciq.ai/organization-settings/user-management/sso-using-saml) first
{% endhint %}

You’ll need to follow these steps:

1\. After enabling SAML on the dashboard and linking the dashboard to Okta

2\. Navigate to the app's general settings in Okta

3\. Enable provisioning using SCIM

<figure><img src="https://downloads.intercomcdn.com/i/o/807118367/9f0ee6d946b3f7a6f2fa7a0f/f9327e1e-20a8-4f18-8539-1241ce35614b.png?expires=1764262800&#x26;signature=6b7957724df508875f8dfe4cb1a30ccbc0ae99ca313c563f5a786a43b3d33afb&#x26;req=fCAgF8h2nodYFb4f3HP0gETUO35ilQRqrIK3hhZDJBCLGxTEnCnodrz%2FNQPQ%0ALAPnF6cNjh%2FquWy0mw%3D%3D%0A" alt=""><figcaption></figcaption></figure>

4\. Navigate to the provisioning tab and edit the provisioning integration

* SCIM connector base URL → SCIM basic URL (found on Configure SCIM modal on the dashboard)
* Unique identifier field for users → set it to “email”
* Supported provisioning actions → enable “Push New Users” & “Push Profile Updates”
* Authentication Mode → set it to “HTTP Header”
* Authorization → Authentication Token (found on Configure SCIM modal on the dashboard)

{% hint style="warning" %}
Enable SCIM from the dashboard first before saving the integration configuration in OKTA
{% endhint %}

5\. Navigate to “Provisioning to App” and edit permissions

<figure><img src="https://downloads.intercomcdn.com/i/o/807123107/8ef55c886774887c31ff9603/3bb1a9f4-b273-4a2a-be65-103e45fe80cc.png?expires=1764262800&#x26;signature=c598f11d26c918ea314e5108b3d4445aec552876271b8c6117d035fafe7c897a&#x26;req=fCAgF8t9nIFYFb4f3HP0gIxEIvEnzFX8ZKUjRvWgpdn%2FZtrMHaFr%2BceLGFQN%0AeZyrY2R0T1BiZI6pkg%3D%3D%0A" alt=""><figcaption></figcaption></figure>

6\. Enable both “Create Users“ & “Deactivate Users“ permissions and save changes

<figure><img src="https://downloads.intercomcdn.com/i/o/ih9pma6x/1401638173/f5d35e212dbbf9d533946e8c5556/image.png?expires=1764262800&#x26;signature=a7d593d1e26107da88b0630650f861a54e6c3c87c7d8ebd3a7332b72e16467ff&#x26;req=dSQnF899lYBYWvMW1HO4zX9d9S1rNJCpp%2Fg340rW9X1El%2FXT8INPqHXT55UQ%0AiAQDeU%2FOxEX3o0Pqszs%3D%0A" alt=""><figcaption></figcaption></figure>

7\. Voila! You have now enabled and configured SCIM on both the dashboard & Okta instances.&#x20;

You can now see assign & un-assign actions reflected on the dashboard once done on Okta.

{% hint style="success" %}

### Recommendation

Additionally you can configure Luciq role and application access mapping when provisioning users to Luciq dashboard.

Follow the procedures [here](https://docs.luciq.ai/organization-settings/user-management/broken-reference) to enable role and application access mapping.
{% endhint %}
