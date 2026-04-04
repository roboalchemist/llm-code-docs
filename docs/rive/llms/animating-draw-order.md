# Source: https://uat.rive.app/docs/editor/animate-mode/animating-draw-order.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Animating Draw Order

export const Marketplace = ({href}) => {
  const hrefWithTracking = `${href}?utm_source=docs&utm_medium=docs_link_card&utm_campaign=docs_to_marketplace_links`;
  return <Card title="Learn by remixing" icon="external-link" href={hrefWithTracking} arrow="true" horizontal>
      Open this file on Marketplace, then click Remix to experiment in the Rive Editor.
    </Card>;
};

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

You can change the draw order of your graphics at design time by moving items up and down the [Hierarchy](/editor/interface-overview/hierarchy)– but what if you want to change the draw order during an animation? Or what if you want to change the draw order without breaking the current hierarchical structure? Rive allows you to accomplish this with Draw Order Rules.

<YouTube id="6J3JIwgUwe0" />

## Draw Order Rules

To animate the draw order of a group or shape, start by selecting it. Use the Draw Order section of the Inspector to create Draw Order Rules.

<Marketplace href="https://rive.app/community/files/26116-48795-animating-draw-order" />

<img src="https://mintcdn.com/rive/LTt3dbNyEAMvuJ4M/images/editor/animate-mode/426adab7-b1d3-47bc-bc42-c5cc397fa9d6.webp?fit=max&auto=format&n=LTt3dbNyEAMvuJ4M&q=85&s=c00eb06083812410bb31e2db382eaed9" alt="Image" width="1340" height="1020" data-path="images/editor/animate-mode/426adab7-b1d3-47bc-bc42-c5cc397fa9d6.webp" />

The Normal rule is the default order (based on [Hierarchy](/editor/interface-overview/hierarchy) order). When the radio button next to this rule is active, the shape appears at its default draw order.

Draw Order Rules allow you to select a target (note that this must be a drawable item, not a group) and whether to draw above or below the target.

<Note>The target must be a drawable item, like a shape. It cannot be a group.</Note>

In Animate mode, use the radio button next to the Draw Order Rules to set a key. Note that these are [Hold keys](/editor/animate-mode/interpolation-easing#hold) as Draw Order cannot be interpolated.

![Image](https://ucarecdn.com/32925768-cbcf-461c-9fe1-b745bf90a34d/)
