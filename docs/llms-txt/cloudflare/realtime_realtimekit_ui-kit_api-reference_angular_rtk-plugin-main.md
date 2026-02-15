# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-plugin-main/index.md

---

title: rtk-plugin-main · Cloudflare Realtime docs
description: API reference for rtk-plugin-main component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-plugin-main/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-plugin-main/index.md
---

A component which loads a plugin.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting |
| `plugin` | `RTKPlugin` | ✅ | - | Plugin |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-plugin-main></rtk-plugin-main>
```

### With Properties

```html
<!-- component.html -->
<rtk-plugin-main
 [meeting]="meeting"
 [plugin]="rtkplugin">
</rtk-plugin-main>
```
