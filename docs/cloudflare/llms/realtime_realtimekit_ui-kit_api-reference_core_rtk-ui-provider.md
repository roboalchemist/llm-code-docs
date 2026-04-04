# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/index.md

---

title: rtk-ui-provider · Cloudflare Realtime docs
description: API reference for rtk-ui-provider component (Web Components (HTML) Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/core/rtk-ui-provider/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig1` | ✅ | - | Config |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting \| null` | ❌ | `null` | Meeting |
| `mode` | `MeetingMode1` | ✅ | - | Fill type |
| `overrides` | `Overrides1` | ❌ | `defaultOverrides` | UI Kit Overrides |
| `showSetupScreen` | `boolean` | ✅ | - | Whether to show setup screen or not |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language utility |

## Usage Examples

### Basic Usage

```html
<rtk-ui-provider></rtk-ui-provider>
```

### With Properties

```html
<rtk-ui-provider>
</rtk-ui-provider>
```

```html
<script>
  const el = document.querySelector("rtk-ui-provider");


  el.config= defaultUiConfig
  el.mode= meeting
  el.showSetupScreen= true;
</script>
```
