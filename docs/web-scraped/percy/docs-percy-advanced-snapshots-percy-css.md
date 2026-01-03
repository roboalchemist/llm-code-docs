# Source: https://www.browserstack.com/docs/percy/advanced-snapshots/percy-css

[Skip to main content](#main-content)[Explore now](https://scanner.browserstack.com?utm_source=hello+bar&utm_medium=website)[Documentation](https://www.browserstack.com/docs/)[Ask the Community](https://www.browserstack.com/discord?ref=docsArticle&source=docs_article_page)
# Percy specific CSS
Learn how to apply Percy-specific CSS to ignore areas from being rendered by Percy

Percy provides a powerful way to take control of rendering to do whatever you want – ignore regions, stabilize dynamic elements, etc.

Percy’s way to do this is something we call “Percy-specific CSS”, which is only applied in the Percy rendering environment. You can use any CSS and it’ll only be rendered in Percy’s rendering environment. This can be very helpful for ignoring regions, hiding areas that produce false-positive visual diffs, or when you’d like more specific control over the state of UI elements like visualizations and animations.

- This applies to both BrowserStack SDK and Percy SDK.
- Usepercy_snapshotfunction if you’re using the Percy SDK for web projects. For Automate projects with the Percy SDK or when using the BrowserStack SDK, usepercy_screenshotfunction.
`percy_snapshot``percy_screenshot`You can apply Percy specific CSS in most SDKs without editing your site or applications CSS files. This can be done by passing apercyCSSoption via the options object. For example:

`percyCSS`
```
await percySnapshot('Home page', { 
  percyCSS: `iframe { display: none; }` 
});

```

`await percySnapshot('Home page', { 
  percyCSS: `iframe { display: none; }` 
});`
## Percy snapshot
You can also configure global Percy CSS via the.percy.ymlfile:

`.percy.yml`
```
version: 1
snapshot:
  percy-css: | 
    iframe { 
      display: none; 
    }

```

`version: 1
snapshot:
  percy-css: | 
    iframe { 
      display: none; 
    }`
### Priority between snapshot level Percy CSS and global Percy CSS
There can be the case when we want certain CSS to get applied on all snapshots and particular CSS on specific snapshot. For this in Percy user can provide both the global CSS and snapshot level CSS by providing the configurations mentioned above.

In these cases we merge the Percy CSS from both the configs to be applied on the snapshot.

- Snapshot Level Percy CSS:p { font-size: 2em; }
`p { font-size: 2em; }`- Global Percy CSS :p { color: purple; }
`p { color: purple; }`The final Percy CSS that would be applied on snapshot would look like :

```
p { color: purple; }
p { font-size: 2rem; }

```

`p { color: purple; }
p { font-size: 2rem; }`We give priority to snapshot level CSS over global CSS in the case where same selector is modifying same property.

- Snapshot Level Percy CSS :p { background-color: yellow !important; }
`p { background-color: yellow !important; }`- Global Percy CSS :p { background-color: green !important; }
`p { background-color: green !important; }`The final Percy CSS that would be applied on snapshot would look like:

```
p { background-color: green !important; }
p { background-color: yellow !important; }

```

`p { background-color: green !important; }
p { background-color: yellow !important; }`In this case we merged Snapshot Level CSS later which leads to higher priority according to CSS Specificity Rules an hence in final rendered snapshotbackground-colorofptag would be Yellow.

`background-color`
### Percy CSS does not change specificity
Percy CSS is appended to the bottom of the</body>tag to help with order, but it’s likely you will need to out-specify your applications CSS (with!importantor otherwise).

`</body>``!important`Consider an example to understand specificity rules:

- Snapshot level Percy CSS:p { background-color: yellow; }
`p { background-color: yellow; }`- Global Percy CSS:p { background-color: green !important; }
`p { background-color: green !important; }`Now in this case although snapshot level CSS has higher priority, but due to!importantkeyword in Global CSS that would take priority over Snapshot Level CSS according to CSS specificity rules and hence in final rendered snapshot,background-colorofptag would be Green.

`!important``background-color`Final merged Percy CSS would look like :

```
p { background-color: green !important; }
p { background-color: yellow; }

```

`p { background-color: green !important; }
p { background-color: yellow; }`
## Percy CSS @media query
You can do so using the@media only percyCSS media query. CSS that is nested under this media query will only apply in Percy and will not affect your normal pages outside of Percy.

`@media only percy`For example, you might have an element that renders differently each time and you want Percy to ignore that element. You can use Percy specific styles to achieve this.

Let’s say you want to apply ahide-in-percyclass to elements you want hidden in Percy. Here’s how you can do that:

`hide-in-percy`
```
@media only percy {
  .hide-in-percy {
    visibility: hidden;
  }
}

```

`@media only percy {
  .hide-in-percy {
    visibility: hidden;
  }
}`And your page would have HTML like this:

```
<div class="hide-in-percy">an element we know we want to ignore in visual tests</div>

```

`<div class="hide-in-percy">an element we know we want to ignore in visual tests</div>`The class names don’t have to be Percy specific, you can put any normal CSS selectors and rules that you want in the media query and they will only be applied when rendering in Percy.

`@media only percy {...}`
### Percy CSS @media query for Storybook
When usingStorybook, you can providepercyCSSalong with othercommon optionseither withstorypercy parameters or using a Percy config file.

[Storybook](https://storybook.js.org/)`percyCSS`[common options](https://www.browserstack.com/docs/percy/take-percy-snapshots/overview#configuration-file)`story`In order to use the Percy CSS media query with Storybook snapshots, you need to modify the Storybook’spreview-head.htmlfile to serve static CSS overrides. This is because Percy uses a content-type-based system to apply styles to HTML and CSS files, and CSS-in-JS breaks this paradigm. See thestorybook documentationfor how to add custom head tags to your project. Here’s an example of apreview-head.htmlfile that includes a default stylesheet, and adds a.hide-in-percyclass styling:

`preview-head.html`[storybook documentation](https://storybook.js.org/configurations/add-custom-head-tags/)`preview-head.html``.hide-in-percy`
```
<link rel="stylesheet" type="text/css" href="default.css">

<style>
@media only percy {
  .hide-in-percy {
    visibility: hidden;
  }
}
</style>

```

You would then add a percy-specificclassNameattribute to your component the example showclassNameas per React syntax:

`className``className`
```
<div className="hide-in-percy">
  <img src="https://i.giphy.com/bcKmIWkUMCjVm.gif" alt="Bom dia"/>
</div>

```

You can see a complete example of this technique in thispull request.

[pull request](https://github.com/percy/percy-storybook/pull/42/files)
#### Debugging Storybook Percy-Specific CSS
It may be helpful to render your storybook project to a static build in order to debug any changes. See theStorybook documentationfor details on how to do this. Once you have generated a static version of your app, you can remove the surrounding@media only percyblock in the markup to preview your Percy-specific styles in your browser.

[Storybook documentation](https://storybook.js.org/basics/exporting-storybook/)`@media only percy`
## Screenshot Issue
If an animated element isn’t rendering correctly in Percy, it may be because Percy disables animations initially to maintain page stability. If the element is hidden or hasopacity: 0at the start, it might not render since the animation is blocked. To fix this, use Percy-specific CSS to make the element visible or display it in its final state.

`opacity: 0`Here’s an example to illustrate this approach:

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fade-In Animation Example</title>
    <style>
        .hidden {
            opacity: 0;
        }
        .fade-in {
            opacity: 0;
            animation: fadeIn 2s forwards;
        }
        @keyframes fadeIn {
            to {
                opacity: 1;
            }
        }
    </style>
</head>
<body>
    <div id = 'hidden-ele' class="hidden fade-in">This text will fade in.</div>
</body>
</html>
});

```

The element starts with opacity: 0 and gradually changes to opacity: 1 during the animation. However, because Percy disables animations, this element won’t be visible in Percy.

Now, apply the following percyCSS code to the animated element to make it visible (or in its final state).

```
await percySnapshot(driver, 'Fading_element', {
      percyCSS: `.hidden {
          opacity: 1
          }`
    })

```

After applying the percyCSS code, the element will render in its final state and be visible.

#### We're sorry to hear that. Please share your feedback so we can do better
Contact ourSupport teamfor immediate help while we work on improving our docs.

[Support team](https://www.browserstack.com/support)
#### We're continuously improving our docs. We'd love to know what you liked
- This page has exactly what I am looking for
- This content & code samples are accurate and up-to-date
- The content on this page is easy to understand
- Other (please tell us more below)
Thank you for your valuable feedback

- ON THIS PAGE
Is this page helping you?

[Support team](https://www.browserstack.com/support)Thank you for your valuable feedback!

[Talk to an Expert](https://www.browserstack.com/contact?ref=docs-page-floating-contact)Welcome to Percy

New to Percy?

[View
          Documentation](https://www.browserstack.com/docs/percy/get-started-without-code-or-automation-script)Select your framework and language to proceed

- Selenium
- Playwright
- Cypress
[Cypress](https://www.browserstack.com/docs/percy/cypress/get-started)- Puppeteer
[Puppeteer](https://www.browserstack.com/docs/percy/puppeteer/get-started)- Ember
[Ember](https://www.browserstack.com/docs/percy/ember/get-started)- Storybook
[Storybook](https://www.browserstack.com/docs/percy/storybook/get-started)- Gatsby
[Gatsby](https://www.browserstack.com/docs/percy/gatsby/get-started)- Jekyll
[Jekyll](https://www.browserstack.com/docs/percy/jekyll/get-started)- Appium
[Appium](https://www.browserstack.com/docs/percy/appium/get-started)- Tricentis Tosca
[Tricentis Tosca](https://www.browserstack.com/docs/percy/tosca/get-started)- Build your own SDK
[Build your own SDK](https://www.browserstack.com/docs/percy/build-your-own-SDK/get-started)