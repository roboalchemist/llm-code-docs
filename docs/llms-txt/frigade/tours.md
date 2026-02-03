# Source: https://docs.frigade.com/guides/tours.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Guide: Product Tours & Hints

<Frame caption="An example of a <Frigade.Tour/>">
  <img src="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=f155b1d2d3b4965cd228c8a2c127c48a" className="h-96" data-og-width="1980" width="1980" data-og-height="2010" height="2010" data-path="images/tours-tooltip-basic.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=280&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=77320f2da88bea5507059f72c476e6c8 280w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=560&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=3f9c18d20127c192c926be55153a57e8 560w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=840&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=5f0c74b38d9d16bd58e7e8887af25e8d 840w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=1100&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=512cdff16492459bab879079990ffe43 1100w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=1650&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=ec95265aa1f3458ac8b90c81b2ad280e 1650w, https://mintcdn.com/frigade-docs/vb0YqHQGpTytLgI7/images/tours-tooltip-basic.png?w=2500&fit=max&auto=format&n=vb0YqHQGpTytLgI7&q=85&s=aad9484870af39b58cfcca4b21881127 2500w" />
</Frame>

## In this guide

1. [Adding a Tour to your application](#adding-a-tour-to-your-application)
2. [Adding Hints to your application](#adding-hints-to-your-application)
3. [Tips and tricks](#tips-and-tricks)

## Adding a Tour to your application

<Steps>
  <Step title="Create a Tour">
    In the Frigade Dashboard, create a new [Tour](https://app.frigade.com/prod/components/tour).
  </Step>

  <Step title="Find your Step anchors">
    Pick out the elements in your application that you want to attach individual Steps to.

    <Info>Each Step in a Tour uses a [CSS Selector](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors) to attach itself to the element in your page that you want to highlight. We recommend adding a unique `id` to your element to ensure that Frigade can find it.</Info>

    ```tsx  theme={"system"}
    <span id="my-element">
      This is the element that we're going to attach a Tour Step to.
    </span>
    ```
  </Step>

  <Step title="Configure your Flow">
    In the Frigade Dashboard, use the `selector` property in each step of your Tour to highlight the desired element in your application:

    ```yaml  theme={"system"}
    steps:
      - title: "Welcome to Frigade!"
        description: "This is a tour of the Frigade platform."
        selector: "#my-element"
    ```
  </Step>

  <Step title="Embed the Tour Component">
    Add the [Tour](/component/tour) Component to your application with its corresponding Flow ID.

    ```tsx  theme={"system"}
    <Frigade.Tour flowId="flow_Bkh43aEjXcrna2lO" />
    ```
  </Step>
</Steps>

## Adding Hints to your application

<Steps>
  <Step title="Create some Hints">
    In the Frigade Dashboard, create new [Hints](https://app.frigade.com/prod/components/hints).
  </Step>

  <Step title="Find your Hint anchors">
    Pick out the elements in your application that you want to attach individual Steps to.

    <Info>Each Hint uses a [CSS Selector](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_selectors) to attach itself to the element in your page that you want to highlight. We recommend adding a unique `id` to your element to ensure that Frigade can find it.</Info>

    ```tsx  theme={"system"}
    <span id="my-element">
      This is the element that we're going to attach a Hint to.
    </span>
    ```
  </Step>

  <Step title="Configure your Flow">
    In the Frigade Dashboard, use the `selector` property in each Hint to highlight the desired element in your application.

    ```yaml  theme={"system"}
    steps:
      - title: "Welcome to Frigade!"
        description: "This is a tour of the Frigade platform."
        selector: "#my-element"
    ```
  </Step>

  <Step title="Embed the Tour Component">
    No, that's not a typo, Hints are actually a specially configured `<Frigade.Tour>`!

    ```tsx  theme={"system"}
    <Frigade.Tour
      flowId='flow_Bkh43aEjXcrna2lO'
      sequential={false} // Show all Steps at once
      defaultOpen={false} // Only show Hint markers
    />
    ```
  </Step>
</Steps>

## Tips and tricks

### Seamless navigation between pages

One of the benefits of Frigade is that it can tap into your existing router to navigate users across pages without janky page refreshes. Check out our guide on [Navigation](/sdk/navigation) for setup.

### Debugging Steps

If a Step in a Tour is not appearing when you expect it to, you can enable debugging by enabling Verbose logging in your browser. To enable this in Chrome Devtools, simply click the three dot menu in the console as shown below:

<Frame caption="Enabling verbose logging in Chrome Devtools">
  <img src="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=2cb121c8d0f6d50b0ef13854c4e88cc5" className="h-96" data-og-width="747" width="747" data-og-height="518" height="518" data-path="images/guides/tours/debug.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=280&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=87a7d41c953e184c6a6516a3f5e885d6 280w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=560&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4abbb3951dc9331370a6f6b4b617277c 560w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=840&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=3a0001bebc5a08f2775d501d9f74eafe 840w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=1100&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=689d603f223b048760769c4add41fa1b 1100w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=1650&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=4436c048e73e7919f760018e1ee60405 1650w, https://mintcdn.com/frigade-docs/2ELnoUYc9O4Ydjzw/images/guides/tours/debug.png?w=2500&fit=max&auto=format&n=2ELnoUYc9O4Ydjzw&q=85&s=5791ff4778ba19a1c93463807329259f 2500w" />
</Frame>

This will log if a selector is not found on the current page.

### Controlling the z-index of Steps

By default, Steps are rendered with a z-index of 9999. To change this, you can use the `zIndex` prop on a Tour:

```tsx  theme={"system"}
<Frigade.Tour flowId="my-flow-id" zIndex={100} />
```

Or alternatively, you can override the z-index for a specific Step directly in the YAML config using the `zIndex` property:

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: My subtitle
    primaryButton:
      title: Got it
    selector: "#my-tour-step-anchor"
    props:
      zIndex: 42
```

### Overriding position for a specific Step

If you want to force a specific Step to show up on the left or right side of the targeted element, you can use the `align` and `side` properties in Config YAML to override the default positioning.
It follows the same syntax as the [align and side props](/component/tour#align) on the `Tour` component.

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: This Step will show up on the left of the target element, after its trailing edge
    primaryButton:
      title: Got it
    selector: "#my-tour-step-anchor"
    props:
      align: after
      side: left
```

### Offset x and y positioning

You can add a custom offset to the x and y positioning of each Step in a Tour using the `sideOffset` and `alignOffset` properties (see [Tour component documentation](/component/tour)).
Alternatively, you can override the offset for a specific Step directly in the YAML config by leveraging the `props` field:

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: My subtitle
    primaryButton:
      title: Got it
    selector: "#my-tour-step-anchor"
    props:
      sideOffset: 10
      alignOffset: -10
```

### Hiding CTA buttons

Sometimes you may want to hide the CTA button on a single Step for a user to take an action in your application rather than simply continuing the tour on every button click. To do this, simply omit the `primaryButton.title` property in the YAML config:

```yaml  theme={"system"}
steps:
  - id: my-tour-step
    title: My title
    subtitle: My subtitle
    # Omitting primaryButton.title will hide the CTA button
    # primaryButton:
    #   title: Got it
    selector: "#my-tour-step-anchor"
```

### Programmatically completing a step

If you want too programmatically complete the step (e.g. an action in your app advances the Flow), see the documentation for automatically [advancing a Flow](/sdk/advanced/completing-a-step).
