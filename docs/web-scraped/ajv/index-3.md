# Source: https://react-page.github.io/

Title: 

URL Source: https://react-page.github.io/

Published Time: Wed, 26 Apr 2023 08:02:49 GMT

Markdown Content:
React Page 5.4.4

[](https://github.com/react-page/react-page)

* * *

* * *

[Docs](https://react-page.github.io/docs)[Github](https://github.com/react-page/react-page)

* * *

[Demo](https://react-page.github.io/)[Read only](https://react-page.github.io/readonly)[Empty editor](https://react-page.github.io/empty)[React Admin example](https://react-page.github.io/examples/reactadmin)

* * *

[Old demo (v0)](https://react-page.github.io/old/demo)[Old import-from-html-Demo](https://react-page.github.io/old/fromhtml)

* * *

[Latest version](https://react-page.github.io/)[beta version](https://react-page.github.io/beta)

Text

Next Level Content Editing
--------------------------

ReactPage
=========

Text

**ReactPage** is a next level content editor for react.

It enables **_webmasters and content editors_**to create the content they want with the `<Components />` you provide as a developer.

Background

Image

Text

Batteries included - Key features
---------------------------------

*   powerful and customizable **RichText Editor (**_powered by_[](https://github.com/vazco/uniforms)[_Slate_](https://github.com/ianstormtaylor/slate/))
*   12-column grid responsive grid layout
*   Drag & Drop cells
*   Undo & Redo, copy and hotkey support
*   Multi-Language support
*   Add any custom Components you like

Text

It's just a react component!
----------------------------

Image

![Image 1](https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg)

Text

**ReactPage** has a simple API - it's basically just like a form field and can be included in any project.

Pass it's current `value` that you might read from your datastore and update the value when `onChange` is called. **It's that simple.**

Set `readOnly={true}` whenever you want to display content without editing capabilities. **ReactPage** will only load what is really required for displaying thanks to code splitting. This results in a **small bundle size.**

Code snippet

```tsx
import Editor from '@react-page/editor'

// use ReactPage for editing Content
<Editor
    cellPlugins={yourCellPlugins}
    value={theCurrentValue}
    onChange={newValue => saveTheValue(newValue)}
/>

// or just for displaying content
<Editor
    cellPlugins={yourCellPlugins}
    value={theCurrentValue}
    readOnly={true}
/>
```

Image

Text

Add anything you want
---------------------

Anything can displayed inside a cell of this editor! You can add text, images, videos and any custom Component you want by creating custom `CellPlugins.`

Provide your webmasters a "recommended products" section for your E-Commerce blog. Show a contact form directly inside your content. Embed Tweets and newest posts from Social media.

Anything is possible with a simple, yet powerful API.

You provide a Component and some metadata about your new `CellPlugin`and you are done. If you additionaly provide a schema of the data of this `CellPlugin,`we will **automatically create a form** for you (_powered by_[_Uniforms_](https://github.com/vazco/uniforms)).

Text

Powerful Rich Text editing
--------------------------

We provide a powerful richtext plugin built upon [](https://github.com/vazco/uniforms)[Slate](https://github.com/ianstormtaylor/slate/). It works out-of-the-box, but is fully customizable. You can customize how everything is rendered by providing custom component for headlines, paragraphs, links and so-on and you can add create your own custom plugins to bring in color, add custom links or custom paragraph styles.

Text

_You can customize the rich text editor anyway you like. You can even add formula editing capabilities:_

f(x)=x 2 f(x) = x^2 f(x)=x 2 f(x) = x^2

Text

Embraces Typescript
-------------------

1.   ReactPage is written in modern typescript and enables developer that include ReactPage into their project with typesafety and peace of mind. Thanks to generics, you can give any CellPlugin the data type that you need.

Twitter timeline

#### A Sample Twitter plugin

Code snippet

```tsx
import type { CellPlugin } from '@react-page/editor';
import React from 'react';
import { Timeline } from 'react-twitter-widgets';

type Data = {
  screenName: string;
  height: number;
  title: string;
};
// you can pass the shape of the data as the generic type argument
const customContentPluginTwitter: CellPlugin<Data> = {
  Renderer: ({ data }) => (
    <div>
      <h4>{data.title}</h4>
      <Timeline
        dataSource={{
          sourceType: 'profile',
          // data has already the right type!
          screenName: data.screenName,
        }}
        options={{
          height: data.height || 600,
        }}
      />
    </div>
  ),
  id: 'twitter-timeline',
  title: 'Twitter timeline',
  description: 'A twitter timeline',
  version: 1,
  controls: {
    type: 'autoform',
    schema: {
      // this JSONschema is type checked against the generic type argument
      // the autocompletion of your IDE helps to create this schema
      properties: {
        title: {
          type: 'string',
          default: 'A Sample Twitter plugin',
        },
        screenName: {
          type: 'string',
          default: 'typescript',
        },
        height: {
          type: 'number',
          default: 600,
        },
      },
      required: ['screenName'],
    },
  },
};

export default customContentPluginTwitter;
```

Text

Server Side Rendering out of the box
------------------------------------

**ReactPage**is built with performance in mind. It can be used for **server side rendering (SSR)**, which makes it not only a great tool for editing, but also for displaying. It's battle tested in nextjs, this example itself is created using nextjs and static page generation.

We try **minimize bundle size** as much as possible. Any UI solely used for editing is not loaded when in readOnly mode.

Text

_ReactPage works in any SSR setup like Next.js or Gatsby_

Image

![Image 2](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Nextjs-logo.svg/800px-Nextjs-logo.svg.png)

Spacer

Image

![Image 3](https://www.gatsbyjs.cn/Gatsby-Logo.svg)

undo

redo

zoom in

zoom out

Edit blocks

Add blocks

Move blocks

Resize blocks

Preview page

Reset

* * *

* * *

[Docs](https://react-page.github.io/docs)[Github](https://github.com/react-page/react-page)

* * *

[Demo](https://react-page.github.io/)[Read only](https://react-page.github.io/readonly)[Empty editor](https://react-page.github.io/empty)[React Admin example](https://react-page.github.io/examples/reactadmin)

* * *

[Old demo (v0)](https://react-page.github.io/old/demo)[Old import-from-html-Demo](https://react-page.github.io/old/fromhtml)

* * *

[Latest version](https://react-page.github.io/)[beta version](https://react-page.github.io/beta)

*   Add blocks to page
*     

*    Text
An advanced rich text area. 

*    Spacer
Resizeable, horizontal and vertical empty space. 

*    Image
Loads an image from an url. 

*    Video
Include videos from Vimeo or YouTube 

*    Divider
A horizontal divider 

*    HTML 5 Video
Add webm, ogg and other HTML5 video 

*   C Custom content plugin
Some custom content plugin with multiple controls 

*   C Custom content Plugin shop list
Some custom content plugin with a list field 

*   T Twitter timeline
A twitter timeline 

*   C Code snippet
A code snippet 

*   C Contact form
A simple, configurable contactform 

*    Background
Add background color, image or gradient 

*   C Custom layout plugin
Some custom layout plugin 

*   C Custom layout plugin with initial text
Some custom layout plugin with initial text
