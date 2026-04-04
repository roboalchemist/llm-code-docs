# Source: https://docs.base44.com/Building-your-app/NPM-packages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Adding and using npm packages

> Extend your app with pre-built code libraries.

## What are npm packages?

Use npm packages to add powerful features and tools to your Base44 applications without having to build everything yourself. You can access reliable, up-to-date code libraries for things like animations, data formatting, and charts, all created by expert developers.

When you use npm packages, you can add advanced features in minutes, rely on well-tested code, and focus on creating what makes your app unique.

<Tip>
  Think of npm packages as little boxes of ready-made code you can plug into your app. Someone else already wrote the code. You just need to install the package and can use all its abilities instantly.
</Tip>

Base44 makes it simple to add npm packages to your app. You can request to add npm packages, review the request, and approve installation, all from the AI chat inside your app editor.

<Card title="Examples of npm packages" icon="display-code">
  * Animation libraries (for example, anime.js)
  * Chart and graph utilities
  * Date and time helpers
  * UI components
  * Drag and drop logic
</Card>

<Warning>
  **Important:**

  All npm packages are created and maintained by third parties. Base44 can’t guarantee the quality, reliability, or security of any external package you install. Always test and validate packages carefully to make sure they work correctly in your app. You are responsible for ensuring that any third-party packages you use meet your project’s needs.
</Warning>

***

## Browsing npm packages

You can find npm packages in the public registry. Each package README includes detailed instructions, usage examples, and peer dependency details, so you can get started right away.

<Tip>
  Use the Base44 [**npm Playground**](https://NPM-Playground.base44.app) to preview npm packages in action and plug them directly into your app.
</Tip>

**To browse Base44 npm packages:**

1. Go to [npmjs.com](https://npmjs.com) to see all available public packages.
2. Click the package you want to use to open its details page.

***

## Adding an npm package to your app

In Base44, you can add npm packages by chatting with the AI. No terminal or manual install commands required.

**To add an npm package to your app:**

1. Go to your app editor.
2. Type in the AI chat the npm package you want to install.
3. When prompted, click **Approve** in the chat.

<Frame caption="The approval window in the AI chat when installing an npm package">
    <img src="https://mintcdn.com/base44/rGwyblVsd7gmCHCl/images/2025-12-03_10-10-11.png?fit=max&auto=format&n=rGwyblVsd7gmCHCl&q=85&s=eeb08663a96f3f5d8842ca2b1f928e13" alt="The approval window in the AI chat when installing an NPM package" width="541" height="207" data-path="images/2025-12-03_10-10-11.png" />
</Frame>

***

## Example of using an npm package

You can use anime.js to create polished entrance animations for your app’s pages and elements. For example, you might want to animate cards, buttons, or charts when a page loads to make your site feel more engaging.

Simply add a prompt such as:

```
Install the npm anime.js and make my app beautiful
```

The AI chat will ask you to approve the installation and the package is installed right into your app.

<Frame caption="Installing an npm package to your app in Base44">
  <img src="https://mintcdn.com/base44/EeT5kuySWp78z63R/images/anima.png?fit=max&auto=format&n=EeT5kuySWp78z63R&q=85&s=e9e48e44298455724c1ddefe6f9f9c19" alt="Installing an NPM package to your app in Base44" title="Installing an NPM package to your app in Base44" style={{ width:"87%" }} width="943" height="949" data-path="images/anima.png" />
</Frame>

Once it is installed, you can use anime.js to animate page sections, icons, and more.

***

## FAQs

Click a question below to learn more.

<AccordionGroup>
  <Accordion title="Is there an official Base44 SDK?">
    Base44 does not currently offer a public SDK. However, you can vote for this feature on our [Product Roadmap](https://feedback.base44.com/roadmap/main?q=sdk).

    For advanced developers, the `npm-base44/sdk` package is available. This package allows you to perform specific backend functions.
  </Accordion>

  <Accordion title="Why am I getting errors when installing npm packages?">
    Npm packages are only supported on [the new Base44 infrastructure](https://docs.base44.com/Building-your-app/Update-to-new-infrastructure). If you are encountering errors, **make sure to update your app** to the new infrastructure.

    **To check if you need to update:**

    1. Go to your app editor.
    2. Look for the **Update Infrastructure** button in the top bar.
    3. Click **Update Infrastructure** if you see it and follow the prompts.

    **Note:** If you do not see the **Update Infrastructure** button, you are already using the new infrastructure.
  </Accordion>

  <Accordion title="What should I do if an NPM package fails to install?">
    If your npm package does not install or gets stuck on pending, try these steps:

    1. Check the chat messages for error details. Sometimes, the AI chat will explain about dependency or compatibility issues with the package you are requesting to install.
    2. Make sure your request matches the exact package name and version.
    3. If install requires approval, verify that you have approved the request in the chat panel.
    4. If the install fails, try re-requesting the package using the chat.
  </Accordion>

  <Accordion title="Can I remove or update a package after installing it?">
    Once you have added an npm package, you cannot remove it from your app. However, if you are not using an npm package in the code but have it installed, it has no affect on your app. 

    If an npm package needs updating, you can simply ask the AI chat to do it for you.
  </Accordion>

  <Accordion title="Can I see which packages are installed?">
    To find out which npm packages you have installed on your app, you can ask the AI chat.
  </Accordion>

  <Accordion title="How can I choose reliable npm packages?">
    Choose the right npm packages by following the recommendations below. Doing a little research on each package, instead of installing it immediately, can help you find reliable options and prevent issues down the line.

    * **Download statistics:** Look up how many downloads the package has on npm. Packages with a strong download history are generally seen as dependable within the development community.
    * **Documentation quality:** Well-documented packages usually make setup and troubleshooting much easier. Look for clear usage instructions, examples, and API references.
    * **License type:** Make sure the package’s license fits your project’s requirements, especially if you’re building something commercial or open-source.
    * **Bundle size and dependencies:** Consider how the package will affect your app’s performance and whether it adds many new dependencies. Lightweight, focused packages reduce potential conflicts and bloat.
    * **Update activity:** Review the project’s repository, such as on GitHub, to see if updates are recent and if maintainers are addressing questions or bug reports. Packages that are kept up to date are usually safer and more compatible with modern tools.
    * **Community input:** Explore comments, ratings, and discussions from npm, GitHub, or programming forums. Other developers’ experiences can alert you to potential issues or give you a better sense of how the package performs in practice.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).