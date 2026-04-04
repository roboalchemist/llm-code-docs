# React Email - Comprehensive Documentation
**Note:** This is an auto-generated comprehensive reference extracted from the official React Email documentation.

## Table of Contents
- Components
- Contributing
- Editor
- Getting Started
- Guides
- Integrations
- Snippets
- Utilities

---

## CLI

## `email dev`

Starts a local development server that will watch your files and automatically rebuild
your email template when you make changes.

**Options**

**F.A.Q**

## `email build`

Copies the preview app for onto `.react-email` and builds it.

## `email start`

Runs the built preview app that is inside `.react-email`.

## `email export`

Generates the plain HTML files of your emails into a `out` directory.

**Note:** 
  A very common misconception is to assume that `email export` is the default or primary way of rendering
  email templates.

  The primary and preferable way is always going to be the [render](/utilities/render) utility,
  by passing in the needed data through props, on the exact moment of sending the email.

  `email export` is a secondary way meant for situations where React Email cannot be used optimally.
  With this secondary way, comes significant drawbacks, mainly the need for manual templating, which
  could be done easily with the `render` utility. It being a secondary way, we would strongly recommend
  you don't use it unless you really are forced into it.

  As an example, two cases where `email export` makes itself necessary include:
  - When the email content must be processed by a backend in a language other than JavaScript.
  - When the platform handling email, such as Shopify, forces you into manual templating.

  You also should not have to worry about `render`'s performance, as typically, the introduced
  time in rendering is going to be milliseconds when compared to manual templating.

**Options**

## `email help `

Shows all the options for a specific command.

## `email resend setup`

Sets up a configuration in your home directory with your Resend API Key by prompting interactively.

## `email resend reset`

Removes your API Key from the configuration in your home directory.

---

## Contributing

## Improving the docs

