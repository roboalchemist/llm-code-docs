# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-poll-form/index.md

---

title: rtk-poll-form · Cloudflare Realtime docs
description: API reference for rtk-poll-form component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-poll-form/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-poll-form/index.md
---

A component that lets you create a poll.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-poll-form></rtk-poll-form>
```

### With Properties

```html
<rtk-poll-form>
</rtk-poll-form>
```

```html
<script>
  const el = document.querySelector("rtk-poll-form");


  el.iconPack= defaultIconPack
</script>
```
