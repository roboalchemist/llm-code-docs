# Source: https://uat.rive.app/docs/editor/fundamentals/edit-vertices.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit Vertices

> No matter the type of vector you create, you can edit the vertices by changing their position or handles in both design and animate mode.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

## Edit Vertices mode

To enter Edit Vertices mode, either select the shape and hit enter twice or select a path and hit enter once.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/EVM.gif?s=35151ad31ed2eb699338b707fe412ced" alt="EVM Gi" width="800" height="458" data-path="images/EVM.gif" />

After activating Edit Vertices mode, you can select any vertex, reposition it, and edit the bezier handles.

### Deep Selection

You may want to select and edit a specific path when dealing with a group of shapes. You can either find that path in the Hierarchy or you can use Deep Selection to select it directly on the Stage.

To select a path within a group on the stage, hold `⌘` (Mac) or `ctrl` (Windows) and click the target path. Alternatively, you can double-click on the path you want to select.

### Path Options

Each path in Edit Vertices mode has a set of path options at the top of the Inspector.

**Done Editing Button**

The Done Editing button can be used to exit Edit Vertices Mode.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/DoneEdit.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=3a712007ff01da10c8369a0b22fcc2c5" alt="Done Edit Pn" width="2808" height="1606" data-path="images/DoneEdit.png" />

**Open Path**

The Open Path button will disconnect the last vertex from the first vertex.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/OpenPath.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=9164e42d75477fec29da0e22e24d9fb1" alt="Open Path Pn" width="2808" height="1606" data-path="images/OpenPath.png" />

**Reverse Direction**

<YouTube id="zp2NNsSTfO8" />

The Reverse Direction button can be used to reverse the direction of the path. Depending on the Fill-Rule, this can eliminate holes in our shape by changing the mathmatical value of the selected path.

**Convert Radial Corners**

Straight vertices with a corner radius will deform when the scale transform is applied to the shape or path layer. You can convert radial corners from a procedural property to a defined set of vertices. This process will eliminate deformation of the corner.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/convert.gif?s=6097625a00f0d19b51c049fee365fb2f" alt="Convert Gi" width="800" height="458" data-path="images/convert.gif" />

## Bezier Handles

**‌Straight**

‌The default handles are set to straight, which creates straight edges between vertices.

<img src="https://mintcdn.com/rive/m-97tWnDKhYq4cwm/images/Straight.png?fit=max&auto=format&n=m-97tWnDKhYq4cwm&q=85&s=99aeeeea0cdd7757a1b001373d23a0ef" alt="Straight Pn" width="2808" height="1606" data-path="images/Straight.png" />

**Corner Radius**

The Corner Radius property allows you to round straight corners. This property only appears on vertices that are set to straight.

**‌Mirrored**

‌Mirrored is the default handle when you create a vertex by clicking and dragging. These handles always keep the same rotation and length.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/mirriored.gif?s=383d95ab2814747673a8482c23623062" alt="Mirriored Gi" width="800" height="458" data-path="images/mirriored.gif" />

**‌Detached‌**

Detached handles allow each handle to have its own rotation and length.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/detached.gif?s=29d28854aa3445a53d9a4572d6a78b2e" alt="Detached Gi" width="800" height="459" data-path="images/detached.gif" />

**‌Asymmetric**

‌Asymmetric handles share the same rotation but can have lengths independently of each other.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/asem.gif?s=db289b47f6e340fe4f99f7de50cd67f1" alt="Asem Gi" width="800" height="459" data-path="images/asem.gif" />