Documentation is extremely important and takes a fair deal of time and effort to write and keep updated. Everything is written in [Markdown](https://www.markdownguide.org/) to facilitate the process of contributing.

## Building new components

We're open to expanding the catalog of components to cover as many use cases as possible. We suggest to open an issue for discussion first to make sure your idea is aligned with the project goals.

## Opening issues

Open an issue to report bugs or to propose new features.

- **Reporting bugs**: describe the bug as clearly as you can, including steps to reproduce, what happened and what you were expecting to happen. Also include browser version, OS and other related software's (npm, Node.js, etc) versions when applicable.

- **Suggesting features**: explain the proposed feature, what it should do, why it is useful, how users should use it. Give us as much info as possible so it will be easier to discuss, access and implement the proposed feature. When you're unsure about a certain aspect of the feature, feel free to leave it open for others to discuss and find an appropriate solution.

## Proposing pull requests

Pull requests are very welcome. Note that if you are going to propose drastic changes, be sure to open an issue for discussion first, to make sure that your PR will be accepted before you spend effort coding it.

- **Forking the repository**: clone it locally and create a branch for your proposed bug fix or new feature. Avoid working directly on the main branch.

- **Making changes**: implement your bug fix or feature, write tests to cover it and make sure all tests are passing. Then commit your changes, push your bug fix/feature branch to the origin (your forked repo) and open a pull request to the upstream (the repository you originally forked)'s main branch.

---

## Deployment

  
    ```diff
     {
       "scripts": {
    +    "build": "email build"
       }
     }
    ```
  
  
    You also need to add "next" on `devDependencies` to work properly:

    ```diff
     {
       "devDependencies": {
    +    "next": "*",
       }
     }
    ```

    This is a limitation on Vercel's Next Framework Preset.
  
  
    In the end, your settings should look like this:

    
      
    
  

---

## React Email

## Why

We believe that email is an extremely important medium for people to communicate. However, we need to stop developing emails like 2010, and rethink how email can be done in {new Date().getFullYear()} and beyond. Email development needs a revamp. A renovation. Modernized for the way we build web apps today.

## Getting Started

React Email is designed to be incrementally adopted, so you can add it to most codebases in a few minutes.

## Components

This is a set of standard components to help you build amazing emails without having to deal with the mess of creating table-based layouts and maintaining archaic markup.

## Integrations

In order to use React Email with any email service provider, you'll need to convert the components made with React into a HTML string. This is done using the [render](/utilities/render) utility.

## Authors

- Bu Kinoshita ([@bukinoshita](https://twitter.com/bukinoshita))
- Zeno Rocha ([@zenorocha](https://twitter.com/zenorocha))

---

## Roadmap

If any of these are important to you please let us know. We use community feedback to plan our roadmap, and we also encourage contributors to submit their ideas on [GitHub Discussions](https://github.com/resend/react-email/discussions) so that we can discuss them with the community.

Feel free to contribute to any of them as well.

## Planned Features

These are the features that we've planned to work on in the near future.

### VS Code extension

Build a VS Code extension where developers can build the email using React on one side and see a live preview right next to it.

- [GitHub Discussion #574](https://github.com/resend/react-email/discussions/574)

---

# Getting Started

## Automatic Setup

Using monorepos? Then, we recommend following the [monorepo setup](/getting-started/monorepo-setup/choose-package-manager).

## 1. Install

We recommend using `create-email`, which sets up everything automatically for you.

This will create a new folder called `react-email-starter` with a few email templates.

## 2. Run locally

First, install the dependencies:

Then, run the development server:

## 3. See changes live

Visit [localhost:3000](http://localhost:3000) and edit any of the files on the `emails` folder to see the changes.

  

## 4. Next steps

---

## Manual Setup

Are you using monorepos? Then we recommend you follow our [monorepos setup](/getting-started/monorepo-setup/choose-package-manager).

## 1. Install dependencies

Install the React Email package locally and a few components.

## 2. Add scripts

Include the following script in your `package.json` file.

```json package.json
{
  "scripts": {
    "email:dev": "email dev"
  }
}
```

## 3. Write an email template

Create a new folder called `emails`, create a file inside called `email.tsx`, and add the following code:

```jsx emails/email.tsx

export default function Email() {
  return (
    
      
      
        <Button
          href="https://example.com"
          style={{ background: "#000", color: "#fff", padding: "12px 20px" }}
        >
          Click me
        
      
    
  );
}
```

## 4. Run locally

Start the development server.

## 5. See changes live

Visit [localhost:3000](http://localhost:3000) and edit `email.tsx` file to see the changes.

  

## 6. Next steps

---

## Migrating to React Email

## From MJML

1. Remove the `mjml` npm package and install `react-email` and `@react-email/components`
2. Find all MJML templates ending with the `.mjml` extension and convert these to React components with the `.tsx` or `.jsx` extension.
3. Replace MJML standard component tags with React Email component tags where possible, including ``, ``, `` etc.
4. Convert custom MJML components with the `.js` extension to React components with the `.tsx` or `.jsx` extension.

---

## Monorepo setup

What package manager are you using?

---

## Setting up for bun workspaces

## 1. Create workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`).

Include a new `package.json` and do not forget to add this to the `workspaces` of your monorepo's `package.json`.

## 2. Install dependencies

Install React Email to the `transactional` workspace.

```sh packages/transactional
bun add react-email -D -E
bun add @react-email/components react react-dom -E
```

## 3. Add scripts

Include the following script in your `package.json` file.

```json packages/transactional/package.json
{
  // ...
  "scripts": {
    "dev": "email dev"
  }
  // ...
}
```

## 4. Write your emails

Create a new folder called `emails`, create a file inside called `email.tsx` and add the following example code:

```jsx packages/transactional/emails/email.tsx

export default function Email() {
  return (
    
      
      
        <Button
          href="https://example.com"
          style={{ background: "#000", color: "#fff", padding: "12px 20px" }}
        >
          Click me
        
      
    
  );
}
```

## 5. Run preview server

Start the email previews development server:

```sh packages/transactional
bun dev
```

## 6. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/email.tsx` file to see the changes.

  

## 7. Try it yourself

---

## Setting up for npm workspaces

## 1. Create workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`).

Include a new `package.json` and do not forget to add this to the `workspaces` of your monorepo's `package.json`.

## 2. Install dependencies

Install React Email in the `transactional` workspace.

```sh packages/transactional
npm install react-email @react-email/preview-server -D -E
npm install @react-email/components react react-dom -E
```

## 3. Add scripts

Include the following script in your `package.json` file.

```json packages/transactional/package.json
{
  // ...
  "scripts": {
    "dev": "email dev"
  }
  // ...
}
```

## 4. Write your emails

Create a new folder called `emails`, create a file inside called `email.tsx` and add the following example code:

```jsx packages/transactional/emails/email.tsx

export default function Email() {
  return (
    
      
      
        <Button
          href="https://example.com"
          style={{ background: "#000", color: "#fff", padding: "12px 20px" }}
        >
          Click me
        
      
    
  );
}
```

## 5. Run preview server

Start the email previews development server:

```sh packages/transactional
npm run dev
```

## 6. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/email.tsx` file to see the changes.

  

## 7. Try it yourself

---

## Setting up for pnpm workspaces

## 1. Create workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`) and 
in there setup a new `package.json` and do not forget to add this to your `pnpm-workspace.yaml`.

## 2. Install dependencies

Install React Email in the `transactional` workspace.

```sh packages/transactional
pnpm add react-email @react-email/preview-server -D -E
pnpm add @react-email/components react react-dom -E
```

## 3. Add scripts

Include the following script in your `package.json` file.

```json packages/transactional/package.json
{
  // ...
  "scripts": {
    "dev": "email dev"
  }
  // ...
}
```

## 4. Write your emails

Create a new folder called `emails`, create a file inside called `email.tsx` and add the following example code:

```jsx packages/transactional/emails/email.tsx

export default function Email() {
  return (
    
      
      
        <Button
          href="https://example.com"
          style={{ background: "#000", color: "#fff", padding: "12px 20px" }}
        >
          Click me
        
      
    
  );
}
```

## 5. Run preview server

Start the email previews development server:

```sh packages/transactional
pnpm dev
```

## 6. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/email.tsx` file to see the changes.

  

## 7. Try it yourself

---

## Setting up for yarn workspaces

  This is a guide intended at users of [yarn modern](https://yarnpkg.com/getting-started/qa#why-should-you-upgrade-to-yarn-modern). 
  For those who are using [yarn classic](https://www.npmjs.com/package/yarn) (`1.x`), you can do something similar to the 
  [pnpm guide](/getting-started/monorepo-setup/pnpm).

## 1. Create transactional workspace

Create a new folder called `transactional` inside of where you keep workspace packages (generally `./packages/*`).

Include a new `package.json` and do not forget to add this to the `workspaces` of your monorepo's `package.json`.

## 2. Set linker either to `node-modules` or to `pnpm`

Currently, React Email can only work with yarn's `node-modules` and `pnpm` [install modes](https://yarnpkg.com/features/linkers)
so you will need to set it to one of these two on your `.yarnrc.yml` file:

```yml .yarnrc.yml
nodeLinker: node-modules
```

## 3. Install dependencies

Install React Email in the `transactional` workspace.

```sh packages/transactional
yarn add react-email @react-email/preview-server -D -E
yarn add @react-email/components react react-dom -E
```

## 4. Add scripts

Include the following script in your `package.json` file.

```json packages/transactional/package.json
{
  // ...
  "scripts": {
    "dev": "email dev"
  }
  // ...
}
```

## 5. Write your emails

Create a new folder called `emails`, create a file inside called `email.tsx` and add the following example code:

```jsx packages/transactional/emails/email.tsx

export default function Email() {
  return (
    
      
      
        <Button
          href="https://example.com"
          style={{ background: "#000", color: "#fff", padding: "12px 20px" }}
        >
          Click me
        
      
    
  );
}
```

## 6. Run preview server

Start the email previews development server:

```sh packages/transactional
yarn dev
```

## 7. See changes live

Visit [localhost:3000](http://localhost:3000) and edit the `emails/email.tsx` file to see the changes.

  

## 8. Try it yourself

---

## Updating React Email

## Update from React Email 4.0 to 5.0

1. Update your React Email packages: `npm install @react-email/components@latest react-email@latest`.
2. Replace all `renderAsync` uses with `render`.

Make sure you update `@react-email/components` alongside `react-email`. The compatibility checker now only supports Tailwind 4, so you need to update both in sync.

### Tailwind 4

This update includes Tailwind 4 via `@react-email/components@latest`. Some utilities have changed since Tailwind 3—review their [upgrade guide](https://tailwindcss.com/docs/upgrade-guide#changes-from-v3) to adjust your code if needed.

Tailwind 4 also changes how classes are handled in components. Previously, passing `className` added an equivalent inlined `style` prop, which caused confusion and performance issues. Now, styles are only inlined on elements, not components. If you were merging utilities with the `style` prop, consider using [tailwind-merge](https://github.com/dcastil/tailwind-merge) instead.

The configuration remains in the `config` prop.

---

# Components

## Button

**Note:** 
  Semantics: Quite often in the email world we talk about buttons, when actually
  we mean links. Behind the scenes this is a `` tag, that is styled like a `` tag.

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    <Button
      href="https://example.com"
      style={{ color: "#61dafb", padding: "10px 20px" }}
    >
      Click me
    
  );
};
```

## Props

---

## Code Block

## Install

Install the component from your command line.

## Getting Started

Add the component into your email component as follows.

```jsx

const Email = () => {
  const code = `export default async (req, res) => {
  try {
    const html = await renderAsync(
      EmailTemplate({ firstName: 'John' })
    );
    return NextResponse.json({ html });
  } catch (error) {
    return NextResponse.json({ error });
  }
}`;

  return (<CodeBlock
    code={code}
    lineNumbers // add this so that there are line numbers beside each code line
    theme={dracula}
    language="javascript"
  />);
};
```

This should render a code-block with the desired theme.

## Theming

Themes for this component are basically a set of styles for each kind of token that can result from prismjs's tokenization. See [here](https://prismjs.com/tokens.html) for more information on the tokens available.

An example of a theme would be this:

```json
{
  "base": {
    "color": "#f8f8f2",
    "background": "#282a36",
    "textShadow": "0 1px rgba(0, 0, 0, 0.3)",
    "fontFamily": "Consolas, Monaco, 'Andale Mono', 'Ubuntu Mono', monospace",
    "textAlign": "left",
    "whiteSpace": "pre",
    "wordSpacing": "normal",
    "wordBreak": "normal",
    "wordWrap": "normal",
    "lineHeight": "1.5",
    "MozTabSize": "4",
    "OTabSize": "4",
    "tabSize": "4",
    "WebkitHyphens": "none",
    "MozHyphens": "none",
    "MsHyphens": "none",
    "hyphens": "none",
    "padding": "1em",
    "margin": ".5em 0",
    "overflow": "auto",
    "borderRadius": "0.3em"
  },
  "comment": {
    "color": "#6272a4"
  },
  "prolog": {
    "color": "#6272a4"
  },
  "doctype": {
    "color": "#6272a4"
  },
  "cdata": {
    "color": "#6272a4"
  },
  "punctuation": {
    "color": "#f8f8f2"
  },
  "property": {
    "color": "#ff79c6"
  },
  // ...
}
```

Each token type can have their own defined styles and for each one of there can be any styles that can be applied directly to `React` elements. 
As you can see from the example `dracula` theme though, there is a defined property called `base` which is the styling for the `pre` element that wraps the HTML being rendered.

For you to not need to defined a theme without any basis, or to not define one that already has been defined, we have many default themes exported from `@react-email/code-block`. 
These themes were generated by a bit of code that converts a CSS file for a prismjs theme into a object theme of these. 
If you want to generate a theme from another existing prismjs theme you can do so by looking into [this](https://github.com/gabrielmfern/from-prismjs-to-react-email-code-block-theme).

## Props

---

## Code Inline

## Install

Install the component from your command line.

## Getting Started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
    return @react-email/code-inline;
}
```

---

## Column

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    
      A
      B
      C
    
  );
};
```

---

## Container

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    
      
        Click me
      
    
  );
};
```

---

## Font

## Install

Install component from your command line.

## Getting started

Add the component to your email template. This applies your font to all tags inside your email.
Note, that not all email clients supports web fonts, this is why it is important to configure your `fallbackFontFamily`.
To view all email clients that supports web fonts [see](https://www.caniemail.com/features/css-at-font-face/)

```jsx

const Email = () => {
  return (
    
      
        <Font
          fontFamily="Roboto"
          fallbackFontFamily="Verdana"
          webFont={{
            url: "https://fonts.gstatic.com/s/roboto/v27/KFOmCnqEu92Fr1Mu4mxKKTU1Kg.woff2",
            format: "woff2",
          }}
          fontWeight={400}
          fontStyle="normal"
        />
      
    
  );
};
```

## Props

---

## HTML

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    
      
        Click me
      
    
  );
};
```

## Props

---

## Head

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include children tags where needed.

```jsx

const Email = () => {
  return (
    
      My email title
    
  );
};
```

---

## Heading

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return Lorem ipsum;
};
```

## Props

---

## Hr

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return ;
};
```

---

## Image

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return ;
};
```

  All email clients can display `.png`, `.gif`, and `.jpg` images.
  Unfortunately, `.svg` images are not well supported, regardless of how they're
  referenced, so avoid using these. See [Can I
  Email](https://www.caniemail.com/features/image-svg/) for more information.

## Props

---

## Link

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return Example;
};
```

## Props

---

## Markdown

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    
      <Markdown
        markdownCustomStyles={{
          h1: { color: "red" },
          h2: { color: "blue" },
          codeInline: { background: "grey" },
        }}
        markdownContainerStyles={{
          padding: "12px",
          border: "solid 1px black",
        }}
      >{`# Hello, World!`}

      {/* OR */}

      
    
  );
};
```

## Props

---

## Preview

**Note:** 
  Email clients have this concept of “preview text” which gives insight into
  what's inside the email before you open. A good practice is to keep that text
  under 90 characters.

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return Email preview text;
};
```

---

## Row

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    
      
        A
      
      
        B
      
      
        C
      
    
  );
};
```

---

## Section

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return (
    {/* A simple `section` */}
    
      Hello World
    

    {/* Formatted with `rows` and `columns` */}
     
      
        Column 1, Row 1
        Column 2, Row 1
      
      
        Column 1, Row 2
        Column 2, Row 2
      
    
  );
};
```

---

## Tailwind

## Install

Install component from your command line.

## Getting started

**Note:** The current `tailwindcss` version used for this component is `4.1.12`

Add the component around your email body content.

```jsx

const Email = () => {
  return (
    <Tailwind
      config={{
        presets: [pixelBasedPreset],
        theme: {
          extend: {
            colors: {
              brand: "#007291",
            },
          },
        },
      }}
    >
      <Button
        href="https://example.com"
        className="bg-brand px-3 py-2 font-medium leading-4 text-white"
      >
        Click me
      
    
  );
};
```

## Props

**Note:** 
    Most email clients are style-limited and some styles may not work.
    
    One example of this is how Tailwind uses `rem` as its main unit for better accessibility. This
    is not supported by [some email clients](https://www.caniemail.com/features/css-unit-rem/), and
    the `pixelBasedPreset` changes it so that the styles are based on `16px` instead.

## Live example

## Known limitations

---

## Text

## Install

Install component from your command line.

## Getting started

Add the component to your email template. Include styles where needed.

```jsx

const Email = () => {
  return Lorem ipsum;
};
```

---

# Utilities

## Render

## 1. Install dependencies

Install package from your command line.

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```jsx email.jsx

export function MyTemplate(props) {
  return (
    
      Some title
      
      Click me
    
  );
}

export default MyTemplate;
```

## 3. Convert to HTML

Import an existing React component and convert into a HTML string.

**Note:** You can use the `pretty` function to beautify the output.

```jsx

const html = await pretty(await render());

console.log(html);
```

This will generate the following output:

```html

  Some title
  
  
    
      
        &nbsp;
      
    
    Click me
    
      
        &nbsp;
      
    
  

```

**Warning:** 
    When running in the browser, to properly support Safari and browsers running on iOS, you will
    need to polyfill the [ReadableByteStreamController API](https://developer.mozilla.org/en-US/docs/Web/API/ReadableByteStreamController#browser_compatibility).

    We recommend [npm i web-streams-polyfill](https://www.npmjs.com/package/web-streams-polyfill). It can be applied as follows in some sort of root file for your website:

    ```jsx
    import "web-streams-polyfill/polyfill";
    ```

## 4. Convert to Plain Text

Plain text versions of emails are important because they ensure that the message can be read by the recipient even if they are unable to view the HTML version of the email.

This is important because not all email clients and devices can display HTML email, and some recipients may have chosen to disable HTML email for security or accessibility reasons.

Here's how to convert a React component into plain text.

```jsx

const html = await render();
const text = toPlainText(html);

console.log(text);
```

This will generate the following output:

```
Some title

---

Click me [https://example.com]
```

## Options

---

# Integrations

## Inbound

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Inbound Node.js SDK](https://www.npmjs.com/package/inboundemail).

Make sure you have an account on [inbound](https://inbound.new?utm_source=react-email%20docs&utm_medium=email&utm_campaign=react_email_campaign), you will need an inbound API key.

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}

export default Email;
```

## 3. Send email

**Note:** When integrating with other services, you need to convert your React template into HTML before sending. Inbound takes care of that for you. You can just directly pass the React template to the SDK.

Import the email template you just built and use the Inbound SDK to send it.

```tsx

const inbound = new Inbound(process.env.INBOUND_API_KEY);

await inbound.emails.send({
  from: 'you@example.com',
  to: 'user@gmail.com',
  subject: 'hello world',
  react: ,
});
```

## 4. Reply to an email

Use the Inbound SDK to reply to an email with the same template you just created.

```tsx

const inbound = new Inbound({
    apiKey: process.env.INBOUND_API_KEY
});

// sending an email via inbound
await inbound.emails.send(email.id,{
  from: "React Email ",
  react: 
});

// replying to an email that was received via inbound
await inbound.emails.reply(email.id,{
  from: "React Email ",
  react: 
});

```

## Try it yourself

---

## Overview

In order to use React Email with any email service provider, you'll need to convert the components made with React into a HTML string. This is done using the [render](/utilities/render) utility. Or you can integrate React Email into your NodeJS application by installing `@babel/preset-typescript` and adding a `.babelrc` config file:

```json .babelrc
{
  "presets": ["@babel/preset-typescript"]
}
```

---

## Send email using AWS SES

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [AWS SES Node.js SDK](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/clients/client-ses/).

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the AWS SES SDK to send it.

```tsx

const ses = new SES({ region: process.env.AWS_SES_REGION })

const emailHtml = await render();

const params: SendEmailCommandInput = {
  Source: 'you@example.com',
  Destination: {
    ToAddresses: ['user@gmail.com'],
  },
  Message: {
    Body: {
      Html: {
        Charset: 'UTF-8',
        Data: emailHtml,
      },
    },
    Subject: {
      Charset: 'UTF-8',
      Data: 'hello world',
    },
  },
};

await ses.sendEmail(params);
```

## Try it yourself

---

## Send email using MailerSend

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [MailerSend Node.js SDK](https://www.npmjs.com/package/mailersend).

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the MailerSend SDK to send it.

```tsx

const mailerSend = new MailerSend({
  apiKey: process.env.MAILERSEND_API_KEY || '',
});

const emailHtml = await render();

const sentFrom = new Sender("you@yourdomain.com", "Your name");
const recipients = [
  new Recipient("your@client.com", "Your Client")
];

const emailParams = new EmailParams()
  .setFrom(sentFrom)
  .setTo(recipients)
  .setSubject("This is a Subject")
  .setHtml(emailHtml)

await mailerSend.email.send(emailParams);
```

## Try it yourself

---

## Send email using Nodemailer

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) and [nodemailer](https://www.npmjs.com/package/nodemailer) packages.

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into a HTML string, and use the Nodemailer SDK to send it.

```tsx

const transporter = nodemailer.createTransport({
  host: 'smtp.forwardemail.net',
  port: 465,
  secure: true,
  auth: {
    user: 'my_user',
    pass: 'my_password',
  },
});

const emailHtml = await render();

const options = {
  from: 'you@example.com',
  to: 'user@gmail.com',
  subject: 'hello world',
  html: emailHtml,
};

await transporter.sendMail(options);
```

## Try it yourself

---

## Send email using Plunk

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Plunk Node.js SDK](https://www.npmjs.com/package/@plunk/node).

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}

export default Email;
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the Plunk SDK to send it.

```tsx

const plunk = new Plunk(process.env.PLUNK_API_KEY);

const emailHtml = await render();

plunk.emails.send({
  to: "hello@useplunk.com",
  subject: "Hello world",
  body: emailHtml,
});
```

## Try it yourself

---

## Send email using Postmark

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Postmark Node.js SDK](https://www.npmjs.com/package/postmark).

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the Postmark SDK to send it.

```tsx

const client = new postmark.ServerClient(process.env.POSTMARK_API_KEY);

const emailHtml = await render();

const options = {
  From: 'you@example.com',
  To: 'user@gmail.com',
  Subject: 'hello world',
  HtmlBody: emailHtml,
};

await client.sendEmail(options);
```

## Try it yourself

---

## Send email using Resend

##  Send email with Resend
Resend was built by the same team that created React Email, which makes this our recommendation to send emails.

### 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Resend Node.js SDK](https://www.npmjs.com/package/resend).

### 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}

export default Email;
```

### 3. Send email

**Note:** When integrating with other services, you need to convert your React template into HTML before sending. Resend takes care of that for you.

Import the email template you just built and use the Resend SDK to send it.

```tsx

const resend = new Resend('re_123456789');

await resend.emails.send({
  from: 'you@example.com',
  to: 'user@gmail.com',
  subject: 'hello world',
  react: ,
});
```

## Set up Templates with Resend

[Resend Templates](https://resend.com/docs/dashboard/templates/introduction) are a great way to collaborate on emails with your team, even if they're not technical. Upload a React Email Template to Resend and your entire team can collaborate in real-time in the visual editor.

Here's how to get started.

### 1. Add your Resend API Key

First, sign up for a [free Resend account](https://resend.com/signup).

Next, set up the Resend integration using the React Email CLI:

```bash
npx react-email@latest resend setup
```

This will prompt you to enter your Resend API Key. To get one, navigate to [API Keys](https://resend.com/api-keys) in your Resend dashboard, click **Create API key**, and ensure that the API Key is scoped to **Full Access**.

Paste the API Key into the terminal and press enter.

### 2. Upload a Template to Resend

Run React Email and visit the **Resend** tab of the toolbar, located at the bottom of the window.

Choose **Upload** or **Bulk Upload** to import your Template to Resend.

If you want to remove the Resend integration, run `npx react-email@latest resend reset`.

## Try it yourself

---

## Send email using Scaleway Transactional Email

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [Scaleway Node.js SDK](https://www.npmjs.com/package/@scaleway/sdk).

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the Scaleway SDK to send it.

```tsx

const client = createClient({
  accessKey: process.env.ACCESS_KEY,
  secretKey: process.env.SECRET_KEY,
  defaultProjectId: process.env.PROJECT_ID,
  defaultRegion: "fr-par",
  defaultZone: "fr-par-1",
});

const transactionalEmailClient = new TransactionalEmail.v1alpha1.API(client);

const emailHtml = await render();

const sender = {
  email: "react-email@transactional.email.fr",
  subject: "TEST",
  name: "Team",
};

const userInvited = {
  email: "XXXX@scaleway.com",
  name: "TEST",
  teamName: "Team",
};

const userInvitedBy = {
  email: "XXXX@scaleway.com",
  name: "TEST",
  teamName: "Team",
};

transactionalEmailClient.createEmail({
  from: {
    email: sender.email,
    name: sender.name,
  },
  to: [
    {
      email: userInvited.email,
      name: userInvited.name,
    },
  ],
  subject: sender.subject,
  text: null,
  html: emailHtml,
});
```

## Try it yourself

---

## Send email using SendGrid

## 1. Install dependencies

Get the [@react-email/components](https://www.npmjs.com/package/@react-email/components) package and the [SendGrid Node.js SDK](https://www.npmjs.com/package/@sendgrid/mail).

## 2. Create an email using React

Start by building your email template in a `.jsx` or `.tsx` file.

```tsx email.tsx

export function Email(props) {
  const { url } = props;

  return (
    
      Click me
    
  );
}
```

## 3. Convert to HTML and send email

Import the email template you just built, convert into an HTML string, and use the SendGrid SDK to send it.

```tsx

sendgrid.setApiKey(process.env.SENDGRID_API_KEY);

const emailHtml = await render();

const options = {
  from: "you@example.com",
  to: "user@gmail.com",
  subject: "hello world",
  html: emailHtml,
};

sendgrid.send(options);
```

## Try it yourself

---

# Guides

## React Intl

React Email supports [React Intl](https://formatjs.github.io/react-intl/) for internationalization.

This guide shows how to convert an English React Email template to support multiple locales.

## Prerequisites

To get the most out of this guide, you’ll need to:

- [Set up React Email](/getting-started/automatic-setup)
- [Install React Intl](https://formatjs.github.io/docs/getting-started/installation)

This guide will use the following email template as a base.

```jsx emails/welcome.jsx
export default function WelcomeEmail({ name }) {
  return (
    
      
      Welcome to Acme
      
        
          
            
              
                Welcome to Acme
              
              
                Hi {name}
              
              
                Thanks for signing up! We're excited to have you on board.
              
              <Button
                href="https://example.com/dashboard"
                className="bg-indigo-600 rounded-md text-white text-base font-semibold no-underline text-center block py-3 px-6 my-6"
              >
                Get Started
              
              
              
                If you have any questions, reply to this email. We're here to help!
              
            
          
        
      
    
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
};
```

## Internationalization with React Intl

React Intl is a library for internationalization and localization that provides a way to format messages in different languages.

### 1. Create messages for each locale

For each locale, create a new JSON file containing the content of the email in that locale.

Alternatively, you can add locale-specific messages in the email file.

```jsx Example expandable
const messages = {
  en: {
    header: 'Welcome to Acme',
    hi: 'Hi',
    thanks: 'Thanks for signing up! We\'re excited to have you on board.',
    'get-started': 'Get Started',
    questions: 'If you have any questions, reply to this email. We\'re here to help!',
  },
  es: {
    header: 'Bienvenido a Acme',
    hi: 'Hola',
    thanks: 'Gracias por registrarte! Estamos emocionados de tenerte en la plataforma.',
    'get-started': 'Comenzar',
    questions: 'Si tienes alguna pregunta, responde a este correo electrónico. Estamos aquí para ayudarte!',
  },
  pt: {
    header: 'Bem-vindo ao Acme',
    hi: 'Olá',
    thanks: 'Obrigado por se inscrever! Estamos ansiosos para te receber na plataforma.',
    'get-started': 'Começar',
    questions: 'Se você tiver alguma dúvida, responda a este e-mail. Estamos aqui para ajudar!',
  },
};
```

### 2. Update the email props

Add the `locale` prop to the email template, interface, and test data.

```jsx emails/welcome.jsx 
// [!code --]
export default function WelcomeEmail({ name }) {
// [!code ++]
export default function WelcomeEmail({ name, locale }) {
  return (
   ...
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
// [!code ++]
  locale: 'en',
};
```

### 3. Update the email template

In the email template, remove the hardcoded content and use `createIntl` to format the email message strings.

```jsx emails/welcome.jsx
// [!code ++]

export default async function WelcomeEmail({ name, locale }) {
// [!code ++:4]
  const { formatMessage } = createIntl({
    locale,
    messages: await import(`../messages/${locale}/welcome-email.json`), // if using locale-specific files
  });

  return (
    
      
// [!code --]
      Welcome to Acme
// [!code ++]
      {formatMessage({ id: 'header' })}
      
        
          
            
              
// [!code --]
                Welcome to Acme
// [!code ++]
                {formatMessage({ id: 'header' })}
              
              
// [!code --]
                Hi {name}
// [!code ++]
                {formatMessage({ id: 'hi' })} {name}
              
              
// [!code --]
                Thanks for signing up! We're excited to have you on board.
// [!code ++]
                {formatMessage({ id: 'thanks' })}
              
              <Button
                href="https://example.com/dashboard"
                className="bg-indigo-600 rounded-md text-white text-base font-semibold no-underline text-center block py-3 px-6 my-6"
              >
// [!code --]
                Get Started
// [!code ++]
                {formatMessage({ id: 'get-started' })}
              
              
              
// [!code --]
                If you have any questions, reply to this email. We're here to help!
// [!code ++]
                {formatMessage({ id: 'questions' })}
              
            
          
        
      
    
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
  locale: 'en',
};
```

### 4. Update any email calls

When calling the email template, pass the `locale` prop to the email component.

## Try it yourself

---

## next-intl

React Email supports [next-intl](https://next-intl.dev) for internationalization.

This guide shows how to convert an English React Email template to support multiple locales.

## Prerequisites

To get the most out of this guide, you’ll need to:

- [Set up React Email](/getting-started/automatic-setup)
- [Install next-intl](https://next-intl.dev/docs/getting-started/app-router)

This guide will use the following email template as a base.

```jsx emails/welcome.jsx
export default function WelcomeEmail({ name }) {
  return (
    
      
      Welcome to Acme
      
        
          
            
              
                Welcome to Acme
              
              
                Hi {name}
              
              
                Thanks for signing up! We're excited to have you on board.
              
              <Button
                href="https://example.com/dashboard"
                className="bg-indigo-600 rounded-md text-white text-base font-semibold no-underline text-center block py-3 px-6 my-6"
              >
                Get Started
              
              
              
                If you have any questions, reply to this email. We're here to help!
              
            
          
        
      
    
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
};
```

## Internationalization with next-intl

next-intl is a library for internationalization and localization for Next.js that provides a way to format messages in different languages.

### 1. Create messages for each locale

For each locale, create a new JSON file containing the content of the email in that locale.

### 2. Update the email props

Add the `locale` prop to the email template, interface, and test data.

```jsx emails/welcome.jsx 
// [!code --]
export default function WelcomeEmail({ name }) {
// [!code ++]
export default function WelcomeEmail({ name, locale }) {
  return (
   ...
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
// [!code ++]
  locale: 'en',
};
```

### 3. Update the email template

In the email template, remove the hardcoded content and use `createTranslator` function to format the email message strings.

```jsx emails/welcome.jsx
// [!code ++]

export default async function WelcomeEmail({ name, locale }) {
// [!code ++:5]
  const t = createTranslator({
    messages: await import(`../messages/${locale}.json`),
    namespace: 'welcome-email',
    locale,
  });

  return (
    
      
// [!code --]
      Welcome to Acme
// [!code ++]
      {t('header')}
      
        
          
            
              
// [!code --]
                Welcome to Acme
// [!code ++]
                {t('header')}
              
              
// [!code --]
                Hi {name}
// [!code ++]
                {t('hi')} {name}
              
              
// [!code --]
                Thanks for signing up! We're excited to have you on board.
// [!code ++]
                {t('thanks')}
              
              <Button
                href="https://example.com/dashboard"
                className="bg-indigo-600 rounded-md text-white text-base font-semibold no-underline text-center block py-3 px-6 my-6"
              >
// [!code --]
                Get Started
// [!code ++]
                {t('get-started')}
              
              
              
// [!code --]
                If you have any questions, reply to this email. We're here to help!
// [!code ++]
                {t('questions')}
              
            
          
        
      
    
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
  locale: 'en',
};
```

You can't use other APIs here because the preview server will not have access to the next intl context that you might have defined in your Next.js app.

### 4. Update any email calls

When calling the email template, pass the `locale` prop to the email component.

## Try it yourself

---

## react-i18next

React Email supports [react-i18next](https://react.i18next.com) for internationalization.

This guide shows how to convert an English React Email template to support multiple locales.

## Prerequisites

To get the most out of this guide, you’ll need to:

- [Set up React Email](/getting-started/automatic-setup)
- [Install react-i18next](https://react.i18next.com/getting-started)

This guide will use the following email template as a base.

```jsx emails/welcome.jsx
export default function WelcomeEmail({ name }) {
  return (
    
      
      Welcome to Acme
      
        
          
            
              
                Welcome to Acme
              
              
                Hi {name}
              
              
                Thanks for signing up! We're excited to have you on board.
              
              <Button
                href="https://example.com/dashboard"
                className="bg-indigo-600 rounded-md text-white text-base font-semibold no-underline text-center block py-3 px-6 my-6"
              >
                Get Started
              
              
              
                If you have any questions, reply to this email. We're here to help!
              
            
          
        
      
    
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
};
```

## Internationalization with react-i18next

react-i18next is a library for internationalization and localization that provides a way to format messages in different languages.

### 1. Create messages for each locale

For each locale, create a new JSON file containing the content of the email in that locale.

### 2. Update the email props

Add the `locale` prop to the email template, interface, and test data.

```jsx emails/welcome.jsx 
// [!code --]
export default function WelcomeEmail({ name }) {
// [!code ++]
export default function WelcomeEmail({ name, locale }) {
  return (
   ...
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
// [!code ++]
  locale: 'en',
};
```

### 3. Setting up helpers

If you don't already, go ahead and create a `getT` helper meant for getting translations on the server:

```js get-t.js expandable

export async function getT(namespace, locale) {
  if (locale && i18next.resolvedLanguage !== locale) {
    await i18next.changeLanguage(locale)
  }
  if (namespace && !i18next.hasLoadedNamespace(namespace)) {
    await i18next.loadNamespaces(namespace)
  }
  return {
    t: i18next.getFixedT(
      locale ?? i18next.resolvedLanguage,
      Array.isArray(namespace) ? namespace[0] : namespace,
    ),
    i18n: i18next
  }
}
```

Where `./i18n` is where you would have setup your i18next, for example:

```js i18n.js expandable

i18next
  .use(initReactI18next)
  .use(resourcesToBackend((language, namespace) => import(`messages/${language}/${namespace}.json`)))
  .init({
    supportedLngs: ['en', 'es', 'pt'],
    fallbackLng: 'en',
    lng: undefined,
    detection: {
      order: ['path', 'htmlTag', 'cookie', 'navigator']
    },
    preload: typeof window === 'undefined' ? ['en', 'es', 'pt'] : [],
  });

export { i18next };
```

### 4. Update the email template

In the email template, remove the hardcoded content and use `getT`'s `t` to format the email message strings.

```jsx emails/welcome.jsx
// [!code ++]

export default async function WelcomeEmail({ name, locale }) {
// [!code ++]
  const { t } = await getT('welcome-email', locale);

  return (
    
      
// [!code --]
      Welcome to Acme
// [!code ++]
      {t('header')}
      
        
          
            
              
// [!code --]
                Welcome to Acme
// [!code ++]
                {t('header')}
              
              
// [!code --]
                Hi {name}
// [!code ++]
                {t('hi')} {name}
              
              
// [!code --]
                Thanks for signing up! We're excited to have you on board.
// [!code ++]
                {t('thanks')}
              
              <Button
                href="https://example.com/dashboard"
                className="bg-indigo-600 rounded-md text-white text-base font-semibold no-underline text-center block py-3 px-6 my-6"
              >
// [!code --]
                Get Started
// [!code ++]
                {t('get-started')}
              
              
              
// [!code --]
                If you have any questions, reply to this email. We're here to help!
// [!code ++]
                {t('questions')}
              
            
          
        
      
    
  );
}

WelcomeEmail.PreviewProps = {
  name: 'John Lennon',
  locale: 'en',
};
```

### 5. Update any email calls

When calling the email template, pass the `locale` prop to the email component.

## Try it yourself

---

# Editor

## Bubble Menu

## Quick start

Add `BubbleMenu.Default` as a child of `EditorProvider` to get a fully-featured formatting toolbar:

```tsx

const extensions = [StarterKit];

export function MyEditor() {
  return (
    
      
    
  );
}
```

Select text to see the toolbar with formatting, alignment, node type selection, and link controls.

## Excluding items

Hide specific items from the default bubble menu using `excludeItems`:

```tsx

```

All excludable item keys:

| Key | Description |
| -- | -- |
| `bold` | Bold toggle |
| `italic` | Italic toggle |
| `underline` | Underline toggle |
| `strike` | Strikethrough toggle |
| `code` | Inline code toggle |
| `uppercase` | Uppercase toggle |
| `align-left` | Left alignment |
| `align-center` | Center alignment |
| `align-right` | Right alignment |
| `node-selector` | Block type selector (paragraph, headings, etc.) |
| `link-selector` | Link add/edit control |

## Hiding on specific nodes or marks

Prevent the bubble menu from appearing on certain node types or when certain marks are active:

```tsx
<BubbleMenu.Default
  hideWhenActiveNodes={['codeBlock', 'button']}
  hideWhenActiveMarks={['link']}
/>
```

This is useful when combining the text bubble menu with contextual menus for links, images, or buttons -- each gets its own menu via `BubbleMenu.Root`:

```tsx

const linkPluginKey = new PluginKey('linkBubbleMenu');

{/* Hide text bubble menu on links and buttons -- their own menus handle those */}

<BubbleMenu.Root
  trigger={bubbleMenuTriggers.nodeWithoutSelection('link')}
  pluginKey={linkPluginKey}
>
  
    
    
    
  

```

## Composing from primitives

For full control, build a custom bubble menu using the compound component API:

```tsx

export function MyEditor() {
  return (
    
      
        
          
          
          
        
        
          
          
          
        
      
    
  );
}
```

`BubbleMenu.Root` wraps everything, `BubbleMenu.ItemGroup` creates visual groupings,
and individual items render the toggle buttons.

## Available items

| Component | Description |
| -- | -- |
| `BubbleMenu.Bold` | Bold toggle |
| `BubbleMenu.Italic` | Italic toggle |
| `BubbleMenu.Underline` | Underline toggle |
| `BubbleMenu.Strike` | Strikethrough toggle |
| `BubbleMenu.Code` | Inline code toggle |
| `BubbleMenu.Uppercase` | Uppercase toggle |
| `BubbleMenu.AlignLeft` | Left alignment |
| `BubbleMenu.AlignCenter` | Center alignment |
| `BubbleMenu.AlignRight` | Right alignment |
| `BubbleMenu.NodeSelector` | Block type dropdown (paragraph, h1-h3, etc.) |
| `BubbleMenu.LinkSelector` | Link add/edit popover |
| `BubbleMenu.Separator` | Visual separator between groups |

## Placement and offset

Control where the bubble menu appears relative to the selection:

```tsx

  {/* items */}

```

---

## BubbleMenu

Everything is accessed through a single import:

```tsx
```

## Pre-built menus

Drop-in menus for common use cases. Each one handles its own trigger logic and plugin key.

### BubbleMenu.Default

Text formatting toolbar that appears on text selection.

```tsx

```

### BubbleMenu.LinkDefault

Link editing menu that appears when clicking a link.

```tsx

```

### BubbleMenu.ButtonDefault

Button link editing menu that appears when clicking a button.

```tsx

```

Same props as `LinkDefault` (except `excludeItems`).

### BubbleMenu.ImageDefault

Image editing menu that appears when clicking an image.

```tsx

```

---

## Combining menus

A typical email editor uses multiple bubble menus together. Use `hideWhenActiveNodes` and `hideWhenActiveMarks`
to prevent overlapping menus:

```tsx

  <BubbleMenu.Default
    hideWhenActiveNodes={['image', 'button']}
    hideWhenActiveMarks={['link']}
  />
  
  
  

```

---

## Compound components

Build fully custom menus using the compound API.

### BubbleMenu.Root

Base container for all custom bubble menus. Provides editor context to children.

```tsx

const myPluginKey = new PluginKey('myCustomMenu');

<BubbleMenu.Root
  trigger={bubbleMenuTriggers.node('image')}
  pluginKey={myPluginKey}
  placement="top"
>
  {/* your custom menu content */}

```

### bubbleMenuTriggers

Factory for common `trigger` functions:

| Trigger | Description |
| -- | -- |
| `bubbleMenuTriggers.textSelection(hideNodes?, hideMarks?)` | Show on text selection. This is the default. |
| `bubbleMenuTriggers.node(name)` | Show when a specific node type is active (e.g., `'button'`, `'image'`) |
| `bubbleMenuTriggers.nodeWithoutSelection(name)` | Show when a node is active but no text is selected (e.g., `'link'`) |

### Text formatting items

| Component | Description |
| -- | -- |
| `BubbleMenu.ItemGroup` | Visual grouping of items |
| `BubbleMenu.Separator` | Divider between groups |
| `BubbleMenu.Bold` | Bold toggle |
| `BubbleMenu.Italic` | Italic toggle |
| `BubbleMenu.Underline` | Underline toggle |
| `BubbleMenu.Strike` | Strikethrough toggle |
| `BubbleMenu.Code` | Inline code toggle |
| `BubbleMenu.Uppercase` | Uppercase toggle |
| `BubbleMenu.AlignLeft` | Left alignment |
| `BubbleMenu.AlignCenter` | Center alignment |
| `BubbleMenu.AlignRight` | Right alignment |
| `BubbleMenu.NodeSelector` | Block type dropdown |
| `BubbleMenu.LinkSelector` | Link add/edit popover |

### Link components

| Component | Description |
| -- | -- |
| `BubbleMenu.LinkToolbar` | Wrapper -- hides when editing mode is active |
| `BubbleMenu.LinkEditLink` | Button that enters editing mode |
| `BubbleMenu.LinkUnlink` | Removes the link |
| `BubbleMenu.LinkOpenLink` | Opens the link in a new tab |
| `BubbleMenu.LinkForm` | Inline form for editing link URLs |

### Button components

| Component | Description |
| -- | -- |
| `BubbleMenu.ButtonToolbar` | Wrapper -- hides when editing mode is active |
| `BubbleMenu.ButtonEditLink` | Button that enters editing mode |
| `BubbleMenu.ButtonUnlink` | Removes the button link |
| `BubbleMenu.ButtonForm` | Inline form for editing button URLs |

### Image components

| Component | Description |
| -- | -- |
| `BubbleMenu.ImageToolbar` | Wrapper -- hides when editing mode is active |
| `BubbleMenu.ImageEditLink` | Button that enters editing mode |

---

## Custom menu example

Here's a complete custom link bubble menu built from compound components:

```tsx

const linkKey = new PluginKey('myLinkMenu');

function MyLinkMenu() {
  return (
    <BubbleMenu.Root
      trigger={bubbleMenuTriggers.nodeWithoutSelection('link')}
      pluginKey={linkKey}
      placement="top"
    >
      
        
        
        
      
      
    
  );
}
```

The `LinkToolbar` automatically hides when `LinkEditLink` is clicked, and `LinkForm`
appears in its place. When the user submits or cancels, the toolbar reappears.

---

## Context

Use `useBubbleMenuContext()` inside any child of `BubbleMenu.Root` to access the editor and editing state:

```tsx

function CustomToolbarItem() {
  const { editor, isEditing, setIsEditing } = useBubbleMenuContext();

  return (
     setIsEditing(true)}>
      Edit
    
  );
}
```

| Field | Type | Description |
| -- | -- | -- |
| `editor` | `Editor` | The TipTap editor instance |
| `isEditing` | `boolean` | Whether the menu is in editing mode |
| `setIsEditing` | `(value: boolean) => void` | Toggle editing mode |

---

## CSS import

```tsx
```

  `@react-email/editor/themes/default.css` bundles all UI component styles.
  Unless you need to cherry-pick, use this single import:

```tsx
```

---

## Buttons

## Quick start

Add `BubbleMenu.ButtonDefault` and a slash command for inserting buttons:

```tsx

const extensions = [StarterKit];

const content = `
  Click the button below to see its bubble menu.
  Click me
  Use the slash command menu (type /) to insert more buttons.
`;

export function MyEditor() {
  return (
    
      
      
    
  );
}
```

## Button content format

Buttons in the editor are represented as styled anchor elements:

```html

  
    Click me
  

```

The wrapping `div` controls alignment (left, center, or right), while the `` tag renders
as a styled button in the editor and serializes to a React Email `` component on export.

## Editing buttons

When you click a button in the editor, the button bubble menu appears with:

- **Edit link** (pencil icon) -- Opens an inline form to change the button's URL
- **Unlink** -- Removes the button link

The form validates URLs and lets you apply or cancel changes inline.

## Inserting buttons programmatically

Use the `setButton` command to insert a button via the editor API:

```tsx
editor.chain().focus().setButton().run();
```

This can be triggered from a custom toolbar:

```tsx

function Toolbar() {
  const { editor } = useCurrentEditor();
  if (!editor) return null;

  return (
     editor.chain().focus().setButton().run()}>
      Insert Button
    
  );
}
```

---

## Column Layouts

## Quick start

Column extensions are included in `StarterKit` by default — no extra imports needed:

```tsx

const extensions = [StarterKit];

export function MyEditor() {
  return ;
}
```

## Inserting columns programmatically

Use the `insertColumns` command to add a column layout:

```tsx
// Insert a 2-column layout
editor.chain().focus().insertColumns(2).run();

// Insert a 3-column layout
editor.chain().focus().insertColumns(3).run();

// Insert a 4-column layout
editor.chain().focus().insertColumns(4).run();
```

## Building a toolbar

Here's a complete example with a toolbar for inserting column layouts, using the `slotBefore`
prop to position it above the editor:

```tsx

const extensions = [StarterKit];

function ToolbarButton({
  label,
  icon,
  onClick,
}: {
  label: string;
  icon?: React.ReactNode;
  onClick: () => void;
}) {
  return (
    
      {icon}
      {label}
    
  );
}

function Toolbar() {
  const { editor } = useCurrentEditor();
  if (!editor) return null;

  return (
    
      <ToolbarButton
        label="2 columns"
        icon={}
        onClick={() => editor.chain().focus().insertColumns(2).run()}
      />
      <ToolbarButton
        label="3 columns"
        icon={}
        onClick={() => editor.chain().focus().insertColumns(3).run()}
      />
      <ToolbarButton
        label="4 columns"
        icon={}
        onClick={() => editor.chain().focus().insertColumns(4).run()}
      />
    
  );
}

export function MyEditor() {
  return (
    <EditorProvider
      extensions={extensions}
      content={content}
      slotBefore={}
    />
  );
}
```

  Use `slotBefore` to render custom UI above the editor, and `useCurrentEditor()` to access
  the editor instance from child components.

## Via slash commands

The default slash commands already include column layouts. Type `/` and search for "columns":

- **Two Columns** — `TWO_COLUMNS`
- **Three Columns** — `THREE_COLUMNS`
- **Four Columns** — `FOUR_COLUMNS`

See [Slash Commands](/editor/features/slash-commands) for setup details.

---

## Custom Extensions

## EmailNode vs TipTap Node

The editor uses `EmailNode` instead of TipTap's standard `Node`, which is a class that extends `Node`. The key difference is a
required `renderToReactEmail()` method that tells the serializer how to convert the node to
a React Email component for HTML export.

```
TipTap Node
├── name, group, content
├── parseHTML()
├── renderHTML()          ← How it looks in the editor
└── ...

EmailNode (extends Node)
├── name, group, content
├── parseHTML()
├── renderHTML()          ← How it looks in the editor
├── renderToReactEmail()  ← How it looks in the exported email HTML
└── ...
```

## Creating a custom node

Here's a complete example of a custom "Callout" node that renders as a highlighted block:

```tsx

const Callout = EmailNode.create({
  name: 'callout',
  group: 'block',
  content: 'inline*',

  parseHTML() {
    return [{ tag: 'div[data-callout]' }];
  },

  renderHTML({ HTMLAttributes }) {
    return [
      'div',
      mergeAttributes(HTMLAttributes, {
        'data-callout': '',
        style:
          'padding: 12px 16px; background: #f4f4f5; border-left: 3px solid #1c1c1c; border-radius: 4px; margin: 8px 0;',
      }),
      0,
    ];
  },

  renderToReactEmail({ children, style }) {
    return (
      <div
        style={{
          ...style,
          padding: '12px 16px',
          backgroundColor: '#f4f4f5',
          borderLeft: '3px solid #1c1c1c',
          borderRadius: '4px',
          margin: '8px 0',
        }}
      >
        {children}
      
    );
  },
});
```

Key methods:

- **`parseHTML()`** — Defines which HTML elements get parsed into this node (for clipboard paste, HTML content)
- **`renderHTML()`** — Controls how the node appears in the editor (in the browser DOM)
- **`renderToReactEmail()`** — Controls how the node is serialized when exporting to email HTML via `composeReactEmail`

## Registering the extension

Add your custom extension to the extensions array alongside `StarterKit`:

```tsx
const extensions = [StarterKit, Callout];
```

## Inserting custom nodes

Use the editor's `insertContent` command to programmatically insert your custom node:

```tsx

function Toolbar() {
  const { editor } = useCurrentEditor();
  if (!editor) return null;

  return (
    <button
      onClick={() =>
        editor
          .chain()
          .focus()
          .insertContent({
            type: 'callout',
            content: [{ type: 'text', text: 'New callout' }],
          })
          .run()
      }
    >
      Insert Callout
    
  );
}
```

## Complete example

Here's the full editor setup with the custom Callout extension, a toolbar, and a bubble menu:

```tsx

const Callout = EmailNode.create({
  name: 'callout',
  group: 'block',
  content: 'inline*',

  parseHTML() {
    return [{ tag: 'div[data-callout]' }];
  },

  renderHTML({ HTMLAttributes }) {
    return [
      'div',
      mergeAttributes(HTMLAttributes, {
        'data-callout': '',
        style:
          'padding: 12px 16px; background: #f4f4f5; border-left: 3px solid #1c1c1c; border-radius: 4px; margin: 8px 0;',
      }),
      0,
    ];
  },

  renderToReactEmail({ children, style }) {
    return (
      <div
        style={{
          ...style,
          padding: '12px 16px',
          backgroundColor: '#f4f4f5',
          borderLeft: '3px solid #1c1c1c',
          borderRadius: '4px',
          margin: '8px 0',
        }}
      >
        {children}
      
    );
  },
});

const extensions = [StarterKit, Callout];

const content = {
  type: 'doc',
  content: [
    {
      type: 'paragraph',
      content: [
        {
          type: 'text',
          text: 'This editor includes a custom Callout node. Use the toolbar to insert one.',
        },
      ],
    },
    {
      type: 'callout',
      content: [
        { type: 'text', text: 'This is a callout block — a custom extension!' },
      ],
    },
  ],
};

function Toolbar() {
  const { editor } = useCurrentEditor();
  if (!editor) return null;

  return (
    <button
      onClick={() =>
        editor
          .chain()
          .focus()
          .insertContent({
            type: 'callout',
            content: [{ type: 'text', text: 'New callout' }],
          })
          .run()
      }
    >
      
      Insert Callout
    
  );
}

export function MyEditor() {
  return (
    <EditorProvider
      extensions={extensions}
      content={content}
      slotBefore={}
    >
      
    
  );
}
```

## Wrapping existing TipTap extensions

Both `EmailNode` and `EmailMark` provide a `.from()` method that wraps an existing TipTap
extension with email serialization support. This is useful when you want to reuse a community
TipTap extension and add email export support without rewriting it.

```tsx

const MyTipTapNode = Node.create({ /* ... */ });

const MyEmailNode = EmailNode.from(MyTipTapNode, ({ children, style }) => {
  return {children};
});
```

```tsx

const MyTipTapMark = Mark.create({ /* ... */ });

const MyEmailMark = EmailMark.from(MyTipTapMark, ({ children, style }) => {
  return {children};
});
```

**Note:** 
  For full API details on all methods (`create`, `from`, `configure`, `extend`), see the
  [`EmailNode`](/editor/api-reference/email-node) and [`EmailMark`](/editor/api-reference/email-mark)
  reference pages.

## Configure and extend

Both `EmailNode` and `EmailMark` support TipTap's standard customization methods:

```tsx
// Configure options
const CustomHeading = Heading.configure({ levels: [1, 2] });

// Extend with additional behavior
const CustomParagraph = Paragraph.extend({
  addKeyboardShortcuts() {
    return {
      'Mod-Shift-p': () => this.editor.commands.setParagraph(),
    };
  },
});
```

---

## Editor

The React Email Editor is a visual WYSIWYG editor for composing email templates in React. It produces email-safe HTML through React Email components and is built on top of [TipTap](https://tiptap.dev/) and [ProseMirror](https://prosemirror.net/).

## Key features

- **Rich text editing** — Paragraphs, headings, lists, code blocks, tables, and more
- **Bubble menus** — Floating formatting toolbars that appear on text selection
- **Slash commands** — Insert content blocks by typing `/`
- **Multi-column layouts** — Two, three, and four column email layouts
- **Email theming** — Built-in themes with customizable CSS properties
- **HTML export** — Convert editor content to email-ready HTML and plain text
- **Custom extensions** — Create your own email-compatible nodes and marks

## Architecture

The editor is organized into five entry points:

| Import | Purpose |
|--------|---------|
| `@react-email/editor/core` | `useEditor` hook, `composeReactEmail` serialization, event bus |
| `@react-email/editor/extensions` | `StarterKit` and 35+ email-aware extensions |
| `@react-email/editor/ui` | Bubble menus, slash commands |
| `@react-email/editor/plugins` | Email theming plugin |
| `@react-email/editor/utils` | Attribute helpers, style utilities |

**Note:** 
  The editor uses [TipTap](https://tiptap.dev/) under the hood, so [TipTap](https://tiptap.dev/) and [ProseMirror](https://prosemirror.net/) concepts apply.
  Extensions are email-aware versions of TipTap nodes and marks that know how to serialize to React Email components.

## Quick links

  
  
  
  
  
  
  

---

## Email Export

## Quick start

Use `composeReactEmail` to convert editor content into email-ready HTML and plain text:

```tsx

const extensions = [StarterKit, EmailTheming];

const content = `
  My Email Newsletter
  Edit this content, then click Export HTML to see the generated email markup.
  The exported HTML uses React Email components and is ready to send.
`;

function ExportPanel() {
  const { editor } = useCurrentEditor();
  const [html, setHtml] = useState('');
  const [exporting, setExporting] = useState(false);

  const handleExport = async () => {
    if (!editor) return;
    setExporting(true);
    const result = await composeReactEmail({ editor, preview: null });
    setHtml(result.html);
    setExporting(false);
  };

  return (
    
      
        {exporting ? 'Exporting...' : 'Export HTML'}
      
      {html && (
        
      )}
    
  );
}

export function MyEditor() {
  return (
    
      
      
    
  );
}
```

## How it works

The `composeReactEmail` function follows this pipeline:

1. **Read** the editor's JSON document
2. **Traverse** each node and mark in the document tree
3. **Call** `renderToReactEmail()` on each `EmailNode` and `EmailMark` extension
4. **Apply** theme styles via the `SerializerPlugin` (if `EmailTheming` is configured)
5. **Wrap** the content in a `BaseTemplate` component
6. **Renders** to an HTML string and plain text version using [render](/utilities/render)

The return value is:

```tsx
const { html, text } = await composeReactEmail({ editor, preview: null });

// html  — Full HTML email string, ready to send
// text  — Plain text version for email clients that don't support HTML
```

## Preview text

The `preview` parameter sets the email preview text — the snippet shown in inbox list views
before the email is opened:

```tsx
const result = await composeReactEmail({
  editor,
  preview: 'Check out our latest updates!',
});
```

Pass `null` to omit preview text.

## Using with theming

When the `EmailTheming` extension is in your extensions array, theme styles are automatically
injected into the exported HTML. The serializer uses the `SerializerPlugin` provided by
`EmailTheming` to resolve styles for each node based on the current theme and depth in the
document tree.

```tsx
const extensions = [StarterKit, EmailTheming.configure({ theme: 'basic' })];

// Later, when exporting:
const { html } = await composeReactEmail({ editor, preview: null });
// html includes all theme styles inline
```

## Full example with export panel

Here's a complete editor with theming and an export panel:

```tsx
  BubbleMenu,
  defaultSlashCommands,
  SlashCommand,
} from '@react-email/editor/ui';

type EditorTheme = 'basic' | 'minimal';

function ControlPanel() {
  const { editor } = useCurrentEditor();
  const [html, setHtml] = useState('');
  const [exporting, setExporting] = useState(false);

  const handleExport = async () => {
    if (!editor) return;
    setExporting(true);
    const result = await composeReactEmail({ editor, preview: null });
    setHtml(result.html);
    setExporting(false);
  };

  return (
    
      
        {exporting ? 'Exporting...' : 'Export HTML'}
      
      {html && (
        <textarea
          readOnly
          value={html}
          rows={16}
          style={{ width: '100%', fontFamily: 'monospace', fontSize: '12px' }}
        />
      )}
    
  );
}

export function FullEmailBuilder() {
  const [theme, setTheme] = useState('basic');
  const extensions = [StarterKit, EmailTheming.configure({ theme })];

  const content = `
    Weekly Newsletter
    Edit this content, then click Export HTML to see the generated email markup.
  `;

  return (
    
      
         setTheme('basic')}>Basic Theme
         setTheme('minimal')}>Minimal Theme
      
      
        
        
        
        
        
      
    
  );
}
```

---

## Email Theming

## Quick start

Import the `EmailTheming` plugin and add it to your extensions:

```tsx

const extensions = [StarterKit, EmailTheming];

export function MyEditor() {
  return (
    
      
    
  );
}
```

## How theming works

Themes are CSS-in-JS style objects that map to email component types (headings, paragraphs,
links, buttons, etc.). Each theme defines a set of `React.CSSProperties` for every supported
component.

During [`composeReactEmail`](/editor/api-reference/compose-react-email), the `EmailTheming`
plugin acts as a `SerializerPlugin` that resolves styles for each node based on its type and
depth in the document tree. These styles are then **inlined directly** onto the rendered React
Email components as `style` attributes — this is necessary because email clients don't
reliably support `` tags or external stylesheets.

The resolved styles are passed to each node's `renderToReactEmail()` method via the `style`
prop, where they can be spread onto the rendered element.

## Built-in themes

The editor ships with two themes:

| Theme | Description |
|-------|-------------|
| `'basic'` | Full styling — typography, spacing, borders, and visual hierarchy. This is the default. |
| `'minimal'` | Essentially no styles. Gives you a blank slate to build your own look from scratch. |

Select a theme with `.configure()`:

```tsx
const extensions = [StarterKit, EmailTheming.configure({ theme: 'basic' })];
```

## Switching themes dynamically

Use React state to toggle themes at runtime. Re-key the `EditorProvider` to apply the new theme:

```tsx

type EditorTheme = 'basic' | 'minimal';

export function MyEditor() {
  const [theme, setTheme] = useState('basic');
  const extensions = [StarterKit, EmailTheming.configure({ theme })];

  return (
    
      
         setTheme('basic')}>Basic
         setTheme('minimal')}>Minimal
      
      
        
      
    
  );
}
```

**Note:** 
  The `key={theme}` on `EditorProvider` forces React to remount the editor when the theme changes,
  ensuring the new theme is applied cleanly.

## Theme components

Themes define styles for the following email components:

| Component | Description |
|-----------|-------------|
| `reset` | CSS reset styles |
| `body` | Email body wrapper |
| `container` | Content container |
| `h1` | Level 1 heading |
| `h2` | Level 2 heading |
| `h3` | Level 3 heading |
| `paragraph` | Text paragraphs |
| `list` | Ordered and unordered lists |
| `listItem` | Individual list items |
| `listParagraph` | Paragraphs inside list items |
| `nestedList` | Nested list styles |
| `blockquote` | Block quotes |
| `codeBlock` | Code blocks |
| `inlineCode` | Inline code |
| `link` | Hyperlinks |
| `button` | Email buttons |
| `section` | Content sections |
| `footer` | Footer area |
| `hr` | Horizontal rules |
| `image` | Images |

## Theme-aware serialization

When `EmailTheming` is in your extensions array, the `composeReactEmail` function automatically
applies theme styles to the exported HTML. No extra configuration needed:

```tsx

// Theme styles are automatically injected into the HTML output
const { html, text } = await composeReactEmail({ editor, preview: null });
```

See [Email Export](/editor/features/email-export) for more details on the serialization pipeline.

---

## EmailMark

`EmailMark` extends TipTap's `Mark` class with an additional `renderToReactEmail()` method
that controls how the mark is serialized when exporting to email HTML via
[`composeReactEmail`](/editor/api-reference/compose-react-email).

Marks are used for inline formatting like bold, italic, links, and custom text annotations.

## Import

```tsx
```

## EmailMark.create

Create a new email-compatible mark from scratch.

```tsx
const Highlight = EmailMark.create({
  name: 'highlight',

  parseHTML() {
    return [{ tag: 'mark' }];
  },

  renderHTML({ HTMLAttributes }) {
    return ['mark', HTMLAttributes, 0];
  },

  renderToReactEmail({ children, style }) {
    return (
      {children}
    );
  },
});
```

The config object accepts all standard [TipTap Mark options](https://tiptap.dev/docs/editor/api/mark)
plus the `renderToReactEmail` method.

### renderToReactEmail props

| Prop | Type | Description |
|------|------|-------------|
| `children` | `React.ReactNode` | The content wrapped by this mark |
| `style` | `React.CSSProperties` | Resolved theme styles for this mark (empty object if no theme) |
| `mark` | `Mark` | The ProseMirror mark instance |
| `node` | `Node` | The ProseMirror node that contains this mark |
| `extension` | `EmailMark` | The extension instance, useful for accessing `options` |

## EmailMark.from

Wrap an existing TipTap mark with email serialization support. This is useful when you want to
reuse a community TipTap extension and add email export support without rewriting it.

```tsx

const EmailStrike = EmailMark.from(Strike, ({ children, style }) => {
  return {children};
});
```

The second argument is the `renderToReactEmail` renderer component. It receives the same props
as described above.

## .configure

Configure options on an `EmailMark` (same as TipTap's `.configure()`):

```tsx

const CustomBold = Bold.configure({ HTMLAttributes: { class: 'custom-bold' } });
```

## .extend

Extend an `EmailMark` with additional behavior:

```tsx

const CustomLink = Link.extend({
  addKeyboardShortcuts() {
    return {
      'Mod-k': () => this.editor.commands.toggleLink({ href: '' }),
    };
  },
});
```

You can also override `renderToReactEmail` when extending:

```tsx
const CustomLink = Link.extend({
  renderToReactEmail({ children, style, mark }) {
    return (
      <a
        href={mark.attrs.href}
        style={{ ...style, color: '#0066cc', textDecoration: 'underline' }}
      >
        {children}
      
    );
  },
});
```

## See also

- [Custom Extensions](/editor/advanced/custom-extensions) — tutorial on building custom extensions
- [`EmailNode`](/editor/api-reference/email-node) — the equivalent class for block nodes
- [`composeReactEmail`](/editor/api-reference/compose-react-email) — the function that calls `renderToReactEmail`

---

## EmailNode

`EmailNode` extends TipTap's `Node` class with an additional `renderToReactEmail()` method
that controls how the node is serialized when exporting to email HTML via
[`composeReactEmail`](/editor/api-reference/compose-react-email).

## Import

```tsx
```

## EmailNode.create

Create a new email-compatible node from scratch.

```tsx
const MyNode = EmailNode.create({
  name: 'myNode',
  group: 'block',
  content: 'inline*',

  parseHTML() {
    return [{ tag: 'div[data-my-node]' }];
  },

  renderHTML({ HTMLAttributes }) {
    return ['div', mergeAttributes(HTMLAttributes, { 'data-my-node': '' }), 0];
  },

  renderToReactEmail({ children, style }) {
    return {children};
  },
});
```

The config object accepts all standard [TipTap Node options](https://tiptap.dev/docs/editor/api/node)
plus the `renderToReactEmail` method.

### renderToReactEmail props

| Prop | Type | Description |
|------|------|-------------|
| `children` | `React.ReactNode` | The serialized child content of this node |
| `style` | `React.CSSProperties` | Resolved theme styles for this node (empty object if no theme) |
| `node` | `Node` | The ProseMirror node instance |
| `extension` | `EmailNode` | The extension instance, useful for accessing `options` |

## EmailNode.from

Wrap an existing TipTap node with email serialization support. This is useful when you want to
reuse a community TipTap extension and add email export support without rewriting it.

```tsx

const EmailBlockquote = EmailNode.from(Blockquote, ({ children, style }) => {
  return (
    
      {children}
    
  );
});
```

The second argument is the `renderToReactEmail` renderer component. It receives the same props
as described above.

## .configure

Configure options on an `EmailNode` (same as TipTap's `.configure()`):

```tsx

const CustomHeading = Heading.configure({ levels: [1, 2] });
```

## .extend

Extend an `EmailNode` with additional behavior:

```tsx

const CustomParagraph = Paragraph.extend({
  addKeyboardShortcuts() {
    return {
      'Mod-Shift-p': () => this.editor.commands.setParagraph(),
    };
  },
});
```

You can also override `renderToReactEmail` when extending:

```tsx
const CustomParagraph = Paragraph.extend({
  renderToReactEmail({ children, style }) {
    return {children};
  },
});
```

## See also

- [Custom Extensions](/editor/advanced/custom-extensions) — tutorial on building custom nodes
- [`EmailMark`](/editor/api-reference/email-mark) — the equivalent class for inline marks
- [`composeReactEmail`](/editor/api-reference/compose-react-email) — the function that calls `renderToReactEmail`

---

## Event Bus

## Overview

The editor provides a typed event bus for communication between components. It's a singleton
instance built on the browser's native `CustomEvent` API with events prefixed as
`@react-email/editor:`.

```tsx
```

## Dispatching events

Fire an event with a payload:

```tsx
editorEventBus.dispatch('bubble-menu:add-link', undefined);
```

## Listening to events

Subscribe to events and clean up when done:

```tsx

function MyComponent() {
  useEffect(() => {
    const subscription = editorEventBus.on('bubble-menu:add-link', () => {
      console.log('Link addition triggered');
    });

    return () => {
      subscription.unsubscribe();
    };
  }, []);

  return null;
}
```

The `on` method returns an object with an `unsubscribe` function. Always unsubscribe in a
cleanup function to avoid memory leaks.

## Built-in events

| Event | Payload | Description |
|-------|---------|-------------|
| `bubble-menu:add-link` | `undefined` | Triggered when the "add link" action is initiated from the bubble menu |

## Adding custom events

Use TypeScript module augmentation to register custom events with full type safety:

```tsx
declare module '@react-email/editor/core' {
  interface EditorEventMap {
    'my-feature:custom-event': { data: string };
    'my-feature:another-event': { count: number };
  }
}
```

Then dispatch and listen with full type checking:

```tsx
// TypeScript knows the payload type
editorEventBus.dispatch('my-feature:custom-event', { data: 'hello' });

editorEventBus.on('my-feature:custom-event', (payload) => {
  // payload is typed as { data: string }
  console.log(payload.data);
});
```

## Event targets

By default, events are dispatched on `window`. You can scope events to a specific DOM element
using the `target` option:

```tsx
// Dispatch on a specific element
const container = document.getElementById('my-editor');
editorEventBus.dispatch('bubble-menu:add-link', undefined, {
  target: container,
});

// Listen on a specific element
editorEventBus.on('bubble-menu:add-link', handler, {
  target: container,
});
```

This is useful when you have multiple editor instances on the same page and want events
to stay scoped to their respective editors.

---

## Extensions

## StarterKit

`StarterKit` bundles all 35+ editor extensions into a single import. It wraps TipTap's
StarterKit and replaces most nodes with email-aware versions that know how to serialize
to React Email components.

```tsx

const extensions = [StarterKit];
```

  Use `StarterKit` unless you need fine-grained control over which extensions are loaded.
  It's the recommended way to set up the editor.

## Configuring extensions

Pass options to configure individual extensions, or set them to `false` to disable:

```tsx
const extensions = [
  StarterKit.configure({
    // Customize heading levels
    Heading: { levels: [1, 2] },

    // Disable strikethrough
    Strike: false,

    // Disable code blocks
    CodeBlockPrism: false,
  }),
];
```

## Using individual extensions

For maximum control, import and compose extensions manually instead of using StarterKit:

```tsx
  Body,
  Bold,
  Heading,
  Italic,
  Link,
  Paragraph,
} from '@react-email/editor/extensions';

const extensions = [Body, Paragraph, Heading, Bold, Italic, Link];
```

  When using individual extensions, you're responsible for including all the extensions
  your content needs. Missing extensions will cause those content types to be dropped.

## Extension categories

For the full API reference with configurable options for each extension, see [Extensions Reference](/editor/api-reference/extensions-list).

---

## Extensions Reference

All extensions are available from `@react-email/editor/extensions` and are included
in `StarterKit` by default. Each can be configured via `StarterKit.configure()` or

---

## Getting Started

## Prerequisites

  The editor requires **React 18+** and a bundler that supports [package exports](https://nodejs.org/api/packages.html#exports) (Vite, Next.js, webpack 5, etc.).

## Install

Install the editor and its peer dependencies:

## Import CSS

The editor ships CSS for its UI components and a default theme. Import the styles you need:

```tsx
// Required for bubble menu styling (covers text, link, button, and image menus)

// Required for slash command menu

// Default color theme
```

  **Shortcut:** `@react-email/editor/themes/default.css` bundles all of the above CSS files
  into a single import. If you don't need to cherry-pick styles, just import this one file:

  ```tsx
  import '@react-email/editor/themes/default.css';
  ```

**Note:** 
  If you prefer to keep your bundle lean, you can import only the CSS for the components you
  use instead of the bundled theme file.

## Minimal editor

The simplest setup uses `StarterKit` with `EditorProvider` — no UI overlays, just a content-editable area
with all core extensions (paragraphs, headings, lists, tables, code blocks, and more):

```tsx

const extensions = [StarterKit];

const content = {
  type: 'doc',
  content: [
    {
      type: 'paragraph',
      content: [
        {
          type: 'text',
          text: 'Start typing or edit this text.',
        },
      ],
    },
  ],
};

export function MyEditor() {
  return ;
}
```

## Adding a bubble menu

To add a floating formatting toolbar that appears when you select text, add `BubbleMenu.Default`
as a child of `EditorProvider`:

```tsx

const extensions = [StarterKit];

const content = {
  type: 'doc',
  content: [
    {
      type: 'paragraph',
      content: [
        { type: 'text', text: 'Select this text to see the bubble menu. Try ' },
        { type: 'text', marks: [{ type: 'bold' }], text: 'bold' },
        { type: 'text', text: ', ' },
        { type: 'text', marks: [{ type: 'italic' }], text: 'italic' },
        { type: 'text', text: ', and other formatting options.' },
      ],
    },
  ],
};

export function MyEditor() {
  return (
    
      
    
  );
}
```

Select text in the editor to see the formatting toolbar with bold, italic, underline, alignment, and more.

## Content format

The editor accepts content in two formats:

**TipTap JSON** — A structured document tree:

```json
{
  "type": "doc",
  "content": [
    {
      "type": "paragraph",
      "content": [
        { "type": "text", "text": "Hello world" }
      ]
    }
  ]
}
```

**HTML string** — Parsed automatically into the editor's document model:

```tsx
const content = `
  Welcome
  This is a link.
`;

```

## Next steps

---

## Link Editing

## Quick start

Use `BubbleMenu.LinkDefault` to add an inline link editing toolbar:

```tsx

const extensions = [StarterKit];

const content = `
  Click on this link to see the link bubble menu.
  Try adding more links by selecting text and pressing Cmd+K.
`;

export function MyEditor() {
  return (
    
      
    
  );
}
```

## How it works

When you click on a link in the editor, the link bubble menu appears with:

- **Edit button** -- Opens an inline form to change the URL
- **Open button** -- Opens the link in a new tab
- **Unlink button** -- Removes the link, keeping the text

To **add a new link**, select text and press `Cmd+K` (or `Ctrl+K` on Windows/Linux).

## Using with the text bubble menu

When combining the link bubble menu with `BubbleMenu.Default`, use `hideWhenActiveMarks` to prevent
the text bubble menu from appearing when a link is focused:

```tsx

  
  

```

Without `hideWhenActiveMarks`, both menus would try to show at the same time when a link is selected.

## HTML content with links

When using HTML strings as content, `` tags are automatically parsed into the editor's
link model:

```tsx
const content = `
  Visit React Email for more info.
`;
```

The link extension is included in `StarterKit` with `openOnClick` disabled by default,
so clicking a link in edit mode focuses it rather than navigating away.

---

## Slash Commands

## Quick start

Add `SlashCommand.Root` with the default command set:

```tsx

const extensions = [StarterKit];

export function MyEditor() {
  return (
    
      
    
  );
}
```

Type `/` in the editor to open the command menu. Use arrow keys to navigate and Enter to select.

## Default commands

The `defaultSlashCommands` array includes these built-in commands:

| Command | Category | Description |
|---------|----------|-------------|
| `TEXT` | Text | Plain text block |
| `H1` | Text | Large heading |
| `H2` | Text | Medium heading |
| `H3` | Text | Small heading |
| `BULLET_LIST` | Text | Unordered list |
| `NUMBERED_LIST` | Text | Ordered list |
| `QUOTE` | Text | Block quote |
| `CODE` | Text | Code snippet |
| `BUTTON` | Layout | Clickable button |
| `DIVIDER` | Layout | Horizontal separator |
| `SECTION` | Layout | Content section |
| `TWO_COLUMNS` | Layout | Two column layout |
| `THREE_COLUMNS` | Layout | Three column layout |
| `FOUR_COLUMNS` | Layout | Four column layout |

Each command is also exported individually, so you can cherry-pick:

```tsx

```

## Adding custom commands

Create a `SlashCommandItem` and include it in the items array:

```tsx
  defaultSlashCommands,
  SlashCommand,
  type SlashCommandItem,
} from '@react-email/editor/ui';

const GREETING: SlashCommandItem = {
  title: 'Greeting',
  description: 'Insert a greeting block',
  icon: ,
  category: 'Custom',
  searchTerms: ['hello', 'greeting', 'welcome'],
  command: ({ editor, range }) => {
    editor
      .chain()
      .focus()
      .deleteRange(range)
      .insertContent({
        type: 'paragraph',
        content: [{ type: 'text', text: 'Hello! Welcome to our newsletter.' }],
      })
      .run();
  },
};

export function MyEditor() {
  return (
    
      <SlashCommand.Root
        items={[...defaultSlashCommands, GREETING]}
      />
    
  );
}
```

The `SlashCommandItem` interface:

## Using individual commands

You can cherry-pick from the default commands to show only specific options:

```tsx

```

This is useful when you want a minimal command palette — for example, only allowing button insertion.

## Controlling visibility

```tsx
<SlashCommand.Root
  items={defaultSlashCommands}
  char="/"
  allow={({ editor }) => !editor.isActive('codeBlock')}
/>
```

---

## SlashCommand

Command menu triggered by typing a character (default: `/`).

## SlashCommand.Root

```tsx

```

### Custom rendering

Use the `children` render function to fully customize how the command list looks.
The render function receives the filtered items, current query, selected index,
and a callback to select an item:

```tsx

  {({ items, query, selectedIndex, onSelect }) => (
    
      {items.map((item, index) => (
        <button
          key={item.title}
          onClick={() => onSelect(index)}
          data-selected={index === selectedIndex}
          className="my-command-item"
        >
          {item.icon}
          
            {item.title}
            {item.description}
          
        
      ))}
      {items.length === 0 && (
        
          No results for "{query}"
        
      )}
    
  )}

```

### Custom commands

Pass your own items to add domain-specific commands alongside (or instead of) the defaults:

```tsx

const customCommands = [
  ...defaultSlashCommands,
  {
    title: 'Image',
    description: 'Insert an image',
    searchTerms: ['photo', 'picture', 'img'],
    icon: ,
    category: 'Media',
    command: ({ editor, range }) => {
      editor.chain().focus().deleteRange(range).setImage({ src: '' }).run();
    },
  },
];

```

---

## SlashCommandItem

```tsx
interface SlashCommandItem {
  title: string;
  description: string;
  searchTerms?: string[];
  icon: ReactNode;
  category: string;
  command: (props: { editor: Editor; range: Range }) => void;
}
```

---

## SlashCommandRenderProps

```tsx
interface SlashCommandRenderProps {
  items: SlashCommandItem[];
  query: string;
  selectedIndex: number;
  onSelect: (index: number) => void;
}
```

---

## Default commands

The `defaultSlashCommands` export includes these built-in commands:

| Command | Category | Description |
|---------|----------|-------------|
| Text | Basic | Plain text paragraph |
| Heading 1 | Headings | Level 1 heading |
| Heading 2 | Headings | Level 2 heading |
| Heading 3 | Headings | Level 3 heading |
| Numbered List | Lists | Ordered list |
| Bullet List | Lists | Unordered list |
| Quote | Basic | Block quote |
| Section | Layout | Content section |
| 2 Columns | Layout | Two-column layout |
| 3 Columns | Layout | Three-column layout |
| 4 Columns | Layout | Four-column layout |
| Divider | Basic | Horizontal rule |
| Code | Basic | Code block |
| Button | Basic | Email button |

---

## CSS import

```tsx
```

---

## Styling

The editor's UI is fully customizable through CSS. Every component uses `data-re-*` attributes
as stable styling hooks, and a set of CSS custom properties (`--re-*`) control the entire color scheme.

## CSS variables

The default theme defines these CSS custom properties on `:root`. Override them on any parent
element to restyle the editor:

```css
.my-editor {
  --re-bg: #1a1a2e;
  --re-text: #eaeaea;
  --re-border: #2a2a3e;
}
```

### Color variables

| Variable | Description | Light default | Dark default |
|----------|-------------|--------------|--------------|
| `--re-bg` | Background color | `#fff` | `#1c1c1c` |
| `--re-border` | Border color | `#e5e5e5` | `#2e2e2e` |
| `--re-text` | Primary text color | `#1c1c1c` | `#ececec` |
| `--re-text-muted` | Secondary/muted text | `#6b6b6b` | `#a0a0a0` |
| `--re-hover` | Hover background | `rgba(0,0,0,0.04)` | `rgba(255,255,255,0.06)` |
| `--re-active` | Active/click background | `rgba(0,0,0,0.06)` | `rgba(255,255,255,0.09)` |
| `--re-pressed` | Pressed/toggled background | `rgba(0,0,0,0.06)` | `rgba(255,255,255,0.09)` |
| `--re-separator` | Separator line color | `#e5e5e5` | `#2e2e2e` |
| `--re-danger` | Destructive action color | `#dc2626` | `#f87171` |
| `--re-danger-hover` | Destructive hover background | `rgba(220,38,38,0.1)` | `rgba(248,113,113,0.15)` |

### Dimension variables

| Variable | Description | Default |
|----------|-------------|---------|
| `--re-radius` | Border radius for containers (menus, dropdowns) | `0.75rem` |
| `--re-radius-sm` | Border radius for buttons and items | `0.5rem` |
| `--re-shadow` | Box shadow for floating elements | `0 10px 15px -3px rgba(0,0,0,0.1), ...` |

### Dark mode

The default theme supports dark mode in two ways:

**Automatic** — via `prefers-color-scheme`:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --re-bg: #1c1c1c;
    --re-text: #ececec;
    /* ... dark values applied automatically */
  }
}
```

**Class-based** — via a `.dark` class on any ancestor:

```css
.dark {
  --re-bg: #1c1c1c;
  --re-text: #ececec;
  /* ... */
}
```

This works out of the box with class-based dark mode libraries (e.g., `next-themes`).

## Data attribute selectors

Every UI component uses `data-re-*` attributes as stable CSS hooks. These are the recommended
way to target specific parts of the editor UI.

### Bubble menu

```css
/* Menu container */
[data-re-bubble-menu] { }

/* Item groups (formatting, alignment) */
[data-re-bubble-menu-group] { }

/* Individual toggle buttons */
[data-re-bubble-menu-item] { }

/* Active/pressed state */
[data-re-bubble-menu-item][data-active] { }

/* Target a specific item by name */
[data-re-bubble-menu-item][data-item="bold"] { }
[data-re-bubble-menu-item][data-item="italic"] { }

/* Separator between groups */
[data-re-bubble-menu-separator] { }
```

Available `data-item` values: `bold`, `italic`, `underline`, `strike`, `code`, `uppercase`,
`align-left`, `align-center`, `align-right`.

### Node selector

The block type dropdown inside the bubble menu:

```css
/* Dropdown wrapper */
[data-re-node-selector] { }

/* Trigger button (shows current block type) */
[data-re-node-selector-trigger] { }

/* Dropdown content panel */
[data-re-node-selector-content] { }

/* Individual block type option */
[data-re-node-selector-item] { }

/* Currently active block type */
[data-re-node-selector-item][data-active] { }
```

### Link selector

The link popover inside the bubble menu:

```css
/* Wrapper */
[data-re-link-selector] { }

/* Trigger button */
[data-re-link-selector-trigger] { }

/* Edit form container */
[data-re-link-selector-form] { }

/* URL input field */
[data-re-link-selector-input] { }

/* Apply button */
[data-re-link-selector-apply] { }

/* Unlink/remove button */
[data-re-link-selector-unlink] { }
```

### Link bubble menu

The standalone menu that appears when clicking a link:

```css
/* Container */
[data-re-link-bm] { }

/* Toolbar with action buttons */
[data-re-link-bm-toolbar] { }

/* Action buttons */
[data-re-link-bm-item] { }
[data-re-link-bm-item][data-item="edit-link"] { }
[data-re-link-bm-item][data-item="open-link"] { }
[data-re-link-bm-item][data-item="unlink"] { }

/* Edit form */
[data-re-link-bm-form] { }
[data-re-link-bm-input] { }
[data-re-link-bm-apply] { }
[data-re-link-bm-unlink] { }
```

### Button bubble menu

The menu that appears when clicking an email button:

```css
/* Container */
[data-re-btn-bm] { }

/* Toolbar */
[data-re-btn-bm-toolbar] { }

/* Action buttons */
[data-re-btn-bm-item] { }
[data-re-btn-bm-item][data-item="edit-link"] { }
```

### Image bubble menu

The menu that appears when clicking an image:

```css
/* Container */
[data-re-img-bm] { }

/* Toolbar */
[data-re-img-bm-toolbar] { }

/* Action buttons */
[data-re-img-bm-item] { }
[data-re-img-bm-item][data-item="edit-link"] { }
```

### Slash command

```css
/* Command palette container */
[data-re-slash-command] { }

/* Individual command item */
[data-re-slash-command-item] { }

/* Currently highlighted item */
[data-re-slash-command-item][data-selected] { }

/* Category header (e.g., "Text", "Layout") */
[data-re-slash-command-category] { }

/* Empty state ("No results") */
[data-re-slash-command-empty] { }
```

## Editor content classes

The editor content area uses the `.tiptap` root class from [TipTap](https://tiptap.dev/docs/editor/getting-started/style-editor). Target content elements with
`.tiptap` as a prefix:

### Typography

```css
/* All editor content */
.tiptap { }

/* Headings */
.tiptap h1 { }
.tiptap h2 { }
.tiptap h3 { }

/* Paragraphs */
.tiptap p { }

/* Block quotes */
.tiptap blockquote { }

/* Horizontal rules */
.tiptap hr { }

/* Code */
.tiptap code { }       /* inline code */
.tiptap pre { }        /* code block */
.tiptap pre code { }   /* code inside block */

/* Lists */
.tiptap ul { }
.tiptap ol { }
```

### Layout and structure

```css
/* Column layouts */
.tiptap .node-columns { }
.tiptap .node-column { }

/* Sections */
.tiptap .node-section { }

/* Email buttons */
.tiptap .node-button { }

/* Links */
.tiptap .node-link { }

/* Placeholder text */
.tiptap .node-placeholder::before { }
```

### Text alignment

The alignment attribute renders as an HTML attribute on block nodes:

```css
.tiptap [alignment="left"] { text-align: left; }
.tiptap [alignment="center"] { text-align: center; }
.tiptap [alignment="right"] { text-align: right; }
```

### Column data types

Column layouts also use `data-type` attributes:

```css
.tiptap [data-type="two-columns"] { }
.tiptap [data-type="three-columns"] { }
.tiptap [data-type="four-columns"] { }
.tiptap [data-type="column"] { }
.tiptap [data-type="section"] { }
```

## Examples

### Custom brand colors

Override the CSS variables to match your brand:

```css
.my-editor {
  --re-bg: #fafaf9;
  --re-border: #d6d3d1;
  --re-text: #1c1917;
  --re-text-muted: #78716c;
  --re-hover: rgba(28, 25, 23, 0.04);
  --re-active: rgba(28, 25, 23, 0.08);
  --re-pressed: rgba(28, 25, 23, 0.08);
  --re-radius: 0.5rem;
  --re-radius-sm: 0.25rem;
}
```

```tsx

  
    
  

```

### Custom bubble menu item styles

Increase icon size and change the active state color:

```css
[data-re-bubble-menu-item] svg {
  width: 1rem;
  height: 1rem;
}

[data-re-bubble-menu-item][data-active] {
  background: #3b82f6;
  color: #fff;
}
```

### Custom slash command appearance

Make the command palette wider with a custom background:

```css
[data-re-slash-command] {
  width: 320px;
  max-height: 400px;
  background: #f8fafc;
}

[data-re-slash-command-item][data-selected] {
  background: #e0f2fe;
}

[data-re-slash-command-category] {
  color: #64748b;
  font-size: 0.625rem;
}
```

### Styling editor content

Customize how content looks inside the editor:

```css
/* Custom heading styles */
.tiptap h1 {
  font-size: 1.75rem;
  letter-spacing: -0.025em;
  color: #0f172a;
}

/* Custom blockquote */
.tiptap blockquote {
  border-left: 4px solid #3b82f6;
  background: #eff6ff;
  padding: 0.75rem 1rem;
  border-radius: 0.25rem;
}

/* Custom column gap */
.tiptap .node-columns {
  gap: 1rem;
}

/* Custom button appearance in the editor */
.tiptap .node-button {
  background: #2563eb;
  color: #fff;
  padding: 0.5rem 1.5rem;
  border-radius: 0.375rem;
  text-decoration: none;
}
```

  Content styling in the editor (via `.tiptap` selectors) only affects how content looks while
  editing. The exported email HTML is styled separately via the [Theming](/editor/features/theming) system.

---

## Theming API

## EmailTheming extension

The `EmailTheming` extension from `@react-email/editor/plugins` adds theme-aware styling
to the editor and provides a `SerializerPlugin` for theme-aware HTML export.

```tsx

const extensions = [StarterKit, EmailTheming.configure({ theme: 'basic' })];
```

## Types

### EditorTheme

```tsx
type EditorTheme = 'basic' | 'minimal';
```

---

### KnownThemeComponents

All component keys that a theme can style:

```tsx
type KnownThemeComponents =
  | 'reset'
  | 'body'
  | 'container'
  | 'h1'
  | 'h2'
  | 'h3'
  | 'paragraph'
  | 'list'
  | 'listItem'
  | 'listParagraph'
  | 'nestedList'
  | 'blockquote'
  | 'codeBlock'
  | 'inlineCode'
  | 'link'
  | 'button'
  | 'section'
  | 'footer'
  | 'hr'
  | 'image';
```

---

### KnownCssProperties

CSS properties that can be customized per theme component:

**Layout:** `align`, `width`, `height`, `padding`, `paddingTop`, `paddingRight`,
`paddingBottom`, `paddingLeft`, `margin`, `marginTop`, `marginRight`, `marginBottom`,
`marginLeft`

**Appearance:** `backgroundColor`, `color`, `borderRadius`, `borderWidth`, `borderColor`,
`borderStyle`

**Typography:** `fontSize`, `fontWeight`, `lineHeight`, `textDecoration`, `fontFamily`,
`letterSpacing`

---

### CssJs

A mapping of theme component keys to CSS properties:

```tsx
type CssJs = Partial>;
```

---

### PanelGroup

Represents a group of configurable theme properties for a component:

```tsx
interface PanelGroup {
  id: string;
  title: string;
  headerSlot?: React.ReactNode;
  classReference?: string;
  inputs: PanelInputProperty[];
}
```

---

### PanelInputProperty

An individual configurable CSS property within a panel:

```tsx
interface PanelInputProperty {
  label: string;
  type: 'text' | 'number' | 'color' | 'select';
  value: string;
  prop: string;
  classReference: string;
  unit?: string;
  options?: { label: string; value: string }[];
  placeholder?: string;
  category?: string;
}
```

## Utility functions

### getMergedCssJs

Merges the base theme styles with custom panel overrides:

```tsx

const mergedStyles = getMergedCssJs(theme, panelStyles);
```

---

### getResolvedNodeStyles

Resolves the final CSS styles for a specific node based on theme and document depth:

```tsx

const styles = getResolvedNodeStyles(node, depth, mergedCssJs);
```

---

### getThemeComponentKey

Maps a node type and depth to a theme component key:

```tsx

const paragraphKey = getThemeComponentKey('paragraph', 0); // 'paragraph'
const nestedListKey = getThemeComponentKey('bulletList', 2); // 'nestedList'
```

---

### stylesToCss

Converts a theme's style definitions to a CSS object:

```tsx

const css = stylesToCss(styles, theme);
```

---

### useEmailTheming

React hook that provides access to the current theme state from within the editor:

```tsx

function MyComponent() {
  const theming = useEmailTheming(editor);
  // Access theming.styles, theming.theme, theming.css
}
```

---

## composeReactEmail

The `composeReactEmail` function is the core of the editor's email export system. It takes
the editor's document tree, walks every node and mark, calls each extension's
`renderToReactEmail()` method, applies theme styles, wraps everything in an email-ready
template, and produces both HTML and plain text output.

## Import

```tsx
```

## Signature

```tsx
async function composeReactEmail(params: {
  editor: Editor;
  preview: string | null;
}): Promise;
```

## Parameters

## Return value

Returns a `Promise` that resolves to an object with:

| Field | Type | Description |
|-------|------|-------------|
| `html` | `string` | Full HTML email string, ready to send |
| `text` | `string` | Plain text version for email clients that don't support HTML |

Both are generated in parallel for performance.

---

## The serialization pipeline

Understanding how `composeReactEmail` works helps you write better custom extensions and
debug rendering issues.

### 1. Extract document and extensions

The function reads the editor's JSON document (via `editor.getJSON()`) and collects all
registered extensions into a name-to-extension map for fast lookup.

### 2. Find the SerializerPlugin

It searches extensions for one that provides a `SerializerPlugin` — an interface with two
methods:

- **`getNodeStyles(node, depth, editor)`** — returns `React.CSSProperties` for a given node
- **`BaseTemplate({ previewText, children, editor })`** — wraps the serialized content in an email structure

The [`EmailTheming`](/editor/features/theming) extension implements this interface. If no
plugin is found, styles default to `{}` and the built-in `DefaultBaseTemplate` is used.

### 3. Traverse the document tree

It recursively walks the ProseMirror document. For each node it:

1. **Resolves styles** — calls `serializerPlugin.getNodeStyles(node, depth, editor)` to get
   theme styles, then merges any inline styles from the node's attributes
2. **Renders unknown nodes as `null`** — if the node type isn't registered or isn't an
   [`EmailNode`](/editor/api-reference/email-node), it returns `null`
3. **Renders the node** — calls the extension's `renderToReactEmail()` component, passing
   `children` (from recursing into child nodes), `style`, `node`, and `extension`
4. **Wraps with marks** — iterates through the node's marks (bold, italic, link, etc.) and
   wraps the rendered output with each mark's `renderToReactEmail()`

### 4. Depth tracking

Depth starts at `0` and only increments inside list nodes (`bulletList`, `orderedList`).
This enables different styling for nested vs. top-level elements — for example, paragraphs
inside list items use the `listParagraph` theme key instead of `paragraph`.

### 5. Style resolution order

Styles are resolved in this priority (highest wins):

1. **Inline styles** — styles set directly on a node via the editor (e.g., text alignment)
2. **Theme styles** — styles from the active theme via `getNodeStyles()`
3. **Extension defaults** — hardcoded styles in each extension's `renderToReactEmail()`

Inside each extension's renderer, these are typically merged:

```tsx
renderToReactEmail({ children, style, node }) {
  return (
    <p style={{
      ...style,                            // theme styles
      ...inlineCssToJs(node.attrs?.style), // inline overrides
    }}>
      {children}
    
  );
}
```

### 6. Wrap in BaseTemplate

The serialized content is wrapped in a `BaseTemplate` that provides the email's
outer structure.

The **default template** renders:

```tsx

  
    
    
    
    <meta
      content="telephone=no,address=no,email=no,date=no,url=no"
      name="format-detection"
    />
  
  {previewText && {previewText}}
  
    
      
        {children}
      
    
  

```

When [`EmailTheming`](/editor/features/theming) is active, its `BaseTemplate` replaces the
default — it adds theme-specific body/container styles and can inject global CSS via a
`` tag in the ``.

### 7. Render to HTML and plain text

The React tree is rendered to an HTML string using `@react-email/components`' `render()`
function. Both the formatted HTML and a plain text version (tags stripped, text preserved)
are produced in parallel from the final React tree.

---

## Usage

### Basic export

```tsx

const { html, text } = await composeReactEmail({ editor, preview: null });
```

### With preview text

The `preview` parameter sets the inbox preview snippet — the text shown before the email
is opened:

```tsx
const { html, text } = await composeReactEmail({
  editor,
  preview: 'Check out our latest updates!',
});
```

Pass `null` to omit preview text entirely.

### With theming

When the [`EmailTheming`](/editor/features/theming) extension is in your extensions array,
theme styles are automatically inlined into every node during export:

```tsx

const extensions = [StarterKit, EmailTheming.configure({ theme: 'basic' })];

// Theme styles are injected automatically — no extra config needed
const { html } = await composeReactEmail({ editor, preview: null });
```

### Full example with export panel

```tsx

function ExportPanel() {
  const { editor } = useCurrentEditor();
  const [html, setHtml] = useState('');
  const [exporting, setExporting] = useState(false);

  const handleExport = async () => {
    if (!editor) return;
    setExporting(true);
    const result = await composeReactEmail({ editor, preview: null });
    setHtml(result.html);
    setExporting(false);
  };

  return (
    
      
        {exporting ? 'Exporting...' : 'Export HTML'}
      
      {html && (
        <textarea
          readOnly
          value={html}
          rows={16}
          style={{ width: '100%', fontFamily: 'monospace' }}
        />
      )}
    
  );
}
```

---

## See also

- [`EmailNode`](/editor/api-reference/email-node) — defines how nodes serialize via `renderToReactEmail()`
- [`EmailMark`](/editor/api-reference/email-mark) — defines how marks serialize via `renderToReactEmail()`
- [Email Export](/editor/features/email-export) — guide with full editor + export examples
- [Theming](/editor/features/theming) — how `EmailTheming` provides styles and templates to the serializer

---

## useEditor

## Import

```tsx
```

## Parameters

Any additional [TipTap `UseEditorOptions`](https://tiptap.dev/docs/editor/api/editor#settings)
are also accepted and forwarded to the underlying TipTap editor.

## Return value

## Collaboration support

  When collaboration extensions are detected (`liveblocksExtension` or `collaboration`), the
  hook automatically:
  - Ignores the `content` parameter (content is managed by the collab provider)
  - Excludes the `UndoRedo` extension (collab extensions handle their own history)

## Example

Use `useEditor` directly when you need more control than `EditorProvider` offers:

```tsx

export function MyEditor() {
  const { editor, isEditorEmpty, contentError } = useEditor({
    content: { type: 'doc', content: [] },
    onUpdate: (editor) => {
      console.log('Content changed:', editor.getJSON());
    },
    onReady: (editor) => {
      console.log('Editor ready');
    },
  });

  if (contentError) {
    return Error: {contentError.message};
  }

  if (!editor) {
    return Loading...;
  }

  return (
    
       el && editor.setOptions({ element: el })} />
      {isEditorEmpty && Start typing...}
    
  );
}
```

  For most use cases, `EditorProvider` from `@tiptap/react` is simpler.
  Use `useEditor` when you need direct access to the editor instance before rendering,
  or when integrating with complex state management.

---

# Contributing

## Building

We use [tsup](https://github.com/egoist/tsup) to build most packages. (The only exception for this is the `@react-email/tailwind` package which currently uses `vite` due to a few issues with `tsup` and `tailwindcss`'s bundling.)

To build a package run:

```bash package/* (ex: package/render)
pnpm build
```

Building in each package will run `tsup` with a few settings, typically `src/index.ts --format esm,cjs --dts --external react`.
Tsup handles building both [ESM](https://nodejs.org/api/esm.html) and
[CJS](https://nodejs.org/docs/latest/api/modules.html) versions along with the type definitions exported from the entry point, `src/index.ts`, without bundling `react`, which can cause issues.

### Why build before publishing?

We build most of the packages before publishing for a few reasons:

1. All the exported types can be imported from the same place the JavaScript is imported
2. We have proper [CommonJS](https://nodejs.org/docs/latest/api/modules.html#modules-commonjs-modules)
and [ES Modules](https://nodejs.org/api/esm.html#modules-ecmascript-modules) support
3. Code that isn't exported is not published or downloaded

---

## Codebase overview

We've created this guide to help new contributors understand and navigate the React Email codebase.

## Top-level directories

After cloning the [React Email repository](https://github.com/resend/react-email) you will see a few root-level directories. Here's a brief overview of each:

  
    
      Directory
      Description
    
  
  
    
      
[apps](https://github.com/resend/react-email/tree/canary/apps)
      
      
        Here you can find all of the apps related to our online presence, like:
        - this documentation (under [apps/docs](https://github.com/resend/react-email/tree/canary/apps/docs)),
        - the demo emails we have on [demo.react.email](https://demo.react.email/preview/notifications/vercel-invite-user)
          (under [apps/demo](https://github.com/resend/react-email/tree/canary/apps/demo))
        - the Next app we have for our landing page on [react.email](https://react.email) (under [apps/web](https://github.com/resend/react-email/tree/canary/apps/web))
      
    
    
      
[benchmarks](https://github.com/resend/react-email/tree/canary/benchmarks)
      
      
        We make benchmarks from version-to-version to demonstrate data-observable performance gains with metrics like *p99 and p75*.

        For example, see the [Improved Performance for Tailwind Emails](https://resend.com/blog/improved-performance-for-tailwind-emails) benchmark.
      
    
    
      
        [packages](https://github.com/resend/react-email/tree/canary/packages)
      
      
        Most contributions will be made to the packages in this directory.

        This directory contains all our published [NPM](https://www.npmjs.com/) packages.
        Each subdirectory is a single component published as its own package, with the exception of a few packages that serve as shared configuration.
      
    
  

  Feel free to [open a discussion](https://github.com/resend/react-email/discussions/new?category=ideas) if you have suggestions on how to better structure these packages to make them more manageable and approachable.

## Multiple packages

The react-email repository is a [pnpm monorepo](https://pnpm.io/next/workspaces), which means it contains
multiple packages.

Because we use pnpm, you will need to use [pnpm](https://pnpm.io/) to install and run each package. If you do not have pnpm installed, we recommend you install it using [corepack](https://github.com/nodejs/corepack):

```bash
corepack enable
corepack prepare pnpm@latest --activate
```

Currently, we have the following packages:

  
    - [@react-email/body](https://github.com/resend/react-email/tree/canary/packages/body)
    - [@react-email/button](https://github.com/resend/react-email/tree/canary/packages/button)
    - [@react-email/code-block](https://github.com/resend/react-email/tree/canary/packages/code-block)
    - [@react-email/code-inline](https://github.com/resend/react-email/tree/canary/packages/code-inline)
    - [@react-email/column](https://github.com/resend/react-email/tree/canary/packages/column)
    - [@react-email/components](https://github.com/resend/react-email/tree/canary/packages/components)
    - [@react-email/container](https://github.com/resend/react-email/tree/canary/packages/container)
    - [create-email](https://github.com/resend/react-email/tree/canary/packages/create-email)
      - Used for our [automatic setup](/getting-started/automatic-setup)
  
  
    - [@react-email/font](https://github.com/resend/react-email/tree/canary/packages/font)
    - [@react-email/head](https://github.com/resend/react-email/tree/canary/packages/head)
    - [@react-email/heading](https://github.com/resend/react-email/tree/canary/packages/heading)
    - [@react-email/hr](https://github.com/resend/react-email/tree/canary/packages/hr)
    - [@react-email/html](https://github.com/resend/react-email/tree/canary/packages/html)
    - [@react-email/img](https://github.com/resend/react-email/tree/canary/packages/img)
    - [@react-email/link](https://github.com/resend/react-email/tree/canary/packages/link)
    - [@react-email/markdown](https://github.com/resend/react-email/tree/canary/packages/markdown)
    - [@react-email/preview](https://github.com/resend/react-email/tree/canary/packages/preview)
  
  
    - [react-email](https://github.com/resend/react-email/tree/canary/packages/react-email)
      - The package for our [email CLI](/cli)
    - [@react-email/preview-server](https://github.com/resend/react-email/tree/canary/packages/preview-server)
    - [@react-email/render](https://github.com/resend/react-email/tree/canary/packages/render)
    - [@react-email/row](https://github.com/resend/react-email/tree/canary/packages/row)
    - [@react-email/section](https://github.com/resend/react-email/tree/canary/packages/section)
    - [@react-email/tailwind](https://github.com/resend/react-email/tree/canary/packages/tailwind)
    - [@react-email/text](https://github.com/resend/react-email/tree/canary/packages/text)
  

Most of these packages are very small and can be easily understood by reading the code, so feel free to explore.

### Turborepo

We encourage using [turborepo](https://turbo.build/repo) to manage the packages.

It's often helpful to [install Turborepo globally](https://turbo.build/repo/docs/installing) to make it easier to run commands in any of the repositories. With a global installation, running `turbo build` in any of the packages will build both the package
you are on as well as the dependent packages. The global installation handles [version mismatching as well](https://turbo.build/repo/docs/installing#install-per-repository).

### The React Email CLI

The CLI is built using [commander](https://www.npmjs.com/package/commander), a CLI builder for node. It handles
parsing of command line arguments and ensuring that the syntax for the command is as expected.

The `build`, `dev`, and `start` commands all depend on the user first installing `@react-email/preview-server`.
Locally installing the preview server also includes all the required dependencies so you can run the necessary commands.

[nypm](https://www.npmjs.com/package/nypm) and [jiti](https://www.npmjs.com/package/jiti) work together to first ensure `@react-email/preview-server` is installed and then to import it into the CLI.

The Preview Server and the CLI work together. The CLI detects changes to files
in the user's dependency graph with [chokidar](https://www.npmjs.com/package/chokidar) and then sends
the updated files to the Preview Server using [socket.io](https://socket.io/). Other details, like the path to the user's emails directory, are handled through environment variables.

### The Preview Server

The Preview Server is a Next.js app that uses `esbuild` at runtime to bundle the
user's email templates and then renders them using the [render](/utilities/render) utility.

As changes from the CLI are passed through [socket.io](https://socket.io/) to the Preview Server, the preview updates automatically.

## Testing

For testing, we use [vitest](https://vitest.dev/). We prefer to define globals and run tests under the `happy-dom` environment.

We do not strictly enforce testing coverage, but encourage it.

For help testing, see our [Development workflow guide](/contributing/development-workflow/2-running-tests).

The `@react-email/render` package's `renderAsync` does a fair bit of magic to simulate `edge` and other environments that are not supported by `happy-dom`. For this use case, we override the [environment on a per-file basis](https://vitest.dev/guide/environment#environments-for-specific-files) for its tests

## Linting

We use [biomejs](https://biomejs.dev/) for linting and formatting. Both the linting and formatting are ensured by our GitHub CI so make sure you lint and format your code (`pnpm lint:fix`) before opening a PR or asking for a review on it.

For help linting and formatting, see our [Development workflow guide on linting](/contributing/development-workflow/3-linting).

## Building

We use [tsup](https://github.com/egoist/tsup) to build most packages. (The only exception for this is the `@react-email/tailwind` package which currently uses `vite` due to a few issues with `tsup` and `tailwindcss`'s bundling.) For help building packages, see our [Development workflow guide](/contributing/development-workflow/4-building).

Building in each package will run `tsup` with a few settings, typically `src/index.ts --format esm,cjs --dts --external react`.
Tsup handles building both ESM and CJS versions along with the type definitions exported from the entry point, `src/index.ts`, without bundling `react`, which can cause issues.

### Why build before publishing?

We build most of the packages before publishing for a few reasons:

1. All the exported types can be imported from the same place the JavaScript is imported
2. We have proper [CommonJS](https://nodejs.org/docs/latest/api/modules.html#modules-commonjs-modules)
and [ES Modules](https://nodejs.org/api/esm.html#modules-ecmascript-modules) support
3. Code that isn't exported is not published or downloaded

---

## Editing the components

To facilitate developing components, use the built-in [playground](https://github.com/resend/react-email/tree/canary/playground), which automatically hot reloads when you make changes to the components during development.

## 1. Create an email template

Create a new file at `playground/emails/testing.tsx`

```tsx playground/emails/testing.tsx

export default function Testing() {
  return 
    
      

      
        
          This is a testing email template.
        
      
    
  ;
}
```

The `.gitignore` file will ignore all changes in [playground/emails](https://github.com/resend/react-email/tree/canary/playground/emails) so you can test component changes and use cases in example templates without committing them to the repository.

## 2. Run playground server

```sh
pnpm dev
```

## 3. Open in your browser

Go to http://localhost:3000

---

## Getting Started

Thank you for considering contributing to React Email.

We've created this guide to help you better understand how to contribute to the project, even if you've never contributed to an open source project before.

## How to report bugs

To report a bug, please first read our guide on [opening issues](/contributing/opening-issues).

## How to contribute code

To open a pull request, please first read our guide on [opening pull requests](/contributing/opening-pull-requests), which outlines our process for RFCs and pull requests.

### Codebase overview
If you need help getting familiar with our codebase, we recommend reading our [Codebase overview guide](/contributing/codebase-overview).

### Development workflow guide
We have also created a Development workflow guide to help you get familiar with the development workflow for React Email. It includes instructions for:
1. [Setting up your development environment](/contributing/development-workflow/1-setup)
2. [Running tests](/contributing/development-workflow/2-running-tests)
3. [Linting](/contributing/development-workflow/3-linting)
4. [Building](/contributing/development-workflow/4-building)
5. [Writing documentation](/contributing/development-workflow/5-writing-docs)

---

## Linting

We use [biomejs](https://biomejs.dev/) for linting and formatting. Both linting and formatting are ensured by our GitHub CI, so before opening a PR or asking for a review, please lint and format your code.

## Check for linting issues
To check if there are any linting issues, run `pnpm lint` on the root of the workspace.

```bash
pnpm lint
```

To lint or format the entire project, run `pnpm lint:fix` on the root of the workspace.

```bash
pnpm lint:fix
```

Both the linting and formatting are ensured by our GitHub CI so make sure you lint and format your code before opening a PR or asking for a review on it.

---

## Opening issues

Opening issues is a crucial step in open-source, as issues keep projects stable and help maintainers understand the needs of the community.

To help us maintain a stable project, please observe the following guidelines and general rules:

## Open issues for bugs only

We ask that **issues are only opened for bugs**, and not for questions or feature requests. Questions and feature requests should be asked in [Discussions](https://github.com/resend/react-email/discussions).

## Include a proper reproduction

To ensure your issue can be addressed, please **include a proper reproduction**.

Please avoid:
- Setting the link to the reproduction pointing to our repository
- Providing a code snippet that does not sufficiently reproduce the issue

Failing to include a proper reproduction may require extra back-and-forth between you and us, slow the process of fixing the issue for you and others, and make it harder to check if the issue has been fixed on a new release.

## Test the latest versions before opening an issue

Before opening an issue regarding a bug, please test with both:
1. the latest canary version
2. the latest stable version

If the bug is fixed on canary, you can still open an issue, and we will tag it with `Fixed under canary` so others will know it has been fixed.

If you do find that the bug was introduced in a specific version, and an older
version didn't have the issue then you should mention that this is a regression
and in what versions it was introduced.

## Conclusion

Now that you are ready, click below to open an issue! Thank you so much for contributing.

  <a
    className="border-none transition-colors text-white rounded-md px-3 items-center flex text-small h-10 transition colors"
    href="https://github.com/resend/react-email/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=1.bug_report.yml"
    style={{ backgroundColor: '#238636' }}
  >
    Open new issue
  

---

## Opening pull requests

Thank you for considering opening a pull requests to the project. Without contributions, React Email would not be possible.

Before opening a pull request, please first view our [Development workflow](/contributing/development-workflow/1-setup). The setup guide will help you properly set up the project.

## Contribution guidelines

We ask all contributors follow a few guidelines before contributing.

### Discuss features before contributing

While our community is open-source, we ask that features be discussed before they are implemented.

To discuss a feature, please open up a [discussion](https://github.com/resend/react-email/discussions/new?category=ideas) as an [RFC](https://pt.wikipedia.org/wiki/Request_for_Comments).

Once we come to an agreement on the feature and its implementation, you are welcome to create the feature and open a pull request.

### Create an issue for a bug before contributing

If you've found a bug, and plan to fix it, please open up
[a proper issue](https://github.com/resend/react-email/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=1.bug_report.yml) first. While you develop your fix, the issue can help us track the work, allow for other voices to offer suggestions, provide workarounds for those facing the bug if possible, and finish fixing the bug if you are no longer able to fix the issue.

Whenever possible, please add tests to your fixes, to ensure that regressions aren't introduced in later versions of the codebase.

## Creating the pull request

Please create your pull request using the following steps:

1. Create [a fork](https://github.com/resend/react-email/fork) of the repo
2. Create a new branch that represents your changes
3. Make your changes and commit them to your branch
4. Create the pull request from your fork pointing to the `canary` branch

## Writing a good description

Once you open your pull request, we will need to review it. The better your communicate what you did, the easier and quicker we can review your PR.

Currently, we do not have a pull request template you can follow to help you, but you can follow some common guidelines.

### 1. Describe your intent

Every change has an intent.
- **Bug** fix pull requests intend fix issues.
- **Feature** pull requests add new features.

Understanding your intent helps maintainers read your code quicker, offer more helpful feedback, and ultimately merge your request.

### 2. Describe your technical difficulties

If you went through technical difficulties, describe them.

Explaining your difficulties also gives you a chance to describe your thought process, which solutions you considered and discarded, and why you chose the one you did. This process can help avoid unnecessary back and forth and allows us to provide more helpful feedback.

### 3. Write down the specific changes the pull request introduces

Writing down your specific changes—both generally and technically—makes it clear what your code does. Consider also including what key points your code does not address if appropriate to help us understand the scope of your work.

## Getting in touch with us

If you have any questions or need help, you can find us on [GitHub Discussions](https://github.com/resend/react-email/discussions).

---

## Running tests

For testing, we use [vitest](https://vitest.dev/). We prefer to define globals and run tests under the `happy-dom` environment.

The `@react-email/render` package's `renderAsync` does a fair bit of magic to simulate `edge` and other environments that are not supported by `happy-dom`. For this use case, we override the [environment on a per-file basis](https://vitest.dev/guide/environment#environments-for-specific-files) for its tests

We do not strictly enforce testing coverage, but encourage it. A good rule of thumb is that if you need to simulate use
cases to check whether a specific portion of code works, you should split it into a function with a matching unit test.

After you have gone through the [setup](/contributing/development-workflow/1-setup) run
`pnpm test` inside any package. This will run the tests only once. We have two
scripts defined on our packages for testing:

- `pnpm test`: Runs all the tests once. If you run it on the root, it will run the
  tests for all packages using
  [turborepo](/contributing/codebase-overview#turborepo)
- `pnpm test:watch`: Runs all the tests and watches for changes. Vitest
  automatically only runs the tests that are affected by the code you've
  changed.

---

## Setup

Before you can start developing, you will need to get the project setup.

**Note:** 
To contribute to the project, you must use **Node 18** or higher.

  
    ```bash
    git clone https://github.com/resend/react-email
    ```
  
  Enable pnpm through corepack}>
    ```bash inside of react-email
    corepack enable
    corepack prepare pnpm@latest --activate
    ```
  
  
    ```bash inside of react-email
    pnpm install
    ```
  
  
    ```bash inside of react-email
    pnpm link ./packages/react-email/dev -g
    ```
    
    Linking the CLI globally runs the CLI's source code when you use the `email-dev` command, avoiding the need to rebuild the CLI.
    
  

If you plan to contribute to the docs, view our [Writing docs](/contributing/development-workflow/5-writing-docs) guide for additional setup.

If you have any trouble, please [reach out on GitHub Discussions](https://github.com/resend/react-email/discussions) or consider [opening up an issue on GitHub](https://github.com/resend/react-email/issues/new?assignees=&labels=Type%3A+Bug&projects=&template=1.bug_report.yml) after reading the [issue guidelines](/contributing/opening-issues).

---

## Writing docs

We use [Mintlify](https://mintlify.com/) for our documentation.

To preview the docs, you just need to run:

```sh apps/docs
pnpm dev
```

Check out [Mintlify's development guide](https://mintlify.com/docs/development)
for a few more interesting development tools.

## Components

Mintlify uses `mdx` to allow us to write docs in a composable ways. Because of
`mdx`, we can build [our own
components](https://mintlify.com/docs/reusable-snippets#reusable-components)
but it's always best to use the components Mintlify already provides us. Before writing down a new component, check their [full list of components](https://mintlify.com/docs/content/components).

---
