# Source: https://uat.rive.app/docs/editor/fundamentals/freeze-and-origin.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Freeze and Origin

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="nA15ZXkMb_c" />

When you transform objects, their children inherit the same transformations. The location where these transformations happen (sometimes called the origin, anchor point, or pivot) affects how your objects animate.

For example, manipulating the scale of a group creates different results if the scale originates in the center or the bottom.

You need to reposition the parent group to change the point of origin for these transformations. However, moving a parent causes all the children to move with it. The Freeze feature makes it possible to achieve this without having to rework the hierarchy structure.

# Origin of a Procedural Path

Procedural objects (like artboards and procedural paths) have an origin property. The origin of a procedural path determines where its properties originate from. For example, changing the width of a rectangle with its origin in the middle (50% X and 50% Y) causes it to grow from its center.

<img src="https://mintcdn.com/rive/DTnv-S0T6YU6evKP/images/editor/fundamentals/freeze-origin-center.gif?s=46f9070519489cfdf50bc87b76abad54" alt="Origin in the center" width="1200" height="500" data-path="images/editor/fundamentals/freeze-origin-center.gif" />

Changing the width on a rectangle with its origin on the left side (0% X) causes it to grow from its left.

<img src="https://mintcdn.com/rive/DTnv-S0T6YU6evKP/images/editor/fundamentals/freeze-origin-left.gif?s=3c091b27c295d701d6ba184962ad486a" alt="Origin on the left" width="1200" height="517" data-path="images/editor/fundamentals/freeze-origin-left.gif" />

This is particularly useful when animating paths that have other procedural properties enabled, such as rounded corners.

You can use the Freeze feature to change the Origin position on the Stage. Alternatively, set the exact value in the Inspector.

# Origin of a Custom Path and Group

### Freeze Mode

The Freeze feature allows you to move any parent object (groups, shapes, bones) without affecting the position of its children. Activate Freeze in the [Transform Tools menu](../interface-overview/toolbar) or use the `Y` shortcut.

When Freeze Mode is active, you'll notice that your Stage is wrapped in a blue outline. You're now free to move the Origin without affecting the children.

Be sure to turn off Freeze by pressing `Y` again.

# Changin Origin with Align Tools

You can quickly change the location of an origin with the align tools.

Start by selecting the shape, then holding Option on Mac, or Alt on Windows. \
\
This now allows the align tool to repostion the Origin various positions.
