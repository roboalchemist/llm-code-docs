# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/dashboard/refreshengine.md

# RefreshEngine

## cdf.dashboard. RefreshEngine

Class that manages the periodic refresh of components.

**AMD Module**

```
require(["cdf/dashboard/RefreshEngine"], function(RefreshEngine) { /* code goes here */ });
```

## Constructor

| Name                         | Description                                            |
| ---------------------------- | ------------------------------------------------------ |
| new RefreshEngine(dashboard) | Class that manages the periodic refresh of components. |

## Methods

| Name                                                    | Description                                                                                                       |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| dispose()                                               | Clears resources associated with the refresh engine.                                                              |
| fireGlobalRefresh()                                     | Updates all components that do not have a valid refresh period.                                                   |
| fireRefresh()                                           | Pops up due items from the queue, refreshes components and sets the next timeout.                                 |
| getRefreshPeriod(component) : `number`                  | Gets the refresh period for a component.                                                                          |
| processComponent(component) : `boolean`                 | Removes and adds the given component into the refresh queue restarting the timer if it is the first in the queue. |
| processComponents() : `boolean`                         | Clears the queue, adds all the dashboard components into the queue, and restarts the timer.                       |
| registerComponent(component, refreshPeriod) : `boolean` | Sets a components refresh period and clears it from the queue.                                                    |
| setGlobalRefresh(refreshPeriod)                         | Sets the global refresh period.                                                                                   |
| unregisterComponent(component)                          | Removes the component registration from the refresh engine queue.                                                 |

## Constructor Details

| **new RefreshEngine**(dashboard)                                                                                        |               |                                                             |
| ----------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------- |
| <p>Builds a new refresh engine for the provided dashboard.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 18</p> |               |                                                             |
| Name                                                                                                                    | Default Value | Summary                                                     |
| dashboard : `cdf.dashboard.Dashboard`                                                                                   |               | The dashboard instance to be managed by the refresh engine. |

\## Methods Details

| **dispose**()                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------- |
| <p>Clears resources associated with the refresh engine.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 462</p> |

| **fireGlobalRefresh**()                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>Called when a valid <code>globalRefreshPeriod</code> exists. It updates all components that do not have a valid refresh period.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 421</p> |

| **fireRefresh**()                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>Pops up due items from the queue, refreshes components and sets the next timeout.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 393</p> |

| **getRefreshPeriod**(component) : `number`                                                                |                                                                   |                       |
| --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------- |
| <p>Gets the refresh period for a component.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 350</p> |                                                                   |                       |
| Name                                                                                                      | Default Value                                                     | Summary               |
| component : `cdf.components.BaseComponent`                                                                |                                                                   | The target component. |
| Name                                                                                                      | Description                                                       |                       |
| `number`                                                                                                  | The components refresh period value or the value of `NO_REFRESH`. |                       |

| **processComponent**(component) : `boolean`                                                                                                                  |                                                                                          |                           |   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | ------------------------- | - |
| <p>Removes and adds the given component into the refresh queue. If the component is the first in the sorted queue, {cdf.dashboard.RefreshEngine.restartTimer | restartTimer} is executed.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 366</p> |                           |   |
| Name                                                                                                                                                         | Default Value                                                                            | Summary                   |   |
| component : `cdf.components.BaseComponent`                                                                                                                   |                                                                                          | The component to process. |   |
| Name                                                                                                                                                         | Description                                                                              |                           |   |
| `boolean`                                                                                                                                                    | `true` after the component was correctly processed.                                      |                           |   |

| **processComponents**() : `boolean`                                                                                                                          |                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| <p>Clears the queue, adds all the dashboard components into the queue, and restarts the timer.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 380</p> |                                            |
| Name                                                                                                                                                         | Description                                |
| `boolean`                                                                                                                                                    | `true` after the components are processed. |

| **registerComponent**(component, refreshPeriod) : `boolean`                                                                                                                                                                   |                                                     |                                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------ |
| <p>Sets a components refresh period and clears it from the queue. <code>processComponent</code> must be called to activate the refresh timer for the component.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 321</p> |                                                     |                                |
| Name                                                                                                                                                                                                                          | Default Value                                       | Summary                        |
| component : `cdf.components.BaseComponent`                                                                                                                                                                                    |                                                     | The component to register.     |
| refreshPeriod : `number`                                                                                                                                                                                                      |                                                     | The associated refresh period. |
| Name                                                                                                                                                                                                                          | Description                                         |                                |
| `boolean`                                                                                                                                                                                                                     | `true` if registration succeeds, `false` otherwise. |                                |

| **setGlobalRefresh**(refreshPeriod)                                                              |               |                        |
| ------------------------------------------------------------------------------------------------ | ------------- | ---------------------- |
| <p>Sets the global refresh period.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 438</p> |               |                        |
| Name                                                                                             | Default Value | Summary                |
| refreshPeriod : `number`                                                                         |               | Refresh period to set. |

| **unregisterComponent**(component)                                                                                                 |               |                              |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------- | ---------------------------- |
| <p>Removes the component registration from the refresh engine queue.</p><p>\*\*Source:\*\*dashboard/RefreshEngine.js, line 336</p> |               |                              |
| Name                                                                                                                               | Default Value | Summary                      |
| component :                                                                                                                        |               | the component to unregister. |
