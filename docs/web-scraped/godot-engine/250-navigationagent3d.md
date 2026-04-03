# NavigationAgent3D

# NavigationAgent3D
Experimental:This class may be changed or removed in future versions.
Inherits:Node<Object
A 3D agent used to pathfind to a position while avoiding obstacles.

## Description
A 3D agent used to pathfind to a position while avoiding static and dynamic obstacles. The calculation can be used by the parent node to dynamically move it along the path. Requires navigation data to work correctly.
Dynamic obstacles are avoided using RVO collision avoidance. Avoidance is computed before physics, so the pathfinding information can be used safely in the physics step.
Note:After setting thetarget_positionproperty, theget_next_path_position()method must be used once every physics frame to update the internal path logic of the navigation agent. The vector position it returns should be used as the next movement position for the agent's parent node.
Note:Several methods of this class, such asget_next_path_position(), can trigger a new path calculation. Calling these in your callback to an agent's signal, such aswaypoint_reached, can cause infinite recursion. It is recommended to call these methods in the physics step or, alternatively, delay their call until the end of the frame (seeObject.call_deferred()orObject.CONNECT_DEFERRED).

## Tutorials
- Using NavigationAgents
Using NavigationAgents

## Properties

| bool | avoidance_enabled | false |
|---|---|---|
| int | avoidance_layers | 1 |
| int | avoidance_mask | 1 |
| float | avoidance_priority | 1.0 |
| bool | debug_enabled | false |
| Color | debug_path_custom_color | Color(1,1,1,1) |
| float | debug_path_custom_point_size | 4.0 |
| bool | debug_use_custom | false |
| float | height | 1.0 |
| bool | keep_y_velocity | true |
| int | max_neighbors | 10 |
| float | max_speed | 10.0 |
| int | navigation_layers | 1 |
| float | neighbor_distance | 50.0 |
| float | path_desired_distance | 1.0 |
| float | path_height_offset | 0.0 |
| float | path_max_distance | 5.0 |
| BitField[PathMetadataFlags] | path_metadata_flags | 7 |
| PathPostProcessing | path_postprocessing | 0 |
| float | path_return_max_length | 0.0 |
| float | path_return_max_radius | 0.0 |
| float | path_search_max_distance | 0.0 |
| int | path_search_max_polygons | 4096 |
| PathfindingAlgorithm | pathfinding_algorithm | 0 |
| float | radius | 0.5 |
| float | simplify_epsilon | 0.0 |
| bool | simplify_path | false |
| float | target_desired_distance | 1.0 |
| Vector3 | target_position | Vector3(0,0,0) |
| float | time_horizon_agents | 1.0 |
| float | time_horizon_obstacles | 0.0 |
| bool | use_3d_avoidance | false |
| Vector3 | velocity | Vector3(0,0,0) |

bool
avoidance_enabled
false
avoidance_layers
avoidance_mask
float
avoidance_priority
bool
debug_enabled
false
Color
debug_path_custom_color
Color(1,1,1,1)
float
debug_path_custom_point_size
bool
debug_use_custom
false
float
height
bool
keep_y_velocity
true
max_neighbors
float
max_speed
10.0
navigation_layers
float
neighbor_distance
50.0
float
path_desired_distance
float
path_height_offset
float
path_max_distance
BitField[PathMetadataFlags]
path_metadata_flags
PathPostProcessing
path_postprocessing
float
path_return_max_length
float
path_return_max_radius
float
path_search_max_distance
path_search_max_polygons
4096
PathfindingAlgorithm
pathfinding_algorithm
float
radius
float
simplify_epsilon
bool
simplify_path
false
float
target_desired_distance
Vector3
target_position
Vector3(0,0,0)
float
time_horizon_agents
float
time_horizon_obstacles
bool
use_3d_avoidance
false
Vector3
velocity
Vector3(0,0,0)

## Methods

