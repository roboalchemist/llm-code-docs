# Source: https://uat.rive.app/docs/editor/constraints/follow-path-constraint.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Follow Path Constraint

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

The Follow Path Constraint makes complex motion much easier to create by allowing us to constrain an object to a path. Watch the video, or read more below.

<YouTube id="9Gp_Kz-ylT4" />

## Setting up a Follow Path Constraint

First we’ll need both an object to constrain and a path to constrain it to.

Next, add a new constraint and select the Follow Path Constraint.

![Image](https://ucarecdn.com/bd36e6f4-22e8-4b06-8f1d-653fa6216b69/)

Now, use the target button and select the path you want to constrain the object to.

## Follow Path Properties

Like other Constraints, the Follow Path Constraint has many different properties we can customize.

#### Strength

The strength property dictates how strictly the constrained object will adhere to the constrained property.

#### Target

The Target tells the constraint which path to follow.

#### Distance

The Distance property moves the object up and down the path. As the percent increases, the constrained object moves along the path. Note that this property can exceed 100%.

![Image](https://ucarecdn.com/ad560245-56cd-49c9-8112-ef10c1edeaac/)

#### Orient

The Orient toggle controls the constrained objects rotation.

When the Orient toggle is on, the object will adjust its rotation according to the path. Note that you can’t make manual rotation changes to the object in this state.

![Image](https://ucarecdn.com/74c0ef38-e82e-40ec-a2cf-c1aa963bbc55/)

When the Orient toggle is set to off, the rotation of the constrained object does not change. This means you’ll be able to manually change the rotation of the object as you see fit.

#### Offset

The Offset toggle allows the constrained object to move along the path, but from its current, offset position.
