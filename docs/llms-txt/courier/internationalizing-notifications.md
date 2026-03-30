# Source: https://www.courier.com/docs/tutorials/content/internationalizing-notifications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Internationalize Notifications

> Send multi-language notifications using locale-based conditions, separate templates, or dynamic variables.

There are multiple ways to internationalize your notifications with Courier. The best option depends on the number of languages you support and the complexity of your templates.

## Choose Your Approach

| Approach                        | Best For                                     | Logic Location            |
| ------------------------------- | -------------------------------------------- | ------------------------- |
| Multiple channels, one template | Few languages, single channel type           | Courier (send conditions) |
| Multiple templates              | Many languages, multi-channel                | Your system               |
| Variables from data payload     | Dynamic content, external translation system | Your system               |

### Multiple Channels, One Template

In this model, you create one channel per language within a single template. Courier routes to the correct channel based on [send conditions](/platform/content/template-settings/send-conditions).

This works well for single-channel notifications or when you support just a few languages. Templates can get complex when you have multiple channel types (email, SMS, push) and many languages.

**Requirements:**

* [Channel-level conditionals](/platform/content/template-settings/send-conditions#for-notifications-and-channels)
* User locale stored in [profile](/api-reference/user-profiles/get-a-profile) or sent with the request

<Steps>
  <Step title="Store locale on user profiles">
    Add a `locale` property with [ISO 639-1](https://www.andiamo.co.uk/resources/iso-language-codes/) language codes like `en`, `en_US`, `fr`, `fr_FR`, etc.

    You can store this in Courier profiles or include it in the send request.
  </Step>

  <Step title="Add a channel for each language">
    Create separate channels in your template for each language you support.

    <Frame caption="Each channel corresponds to a different language">
      <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/internationalization-template.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=36ece5a022e7e3d055337d746695d8b9" alt="Template with multiple language channels" width="2652" height="1728" data-path="assets/platform/content/internationalization-template.png" />
    </Frame>
  </Step>

  <Step title="Set up send conditions">
    Configure each channel's send condition to match the corresponding locale.

    <Frame caption="Set a conditional based on locale">
      <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/internationalization-conditional.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=ecc8c05a0bb40bc4cff45ab3899d105a" alt="Channel send condition for locale" width="2652" height="1728" data-path="assets/platform/content/internationalization-conditional.png" />
    </Frame>
  </Step>
</Steps>

### Multiple Templates

In this model, you create a separate template for each language. Your system determines which template to trigger based on the user's language.

This is best for multi-channel notifications when you support many languages, as it keeps each template simple and focused.

<Steps>
  <Step title="Create a template for each language">
    For five supported languages, create five versions of the same template.

    <Frame caption="Templates organized by region">
      <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/internationalization-designer-overview.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=d6123f4c695641c488fd193def2dc129" alt="Templates organized by language" width="903" height="638" data-path="assets/platform/content/internationalization-designer-overview.png" />
    </Frame>
  </Step>

  <Step title="Map language-specific events">
    Assign a unique event name to each template (e.g., `welcome-email-en`, `welcome-email-fr`).

    <Frame caption="Map an event to each template">
      <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/internationalization-event.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=1316683569c32ca44cb29302c1b7f0a6" alt="Event mapping" width="612" height="337" data-path="assets/platform/content/internationalization-event.png" />
    </Frame>
  </Step>

  <Step title="Trigger the correct event">
    In your application, determine the user's language and trigger the corresponding event.
  </Step>
</Steps>

### Variables From Data Payload

In this model, you maintain a single template and pass translated content in your send request. The template uses variables to display the localized content.

This approach works well when you manage translations in your own backend or use an external translation service.

<Steps>
  <Step title="Translate content in your backend">
    Store translated strings in your database or translation management system.
  </Step>

  <Step title="Include translations in the send request">
    Pass the translated content in the `data` object:

    ```json  theme={null}
    {
      "message": {
        "to": { "email": "user@example.com" },
        "template": "TEMPLATE_ID",
        "data": {
          "greeting": "Bonjour",
          "welcome_message": "Bienvenue sur notre plateforme!",
          "cta_text": "Commencer"
        }
      }
    }
    ```
  </Step>

  <Step title="Use variables in your template">
    Reference the translated content using variables.

    <Frame caption="Template using variables for content">
      <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/internationalization-variables.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=f6e3fc7c8edb94581faf723a4d54e826" alt="Template with variables" width="1115" height="797" data-path="assets/platform/content/internationalization-variables.png" />
    </Frame>
  </Step>

  <Step title="Test with localized content">
    Create test events with translated values to preview the result.

    <Frame caption="Test event with translated values">
      <img src="https://mintcdn.com/courier-4f1f25dc/oLXFxRwf6FuGv1s3/assets/platform/content/internationalization-test-event.png?fit=max&auto=format&n=oLXFxRwf6FuGv1s3&q=85&s=4e65279426acd105851a49c11e0c6e0d" alt="Test event with translations" width="1046" height="704" data-path="assets/platform/content/internationalization-test-event.png" />
    </Frame>

    <Frame caption="Preview shows localized content">
      <img src="https://mintcdn.com/courier-4f1f25dc/gz4K47lGiLRsrGch/assets/platform/content/internationalization-preview.png?fit=max&auto=format&n=gz4K47lGiLRsrGch&q=85&s=67ab63001afa793eb3671b9ab246a08a" alt="Localized preview" width="674" height="693" data-path="assets/platform/content/internationalization-preview.png" />
    </Frame>
  </Step>
</Steps>

## API-Driven Localization

For teams using translation management systems (TMS), Courier provides APIs to programmatically manage translations at the block level. This feature is available on Business and Enterprise plans.

See [Localization](/platform/content/localization) for API details.

## Formatting Dates and Numbers

For locale-specific date and number formatting, see [Handlebars Helpers](/platform/content/template-designer/handlebars-designer#use-cases).
