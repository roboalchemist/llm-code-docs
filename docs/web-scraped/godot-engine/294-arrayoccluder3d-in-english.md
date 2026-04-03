# ArrayOccluder3D in English

# ArrayOccluder3D
Inherits:Occluder3D<Resource<RefCounted<Object
3D polygon shape for use with occlusion culling inOccluderInstance3D.

## Description
ArrayOccluder3Dstores an arbitrary 3D polygon shape that can be used by the engine's occlusion culling system. This is analogous toArrayMesh, but for occluders.
SeeOccluderInstance3D's documentation for instructions on setting up occlusion culling.

## Tutorials
- Occlusion culling
Occlusion culling

## Properties

| PackedInt32Array | indices | PackedInt32Array() |
|---|---|---|
| PackedVector3Array | vertices | PackedVector3Array() |

PackedInt32Array
indices
PackedInt32Array()
PackedVector3Array
vertices
PackedVector3Array()

## Methods

| void | set_arrays(vertices:PackedVector3Array, indices:PackedInt32Array) |

void
set_arrays(vertices:PackedVector3Array, indices:PackedInt32Array)

## Property Descriptions
PackedInt32Arrayindices=PackedInt32Array()🔗
- voidset_indices(value:PackedInt32Array)
voidset_indices(value:PackedInt32Array)
- PackedInt32Arrayget_indices()
PackedInt32Arrayget_indices()
The occluder's index position. Indices determine which points from theverticesarray should be drawn, and in which order.
Note:The occluder is always updated after setting this value. If creating occluders procedurally, consider usingset_arrays()instead to avoid updating the occluder twice when it's created.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedInt32Arrayfor more details.
PackedVector3Arrayvertices=PackedVector3Array()🔗
- voidset_vertices(value:PackedVector3Array)
voidset_vertices(value:PackedVector3Array)
- PackedVector3Arrayget_vertices()
PackedVector3Arrayget_vertices()
The occluder's vertex positions in local 3D coordinates.
Note:The occluder is always updated after setting this value. If creating occluders procedurally, consider usingset_arrays()instead to avoid updating the occluder twice when it's created.
Note:The returned array iscopiedand any changes to it will not update the original property value. SeePackedVector3Arrayfor more details.

## Method Descriptions
voidset_arrays(vertices:PackedVector3Array, indices:PackedInt32Array)🔗
Setsindicesandvertices, while updating the final occluder only once after both values are set.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.