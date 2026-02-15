# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification/index.md

---

title: rtk-notification · Cloudflare Realtime docs
description: API reference for rtk-notification component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-notification/index.md
---

A component which shows a notification. You need to remove the element after you receive the `rtkNotificationDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `notification` | `Notification` | ✅ | - | Message |
| `paused` | `boolean` | ✅ | - | Stops timeout when true |
| `size` | `Size` | ✅ | - | Size |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-notification></rtk-notification>
```

### With Properties

```html
<rtk-notification
 size="md">
</rtk-notification>
```

```html
<script>
  const el = document.querySelector("rtk-notification");


  el.paused= true;
</script>
```
