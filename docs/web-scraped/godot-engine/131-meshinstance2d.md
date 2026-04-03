# MeshInstance2D

# MeshInstance2D
Inherits:Node2D<CanvasItem<Node<Object
Node used for displaying aMeshin 2D.

## Description
Node used for displaying aMeshin 2D. This can be faster to render compared to displaying aSprite2Dnode with large transparent areas, especially if the node takes up a lot of space on screen at high viewport resolutions. This is because using a mesh designed to fit the sprite's opaque areas will reduce GPU fill rate utilization (at the cost of increased vertex processing utilization).
When aMeshhas to be instantiated more than thousands of times close to each other, consider using aMultiMeshin aMultiMeshInstance2Dinstead.
AMeshInstance2Dcan be created from an existingSprite2Dvia a tool in the editor toolbar. Select theSprite2Dnode, then chooseSprite2D > Convert to MeshInstance2Dat the top of the 2D editor viewport.

## Tutorials
- 2D meshes
2D meshes

## Properties

| Mesh | mesh |
|---|---|
| Texture2D | texture |

Mesh
mesh
Texture2D
texture

## Signals
texture_changed()🔗
Emitted when thetextureis changed.

## Property Descriptions
Meshmesh🔗
- voidset_mesh(value:Mesh)
voidset_mesh(value:Mesh)
- Meshget_mesh()
Meshget_mesh()
TheMeshthat will be drawn by theMeshInstance2D.
Texture2Dtexture🔗
- voidset_texture(value:Texture2D)
voidset_texture(value:Texture2D)
- Texture2Dget_texture()
Texture2Dget_texture()
TheTexture2Dthat will be used if using the defaultCanvasItemMaterial. Can be accessed asTEXTUREin CanvasItem shader.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.