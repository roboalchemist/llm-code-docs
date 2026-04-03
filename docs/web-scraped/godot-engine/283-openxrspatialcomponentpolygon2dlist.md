# OpenXRSpatialComponentPolygon2DList

# OpenXRSpatialComponentPolygon2DList
Experimental:This class may be changed or removed in future versions.
Inherits:OpenXRSpatialComponentData<RefCounted<Object
Object for storing the queries polygon2d result data.

## Description
Object for storing the queries 2D polygon result data when callingOpenXRSpatialEntityExtension.query_snapshot().

## Methods

| Transform3D | get_transform(index:int)const |
|---|---|
| PackedVector2Array | get_vertices(snapshot:RID, index:int)const |

Transform3D
get_transform(index:int)const
PackedVector2Array
get_vertices(snapshot:RID, index:int)const

## Method Descriptions
Transform3Dget_transform(index:int)const🔗
Returns the transform for positioning our polygon for the entity at thisindex.
PackedVector2Arrayget_vertices(snapshot:RID, index:int)const🔗
Returns the polygon vertices for the entity at thisindex.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.