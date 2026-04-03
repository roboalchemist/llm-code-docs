# VisualShaderNodeParticleMeshEmitter in English

# VisualShaderNodeParticleMeshEmitter

Inherits:VisualShaderNodeParticleEmitter<VisualShaderNode<Resource<RefCounted<Object
A visual shader node that makes particles emitted in a shape defined by aMesh.

## Description

VisualShaderNodeParticleEmitterthat makes the particles emitted in a shape of the assignedmesh. It will emit from the mesh's surfaces, either all or only the specified one.

## Properties

| Mesh | mesh |  |
|---|---|---|
| int | surface_index | 0 |
| bool | use_all_surfaces | true |

Mesh
mesh
surface_index
bool
use_all_surfaces
true

## Property Descriptions

Meshmesh🔗

- voidset_mesh(value:Mesh)
voidset_mesh(value:Mesh)
- Meshget_mesh()
Meshget_mesh()
TheMeshthat defines emission shape.
intsurface_index=0🔗
- voidset_surface_index(value:int)
voidset_surface_index(value:int)
- intget_surface_index()
intget_surface_index()
Index of the surface that emits particles.use_all_surfacesmust befalsefor this to take effect.
booluse_all_surfaces=true🔗
- voidset_use_all_surfaces(value:bool)
voidset_use_all_surfaces(value:bool)
- boolis_use_all_surfaces()
boolis_use_all_surfaces()
Iftrue, the particles will emit from all surfaces of the mesh.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
