# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/index.md

---

title: RtkMarkdownView · Cloudflare Realtime docs
description: API reference for RtkMarkdownView component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkmarkdownview/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `maxLength` | `number` | ✅ | - | max length of text to render as markdown |
| `text` | `string` | ✅ | - | raw text to render as markdown |

## Usage Examples

### Basic Usage

```tsx
import { RtkMarkdownView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkMarkdownView />;
}
```

### With Properties

```tsx
import { RtkMarkdownView } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkMarkdownView
      maxLength={42}
      text="example"
    />
  );
}
```
