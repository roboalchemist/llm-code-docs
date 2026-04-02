Source: https://docs.slack.dev/changelog/2017/09/01/locale-locale-locale

# Locale locale locale

September 1, 2017

Slack now supports multiple languages, and your app or integration can too.

Add a `locale` in [user](/reference/objects/user-object) and [conversation](/reference/objects/conversation-object) by using the `include_locale=true` parameter when requesting a bundle of Web API methods supporting it.

The locale field is a string containing a [IETF language code](https://en.wikipedia.org/wiki/IETF_language_tag), such as `en-US`. `fr-FR`, `es-ES`, or `de-DE`, and other future values.

We now support `include_locale` on these methods. Opt-in to receive a `locale` field in user profiles or the `locale` of a conversation.

* [`conversations.info`](/reference/methods/conversations.info)
* [`rtm.start`](/reference/methods/rtm.start)
* [`users.info`](/reference/methods/users.info)
* [`users.list`](/reference/methods/users.list)

If you don't include the parameter, no `locale` will be provided. It's opt-in.

You'll also see locale information changes in related user profile change events in the RTM and Events APIs.

## What isn't changing? {#not_changing}

We're not forcing `locale` fields on you. If you don't opt in you won't see them, except maybe in user profile change events.

Your apps and bots cannot yet declare their locale.

## What happens if I do nothing? {#happens}

Nothing really. You and your app won't "know" the locale of a user or conversational space. You won't be able to customize your app's experience for them. Your app or bot will just speak in its native tongue.

## How do I prepare? {#prepare}

Start sending the `include_locale` parameter to relevant methods. Consume the `locale` value and customize experience, like the language or maybe cultural references to be appropriate for that region, culture, or language.

Stay tuned for best practices in app and bot internationalization.

## When is this happening? {#when}

This all started happening on September 12, 2017.

**Tags:**

* [New feature](/changelog/tags/new-feature)
