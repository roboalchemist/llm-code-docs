# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/index.md

---

title: RtkTranscript · Cloudflare Realtime docs
description: API reference for RtkTranscript component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktranscript/index.md
---

A component which shows a transcript. You need to remove the element after you receive the `rtkTranscriptDismiss` event.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |
| `transcript` | `Transcript & { renderedId?: string }` | ❌ | - | Message |

## Usage Examples

### Basic Usage

```tsx
import { RtkTranscript } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkTranscript />;
}
```

### With Properties

```tsx
import { RtkTranscript } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkTranscript
      t={rtki18n}
      transcript="example"
    />
  );
}
```
