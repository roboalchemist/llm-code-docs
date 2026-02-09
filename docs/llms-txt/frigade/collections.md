# Source: https://docs.frigade.com/platform/collections.md

# Source: https://docs.frigade.com/guides/custom/collections.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Custom Components in Collections

[Collections](/platform/collections) allow you to deploy [Flows](/platform/flows) without having to manually embed them in your app code, which is great! Who doesn't love no-code deploys? But you may be asking "How do I use Custom Components if I'm not rendering React components directly?" Great question, let's dig in to how to use Custom Components in Collections.

To start, let's get a Collection set up with a Custom Flow in it:

<Steps>
  <Step title="Create a &#x22;Macguffins&#x22; Collection">
    In the Frigade web app, [Create a Collection](/platform/collections#creating-a-collection) named "Macguffins".
  </Step>

  <Step title="Create a new Custom Flow">
    1. In the top nav bar, click the "Create" button and select "Custom" from the list of available Flow types.
    2. Use the three dot menu to rename your flow to "The Rug"
    3. In the Advanced Flow editor, replace the default YAML with the following:

    ```yaml  theme={"system"}
    type: macguffin
    title: The Rug
    subtitle: It really ties the room together.
    owner: The Dude
    ```
  </Step>

  <Step title="Add your Flow to the Macguffins Collection">
    1. Select "Collections" in the left nav bar
    2. Click "Macguffins" from the list of Collections
    3. Click "Add Flows" and select "The Rug"
    4. Click "Save Collection" (or press CMD+S)
  </Step>

  <Step title="Embed the Macguffins Collection in your app">
    1. Click "In-App Channel" to show the embed code for your Collection
    2. Paste the embed code into your app
  </Step>
</Steps>

Great! Excellent job so far, you should now have a Collection in your app that does absolutely nothing. But this is a good thing! You've defined a Flow with a `type: macguffin` that's unknown to Frigade -- we don't have a built-in Component in the SDK that matches that Flow type, so there's nothing to render yet.

Let's fix that by wiring up a new `<Macguffin>` Component and registering it with the Frigade `<Provider>` so that we know how to render Flows with `type: macguffin`.

<Steps>
  <Step title="Create a Macguffin Component">
    Paste the following code into `Macguffin.tsx`

    ```jsx  theme={"system"}
    import { Flow, type FlowProps } from '@frigade/react';

    export function Macguffin(props: FlowProps) {
      return (
        <Flow {...props}>
          {({ flow }) => {
            <h3>{flow.title}</h3>
            <p>{flow.subtitle}</p>
            <p>{flow.owner}</p>
          }}
        </Flow>
      )
    }
    ```
  </Step>

  <Step title="Pass your Component into the Provider">
    Add the `flowTypes` prop to `<Frigade.Provider>` to map your new `<Macguffin>` Component to the `macguffin` Flow type

    ```jsx  theme={"system"}
    import * as Frigade from '@frigade/react';

    import { Macguffin } from 'Macguffin.tsx'

    export function App() {
     return (
       <Frigade.Provider apiKey="..." flowTypes={{
         macguffin: Macguffin
       }}>
         {/* ... */}
       </Frigade.Provider>
     )
    }
    ```
  </Step>
</Steps>

That's it, you're done. You should now see your `<Macguffin>` rendering the contents of your Flow. Now that you have it set up, you can deploy any Flow with `type: macguffin` to any Collection.
