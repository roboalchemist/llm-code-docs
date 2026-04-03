# MeshInstance3D in English

# MeshInstance3D

Inherits:GeometryInstance3D<VisualInstance3D<Node3D<Node<Object
Inherited By:SoftBody3D
Node that instances meshes into a scenario.

## Description

MeshInstance3D is a node that takes aMeshresource and adds it to the current scenario by creating an instance of it. This is the class most often used to render 3D geometry and can be used to instance a singleMeshin many places. This allows reusing geometry, which can save on resources. When aMeshhas to be instantiated more than thousands of times at close proximity, consider using aMultiMeshin aMultiMeshInstance3Dinstead.

## Tutorials

- 3D Material Testers Demo
3D Material Testers Demo
- 3D Kinematic Character Demo
3D Kinematic Character Demo
- 3D Platformer Demo
3D Platformer Demo
- Third Person Shooter (TPS) Demo
Third Person Shooter (TPS) Demo

## Properties

| Mesh | mesh |  |
|---|---|---|
| NodePath | skeleton | NodePath("") |
| Skin | skin |  |

Mesh
mesh
NodePath
skeleton
NodePath("")
Skin
skin

## Methods

| ArrayMesh | bake_mesh_from_current_blend_shape_mix(existing:ArrayMesh= null) |
|---|---|
| ArrayMesh | bake_mesh_from_current_skeleton_pose(existing:ArrayMesh= null) |
| void | create_convex_collision(clean:bool= true, simplify:bool= false) |
| void | create_debug_tangents() |
| void | create_multiple_convex_collisions(settings:MeshConvexDecompositionSettings= null) |
| void | create_trimesh_collision() |
| int | find_blend_shape_by_name(name:StringName) |
| Material | get_active_material(surface:int)const |
| int | get_blend_shape_count()const |
| float | get_blend_shape_value(blend_shape_idx:int)const |
| SkinReference | get_skin_reference()const |
| Material | get_surface_override_material(surface:int)const |
| int | get_surface_override_material_count()const |
| void | set_blend_shape_value(blend_shape_idx:int, value:float) |
| void | set_surface_override_material(surface:int, material:Material) |

ArrayMesh
bake_mesh_from_current_blend_shape_mix(existing:ArrayMesh= null)
ArrayMesh
bake_mesh_from_current_skeleton_pose(existing:ArrayMesh= null)
void
create_convex_collision(clean:bool= true, simplify:bool= false)
void
create_debug_tangents()
void
create_multiple_convex_collisions(settings:MeshConvexDecompositionSettings= null)
void
create_trimesh_collision()
find_blend_shape_by_name(name:StringName)
Material
get_active_material(surface:int)const
get_blend_shape_count()const
float
get_blend_shape_value(blend_shape_idx:int)const
SkinReference
get_skin_reference()const
Material
get_surface_override_material(surface:int)const
get_surface_override_material_count()const
void
set_blend_shape_value(blend_shape_idx:int, value:float)
void
set_surface_override_material(surface:int, material:Material)

## Property Descriptions

Meshmesh🔗

- voidset_mesh(value:Mesh)
voidset_mesh(value:Mesh)
- Meshget_mesh()
Meshget_mesh()
TheMeshresource for the instance.
NodePathskeleton=NodePath("")🔗
- voidset_skeleton_path(value:NodePath)
voidset_skeleton_path(value:NodePath)
- NodePathget_skeleton_path()
NodePathget_skeleton_path()
NodePathto theSkeleton3Dassociated with the instance.
Note:The default value of this property has changed in Godot 4.6. EnableProjectSettings.animation/compatibility/default_parent_skeleton_in_mesh_instance_3dif the old behavior is needed for compatibility.
Skinskin🔗
- voidset_skin(value:Skin)
voidset_skin(value:Skin)
- Skinget_skin()
Skinget_skin()
TheSkinto be used by this instance.

## Method Descriptions

