# Source: https://redocly.com/docs/realm/customization/eject-components/eject-components-tutorial.md

## Eject components tutorial

### Update tabs component behavior

Let's imagine you are writing a tutorial describing how to write code to work with your product.
You decided to use Redocly's [tabs](https://redocly.com/learn/markdoc/tags/tabs) Markdoc tag to show code examples in different languages.
As you are working, you decide it would be nice if a user could select their preferred programming language once triggering the update of all other tabs on the page to the selected programming language.

But you notice, the Redocly [tabs](https://redocly.com/learn/markdoc/tags/tabs) Markdoc tag, does not have the ability to configure syncing between tabs.
So you decide to eject the component to update the behavior to allow configuring syncing between tabs.

Tabs without syncing
### Eject the tabs component in Reunite

For this tutorial we are going to eject the component using the [Reunite editor](/docs/realm/customization/eject-components/eject-components-in-reunite).
To eject the component using the Reunite editor:

1. Select **Editor** on the left side navigation.
2. Click the **Theme components** in the **Files** section.
3. Search for **tabs**.
4. Find the **Tabs.tsx** component and click the eject icon.


Eject tabs component
After ejecting, the component is added to the `@theme` folder at the path `@theme/markdoc/components/Tabs/Tabs.tsx` where we can modify it.

### Implement `useTabs` hook

Create a new `useTabs.ts` file adjacent to the `Tabs.tsx` file and copy the code from the example.
You can also download all examples and drag and drop them to the `@theme/markdoc/components/Tabs` folder.

This custom hook reuses the original `useTabs` hook and adds syncing functionality between tabs with the same `syncId`.
It stores the `activeTab` state in `localStorage` after an update was triggered, and all other tabs are subscribed to the storage events to update their state.
Also, for initial mount, it gets the `activeTab` from `localStorage` to preserve the tabs state even after a page is reloaded.

This tutorial does not provide step-by-step instructions for every customization.
Each case is unique and requires a different approach.
React, Markdoc and TypeScript knowledge is required to customize it.

### Replace the `useTabs` hook inside the Tabs component

Replace the original `useTabs` hook import with the custom hook.

Extend the `TabsProps` interface to include the `syncId` prop.

Add the `syncId` prop to the `Tabs` component.

And finally, pass the `syncId` prop to the `useTabs` hook.

### Extend the tabs Markdoc schema

We also need to update the tabs interface to be able to pass the `syncId` prop to the `tabs` Markdoc component, which passes the `syncId` to our modified `Tabs` React component.

#### Eject the tags Markdoc schema

1. Select **Editor** on the left side navigation.
2. Click the **Theme components** in the **Files** section.
3. Search for **tabs**.
4. Find the **tabs.ts** tag and click the eject icon.


Add the `syncId` Markdoc attribute to the `tabs` tag.

To fix a warning, let's redefine our Markdoc schema.
Create a new `schema.ts` inside the `@theme/markdoc` folder and copy the code from the example.

### Create a tutorial page

To test our changes, let's create a `tutorial.md` page in the root of the project and copy the code from the example.

Your file structure should look like this:


```treeview Example of ejected components and a tutorial page
âââ @theme/
â   âââ markdoc/
â       âââ components/
â       â   âââ Tabs/
â       â       âââ Tabs.tsx
â       â       âââ useTabs.ts
â       âââ tags/
â       â   âââ tabs.ts
â       âââ schema.ts
âââ tutorial.md
```

Since we added `syncId` attributes to the `tabs` tags, we can sync the tabs state between those tabs with the same `syncId`.

Test it out.
Do the tabs sync?

### ð Congratulations

You have successfully ejected the `Tabs` component and added custom functionality to it.
Don't forget, with great power comes great responsibility, now you are responsible for maintaining the component ð.