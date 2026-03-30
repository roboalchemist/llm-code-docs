# Source: https://developers.webflow.com/devlink/docs/component-export.mdx

***

title: Component Export
description: Bridge design and code by exporting Webflow components to React applications.
subtitle: 'Design in Webflow, export to React'
----------------------------------------------

With DevLink, you can export Webflow designs directly to React. Designers create reusable components visually in Webflow, and developers use DevLink to bring those components into React projects, including Webflow Cloud apps, with ease.

<CardGroup cols={2}>
  <Card
    title="Design visually"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Favicon.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Favicon.svg" alt="" className="light-icon" />
      </>
    }
  >
    Create components using Webflow's visual editor with no code required.
  </Card>

  <Card
    title="Export to React"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/ComponentsCode.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/ComponentsCode.svg" alt="" className="light-icon" />
      </>
    }
  >
    Transform Webflow components into React components with a single command.
  </Card>

  <Card
    title="Preserve design systems"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Styles.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Styles.svg" alt="" className="light-icon" />
      </>
    }
  >
    Preserve styles, variables, components and interactions from your Webflow design.
  </Card>

  <Card
    title="Stay in sync"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DevLink.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DevLink.svg" alt="" className="light-icon" />
      </>
    }
  >
    Update your design system in Webflow, then sync changes to your codebase.
  </Card>
</CardGroup>

***

## Get started with Exported Components

<Card
  title="Get Started"
  iconPosition="left"
  iconSize="12"
  icon={
  <>
    <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CirclePlay.svg" alt="" className="dark-icon" />
    <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CirclePlay.svg" alt="" className="light-icon" />
  </>
}
>
  Follow the [Getting Started](/devlink/docs/quick-start/quick-start-component-export) guide to configure your project for DevLink and export your components.

  <br />

  <div>
    <Button href="/devlink/docs/quick-start/quick-start-component-export">
      Get Started
    </Button>
  </div>
</Card>

***

## Working with Exported Components

DevLink translates your Webflow components into React components through a simple workflow:

<Steps>
  <Step title="Design in Webflow">
    Create styles, variables, and components in Webflow's best-in-class visual editor.
  </Step>

  <Step title="Configure DevLink">
    [Set up the connection](/devlink/docs/component-export/installation) between your Webflow project and your React application.
  </Step>

  <Step title="Sync your design system">
    Use the Webflow CLI to export and [sync styles, variables, and components](/devlink/docs/component-export/whats-exported) to your project.
  </Step>

  <Step title="Use your design system in your React app">
    Import the global styles and generated React components into your application code.
  </Step>

  <Step title="Add functionality">
    Enhance the components with [custom logic, state, and interactivity.](/devlink/usage/framework-guides)
  </Step>
</Steps>

## Learn more

Explore to use Exported Components in your React projects:

<CardGroup cols={2}>
  <Card
    title="Design Guidelines"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/DevLink.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/DevLink.svg" alt="" className="light-icon" />
      </>
    }
    href="/devlink/docs/component-export/design-guidelines/component-architecture"
  >
    Learn how to structure and design components in Webflow for clean export to React.

    <br />

    <Button href="/devlink/docs/component-export/design-guidelines/component-architecture">
      Learn more
    </Button>
  </Card>

  <Card
    title="Usage Documentation"
    iconPosition="left"
    iconSize="12"
    icon={
    <>
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/ComponentsCode.svg" alt="" className="dark-icon" />
      <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/ComponentsCode.svg" alt="" className="light-icon" />
    </>
  }
    href="/devlink/usage/framework-guides"
  >
    Discover how to integrate and extend DevLink components in your React projects.

    <br />

    <Button href="/devlink/usage/framework-guides">
      Learn more
    </Button>
  </Card>
</CardGroup>