ArrayMeshbake_mesh_from_current_blend_shape_mix(existing:ArrayMesh= null)🔗
Takes a snapshot from the currentArrayMeshwith all blend shapes applied according to their current weights and bakes it to the providedexistingmesh. If noexistingmesh is provided a newArrayMeshis created, baked and returned. Mesh surface materials are not copied.
Performance:Meshdata needs to be received from the GPU, stalling theRenderingServerin the process.
ArrayMeshbake_mesh_from_current_skeleton_pose(existing:ArrayMesh= null)🔗
Takes a snapshot of the current animated skeleton pose of the skinned mesh and bakes it to the providedexistingmesh. If noexistingmesh is provided a newArrayMeshis created, baked, and returned. Requires a skeleton with a registered skin to work. Blendshapes are ignored. Mesh surface materials are not copied.
Performance:Meshdata needs to be retrieved from the GPU, stalling theRenderingServerin the process.
voidcreate_convex_collision(clean:bool= true, simplify:bool= false)🔗
This helper creates aStaticBody3Dchild node with aConvexPolygonShape3Dcollision shape calculated from the mesh geometry. It's mainly used for testing.
Ifcleanistrue(default), duplicate and interior vertices are removed automatically. You can set it tofalseto make the process faster if not needed.
Ifsimplifyistrue, the geometry can be further simplified to reduce the number of vertices. Disabled by default.
voidcreate_debug_tangents()🔗
This helper creates aMeshInstance3Dchild node with gizmos at every vertex calculated from the mesh geometry. It's mainly used for testing.
voidcreate_multiple_convex_collisions(settings:MeshConvexDecompositionSettings= null)🔗
This helper creates aStaticBody3Dchild node with multipleConvexPolygonShape3Dcollision shapes calculated from the mesh geometry via convex decomposition. The convex decomposition operation can be controlled with parameters from the optionalsettings.
voidcreate_trimesh_collision()🔗
This helper creates aStaticBody3Dchild node with aConcavePolygonShape3Dcollision shape calculated from the mesh geometry. It's mainly used for testing.
intfind_blend_shape_by_name(name:StringName)🔗
Returns the index of the blend shape with the givenname. Returns-1if no blend shape with this name exists, including whenmeshisnull.
Materialget_active_material(surface:int)const🔗
Returns theMaterialthat will be used by theMeshwhen drawing. This can return theGeometryInstance3D.material_override, the surface overrideMaterialdefined in thisMeshInstance3D, or the surfaceMaterialdefined in themesh. For example, ifGeometryInstance3D.material_overrideis used, all surfaces will return the override material.
Returnsnullif no material is active, including whenmeshisnull.
intget_blend_shape_count()const🔗
Returns the number of blend shapes available. Produces an error ifmeshisnull.
floatget_blend_shape_value(blend_shape_idx:int)const🔗
Returns the value of the blend shape at the givenblend_shape_idx. Returns0.0and produces an error ifmeshisnullor doesn't have a blend shape at that index.
SkinReferenceget_skin_reference()const🔗
Returns the internalSkinReferencecontaining the skeleton'sRIDattached to this RID. See alsoResource.get_rid(),SkinReference.get_skeleton(), andRenderingServer.instance_attach_skeleton().
Materialget_surface_override_material(surface:int)const🔗
Returns the overrideMaterialfor the specifiedsurfaceof theMeshresource. See alsoget_surface_override_material_count().
Note:This returns theMaterialassociated to theMeshInstance3D's Surface Material Override properties, not the material within theMeshresource. To get the material within theMeshresource, useMesh.surface_get_material()instead.
intget_surface_override_material_count()const🔗
Returns the number of surface override materials. This is equivalent toMesh.get_surface_count(). See alsoget_surface_override_material().
voidset_blend_shape_value(blend_shape_idx:int, value:float)🔗
Sets the value of the blend shape atblend_shape_idxtovalue. Produces an error ifmeshisnullor doesn't have a blend shape at that index.
voidset_surface_override_material(surface:int, material:Material)🔗
Sets the overridematerialfor the specifiedsurfaceof theMeshresource. This material is associated with thisMeshInstance3Drather than withmesh.
Note:This assigns theMaterialassociated to theMeshInstance3D's Surface Material Override properties, not the material within theMeshresource. To set the material within theMeshresource, useMesh.surface_set_material()instead.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
