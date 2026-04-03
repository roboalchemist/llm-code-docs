# OpenXRSpatialComponentPlaneSemanticLabelList

# OpenXRSpatialComponentPlaneSemanticLabelList
Experimental:This class may be changed or removed in future versions.
Inherits:OpenXRSpatialComponentData<RefCounted<Object
Object for storing the queries plane semantic label result data.

## Description
Object for storing the queries plane semantic label result data when callingOpenXRSpatialEntityExtension.query_snapshot().

## Methods

| PlaneSemanticLabel | get_plane_semantic_label(index:int)const |

PlaneSemanticLabel
get_plane_semantic_label(index:int)const

## Enumerations
enumPlaneSemanticLabel:🔗
PlaneSemanticLabelPLANE_SEMANTIC_LABEL_UNCATEGORIZED=1
Uncategorized plane.
PlaneSemanticLabelPLANE_SEMANTIC_LABEL_FLOOR=2
Plane represents a floor.
PlaneSemanticLabelPLANE_SEMANTIC_LABEL_WALL=3
Plane represents a wall.
PlaneSemanticLabelPLANE_SEMANTIC_LABEL_CEILING=4
Plane represents a ceiling.
PlaneSemanticLabelPLANE_SEMANTIC_LABEL_TABLE=5
Plane represents the surface of a table.

## Method Descriptions
PlaneSemanticLabelget_plane_semantic_label(index:int)const🔗
Returns the plane semantic label for the parent entity at thisindex.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.