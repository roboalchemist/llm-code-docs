# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/index.md

---

title: rtk-emoji-picker · Cloudflare Realtime docs
description: API reference for rtk-emoji-picker component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-emoji-picker/index.md
---

A very simple emoji picker component.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `focusWhenOpened` | `boolean` | ✅ | - | Controls whether or not to focus on mount |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-emoji-picker></rtk-emoji-picker>
```

### With Properties

```html
<rtk-emoji-picker>
</rtk-emoji-picker>
```

```html
<script>
  const el = document.querySelector("rtk-emoji-picker");


  el.focusWhenOpened= true;
</script>
```
