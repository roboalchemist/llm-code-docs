# Source: https://posthog.com/docs/product-tours/creating-product-tours.md

# Create product tours - Docs

**Product tours is in private alpha**

Product Tours is currently in private alpha. [Share your thoughts](https://app.posthog.com/external_surveys/019af5f5-a50e-0000-b10f-e8c30c0b73a0) and we'll reach out with early access.

**Currently only available on the web. Requires `posthog-js` >= v1.324.0.**

Product tours are multi-step walkthroughs that highlight elements in your UI. You build them visually using the PostHog toolbar directly on your site.

## Create a new tour

1.  Go to [Product tours](https://app.posthog.com/product_tours) in PostHog
2.  Click **New** and select **Product tour**
3.  Enter a name for your tour and click **Create**

After creation, you're taken to the tour editor where you can start building your tour.

## Define your tour steps

The Toolbar is where you'll build the "skeleton" of your tour. Create steps, optionally attached to elements on your page, and configure some basic settings for them.

![Product Tour Toolbar editor](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_05_at_10_04_48_PM_129f5894c4.png)![Product Tour Toolbar editor](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_05_at_10_04_17_PM_a56ff45a20.png)

When attaching elements to steps, you'll be able to choose between **Auto** and **Manual** targeting.

-   **Auto**: Click your element and we'll collect data about it so we can reliably find it again during tours.
-   **Manual**: Provide a CSS selector for us to target the element.

To learn more about auto vs. manual element targeting, see [Element selection](/docs/product-tours/element-selection.md).

**Tip:** If the sidebar overlaps with elements on your site, click the toggle button in the sidebar header to move it to the left or right side of the screen.

### Record your session (optional)

When you first open the toolbar, you'll see a modal asking if you want to enable session replay. If you opt in, PostHog records your DOM interactions while you build the tour – not your screen, camera, or other tabs. This helps us understand how you build product tours so we can build a better product!

The recording respects any `.ph-no-capture` privacy markers on your site. All inputs are masked by default.

## Edit step content

After defining your tour structure in the toolbar, edit step content (text, formatting, images) in the main PostHog app.

Tour-wide settings like styling and display conditions are available in the right panel.

Below the content editor, you'll find step-specific settings like button configuration and targeting precision.

![Product Tour editor](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_05_at_10_00_11_PM_d3f39b13c4.png)![Product Tour editor](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_05_at_9_59_06_PM_bcf1538067.png)

## Step progression

Steps can progress via buttons or when the user clicks the target element. Guide users through real interactions, not just info.

## Step types

### Pop-up steps

The default. Show a tooltip with your content, positioned anywhere on the screen or attached to a particular element on the page.

![Pop-up step example](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_05_at_9_43_34_PM_3f352cf68b.png)

### Survey steps

Embed a survey question mid-tour (open text or rating scale). Responses are captured as events.

![Survey step example](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2026_02_05_at_10_02_02_PM_e335e8f0bb.png)

## Save and launch

Changes auto-save as you edit. A status indicator in the header shows whether your changes are **unsaved**, **saving**, or **saved**.

When you're done, click **Save** to publish your changes or **Cancel** to discard the draft. When ready, [launch the tour](/docs/product-tours/managing-tours.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better