# Source: https://www.daytona.io/docs/en/regions.md

The Daytona SDK can be configured to run in multiple geographic regions. The following regions are currently available:

| Region        | Target |
| ------------- | ---- |
| United States | `us` |
| Europe        | `eu` |

The region is specificed by setting the `target` parameter on initialization:

```python
from daytona import Daytona, DaytonaConfig

# Configure Daytona to use the US region
config = DaytonaConfig(
    target="us"
)

# Initialize the Daytona client with the specified configuration
daytona = Daytona(config)
```
```typescript
import { Daytona } from '@daytonaio/sdk';

// Configure Daytona to use the EU region
const daytona: Daytona = new Daytona({
    target: "eu"
});
```

For more information, see [Configuration](https://www.daytona.io/docs/configuration.md).