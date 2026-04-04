# Source: https://posthog.com/docs/product-tours/localization.md

# Localization - Docs

**Product tours is in private alpha**

Product Tours is currently in private alpha. [Share your thoughts](https://app.posthog.com/external_surveys/019af5f5-a50e-0000-b10f-e8c30c0b73a0) and we'll reach out with early access.

**Currently only available on the web. Requires `posthog-js` >= v1.324.0.**

Configure your tours, banners, and announcements to display in the user's locale.

## How it works

For tours and announcements, you can create any number of **Translations**.

Each translation is keyed on a [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag).

When a tour or announcement is displayed, PostHog chooses the translation based on the user's browser language or your `override_display_language` config setting.

## Creating translations

### Set the default language

First, set the default language for your tour.

When you set a default language, all existing tour content is mapped to the new default.

This is used as a fallback when the user's language cannot be determined, or when your tour does not support the user's provided language.

Open the **Translations** panel in the editor, and enter a language code that represents your tour's default.

![Product Tour Translations panel](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_16_at_7_45_43_PM_c55596a1e6.png)

### Add a new language

Once the default is set, you can add more languages in the same **Translations** panel.

Enter a new language code, click the plus button to add it, then click the language card to select it.

![Product Tour Translations panel](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_16_at_8_04_07_PM_53f2b73cdc.png)

Once selected, a new language code appears at the top of the editor, and you can make any changes necessary for this translation.

If you have other translatable fields beyond the pop-up content, they appear below the content editor.

![Product Tour Translations panel](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_16_at_8_06_51_PM_f9ac90017b.png)

## Language code matching

When determining which tour translation to use, we run the following checks in this order:

1.  **Exact match** – A user with language `en-US` matches a tour with translation `en-US`.
2.  **Base match** – If no exact matches are found, we check for translations matching the user's "base" language. For example, a user language `en-GB` will match a tour with translation `en`, if no translation exists specifically for `en-GB`.
3.  **Fallback** – If neither of the above are successful, we fall back to the tour's default language.

**Base matching is one-directional**

A user with language `en` will not match a tour translation `en-US`. For this reason, we recommend keeping your translation keys as base-only (like `en`), unless you have translations for specific dialects.

## Language overrides

By default, PostHog uses the user's browser language to determine which tour translation to show.

This can be overridden by setting the `override_display_language` property in `posthog.init`.

typescript

PostHog AI

```typescript
// set in posthog.init
posthog.init('<ph_project_token>', {
  api_host: '<ph_app_host>',
  defaults: '2026-01-30',
  disable_product_tours: false,
  override_display_language: 'en-US',
});
```

You can also use the `posthog.set_config` method to change the configuration after initialization.

typescript

PostHog AI

```typescript
posthog.set_config({
  override_display_language: 'en-GB',
})
```

## Which languages should you support?

This is different for everyone, but you can quickly check common browser languages from your users by running a query like this in the [SQL editor](https://app.posthog.com/sql):

SQL

[Run in PostHog](https://us.posthog.com/sql?open_query=SELECT+%0A++++properties.%24browser_language+AS+language%2C%0A++++uniq%28distinct_id%29+AS+unique_users%0AFROM+events%0AWHERE+event+%3D+'%24pageview'%0A++++AND+timestamp+%3E%3D+now%28%29+-+interval+30+day%0AGROUP+BY+language%0AORDER+BY+unique_users+DESC%0ALIMIT+100)

PostHog AI

```sql
SELECT
    properties.$browser_language AS language,
    uniq(distinct_id) AS unique_users
FROM events
WHERE event = '$pageview'
    AND timestamp >= now() - interval 30 day
GROUP BY language
ORDER BY unique_users DESC
LIMIT 100
```

This will show the top 100 languages based on `$pageview` events, grouped by distinct IDs, in the past 30 days.

![Product Tour Translations panel](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_17_at_12_31_33_PM_2dac28a17d.png)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better