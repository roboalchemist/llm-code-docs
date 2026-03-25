# Source: https://uat.rive.app/docs/runtimes/artboards.md

# Source: https://uat.rive.app/docs/editor/fundamentals/artboards.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Artboards

> Artboards are the foundation of a file.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="xdqqPAlB4n8" />

Artboards are the foundation of your composition across both design and animate mode. They act as the root of every hierarchy and let you define a scene's dimensions and background color. You can create infinite artboards on the [Stage](../interface-overview/stage), but each Rive file has at least one artboard.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/artboard.png?fit=max&auto=format&n=3TdvqAcmyPpedEbB&q=85&s=2bb26656a68245ec80a786d9db76ef7c" alt="Artboard Pn" width="2806" height="1610" data-path="images/artboard.png" />

## ​Active artboard

The active artboard is represented with an Active tag next to its name on the stage. You can activate an artboard by clicking on it or any of its children within the stage. Note that sections of the editor will only surface content associated with the active artboard. For instance, only the active artboard's hierarchy is displayed in the tree. Similarly, only animations referenced to the active artboard will surface within the timeline.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/active.gif?s=cd898d39d3b3579806477de8b5e09f2c" alt="Active Gi" title="Active Gi" style={{ width:"100%" }} width="800" height="459" data-path="images/active.gif" />

The active artboard is represented with a dot next to its name on the stage. You can activate an artboard by clicking on it or any of its children within the stage. Note that sections of the editor will only surface content associated with the active artboard. For instance, only the active artboard's hierarchy is displayed in the tree. Similarly, only animations referenced to the active artboard will surface within the timeline.

## Default State Machine

The default state machine is the state machine that will be played when using the play button in the Toolbar. In addition to setting the default state machine, this also sets the default artboard that a developer will see when using this file outside of Rive.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/defaultSM.gif?s=294764126c972f137e48c76d39b70f41" alt="Default SM Gi" width="800" height="458" data-path="images/defaultSM.gif" />

To change the default state machine, use the dropdown to select the one you want to use.

You can quickly play the selected state machine from Design Mode by holding shift and hitting the space bar.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/playDefault.gif?s=e1a2a60b8caf3720d7910b00078e4a3e" alt="Play Default Gi" width="800" height="458" data-path="images/playDefault.gif" />

## ​Creating an artboard

Before creating any graphics, you'll first need to create an artboard. There are two ways to create an artboard.

In a new file, you'll find options on the stage to define an artboards dimentions or to select from a few defined presets. Once you've decided on the properties, you can then hit the Create Artboard button.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/create_AB.gif?s=b92c12f253f906f337852d42a3e81b94" alt="Create AB Gi" width="800" height="458" data-path="images/create_AB.gif" />

Alternitively, you can use the​ Artboard tool which is found in the Artboard menu, or by using the shotcut A. With the tool active, click and drag to define the bounds. You can always adjust the size and position by selecting the artboard in the [Hierarchy](../interface-overview/hierarchy) to surface its properties in the [Inspector](../interface-overview/inspector).

## Artboard properties

Every artboard has various properties that can be changed in the [Inspector](../interface-overview/inspector). Some of the attributes that can be changed include an artboard's position on the [Stage](../interface-overview/stage), its size, layout properties, fill color, origin point, and render presets.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/artboard_prop.png?fit=max&auto=format&n=3TdvqAcmyPpedEbB&q=85&s=d6bd2b308e71a38bd30a94844fe85b4b" alt="Artboard Prop Pn" width="2808" height="1606" data-path="images/artboard_prop.png" />

## **Position**

The position of the artboard on the stage is controlled by the position properties of the artboard.

## Size and Size Type

By default, artboards are set to a fixed size with that size being determined by the Width and Height properties.

<img src="https://mintcdn.com/rive/m-97tWnDKhYq4cwm/images/WandH.png?fit=max&auto=format&n=m-97tWnDKhYq4cwm&q=85&s=192a9e314eed1d01c080368d0dac9e46" alt="Wand H Pn" width="2808" height="1606" data-path="images/WandH.png" />

**Link Icon**

Like other properties where the link icon is found, it can be used to lock the current ratio of the size properties.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/link.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=4fc34998113177e1d41ce3b86f8ed430" alt="Link Pn" width="2808" height="1606" data-path="images/link.png" />

**Size Type**

There are two sizing modes an artboard can have; Fixed, and Hug. These can be changed by using the dropdown under both the Width and Height properties.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/size_type.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=07e4c4109c1dbc0bdd7a22ac3196bd20" alt="Size Type Pn" width="2808" height="1606" data-path="images/size_type.png" />

As the name suggests, the Fixed type allows you to define and animate the artboards size properties.

The Hug type will let the artboard automatically size its height, width, or both to fit it's children. Note that this option is only available if the artboard has at least one child layout object.

## Origin

The origin of an artboard determines the point from which all objects associated with the artboard will be measured. By default, the origin of an artboard is X:0%, Y:0%. These values place the origin at the top left of the artboard.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/origin.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=13b42ac576e95939d6d2694b75e682b5" alt="Origin Pn" width="2808" height="1606" data-path="images/origin.png" />

As you increase the value of either the X or Y, that shifts the origin point to the right (on the X), and down (on the Y).

You won't typically be changing the origin of an artboard, but if you plan on changing the origin, it's best done before any animation work is done. Changing the origin after animation keys are added can cause objects to appear out of position due to the origin shifting to a new position.

**Component Origin**

It's important to remember that a Component shares the origin of its source artboard. If you plan to do things like scale or rotate the Component, changing the origin will help make that process easier.

If you forget to change the origin after adding animations, you can always add the Component to a group, which will give you the same level of control.

## Layout Settings

Since an Artboard is the root object that all other objects are added to, Artboards allow you to add and adjust their layout properties. Read more about layouts [here](https://rive.app/docs/editor/layouts/layouts-overview).

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/layout.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=c03eac2405f1d605de837d2cb4861a1b" alt="Layout Pn" width="2808" height="1606" data-path="images/layout.png" />

Note that these properties only take effect when one or more layouts have been added to the artboard.

## Fill and Stroke

Like other objects in Rive, Artboards can have one or more fills or strokes added to them. The process of adding and customizing fills and strokes is the same for both artboards and objects in the hierarchy.

<img src="https://mintcdn.com/rive/elfzBCmSzH1vAxLJ/images/fillandstroke.png?fit=max&auto=format&n=elfzBCmSzH1vAxLJ&q=85&s=226286e7d34a54112df2d1f2f0d40fa2" alt="Fillandstroke Pn" width="2808" height="1606" data-path="images/fillandstroke.png" />

Read more about fills and strokes [here](https://rive.app/docs/editor/fundamentals/fill-and-stroke).

## Render Presets

Selecting an artboard allows you to create Render Presets that can be used to render out static graphics such as PNGs and SVGs, as well as video and motion files like PNG sequences and MP4s.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/render.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=75017ebe6120f20072efdb29a991214c" alt="Render Pn" width="2808" height="1606" data-path="images/render.png" />

Read more about creating render presets [here](https://rive.app/docs/editor/exporting/exporting-for-video-and-static-design).

## Selected Colors

When an artboard is selected, you can see, target, and adjust all colors associated with every object on the artboard.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/selectColor.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=914dd16122c497fcc2505e8aff40f32a" alt="Select Color Pn" width="2808" height="1606" data-path="images/selectColor.png" />
