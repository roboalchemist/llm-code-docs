# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-draft-attachment-view/index.md

---

title: rtk-draft-attachment-view · Cloudflare Realtime docs
description: API reference for rtk-draft-attachment-view component (Web
  Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-draft-attachment-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-draft-attachment-view/index.md
---

A component which renders the draft attachment to send

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `attachment` | `{ type: 'image' \| 'file'; file: File; }` | ✅ | - | Attachment to display |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-draft-attachment-view></rtk-draft-attachment-view>
```

### With Properties

```html
<rtk-draft-attachment-view>
</rtk-draft-attachment-view>
```

```html
<script>
  const el = document.querySelector("rtk-draft-attachment-view");


  el.attachment= {};
</script>
```
