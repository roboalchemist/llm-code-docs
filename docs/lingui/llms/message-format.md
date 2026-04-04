# Source: https://lingui.dev/guides/message-format.md

# ICU MessageFormat

ICU MessageFormat is a flexible and powerful syntax designed to express the grammatical nuances of different languages. Its flexibility ensures that your application can handle grammatical variations, making it essential for effective internationalization.

## Overview[​](#overview "Direct link to Overview")

### Simple text[​](#simple-text "Direct link to Simple text")

Example: `Refresh inbox`

### Variables[​](#variables "Direct link to Variables")

Example: `Attachment {name} saved`

### Plurals[​](#plurals "Direct link to Plurals")

> Using language specific plural forms (`one`, `other`):

```
{count, plural, one {Message} other {Messages}}
```

> Using exact matches for specific counts (`=0`):

```
{count, plural, =0 {No messages}
                one {# message}
                other {# messages}}
```

> Offsetting plural forms:

```
{count, plural, offset:1
                =0 {Nobody read this message}
                =1 {Only you read this message}
                one {You and # friend read this message}
                other {You and # friends read this message}
```

### Select[​](#select "Direct link to Select")

```
{gender, select, male {He replied to your message}
                 female {She replied to your message}
                 other {They replied to your message}}
```

### Ordinals[​](#ordinals "Direct link to Ordinals")

```
{count, selectOrdinal, one {#st message}
                       two {#nd message}
                       few {#rd message}
                       other {#th message}}
```

## See Also[​](#see-also "Direct link to See Also")

* [Pluralization](/guides/plurals.md)
* [ICU Playground](https://format-message.github.io/icu-message-format-for-translators/editor.html)
