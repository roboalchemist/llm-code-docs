# Source: https://docs.tokens.studio/transform-tokens/style-dictionary.md

# Style Dictionary + SD Transforms

## Transforming Design Tokens with Style Dictionary

[Style Dictionary](https://styledictionary.com/) is a powerful tool for transforming design tokens into usable code for different platforms, such as the web with CSS variables.

Tokens coming from Tokens Studio require an additional step: [@Tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms), an npm package that prepares Tokens for Style Dictionary.

This guide covers the basics of installing and using Style Dictionary. For full details, head to <https://styledictionary.com/>

### Install with NPM

Before we begin, we need to install Style Dictionary. You can install it using npm, which is a package manager for Node.js. We also assume you will need the [@tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms) integration package if you're a Tokens Studio user.

Open your terminal and run the following command:

```
npm install style-dictionary @tokens-studio/sd-transforms
```

### Using Style Dictionary

Once Style Dictionary is installed, we can start transforming our design tokens. Here's an overview of the process:

1. Define your design tokens in a JSON file.
2. Configure Style Dictionary to transform your design tokens into usable code.
3. Generate code for your target platform.

### SD-Transforms

We provide official transforms in the form of a package called [@tokens-studio/sd-transforms](https://www.npmjs.com/package/@tokens-studio/sd-transforms). You can customize these transforms or create your own to fit your needs. More information can be found on npm.

### Style Dictionary Configurator

[Style Dictionary Configurator](https://configurator.tokens.studio/) is a web-based tool that allows you to transform your design tokens directly in your browser. It uses Style Dictionary under the hood and can be a convenient way to experiment with Style Dictionary without installing it on your computer.

<div data-full-width="true"><figure><img src="https://3704321769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fds8Db2rgs9JSaG6grP0o%2Fuploads%2FZFWyIDJ8TTgum6566W4X%2Fspacer-image.png?alt=media&#x26;token=ca910cc6-4dd1-4019-940b-c67bbb539bd4" alt=""><figcaption></figcaption></figure></div>

### FAQ

#### Excluding/splitting sets in the output

**Question**: I want to exclude certain sets from the output, since my Design System will not need to use those tokens directly.

**Answer**: You can use [Style Dictionary Filters](https://styledictionary.com/reference/hooks/filters/) for this, to filter a set by the token's `filePath` property, which tells you which source file the token originated from. There is an in-depth example that goes one step further, [using filters to split your outputs in different files/folders](https://styledictionary.com/examples/splitting-output-files/)
