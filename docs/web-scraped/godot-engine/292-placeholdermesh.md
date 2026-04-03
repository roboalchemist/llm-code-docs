# PlaceholderMesh

# PlaceholderMesh
Inherits:Mesh<Resource<RefCounted<Object
Placeholder class for a mesh.

## Description
This class is used when loading a project that uses aMeshsubclass in 2 conditions:
- When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
When running the project exported in dedicated server mode, only the texture's dimensions are kept (as they may be relied upon for gameplay purposes or positioning of other elements). This allows reducing the exported PCK's size significantly.
- When this subclass is missing due to using a different engine version or build (e.g. modules disabled).
When this subclass is missing due to using a different engine version or build (e.g. modules disabled).

## Properties

| AABB | aabb | AABB(0,0,0,0,0,0) |

AABB
aabb
AABB(0,0,0,0,0,0)

## Property Descriptions
AABBaabb=AABB(0,0,0,0,0,0)🔗
- voidset_aabb(value:AABB)
voidset_aabb(value:AABB)
- AABBget_aabb()
AABBget_aabb()
The smallestAABBenclosing this mesh in local space.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.