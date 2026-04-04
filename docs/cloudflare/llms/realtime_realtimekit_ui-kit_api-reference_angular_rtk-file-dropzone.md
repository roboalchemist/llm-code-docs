# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/index.md

---

title: rtk-file-dropzone · Cloudflare Realtime docs
description: API reference for rtk-file-dropzone component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-file-dropzone/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `hostEl` | `HTMLElement` | ✅ | - | Host element on which drop events to attach |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n1` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-file-dropzone></rtk-file-dropzone>
```

### With Properties

```html
<!-- component.html -->
<rtk-file-dropzone
 [hostEl]="htmlelement">
</rtk-file-dropzone>
```
