# Source: https://uat.rive.app/docs/editor/fundamentals/shapes-and-paths-overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Shapes and Paths Overview

> Rive allows you to create, edit, and animate vector graphics using either procedural or custom shapes. These graphics combine shape and path layers to define them, which Rive exposes to give you greater flexibility and control with your designs and animations.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

To learn more about Shape and Path layers, watch our video on Shapes and Paths, or read more below.

<YouTube id="KunkCnbkTsg" />

## Shape layer

<img src="https://mintcdn.com/rive/dYBUwExuLozkRR-u/images/editor/fundamentals/shape-and-path-shapelayer.png?fit=max&auto=format&n=dYBUwExuLozkRR-u&q=85&s=6c6f698be08c17ece6ef3c80661d814e" alt="Shape Layer" width="1506" height="694" data-path="images/editor/fundamentals/shape-and-path-shapelayer.png" />

Vectors in Rive are rendered on shape layers. Shape layers define the style of the shape by allowing you to customize the fill and stroke.\`

<img src="https://mintcdn.com/rive/dYBUwExuLozkRR-u/images/editor/fundamentals/shape-and-path-fill.png?fit=max&auto=format&n=dYBUwExuLozkRR-u&q=85&s=11273f97c8d4ea660cfc394c7c7e6129" alt="Fill and Stroke" width="1778" height="1063" data-path="images/editor/fundamentals/shape-and-path-fill.png" />

## Path layer

<img src="https://mintcdn.com/rive/dYBUwExuLozkRR-u/images/editor/fundamentals/shape-and-path-pathlayer.gif?s=4775f24f8e247de8505701a142f75580" alt="Path Layer" width="1200" height="444" data-path="images/editor/fundamentals/shape-and-path-pathlayer.gif" />

The actual shape of a vector is defined by a path (or multiple paths). Expanding a shape layer in Rive will reveal the paths it's using.

<img src="https://mintcdn.com/rive/dYBUwExuLozkRR-u/images/editor/fundamentals/shape-and-path-move.gif?s=1eef0524259866a2f2f540af0a1531ba" alt="Move Path" width="1200" height="425" data-path="images/editor/fundamentals/shape-and-path-move.gif" />

‌You can add new paths to any shape by dragging and dropping an existing path onto the desired shape layer.

### Path layer properties

Path layers display properties that to the type of path. Learn more about [Procedural Shapes](/editor/fundamentals/procedural-shapes).

<img src="https://mintcdn.com/rive/dYBUwExuLozkRR-u/images/editor/fundamentals/shape-and-path-properties.png?fit=max&auto=format&n=dYBUwExuLozkRR-u&q=85&s=6e9e68ab8a209c0c796e966e34d9b922" alt="Path layer Properties" width="1507" height="844" data-path="images/editor/fundamentals/shape-and-path-properties.png" />

## Enter and Esc shortcuts

Use the `Enter` key to quickly navigate down the Hierarchy. If you have a shape selected, this allows you to select the child path layer quickly.

Use the `Esc` key to quickly navigate up the Hierarchy. If you have a path selected, this allows you to select the parent shape layer quickly.
