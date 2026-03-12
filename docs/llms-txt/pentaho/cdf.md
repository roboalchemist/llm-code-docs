# Source: https://docs.pentaho.com/pba-ctools/pentaho-cdf-api/cdf.md

# cdf

## cdf

The cdf namespace.

**Source:**\_doc/namespace.jsdoc, line 14

## Child Namespaces

| Name       | Summary                       |
| ---------- | ----------------------------- |
| components | The cdf.components namespace. |
| dashboard  | The cdf.dashboard namespace.  |
| queries    | The cdf.queries namespace.    |

## Classes

| Name                | Summary                                                                                                                                                                                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Dashboard.Blueprint | Represents a Blueprint dashboard.                                                                                                                                                                               |
| Dashboard.Bootstrap | Represents a Bootstrap dashboard.                                                                                                                                                                               |
| Dashboard.Clean     | Represents a clean (no css engine) dashboard.                                                                                                                                                                   |
| AddIn               | Class that allows creating Static or Scriptable add-ins.                                                                                                                                                        |
| Logger              | Allows logging messages in the console.                                                                                                                                                                         |
| OlapUtils           | OlapUtils is a collection of functions allowing client side CDF to issue MDX queries. This functionality is completely deprecated now and only used by the MdxQueryGroupComponent, which is deprecated as well. |

## Events

| Name | Summary                                      |
| ---- | -------------------------------------------- |
| cdf  | Event triggered along with lifecycle events. |

## Events Details

| **cdf**                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>This event is triggered along with any other dashboard or component main event. Can be used in a more generic way, e.g., to proxy dashboard/component lifecycle events.</p><p><strong>Source:</strong>\_doc/events.jsdoc, line 14</p> |
