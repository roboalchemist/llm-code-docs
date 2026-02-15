# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-audio/index.md

---

title: rtk-participants-audio · Cloudflare Realtime docs
description: API reference for rtk-participants-audio component (Angular Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-audio/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/angular/rtk-participants-audio/index.md
---

A component which plays all the audio from participants and screenshares.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `preloadedAudioElem` | `HTMLAudioElement` | ✅ | - | Pass existing audio element |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```html
<!-- component.html -->
<rtk-participants-audio></rtk-participants-audio>
```

### With Properties

```html
<!-- component.html -->
<rtk-participants-audio
 [meeting]="meeting"
 [preloadedAudioElem]="htmlaudioelement">
</rtk-participants-audio>
```
