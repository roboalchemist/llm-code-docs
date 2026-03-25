# Source: https://uat.rive.app/docs/editor/constraints/constraints-overview.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Constraints Overview

> Learn how to use constraints in Rive.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="jYW0WuvEw_4" />

Constraints are a way to control the properties of an object through another target object. Some constraints can set limits on these properties (and their hierarchical relationships), while others can copy properties from one object to another.

Examples of where to use constraints:

* Make a character's eyes follow a target.

![Image](https://ucarecdn.com/0e6ea627-fda9-499a-b68c-3bef583ab345/)

* Ensure a character's feet stay planted on the floor while their legs automatically bend at the knees.

![Image](https://ucarecdn.com/6b0130b4-3f8a-42c8-9c55-106165c552bf/)

* Make all the wheels on a vehicle rotate together.
* Make the hands on a clock rotate.
* Copy translation, rotation, or scale from another object.
* Push an object away as one gets closer, or ensure an object always stays close to another one.

Types of constraints in Rive:

* [IK Constraint](/editor/constraints/ik-constraint)​
* [Distance Constraint](/editor/constraints/distance-constraint)
* [Transform Constraint](/editor/constraints/transform-constraint)​
* [Translation Constraint](/editor/constraints/translation-constraint)
* [Scale Constraint](/editor/constraints/scale-constraint)
* [Rotation Constraint](/editor/constraints/rotation-constraint)
