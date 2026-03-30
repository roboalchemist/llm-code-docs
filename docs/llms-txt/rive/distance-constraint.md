# Source: https://uat.rive.app/docs/editor/constraints/distance-constraint.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Distance Constraint

> The Distance Constraint makes an object stay close, far, or exactly at a specific distance to another object.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

## How to create a Distance Constraint

<YouTube id="Nvwf27EIvdw" />

<Steps>
  <Step title="Add a Distance Constraint to an object">
    Use the Constraints section of the Inspector to add a Distance Constraint to an object.

    ![Image](https://ucarecdn.com/b6ad1d9b-706a-4090-9585-cb2954bfc45a/)
  </Step>

  <Step title="Choose a target">
    Use the new constraint's fly-out menu to select a target for this constraint.

    ![Image](https://ucarecdn.com/ce97fabc-04ab-463c-bd77-0c75a37f43a1/)
  </Step>

  <Step title="Test that the Distance Constraint is working">
    Moving the target object now causes the constrained object to stay close (which is the default mode).

    ![Image](https://ucarecdn.com/0cf99e7d-b1e1-4a0a-988d-9235c28e5868/)
  </Step>
</Steps>

## Strength

The Strength property determines how much the constrained object is affected.

A Strength of 0% means the constraint won't have any effect.

## Distance

The distance that the object will be constrained from the target object. A red constraining circle is drawn on the stage to represent this value.

## Mode

### Closer

The owner is constrained closer than the Distance setting. In other words, the owner is constrained inside the constraining sphere.

### Further

The owner is constrained further than the Distance setting. In other words, the owner is constrained outside the constraining sphere.

### Exactly

The owner is constrained exactly at the distance of the constraining sphere.
