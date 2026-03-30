# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-waiting-screen/index.md

---

title: rtk-waiting-screen · Cloudflare Realtime docs
description: API reference for rtk-waiting-screen component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-waiting-screen/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-waiting-screen/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-waiting-screen></rtk-waiting-screen>
```

### With Properties

```html
<rtk-waiting-screen>
</rtk-waiting-screen>
```

```html
<script>
  const el = document.querySelector("rtk-waiting-screen");


  el.meeting= meeting
</script>
```
