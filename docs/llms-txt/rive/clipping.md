# Source: https://uat.rive.app/docs/editor/manipulating-shapes/clipping.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Clipping

> Clipping allows you to cut one shape out from another.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="bxmipy1Gv6Y" />

## How to use Clipping

Select the shape or group you want to clip and hit the plus button next to the Clipping options in the Inspector. After hitting the plus button, you'll notice a blue border appear around the stage, indicating that you can pick a shape as the clipping source. Now, select the path you want to use as a clipping path. Remember, the clipping target must be a shape, not a group or any other object.

<img src="https://mintcdn.com/rive/YE39faeBfdtfz4ja/images/editor/manipulating-shapes/Clipping.gif?s=1a76308a76a18fd8e0d35181871072f4" alt="Clipping Gi" width="800" height="459" data-path="images/editor/manipulating-shapes/Clipping.gif" />

You can add as many clipping paths to a shape as you'd like.

## Clipping and path direction

If you have shapes that aren't clipping, or only partially clipping, be sure to check the winding of that shape. In most cases, reversing the direction of the path fixes this problem.

<img src="https://mintcdn.com/rive/YE39faeBfdtfz4ja/images/editor/manipulating-shapes/ReverseDirection.gif?s=98db38b1111e9e131f8ece9525e0c5a4" alt="Reverse Direction Gi" width="800" height="459" data-path="images/editor/manipulating-shapes/ReverseDirection.gif" />

## Inverse Clipping

Clipping is typically used to hide a part of your graphics. In the example below, we're using an ellipse to show only part of our jewel graphic.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/cb6d8e76-41f9-4ef3-81db-80db5ef37412.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=fef05c3bc24c07904da7e5495343164b" alt="Image" width="1500" height="800" data-path="images/editor/manipulating-shapes/cb6d8e76-41f9-4ef3-81db-80db5ef37412.webp" />

You occasionally may want to invert the clipping, so that only the graphics outside of the clipping paths are drawn.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/7d83b2ef-77de-4c9d-9220-12977d137fef.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=0be91147e6dd6b23569ac93438a625f8" alt="Image" width="1500" height="800" data-path="images/editor/manipulating-shapes/7d83b2ef-77de-4c9d-9220-12977d137fef.webp" />

This is achieved using a clipping path that looks like the gray shape in the image below.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/b71b9c54-7d99-43d9-9614-29ada59bf6cc.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=cc328eff3fd1e349c08d818dc29389ba" alt="Image" width="1500" height="800" data-path="images/editor/manipulating-shapes/b71b9c54-7d99-43d9-9614-29ada59bf6cc.webp" />

To create this shape, draw a rectangle the size of the artboard. Add both the rectangle path and ellipse path to the same shape layer in your Hierarchy.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/2c9721d3-a003-47c4-b0b8-e8da713831da.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=4a8e2432ac028da590ba39d837cb3265" alt="Image" width="736" height="373" data-path="images/editor/manipulating-shapes/2c9721d3-a003-47c4-b0b8-e8da713831da.webp" />

Note that your shape might not show a hole as ours does. That's because you need to set the Fill Rule of your shape to Even-Odd. This setting doesn't affect your Clipping Path, but it helps explain how the Even-Odd operation works, which will be useful later!

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/4e35e170-b0e0-470b-8d2c-53bf74388fd7.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=3c8167cff5b600256ebf462b56715d00" alt="Image" width="701" height="448" data-path="images/editor/manipulating-shapes/4e35e170-b0e0-470b-8d2c-53bf74388fd7.webp" />

Select the group containing the jewel and use the "plus" icon in the Clipping section of the Inspector. Next, select the Clipping Shape as the target.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/a5b01f21-4757-435b-8a6b-f822cc519005.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=7170d6c4558cbeb292a2a27b9eb28efe" alt="Image" width="1038" height="461" data-path="images/editor/manipulating-shapes/a5b01f21-4757-435b-8a6b-f822cc519005.webp" />

Open the Clip Options and set the Operation to Even-Odd.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/c38910e3-9b33-4fef-a69f-5a2154aa6eec.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=5e50206a83a30ef381f93e0c07afccf7" alt="Image" width="583" height="260" data-path="images/editor/manipulating-shapes/c38910e3-9b33-4fef-a69f-5a2154aa6eec.webp" />

Be sure to hide the visibility of your clipping shape so it doesn't cover your graphic.
