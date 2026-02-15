# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/index.md

---

title: rtk-audio-grid · Cloudflare Realtime docs
description: API reference for rtk-audio-grid component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-audio-grid/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ✅ | - | Config |
| `hideSelf` | `boolean` | ✅ | - | Whether to hide self in the grid |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon Pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `size` | `Size1` | ✅ | - | Size |
| `states` | `States1` | ✅ | - | States |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-audio-grid></rtk-audio-grid>
```

### With Properties

```html
<rtk-audio-grid>
</rtk-audio-grid>
```

```html
<script>
  const el = document.querySelector("rtk-audio-grid");


  el.config= defaultUiConfig
  el.hideSelf= true;
  el.meeting= meeting
</script>
```
