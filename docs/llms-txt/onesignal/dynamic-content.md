# Source: https://documentation.onesignal.com/docs/en/dynamic-content.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Dynamic Content with CSV

> Learn how to use OneSignal Dynamic Content to personalize Push Notifications, SMS, and Emails at scale using CSV uploads and Liquid syntax.

## Overview

OneSignal provides several ways to [personalize message content](./message-personalization) at scale. This guide focuses on using the Dynamic Content with CSV upload feature found in the OneSignal dashboard for push, email, and SMS.

**Key benefits:**

* **Use a CSV to personalize at scale** – One message, custom experiences for everyone
* **Multi-language support** – Automatic language switching per user
* **Dynamic segmentation** – Content adapts to user properties (language, region, campaign ID)
* **Team collaboration** – Non-technical users edit content in CSV files
* **Cross-channel compatibility** – Reuse CSV logic across channels

**Common use cases:**

* Multi-language onboarding or marketing
* Region-specific promotions
* Event announcements per location
* Campaign-based personalization

***

## Dynamic Content with CSV setup steps

**Quick reference:**

1. Create a CSV file with your content variations.
2. Map the CSV data to the message using the `dynamic_content` property in liquid syntax.
3. Create a new message or [template](./templates) from the OneSignal dashboard.
4. Select the **Dynamic Content** or **Personalization** button.
5. Upload the CSV file and send the message.

### CSV requirements & setup

* **File size:** Under 200 KB
* **Column headers:**
  * Reserve the first column header for the tag key or leave blank to reference sections
  * Alphanumeric characters and underscores only
  * Use underscores (`_`) instead of spaces
* **Encoding:** UTF-8

Start with a blank CSV or use a provided template. Templates are provided when selecting the **Dynamic Content** or **Personalization** button in the message and template editors.

<Frame caption="Dynamic Content button found in the message editor.">
  <img src="https://mintcdn.com/onesignal/jBdBk5XvQR5eKOks/images/docs/772f91e24ebca83a05d4e96819a41ec58d5ca0acd3a715e971c4a43ba7654494-Screenshot_2025-02-10_at_5.23.32_PM.png?fit=max&auto=format&n=jBdBk5XvQR5eKOks&q=85&s=c51a6fcb07f7aab797cbfe74423530cb" width="1960" height="380" data-path="images/docs/772f91e24ebca83a05d4e96819a41ec58d5ca0acd3a715e971c4a43ba7654494-Screenshot_2025-02-10_at_5.23.32_PM.png" />
</Frame>

Templates are available for:

* **Multi-language** – Localize content by language
* **Content personalization** – Customize content by Data Tags

<Frame caption="CSV template options in the OneSignal dashboard.">
  <img src="https://mintcdn.com/onesignal/YOTSrtBSoqdrJ37A/images/docs/47f48b79aa100bd5d2c59a418216bafba75daaa92d0bf939dcd3ccceca39cd7c-Screenshot_2025-02-10_at_5.26.15_PM.png?fit=max&auto=format&n=YOTSrtBSoqdrJ37A&q=85&s=87947eb40093580c8589cf7eb4183564" width="1986" height="870" data-path="images/docs/47f48b79aa100bd5d2c59a418216bafba75daaa92d0bf939dcd3ccceca39cd7c-Screenshot_2025-02-10_at_5.26.15_PM.png" />
</Frame>

#### Example CSVs

This guide will use the following example CSV data.

