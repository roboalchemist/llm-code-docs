# Source: https://uat.rive.app/docs/editor/manipulating-shapes/solos.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Solos

> A Solo is similar to a group, but only one of the elements inside the solo is rendered at a time. This is much faster than having to animate the opacity of each object individually.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="diYNK8aidaE" />

## Creating a Solo

There are two ways to create a solo. The first is to select multiple items on your artboard, right click them in the Hierarchy, and click "Wrap in Solo".

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/28ce305c-d84f-45ca-b70f-f0aa925ec21e.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=0e711652936036bea7fe34f118130a3d" alt="Wrap in Solo" width="1063" height="458" data-path="images/editor/manipulating-shapes/28ce305c-d84f-45ca-b70f-f0aa925ec21e.webp" />

The second option is to select the **Solo** tool from the **Hierarchy Tools** dropdown (or click **S** on your keyboard) and click anywhere on your artboard. Now that you have a Solo in your Hierarchy, you can drag elements into it.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/0bacaffd-b25c-445f-9677-a4f31c4c2043.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=63913d134d7716eb7d074bc0002fc7ae" alt="Solo Tool" width="1058" height="385" data-path="images/editor/manipulating-shapes/0bacaffd-b25c-445f-9677-a4f31c4c2043.webp" />

## Animating Solos

You can animate solos by opening a timeline and clicking the solo's radio buttons in the Hierarchy.

<img src="https://mintcdn.com/rive/IMrXM-oXoMvrTV9Y/images/editor/manipulating-shapes/8be34515-c2e9-46f9-9dc3-7347e2528dd9.webp?fit=max&auto=format&n=IMrXM-oXoMvrTV9Y&q=85&s=bb7842a800543be3f35f9d1ac8b3ff2c" alt="Image" width="1290" height="553" data-path="images/editor/manipulating-shapes/8be34515-c2e9-46f9-9dc3-7347e2528dd9.webp" />

## Creating New Skins

One of the most common use cases for Solos is creating new skins for a character.

![Image](https://ucarecdn.com/1dc10aa9-1dd9-438d-8a3d-8b8192ff9647/)

## Change the underlying rig

Sometimes when we animate an object or character, we need to create animations at different angles. Solos allow us to create multiple rigs and switch between them during our animation.

![Image](https://ucarecdn.com/c168815b-d92e-4c8e-b5f6-4ecbc013e08d/)

## Frame-by-frame animation

The ability to toggle between many images gives you a quick way to create frame by frame effects.

![Image](https://ucarecdn.com/76841fdd-3190-46d5-b553-e33bd7cf9c6d/)
