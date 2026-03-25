# Source: https://uat.rive.app/docs/editor/constraints/scale-constraint.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Scale Constraint

> The Scale Constraint allows you to set limits on an object's scale and/or copy the scale properties from a target object. These properties can be independently activated.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="4fFuGQHAiIQ" />

## How to create a Scale Constraint

<Steps>
  <Step title="Add a Scale Constraint to an object">
    Use the Constraints section of the Inspector to add a Scale Constraint to an object.

    ![Image](https://ucarecdn.com/ae4a6d01-89b4-423d-988d-73a7094e4d8a/)
  </Step>

  <Step title="Choose a target">
    ![Image](https://ucarecdn.com/dde72565-7f0f-447b-a98a-3cc33c55c79a/)

    Use the new constraint's fly-out menu to select a target for this constraint.

    ![Image](https://ucarecdn.com/52454a24-75d9-464b-8c8e-29de2e620b8a/)
  </Step>

  <Step title="Test that the Scale Constraint is working">
    Manipulating the target object now causes the constrained object to Scale properties.
  </Step>
</Steps>

## Strength

The Strength property determines how much the constrained object is affected.

A Strength of 0% means the constraint won't have any effect.

A Strength of 50% means half the value from the target will be applied.

## Transform Space

### Source Space

Choose whether this constraint should use World or Local coordinates for the Source Space.

### Destination Space

Choose whether this constraint should use World or Local coordinates for the Destination Space.

### Min/Max Space

Choose whether this constraint should use World or Local coordinates for the Min/Max Space.
