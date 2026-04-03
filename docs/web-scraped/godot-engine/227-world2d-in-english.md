# World2D in English

# World2D
Inherits:Resource<RefCounted<Object
A resource that holds all components of a 2D world, such as a canvas and a physics space.

## Description
Class that has everything pertaining to a 2D world: A physics space, a canvas, and a sound space. 2D nodes register their resources into the current 2D world.

## Tutorials
- Ray-casting
Ray-casting

## Properties

| RID | canvas |
|---|---|
| PhysicsDirectSpaceState2D | direct_space_state |
| RID | navigation_map |
| RID | space |

canvas
PhysicsDirectSpaceState2D
direct_space_state
navigation_map
space

## Property Descriptions
RIDcanvas🔗
- RIDget_canvas()
RIDget_canvas()
TheRIDof this world's canvas resource. Used by theRenderingServerfor 2D drawing.
PhysicsDirectSpaceState2Ddirect_space_state🔗
- PhysicsDirectSpaceState2Dget_direct_space_state()
PhysicsDirectSpaceState2Dget_direct_space_state()
Direct access to the world's physics 2D space state. Used for querying current and potential collisions. When using multi-threaded physics, access is limited toNode._physics_process()in the main thread.
RIDnavigation_map🔗
- RIDget_navigation_map()
RIDget_navigation_map()
TheRIDof this world's navigation map. Used by theNavigationServer2D.
RIDspace🔗
- RIDget_space()
RIDget_space()
TheRIDof this world's physics space resource. Used by thePhysicsServer2Dfor 2D physics, treating it as both a space and an area.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.