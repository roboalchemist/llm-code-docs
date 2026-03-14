# Source: https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant/available-providers/openai.md

# OpenAI

{% hint style="info" %}
The AI Writing Assistant AddOn is only available for [Superpowers](https://developers.beefree.io/pricing-plans) and [Enterprise](https://developers.beefree.io/pricing-plans) plans. The AI Writing Assistant and OpenAI provider are available for Email, Page, and Popup builders.
{% endhint %}

## **Overview**

This page discusses how to configure OpenAI as a provider for the [AI Writing Assistant AddOn](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant) within the Beefree SDK Developer Console. If the AI Writing Assistant AddOn is already enabled for your application, and you'd like to switch providers, take the steps outlined in the [Switch Providers](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant/..#switch-providers) section of the [AI Writing Assistant page](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant/..#switch-providers) to enable OpenAI as your new provider.

{% hint style="info" %}
**Note:** [ChatGPT4o Mini](https://platform.openai.com/docs/models) is the model used when you configure OpenAI as your provider.
{% endhint %}

## **Prerequisites**

Prior to getting started, ensure you have the following:

* An OpenAI account and API Key.
* The AI Writing Assistant AddOn enabled in the [Beefree SDK Developer Console](https://developers.beefree.io/login?from=website_menu).
* Beefree SDK [Superpowers or Enterprise plan](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant/available-providers/broken-reference).

## **Configuration Steps**

Take the following steps to configure this provider:

1. Log in to the [Beefree SDK Developer Console](https://developers.beefree.io/login?from=website_menu).
2. Navigate to the application with the AI Writing Assistant enabled.
   1. Click **Details**.
3. Navigate to the **AddOns** under **Application configuration** section.
   1. Click **View more**.
4. Click the **Manage Providers** tab.
5. Click **Add provider**.
6. Complete the required information.\*
7. Click **Save** to save your provider configuration.

\*Reference the [Required Provider Information](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant/..#required-provider-information) section of the [AI Writing Assistant AddOn page](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant) to reference what information is required to configure OpenAI as a provider.

### Shared Logic Considerations

Consider the following shared logic when integrating the AI Writing Assistant AddOn and OpenAI as a provider:

* **Methods:** The methods used for the OpenAI provider are inherited from the [AI Writing Assistant AddOn](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant). These include functionality for generating content for supported block types (Title, Paragraph, List, Button) and for handling metadata.
* **Events:** The integration supports all events from the [AI Writing Assistant](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant), such as tracking user actions and processing content generation requests.
* **Callbacks:** All callbacks associated with the OpenAI provider are inherited from the [AI Writing Assistant](https://docs.beefree.io/beefree-sdk/builder-addons/partner-addons/ai-writing-assistant). They manage notifications for successful or failed content generation attempts.

### Additional Considerations

* **Billing**: Refer to [OpenAI’s pricing documentation](https://help.openai.com/en/collections/3943089-account-login-and-billing) for more information.
