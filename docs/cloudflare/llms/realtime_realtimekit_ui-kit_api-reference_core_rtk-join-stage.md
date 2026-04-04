# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-join-stage/index.md

---

title: rtk-join-stage · Cloudflare Realtime docs
description: API reference for rtk-join-stage component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-join-stage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-join-stage/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | UI Config |
| `dataConfig` | `ModalDataConfig` | ✅ | - | Content Config |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<rtk-join-stage></rtk-join-stage>
```

### With Properties

```html
<rtk-join-stage
 size="md">
</rtk-join-stage>
```

```html
<script>
  const el = document.querySelector("rtk-join-stage");


  el.meeting= meeting
</script>
```
