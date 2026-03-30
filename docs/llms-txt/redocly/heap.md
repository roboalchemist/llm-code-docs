# Source: https://redocly.com/docs/realm/config/analytics/heap.md

# Heap Analytics

Integrate Heap Analytics into Redocly project.

## Configuration

| Option | Type | Description |
|  --- | --- | --- |
| appId | string | **REQUIRED.** Heap analytics App ID |
| includeInDevelopment | boolean | Set this option to `true` to enable Heap Analytics in development mode and preview builds.
Default is `false`. |


## Example


```yaml
analytics:
  heap:
    includeInDevelopment: true
    aooUd: my-app-id
```