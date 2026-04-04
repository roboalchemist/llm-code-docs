# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/index.md

---

title: rtk-chat-search-results · Cloudflare Realtime docs
description: API reference for rtk-chat-search-results component (Web Components
  (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-chat-search-results/index.md
---

@deprecated `rtk-chat-search-results` is deprecated and will be removed soon. Use `rtk-chat-messages-ui-paginated` instead. -

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `channelId` | `string` | ✅ | - | Channel id |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `query` | `string` | ✅ | - | Search query |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-chat-search-results></rtk-chat-search-results>
```

### With Properties

```html
<rtk-chat-search-results
 channelId="example"
 query="example">
</rtk-chat-search-results>
```

```html
<script>
  const el = document.querySelector("rtk-chat-search-results");


  el.meeting= meeting
</script>
```
