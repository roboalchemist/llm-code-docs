# Source: https://docs.chatling.ai/web-widget/installation/shopify.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Shopify

> Learn how to add Chatling to your Shopify store

## Method 1: Using theme.liquid

1. Go to your dashboard.
2. Click `Deploy` button in the sidebar menu.

<img src="https://chatling-assets.b-cdn.net/deploy-ai-agent.jpg" width="500" alt="Open Deploy page" />

3. Click the `Manage` button under the `Website Widget` option.

<img src="https://chatling-assets.b-cdn.net/manage-website-widget-chatbot.jpg" width="600" alt="Manage website widget" />

4. Design the appearance of the widget by clicking the `Open widget designer` button.

<img src="https://chatling-assets.b-cdn.net/open-website-widget-designer.jpg" width="500" alt="Open website widget designer" />

5. Select the display mode for your chatbot, such as "Floating Chat", "Inline", or "Fullscreen".

<img src="https://chatling-assets.b-cdn.net/configure-website-widget-display-type.jpg" width="500" alt="Configure website widget display type" />

6. Copy the widget code.

<img src="https://chatling-assets.b-cdn.net/website-widget-code.jpg" width="500" alt="Copy widget code" />

7. Go to your Shopify dashboard and click on `Online Store` from the sidebar.

<img src="https://chatling-assets.b-cdn.net/8b3114ad-4b34-49c1-b24f.jpg" width="350" />

8. Edit your theme by clicking the ellipsis icon next to your current theme and choosing `Edit code`.

<img src="https://chatling-assets.b-cdn.net/3e16b15a-6bc5-45c3-bf8e.jpg" width="600" />

9. Find and open the `theme.liquid` file From the sidebar where the list of files is displayed.

<img src="https://chatling-assets.b-cdn.net/48cde0d8-f309-4c73-97aa.jpg" width="250" />

10. Paste the widget code in the `<head>` section. You can paste it anywhere between the opening `<head>` tag and the closing `</head>` tag.

<img src="https://chatling-assets.b-cdn.net/12378539-03e7-4e2a-88ca.jpg" width="600" />

11. Click the Save button.

The chatbot will be live on your website and should appear across all your store's pages.

<img src="https://chatling-assets.b-cdn.net/70e38199-d0e9-4d6b-a77e.jpg" width="600" />

## Method 2: Using Customization

1. Follow steps 1-6 from Method 1 to copy the widget code.

2. From your Shopify dashboard, click on `Online Store` and go to `Themes`.

<img src="https://chatling-assets.b-cdn.net/open-themes-shopify.jpg" width="350" />

3. Click on the `Customize` button next to your current theme.

<img src="https://chatling-assets.b-cdn.net/click-customize-theme-shopify.jpg" width="600" />

4. Under the `Header` section, choose `Add section`. Search for `Custom liquid` and add it.

<img src="https://chatling-assets.b-cdn.net/add-custom-liquid-shopify.jpg" width="500" />

5. Open the `Custom liquid` editor and paste your widget code into the `Liquid code` field.

<img src="https://chatling-assets.b-cdn.net/add-chatling-widget-code-to-custom-liquid.jpg" width="350" />

6. Set the `Top padding` and `Bottom padding` to `0` so the section doesn't create a blank space in your site's header.

<img src="https://chatling-assets.b-cdn.net/set-padding-to-zero-shopify-custom-liquid.jpg" width="350" />

7. Click the `Save` button.

The widget will be live on your website and should appear across all your store's pages.

<img src="https://chatling-assets.b-cdn.net/shopify-chatbot-preview-using-custom-liquid.jpg" width="600" />
