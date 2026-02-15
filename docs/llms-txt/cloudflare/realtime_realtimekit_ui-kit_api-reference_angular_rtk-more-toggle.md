# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-more-toggle/index.md

---

title: rtk-more-toggle · Cloudflare Realtime docs
description: API reference for rtk-more-toggle component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-more-toggle/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-more-toggle/index.md
---

A button which toggles visibility of a more menu. When clicked it emits a `rtkStateUpdate` event with the data:

```ts
{ activeMoreMenu: boolean; }
```

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `size` | `Size` | ✅ | - | Size |
| `states` | `States` | ✅ | - | States object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-more-toggle></rtk-more-toggle>
```

### With Properties

```html
<!-- component.html -->
<rtk-more-toggle
 size="md">
</rtk-more-toggle>
```
