# Source: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/index.md

---

title: RtkTooltip · Cloudflare Realtime docs
description: API reference for RtkTooltip component (React Library)
lastUpdated: 2026-02-10T17:40:43.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/
  md: https://developers.cloudflare.com/realtime/realtimekit/ui-kit/api-reference/react/rtktooltip/index.md
---

Tooltip component which follows RTK Design System.

## Properties

| Property | Type | Required | Default | Description |
| - | - | - | - | - |
| `delay` | `number` | ✅ | - | Delay before showing the tooltip |
| `disabled` | `boolean` | ✅ | - | Disabled |
| `kind` | `TooltipKind` | ✅ | - | Tooltip kind |
| `label` | `string` | ✅ | - | Tooltip label |
| `open` | `boolean` | ✅ | - | Open |
| `placement` | `Placement` | ✅ | - | Placement of menu |
| `size` | `Size` | ✅ | - | Size |
| `variant` | `TooltipVariant` | ✅ | - | Tooltip variant |

## Usage Examples

### Basic Usage

```tsx
import { RtkTooltip } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return <RtkTooltip />;
}
```

### With Properties

```tsx
import { RtkTooltip } from '@cloudflare/realtimekit-react-ui';


function MyComponent() {
  return (
    <RtkTooltip
      delay={42}
      disabled={true}
      kind={tooltipkind}
    />
  );
}
```
