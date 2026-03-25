# Source: https://uat.rive.app/docs/editor/state-machine/layers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Layers

> Layers let you build more complex logic and animation with the state machine.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<YouTube id="7Vb1LosMzwk" />

A layer on the state machine allows you to play a single animation at a time. For this reason, you can create multiple layers if you wish to mix multiple animations or add additional interactions to a state machine.

This example uses layers to mix different background animations, and add multiple interactions onto a single artboard.

![Using multiple Layers](https://ucarecdn.com/aeedde5a-598f-42b3-a5df-81212757395e/)

### Creating a new layer

To create a new layer, use the plus button on the Layers Tab.

<img src="https://mintcdn.com/rive/kz3-JP-PIC2RXp04/images/editor/state-machine/state-machine-layer-create.gif?s=4a21b6f84b27f5d561bd727edefd4e8a" alt="Add a new Layer" width="1200" height="418" data-path="images/editor/state-machine/state-machine-layer-create.gif" />

Notice that each new tab that you create comes with the Default States.

### Layer Order

It may not be obvious, but the order of your Layers matter, with Layers to the right taking priority over the Layers to the left. In most cases, this won’t matter, but if your Layers have States that control the same object properties, the animations in the right most layer will take priority over the layers to the left as they mix.

<YouTube id="Fc9MutscvAo" />

**Changing layer order**

You can change the layer order by dragging and dropping your layers around on the Layers tab.

<img src="https://mintcdn.com/rive/kz3-JP-PIC2RXp04/images/editor/state-machine/state-machine-layer-order.gif?s=113a074cbd93cfb5510b1c3e34443723" alt="Move layers" title="" style={{ width:"100%" }} width="1200" height="354" data-path="images/editor/state-machine/state-machine-layer-order.gif" />

**Delete layer**

You can delete a layer with right click over the name and selecting the option "Delete Layer".

<img src="https://mintcdn.com/rive/kz3-JP-PIC2RXp04/images/editor/state-machine/state-machine-layer-delete.gif?s=f57e7d962a6176e5719ea338b6be8b2e" alt="Delete layer" width="1200" height="354" data-path="images/editor/state-machine/state-machine-layer-delete.gif" />

**Duplicate layer**

You can delete a layer with right click over the name and selecting the option "Delete Layer".

<img src="https://mintcdn.com/rive/kz3-JP-PIC2RXp04/images/editor/state-machine/state-machine-layer-duplicate.gif?s=d09eb687f2643b40f2be962eb4cf711f" alt="Duplicate layer" width="1200" height="356" data-path="images/editor/state-machine/state-machine-layer-duplicate.gif" />

**Disable and Enable layer**

You can delete a layer with right click over the name and selecting the option "Delete Layer".

<img src="https://mintcdn.com/rive/kz3-JP-PIC2RXp04/images/editor/state-machine/state-machine-layer-disable.gif?s=9eba7ddedaa7cef07bda719600d69014" alt="Disable and Enable layer" width="1200" height="356" data-path="images/editor/state-machine/state-machine-layer-disable.gif" />
