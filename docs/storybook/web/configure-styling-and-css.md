# Storybook Documentation
# Source: https://storybook.js.org/docs/configure/styling-and-css
# Page: /docs/configure/styling-and-css

# Styling and CSS

ReactVueAngularWeb ComponentsMore

There are many ways to include CSS in a web application, and correspondingly there are many ways to include CSS in Storybook. Usually, it is best to try and replicate what your application does with styling in Storybook’s configuration.

## 

CSS

Storybook supports importing CSS files in a few different ways. Storybook will inject these tags into the preview iframe where your components render, not the Storybook Manager UI. The best way to import CSS depends on your project's configuration and your preferences.

### 

Import bundled CSS (Recommended)

All Storybooks are pre-configured to recognize imports for CSS files. To add global CSS for all your stories, import it in [`.storybook/preview.ts`](./index#configure-story-rendering). These files will be subject to HMR, so you can see your changes without restarting your Storybook server.

CSF 3CSF Next 🧪

.storybook/preview.ts

Typescript
    
    
    // Replace your-framework with the framework you are using, e.g. react-vite, nextjs, vue3-vite, etc.
    import type { Preview } from '@storybook/your-framework';
     
    import '../src/styles/global.css';
     
    const preview: Preview = {
      parameters: {},
    };
     
    export default preview;

If your component files import their CSS files, this will work too. However, if you're using CSS processor tools like Sass or Postcss, you may need some more configuration.

### 

Include static CSS

If you have a global CSS file that you want to include in all your stories, you can import it in [`.storybook/preview-head.html`](./story-rendering#adding-to-head). However, these files will not be subject to HMR, so you'll need to restart your Storybook server to see your changes.

.storybook/preview-head.html
    
    
    <!-- Loads a font from a CDN -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&display=swap"
      rel="stylesheet"
    />
    <!-- Load your CSS file -->
    <link rel="stylesheet" href="path/to/your/styles.css" />

## 

CSS modules

### 

Vite

Vite comes with CSS modules support out-of-the-box. If you have customized the CSS modules configuration in your `vite.config.js` this will automatically be applied to your Storybook as well. Read more about [Vite's CSS modules support](https://vitejs.dev/guide/features.html#css-modules).

### 

Webpack

📣

Using `@storybook/nextjs`?

Storybook recreates your Next.js configuration, so you can use CSS modules in your stories without any extra configuration.

If you're using Webpack and want to use CSS modules, you'll need some extra configuration. We recommend installing [`@storybook/addon-styling-webpack`](https://storybook.js.org/addons/@storybook/addon-styling-webpack/) to help you configure these tools.

## 

PostCSS

### 

Vite

Vite comes with PostCSS support out-of-the-box. If you have customized the PostCSS configuration in your `vite.config.js` this will automatically be applied to your Storybook as well. Read more about [Vite's PostCSS support](https://vitejs.dev/guide/features.html#postcss).

### 

Webpack

📣

Using `@storybook/nextjs`?

Storybook recreates your Next.js configuration, so you can use PostCSS in your stories without any extra configuration.

If you're using Webpack and want to use PostCSS, you'll need some extra configuration. We recommend installing [`@storybook/addon-styling-webpack`](https://storybook.js.org/addons/@storybook/addon-styling-webpack/) to help you configure these tools.

## 

CSS pre-processors

### 

Vite

Vite comes with Sass, Less, and Stylus support out-of-the-box. Read more about [Vite's CSS Pre-processor support](https://vitejs.dev/guide/features.html#css-pre-processors).

### 

Webpack

📣

Using `@storybook/nextjs`?

Storybook recreates your Next.js configuration, so you can use Sass in your stories without any extra configuration.

If you're using Webpack and want to use Sass or less, you'll need some extra configuration. We recommend installing [`@storybook/addon-styling-webpack`](https://storybook.js.org/addons/@storybook/addon-styling-webpack/) to help you configure these tools. Or if you'd prefer, you can customize [Storybook's webpack configuration yourself](../builders/webpack#override-the-default-configuration) to include the appropriate loader(s).

## 

CSS-in-JS

CSS-in-JS libraries are designed to use basic JavaScript, and they often work in Storybook without any extra configuration. Some libraries expect components to render in a specific rendering “context” (for example, to provide themes), which can be accomplished with `@storybook/addon-themes`'s [`withThemeFromJSXProvider` decorator](https://github.com/storybookjs/storybook/blob/next/code/addons/themes/docs/api.md#withthemefromjsxprovider).

## 

Adding webfonts

### 

`.storybook/preview-head.html`

If you need webfonts to be available, you may need to add some code to the [`.storybook/preview-head.html`](./story-rendering#adding-to-head) file. We recommend including any assets with your Storybook if possible, in which case you likely want to configure the [static file location](./integration/images-and-assets#serving-static-files-via-storybook-configuration).

### 

`.storybook/preview.ts`

If you're using something like [`fontsource`](https://fontsource.org/) for your fonts, you can import the needed css files in your [`.storybook/preview.ts`](./index#configure-story-rendering) file.

Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/configure/styling-and-css.mdx)