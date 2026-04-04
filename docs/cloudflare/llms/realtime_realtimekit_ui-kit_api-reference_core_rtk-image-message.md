# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message/index.md

---

title: rtk-image-message · Cloudflare Realtime docs
description: API reference for rtk-image-message component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-image-message/index.md
---

@deprecated `rtk-image-message` is deprecated and will be removed soon. Use `rtk-image-message-view` instead. A component which renders an image message from chat.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `isContinued` | `boolean` | ✅ | - | Whether the message is continued by same user |
| `message` | `ImageMessage` | ✅ | - | Text message object |
| `now` | `Date` | ✅ | - | Date object of now, to calculate distance between dates |
| `showBubble` | `boolean` | ✅ | - | show message in bubble |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-image-message></rtk-image-message>
```

### With Properties

```html
<rtk-image-message>
</rtk-image-message>
```

```html
<script>
  const el = document.querySelector("rtk-image-message");


  el.isContinued= true;
</script>
```
