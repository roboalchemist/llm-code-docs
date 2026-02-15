# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/index.md

---

title: RtkStage · Cloudflare Realtime docs
description: API reference for RtkStage component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkstage/index.md
---

A component used as a stage that commonly houses the `grid` and `sidebar` components.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack` | ❌ | `defaultIconPack` | Icon pack |
| `t` | `RtkI18n` | ❌ | `useLanguage()` | Language |

## Usage Examples

### Basic Usage

```tsx
import { RtkStage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkStage />;
}
```

### With Properties

```tsx
import { RtkStage } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkStage
      iconPack={defaultIconPack}
      t={rtki18n}
    />
  );
}
```
