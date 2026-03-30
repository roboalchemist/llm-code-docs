# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/index.md

---

title: RtkPollForm · Cloudflare Realtime docs
description: API reference for RtkPollForm component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkpollform/index.md
---

A component that lets you create a poll.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkPollForm } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkPollForm />;
}
```

### With Properties

```tsx
import { RtkPollForm } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkPollForm
      iconPack={defaultIconPack}
      t={rtki18n}
    />
  );
}
```
