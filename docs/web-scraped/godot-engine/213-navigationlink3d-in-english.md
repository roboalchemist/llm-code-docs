# NavigationLink3D in English

# NavigationLink3D
Experimental:This class may be changed or removed in future versions.
Inherits:Node3D<Node<Object
A link between two positions onNavigationRegion3Ds that agents can be routed through.

## Description
A link between two positions onNavigationRegion3Ds that agents can be routed through. These positions can be on the sameNavigationRegion3Dor on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation mesh, such as ziplines, teleporters, or gaps that can be jumped across.

## Tutorials
- Using NavigationLinks
Using NavigationLinks

## Properties

| bool | bidirectional | true |
|---|---|---|
| bool | enabled | true |
| Vector3 | end_position | Vector3(0,0,0) |
| float | enter_cost | 0.0 |
| int | navigation_layers | 1 |
| Vector3 | start_position | Vector3(0,0,0) |
| float | travel_cost | 1.0 |

bool
bidirectional
true
bool
enabled
true
Vector3
end_position
Vector3(0,0,0)
float
enter_cost
navigation_layers
Vector3
start_position
Vector3(0,0,0)
float
travel_cost

## Methods

| Vector3 | get_global_end_position()const |
|---|---|
| Vector3 | get_global_start_position()const |
| bool | get_navigation_layer_value(layer_number:int)const |
| RID | get_navigation_map()const |
| RID | get_rid()const |
| void | set_global_end_position(position:Vector3) |
| void | set_global_start_position(position:Vector3) |
| void | set_navigation_layer_value(layer_number:int, value:bool) |
| void | set_navigation_map(navigation_map:RID) |

Vector3
get_global_end_position()const
Vector3
get_global_start_position()const
bool
get_navigation_layer_value(layer_number:int)const
get_navigation_map()const
get_rid()const
void
set_global_end_position(position:Vector3)
void
set_global_start_position(position:Vector3)
void
set_navigation_layer_value(layer_number:int, value:bool)
void
set_navigation_map(navigation_map:RID)

## Property Descriptions
boolbidirectional=true🔗
- voidset_bidirectional(value:bool)
voidset_bidirectional(value:bool)
- boolis_bidirectional()
boolis_bidirectional()
Whether this link can be traveled in both directions or only fromstart_positiontoend_position.
boolenabled=true🔗
- voidset_enabled(value:bool)
voidset_enabled(value:bool)
- boolis_enabled()
boolis_enabled()
Whether this link is currently active. Iffalse,NavigationServer3D.map_get_path()will ignore this link.
Vector3end_position=Vector3(0,0,0)🔗
- voidset_end_position(value:Vector3)
voidset_end_position(value:Vector3)
- Vector3get_end_position()
Vector3get_end_position()
Ending position of the link.
This position will search out the nearest polygon in the navigation mesh to attach to.
The distance the link will search is controlled byNavigationServer3D.map_set_link_connection_radius().
floatenter_cost=0.0🔗
- voidset_enter_cost(value:float)
voidset_enter_cost(value:float)
- floatget_enter_cost()
floatget_enter_cost()
When pathfinding enters this link from another regions navigation mesh theenter_costvalue is added to the path distance for determining the shortest path.
intnavigation_layers=1🔗
- voidset_navigation_layers(value:int)
voidset_navigation_layers(value:int)
- intget_navigation_layers()
intget_navigation_layers()
A bitfield determining all navigation layers the link belongs to. These navigation layers will be checked when requesting a path withNavigationServer3D.map_get_path().
Vector3start_position=Vector3(0,0,0)🔗
- voidset_start_position(value:Vector3)
voidset_start_position(value:Vector3)
- Vector3get_start_position()
Vector3get_start_position()
Starting position of the link.
This position will search out the nearest polygon in the navigation mesh to attach to.
The distance the link will search is controlled byNavigationServer3D.map_set_link_connection_radius().
floattravel_cost=1.0🔗
- voidset_travel_cost(value:float)
voidset_travel_cost(value:float)
- floatget_travel_cost()
floatget_travel_cost()
When pathfinding moves along the link the traveled distance is multiplied withtravel_costfor determining the shortest path.

## Method Descriptions
Vector3get_global_end_position()const🔗
Returns theend_positionthat is relative to the link as a global position.
Vector3get_global_start_position()const🔗
Returns thestart_positionthat is relative to the link as a global position.
boolget_navigation_layer_value(layer_number:int)const🔗
Returns whether or not the specified layer of thenavigation_layersbitmask is enabled, given alayer_numberbetween 1 and 32.
RIDget_navigation_map()const🔗
Returns the current navigation mapRIDused by this link.
RIDget_rid()const🔗
Returns theRIDof this link on theNavigationServer3D.
voidset_global_end_position(position:Vector3)🔗
Sets theend_positionthat is relative to the link from a globalposition.
voidset_global_start_position(position:Vector3)🔗
Sets thestart_positionthat is relative to the link from a globalposition.
voidset_navigation_layer_value(layer_number:int, value:bool)🔗
Based onvalue, enables or disables the specified layer in thenavigation_layersbitmask, given alayer_numberbetween 1 and 32.
voidset_navigation_map(navigation_map:RID)🔗
Sets theRIDof the navigation map this link should use. By default the link will automatically join theWorld3Ddefault navigation map so this function is only required to override the default map.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.