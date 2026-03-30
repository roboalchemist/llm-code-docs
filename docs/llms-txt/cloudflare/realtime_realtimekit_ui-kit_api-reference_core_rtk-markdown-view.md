# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view/index.md

---

title: rtk-markdown-view · Cloudflare Realtime docs
description: API reference for rtk-markdown-view component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-markdown-view/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `maxLength` | `number` | ✅ | - | max length of text to render as markdown |
| `text` | `string` | ✅ | - | raw text to render as markdown |

## Usage Examples

### Basic Usage

```html
<rtk-markdown-view></rtk-markdown-view>
```

### With Properties

```html
<rtk-markdown-view
 text="example">
</rtk-markdown-view>
```

```html
<script>
  const el = document.querySelector("rtk-markdown-view");


  el.maxLength= 42;
</script>
```
