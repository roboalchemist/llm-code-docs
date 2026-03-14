# Source: https://uat.rive.app/docs/editor/fundamentals/procedural-shapes.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Procedural Shapes

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="vU5SrgymGD8" />

## Creating a procedural shape

<img src="https://mintcdn.com/rive/Ft3_TIyFWFSLdOpR/images/editor/fundamentals/procedural-shapes-menu.png?fit=max&auto=format&n=Ft3_TIyFWFSLdOpR&q=85&s=7472ba4a4f10c7e2f9b153e0d47f07f5" alt="Procedural Shapes Menu" width="1596" height="645" data-path="images/editor/fundamentals/procedural-shapes-menu.png" />

Under the Create Tools menu, you will find shape tools that are defined by procedural properties like width, height, corner radius, number of points, and more.

<img src="https://mintcdn.com/rive/Ft3_TIyFWFSLdOpR/images/editor/fundamentals/procedural-shapes-create.gif?s=53a2cf4a6b91cf4a1413ba17df6b37a6" alt="Create Shape" width="1200" height="690" data-path="images/editor/fundamentals/procedural-shapes-create.gif" />

Select the tool then click and drag anywhere inside an artboard. Hold `shift` to constrain the proportions of the shape.

### Convert a procedural path to a custom path

<img src="https://mintcdn.com/rive/Ft3_TIyFWFSLdOpR/images/editor/fundamentals/procedural-shapes-convert.gif?s=89f1e611514fad03bc8e3a83f02ecd49" alt="Convert a procedural path to a custom path" width="1200" height="557" data-path="images/editor/fundamentals/procedural-shapes-convert.gif" />

To edit the vertices of a procedural path, press `Enter` on your keyboard. This will covert the path into a custom path and allow you to modify the position of each vertex. Procedural properties (e.g. width, height, number of points) will no longer be available. Keep in mind that any animations applied to these properties will also be removed once the procedural path is converted to a custom path.

### Origin of a procedural path

The [origin](/editor/fundamentals/freeze-and-origin) of a procedural path determines where its properties originate from. For example, changing the width on a rectangle with its origin in the middle (50% X and 50% Y) causes it to grow from its center.

<img src="https://mintcdn.com/rive/Ft3_TIyFWFSLdOpR/images/editor/fundamentals/procedural-shapes-size.gif?s=2eb359c3810f84d2b56f8274df7fc291" alt="Change size of procedura shape" width="1200" height="500" data-path="images/editor/fundamentals/procedural-shapes-size.gif" />

Changing the width of a rectangle with its origin on the left side (0% X) causes it to grow from its left.

<img src="https://mintcdn.com/rive/Ft3_TIyFWFSLdOpR/images/editor/fundamentals/procedural-shapes-origin.gif?s=cd318a6d03551d0377d6a5d7e124b8ec" alt="Origin in procedural shapes" width="1200" height="517" data-path="images/editor/fundamentals/procedural-shapes-origin.gif" />

This is particularly useful when animating paths that have other procedural properties enabled, such as rounded corners.
