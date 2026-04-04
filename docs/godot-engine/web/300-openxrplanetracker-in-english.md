# OpenXRPlaneTracker in English

# OpenXRPlaneTracker

Experimental:This class may be changed or removed in future versions.
Inherits:OpenXRSpatialEntityTracker<XRPositionalTracker<XRTracker<RefCounted<Object
Spatial entity tracker for our spatial entity plane tracking extension.

## Description

Spatial entity tracker for our OpenXR spatial entity plane tracking extension. These trackers identify entities in our real space such as walls, floors, tables, etc. and map their location to our virtual space.

## Properties

| Vector2 | bounds_size | Vector2(0,0) |
|---|---|---|
| PlaneAlignment | plane_alignment | 0 |
| String | plane_label | "" |

Vector2
bounds_size
Vector2(0,0)
PlaneAlignment
plane_alignment
String
plane_label

## Methods

| void | clear_mesh_data() |
|---|---|
| Mesh | get_mesh() |
| Transform3D | get_mesh_offset()const |
| Shape3D | get_shape(thickness:float= 0.01) |
| void | set_mesh_data(origin:Transform3D, vertices:PackedVector2Array, indices:PackedInt32Array= PackedInt32Array()) |

void
clear_mesh_data()
Mesh
get_mesh()
Transform3D
get_mesh_offset()const
Shape3D
get_shape(thickness:float= 0.01)
void
set_mesh_data(origin:Transform3D, vertices:PackedVector2Array, indices:PackedInt32Array= PackedInt32Array())

## Signals

mesh_changed()🔗
Emitted when our mesh data has changed the mesh instance and collision needs to be updated.

## Property Descriptions

Vector2bounds_size=Vector2(0,0)🔗

- voidset_bounds_size(value:Vector2)
voidset_bounds_size(value:Vector2)
- Vector2get_bounds_size()
Vector2get_bounds_size()
The bounding size of the plane. This is a 2D size.
PlaneAlignmentplane_alignment=0🔗
- voidset_plane_alignment(value:PlaneAlignment)
voidset_plane_alignment(value:PlaneAlignment)
- PlaneAlignmentget_plane_alignment()
PlaneAlignmentget_plane_alignment()
The main alignment in space of this plane.
Stringplane_label=""🔗
- voidset_plane_label(value:String)
voidset_plane_label(value:String)
- Stringget_plane_label()
Stringget_plane_label()
The semantic label for this plane.

## Method Descriptions

voidclear_mesh_data()🔗
Clears the mesh data for this tracker. You should only call this if you are handling your own discovery logic.
Meshget_mesh()🔗
Gets a mesh created from either the mesh data or from our bounding size for this plane.
Transform3Dget_mesh_offset()const🔗
Gets the transform by which to offset the mesh and collision shape from our pose to display these correctly.
Shape3Dget_shape(thickness:float= 0.01)🔗
Gets a collision shape built either from the mesh data or from our bounding size for this plane.
voidset_mesh_data(origin:Transform3D, vertices:PackedVector2Array, indices:PackedInt32Array= PackedInt32Array())🔗
Sets the mesh data for this plane. You should only call this if you are handling your own discovery logic.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
