# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-settings-toggle/index.md

---

title: rtk-settings-toggle · Cloudflare Realtime docs
description: API reference for rtk-settings-toggle component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-settings-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-settings-toggle/index.md
---

A button which toggles visibility of settings module. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeSettings: boolean; }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `variant` | `ControlBarVariant` | ✅ | - | Variant |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-settings-toggle></rtk-settings-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-settings-toggle
 size="md"
 variant="button">
</rtk-settings-toggle>
```
