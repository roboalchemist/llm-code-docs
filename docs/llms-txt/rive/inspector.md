# Source: https://uat.rive.app/docs/editor/interface-overview/inspector.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Inspector

> The Inspector is located on the right side of the Editor. It shows all of the editable properties of all objects in the Rive editor.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

# Inspector

An object's editable properties can be found in the Inspector. The Inspector changes dynamically depending on your selected object and where you are in the editor.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/inspector.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=cf71221aef76546adfa431ace841e657" alt="Inspector Pn" width="2816" height="1628" data-path="images/inspector.png" />

## Background Color, Tags, Default Interpolation

When nothing is selected, the Inspector has three sections: Backgrounds, Tags, and Default Interpolation.

**Background color**

Found at the top of the Inspector, this section allows you to change the background color of the editor for both Animate and Design modes. This is a helpful way to remind yourself which mode you are currently in.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/backgrounds.png?fit=max&auto=format&n=3TdvqAcmyPpedEbB&q=85&s=48a7a4b1a3c9b62b827ddabfc009de99" alt="Backgrounds Pn" width="2806" height="1610" data-path="images/backgrounds.png" />

**Tags**

Below the background color, you can see, edit, and add new tags to your file. Learn more about tags [here](https://rive.app/docs/editor/tagging).

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/tags.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=a622ec3e00b9393df8accc2cef7ace16" alt="Tags Pn" width="2806" height="1610" data-path="images/tags.png" />

**Default Interpolation**

Below Tags is the Default Interpolation for your file.

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/default_Int.png?fit=max&auto=format&n=3TdvqAcmyPpedEbB&q=85&s=6c57f98a38a1bfcb0940d0dae48189a8" alt="Default Int Pn" width="2806" height="1610" data-path="images/default_Int.png" />

When you set a key on the timeline, it will use the file's default interpolation until it's changed on the timeline. By changing the default interpolation, you can control which interpolation curve is applied to new keys.

## Align and Distribute tools

<YouTube id="LBB3BDo5pR4" />

When one or more objects, such as shapes or groups, are selected, the Align tools appear at the top of the inspector. Use them to align or distribute the selected objects. Read more about the Align tools here.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/Align.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=c7e538412ee0036e9764b5a269fc17fa" alt="Align Pn" width="2806" height="1610" data-path="images/Align.png" />

## Layout and N-Slicing

When one or more objects, such as shapes or groups, are selected, the inspector gives the option to layout or n-slice the current selection.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/LOandN.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=318ebab643428cfe06a98b269988158c" alt="L Oand N Pn" width="2806" height="1610" data-path="images/LOandN.png" />

<CardGroup cols={2}>
  <Card title="Layouts" icon="page" iconType="solid" href="https://rive.app/docs/editor/layouts/layouts-overview">
    Layouts let you build responsive designs.
  </Card>

  <Card title="N-Slicing" icon="page" iconType="solid" href="https://rive.app/docs/editor/layouts/n-slicing">
    N-slicing lets you stretch or repeat parts of raster and vector designs.
  </Card>
</CardGroup>

## Transform properties

The transform properties of an object appear below the Align tools. Generally, these properties include position, scale, and rotation, but they can also include width and height if you have a path layer selected.

<img src="https://mintcdn.com/rive/m-97tWnDKhYq4cwm/images/Transform.png?fit=max&auto=format&n=m-97tWnDKhYq4cwm&q=85&s=9fbd5ac07b502be065baa40b8037a648" alt="Transform Pn" width="2806" height="1610" data-path="images/Transform.png" />

## Layer properties

Below the transform properties, you'll find several properties that allow you to customize the look of some objects on the stage. These properties include blend mode, opacity, fill, and stroke.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/Layer.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=3f58c29ee9a7fbc9813535b9984fb7d0" alt="Layer Pn" width="2806" height="1610" data-path="images/Layer.png" />

## Additional properties

Below the Layer properties, you'll find many additional properties that you can add such as Clipping, Constraints, Custom Draw Order, and Selection Colors

<img src="https://mintcdn.com/rive/3TdvqAcmyPpedEbB/images/additional.png?fit=max&auto=format&n=3TdvqAcmyPpedEbB&q=85&s=de57d0373b7c58ad4bc775b37de79bef" alt="Additional Pn" width="2806" height="1610" data-path="images/additional.png" />

<CardGroup cols="3">
  <Card title="Manipulating Shapes" icon="page" iconType="solid" href="../manipulating-shapes/manipulating-shapes">
    The Rive editor gives you multiple ways to manipulate your graphics to create the animation that you want. I
  </Card>

  <Card title="Constraints" icon="page" iconType="solid" href="../constraints/">
    Constraints are a way to control the properties of an object through another target object.
  </Card>

  <Card title="Animate Mode" icon="page" iconType="solid" href="../animate-mode/">
    Rive has two distinct modes, Design and Animate.
  </Card>
</CardGroup>

### Motion and State Properties

This section shows customizable properties when Keys, Transitions, or States are selected.

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/motioninspector.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=1dcda320e3e24d854d96a6aafaec9d65" alt="Motioninspector Pn" width="2806" height="1610" data-path="images/motioninspector.png" />

<CardGroup cols={3}>
  <Card title="Interpolation Panel" icon="page" iconType="solid" href="https://rive.app/docs/editor/animate-mode/interpolation-easing">
    Selecting a key brings up the interpolation panel.
  </Card>

  <Card title="Transition Properties" icon="page" iconType="solid" href="https://rive.app/docs/editor/state-machine/transitions">
    Selecting a transition will show customizable transition properties.
  </Card>

  <Card title="State Properties" icon="page" iconType="solid" href="https://rive.app/docs/editor/state-machine/states">
    State properties are customizable by selecting a state.
  </Card>
</CardGroup>