| float | distance_to_target()const |
|---|---|
| bool | get_avoidance_layer_value(layer_number:int)const |
| bool | get_avoidance_mask_value(mask_number:int)const |
| PackedVector3Array | get_current_navigation_path()const |
| int | get_current_navigation_path_index()const |
| NavigationPathQueryResult3D | get_current_navigation_result()const |
| Vector3 | get_final_position() |
| bool | get_navigation_layer_value(layer_number:int)const |
| RID | get_navigation_map()const |
| Vector3 | get_next_path_position() |
| float | get_path_length()const |
| RID | get_rid()const |
| bool | is_navigation_finished() |
| bool | is_target_reachable() |
| bool | is_target_reached()const |
| void | set_avoidance_layer_value(layer_number:int, value:bool) |
| void | set_avoidance_mask_value(mask_number:int, value:bool) |
| void | set_navigation_layer_value(layer_number:int, value:bool) |
| void | set_navigation_map(navigation_map:RID) |
| void | set_velocity_forced(velocity:Vector3) |

float
distance_to_target()const
bool
get_avoidance_layer_value(layer_number:int)const
bool
get_avoidance_mask_value(mask_number:int)const
PackedVector3Array
get_current_navigation_path()const
get_current_navigation_path_index()const
NavigationPathQueryResult3D
get_current_navigation_result()const
Vector3
get_final_position()
bool
get_navigation_layer_value(layer_number:int)const
get_navigation_map()const
Vector3
get_next_path_position()
float
get_path_length()const
get_rid()const
bool
is_navigation_finished()
bool
is_target_reachable()
bool
is_target_reached()const
void
set_avoidance_layer_value(layer_number:int, value:bool)
void
set_avoidance_mask_value(mask_number:int, value:bool)
void
set_navigation_layer_value(layer_number:int, value:bool)
void
set_navigation_map(navigation_map:RID)
void
set_velocity_forced(velocity:Vector3)

## Signals
link_reached(details:Dictionary)🔗
Signals that the agent reached a navigation link. Emitted when the agent moves withinpath_desired_distanceof the next position of the path when that position is a navigation link.
The details dictionary may contain the following keys depending on the value ofpath_metadata_flags:
- position: The start position of the link that was reached.
position: The start position of the link that was reached.
- type: AlwaysNavigationPathQueryResult3D.PATH_SEGMENT_TYPE_LINK.
type: AlwaysNavigationPathQueryResult3D.PATH_SEGMENT_TYPE_LINK.
- rid: TheRIDof the link.
rid: TheRIDof the link.
- owner: The object which manages the link (usuallyNavigationLink3D).
owner: The object which manages the link (usuallyNavigationLink3D).
- link_entry_position: Ifowneris available and the owner is aNavigationLink3D, it will contain the global position of the link's point the agent is entering.
link_entry_position: Ifowneris available and the owner is aNavigationLink3D, it will contain the global position of the link's point the agent is entering.
- link_exit_position: Ifowneris available and the owner is aNavigationLink3D, it will contain the global position of the link's point which the agent is exiting.
link_exit_position: Ifowneris available and the owner is aNavigationLink3D, it will contain the global position of the link's point which the agent is exiting.
navigation_finished()🔗
Signals that the agent's navigation has finished. If the target is reachable, navigation ends when the target is reached. If the target is unreachable, navigation ends when the last waypoint of the path is reached. This signal is emitted only once per loaded path.
This signal will be emitted just aftertarget_reachedwhen the target is reachable.
path_changed()🔗
Emitted when the agent had to update the loaded path:
- because path was previously empty.
because path was previously empty.
- because navigation map has changed.
because navigation map has changed.
- because agent pushed further away from the current path segment than thepath_max_distance.
because agent pushed further away from the current path segment than thepath_max_distance.
target_reached()🔗
Signals that the agent reached the target, i.e. the agent moved withintarget_desired_distanceof thetarget_position. This signal is emitted only once per loaded path.
This signal will be emitted just beforenavigation_finishedwhen the target is reachable.
It may not always be possible to reach the target but it should always be possible to reach the final position. Seeget_final_position().
velocity_computed(safe_velocity:Vector3)🔗
Notifies when the collision avoidance velocity is calculated. Emitted every update as long asavoidance_enabledistrueand the agent has a navigation map.
waypoint_reached(details:Dictionary)🔗
Signals that the agent reached a waypoint. Emitted when the agent moves withinpath_desired_distanceof the next position of the path.
The details dictionary may contain the following keys depending on the value ofpath_metadata_flags:
- position: The position of the waypoint that was reached.
position: The position of the waypoint that was reached.
- type: The type of navigation primitive (region or link) that contains this waypoint.
type: The type of navigation primitive (region or link) that contains this waypoint.
- rid: TheRIDof the containing navigation primitive (region or link).
rid: TheRIDof the containing navigation primitive (region or link).
- owner: The object which manages the containing navigation primitive (region or link).
owner: The object which manages the containing navigation primitive (region or link).

