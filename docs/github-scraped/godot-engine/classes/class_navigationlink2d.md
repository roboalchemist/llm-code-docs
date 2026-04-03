:github_url: hide



# NavigationLink2D

**Experimental:** This class may be changed or removed in future versions.

**Inherits:** [Node2D<class_Node2D>] **<** [CanvasItem<class_CanvasItem>] **<** [Node<class_Node>] **<** [Object<class_Object>]

A link between two positions on [NavigationRegion2D<class_NavigationRegion2D>]\ s that agents can be routed through.


## Description

A link between two positions on [NavigationRegion2D<class_NavigationRegion2D>]\ s that agents can be routed through. These positions can be on the same [NavigationRegion2D<class_NavigationRegion2D>] or on two different ones. Links are useful to express navigation methods other than traveling along the surface of the navigation polygon, such as ziplines, teleporters, or gaps that can be jumped across.


## Tutorials

- [../tutorials/navigation/navigation_using_navigationlinks](Using NavigationLinks .md)


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`bidirectional<class_NavigationLink2D_property_bidirectional>`         | ``true``          |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`bool<class_bool>`       | :ref:`enabled<class_NavigationLink2D_property_enabled>`                     | ``true``          |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`end_position<class_NavigationLink2D_property_end_position>`           | ``Vector2(0, 0)`` |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`     | :ref:`enter_cost<class_NavigationLink2D_property_enter_cost>`               | ``0.0``           |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`int<class_int>`         | :ref:`navigation_layers<class_NavigationLink2D_property_navigation_layers>` | ``1``             |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`start_position<class_NavigationLink2D_property_start_position>`       | ``Vector2(0, 0)`` |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
> | :ref:`float<class_float>`     | :ref:`travel_cost<class_NavigationLink2D_property_travel_cost>`             | ``1.0``           |
> +-------------------------------+-----------------------------------------------------------------------------+-------------------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_global_end_position<class_NavigationLink2D_method_get_global_end_position>`\ (\ ) |const|                                                                      |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Vector2<class_Vector2>` | :ref:`get_global_start_position<class_NavigationLink2D_method_get_global_start_position>`\ (\ ) |const|                                                                  |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>`       | :ref:`get_navigation_layer_value<class_NavigationLink2D_method_get_navigation_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`\ ) |const|                          |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_navigation_map<class_NavigationLink2D_method_get_navigation_map>`\ (\ ) |const|                                                                                |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`RID<class_RID>`         | :ref:`get_rid<class_NavigationLink2D_method_get_rid>`\ (\ ) |const|                                                                                                      |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_global_end_position<class_NavigationLink2D_method_set_global_end_position>`\ (\ position\: :ref:`Vector2<class_Vector2>`\ )                                    |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_global_start_position<class_NavigationLink2D_method_set_global_start_position>`\ (\ position\: :ref:`Vector2<class_Vector2>`\ )                                |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_navigation_layer_value<class_NavigationLink2D_method_set_navigation_layer_value>`\ (\ layer_number\: :ref:`int<class_int>`, value\: :ref:`bool<class_bool>`\ ) |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                        | :ref:`set_navigation_map<class_NavigationLink2D_method_set_navigation_map>`\ (\ navigation_map\: :ref:`RID<class_RID>`\ )                                                |
> +-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[bool<class_bool>] **bidirectional** = `true` [🔗<class_NavigationLink2D_property_bidirectional>]


- |void| **set_bidirectional**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_bidirectional**\ (\ )

Whether this link can be traveled in both directions or only from [start_position<class_NavigationLink2D_property_start_position>] to [end_position<class_NavigationLink2D_property_end_position>].


----



[bool<class_bool>] **enabled** = `true` [🔗<class_NavigationLink2D_property_enabled>]


- |void| **set_enabled**\ (\ value\: [bool<class_bool>]\ )
- [bool<class_bool>] **is_enabled**\ (\ )

Whether this link is currently active. If `false`, [NavigationServer2D.map_get_path()<class_NavigationServer2D_method_map_get_path>] will ignore this link.


----



[Vector2<class_Vector2>] **end_position** = `Vector2(0, 0)` [🔗<class_NavigationLink2D_property_end_position>]


- |void| **set_end_position**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_end_position**\ (\ )

Ending position of the link.

This position will search out the nearest polygon in the navigation mesh to attach to.

The distance the link will search is controlled by [NavigationServer2D.map_set_link_connection_radius()<class_NavigationServer2D_method_map_set_link_connection_radius>].


