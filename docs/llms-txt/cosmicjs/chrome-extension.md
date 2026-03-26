# Source: https://www.cosmicjs.com/docs/chrome-extension.md

# Cosmic Chrome Extension

The [Cosmic Chrome Extension](https://chromewebstore.google.com/detail/cosmic-chrome-extension/ooihoppnbephpmmpiadjmpeicihmjong) is a tool that allows you to easily access your Cosmic content from your Cosmic powered website.

## How it works

This extension automatically highlights areas on the page that can be edited in the Cosmic CMS, and will provide a link directly to the Cosmic dashboard for easy editing access.

## How to install

1. Go to the [Cosmic Chrome Extension on the Chrome Web Store](https://chromewebstore.google.com/detail/cosmic-chrome-extension/ooihoppnbephpmmpiadjmpeicihmjong)
2. Click "Add to Chrome"
3. Click "Add extension"
4. After installing the Cosmic Chrome Extension, you will then need to configure your Bucket slug. Click on the Cosmic icon located in the top right of your Chrome browser. Set your Bucket slug (this can be found in Your Project > API access). Then set edit mode to On.

## Demo

After installing the extension, go to the [Cosmic Podcast Network](https://cosmic-podcast-network.vercel.app) and click the Cosmic icon in the top right of your browser to open the Cosmic Chrome Extension.

## How to use

1. **Codebase updates**
In your website codebase, around any element that can be edited in Cosmic, set an attribute for `data-cosmic-object="your-cosmic-object-id"`. You can find the Cosmic Object ID in the API response or in the Cosmic dashboard. See the [Objects section in the docs](/docs/api/objects) section for more info.

2. **Install and configure**
After installing the Cosmic Chrome Extension, you will then need to configure your Bucket slug. Click on the Cosmic icon located in the top right of your Chrome browser. Set your Bucket slug (this can be found in Your Project > API access). Then set edit mode to On.

3. **Testing**
Now you should see any element with a Cosmic Object ID lit up with a Cosmic blue border with a link that takes you directly to the area in the Cosmic dashboard to update the content.