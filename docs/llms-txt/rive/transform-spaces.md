# Source: https://uat.rive.app/docs/editor/fundamentals/transform-spaces.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Transform Spaces

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

Container Objects, like Groups, Bones, and Layouts, allow you to create new transform spaces for your graphics, opening up the ability to animate graphics from multiple areas of interest. For example, you might want a planet to rotate on its own axis while also rotating around another planet. Multiple transform spaces (achieved by nesting groups, bones, and other container objects) allow you to achieve this.

This technique is a fundamental concept for all motion graphics. To learn more about transform spaces, be sure to watch our video on hierarchical relationships.

<YouTube id="IcSXchdnzHM" />

## Transform space example

![Image](https://ucarecdn.com/8d60bc32-96ce-4b77-ade8-836f7c92b51d/)

Nest multiple groups to transform your shapes from different locations. In the example above, a group is rotating the Earth, another is rotating the Moon around the Earth, and another is rotating the moon on its axis.

![Image](https://ucarecdn.com/ab64bd82-90f1-46eb-b50a-506ec16e36ff/)