----



[float<class_float>] **enter_cost** = `0.0` [🔗<class_NavigationLink2D_property_enter_cost>]


- |void| **set_enter_cost**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_enter_cost**\ (\ )

When pathfinding enters this link from another regions navigation mesh the [enter_cost<class_NavigationLink2D_property_enter_cost>] value is added to the path distance for determining the shortest path.


----



[int<class_int>] **navigation_layers** = `1` [🔗<class_NavigationLink2D_property_navigation_layers>]


- |void| **set_navigation_layers**\ (\ value\: [int<class_int>]\ )
- [int<class_int>] **get_navigation_layers**\ (\ )

A bitfield determining all navigation layers the link belongs to. These navigation layers will be checked when requesting a path with [NavigationServer2D.map_get_path()<class_NavigationServer2D_method_map_get_path>].


----



[Vector2<class_Vector2>] **start_position** = `Vector2(0, 0)` [🔗<class_NavigationLink2D_property_start_position>]


- |void| **set_start_position**\ (\ value\: [Vector2<class_Vector2>]\ )
- [Vector2<class_Vector2>] **get_start_position**\ (\ )

Starting position of the link.

This position will search out the nearest polygon in the navigation mesh to attach to.

The distance the link will search is controlled by [NavigationServer2D.map_set_link_connection_radius()<class_NavigationServer2D_method_map_set_link_connection_radius>].


----



[float<class_float>] **travel_cost** = `1.0` [🔗<class_NavigationLink2D_property_travel_cost>]


- |void| **set_travel_cost**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_travel_cost**\ (\ )

When pathfinding moves along the link the traveled distance is multiplied with [travel_cost<class_NavigationLink2D_property_travel_cost>] for determining the shortest path.


----


## Method Descriptions



[Vector2<class_Vector2>] **get_global_end_position**\ (\ ) |const| [🔗<class_NavigationLink2D_method_get_global_end_position>]

Returns the [end_position<class_NavigationLink2D_property_end_position>] that is relative to the link as a global position.


----



[Vector2<class_Vector2>] **get_global_start_position**\ (\ ) |const| [🔗<class_NavigationLink2D_method_get_global_start_position>]

Returns the [start_position<class_NavigationLink2D_property_start_position>] that is relative to the link as a global position.


----



[bool<class_bool>] **get_navigation_layer_value**\ (\ layer_number\: [int<class_int>]\ ) |const| [🔗<class_NavigationLink2D_method_get_navigation_layer_value>]

Returns whether or not the specified layer of the [navigation_layers<class_NavigationLink2D_property_navigation_layers>] bitmask is enabled, given a `layer_number` between 1 and 32.


----



[RID<class_RID>] **get_navigation_map**\ (\ ) |const| [🔗<class_NavigationLink2D_method_get_navigation_map>]

Returns the current navigation map [RID<class_RID>] used by this link.


----



[RID<class_RID>] **get_rid**\ (\ ) |const| [🔗<class_NavigationLink2D_method_get_rid>]

Returns the [RID<class_RID>] of this link on the [NavigationServer2D<class_NavigationServer2D>].


----



|void| **set_global_end_position**\ (\ position\: [Vector2<class_Vector2>]\ ) [🔗<class_NavigationLink2D_method_set_global_end_position>]

Sets the [end_position<class_NavigationLink2D_property_end_position>] that is relative to the link from a global `position`.


----



|void| **set_global_start_position**\ (\ position\: [Vector2<class_Vector2>]\ ) [🔗<class_NavigationLink2D_method_set_global_start_position>]

Sets the [start_position<class_NavigationLink2D_property_start_position>] that is relative to the link from a global `position`.


----



|void| **set_navigation_layer_value**\ (\ layer_number\: [int<class_int>], value\: [bool<class_bool>]\ ) [🔗<class_NavigationLink2D_method_set_navigation_layer_value>]

Based on `value`, enables or disables the specified layer in the [navigation_layers<class_NavigationLink2D_property_navigation_layers>] bitmask, given a `layer_number` between 1 and 32.


----



|void| **set_navigation_map**\ (\ navigation_map\: [RID<class_RID>]\ ) [🔗<class_NavigationLink2D_method_set_navigation_map>]

Sets the [RID<class_RID>] of the navigation map this link should use. By default the link will automatically join the [World2D<class_World2D>] default navigation map so this function is only required to override the default map.

