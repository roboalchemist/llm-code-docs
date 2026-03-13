# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/helper/util/InfinityAxis.md

# [InfinityAxis](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityAxis)

This class manages a single axis for the [InfinityScroller](https://bryntum.com/docs/gantt/api/#Core/helper/util/InfinityScroller).

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[owner](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityAxis#config-owner)
The owning `InfinityScroller` for this axis.

[drift](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityAxis#config-drift)
The delta between a logical scroll position and physical scroll position. In other words, adding the drift to a logical scroll position, produces the corresponding physical scroll position.

[pos](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityAxis#config-pos)
The logical scroll position.

[range](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityAxis#config-range)
The logical scroll range as a two element array containing the range's lower bound and upper bound, respectively.

## Functions

Functions are methods available for calling on the class

[toPhysical](https://bryntum.com/docs/gantt/api/Core/helper/util/InfinityAxis#function-toPhysical)
Returns the physical scroll position for the given logical scroll position. Valid physical scroll positions are not negative. This method returns NaN for logical scroll positions that cannot be converted to a valid, physical scroll position.
