# Source: https://docs.logrocket.com/docs/zendesk.md

# Zendesk

Integrating LogRocket with [Zendesk](https://zendesk.com)

### Basic Integration

This integration adds a LogRocket link to every Zendesk ticket, allowing your support team to quickly watch user sessions from the moment a ticket is created.

After a ticket is submitted, a link to LogRocket will appear as a private note after the initial ticket message. This message will not trigger notifications and is not visible to end-users. A note will only be added if that user actually has LogRocket sessions.

If you use Zendesk's [Brands](https://support.zendesk.com/hc/en-us/articles/4408829476378-Setting-up-multiple-brands) feature to sort tickets, you can select which Brands should receive a LogRocket note. This selection can be made in the Zendesk Integration Settings in LogRocket after enabling the integration.

<Image align="center" src="https://files.readme.io/869536f2ca572a7b49f84d2379877fef585eb375310a138e9ae99c4faa931a0a-Screenshot_2025-01-08_at_10.00.10_AM.png" />

> 🚧 Note
>
> If you aren't receiving a note, be sure that you are identifying your users via the email field in both the LogRocket and Zendesk SDK.

<br />

### AI-Powered Summaries from Galileo Highlights

[Galileo Highlights](https://docs.logrocket.com/docs/galileo-highlights-beta) helps support reps quickly solve user-reported issues by pinpointing their exact area of confusion in the product. When the Highlights Zendesk integration is enabled, LogRocket automatically posts a private comment summarizing the user’s activity leading up to their support request. The focus is on the context and content of their question, giving you immediate insight into the issue.

Key Benefits:

* Instant Context: Get a concise summary of what the user did before submitting their request, allowing you to understand the problem at a glance.
* Quick Access: Direct links to the full session are provided, enabling you to dive deeper whenever necessary.\
  With Galileo Highlights, resolving support issues has never been faster or more intuitive.
* Visual Insights: View screenshots of significant moments from the session, so you can grasp the situation without needing to watch the entire session.

Contact [support@logrocket.com](mailto:support@logrocket.com) for access to this feature, which is available for Pro and Enterprise plans. We offer a complimentary trial period followed by a range of pricing options.

<br />

<Image align="center" src="https://files.readme.io/4a2d918-Galileo_Highlights_API.png" />

## Install

In the Integrations tab of the settings page, simply click on the Zendesk integration button to automatically set it up. You will be asked for your Zendesk subdomain, then you will be redirected to Zendesk to authenticate and authorize LogRocket. After that you can click that button again to change settings.

> 🚧 Requirements
>
> * Your account must have integrations enabled (Team plan or above)
> * You must authenticate with an Agent that has the **admin role**.
> * Please note that this integration can only be enabled for **one project**.  If you are looking for multi project support, we recommend following the instructions for the alternative integrations below

![](https://files.readme.io/667ad3c-Screen_Shot_2018-05-23_at_4.16.45_PM.png "Screen Shot 2018-05-23 at 4.16.45 PM.png")

To limit the integration by Zendesk's [Brands](https://support.zendesk.com/hc/en-us/articles/4408829476378-Setting-up-multiple-brands), first complete the initial installation above. Then, follow these steps:

1. Click on the Zendesk icon after setting up your integration
2. Select brands from the sidebar
3. Save

## Alternative Integration with Text

> ❗️ Zendesk has [discontinued support](https://support.zendesk.com/hc/en-us/articles/6589414770074-Announcing-the-discontinuation-of-select-Built-by-Zendesk-apps) for Zendesk Text

This manual integration uses the Text app from Zendesk to add a link to a user’s LogRocket sessions on ticket pages.

### Install

1. Install the free [Text](https://www.zendesk.com/apps/support/text/) app from the Zendesk directory.

2. Specify a title.

3. For the text display, add the following link (making sure to change YOUR\_ORG and YOUR\_APP with your application ID)

```text
"https://app.logrocket.com/YOUR_ORG/YOUR_APP/sessions?e={{ticket.requester.email}}"
```

4. To view the link, navigate to a ticket and open the Apps panel by clicking the Apps button in the upper right.

<Image align="center" alt={1044} caption="view of LR sessions within ticket" title="image.png" src="https://files.readme.io/6a27a6b-image.png" />

For more information on the Text app, see [here](https://support.zendesk.com/hc/en-us/articles/203660696-Providing-agents-with-more-information-using-the-Iframe-and-Text-apps#topic_b2k_5bw_3m).

## Alternative Integration with URL Builder

This manual integration uses the URL Builder Zendesk app to add a link to LogRocket on ticket pages.

### Install

1. Install the [URL Builder](https://www.zendesk.com/apps/support/url-builder-pro/) app from the Zendesk directory.

2. Add the following to the configuration section (making sure to change YOUR\_ORG and YOUR\_APP with your application id)

```json
[{
  "title": "LogRocket", 
  "url": "https://app.logrocket.com/YOUR_ORG/YOUR_APP/sessions?e={{ticket.requester.email}}"
}]
```

The link to LogRocket will appear on the right "Apps" sidebar:

![](https://files.readme.io/fb55e75-50deb00-Image_2017-12-28_at_5.15.46_PM.png "50deb00-Image_2017-12-28_at_5.15.46_PM.png")