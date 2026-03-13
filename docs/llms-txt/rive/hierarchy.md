# Source: https://uat.rive.app/docs/editor/interface-overview/hierarchy.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Hierarchy

> The Hierarchy shows you all of the objects, assets, and view models in your file. This view changes based on the artboard, component, or tab you have selected.

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

# Switching Views

To switch between the different panels, click on the desired panel.

<img src="https://mintcdn.com/rive/m-97tWnDKhYq4cwm/images/SwitchView.gif?s=372cd388e8fae1a9b9a3307d53c4e559" alt="Switch View Gi" width="800" height="459" data-path="images/SwitchView.gif" />

# Hierarchy

The Hierarchy is a tree view, which shows both the parent-child relationships between objects on the stage as well as the order in which they are rendered. Learn about the Hierarchy by either watching the video or reading more below.

<YouTube id="FnnZV57Dp3c" />

Parent-child relationships are a core concept in Rive, which allows you to create complex layered animations with minimal effort. [Groups](/editor/fundamentals/groups) and [Bones](/editor/manipulating-shapes/bones) can have children in Rive.

Each row in the Hierarchy represents an item on the stage. A circle button with an arrow appears next to items that have children nested underneath them. This button allows you to expand and collapse the list of children.

## **Parent-child relationships**

<YouTube id="FnnZV57Dp3c" />

Any type of object can be a parent or a child of another type of object. When an object is a child of another object, it inherits all the transformations of its parent. For example, changing a parent objects scale will affect the child object. These transformations take place from the parents origin, not the local origin.

![Image](https://ucarecdn.com/7aed46e0-3a37-42c8-977f-f836f87a3304/)

The depth of these parent/child relationships is infinite, so you can keep stacking (or nesting) items to create grandchildren, great-grandchildren, and so on.

### **Change parent-child relationships**

To change the relationship between objects, drag and drop the object onto or out of another.

![Image](https://ucarecdn.com/b58a873b-0d11-47fc-8048-48ea3b106fec/)

## **Draw Order**

In addition to displaying the relationships between objects, the Hierarchy shows you the Draw Order of a file, with the objects at the top being rendered in front and the objects at the bottom being rendered at the back.

### **Change Draw Order**

![Image](https://ucarecdn.com/5aeb4f67-a7f6-4efe-83bd-975880f79618/)

To change the Draw Order of objects on the stage, drag and drop the shape, or group of shapes above or below another in the list. Note that draw order also affects how objects are placed and treated in a layout. Read more about that [here](https://rive.app/docs/editor/layouts/layouts-overview).

The Draw Order can be animated, but the process is a bit more in-depth. Read about it on the [Animating Draw Order](https://rive.app/docs/editor/animate-mode/animating-draw-order) page.

## **Right Click Menu**

Right clicking any object in the hierarchy will bring up a menu with different options for each object. In the menu you'll find the ability to copy and paste both objects and styles, delete objects, wrap objects in [layouts](https://rive.app/docs/editor/layouts/layouts-overview) and [solos](https://rive.app/docs/editor/manipulating-shapes/solos), show the dependency graph, add a [tag](https://rive.app/docs/editor/tagging), reverse the draw order, and[export a name](https://rive.app/docs/editor/exporting/exporting-for-runtime).

<img src="https://mintcdn.com/rive/OxZXMWcayraTF8IT/images/right_click.png?fit=max&auto=format&n=OxZXMWcayraTF8IT&q=85&s=c8c0ff91b76c25b12de9ec3438fdf38b" alt="Right Click Pn" width="2806" height="1610" data-path="images/right_click.png" />

Many of these options have shortcuts which can either be found next to the option, or in the shortcut menu.

# ​Assets Panel

The assets panel is a list view of your Images, Lottie files, Audio, and Custom fonts. This panel allows you to add, remove, replace, and modify all assets added in the file. Read more about importing and modifying assets below.

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/Assets.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=0bd795237e46f64174bca0d7bb6382c5" alt="Assets Pn" width="2806" height="1610" data-path="images/Assets.png" />

<CardGroup cols="3">
  <Card title="Importing Assets" icon="page" iconType="solid" href="https://rive.app/docs/editor/fundamentals/importing-assets" />

  <Card title="Audio Events" icon="page" iconType="solid" href="https://rive.app/docs/editor/events/audio-events" />
</CardGroup>

# Data Panel

The Data Panel is where all View Models, Enums, and Coverters for a file are created, organized, and viewed.  The panel is broken into three seperate spaces; View Models, Enums, and Converters. Read more about Data Binding [here](https://rive.app/docs/editor/data-binding/overview).

<img src="https://mintcdn.com/rive/023_vUv4_zHxZVTt/images/Data.png?fit=max&auto=format&n=023_vUv4_zHxZVTt&q=85&s=75e3a4d7de505f35a504ba5147f9a78f" alt="Data Pn" width="2806" height="1610" data-path="images/Data.png" />

The plus button on the right of each section allows you to add a new View Model, Enum, or Converter.

If any section has elements associated with it, the list can be expanded or collapsed using the arrow icon on the left.