## Property Descriptions
boolavoidance_enabled=false🔗
- voidset_avoidance_enabled(value:bool)
voidset_avoidance_enabled(value:bool)
- boolget_avoidance_enabled()
boolget_avoidance_enabled()
Iftruethe agent is registered for an RVO avoidance callback on theNavigationServer3D. Whenvelocityis set and the processing is completed asafe_velocityVector3 is received with a signal connection tovelocity_computed. Avoidance processing with many registered agents has a significant performance cost and should only be enabled on agents that currently require it.
intavoidance_layers=1🔗
- voidset_avoidance_layers(value:int)
voidset_avoidance_layers(value:int)
- intget_avoidance_layers()
intget_avoidance_layers()
A bitfield determining the avoidance layers for this NavigationAgent. Other agents with a matching bit on theavoidance_maskwill avoid this agent.
intavoidance_mask=1🔗
- voidset_avoidance_mask(value:int)
voidset_avoidance_mask(value:int)
- intget_avoidance_mask()
intget_avoidance_mask()
A bitfield determining what other avoidance agents and obstacles this NavigationAgent will avoid when a bit matches at least one of theiravoidance_layers.
floatavoidance_priority=1.0🔗
- voidset_avoidance_priority(value:float)
voidset_avoidance_priority(value:float)
- floatget_avoidance_priority()
floatget_avoidance_priority()
The agent does not adjust the velocity for other agents that would match theavoidance_maskbut have a loweravoidance_priority. This in turn makes the other agents with lower priority adjust their velocities even more to avoid collision with this agent.
booldebug_enabled=false🔗
- voidset_debug_enabled(value:bool)
voidset_debug_enabled(value:bool)
- boolget_debug_enabled()
boolget_debug_enabled()
Iftrueshows debug visuals for this agent.
Colordebug_path_custom_color=Color(1,1,1,1)🔗
- voidset_debug_path_custom_color(value:Color)
voidset_debug_path_custom_color(value:Color)
- Colorget_debug_path_custom_color()
Colorget_debug_path_custom_color()
Ifdebug_use_customistrueuses this color for this agent instead of global color.
floatdebug_path_custom_point_size=4.0🔗
- voidset_debug_path_custom_point_size(value:float)
voidset_debug_path_custom_point_size(value:float)
- floatget_debug_path_custom_point_size()
floatget_debug_path_custom_point_size()
Ifdebug_use_customistrueuses this rasterized point size for rendering path points for this agent instead of global point size.
booldebug_use_custom=false🔗
- voidset_debug_use_custom(value:bool)
voidset_debug_use_custom(value:bool)
- boolget_debug_use_custom()
boolget_debug_use_custom()
Iftrueuses the defineddebug_path_custom_colorfor this agent instead of global color.
floatheight=1.0🔗
- voidset_height(value:float)
voidset_height(value:float)
- floatget_height()
floatget_height()
The height of the avoidance agent. Agents will ignore other agents or obstacles that are above or below their current position + height in 2D avoidance. Does nothing in 3D avoidance which uses radius spheres alone.
boolkeep_y_velocity=true🔗
- voidset_keep_y_velocity(value:bool)
voidset_keep_y_velocity(value:bool)
- boolget_keep_y_velocity()
boolget_keep_y_velocity()
Iftrue, and the agent uses 2D avoidance, it will remember the set y-axis velocity and reapply it after the avoidance step. While 2D avoidance has no y-axis and simulates on a flat plane this setting can help to soften the most obvious clipping on uneven 3D geometry.
intmax_neighbors=10🔗
- voidset_max_neighbors(value:int)
voidset_max_neighbors(value:int)
- intget_max_neighbors()
intget_max_neighbors()
The maximum number of neighbors for the agent to consider.
floatmax_speed=10.0🔗
- voidset_max_speed(value:float)
voidset_max_speed(value:float)
- floatget_max_speed()
floatget_max_speed()
The maximum speed that an agent can move.
intnavigation_layers=1🔗
- voidset_navigation_layers(value:int)
voidset_navigation_layers(value:int)
- intget_navigation_layers()
intget_navigation_layers()
A bitfield determining which navigation layers of navigation regions this agent will use to calculate a path. Changing it during runtime will clear the current navigation path and generate a new one, according to the new navigation layers.
floatneighbor_distance=50.0🔗
- voidset_neighbor_distance(value:float)
voidset_neighbor_distance(value:float)
- floatget_neighbor_distance()
floatget_neighbor_distance()
The distance to search for other agents.
floatpath_desired_distance=1.0🔗
- voidset_path_desired_distance(value:float)
voidset_path_desired_distance(value:float)
- floatget_path_desired_distance()
floatget_path_desired_distance()
The distance threshold before a path point is considered to be reached. This allows agents to not have to hit a path point on the path exactly, but only to reach its general area. If this value is set too high, the NavigationAgent will skip points on the path, which can lead to it leaving the navigation mesh. If this value is set too low, the NavigationAgent will be stuck in a repath loop because it will constantly overshoot the distance to the next point on each physics frame update.
floatpath_height_offset=0.0🔗
- voidset_path_height_offset(value:float)
voidset_path_height_offset(value:float)
- floatget_path_height_offset()
floatget_path_height_offset()
The height offset is subtracted from the y-axis value of any vector path position for this NavigationAgent. The NavigationAgent height offset does not change or influence the navigation mesh or pathfinding query result. Additional navigation maps that use regions with navigation meshes that the developer baked with appropriate agent radius or height values are required to support different-sized agents.
floatpath_max_distance=5.0🔗
- voidset_path_max_distance(value:float)
voidset_path_max_distance(value:float)
- floatget_path_max_distance()
floatget_path_max_distance()
The maximum distance the agent is allowed away from the ideal path to the final position. This can happen due to trying to avoid collisions. When the maximum distance is exceeded, it recalculates the ideal path.
BitField[PathMetadataFlags]path_metadata_flags=7🔗
- voidset_path_metadata_flags(value:BitField[PathMetadataFlags])
voidset_path_metadata_flags(value:BitField[PathMetadataFlags])
- BitField[PathMetadataFlags]get_path_metadata_flags()
BitField[PathMetadataFlags]get_path_metadata_flags()
Additional information to return with the navigation path.
PathPostProcessingpath_postprocessing=0🔗
- voidset_path_postprocessing(value:PathPostProcessing)
voidset_path_postprocessing(value:PathPostProcessing)
- PathPostProcessingget_path_postprocessing()
PathPostProcessingget_path_postprocessing()
The path postprocessing applied to the raw path corridor found by thepathfinding_algorithm.
floatpath_return_max_length=0.0🔗
- voidset_path_return_max_length(value:float)
voidset_path_return_max_length(value:float)
- floatget_path_return_max_length()
floatget_path_return_max_length()
The maximum allowed length of the returned path in world units. A path will be clipped when going over this length.
floatpath_return_max_radius=0.0🔗
- voidset_path_return_max_radius(value:float)
voidset_path_return_max_radius(value:float)
- floatget_path_return_max_radius()
floatget_path_return_max_radius()
The maximum allowed radius in world units that the returned path can be from the path start. The path will be clipped when going over this radius. Compared topath_return_max_length, this allows the agent to go that much further, if they need to walk around a corner.
Note:This will perform a sphere clip considering only the actual navigation mesh path points with the first path position being the sphere's center.
floatpath_search_max_distance=0.0🔗
- voidset_path_search_max_distance(value:float)
voidset_path_search_max_distance(value:float)
- floatget_path_search_max_distance()
floatget_path_search_max_distance()
The maximum distance a searched polygon can be away from the start polygon before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of0or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.
intpath_search_max_polygons=4096🔗
- voidset_path_search_max_polygons(value:int)
voidset_path_search_max_polygons(value:int)
- intget_path_search_max_polygons()
intget_path_search_max_polygons()
The maximum number of polygons that are searched before the pathfinding cancels the search for a path to the (possibly unreachable or very far away) target position polygon. In this case the pathfinding resets and builds a path from the start polygon to the polygon that was found closest to the target position so far. A value of0or below counts as unlimited. In case of unlimited the pathfinding will search all polygons connected with the start polygon until either the target position polygon is found or all available polygon search options are exhausted.
PathfindingAlgorithmpathfinding_algorithm=0🔗
- voidset_pathfinding_algorithm(value:PathfindingAlgorithm)
voidset_pathfinding_algorithm(value:PathfindingAlgorithm)
- PathfindingAlgorithmget_pathfinding_algorithm()
PathfindingAlgorithmget_pathfinding_algorithm()
The pathfinding algorithm used in the path query.
floatradius=0.5🔗
- voidset_radius(value:float)
voidset_radius(value:float)
- floatget_radius()
floatget_radius()
The radius of the avoidance agent. This is the "body" of the avoidance agent and not the avoidance maneuver starting radius (which is controlled byneighbor_distance).
Does not affect normal pathfinding. To change an actor's pathfinding radius bakeNavigationMeshresources with a differentNavigationMesh.agent_radiusproperty and use different navigation maps for each actor size.
floatsimplify_epsilon=0.0🔗
- voidset_simplify_epsilon(value:float)
voidset_simplify_epsilon(value:float)
- floatget_simplify_epsilon()
floatget_simplify_epsilon()
The path simplification amount in worlds units.
boolsimplify_path=false🔗
- voidset_simplify_path(value:bool)
voidset_simplify_path(value:bool)
- boolget_simplify_path()
boolget_simplify_path()
Iftruea simplified version of the path will be returned with less critical path points removed. The simplification amount is controlled bysimplify_epsilon. The simplification uses a variant of Ramer-Douglas-Peucker algorithm for curve point decimation.
Path simplification can be helpful to mitigate various path following issues that can arise with certain agent types and script behaviors. E.g. "steering" agents or avoidance in "open fields".
floattarget_desired_distance=1.0🔗
- voidset_target_desired_distance(value:float)
voidset_target_desired_distance(value:float)
- floatget_target_desired_distance()
floatget_target_desired_distance()
The distance threshold before the target is considered to be reached. On reaching the target,target_reachedis emitted and navigation ends (seeis_navigation_finished()andnavigation_finished).
You can make navigation end early by setting this property to a value greater thanpath_desired_distance(navigation will end before reaching the last waypoint).
You can also make navigation end closer to the target than each individual path position by setting this property to a value lower thanpath_desired_distance(navigation won't immediately end when reaching the last waypoint). However, if the value set is too low, the agent will be stuck in a repath loop because it will constantly overshoot the distance to the target on each physics frame update.
Vector3target_position=Vector3(0,0,0)🔗
- voidset_target_position(value:Vector3)
voidset_target_position(value:Vector3)
- Vector3get_target_position()
Vector3get_target_position()
If set, a new navigation path from the current agent position to thetarget_positionis requested from the NavigationServer.
floattime_horizon_agents=1.0🔗
- voidset_time_horizon_agents(value:float)
voidset_time_horizon_agents(value:float)
- floatget_time_horizon_agents()
floatget_time_horizon_agents()
The minimal amount of time for which this agent's velocities, that are computed with the collision avoidance algorithm, are safe with respect to other agents. The larger the number, the sooner the agent will respond to other agents, but less freedom in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.
floattime_horizon_obstacles=0.0🔗
- voidset_time_horizon_obstacles(value:float)
voidset_time_horizon_obstacles(value:float)
- floatget_time_horizon_obstacles()
floatget_time_horizon_obstacles()
The minimal amount of time for which this agent's velocities, that are computed with the collision avoidance algorithm, are safe with respect to static avoidance obstacles. The larger the number, the sooner the agent will respond to static avoidance obstacles, but less freedom in choosing its velocities. A too high value will slow down agents movement considerably. Must be positive.
booluse_3d_avoidance=false🔗
- voidset_use_3d_avoidance(value:bool)
voidset_use_3d_avoidance(value:bool)
- boolget_use_3d_avoidance()
boolget_use_3d_avoidance()
Iftrue, the agent calculates avoidance velocities in 3D omnidirectionally, e.g. for games that take place in air, underwater or space. Agents using 3D avoidance only avoid other agents using 3D avoidance, and react to radius-based avoidance obstacles. They ignore any vertex-based obstacles.
Iffalse, the agent calculates avoidance velocities in 2D along the x and z-axes, ignoring the y-axis. Agents using 2D avoidance only avoid other agents using 2D avoidance, and react to radius-based avoidance obstacles or vertex-based avoidance obstacles. Other agents using 2D avoidance that are below or above their current position includingheightare ignored.
Vector3velocity=Vector3(0,0,0)🔗
- voidset_velocity(value:Vector3)
voidset_velocity(value:Vector3)
- Vector3get_velocity()
Vector3get_velocity()
Sets the new wanted velocity for the agent. The avoidance simulation will try to fulfill this velocity if possible but will modify it to avoid collision with other agents and obstacles. When an agent is teleported to a new position, useset_velocity_forced()as well to reset the internal simulation velocity.

## Method Descriptions
floatdistance_to_target()const🔗
Returns the distance to the target position, using the agent's global position. The user must settarget_positionin order for this to be accurate.
boolget_avoidance_layer_value(layer_number:int)const🔗
Returns whether or not the specified layer of theavoidance_layersbitmask is enabled, given alayer_numberbetween 1 and 32.
boolget_avoidance_mask_value(mask_number:int)const🔗
Returns whether or not the specified mask of theavoidance_maskbitmask is enabled, given amask_numberbetween 1 and 32.
PackedVector3Arrayget_current_navigation_path()const🔗
Returns this agent's current path from start to finish in global coordinates. The path only updates when the target position is changed or the agent requires a repath. The path array is not intended to be used in direct path movement as the agent has its own internal path logic that would get corrupted by changing the path array manually. Use the intendedget_next_path_position()once every physics frame to receive the next path point for the agents movement as this function also updates the internal path logic.
intget_current_navigation_path_index()const🔗
Returns which index the agent is currently on in the navigation path'sPackedVector3Array.
NavigationPathQueryResult3Dget_current_navigation_result()const🔗
Returns the path query result for the path the agent is currently following.
Vector3get_final_position()🔗
Returns the reachable final position of the current navigation path in global coordinates. This position can change if the agent needs to update the navigation path which makes the agent emit thepath_changedsignal.
boolget_navigation_layer_value(layer_number:int)const🔗
Returns whether or not the specified layer of thenavigation_layersbitmask is enabled, given alayer_numberbetween 1 and 32.
RIDget_navigation_map()const🔗
Returns theRIDof the navigation map for this NavigationAgent node. This function returns always the map set on the NavigationAgent node and not the map of the abstract agent on the NavigationServer. If the agent map is changed directly with the NavigationServer API the NavigationAgent node will not be aware of the map change. Useset_navigation_map()to change the navigation map for the NavigationAgent and also update the agent on the NavigationServer.
Vector3get_next_path_position()🔗
Returns the next position in global coordinates that can be moved to, making sure that there are no static objects in the way. If the agent does not have a navigation path, it will return the position of the agent's parent. The use of this function once every physics frame is required to update the internal path logic of the NavigationAgent.
floatget_path_length()const🔗
Returns the length of the currently calculated path. The returned value is0.0, if the path is still calculating or no calculation has been requested yet.
RIDget_rid()const🔗
Returns theRIDof this agent on theNavigationServer3D.
boolis_navigation_finished()🔗
Returnstrueif the agent's navigation has finished. If the target is reachable, navigation ends when the target is reached. If the target is unreachable, navigation ends when the last waypoint of the path is reached.
Note:Whiletrueprefer to stop calling update functions likeget_next_path_position(). This avoids jittering the standing agent due to calling repeated path updates.
boolis_target_reachable()🔗
Returnstrueifget_final_position()is withintarget_desired_distanceof thetarget_position.
boolis_target_reached()const🔗
Returnstrueif the agent reached the target, i.e. the agent moved withintarget_desired_distanceof thetarget_position. It may not always be possible to reach the target but it should always be possible to reach the final position. Seeget_final_position().
voidset_avoidance_layer_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in theavoidance_layersbitmask, given alayer_numberbetween 1 and 32.
voidset_avoidance_mask_value(mask_number:int, value:bool)🔗
Based onvalue, enables or disables the specified mask in theavoidance_maskbitmask, given amask_numberbetween 1 and 32.
voidset_navigation_layer_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thenavigation_layersbitmask, given alayer_numberbetween 1 and 32.
voidset_navigation_map(navigation_map:RID)🔗
Sets theRIDof the navigation map this NavigationAgent node should use and also updates theagenton the NavigationServer.
voidset_velocity_forced(velocity:Vector3)🔗
Replaces the internal velocity in the collision avoidance simulation withvelocity. When an agent is teleported to a new position this function should be used in the same frame. If called frequently this function can get agents stuck.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.