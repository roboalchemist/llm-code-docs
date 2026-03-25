# Source: https://uat.rive.app/docs/editor/layouts/layout-styles.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Styles

> Layouts can have styles applied directly to them

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

Though Layouts behave as containers for other Rive objects, Layouts themselves can contain styles including:

* Fills
* Strokes
* Feathers
* Blend Modes
* Corner Radius

## Background and Foreground styles

The above mentioned styles can be applied to a Layout such that either the style renders above (in front of) or below (behind) the Layout's child objects. This can be useful for example, in cases where the Fill and Feathered drop shadow needs to render behind the children, but the stroke should render in front of the children.

<img src="https://mintcdn.com/rive/KnNrDuhU1mIj7cOb/images/editor/layout-fills-strokes.png?fit=max&auto=format&n=KnNrDuhU1mIj7cOb&q=85&s=5661c2a1c834a2791af2d7081a06004f" alt="Image" width="542" height="296" data-path="images/editor/layout-fills-strokes.png" />

## Corner Radius

Fills, strokes and feathers applied on a Layout generate a rectangular shape, but you can modify any of the corners to have a custom corner radius. When applied, both background and foreground styles will draw themselves respecting the corner radius value.

<Tip>Corner radius also determines the shape of the Layout's clipping bounds, so if you enable clipping on the Layout, it's children will be clipped using the corner radius values</Tip>

## Blend Modes

When a Layout has a background and/or foreground fill or stroke applied, a blend mode can be applied to the Layout that affects overlapping objects in two ways:

* If a style is applied to the background, it will apply the blend to any objects behind the Layout itself.
* If a style is applied to the foreground, it will apply the blend to all of the Layout's children, the Layout's background AND any objects behind the Layout itself.
