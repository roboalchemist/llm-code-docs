# Source: https://developers.webflow.com/designer/reference/introduction.mdx

***

title: Introduction
slug: designer/reference/introduction
description: >-
Webflow's Designer APIs let you build apps that programmatically control the
Webflow Designer.
hidden: false
layout: overview
hide-toc: true
'og:title': Webflow's Designer APIs
'og:description': >-
Webflow's Designer APIs let you build apps that programmatically control the
Webflow Designer.
'og:keywords': Webflow API
--------------------------

<video autoplay loop muted>
    

  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_Introduction_v3_24fps.webm" type="video/webm" />

    Your browser does not support HTML video.
</video>

Webflow's Designer APIs let you build apps that programmatically control the Webflow Designer. With these APIs, developers can create tools that automatically add elements to pages, apply styles, manage components, and streamline design workflows.

<br />

## Getting started

To start using the Designer APIs, [register a Webflow App](/data/docs/getting-started-apps) and create a [Designer Extension](/designer/docs/getting-started-designer-extensions) using the [Webflow CLI.](/designer/reference/webflow-cli) Once you have your Designer Extension running locally on a Webflow project, you can start using the Designer APIs to create elements, styles, components, and more.

<CardGroup>
  <Card
    title="Create your first extension"
    iconPosition="left"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/App.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/App.svg" alt="" className="block dark:hidden" />
        </>
    }
    href="/designer/docs/getting-started-designer-extensions"
  >
    Follow our step-by-step guide to build and deploy your first Designer Extension<br /><br />

    <a href="/designer/docs/getting-started-designer-extensions">
      <button class="cc-primary">
        Create a Designer Extension
      </button>
    </a>
  </Card>

  <Card
    title="Try the interactive playground"
    iconPosition="left"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/PublishDesigner.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/PublishDesigner.svg" alt="" className="block dark:hidden" />
        </>
    }
    href="https://webflow.com/oauth/authorize?response_type=code&client_id=19511de1ec410f9228d8dcbc9420e67916dea80d86d18f0c9a533eb475ea0f62"
  >
    Experiment with live API calls in our interactive playground environment<br /><br />
    <button class="cc-primary">Test the API playground</button>
  </Card>
</CardGroup>

<br />

## Working with the Designer APIs

The Designer APIs provide several objects and methods that give Apps control over the Webflow Designer. Each object serves a specific purpose and contains methods to help you design automated workflows for teams working in Webflow.

<CardGroup>
  <Card
    title="Elements"
    href="/designer/reference/elements-overview"
    iconPosition="left"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Grid.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Grid.svg" alt="" className="block dark:hidden" />
        </>
    }
  >
    Create and manipulate elements on the canvas, including their properties, content, and styles.
  </Card>

  <Card
    title="Styles"
    href="/designer/reference/styles-overview"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Styles.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Styles.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Manage reusable CSS classes to control the visual appearance of elements across your site.
  </Card>

  <Card
    title="Components"
    href="/designer/reference/components-overview"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Components.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Components.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Create and modify reusable element groups to maintain consistency across your designs.
  </Card>

  <Card
    title="Variables"
    href="/designer/reference/variables-overview"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Variable.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Variable.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Define and manage global values for numbers, percentages, sizes, colors, and fonts.
  </Card>

  <Card
    title="Pages"
    href="/designer/reference/pages-overview"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/PageBuilding.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/PageBuilding.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconPosition="left"
    iconSize="12"
  >
    Manage page properties, SEO settings, and site structure.
  </Card>

  <Card
    title="Extension Utilities"
    href="/designer/reference/extension-utilities"
    iconPosition="left"
    iconSize="12"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/ToolNut.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/ToolNut.svg" alt="" className="block dark:hidden" />
        </>
    }
  >
    Utility methods to manage your extension's behavior and interaction with the Designer.
  </Card>
</CardGroup>

<br />

## How the Designer APIs work in Webflow

Designer APIs are client-side JavaScript APIs that execute in the browser via an iframe. They interact with Webflow just as a user would - creating elements, applying styles, and modifying properties. This client-side approach allows your apps to directly manipulate the Designer interface in real-time, creating a seamless integration between your code and the Webflow environment.

To work with objects in your Webflow project, you'll need to reference the object using an appropriate method, and then make changes using the available methods.

<Tabs>
  <Tab title="Referencing objects">
    * **Existing Objects:** Get an existing object using an appropriate **GET** method. For example, to get the currently selected element, you can use the [`webflow.getSelectedElement()`](/designer/reference/get-selected-element) method. You can see all the methods available for retrieving objects in the [Designer API Reference](/designer/reference/elements-overview).

    * **New Objects:** Create a new object using an appropriate **CREATE** method. When you create a new object, Webflow will always return a reference to the new object. For example, to create a new element, you can use the [`element.after()`](/designer/reference/insert-element-after) method. You can see all the methods available for creating objects in the [Designer API Reference](/designer/reference/elements-overview).

    <div>
      <Frame background="subtle" caption="`webflow.getSelectedElement()` returns a reference to the currently selected element.">
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/17d1ef94bda2296a5c365947d98c551f101ba498801c0abb42850a93982accb3/assets/images/26ae3a1-Getting_a_reference_to_a_resource.png" alt="Getting a reference to a resource" />
      </Frame>
    </div>
  </Tab>

  <Tab title="Modifying objects">
    Once you've referenced an object, you can start manipulating it using the available methods on that object. Each object has its own set of methods, so be sure to refer to the [Designer API Reference](/designer/reference/elements-overview) for the object you're working with.

    In the example below, we're using the [`element.setCustomAttribute()`](/designer/reference/custom-attributes/setCustomAttribute) method to set a custom attribute on the element. When the custom attribute is set, the element will be updated in the Webflow Designer, and the information about the updated object will be returned to the Designer Extension.

    <div>
      <Frame background="subtle" caption="`element.setCustomAttribute()` sets a custom attribute on the element, then sends the updated object back to the Designer Extension.">
        <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/3b78ee45acd2c5a5b79458bd1f6b77277e8534b706c1130f5a0d53d8f11555fb/products/designer/pages/DEsignerAPI/assets/saving-changes-to-a-resource.png" alt="Saving changes to an element" />
      </Frame>
    </div>
  </Tab>
</Tabs>
