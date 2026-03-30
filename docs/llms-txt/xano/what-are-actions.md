# Source: https://docs.xano.com/xano-actions/what-are-actions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Actions

<Frame>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/Ixhk4Sv4mfM?si=YwYfO4stlg9No3M3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

A Xano Action is a powerful, zero-dependency function that anyone can create, share, fork (create new versions), and install. Actions can be previewed, tested, and edited in Run mode outside of a Xano instance, meaning they do not require an account for testing and trying them out.

Actions are a lightweight version of the Xano function stack designed for specific processes such as integrations with external APIs or business logic executions. They are similar to custom functions, but without dependencies and shareable to anyone.

Discover Actions on [xano.com/actions](https://www.xano.com/actions). Browse Actions created by the Xano team or other community members. Clicking on an Action allows you to:

* **Run & Debug** the Action.

* **Make edits** to the Action.

* **Clone**: Make a copy of the Action, change whatever you'd like, and publish a new (separate) version of the Action.

* **Add** the Action into your workspace to be used in any function stack.

### What does zero dependency mean?

Actions are designed not to contain dependencies to support more seamless integration to existing Xano workspaces and function stacks. Additionally, it promotes easy shareability for anyone, regardless of if they're a Xano user, to interact with Actions.

<Info>
  Zero-dependency means Actions do not contain:

  * Database request functions or database tables

  * Middleware

  * Environment variables\*

  * Lambdas

  * Redis caching

  * Multiple Xano objects

  * Docker Microservices

  *\*Settings registry is available for actions for API keys and other sensitive tokens or keys.*
</Info>

### Browsing ans Using Actions

<Steps>
  <Step title="From the left-hand navigation menu, click Actions" />

  <Step title="Browse for and add new actions from here, or at xano.com/actions" />

  <Step title="From any function stack, under the Actions category, you'll see your installed actions available for use">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/137a5e16-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=8954742e24634e4b3e683de0c732330d" width="1136" height="780" data-path="images/137a5e16-image.jpeg" />
    </Frame>
  </Step>
</Steps>

### Creating an Action

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7a132f3d-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=51e2d33fb08fe5b0bd1fb7086d6d19c1" width="1224" height="494" data-path="images/7a132f3d-image.jpeg" />
</Frame>

Click **+ Create Action** to begin building a new Action.

Building a new Action is very similar to building in a[regular Xano function stack.](/the-function-stack/building-with-visual-development#the-anatomy-of-the-visual-builder)

<Info>
  Please note that because Actions are designed to not have dependencies outside of the Action itself, certain functions such as database operations are not available.
</Info>

### Action Settings

Click the three dots in the upper-right corner to access **Action Settings**. From this panel, you can update the following:

**Name** - Give your action a unique name

**Instructions** - You can write documentation to accompany your action here. This field supports markdown for formatting (see below). View the expandable section below for a quick reference.

### Basic Markdown Reference

A quick guide to simple text formatting inside Xano.\
No images or advanced components—just the essentials.

***

## Headings

Use `#` to create headings. More `#` = smaller heading.

# Heading 1

## Heading 2

### Heading 3

#### Heading 4

***

## Paragraphs & Line Breaks

* Leave a blank line between paragraphs.
* Add two spaces at the end of a line for a single line break.

This is a paragraph.

This is another paragraph.\
This line breaks here.

***

## Emphasis

*italic* or *italic*\
**bold** or **bold**\
***bold & italic***\
~~strikethrough~~

***

## Lists

**Unordered list**

* Item one
* Item two
  * Nested item

- You can use asterisks too

**Ordered list**

1. First item
2. Second item
   1. Sub-item
3. Third item

***

## Links

[Link text](https://example.com)

***

## Code

Inline `code` is wrapped in backticks.

You can also preview your instructions using the \*\*Preview \*\*tab.

**Category** - You must provide a category for your Action before publishing

**Video URL** - You can insert a YouTube or Loom video link here to accompany your action

### Action Packages

Packages can be used to bundle and install multiple Actions at once.

<Steps>
  <Step title="Click &#x22;My Packages&#x22; on the left-hand navigation.">
    <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/9448fb13-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=3b447aa51738e0404071c94a3c8e0280" width="132" height="35" data-path="images/9448fb13-image.jpeg" />
  </Step>

  <Step title="Give your package a name, description, and check the other settings in the panel that opens." />

  <Step title="Add Actions to your package by clicking &#x22;Add Actions&#x22;.">
    <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/c95bf0ba-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=411da28be58d7fdffac00595ccb08425" width="108" height="45" data-path="images/c95bf0ba-image.jpeg" />

    You can choose to either copy the action into the package, or move it.

    You can also create new actions at this time specifically for your package.
  </Step>

  <Step title="When your Package is ready, click Publish, and once publishing completes, you can add it to your workspace(s)." />
</Steps>

### Publishing

When you publish your Action, you'll be able to review and make any changes to the documentation and certain Action settings once more before going live.

Make sure to choose the appropriate access level for your Action.

**Public** - This Action will be available for anyone to browse for, install and use.

**Private** - This Action will not be available for distribution. Use this for specific Actions that you only want to use internally.

**Unlisted** - This Action will be available to anyone that has the URL, but will not be found when browsing available Actions.

### Settings Registry

Because Actions have no dependencies, each Action contains a Settings Registry, which is used in a similar manner to [environment variables](/the-function-stack/environment-variables). You will use the Settings Registry for situations where an Action requires an API key or other sensitive data that you need to ensure users of the Action supply without supplying it yourself.

To add a new value to the Settings Registry, just add a new input to your Action. In the settings for that input, you'll see a new option in the **Configuration** section called Settings Registry.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a40769bf-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=a0ec5efb6ab8cf31aacbdbbde7814e2f" width="1440" height="744" data-path="images/a40769bf-image.jpeg" />
</Frame>

Checking this box will mark this input as part of the Settings Registry, enabling you to provide your own data for testing and make sure it is apparent when these values need to be provided for others utilizing the Action you are building.

### Deleting an Action

<Info>
  Please note that deleting an action does not impact users who have already imported your action into their workspace.
</Info>

Click the settings icon in the top-right of your published action, and click Delete Action\*\*.\*\*

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/186a70fa-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=4b0ae022f38a1552297cbba9974eeaed" width="674" height="335" data-path="images/186a70fa-image.jpeg" />
</Frame>

Think of projects as a folder for related actions to reside in. They are necessary for any actions you create, and include a number of helpful features to keep you organized.

### Actions

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/273727de-image.jpeg?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=e8825488af1c1817e40e76ddac18f5a7" width="2304" height="580" data-path="images/273727de-image.jpeg" />
</Frame>

Your project can have multiple Actions inside of it. You can add new actions to a Project by clicking Create Action inside of the Project.

### Members

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b6ba2ca6-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=78a700e0119c5f9bd5f104b27cd789fa" width="2304" height="609" data-path="images/b6ba2ca6-image.jpeg" />
</Frame>

You can invite collaborators to a Project that you own by clicking the **Invite Collaborators** button.

Once you've sent an invite, it will show up on the Members screen, as shown below.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e8e09e2c-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=fa549419998effb2cc998c995eaabcd7" width="1067" height="514" data-path="images/e8e09e2c-image.jpeg" />
</Frame>

The invitee will receive an email similar to the one below allowing them to accept the invitation.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/9ae077e7-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=53cdbc0c65fd199112d7666861321682" width="1306" height="703" data-path="images/9ae077e7-image.jpeg" />
</Frame>

### Settings

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/bfd49fbb-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=b83938c0ef8a3f7cb0b84a4b78a9ded3" width="2304" height="999" data-path="images/bfd49fbb-image.jpeg" />
</Frame>

**Name** - The name of your project

**Custom Project ID** - You can assign a custom ID to your project here. The project ID determines the slug, or portion of the URL, that leads to the project.

**Description** - A description of your project

From this screen, you can also delete your project.

```
```


Built with [Mintlify](https://mintlify.com).