# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-logo/index.md

---

title: rtk-logo · Cloudflare Realtime docs
description: API reference for rtk-logo component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-logo/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-logo/index.md
---

A component which loads the logo from your config, or via the `logo-url` attribute.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `config` | `UIConfig` | ❌ | `createDefaultConfig()` | Config object |
| `logoUrl` | `string` | ✅ | - | Logo URL |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-logo></rtk-logo>
```

### With Properties

```html
<!-- component.html -->
<rtk-logo
 logoUrl="example"
 [meeting]="meeting">
</rtk-logo>
```