<Tabs>
  <Tab title="Multi-language Template Example">
    * Map the column headers to your [supported language codes](./multi-language-messaging#supported-languages).
    * Add your translations to each row for each language code.
    * If you have multiple sections (like in an email), designate the first column as the section name.

    In this example:

    * We have 3 languages: English, Spanish, and French.
    * We have 2 sections: "section\_1" and "section\_2".

    <Frame caption="Multi-language CSV matching user language attribute to content (similar to VLOOKUP).">
      <img src="https://mintcdn.com/onesignal/0qspEXXeJ8zJbkJ-/images/docs/8716e43deead16759c2500d85900d2d1be8b6a9c51e0477160569b05534a58fb-Screenshot_2025-02-10_at_8.37.25_PM.png?fit=max&auto=format&n=0qspEXXeJ8zJbkJ-&q=85&s=4a20651cf2949bad117b8a9fda432536" width="1438" height="220" data-path="images/docs/8716e43deead16759c2500d85900d2d1be8b6a9c51e0477160569b05534a58fb-Screenshot_2025-02-10_at_8.37.25_PM.png" />
    </Frame>
  </Tab>

  <Tab title="Content Personalization Template Example">
    * Map the first column header to the tag key and underlying rows to the values you want to reference. See [Tags](./add-user-data-tags) for more information on adding tags to users.
    * Map the remaining column headers to the sections or components you want to personalize.

    In this example:

    * We have a tag key: `campaign_id` with possible values of `A` and `B`.
    * We have 2 sections or components: "title", "message", and "url".

    <Frame caption="Personalization CSV using campaign_id Data Tag.">
      <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2d49628c7c891801e50b7f397442f5887e7b776897d24788be16887ed191f631-Screenshot_2025-04-10_at_9.47.35_AM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=23ec0fe2224cc3103e7a7c62168dd050" width="1406" height="160" data-path="images/docs/2d49628c7c891801e50b7f397442f5887e7b776897d24788be16887ed191f631-Screenshot_2025-04-10_at_9.47.35_AM.png" />
    </Frame>

    <Warning>
      **Important:** Remove spaces and non-alphanumeric characters from CSV headers
      or use hash notation in Liquid.
    </Warning>

    <Frame caption="Detailed CSV example using Liquid syntax to reference user Data Tags.">
      <img src="https://mintcdn.com/onesignal/tc0EvmtSSX56SX0c/images/docs/9352ff1-event_translation.csv.png?fit=max&auto=format&n=tc0EvmtSSX56SX0c&q=85&s=e71b92286f500fc201b95bafa2b38a85" width="3189" height="2646" data-path="images/docs/9352ff1-event_translation.csv.png" />
    </Frame>
  </Tab>
</Tabs>

### Map CSV data to message content

Using [Liquid syntax](./using-liquid-syntax), reference the CSV data in your message using the `dynamic_content` property:

```liquid  theme={null}
{{dynamic_content.file_name.message_component[user_property]}}
or
{{dynamic_content.file_name[user_property].message_component}}
```

**Parameters:**

* `dynamic_content` – The property name used to reference the CSV data
* `file_name` – CSV file name (without `.csv` extension)
* `message_component` – The specific message component you want to personalize. This is the static text in the CSV column header or first row.
* `user_property` – The [user property](./message-personalization#properties) you want to reference.

**Fallback content:**

Always use hard-coded string `default` fallbacks to ensure messages render if the CSV lookup or Dynamic Content fails.

```liquid Liquid syntax for the fallback theme={null}
{{ dynamic_content.my_template.header[user.language] | default: "Welcome to our latest update" }}
```

This means if the CSV lookup or Dynamic Content fails, the message will render the fallback text `"Welcome to our latest update"`.

This ensures:

* Dynamic Content is used when available
* A hard-coded message appears if Dynamic Content fails
* Users never receive blank content

<Tabs>
  <Tab title="Multi-language Message Example">
    ```csv translations.csv theme={null}
    ,en,es,fr
    section_1,Hello,Hola,Bonjour
    section_2,Thanks for shopping with us...,Gracias por comprar con nosotros...,Merci pour votre achat avec nous...
    ```

    * The `file_name` is `translations.csv`.
    * The `message_component` is in the rows of the first column `section_1` and `section_2`.
    * The `user_property` is the column header matching language code. We can reference this on the user with the `user.language` [property](./message-personalization#properties).

    ```liquid Basic Liquid syntax for the multi-language message theme={null}
    {{dynamic_content.translations.section_1[user.language]}}
    {{dynamic_content.translations.section_2[user.language]}}
    ```

    ```liquid (Recommended) Liquid syntax with default fallback for the multi-language message theme={null}
    {% assign supported_langs = "en,es,fr,de" | split: "," %}
    {% assign lang = user.language | default: "en" %}

    {% unless supported_langs contains lang %}
      {% assign lang = "en" %}
    {% endunless %}

    {{ dynamic_content.translations.section_1[lang] | default: "Hello" }}
    {{ dynamic_content.translations.section_2[lang] | default: "Thanks for shopping with us..." }}
    ```

    <Frame caption="Adding Liquid syntax for multi-language email content.">
      <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/d0df135475c202308b5b5e40f3893f1beff6d7d387a99e9264c5c5936283d699-Screenshot_2025-02-10_at_10.08.20_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=bb3aaec56a1bcca6e1400b096a5550b7" width="1062" height="446" data-path="images/docs/d0df135475c202308b5b5e40f3893f1beff6d7d387a99e9264c5c5936283d699-Screenshot_2025-02-10_at_10.08.20_PM.png" />
    </Frame>
  </Tab>

  <Tab title="Content Personalization Message Example">
    ```csv content_personalization_template.csv theme={null}
    campaign_id,title,message,url
    campaign_123,Flash deal for you,Tap to claim,https://example.com/flash
    campaign_456,Weekend picks are here,See what's trending,https://example.com/weekend
    default,Our latest offers,See what's new,https://example.com
    ```

    * The `file_name` is `content_personalization_template.csv`.
    * The `user_property` maps to the tag key: `campaign_id`.
    * The `message_component` is the column header mapped to the section of the message you want to personalize (title, message, or url).

    ```liquid Liquid syntax for the content personalization message theme={null}
    {{ dynamic_content.content_personalization_template[campaign_id].title }}
    {{ dynamic_content.content_personalization_template[campaign_id].message }}
    {{ dynamic_content.content_personalization_template[campaign_id].url }}
    ```

    ```liquid (Recommended) Liquid syntax with default fallback for the content personalization message theme={null}
    {% assign cid = campaign_id | default: "default" %}

    {% unless dynamic_content.content_personalization_template[cid] %}
      {% assign cid = "default" %}
    {% endunless %}

    {{ dynamic_content.content_personalization_template[cid].title | default: "Our latest offers" }}
    {{ dynamic_content.content_personalization_template[cid].message | default: "See what's new" }}
    {{ dynamic_content.content_personalization_template[cid].url | default: "https://example.com" }}
    ```

    <Frame caption="Adding Liquid syntax for campaign-based push personalization.">
      <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1c80cff787617df73a16bd4858446a07db6af84f4d79404c4a2ad34e3e509876-Screenshot_2025-02-10_at_9.53.13_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=37a96d318756adc6b0f2a35aecc20c92" alt="Dynamic Content personalization Liquid example" width="1774" height="1018" data-path="images/docs/1c80cff787617df73a16bd4858446a07db6af84f4d79404c4a2ad34e3e509876-Screenshot_2025-02-10_at_9.53.13_PM.png" />
    </Frame>
  </Tab>
</Tabs>

<Check>
  Use Liquid with `default` fallback to update subject lines, preheaders, button
  labels, and URLs.
</Check>

***

## Usage considerations

### How can I test the Dynamic Content with CSV?

We recommend using email to test multiple variations of the message.

* You can use the `+` addressing in emails to test multiple variations: `username+test@example.com`
* Set tags follwing the above multi-language and content personalization examples.
* See [Import](./import) for more on uploading multiple users and data tags.

### When to use Dynamic Content with CSV vs. other personalization options

* Use **Dynamic Content with CSV** if you are sending messages from the dashboard and have access to user data with a CSV file.
* For other options of addign dynamic content to messages, see **[Message Personalization](./message-personalization)** or [Multi-language Messaging](./multi-language-messaging) options.

### Updating templates

Re-upload CSVs via dashboard or use the [Update Template API](/reference/update-template) `dynamic_content` property.

### Special characters in keys

**Hash notation** (for non-alphanumeric keys):

```liquid  theme={null}
{{ dynamic_content.file_name["!the_row!"]["&the_column&"] }}
```

**Dot notation** (for standard keys):

```liquid  theme={null}
{{ dynamic_content.file_name.the_row.the_column }}
```

***

## Related articles

* [Message Personalization](./message-personalization) - Overview of all personalization options
* [Using Liquid Syntax](./using-liquid-syntax) - Complete Liquid syntax reference
* [Import](./import) - Upload user data and segments
* [Templates](./templates) - Create reusable message templates

***

Built with [Mintlify](https://mintlify.com).
