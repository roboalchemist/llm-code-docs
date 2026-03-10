# Source: https://developers.webflow.com/code-components/introduction.mdx

***

title: Code Components
slug: introduction
description: Import reusable React components for use in Webflow via DevLink.
hidden: false
subtitle: Import React components for use in Webflow via DevLink.
canonical-url: '[https://developers.webflow.com/code-components/introduction](https://developers.webflow.com/code-components/introduction)'
-------------------------------------------------------------------------------------------------------------------------------------------

DevLink lets you import code components directly to Webflow, bridging the gap between code and visual development. Build advanced, interactive components in your codebase, and deploy them to Webflow. In Webflow, use code components directly on the canvas with props, slots, and variants for flexible composition.

***

### Get started

<CardGroup columns={2}>
  <Card
    title="Quick start"
    href="/code-components/introduction/quick-start"
    iconPosition="left"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/PublishMarketing.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/PublishMarketing.svg" alt="" className="light-icon" />
            </>
        }
  >
    Create a code component and share an example library to your workspace
  </Card>

  <Card
    title="Configure your codebase"
    href="/code-components/installation"
    iconPosition="left"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/ComponentsCode.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/ComponentsCode.svg" alt="" className="light-icon" />
            </>
        }
  >
    Update your existing library to work with DevLink and code components
  </Card>
</CardGroup>

***

## Key capabilities

With code components, you get full control over your React development:

* **Develop in React** <br />
  Use hooks, state, effects, and context to build advanced components
* **Visual composition** <br />
  Expose props and slots for designers to design visually in Webflow
* **Shared library distribution** <br />
  Share, update, and install code components on any site in your Workspace with Libraries

[Learn more about configuring your components for Webflow →](/code-components/define-code-component)

***

## How code components work in Webflow

{/* TODO: Add a diagram showing the flow from codebase → CLI → Webflow → Canvas. */}

{/* <!-- vale off --> */}

<Steps>
  <Step title="Build components in your codebase">
    Create React components with hooks, state management, and API integrations. Reference Webflow variables to allow components to adapt to an individual site's colors, typography, sizes, and spacing.
  </Step>

  <Step title="Declare a Webflow component in your codebase">
    Use `declareComponent` to wrap an existing React component, then define [prop types](/code-components/reference/prop-types) to make them available in the Webflow Designer.
  </Step>

  <Step title="Import components to Webflow">
    Use [DevLink](/devlink) to bundle and publish your components as a shared library for users to install across a workspace.
  </Step>

  <Step title="Install components to a site">
    Install code components as a [shared library](https://help.webflow.com/hc/en-us/articles/33961343551763-Libraries) on any Webflow site in your workspace.
  </Step>

  <Step title="Design visually">
    Drag and drop components onto the canvas, configure props and slots in the right panel, and customize styling through each site's variables to integrate with a specific design system.
  </Step>
</Steps>

{/* <!-- vale on --> */}
