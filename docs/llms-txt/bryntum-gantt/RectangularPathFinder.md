# Source: https://bryntum.com/products/gantt/docs-llm/api/Scheduler/util/RectangularPathFinder.md

# [RectangularPathFinder](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder)

Class which finds rectangular path, i.e. path with 90 degrees turns, between two boxes.

## Configs

Configs are options you supply in a configuration object when creating an instance of this class

[startSide](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-startSide)
Default start connection side: 'left', 'right', 'top', 'bottom'

[startArrowMargin](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-startArrowMargin)
Default start arrow staff size in pixels

[startShift](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-startShift)
Default starting connection point shift from box's arrow pointing side middle point

[endSide](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-endSide)
Default end arrow pointing direction, possible values are: 'left', 'right', 'top', 'bottom'

[endArrowMargin](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-endArrowMargin)
Default end arrow staff size in pixels

[endShift](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-endShift)
Default ending connection point shift from box's arrow pointing side middle point

[verticalMargin](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-verticalMargin)
Start / End box vertical margin, the amount of pixels from top and bottom line of a box where drawing is prohibited

[horizontalMargin](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-horizontalMargin)
Start / End box horizontal margin, the amount of pixels from left and right line of a box where drawing

[otherBoxes](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-otherBoxes)
Other rectangular areas (obstacles) to search path through

[client](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#config-client)
The owning Scheduler. Mandatory so that it can determin RTL state.

## Functions

Functions are methods available for calling on the class

[findPath](https://bryntum.com/docs/gantt/api/Scheduler/util/RectangularPathFinder#function-findPath)
Returns list of horizontal and vertical segments connecting two boxes

   |    | |  |    |       |
 --+----+----+----\*-------\*---
 --+=>Start  +----\*-------\*--
 --+----+----+----\*-------\*--
   |    | |  |    |       |
   |    | |  |    |       |
 --\*----\*-+-------+-------+--
 --\*----\*-+         End <=+--
 --\*----\*-+-------+-------+--
   |    | |  |    |       |

Path goes by lines (-=) and turns at intersections (+), boxes depicted are adjusted by horizontal/vertical margin and arrow margin, original boxes are smaller (path can't go at original box borders). Algorithm finds the shortest path with minimum amount of turns. In short it's mix of "Lee" and "Dijkstra pathfinding" with turns amount taken into account for distance calculation.

The algorithm is not very performant though, it's O(N^2), where N is amount of points in the grid, but since the maximum amount of points in the grid might be up to 34 (not 36 since two box middle points are not permitted) that might be ok for now.
