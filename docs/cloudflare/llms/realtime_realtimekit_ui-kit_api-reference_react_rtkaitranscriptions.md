# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/index.md

---

title: RtkAiTranscriptions · Cloudflare Realtime docs
description: API reference for RtkAiTranscriptions component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkaitranscriptions/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `initialTranscriptions` | `Transcript[]` | ✅ | - | Initial transcriptions |
| `meeting` | `Meeting` | ✅ | - | Meeting object |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkAiTranscriptions } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkAiTranscriptions />;
}
```

### With Properties

```tsx
import { RtkAiTranscriptions } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkAiTranscriptions
      initialTranscriptions={[]}
      meeting={meeting}
    />
  );
}
```
