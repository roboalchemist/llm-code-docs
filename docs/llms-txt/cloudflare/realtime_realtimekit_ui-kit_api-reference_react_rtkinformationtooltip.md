# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/index.md

---

title: RtkInformationTooltip · Cloudflare Realtime docs
description: API reference for RtkInformationTooltip component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtkinformationtooltip/index.md
---

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `iconPack` | `IconPack1` | ❌ | `defaultIconPack` | Icon pack |

## Usage Examples

### Basic Usage

```tsx
import { RtkInformationTooltip } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkInformationTooltip />;
}
```

### With Properties

```tsx
import { RtkInformationTooltip } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkInformationTooltip
      iconPack={defaultIconPack}
    />
  );
}
```
