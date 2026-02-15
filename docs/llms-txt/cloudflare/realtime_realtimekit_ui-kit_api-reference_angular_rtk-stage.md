# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage/index.md

---

title: rtk-stage · Cloudflare Realtime docs
description: API reference for rtk-stage component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-stage/index.md
---

A component used as a stage that commonly houses the `grid` and `sidebar` components.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-stage></rtk-stage>
```

### With Properties

```html
<!-- component.html -->
<rtk-stage
 [iconPack]="defaultIconPack"
 [t]="rtki18n">
</rtk-stage>
```
