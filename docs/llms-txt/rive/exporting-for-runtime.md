# Source: https://uat.rive.app/docs/editor/exporting/exporting-for-runtime.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Exporting for Runtime

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

<Note>Exporting for runtime is available on paid plans. [Learn more about our plans and pricing](https://rive.app/pricing).</Note>

<YouTube id="H_px35jTqhg" />

To export a file for runtime, select the blue export action on the right-hand side of the toolbar or navigate to `Export` > `For runtime` via the left-hand toolbar menu. You can load the exported `.riv` file into your app, game, or website via any of our [open source runtimes](/runtimes/).

<img src="https://mintcdn.com/rive/LTt3dbNyEAMvuJ4M/images/editor/exporting/94fc0d7c-cc7e-4b17-a6f7-0a00c98db70e.webp?fit=max&auto=format&n=LTt3dbNyEAMvuJ4M&q=85&s=6c5f5a59ec74595c6ac586d26d8844e3" alt="Image" width="4328" height="2774" data-path="images/editor/exporting/94fc0d7c-cc7e-4b17-a6f7-0a00c98db70e.webp" />

## Changes to exporting object names

You may need to access certain objects at runtime, such as a text run to swap a string, or a component to access its inputs. In order to make these objects discoverable at runtime, you'll need to explicitly set it's name to be exported.

Previously, names would be exported if renamed from their default value in the editor. The issue with this approach was it assumed any renamed object was being sought at runtime, when in many cases you may simply want to rename objects to better organise your file — you didn't necessarily need them to be exported into your `.riv` export. Subsequently, we've changed this approach to provide more finite control over what object names get exported.

To export a name, right-click on it in the hierarchy or on the stage and toggle the 'Export name' option.

<Note>Objects with names set to be exported can be identified by the brackets wrapping their name.</Note>

<img src="https://mintcdn.com/rive/LTt3dbNyEAMvuJ4M/images/editor/exporting/8a147f5b-4e93-4d45-8984-64746ae1417d.webp?fit=max&auto=format&n=LTt3dbNyEAMvuJ4M&q=85&s=37cf8508b76f93c66f15910521cdeb54" alt="Image" width="786" height="946" data-path="images/editor/exporting/8a147f5b-4e93-4d45-8984-64746ae1417d.webp" />

<Note>Animations, State Machines, Events, and Input names do not require manual export.</Note>

### Benefits of optimizing your names

Exporting an object's name into your `.riv` adds a small amount of data. For large, complex files, the name data can start to add up. For that reason, it's desirable to only export the names you need to reference at runtime.

### Files created before the introduction of explicit export

For files created before this toggle was implemented, we assume any renamed object needs to be discoverable at runtime. That means you may notice a lot of items in your hierarchy being displayed inside brackets when opening an existing file. If, however, you'd prefer to not export the names and make your export size smaller, you can take these steps:

1. From the toolbar menu, select `Export options` > `Remove name exports`.
2. Individually re-enable name exports for objects you need to access at runtime by right-clicking them in the hierarchy or on the stage and selecting `Export name`.

<img src="https://mintcdn.com/rive/LTt3dbNyEAMvuJ4M/images/editor/exporting/33b3efc7-3a2d-4c19-9ebd-c2dd1a0636c1.webp?fit=max&auto=format&n=LTt3dbNyEAMvuJ4M&q=85&s=418fda8b2b603477710df32af04c8301" alt="Image" width="1468" height="1157" data-path="images/editor/exporting/33b3efc7-3a2d-4c19-9ebd-c2dd1a0636c1.webp" />
