# Source: https://uat.rive.app/docs/editor/fundamentals/pen-tool-overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Pen Tool Overview

> The Pen tool allows you to create custom vector paths as well as add additional vertices to your procedural paths. Learn more about the Pen tool by either watching the video or reading more below.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="dE1OEaaX5dw" />

## Creating custom shapes

The Pen tool allows you to create custom vector shapes. Activate the Pen tool by finding it under the Create Tools menu or by using the `P` shortcut.

Click on the stage to place vertices.

<img src="https://mintcdn.com/rive/3Kg1AF4ZMQvAbAVg/images/editor/fundamentals/pen-tool-create.gif?s=aaed4929c9d48e1694acc1a410f8ef34" alt="Image" width="1450" height="750" data-path="images/editor/fundamentals/pen-tool-create.gif" />

Click and drag to create a vertex with bezier handles. When you are finished, hit `esc` on your keyboard.

<img src="https://mintcdn.com/rive/3Kg1AF4ZMQvAbAVg/images/editor/fundamentals/pen-tool-create-handless.gif?s=8491415ee5c9a63b5a3abc356002587f" alt="Image" width="1450" height="750" data-path="images/editor/fundamentals/pen-tool-create-handless.gif" />

## Path & vertex shortcuts

* Hold Alt (Opt) to detach the Pen tool while drawing a path.
* Ctrl+click (Cmd+click) on the vertex to toggle between mirrored and straight handles.
* With Select or Pen tool, Ctrl+click (Cmd+click) on the vertex handle to remove that handle.
* With Select or Pen tool, Alt+click (Opt+click) on a vertex handle to detach the handle.
* With Pen tool, Alt+click (Opt+click) on a vertex to delete the vertex.
* Alt+drag (Option+drag) to duplicate vertices.
