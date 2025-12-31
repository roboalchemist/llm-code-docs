# React I18Next Documentation

Source: https://react.i18next.com/llms-full.txt

---

# Introduction

{% hint style="success" %}
🎉 Announcing [`i18next-cli`](https://github.com/i18next/i18next-cli):\
&#x20;       The New Official Toolkit for i18next.\
⇒ [Learn More](https://www.locize.com/blog/i18next-cli)
{% endhint %}

## What is react-i18next?

react-i18next is a powerful **internationalization** framework for [**React**](https://reactjs.org) / [**React Native**](https://reactnative.dev/) which is based on [**i18next**](https://www.i18next.com). Check out the [history of i18next](https://www.i18next.com/misc/the-history-of-i18next) and [when react-i18next was introduced](https://www.i18next.com/misc/the-history-of-i18next#v2).

{% hint style="info" %}
You should read the [i18next](https://www.i18next.com) documentation. The [configuration options](https://www.i18next.com/overview/configuration-options) and translation functionalities like [plurals](https://www.i18next.com/translation-function/plurals), [formatting](https://www.i18next.com/translation-function/formatting), [interpolation](https://www.i18next.com/translation-function/interpolation), ... are documented there.
{% endhint %}

The module provides multiple components eg. to assert that needed translations get loaded or that your content gets rendered when the language changes.

{% hint style="warning" %}
Managing JSON files manually?\
When your project grows, streamline your workflow with [locize](https://locize.com), the official TMS built by the creators of i18next. [**Try it for free!**](https://www.locize.com/i18next)
{% endhint %}

{% embed url="<https://www.youtube.com/watch?t=705s&v=SA_9i4TtxLQ>" %}

> **Official CLI**
>
> ⭐ [i18next-cli](https://github.com/i18next/i18next-cli)
>
> The official, high-performance, all-in-one command-line tool for i18next. It handles key extraction, code linting, locale syncing, and type generation. It's built with modern technologies for maximum speed and accuracy. This is the recommended tool for all i18next projects.

As react-i18next depends on [i18next](http://i18next.com) you can use it in any other UI framework and on the server-side (node.js, .net, ...) too. Like the React philosophy - just:

> **Learn once - translate everywhere**.

{% hint style="success" %}
Check out [this video](https://youtu.be/37rcHVcQ6t0) and the corresponding [blog post](https://www.locize.com/blog/how-to-easily-add-i18n-to-your-software) about "Vite + React + TypeScript" with i18next.

<img src="https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2F0NoUAddfsm34lCDr3VhV%2Ftitle1.png?alt=media&#x26;token=1ef7f6d1-c2c5-415b-915b-fae394982d2e" alt="" data-size="original">
{% endhint %}

{% hint style="success" %}
[Here](https://locize.com/blog/react-i18next/) you'll find a simple tutorial on how to best use react-i18next.\
Some basics of i18next and some cool possibilities on how to optimize your localization workflow.[\ <img src="https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2Fgit-blob-f210314bc6f460e15c18cd3c5c132fff8c2ad2b8%2Ftitle%20width.jpg?alt=media" alt="" data-size="original">](https://locize.com/blog/react-i18next/)
{% endhint %}

{% hint style="info" %}
**Using Next.js?**\
[Here](https://locize.com/blog/next-i18next/) you'll find a blog post on how to best use [next-i18next](https://github.com/i18next/next-i18next) with [client side translation download](https://github.com/i18next/next-i18next#client-side-loading-of-translations-via-http) and SEO optimization.

[![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FoAxHedQ5XnB6rQXtv0hn%2Fnext-i18next.jpg?alt=media\&token=7a4b9ade-447c-40bf-9341-6148372b6158)](https://locize.com/blog/next-i18next/)\
\
**Using Next.js with the new App Router?**\
Then [this article](https://www.locize.com/blog/i18n-next-app-router) is what you are looking for!

[![](https://cdn.prod.website-files.com/67a323e323a50df7f24f0a94/67f268673fcfae53e5d4697c_i18n-next-app-router.jpg)](https://www.locize.com/blog/i18n-next-app-router)
{% endhint %}

{% hint style="info" %}
**Using Remix?**\
[Here](https://github.com/locize/locize-remix-i18next-example) you'll find a simple example and [here a step by step tutorial](https://locize.com/blog/remix-i18n/) on how to best use remix-i18next.

[![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FnMxpvTcUJTKOe0CoaBgO%2Fremix-localization.jpg?alt=media\&token=cacac368-f199-417b-8a36-3ccb90f26384)](https://locize.com/blog/remix-i18n/)
{% endhint %}

{% hint style="info" %}
**Using Gatsby?**\
[Here](https://github.com/locize/locize-gatsby-example) you can find an example and an appropriate [blog post](https://locize.com/blog/gatsby-i18n/).

[![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FoHXi7oJPwGpWEgt3Mbtv%2Fgatsby-i18next.jpg?alt=media\&token=c27b1939-46eb-4d97-9124-ba2c33fd3190)](https://locize.com/blog/gatsby-i18n/)
{% endhint %}

## What does my code look like

**Before:** Your React code would have looked something like:

```jsx
...
<div>Just simple content</div>
<div>
  Hello <strong title="this is your name">{name}</strong>, you have {count} unread message(s). <Link to="/msgs">Go to messages</Link>.
</div>
...
```

**After:** With the `Trans` component just change it to:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
...
<div>{t('simpleContent')}</div>
<Trans i18nKey="userMessagesUnread" count={count}>
  Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message(s). <Link to="/msgs">Go to messages</Link>.
</Trans>
...
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
...
<div>{t($ => $.simpleContent)}</div>
<Trans i18nKey="userMessagesUnread" count={count}>
  Hello <strong title={t($ => $.nameTitle)}>{{name}}</strong>, you have {{count}} unread message(s). <Link to="/msgs">Go to messages</Link>.
</Trans>
...
```

{% endtab %}
{% endtabs %}

If you prefer not using semantic keys but text - [that's also possible](https://www.i18next.com/principles/fallback.html#key-fallback).

## On top: [Localization as a service](https://locize.com)

i18next supports translation management tools such as [locize.com](http://locize.com/?utm_source=react_i18next_com\&utm_medium=gitbook).

{% hint style="success" %}
[Here](https://github.com/locize/react-tutorial) you can find a step by step guide, which will unleash the full power of i18next in combination with locize.\
See how your developer experience with this localization workflow [could look like](https://youtu.be/osScyaGMVqo).\
There's also the possibility to have an [even more focused developer experience](https://youtu.be/VfxBpSXarlU), with the help of the [auto-machinetranslation workflow](https://docs.locize.com/whats-inside/auto-machine-translation) and the use of the save missing keys functionality, new keys not only gets added to locize automatically, while developing the app, but are also [automatically translated](https://youtu.be/VfxBpSXarlU) into the target languages using machine translation (like [Google Translate](https://cloud.google.com/translate)).
{% endhint %}

{% embed url="<https://www.youtube.com/watch?v=TFV_vhJs5DY>" %}

[Learn more about the enterprise offering](https://www.i18next.com/overview/for-enterprises)


# Getting started

## Installation

### Install using npm

react-i18next can be added to your project using **npm**:

```bash
# npm
$ npm install react-i18next i18next --save
```

In the `/dist` folder you find specific builds for `commonjs`, `es6 modules`,...

{% hint style="info" %}
The module is optimized to load by webpack, rollup, ... The correct entry points are already configured in the package.json. There should be no extra setup needed to get the best build option.
{% endhint %}

### Load from CDN

You can also add a script tag to load react-i18next from one of the CDNs providing it, eg.:

**unpkg.com**

* <https://unpkg.com/react-i18next/react-i18next.js>
* <https://unpkg.com/react-i18next/react-i18next.min.js>

## Translation "how to"

{% hint style="info" %}
You should read the [i18next](https://www.i18next.com) documentation at some point as we do not repeat all the [configuration options](https://www.i18next.com/overview/configuration-options) and translation functionalities like [plurals](https://www.i18next.com/translation-function/plurals), [formatting](https://www.i18next.com/translation-function/formatting), [interpolation](https://www.i18next.com/translation-function/interpolation), ... here.
{% endhint %}

> **Official CLI**
>
> ⭐ [i18next-cli](https://github.com/i18next/i18next-cli)
>
> The official, high-performance, all-in-one command-line tool for i18next. It handles key extraction, code linting, locale syncing, and type generation. It's built with modern technologies for maximum speed and accuracy. This is the recommended tool for all i18next projects.

**You have two options to translate your content:**

### Simple content

Simple content can easily be translated using the provided `t` function.

**Before:**

```jsx
<div>Just simple content</div>
```

**After:**

{% tabs %}
{% tab title="JavaScript" %}

```jsx
<div>{t('simpleContent')}</div>
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
<div>{t($ => $.simpleContent)}</div>
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
You will get the t function by using the [useTranslation](https://react.i18next.com/latest/usetranslation-hook) hook or the [withTranslation](https://react.i18next.com/latest/withtranslation-hoc) hoc.
{% endhint %}

### JSX tree

Sometimes you might want to include html formatting or components like links into your translations. (Always try to get the best result for your translators - the final string to translate should be a complete sentence).

**Before:** Your react code would have looked something like:

```jsx
<div>
  Hello <strong title="this is your name">{name}</strong>, you have {count} unread message(s). <Link to="/msgs">Go to messages</Link>.
</div>
```

**After:** With the trans component just change it to:

```jsx
<Trans i18nKey="userMessagesUnread" count={count}>
  Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

{% tabs %}
{% tab title="JavaScript" %}

```
<Trans i18nKey="userMessagesUnread" count={count}>
  Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

{% endtab %}

{% tab title="TypeScript" %}

```
<Trans i18nKey="userMessagesUnread" count={count}>
  Hello <strong title={t($ => $.nameTitle)}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

{% endtab %}
{% endtabs %}

{% hint style="info" %}
Learn more about the Trans Component [here](https://react.i18next.com/latest/trans-component)
{% endhint %}

## Basic sample

This basic sample tries to add i18n in a one file sample.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from "react";
import { createRoot } from 'react-dom/client';
import i18n from "i18next";
import { useTranslation, initReactI18next } from "react-i18next";

i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    // the translations
    // (tip move them in a JSON file and import them,
    // or even better, manage them via a UI: https://react.i18next.com/guides/multiple-translation-files#manage-your-translations-with-a-management-gui)
    resources: {
      en: {
        translation: {
          "Welcome to React": "Welcome to React and react-i18next"
        }
      }
    },
    lng: "en", // if you're using a language detector, do not define the lng option
    fallbackLng: "en",

    interpolation: {
      escapeValue: false // react already safes from xss => https://www.i18next.com/translation-function/interpolation#unescape
    }
  });

function App() {
  const { t } = useTranslation();

  return <h2>{t('Welcome to React')}</h2>;
}

// append app to dom
const root = createRoot(document.getElementById('root'));
root.render(
  <App />
);
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from "react";
import { createRoot } from 'react-dom/client';
import i18n from "i18next";
import { useTranslation, initReactI18next } from "react-i18next";

i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    // the translations
    // (tip move them in a JSON file and import them,
    // or even better, manage them via a UI: https://react.i18next.com/guides/multiple-translation-files#manage-your-translations-with-a-management-gui)
    resources: {
      en: {
        translation: {
          "Welcome to React": "Welcome to React and react-i18next"
        }
      }
    },
    lng: "en", // if you're using a language detector, do not define the lng option
    fallbackLng: "en",

    interpolation: {
      escapeValue: false // react already safes from xss => https://www.i18next.com/translation-function/interpolation#unescape
    }
  });

function App() {
  const { t } = useTranslation();

  return <h2>{t($ => $['Welcome to React'])}</h2>;
}

// append app to dom
const root = createRoot(document.getElementById('root'));
root.render(
  <App />
);
```

{% endtab %}
{% endtabs %}

#### RESULT:

![Preview of content](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2Fgit-blob-2339aca23da3ae3e18d4a101235e3b6cce111ad3%2FScreen%20Shot%202018-09-30%20at%2016.58.18.png?alt=media)

{% hint style="info" %}
This sample while very simple does come with some [drawbacks](https://react.i18next.com/guides/the-drawbacks-of-other-i18n-solutions) to getting the full potential from using react-i18next you should read the extended [step by step guide](https://react.i18next.com/latest/using-with-hooks).
{% endhint %}

### Do you like to read a more complete step by step tutorial?

{% hint style="success" %}
[Here](https://locize.com/blog/react-i18next/) you'll find a simple tutorial on how to best use react-i18next.\
Some basics of i18next and some cool possibilities on how to optimize your localization workflow.[\ <img src="https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2Fgit-blob-f210314bc6f460e15c18cd3c5c132fff8c2ad2b8%2Ftitle%20width.jpg?alt=media" alt="" data-size="original">](https://locize.com/blog/react-i18next/)
{% endhint %}


# Drawbacks of other i18n solutions

Let's make the sample using our own base i18n framework [i18next](https://i18next.com). Like all other solutions, some come with [drawbacks](#the-drawbacks). These will be highlighted after samples.

## Using a pure javascript i18n framework

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import i18n from "i18next";

// translation catalog
const resources = {
  en: {
    translation: {
      "welcome": "Welcome to React and react-i18next"
    }
  }
};

// initialize i18next with catalog and language to use
i18n.init({
  resources,
  lng: "en"
});

class App extends Component {
  render() {
    return <h2>{i18n.t('welcome')}</h2>;
  }
}

// append app to dom
const root = createRoot(document.getElementById('root'));
root.render(
  <App />
);
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import i18n from "i18next";

// translation catalog
const resources = {
  en: {
    translation: {
      "welcome": "Welcome to React and react-i18next"
    }
  }
};

// initialize i18next with catalog and language to use
i18n.init({
  resources,
  lng: "en"
});

class App extends Component {
  render() {
    return <h2>{i18n.t($ => $.welcome)}</h2>;
  }
}

// append app to dom
const root = createRoot(document.getElementById('root'));
root.render(
  <App />
);
```

{% endtab %}
{% endtabs %}

## More react adapted "react-i18n"

The above is basically how every i18n framework for react works. The translations and language get set when initiated and a translation function is made available. You could easily extend this hiding the i18n.init inside a provider and pass down the function by context to another component to translate strings.

So let's make this more visible with some pseudo code:

```javascript
import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import { I18nProvider, FormattedString } from "i18nLib";

// import translation catalog
import resources from './catalog-en.json';

class App extends Component {
  render() {
    return <h2><FormattedString msg="welcome" /></h2>;
  }
}

// append app to dom
const root = createRoot(document.getElementById('root'));
root.render(
  <I18nProvider lng="en" resources={resources}>
    <App />,
  </I18nProvider>
);
```

## The drawbacks

Before we come to the drawbacks let's highlight some advantages of those solutions above - they are very simple to get started.

### Changing the language

Can you easily change the language? Get the translations in other language loaded? Does the language change trigger a rerender?

That's what the [withTranslation](https://react.i18next.com/latest/withtranslation-hoc) higher order component or [useTranslation](https://react.i18next.com/latest/usetranslation-hook) hook do!

### Scale and split your translations into multiple files

When your project gets bigger you do not only want code splitting but you also like to load translations on demand to avoid loading all translations upfront which would result in bad load times for your website.

With loading translations asynchronous there comes another problem - does your framework handle the pending state during loading translation?

That's what the [withTranslation](https://react.i18next.com/latest/withtranslation-hoc) higher order component or [useTranslation](https://react.i18next.com/latest/usetranslation-hook) hook do!

### Can you translate combined jsx nodes in one sentence

Let's take following content:

```javascript
<p>
  Hello <strong>{name}</strong>, you have 
  <Link to="/msgs">{count} unread message(s)</Link>.
</p>
```

In most frameworks you will end having to split this into multiple translation strings. But for your translators it would make sense to have this as one sentence to translate like eg.:

```
Hello <1>{name}</1>, you have <3>{count} unread message(s)</3>.
```

You can do this using the [Trans component](https://react.i18next.com/latest/trans-component).


# Quick start

## Install needed dependencies

We expect you having an existing react application - if not give [Vite](https://vite.dev/guide/#scaffolding-your-first-vite-project) (`npm create vite@latest`) or similar a try.

Install both react-i18next and i18next packages:

```bash
npm install react-i18next i18next --save
```

Why do you need i18next package? i18next is the core that provides all translation functionality while react-i18next gives some extra power for using with react.

#### Do you directly want to see an example?

Check out this basic [react example](https://github.com/i18next/react-i18next/tree/master/example/react) with a [browser language-detector](https://github.com/i18next/i18next-browser-languageDetector) and a [http backend](https://github.com/i18next/i18next-http-backend) to load translations from.

#### Do you like to read a more complete step by step tutorial?

{% hint style="success" %}
[Here](https://locize.com/blog/react-i18next/) you'll find a simple tutorial on how to best use react-i18next.\
Some basics of i18next and some cool possibilities on how to optimize your localization workflow.[\
![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2Fgit-blob-f210314bc6f460e15c18cd3c5c132fff8c2ad2b8%2Ftitle%20width.jpg?alt=media)](https://locize.com/blog/react-i18next/)
{% endhint %}

## Configure i18next

Create a new file `i18n.js` beside your `index.js` containing following content:

```javascript
import i18n from "i18next";
import { initReactI18next } from "react-i18next";

// the translations
// (tip move them in a JSON file and import them,
// or even better, manage them separated from your code: https://react.i18next.com/guides/multiple-translation-files)
const resources = {
  en: {
    translation: {
      "Welcome to React": "Welcome to React and react-i18next"
    }
  },
  fr: {
    translation: {
      "Welcome to React": "Bienvenue à React et react-i18next"
    }
  }
};

i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    resources,
    lng: "en", // language to use, more information here: https://www.i18next.com/overview/configuration-options#languages-namespaces-resources
    // you can use the i18n.changeLanguage function to change the language manually: https://www.i18next.com/overview/api#changelanguage
    // if you're using a language detector, do not define the lng option

    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

  export default i18n;
```

{% hint style="info" %}
The file does not need to be named `i18n.js`, it can be any other filename. Just make sure you import it accordingly.
{% endhint %}

The interesting part here is by `i18n.use(initReactI18next)` we pass the i18n instance to react-i18next which will make it available for all the components via the context api.

Then import that in `index.js`:

```javascript
import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import './i18n';
import App from './App';

// append app to dom
const root = createRoot(document.getElementById('root'));
root.render(
  <App />
);
```

{% tabs %}
{% tab title="JavaScript" %}
{% hint style="info" %}
If you need to access the `t` function or the `i18next` instance from outside of a React component you can simply import your `./i18n.js` and use the exported i18next instance:

<pre><code><strong>import i18next from './i18n'
</strong>
i18next.t('my.key')
</code></pre>

\
Also read about this [here](https://www.locize.com/blog/how-to-use-i18next-t-outside-react-components) and [here](https://github.com/i18next/react-i18next/issues/1236#issuecomment-762039023).
{% endhint %}
{% endtab %}

{% tab title="TypeScript" %}
{% hint style="info" %}
If you need to access the `t` function or the `i18next` instance from outside of a React component you can simply import your `./i18n.js` and use the exported i18next instance:

<pre><code><strong>import i18next from './i18n'
</strong>
i18next.t($ => $.my.key)
</code></pre>

\
Also read about this [here](https://www.locize.com/blog/how-to-use-i18next-t-outside-react-components) and [here](https://github.com/i18next/react-i18next/issues/1236#issuecomment-762039023).
{% endhint %}
{% endtab %}
{% endtabs %}

## Translate your content

### Using the hook

Using the hook in functional components is one of the options you have.

The `t` function is the main function in i18next to translate content. Read the [documentation](https://www.i18next.com/translation-function/essentials) for all the options.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from 'react';

// the hook
import { useTranslation } from 'react-i18next';

function MyComponent () {
  const { t, i18n } = useTranslation();
  return <h1>{t('Welcome to React')}</h1>
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from 'react';

// the hook
import { useTranslation } from 'react-i18next';

function MyComponent () {
  const { t, i18n } = useTranslation();
  return <h1>{t($ => $['Welcome to React'])}</h1>
}
```

{% endtab %}
{% endtabs %}

Learn more about the hook [useTranslation](https://react.i18next.com/latest/usetranslation-hook).

### Using the HOC

Using higher order components is one of the most used method to extend existing components by passing additional props to them.

The `t` function is the main function in i18next to translate content. Read the [documentation](https://www.i18next.com/translation-function/essentials) for all the options.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from 'react';

// the hoc
import { withTranslation } from 'react-i18next';

function MyComponent ({ t }) {
  return <h1>{t('Welcome to React')}</h1>
}

export default withTranslation()(MyComponent);
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from 'react';

// the hoc
import { withTranslation } from 'react-i18next';

function MyComponent ({ t }) {
  return <h1>{t($ => $['Welcome to React'])}</h1>
}

export default withTranslation()(MyComponent);
```

{% endtab %}
{% endtabs %}

Learn more about the higher order component [withTranslation](https://react.i18next.com/latest/withtranslation-hoc).

### Using the render prop

The render prop enables you to use the `t` function inside your component.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from 'react';

// the render prop
import { Translation } from 'react-i18next';

export default function MyComponent () {
  return (
    <Translation>
      {
        t => <h1>{t('Welcome to React')}</h1>
      }
    </Translation>
  )
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from 'react';

// the render prop
import { Translation } from 'react-i18next';

export default function MyComponent () {
  return (
    <Translation>
      {
        t => <h1>{t($ => $['Welcome to React'])}</h1>
      }
    </Translation>
  )
}
```

{% endtab %}
{% endtabs %}

Learn more about the render prop [Translation](https://react.i18next.com/latest/translation-render-prop).

### Using the Trans component

The Trans component is the best way to translate a JSX tree in one translation. This enables you to eg. easily translate text containing a link component or formatting like `<strong>`.

```jsx
import React from 'react';
import { Trans } from 'react-i18next';

export default function MyComponent () {
  return <Trans><H1>Welcome to React</H1></Trans>
}

// the translation in this case should be
"<0>Welcome to React</0>": "<0>Welcome to React and react-i18next</0>"
```

Don't worry if you do not yet understand how the Trans component works in detail. Learn more about it [here](https://react.i18next.com/latest/trans-component).

## Next steps

Depending on your learning style, you can now read the more in-depth [step by step](https://react.i18next.com/latest/using-with-hooks) guide and learn how to load translations using xhr or how to change the language.

Prefer having code to checkout? Directly dive into our examples:

* [Example react](https://github.com/i18next/react-i18next/tree/master/example/react)

> **Would you like to visually check the progress state of your translations?**
>
> *Try* [*translation-check*](https://github.com/locize/translation-check)*, it shows an overview of your translations in a nice UI. Check which keys are not yet translated.*\
> [![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-L9iS6WpW81N7RGRTQ-K%2F-McU0OVWmskDXbjzjn-O%2F-McU11WehFkeBR6Vvagy%2Fpreview.jpg?alt=media\&token=ee6dbf07-a733-4499-b562-36592c601d56)](https://github.com/locize/translation-check)


# Multiple Translation Files

One of the advantages of react-i18next is based on i18next it supports the separation of translations into multiple files - which are called namespaces in i18next context -> as you're accessing keys from a namespace defining that as a prefix:

So while this takes the translation from the defined default namespace:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
i18next.t('look.deep');
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
i18next.t($ => $.look.deep);
```

{% endtab %}
{% endtabs %}

This will lookup the key in a namespace (file) called common.json:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
i18next.t('common:look.deep'); // not recommended with ns prefix when used in combination with natural language keys
// better use the ns option:
i18next.t('look.deep', { ns: 'common' })
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
i18next.t($ => $.look.deep, { ns: 'common' })
```

{% endtab %}
{% endtabs %}

In order to use multiple namespaces/translation files, you need to specify it when calling [`useTranslation`](https://react.i18next.com/latest/usetranslation-hook) :

```javascript
const { t } = useTranslation(['translation', 'common']);
```

[`withTranslation`](https://react.i18next.com/latest/withtranslation-hoc):

```javascript
withTranslation(['translation', 'common'])(MyComponent);
```

or [`Translation`](https://react.i18next.com/latest/translation-render-prop):

{% tabs %}
{% tab title="JavaScript" %}

```jsx
<Translation ns={['translation', 'common']}>
{
  (t) => <p>{t('look.deep', { ns: 'common' })}</p>
}
</Translation>
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
<Translation ns={['translation', 'common']}>
{
  (t) => <p>{t($ => $.look.deep, { ns: 'common' })}</p>
}
</Translation>
```

{% endtab %}
{% endtabs %}

## Separating translation files

In i18next you have a lot of options to add translations on init, in your code calling API methods or using one of the backend implementation. For a detailed write up check out the ["Add or load translation guide on i18next.com"](https://www.i18next.com/how-to/add-or-load-translations).

With react-i18next you can use any of the components passing down the `t` function to your components to load namespaces:

* [useTranslation (hook)](https://react.i18next.com/latest/usetranslation-hook)
* [withTranslation (HOC)](https://react.i18next.com/latest/withtranslation-hoc)
* [Translation (render prop)](https://react.i18next.com/latest/translation-render-prop)

All take arguments to define which namespaces to load and will Suspense rendering until those got loaded.

So you do not need to load all translations upfront enabling you to create huge react based applications without slowing down loading of the first page cause all translations need to be loaded upfront (hello other i18n implementations).

## Manage your translations with a management GUI

### [**locize**](https://locize.com) is the perfect translation management tool for your [**i18next**](https://www.i18next.com) project

#### ➡️ [i18next](https://www.i18next.com/) + [locize](https://locize.com/) = [true continuous localization](https://locize.com/how-it-works.html#continouslocalization)

[Here](https://github.com/locize/react-tutorial) you can find a step by step guide, which will unleash the full power of i18next in combination with locize.\
See how your developer experience with this localization workflow [could look like](https://youtu.be/osScyaGMVqo).\
There's also the possibility to have an [even more focused developer experience](https://youtu.be/VfxBpSXarlU), with the help of the [auto-machinetranslation workflow](https://docs.locize.com/whats-inside/auto-machine-translation) and the use of the save missing keys functionality, new keys not only gets added to locize automatically, while developing the app, but are also [automatically translated](https://youtu.be/VfxBpSXarlU) into the target languages using machine translation (like [Google Translate](https://cloud.google.com/translate)).

{% embed url="<https://youtu.be/osScyaGMVqo>" %}

{% embed url="<https://youtu.be/VfxBpSXarlU>" %}


# Step by step guide

## Install needed dependencies

We expect you to have an existing react application supporting [hooks](https://reactjs.org/docs/hooks-intro.html) (at least v16.7.0-alpha of react and react-dom).

Install both react-i18next and i18next packages:

```bash
npm install react-i18next i18next --save

# if you'd like to detect user language and load translation
npm install i18next-http-backend i18next-browser-languagedetector --save
```

### Configure i18next

I18next is the core of the i18n functionality while react-i18next extends and glues it to react.

Create a new file `i18n.js` beside your `index.js` containing following content:

```javascript
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
// don't want to use this?
// have a look at the Quick start guide 
// for passing in lng and translations on init

i18n
  // load translation using http -> see /public/locales (i.e. https://github.com/i18next/react-i18next/tree/master/example/react/public/locales)
  // learn more: https://github.com/i18next/i18next-http-backend
  // want your translations to be loaded from a professional CDN? => https://github.com/locize/react-tutorial#step-2---use-the-locize-cdn
  .use(Backend)
  // detect user language
  // learn more: https://github.com/i18next/i18next-browser-languageDetector
  .use(LanguageDetector)
  // pass the i18n instance to react-i18next.
  .use(initReactI18next)
  // init i18next
  // for all options read: https://www.i18next.com/overview/configuration-options
  .init({
    fallbackLng: 'en',
    debug: true,

    interpolation: {
      escapeValue: false, // not needed for react as it escapes by default
    }
  });


export default i18n;
```

The interesting part here is by `i18n.use(initReactI18next)` we pass the i18n instance to react-i18next which will make it available for all the components.

Then import that in `index.js`:

```javascript
import React, { Component } from "react";
import { createRoot } from 'react-dom/client';
import App from './App';

// import i18n (needs to be bundled ;)) 
import './i18n';

const root = createRoot(document.getElementById('root'));
root.render(
  <App />
);
```

{% tabs %}
{% tab title="JavaScript" %}
{% hint style="info" %}
If you need to access the `t` function or the `i18next` instance from outside of a React component you can simply import your `./i18n.js` and use the exported i18next instance:

```
import i18next from './i18n'

i18next.t('my.key')
```

{% endhint %}
{% endtab %}

{% tab title="TypeScript" %}
{% hint style="info" %}
If you need to access the `t` function or the `i18next` instance from outside of a React component you can simply import your `./i18n.js` and use the exported i18next instance:

```
import i18next from './i18n'

i18next.t($ => $.my.key)
```

{% endhint %}
{% endtab %}
{% endtabs %}

### Translate your content

#### Using the useTranslation hook

You can use the hook inside your functional components like:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React, { Suspense } from 'react';
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t, i18n } = useTranslation();

  return <h1>{t('Welcome to React')}</h1>
}

// i18n translations might still be loaded by the http backend
// use react's Suspense
export default function App() {
  return (
    <Suspense fallback="loading">
      <MyComponent />
    </Suspense>
  );
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React, { Suspense } from 'react';
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t, i18n } = useTranslation();

  return <h1>{t($ => $['Welcome to React'])}</h1>
}

// i18n translations might still be loaded by the http backend
// use react's Suspense
export default function App() {
  return (
    <Suspense fallback="loading">
      <MyComponent />
    </Suspense>
  );
}
```

{% endtab %}
{% endtabs %}

The useTranslation hook function takes one options argument. You can either pass in a namespace or an array of namespaces to load.

```javascript
const { t, i18n } = useTranslation('common');

const { t, i18n } = useTranslation(['page1', 'common']);
```

#### Translation Files

Create a new file `public/locales/<language_code>/translation.json` with the following sample content.

```
{
  "title": "Welcome to react using react-i18next",
  "description": {
    "part1": "To get started, edit <1>src/App.js</1> and save to reload.",
    "part2": "Switch language between english and german using buttons above."
  }
}
```

Files are plain JSON you can checkout the full sample [here](https://github.com/i18next/react-i18next/tree/master/example/react/public/locales).

{% hint style="info" %}
Please note the t function will be either bound to the default namespace defined on i18next init or to the first one passed in arguments.
{% endhint %}

{% content-ref url="../guides/multiple-translation-files" %}
[multiple-translation-files](https://react.i18next.com/guides/multiple-translation-files)
{% endcontent-ref %}

#### Using the withTranslation HOC

There might be some legacy cases where you are still forced to use classes. Don't worry, we still provide a hoc to cover these cases:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React, { Component, Suspense } from 'react';
import { withTranslation } from 'react-i18next';

class LegacyComponentClass extends Component {
  render() {
    const { t } = this.props;

    return (
      <h1>{t('Welcome to React')}</h1>
    )
  }
}
const MyComponent = withTranslation()(LegacyComponentClass)

// i18n translations might still be loaded by the http backend
// use react's Suspense
export default function App() {
  return (
    <Suspense fallback="loading">
      <MyComponent />
    </Suspense>
  );
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React, { Component, Suspense } from 'react';
import { withTranslation } from 'react-i18next';

class LegacyComponentClass extends Component {
  render() {
    const { t } = this.props;

    return (
      <h1>{t($ => $['Welcome to React'])}</h1>
    )
  }
}
const MyComponent = withTranslation()(LegacyComponentClass)

// i18n translations might still be loaded by the http backend
// use react's Suspense
export default function App() {
  return (
    <Suspense fallback="loading">
      <MyComponent />
    </Suspense>
  );
}
```

{% endtab %}
{% endtabs %}

The withTranslation hook function takes one options argument. You can either pass in a namespace or a array of namespaces to load.

```javascript
withTranslation('common')(LegacyComponentClass);

withTranslation(['page1', 'common'])(LegacyComponentClass);
```

#### Using the Trans component

The Trans component is the best way to translate a JSX tree in one translation. This enables you to eg. easily translate text containing a link component or formatting like `<strong>`.

```jsx
import React from 'react';
import { Trans } from 'react-i18next';

export default function MyComponent () {
  return <Trans>Welcome to <strong>React</strong></Trans>
}

// the translation in this case should be
"Welcome to <1>React</1>": "Welcome to <1>React and react-i18next</1>"
```

Don't worry if you do not yet understand how the Trans component works in detail. Learn more about it [here](https://react.i18next.com/latest/trans-component).

## See the sample

Prefer having code to checkout? Directly dive into our example:

* [using hooks with react-i18next](https://github.com/i18next/react-i18next/tree/master/example/react)

### Do you like to read a more complete step by step tutorial?

{% hint style="success" %}
[Here](https://locize.com/blog/react-i18next/) you'll find a simple tutorial on how to best use react-i18next.\
Some basics of i18next and some cool possibilities on how to optimize your localization workflow.[\
![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2Fgit-blob-f210314bc6f460e15c18cd3c5c132fff8c2ad2b8%2Ftitle%20width.jpg?alt=media)](https://locize.com/blog/react-i18next/)
{% endhint %}


# i18next instance

The instance is an initialized i18next instance. In the following code snippet, we add a backend to load translations from server and a language detector for detecting user language.

> You can learn more about [i18next](http://i18next.com) and [plugins](https://www.i18next.com/plugins-and-utils.html#plugins) on the i18next website.

```javascript
import i18n from 'i18next';
import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
import { initReactI18next } from 'react-i18next';


i18n
  .use(Backend)
  .use(LanguageDetector)
  .use(initReactI18next) // bind react-i18next to the instance
  .init({
    fallbackLng: 'en',
    debug: true,

    interpolation: {
      escapeValue: false, // not needed for react!!
    },

    // react i18next special options (optional)
    // override if needed - omit if ok with defaults
    /*
    react: {
      bindI18n: 'languageChanged',
      bindI18nStore: '',
      transEmptyNodeValue: '',
      transSupportBasicHtmlNodes: true,
      transKeepBasicHtmlNodesFor: ['br', 'strong', 'i'],
      useSuspense: true,
    }
    */
  });


export default i18n;
```

All additional options for react in init options:

| options                    | default                     | description                                                                                                                                                                                                  |
| -------------------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| bindI18n                   | 'languageChanged'           | <p>which events trigger a rerender, can be set to false or string of events<br>separated by ""</p>                                                                                                           |
| bindI18nStore              | ''                          | define which events on [resourceStore](https://www.i18next.com/overview/api#store-events) should trigger a rerender                                                                                          |
| transEmptyNodeValue        | ''                          | how to treat failed lookups in Trans component                                                                                                                                                               |
| transSupportBasicHtmlNodes | true                        | <p>convert eg. <code>\<br/></code> found in translations to a react component of type br<br><a href="../trans-component#using-for-simple-html-elements-in-translations-v-10-4-0">See Trans component</a></p> |
| transKeepBasicHtmlNodesFor | \['br', 'strong', 'i', 'p'] | <p>Which nodes not to convert in defaultValue generation in the Trans component.<br><a href="../trans-component#using-for-simple-html-elements-in-translations-v-10-4-0">See Trans component</a></p>         |
| useSuspense                | true                        | If using Suspense or not                                                                                                                                                                                     |
| keyPrefix                  | undefined                   | the optional `keyPrefix` will be automatically applied to the returned `t` function in [useTranslation](https://react.i18next.com/usetranslation-hook#optional-keyprefix-option) for example.                |

For more initialization options have look at the [docs](https://www.i18next.com/overview/configuration-options).


# useTranslation (hook)

## What it does

It gets the `t` function and `i18n` instance inside your functional component.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from 'react';
import { useTranslation } from 'react-i18next';

export function MyComponent() {
  const { t, i18n } = useTranslation(); // not passing any namespace will use the defaultNS (by default set to 'translation')
  // or const [t, i18n] = useTranslation();

  return <p>{t('my translated text')}</p>
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from 'react';
import { useTranslation } from 'react-i18next';

export function MyComponent() {
  const { t, i18n } = useTranslation(); // not passing any namespace will use the defaultNS (by default set to 'translation')
  // or const [t, i18n] = useTranslation();

  return <p>{t($ => $['my translated text'])}</p>
}
```

{% endtab %}
{% endtabs %}

While most of the time you only need the `t` function to translate your content, you can also get the i18n instance (in order to change the language).

```javascript
i18n.changeLanguage('en-US');
```

{% hint style="info" %}
The `useTranslation` hook will trigger a [Suspense](https://reactjs.org/docs/concurrent-mode-suspense.html) if not ready (eg. pending load of translation files). You can set `useSuspense` to false if prefer not using Suspense.
{% endhint %}

## When to use?

Use the `useTranslation` hook inside your **functional components** to access the translation function or i18n instance.

{% hint style="success" %}
In [this tutorial](https://locize.com/blog/react-i18next/) you'll find some ways on how to use this useTranslation hook.

You'll also see how to use it when you need to work with [multiple namespaces](https://locize.com/blog/react-i18next/#multiple-namespaces).[\ <img src="https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2Fgit-blob-f210314bc6f460e15c18cd3c5c132fff8c2ad2b8%2Ftitle%20width.jpg?alt=media" alt="" data-size="original">](https://locize.com/blog/react-i18next/)
{% endhint %}

## useTranslation params

### Loading namespaces

{% tabs %}
{% tab title="JavaScript" %}

<pre class="language-jsx"><code class="lang-jsx"><strong>// load a specific namespace
</strong><strong>// the t function will be set to that namespace as default
</strong>const { t, i18n } = useTranslation('ns1');
t('key'); // will be looked up from namespace ns1

// load multiple namespaces
// the t function will be set to first namespace as default
const { t, i18n } = useTranslation(['ns1', 'ns2', 'ns3']);
t('key'); // will be looked up from namespace ns1
t('key', { ns: 'ns2' }); // will be looked up from namespace ns2
</code></pre>

{% endtab %}

{% tab title="TypeScript" %}

```tsx
// load a specific namespace
// the t function will be set to that namespace as default
const { t, i18n } = useTranslation('ns1');
t('key'); // will be looked up from namespace ns1

// load multiple namespaces
// the t function will be set to first namespace as default
const { t, i18n } = useTranslation(['ns1', 'ns2', 'ns3']);
t($ => $.key); // will be looked up from namespace ns1
t($ => $.key, { ns: 'ns2' }); // will be looked up from namespace ns2
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Only the `t` function is bound to the namespace, behind the scenes it uses the [getFixedT](https://www.i18next.com/overview/api#getfixedt) function of i18next.\
The `i18n` instance is the normal i18next instance. Not bound to anything special.
{% endhint %}

### Overriding the i18next instance

```javascript
// passing in an i18n instance
// use only if you do not like the default instance
// set by i18next.use(initReactI18next) or the I18nextProvider
import i18n from './i18n';
const { t, i18n } = useTranslation('ns1', { i18n });
```

### Optional keyPrefix option

> available in react-i18next version >= 11.12.0
>
> depends on i18next version >= 20.6.0

{% tabs %}
{% tab title="JavaScript" %}

```jsx
// having JSON in namespace "translation" like this:
/*{
    "very": {
      "deeply": {
        "nested": {
          "key": "here"
        }
      }
    }
}*/
// you can define a keyPrefix to be used for the resulting t function
const { t } = useTranslation('translation', { keyPrefix: 'very.deeply.nested' });
const text = t('key'); // "here"
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
// having JSON in namespace "translation" like this:
/*{
    "very": {
      "deeply": {
        "nested": {
          "key": "here"
        }
      }
    }
}*/
// you can define a keyPrefix to be used for the resulting t function
const { t } = useTranslation('translation', { keyPrefix: 'very.deeply.nested' });
const text = t($ => $.key); // "here"
```

{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="JavaScript" %}
{% hint style="warning" %}
Do **not** use the `keyPrefix` option if you want to use keys with prefixed namespace notation:

i.e.

```javascript
const { t } = useTranslation('translation', { keyPrefix: 'very.deeply.nested' });
const text = t('ns:key'); // this will not work
```

{% endhint %}
{% endtab %}

{% tab title="TypeScript" %}
{% hint style="warning" %}
Do **not** use the `keyPrefix` option if you want to use keys with prefixed namespace notation:

i.e.

```javascript
const { t } = useTranslation('translation', { keyPrefix: 'very.deeply.nested' });
const text = t($ => $.key, { ns: 'ns' }); // this will not work
```

{% endhint %}
{% endtab %}
{% endtabs %}

### Optional lng option

> available in react-i18next version >= 12.3.1

{% tabs %}
{% tab title="JavaScript" %}

```jsx
// you can pass a language to be used for the resulting t function
const { t } = useTranslation('translation', { lng: 'de' });
const text = t('key'); // "hier"
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
// you can pass a language to be used for the resulting t function
const { t } = useTranslation('translation', { lng: 'de' });
const text = t($ => $.key); // "hier"
```

{% endtab %}
{% endtabs %}

### Not using Suspense

```javascript
// additional ready will state if translations are loaded or not
const { t, i18n, ready } = useTranslation('ns1', { useSuspense: false });
```

{% hint style="info" %}
Not using Suspense you will need to handle the not ready state yourself by eg. render a loading component as long `!ready` . Not doing so will result in rendering your translations before they loaded which will cause save missing be called although translations exists (just yet not loaded).
{% endhint %}


# withTranslation (HOC)

## What it does

The `withTranslation` is a classic HOC (higher order component) and gets the `t` function and `i18n` instance inside your component via props.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from 'react';
import { withTranslation } from 'react-i18next';

function MyComponent({ t, i18n }) {
  return <p>{t('my translated text')}</p>
}

export default withTranslation()(MyComponent);
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from 'react';
import { withTranslation } from 'react-i18next';

function MyComponent({ t, i18n }) {
  return <p>{t($ => $['my translated text'])}</p>
}

export default withTranslation()(MyComponent);
```

{% endtab %}
{% endtabs %}

While you most time only need the t function to translate your content you also get the i18n instance to eg. change the language.

```javascript
i18n.changeLanguage('en-US');
```

{% hint style="info" %}
The `withTranslation` HOC will trigger a [Suspense](https://reactjs.org/docs/code-splitting.html#suspense) if not ready (eg. pending load of translation files). You can set `useSuspense` to false if prefer not using Suspense.
{% endhint %}

## When to use?

Use the `withTranslation` HOC to wrap **any component (class or function)** to access the translation function or i18n instance.

## withTranslation params

### Loading namespaces

{% tabs %}
{% tab title="JavaScript" %}

```jsx
// load a specific namespace
// the t function will be set to that namespace as default
withTranslation('ns1')(MyComponent);

// inside your component MyComponent
this.props.t('key'); // will be looked up from namespace ns1

// load multiple namespaces
// the t function will be set to first namespace as default
withTranslation(['ns1', 'ns2', 'ns3'])(MyComponent);

// inside your component MyComponent
this.props.t('key'); // will be looked up from namespace ns1
this.props.t('key', { ns: 'ns2' }); // will be looked up from namespace ns2
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
// load a specific namespace
// the t function will be set to that namespace as default
withTranslation('ns1')(MyComponent);

// inside your component MyComponent
this.props.t($ => $.key); // will be looked up from namespace ns1

// load multiple namespaces
// the t function will be set to first namespace as default
withTranslation(['ns1', 'ns2', 'ns3'])(MyComponent);

// inside your component MyComponent
this.props.t($ => $.key); // will be looked up from namespace ns1
this.props.t($ => $.key, { ns: 'ns2' }); // will be looked up from namespace ns2
```

{% endtab %}
{% endtabs %}

### Overriding the i18next instance

```javascript
// passing in an i18n instance
// use only if you do not like the default instance
// set by i18next.use(initReactI18next) or the I18nextProvider
import i18n from './i18n';

const ExtendedComponent = withTranslation('ns1')(MyComponent);

<ExtendedComponent i18n={i18n} />
```

### Not using Suspense

```javascript
// use tReady prop in MyComponent to check if translations
// are already loaded or not
const ExtendedComponent = withTranslation()(MyComponent);

<ExtendedComponent useSuspense={false} />
```

{% hint style="info" %}
Not using Suspense you will need to handle the not ready state yourself by eg. render a loading component as long `!props.tReady` . Not doing so will result in rendering your translations before they loaded which will cause save missing be called although translations exist (just yet not loaded).
{% endhint %}

## How to

### use ref (>= v10.6.0)

You can use forwardRefs like:

```jsx
const Wrapped = withTranslation('translation', { withRef: true })(MyComponent);

// then pass a ref in your render method like
const myRef = React.createRef();
<Wrapped ref={myRef} />;

// use myRef.current to access it
```

### hoist non-react statics

The HOC does not hoist statics itself so you might append those statics manually or by using a module.

Use [hoist-non-react-statics](https://github.com/mridgway/hoist-non-react-statics) yourself:

```jsx
import React, { Component } from 'react';
import { withTranslation } from 'react-i18next';
import hoistStatics from 'hoist-non-react-statics';

class MyComponent extends Component {
  static ...
}

export default hoistStatics(withTranslation()(MyComponent), MyComponent);
```

Or simply hoist the one/two statics yourself:

```jsx
import React, { Component } from 'react';
import { withTranslation } from 'react-i18next';
import hoistStatics from 'hoist-non-react-statics';

class MyComponent extends Component {
  static ...
}

const Extended = withTranslation()(MyComponent);
Extended.static = MyComponent.static;

export default Extended;
```

### use TypeScript with class components

To get proper type annotations while using TypeScript, import the interface `WithTranslation` and extend it with your own props interface.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React, { Component } from 'react';
import { withTranslation, WithTranslation } from 'react-i18next';

class MyComponent extends Component {
  render() {
    return <div>{this.props.t('My translated text')}</div>
  }
}

export default withTranslation()(MyComponent);
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React, { Component } from 'react';
import { withTranslation, WithTranslation } from 'react-i18next';

class MyComponent extends Component<IProps, IState> {
  render() {
    return <div>{this.props.t($ => $['My translated text'])}</div>
  }
}

interface IProps extends WithTranslation {
  prop: any;
}

interface IState {
  state: any;
}

export default withTranslation()(MyComponent);
```

{% endtab %}
{% endtabs %}


# Translation (render prop)

## What it does <a href="#what-it-does" id="what-it-does"></a>

The `Translation` is a render prop and gets the `t` function and `i18n` instance to your component.

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React from 'react';
import { Translation } from 'react-i18next';

export function MyComponent() {
  return (
    <Translation>
      {
        (t, { i18n }) => <p>{t('my translated text')}</p>
      }
    </Translation>
  )
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React from 'react';
import { Translation } from 'react-i18next';

export function MyComponent() {
  return (
    <Translation>
      {
        (t, { i18n }) => <p>{t($ => $['my translated text'])}</p>
      }
    </Translation>
  )
}
```

{% endtab %}
{% endtabs %}

While you most time only need the t function to translate your content you also get the i18n instance to eg. change the language.

```javascript
i18n.changeLanguage('en-US');
```

{% hint style="info" %}
The `Translation` render prop will trigger a [Suspense](https://reactjs.org/docs/code-splitting.html#suspense) if not ready (eg. pending load of translation files). You can set `useSuspense` to false if prefer not using Suspense.
{% endhint %}

## When to use?

Use the `Translation` render prop inside **any component (class or function)** to access the translation function or i18n instance.

## Translation params

### Loading namespaces

{% tabs %}
{% tab title="JavaScript" %}

```jsx
// load a specific namespace
// the t function will be set to that namespace as default
<Translation ns="ns1">
{
  (t) => <p>{t('my translated text')}</p> // will be looked up from namespace ns1
}
</Translation>

// load multiple namespaces
// the t function will be set to first namespace as default
<Translation ns={['ns1', 'ns2', 'ns3']}>
{
  (t) => <p>{t('my translated text')}</p> // will be looked up from namespace ns1
}
</Translation>
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
// load a specific namespace
// the t function will be set to that namespace as default
<Translation ns="ns1">
{
  (t) => <p>{t($ => $['my translated text'])}</p> // will be looked up from namespace ns1
}
</Translation>

// load multiple namespaces
// the t function will be set to first namespace as default
<Translation ns={['ns1', 'ns2', 'ns3']}>
{
  (t) => <p>{t($ => $['my translated text'])}</p> // will be looked up from namespace ns1
}
</Translation>
```

{% endtab %}
{% endtabs %}

### Overriding the i18next instance

{% tabs %}
{% tab title="JavaScript" %}

```jsx
// passing in an i18n instance
// use only if you do not like the default instance
// set by i18next.use(initReactI18next) or the I18nextProvider
import i18n from './i18n';

<Translation i18n={i18n}>
{
  (t, { i18n }) => <p>{t('my translated text')}</p> // will be looked up from namespace ns1
}
</Translation>
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
// passing in an i18n instance
// use only if you do not like the default instance
// set by i18next.use(initReactI18next) or the I18nextProvider
import i18n from './i18n';

<Translation i18n={i18n}>
{
  (t, { i18n }) => <p>{t($ => $['my translated text'])}</p> // will be looked up from namespace ns1
}
</Translation>
```

{% endtab %}
{% endtabs %}


# Trans Component

{% hint style="success" %}
🎉 Announcing [`i18next-cli`](https://github.com/i18next/i18next-cli):\
&#x20;       The New Official Toolkit for i18next.\
⇒ [Learn More](https://www.locize.com/blog/i18next-cli)
{% endhint %}

## Important note

While `<Trans>` gives you a lot of power by letting you interpolate or translate complex React elements, the truth is: in most cases you don't even need it.

**As long you have no React/HTML nodes integrated into a cohesive sentence** (text formatting like `strong`, `em`, link components, maybe others), **you won't need it** - most of the times you will be using the good old `t` function.

You may be looking directly for the [Trans props](https://react.i18next.com/latest/trans-component#trans-props).

{% hint style="warning" %}
It does ONLY interpolation. It does not rerender on language change or load any translations needed. Check [`useTranslation` hook](https://react.i18next.com/latest/usetranslation-hook) or [`withTranslation` HOC](https://react.i18next.com/latest/withtranslation-hoc) for those cases.
{% endhint %}

```javascript
import React from 'react';
import { Trans, useTranslation } from 'react-i18next'

function MyComponent() {
  const { t } = useTranslation('myNamespace');

  return <Trans t={t}>Hello World</Trans>;
}
```

{% hint style="info" %}
Have a look at the [i18next documentation](https://www.i18next.com) for details on the the `t` function:

* [essentials](https://www.i18next.com/translation-function/essentials.html)
* [interpolation](https://www.i18next.com/translation-function/interpolation.html)
* [formatting](https://www.i18next.com/translation-function/formatting.html)
* [plurals](https://www.i18next.com/translation-function/plurals.html)
  {% endhint %}

## Samples

### Using with React components

So you learned there is no need to use the Trans component everywhere (the plain `t` function will just do fine in most cases).

This component enables you to nest any React content to be translated as one cohesive string. It supports both plural and interpolation. The `<Trans>` component will automatically use the most relevant `t()` function (from the [context instance](https://react.i18next.com/latest/i18nextprovider) or the global instance), unless overridden via the `i18n` or `t` props.

*Let's say you want to create following HTML output:*

> Hello **Arthur**, you have 42 unread messages. [Go to messages](https://react.i18next.com/legacy-v9/trans-component).

**Before:** Your untranslated React code would have looked something like:

```javascript
function MyComponent({ person, messages }) {
  const { name } = person;
  const count = messages.length;

  return (
    <>
      Hello <strong title="This is your name">{name}</strong>, you have {count} unread message(s). <Link to="/msgs">Go to messages</Link>.
    </>
  );
}
```

**After:** With the Trans component just change it to:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import { Trans } from 'react-i18next';

function MyComponent({ person, messages }) {
  const { name } = person;
  const count = messages.length;

  return (
    <Trans i18nKey="userMessagesUnread" count={count}>
      Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
    </Trans>
  );
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import { Trans } from 'react-i18next';

function MyComponent({ person, messages }) {
  const { name } = person;
  const count = messages.length;

  return (
    <Trans i18nKey="userMessagesUnread" count={count}>
      Hello <strong title={t($ => $.nameTitle)}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
    </Trans>
  );
}
```

{% endtab %}
{% endtabs %}

*Your en.json (translation strings) will look like:*

```javascript
"nameTitle": "This is your name",
"userMessagesUnread_one": "Hello <1>{{name}}</1>, you have {{count}} unread message. <5>Go to message</5>.",
"userMessagesUnread_other": "Hello <1>{{name}}</1>, you have {{count}} unread messages.  <5>Go to messages</5>.",
```

{% hint style="info" %}
[**saveMissing**](https://www.i18next.com/overview/configuration-options#missing-keys) will send a valid `defaultValue` based on the component children.\
Also, The `i18nKey` is optional, in case you already use text as translation keys.
{% endhint %}

### Alternative usage which lists the components (v11.6.0)

```javascript
<Trans
  i18nKey="myKey" // optional -> fallbacks to defaults if not provided
  defaults="hello <italic>beautiful</italic> <bold>{{what}}</bold>" // optional defaultValue
  values={{ what: 'world'}}
  components={{ italic: <i />, bold: <strong /> }}
/>
```

This format is useful if you want to interpolate the same node multiple times. Another advantage is the simpler named tags, which avoids the trouble with index guessing - however, this can also be achieved with `transSupportBasicHtmlNodes`, see the next section.

{% hint style="warning" %}
Existing self-closing HTML tag names are reserved keys and won't work. Examples: `link: <Link />`, `img: <img src="" />`, `media: <img src="" />`
{% endhint %}

{% hint style="info" %}
Make sure you also adapt your translation resources to include the *named tags* (`<italic>`) instead of the *indexed tags* (`<0>`)!
{% endhint %}

### Overriding React component props (v11.5.0)

In some cases you may want to override the props of a given component based on the active language.

This can be achieved by providing prop values inside of your translations. Such values will override whatever has been passed to the component present in the `components` prop of the `Trans` component.

In the example below we want our custom link component to have a different `href` value based on the active language. This is how our custom link component is being used:

```javascript
<Trans
  i18nKey="myKey"
  components={{ 
    CustomLink: <MyCustomLinkComponent href="value-to-be-overridden"/> 
    }}
/>
```

with the following being our translation message:

```json
  "myKey": "This is a <CustomLink href=\"https://example.com/\">link to example.com</CustomLink>."
```

This setup will render the following JSX:

```html
This is a <MyCustomLinkComponent href="https://example.com/">link to example.com</MyCustomLinkComponent>.
```

This approach also works with listed components:

```javascript
<Trans
  i18nKey="myKey"
  components={[ <MyCustomLinkComponent href="value-to-be-overridden"/> ]}
/>
```

With this then making up our translation message:

```json
  "myKey": "This is a <0 href=\"https://example.com/\">link to example.com</0>."
```

### Usage with simple HTML elements like \<br /> and others (v10.4.0)

There are two options that allow you to have basic HTML tags inside your translations, instead of numeric indexes. However, this only works for elements without additional attributes (like `className`), having none or a single text children.

Examples of elements that will be readable in translation strings:

* `<br/>`
* `<strong>bold</strong>`
* `<p>some paragraph</p>`

Examples that will be converted to indexed nodes:

* `<i className="icon-gear" />`: no attributes allowed
* `<strong title="something">{{name}}</strong>`: only text nodes allowed
* `<b>bold <i>italic</i></b>`: no nested elements, even simple ones

```jsx
<Trans i18nKey="welcomeUser">
  Hello <strong>{{name}}</strong>. <Link to="/inbox">See my profile</Link>
</Trans>
// JSON -> "welcomeUser": "Hello <strong>{{name}}</strong>. <1>See my profile</1>"

<Trans i18nKey="multiline">
  Some newlines <br/> would be <br/> fine
</Trans>
// JSON -> "multiline": "Some newlines <br/> would be <br/> fine"
```

Here is what can be configured in `i18next.options.react` that affect this behaviour:

| Option                          | Default                      | Description                                                                                                                                                                                                                                                             |
| ------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `transSupportBasicHtmlNodes`    | `true`                       | Enables keeping the name of simple nodes (e.g. `<br/>`) in translations instead of indexed keys                                                                                                                                                                         |
| `transKeepBasicHtmlNodesFor`    | `['br', 'strong', 'i', 'p']` | Which nodes are allowed to be kept in translations during `defaultValue` generation of `<Trans>`.                                                                                                                                                                       |
| `transWrapTextNodes` (v11.10.0) | `''`                         | Wrap text nodes in a user-specified element. e.g. set it to `span`. By default, text nodes are not wrapped. Can be used to work around a well-known Google Translate issue with React apps. See [facebook/react#11538](https://github.com/facebook/react/issues/11538). |

### Interpolation

You can pass in variables to get interpolated into the translation string by using objects containing those key:values.

```jsx
const person = { name: 'Henry', age: 21 };
const { name, age } = person;

<Trans>
  Hello {{ name }}. // <- = {{ "name": name }}
</Trans>
// Translation string: "Hello {{name}}"


<Trans>
  Hello {{ firstname: person.name }}.
</Trans>
// Translation string: "Hello {{firstname}}"
```

### Plural

You will need to pass the `count` prop:

```jsx
const messages = ['message one', 'message two'];

<Trans i18nKey="newMessages" count={messages.length}>
  You have {{ count: messages.length }} messages.
</Trans>

// Translation strings:
// "newMessages": "You have one message."
// "newMessages_plural": "You have {{count}} messages."
```

### Using with lists (v10.5.0)

You can still use `Array.map()` to turn dynamic content into nodes, using an extra option on a wrapping element:

```jsx
<Trans i18nKey="list_map">
  My dogs are named:
  <ul i18nIsDynamicList>
     {['rupert', 'max'].map(dog => (<li>{dog}</li>))}
  </ul>
</Trans>
// JSON -> "list_map": "My dogs are named: <1></1>"
```

Setting `i18nIsDynamicList` on the parent element will assert the `nodeToString` function creating the string for `saveMissing` will not contain children.

### Alternative usage (components array)

Some use cases, such as the ICU format, might be simpler by just passing content as props:

```javascript
<Trans
  i18nKey="myKey" // optional -> fallbacks to defaults if not provided
  defaults="hello <0>{{what}}</0>" // optional defaultValue
  values={{ what: 'world'}}
  components={[<strong>univers</strong>]}
/>
```

{% hint style="info" %}
`<0>` -> 0 is the index of the component in the components array
{% endhint %}

E.g. this format is needed when using [ICU as translation format](https://github.com/i18next/i18next-icu) as it is not possible to have the needed syntax as children (invalid jsx).

## How to get the correct translation string?

Guessing replacement tags *(<0>\</0>)* of your component is rather difficult. There are four options to get those translations directly generated by i18next:

1. use React Developer Tools to inspect the `<Trans>` component instance and look at the `props.children` array for array index of the tag in question.
2. use `debug = true` in `i18next.init()` options and watch your console for the missing key output
3. use the [saveMissing feature](https://www.i18next.com/configuration-options#missing-keys) of i18next to get those translations pushed to your backend or handled by a custom function.
4. understand how those numbers get generated from child index:

**Sample JSX:**

{% tabs %}
{% tab title="JavaScript" %}

```jsx
<Trans i18nKey="userMessagesUnread" count={count}>
    Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
<Trans i18nKey="userMessagesUnread" count={count}>
    Hello <strong title={t($ => $.nameTitle)}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

{% endtab %}
{% endtabs %}

**Resulting translation string:**

```
"Hello <1>{{name}}</1>, you have {{count}} unread message. <5>Go to message</5>."
```

**The complete the node tree**:

```javascript
Trans.children = [
  'Hello ',                         // 0: only a string
  { children: [{ name: 'Jan' }] },  // 1: <strong> with child object for interpolation
  ', you have ',                    // 2: only a string
  { count: 10 },                    // 3: plain object for interpolation
  ' unread messages. ',             // 4: only a string
  { children: ['Go to messages'] }, // 5: <Link> with a string child
  '.'                               // 6: yep, you guessed: another string
]
```

**Rules:**

* child is a string: nothing to wrap; just take the string
* child is an object: nothing to do; it's used for interpolation
* child is an element: wrap it's children in `<x></x>` where `x` is the index of that element's position in the `children` list; handle its children with the same rules (starting `element.children` index at 0 again)

## Trans props

All properties are optional, although you'll need to use `i18nKey` if you're not using natural language keys (text-based).

| ***name***          | ***type (default)***       | ***description***                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `i18nKey`           | `string (undefined)`       | <p>If you prefer to use text as keys you can omit this, and the translation will be used as key. Can contain the namespace by prepending it in the form <code>'ns:key'</code> (depending on <code>i18next.options.nsSeparator</code>)</p><p>But this is not recommended when used in combination with natural language keys, better use the dedicated ns parameter: <code>\<Trans i18nKey="myKey" ns="myNS">\</Trans></code></p> |
| `ns`                | `string (undefined)`       | Namespace to use. May also be embedded in `i18nKey` but not recommended when used in combination with natural language keys, see above.                                                                                                                                                                                                                                                                                          |
| `t`                 | `function (undefined)`     | `t` function to use instead of the global `i18next.t()` or the `t()` function provided by the nearest [provider](https://react.i18next.com/latest/i18nextprovider).                                                                                                                                                                                                                                                              |
| `count`             | `integer (undefined)`      | Numeric value for pluralizable strings                                                                                                                                                                                                                                                                                                                                                                                           |
| `context`           | `string (undefined)`       | Value used for the [context feature](https://www.i18next.com/translation-function/context).                                                                                                                                                                                                                                                                                                                                      |
| `tOptions`          | `object (undefined)`       | Extra options to pass to `t()` (e.g. `context`, `postProcessor`, ...)                                                                                                                                                                                                                                                                                                                                                            |
| `parent`            | `node (undefined)`         | A component to wrap the content into (can be globally set on `i18next.init`). **Required for React < v16**                                                                                                                                                                                                                                                                                                                       |
| `i18n`              | `object (undefined)`       | i18next instance to use if not provided by context                                                                                                                                                                                                                                                                                                                                                                               |
| `defaults`          | `string (undefined)`       | Use this instead of using the children as default translation value (useful for ICU)                                                                                                                                                                                                                                                                                                                                             |
| `values`            | `object (undefined)`       | Interpolation values if not provided in children                                                                                                                                                                                                                                                                                                                                                                                 |
| `components`        | `array[nodes] (undefined)` | Components to interpolate based on index of tag                                                                                                                                                                                                                                                                                                                                                                                  |
| `shouldUnescape`    | `boolean (false)`          | HTML encoded tags like: `&lt; &amp; &gt;` should be unescaped, to become: `< & >`                                                                                                                                                                                                                                                                                                                                                |
| `transDefaultProps` | `object (undefined)`       | Default props for the `Trans` component. Can be used to set default values for `tOptions`, `shouldUnescape`, `values`, and `components`.                                                                                                                                                                                                                                                                                         |

### i18next options

```javascript
i18next.init({
  // ...
  react: {
    // ...
    hashTransKey: function(defaultValue) {
      // return a key based on defaultValue or if you prefer to just remind you should set a key return false and throw an error
    },
    defaultTransParent: 'div', // a valid react element - required before react 16
    transEmptyNodeValue: '', // what to return for empty Trans
    transSupportBasicHtmlNodes: true, // allow <br/> and simple html elements in translations
    transKeepBasicHtmlNodesFor: ['br', 'strong', 'i'], // don't convert to <1></1> if simple react elements
    transWrapTextNodes: '', // Wrap text nodes in a user-specified element.
                            // i.e. set it to 'span'. By default, text nodes are not wrapped.
                            // Can be used to work around a well-known Google Translate issue with React apps. See: https://github.com/facebook/react/issues/11538
                            // (v11.10.0)
    transDefaultProps: undefined, // default props for Trans component
    // {
    //   tOptions: { interpolation: { escapeValue: true } },
    //   shouldUnescape: true,
    //   values: {},
  }
});
```

{% hint style="warning" %}
Please be aware if you are using **React 15 or below**, you are required to set the `defaultTransParent` option, or pass a `parent` via props.
{% endhint %}

{% hint style="danger" %}
**Are you having trouble when your website is ran through Google Translate?**\
Google Translate seems to manipulate the DOM and makes React quite unhappy!\
**There's a work around:** you can wrap text nodes with`<span>` using `transWrapTextNodes: 'span'`.

*If you want to know more about the Google Translate issue with React, have a look at* [*this*](https://github.com/facebook/react/issues/11538#issuecomment-390386520)*.*
{% endhint %}


# IcuTrans Component

## Important note

This component is an alternative component to [`Trans`](https://react.i18next.com/latest/trans-component) which is designed for use as the internal implementation of [The `icu.macro` Babel macro](https://react.i18next.com/misc/using-with-icu-format). Using it directly is possible, but not recommended.

While `<IcuTrans>` gives you a lot of power by letting you interpolate or translate complex React elements, the truth is: in most cases don't need this power.

**As long you have no React/HTML nodes integrated into a cohesive sentence** (text formatting like `strong`, `em`, link components, maybe others), **you won't need it** - most of the times you will be using the good old `t` function.

[IcuTrans props reference](https://react.i18next.com/latest/icu-trans-component#icutrans-props).

{% hint style="warning" %}
IcuTrans does ONLY interpolation. It does not rerender on language change or load any translations needed. Use [`useTranslation` hook](https://react.i18next.com/latest/usetranslation-hook) or [`withTranslation` HOC](https://react.i18next.com/latest/withtranslation-hoc) with `IcuTrans` to force a re-render on language changes.
{% endhint %}

```javascript
import React from 'react';
import { IcuTrans, useTranslation } from 'react-i18next'

function MyComponent() {
  // this will force a re-render when language changes or translation files are loaded
  const { t } = useTranslation('myNamespace');

  return <IcuTrans defaultTranslation="Hello World" content={[]} t={t}>Hello World</IcuTrans>;
}
```

{% hint style="info" %}
Have a look at the [i18next documentation](https://www.i18next.com) for details on the the `t` function:

* [essentials](https://www.i18next.com/translation-function/essentials.html)
* [interpolation](https://www.i18next.com/translation-function/interpolation.html)
* [formatting](https://www.i18next.com/translation-function/formatting.html)
* [plurals](https://www.i18next.com/translation-function/plurals.html)
  {% endhint %}

## Samples

### Using with React components

For use cases where you need to embed React components into your translations, `IcuTrans` can be used.

This component enables you to nest any React content to be translated as one cohesive string. It supports both plural and interpolation. The `<Trans>` component will automatically use the most relevant `t()` function (from the [context instance](https://react.i18next.com/latest/i18nextprovider) or the global instance), unless overridden via the `i18n` or `t` props.

*Let's say you want to create following HTML output:*

> Hello **Arthur**, you have 42 unread messages. [Go to messages](https://react.i18next.com/legacy-v9/trans-component).

**Before:** Your untranslated React code would have looked something like:

```javascript
function MyComponent({ person, messages }) {
  const { name } = person;
  const count = messages.length;

  return (
    <>
      Hello <strong title="This is your name">{name}</strong>, you have {count} unread message(s). <Link to="/msgs">Go to messages</Link>.
    </>
  );
}
```

**After:** With the IcuTrans component change it to:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import { IcuTrans } from 'react-i18next';

function MyComponent({ person, messages }) {
  const { name } = person;
  const count = messages.length;

  return (
    <IcuTrans
      i18nKey="userMessagesUnread" // optional -> fallbacks to defaults if not provided
      defaultTranslation="hello <0>{{name}}</0>, you have {{count}} unread message. <1>Go to messages</1>."
      values={{ name, count }}
      content={[
        {
          type: "strong",
          props: {
            title: t('nameTitle'),
          },
        },
        {
          type: Link,
          props: {
            to: "/msgs",
          },
        },
      ]}
    />
  );
}
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import { IcuTrans } from 'react-i18next';

function MyComponent({ person, messages }) {
  const { name } = person;
  const count = messages.length;

  return (
    <IcuTrans
      i18nKey="userMessagesUnread" // optional -> fallbacks to defaults if not provided
      defaultTranslation="hello <0>{{name}}</0>, you have {{count}} unread message. <1>Go to messages</1>."
      values={{ name, count }}
      content={[
        {
          type: "strong",
          props: {
            title: t(($) => $.nameTitle),
          },
        },
        {
          type: Link,
          props: {
            to: "/msgs",
          },
        },
      ]}
    />
  );
}
```

{% endtab %}
{% endtabs %}

*Your en.json (translation strings) will look like:*

```javascript
"nameTitle": "This is your name",
"userMessagesUnread_one": "Hello <1>{{name}}</1>, you have {{count}} unread message. <5>Go to message</5>.",
"userMessagesUnread_other": "Hello <1>{{name}}</1>, you have {{count}} unread messages.  <5>Go to messages</5>.",
```

## IcuTrans props

`defaultTranslation` and `contents` are required properties, all others are optional. You'll need to use `i18nKey` if you're not using natural language keys (text-based).

| ***name***           | ***type (default)***   | ***description***                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `i18nKey`            | `string (undefined)`   | <p>If you prefer to use text as keys you can omit this, and the translation will be used as key. Can contain the namespace by prepending it in the form <code>'ns:key'</code> (depending on <code>i18next.options.nsSeparator</code>)</p><p>But this is not recommended when used in combination with natural language keys, better use the dedicated ns parameter: <code>\<Trans i18nKey="myKey" ns="myNS">\</Trans></code></p> |
| `ns`                 | `string (undefined)`   | Namespace to use. May also be embedded in `i18nKey` but not recommended when used in combination with natural language keys, see above.                                                                                                                                                                                                                                                                                          |
| `t`                  | `function (undefined)` | `t` function to use instead of the global `i18next.t()` or the `t()` function provided by the nearest [provider](https://react.i18next.com/latest/i18nextprovider).                                                                                                                                                                                                                                                              |
| `count`              | `integer (undefined)`  | Numeric value for pluralizable strings                                                                                                                                                                                                                                                                                                                                                                                           |
| `context`            | `string (undefined)`   | Value used for the [context feature](https://www.i18next.com/translation-function/context).                                                                                                                                                                                                                                                                                                                                      |
| `tOptions`           | `object (undefined)`   | Extra options to pass to `t()` (e.g. `context`, `postProcessor`, ...)                                                                                                                                                                                                                                                                                                                                                            |
| `parent`             | `node (undefined)`     | A component to wrap the content into (can be globally set on `i18next.init`). **Required for React < v16**                                                                                                                                                                                                                                                                                                                       |
| `i18n`               | `object (undefined)`   | i18next instance to use if not provided by context                                                                                                                                                                                                                                                                                                                                                                               |
| `defaultTranslation` | `string`               | Use this instead of using the children as default translation value (useful for ICU)                                                                                                                                                                                                                                                                                                                                             |
| `values`             | `object (undefined)`   | Interpolation values                                                                                                                                                                                                                                                                                                                                                                                                             |
| `contents`           | `array[TypeDef]`       | Components to interpolate based on index of tag. This should be either `{ type: ComponentFunction }` or for built-in DOM elements `{ type: "a" }`, for example. `props` can be used to pass props to the component `{ type: "a", props: { href="/somewhere" } }`                                                                                                                                                                 |
| `shouldUnescape`     | `boolean (false)`      | HTML encoded tags like: `&lt; &amp; &gt;` should be unescaped, to become: `< & >`                                                                                                                                                                                                                                                                                                                                                |

### i18next options

```javascript
i18next.init({
  // ...
  react: {
    // ...
    hashTransKey: function(defaultValue) {
      // return a key based on defaultValue or if you prefer to just remind you should set a key return false and throw an error
    },
    defaultTransParent: 'div', // a valid react element - required before react 16
    transEmptyNodeValue: '', // what to return for empty Trans
    transSupportBasicHtmlNodes: true, // allow <br/> and simple html elements in translations
    transKeepBasicHtmlNodesFor: ['br', 'strong', 'i'], // don't convert to <1></1> if simple react elements
    transWrapTextNodes: '', // Wrap text nodes in a user-specified element.
                            // i.e. set it to 'span'. By default, text nodes are not wrapped.
                            // Can be used to work around a well-known Google Translate issue with React apps. See: https://github.com/facebook/react/issues/11538
                            // (v11.10.0)
  }
});
```

{% hint style="warning" %}
Please be aware if you are using **React 15 or below**, you are required to set the `defaultTransParent` option, or pass a `parent` via props.
{% endhint %}

{% hint style="danger" %}
**Are you having trouble when your website is ran through Google Translate?**\
Google Translate seems to manipulate the DOM and makes React quite unhappy!\
**There's a work around:** you can wrap text nodes with`<span>` using `transWrapTextNodes: 'span'`.

*If you want to know more about the Google Translate issue with React, have a look at* [*this*](https://github.com/facebook/react/issues/11538#issuecomment-390386520)*.*
{% endhint %}


# I18nextProvider

## What it does

The I18nextProvider does take an i18next instance via prop i18n and passes that down using the context API.

```jsx
import { I18nextProvider } from 'react-i18next';
import i18n from './i18n';
import App from './App';

<I18nextProvider i18n={i18n} defaultNS={'translation'}>
  <App />
</I18nextProvider>
```

## When to use?

You will need to use the provider if you need to support multiple i18next instances - eg. if you provide a component library ([like this example](https://github.com/i18next/react-i18next/tree/master/example/react-component-lib)) or in scenarios for [SSR (ServerSideRendering)](https://react.i18next.com/latest/ssr). Additionally, you have the ability to manage the default namespace(s) by passing defaultNS.

## I18nextProvider props

| ***name***    | **type (*****default)***        | ***description***                                                                         |
| ------------- | ------------------------------- | ----------------------------------------------------------------------------------------- |
| **i18n**      | object (undefined)              | pass i18next instance the provider will pass it down to translation components by context |
| **defaultNS** | string \| string\[] (undefined) | pass defaultNS to manage the default namespace(s)                                         |


# SSR (additional components)

## Using [Next.js](https://nextjs.org/) App Router?

Then check out [this article](https://www.locize.com/blog/i18n-next-app-router) describing how to best internationalize it with i18next.

[![](https://cdn.prod.website-files.com/67a323e323a50df7f24f0a94/67f268673fcfae53e5d4697c_i18n-next-app-router.jpg)](https://www.locize.com/blog/i18n-next-app-router)

## Using [Next.js](https://nextjs.org/)?

You should have a look at [next-i18next](https://github.com/i18next/next-i18next) which extends react-i18next to bring it to next.js the easiest way.

> With `next-i18next@v8.0.0` and `Next.js v10`, next-i18next has done a major rewrite of the package, leveraging the built-in [internationalized routing](https://nextjs.org/docs/advanced-features/i18n-routing) provided by Next.js.
>
> [Here](https://github.com/locize/next-i18next-locize) you can also find a next-i18next app example in combination with locize, that offers 2 different approaches.
>
> `next-i18next@v5.0.0` supports `Next.js v9.5` in [**Serverless** mode](https://nextjs.org/blog/next-8#serverless-nextjs) (as of [July 2020](https://github.com/isaachinman/next-i18next/issues/274#issuecomment-664616304)). If your goal is to use earlier versions of Next.js with Serverless, then you should have a look at ["Next Right Now"](https://github.com/UnlyEd/next-right-now), which is a Next.js 9 boilerplate with built-in `i18next`, `react-i18next` and Locize.
>
> **Looking for an optimized Next.js translations setup?**\
> [Here](https://locize.com/blog/next-i18next/) you'll find a blog post on how to best use next-i18next with client side translation download and SEO optimization.
>
> [![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FoAxHedQ5XnB6rQXtv0hn%2Fnext-i18next.jpg?alt=media\&token=7a4b9ade-447c-40bf-9341-6148372b6158)](https://locize.com/blog/next-i18next/)
>
> ***
>
> **Using SSG / `next export`?**\
> [Here](https://locize.com/blog/next-i18n-static/) you'll find a simple tutorial on how to best use next-i18next in a SSG environment.\
> [<img src="https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FP2JgdD4y4e3ChxOD5iMJ%2Fnext-ssg.jpeg?alt=media&#x26;token=36be4696-ea79-4f73-a9f8-a139fbaaa045" alt="" data-size="original">](https://locize.com/blog/next-i18n-static/)

## Using [Remix](https://remix.run)?

You should have a look at [remix-i18next](https://github.com/sergiodxa/remix-i18next) which extends react-i18next to bring it to Remix the easiest way.

> [Here](https://github.com/locize/locize-remix-i18next-example) you'll find a simple example and [here a step by step tutorial](https://locize.com/blog/remix-i18n/) on how to best use remix-i18next.
>
> [![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FnMxpvTcUJTKOe0CoaBgO%2Fremix-localization.jpg?alt=media\&token=cacac368-f199-417b-8a36-3ccb90f26384)](https://locize.com/blog/remix-i18n/)

## Using [Gatsby](https://www.gatsbyjs.com/)?

You should have a look at [gatsby-plugin-react-i18next](https://github.com/microapps/gatsby-plugin-react-i18next) which extends react-i18next to bring it to Gatsby the easiest way.

> [Here](https://github.com/locize/locize-gatsby-example) you'll find a simple example and [here a step by step tutorial](https://locize.com/blog/gatsby-i18n/) on how to best use [gatsby-plugin-react-i18next](https://github.com/microapps/gatsby-plugin-react-i18next).
>
> [![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-L9iS6WpW81N7RGRTQ-K%2Fuploads%2FoHXi7oJPwGpWEgt3Mbtv%2Fgatsby-i18next.jpg?alt=media\&token=c27b1939-46eb-4d97-9124-ba2c33fd3190)](https://locize.com/blog/gatsby-i18n/)

## Setting the i18next instance based on req

Use the [I18nextProvider](https://react.i18next.com/latest/i18nextprovider) to inject the i18next instance for example bound to the http i18n instance on the request object using [i18next-http-middleware](https://github.com/i18next/i18next-http-middleware).

```jsx
<I18nextProvider i18n={req.i18n}>
  <App />
</I18nextProvider>
```

## Passing initial translations / initial language down to client

To avoid asynchronous loading of translation on the client side (and the possible Suspense out of that) you will need to pass down initialLanguage (will call changeLanguage on i18next) and initialI18nStore (will prefill translations in i18next store).

### using the useSSR hook

```jsx
import React from 'react';
import { useSSR } from 'react-i18next';

export function InitSSR({ initialI18nStore, initialLanguage }) {
  useSSR(initialI18nStore, initialLanguage);

  return <App />
}
```

### using the withSSR HOC

```jsx
import React from 'react';
import { withSSR } from 'react-i18next';
import App from './App';

const ExtendedApp = withSSR()(App);

<ExtendedApp initialLanguage={} initialI18nStore={} />
```

The ExtendedApp in this case will also have the composed `ExtendedApp.getInitialProps()`


# Migrating v9 to v10

v10 is a complete rewrite, taking the chance to clean up some complexity added from v1 to v9.

This means you will need to test your application more cautiously before release.

{% hint style="info" %}
This is a specific migration guide regarding the complete react-i18next rewrite in v10.\
If you're looking for general release notes, please have a look in the [CHANGELOG](https://github.com/i18next/react-i18next/blob/master/CHANGELOG.md) file.
{% endhint %}

## New in v10

The most obvious change is the hook function for use inside functional components:

```jsx
import React from 'react';
import { useTranslation } from 'react-i18next';

export function MyComponent() {
  const [t, i18n] = useTranslation();

  return <p>{t('my translated text')}</p>
}
```

## Components without replacement

The Interpolation component (which was marked as deprecated for a long time and replaced by the Trans Component) was removed finally. You will need to replace it with the Trans Component.

## Migration

Replace your components like described below. If you don't have to use `Suspense` in your existing App you can set `useSuspense: false` in react.init options.react:

```javascript
i18n.init({
  react: {
    useSuspense: false
  }
});
```

## I18nextProvider changes

The `I18nextProvider` no longer provides as many properties as before. Make the necessary changes in your codebase after migrating.

```javascript
// New props
{
  i18n,
  defaultNS,
}

// Old props
{
  i18n,
  defaultNS,
  reportNS,
  lng: i18n && i18n.language,
  t: i18n && i18n.t.bind(i18n),
}
```

## Components v9 -> v10

| Type                | <= v7 (v8)         | v9 (v8)            | v10              |
| ------------------- | ------------------ | ------------------ | ---------------- |
| hook                |                    | -                  | useTranslation   |
| HOC                 | translate          | withNamespaces     | withTranslation  |
| render prop         | I18n               | NamespacesConsumer | Translation      |
| i18next plugin      | reactI18nextModule | reactI18nextModule | initReactI18next |
| Provider            | I18nextProvider    | I18nextProvider    | I18nextProvider  |
| Complex Translation | Trans              | Trans              | Trans            |
| Interpolations      | Interpolate        | Interpolate        | Trans            |


# TypeScript

{% hint style="warning" %}
Make sure you update to **react-i18next >= 13.0.0** and **i18next >= 23.0.1** and follow the instructions [here](https://www.i18next.com/overview/typescript).
{% endhint %}


# Using with ICU format

i18next itself is flexible enough to support multiple existing i18next formats beside its own. So also the ICU format, thanks to [i18next-icu](https://github.com/i18next/i18next-icu).

{% hint style="info" %}
Find the full working sample [here](https://github.com/i18next/react-i18next/tree/master/example/react-icu).
{% endhint %}

![](https://4236364459-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-L9iS6WpW81N7RGRTQ-K%2F-LIeYJONIqnkfR4eHYLx%2F-LIeYNAt0tyLaBiaeOVa%2FScreen%20Shot%202018-07-30%20at%2010.25.19.png?alt=media\&token=9f9ddb82-a1df-4afd-bb58-0a36207a23db)

## Extend the i18n instance with ICU module

To enable ICU format you will need to include the [i18next-icu](https://github.com/i18next/i18next-icu) module into your [i18next instance](https://react.i18next.com/legacy-v9/i18next-instance).

```javascript
import i18n from 'i18next';
import ICU from 'i18next-icu';
import Backend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
import { reactI18nextModule } from 'react-i18next';

i18n
  .use(ICU)
  .use(Backend)
  .use(LanguageDetector)
  .use(reactI18nextModule) // if not using I18nextProvider
  .init({
    fallbackLng: 'en',
    debug: true,

    interpolation: {
      escapeValue: false, // not needed for react!!
    },

    // react i18next special options (optional)
    react: {
      bindI18n: 'languageChanged loaded',
      bindStore: 'added removed',
      nsMode: 'default'
    }
  });


export default i18n;
```

## Use the ICU format

### using t function

{% tabs %}
{% tab title="JavaScript" %}

```jsx
import React, { Component } from 'react';
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t, i18n } = useTranslation();
  // or const [t, i18n] = useTranslation();
  
  return <div>{t('icu', { numPersons: 500 })}</div>
}

// ...

// json
"icu": "{numPersons, plural, =0 {no persons} =1 {one person} other {# persons}}",

// result:
<div>500 persons</div>
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
import React, { Component } from 'react';
import { useTranslation } from 'react-i18next';

function MyComponent() {
  const { t, i18n } = useTranslation();
  // or const [t, i18n] = useTranslation();
  
  return <div>{t($ => $.icu, { numPersons: 500 })}</div>
}

// ...

// json
"icu": "{numPersons, plural, =0 {no persons} =1 {one person} other {# persons}}",

// result:
<div>500 persons</div>
```

{% endtab %}
{% endtabs %}

### using the Trans Component

{% hint style="warning" %}
Warning: direct use of `Trans` (not using the `icu.macro` babel macro) may not be compatible with [`react-compiler`](https://react.dev/learn/react-compiler). Use the `IcuTrans` component or the `icu.macro` babel macro instead.
{% endhint %}

Using ICU syntax is not possible within a JSX node because `{curly brackets}` are reserved for interpolation.

To work around this, you can use the [IcuTrans Component](https://github.com/i18next/react-i18next-gitbook/blob/master/latest/icu-trans-component.md) directly like this:

```javascript
import { IcuTrans } from 'react-i18next';

const user = 'John Doe';

<IcuTrans
  i18nKey="icu_and_trans"
  defaultTranslation="We invited <0>{user}</0>."
  content={[{ type: "strong" }]}
  values={{ user }}
/>

// json
"icu_and_trans": "We invited <0>{user}</0>."

// result
We invited <strong>John Doe</strong>.
```

While this works the resulting JSX is very verbose and prone to errors. Let's use a babel macro to provide more intuitive syntax!

### using babel macros (Trans, Plural, Select)

{% hint style="info" %}
Thanks to using [kentcdodds/babel-plugin-macros](https://github.com/kentcdodds/babel-plugin-macros) we could use some babel magic to transpile nicer looking jsx to above Trans markup.

Check <https://github.com/kentcdodds/babel-plugin-macros/blob/master/other/docs/user.md> for setting babel-plugin-macros up.

Using create-react-app? Make sure you are using react-scripts v2 as it includes the macro plugin.

```
$ # Create a new application
$ npx create-react-app
$ # Upgrade an existing application
$ yarn upgrade react-scripts@2
```

{% endhint %}

```javascript
import { Trans } from 'react-i18next/icu.macro';

const user = 'John Doe';

<Trans i18nKey="icu_and_trans">
  We invited <strong>{user}</strong>.
</Trans>
```

The macro will add the needed import for the `IcuTrans` Component and generate the correct `IcuTrans` component for you.

The correct string for translations will be shown in the browser console output as a missing string (if set debug: true on i18next init) or submitted via saveMissing (have saveMissing set true and a i18next backend supporting saving missing keys).

The defaults parsing supports the `@babel/react` preset, so any expressions that require more complex parsing may not work.

**More samples:**

```jsx
// basic interpolation
<Trans>Welcome, { name }!</Trans>

// interpolation and components
<Trans>Welcome, <strong>{ name }</strong>!</Trans>
<Trans defaults="Welcome, <strong>{ name }</strong>" />

// number formatting
<Trans>Trainers: { trainersCount, number }</Trans>
<Trans>Trainers: <strong>{ trainersCount, number }</strong>!</Trans>
<Trans defaults="Trainers: <strong>{ trainersCount, number }</strong>!" />

// date formatting
<Trans>Caught on { catchDate, date, short }</Trans>
<Trans>Caught on <strong>{ catchDate, date, short }</strong>!</Trans>
<Trans defaults="Caught on <strong>{ catchDate, date, short }</strong>!" />

<Trans>You have <Link to="/inbox">{ unread, number } messages</Link></Trans>
<Trans defaults="You have <Link to='/inbox'>{ unread, number } messages</Link>" />
```

#### Tagged Template for ICU

To support complex interpolations, `react-i18next` provides additional imports from the `icu.macro`. These provide a way to represent translations closer to the ICU messageformat syntax, but in a manner that is compatible with React and strictly typed in typescript.

For example, to format a number:

```javascript
import { Trans } from "react-i18next/icu.macro";

const num = 1;

<Trans i18nKey="number">
 Incremented {num, number} times
</Trans>
```

the above syntax, although valid javascript, will error when using a linting tool like eslint. Instead, we can do this:

```jsx
import { Trans, number } from "react-i18next/icu.macro";

const num = 1;

<Trans i18nKey="number">
 Incremented {number`${num}`} times
</Trans>
```

This results in the translation string `Incremented {num, number} times`

Supported interpolators are `number`, `date`, `time`, `select`, `plural`, and `selectOrdinal`.

More complex skeletons can also be represented:

```jsx
import { Trans, number } from "react-i18next/icu.macro";

const awesomePercentage = 100;

<Trans i18nKey="number">
 It's awesome {number`${awesomePercentage}, ::percent`} of the time
</Trans>
```

This results in the translation string `It's awesome {awesomePercentage, number, ::percent} of the time`.

**Complex interpolations with plural/select/selectOrdinal**

The `plural` and `select` and `selectOrdinal` interpolations support more advanced syntax. For instance, it is possible to interpolate both React elements and other interpolations:

```jsx
import { Trans, plural, number } from "react-i18next/icu.macro";

const awesomePercentage = 100;

<Trans i18nKey="number">
 {plural`${awesomePercentage},
   =0 { It's ${<i>never</i>} awesome }
   =100 { It is ${<b>ALWAYS</b>} awesome! }
   other { It's awesome {number`${awesomePercentage}, ::percent`} of the time }`}
</Trans>
```

This will result in the translation string `{awesomePercentage, plural, =0 { It's <0>never&lt;/0&gt; awesome } =100 { It is <1>ALWAYS&lt;/1&gt; awesome! } =100 { It's awesome {awesomePercentage, number, ::percent} of the time }}`

It possible to nest any interpolated type, including nested `plural`, `select`, or `selectOrdinal`.

**Typescript support for interpolated template strings**

The `number`, `plural`, and `selectOrdinal` functions will error if a non-number typed variable is interpolated.

```jsx
import { Trans, number } from "react-i18next/icu.macro";

// type error below - awesomePercentage must be a number
const awesomePercentage = "100";

<Trans i18nKey="number">
 It's awesome {number`${awesomePercentage}, ::percent`} of the time
</Trans>
```

The `date` and `time` functions will error if a non-Date object is interpolated.

```jsx
import { Trans, date } from "react-i18next/icu.macro";

// type error below - awesomePercentage must be a number
const notADate = "100";

<Trans i18nKey="number">
 What time is it? it's {date`${notADate}`} o'clock
</Trans>
```

Finally, the `select` function will error if a non-string is interpolated.

```jsx
import { Trans, select } from "react-i18next/icu.macro";

// type error below - awesomePercentage must be a number
const notAString = 100;

<Trans i18nKey="number">
 {select`${notAString} oops { you have to pass in a string } other { oh well }`}
</Trans>
```

### Alternative syntax for select and plural

It is also possible to display `select` and `plural` and `selectOrdinal` using Elements `Select`, `Plural` and `SelectOrdinal`. All of them have full type safety in typescript.

#### Select

There is no way to directly add the needed ICU format inside a JSX child - so we had to add another component that gets transpiled to needed Trans component:

```jsx
import { Select } from 'react-i18next/icu.macro';

// simple select
<Select
  i18nKey="optionalKey" // optional key
  switch={gender}
  male="He avoids bugs."
  female="She avoids bugs."
  other="They avoid bugs."
/>
```

```jsx
import { Select } from 'react-i18next/icu.macro';

// select with inner components
<Select
  i18nKey="optionalKey" // optional key
  switch={gender}
  male={<Trans><strong>He</strong> avoids bugs.</Trans>}
  female={<Trans><strong>She</strong> avoids bugs.</Trans>}
  other={<Trans><strong>They</strong> avoid bugs.</Trans>}
/>
```

#### Plural

```jsx
import { Plural } from 'react-i18next/icu.macro';

// simple plural
<Plural
  i18nKey="optionalKey" // optional key
  count={itemsCount}
  $0="There is no item."
  one="There is # item."
  other="There are # items."
/>
```

```jsx
import { Plural } from 'react-i18next/icu.macro';

// plural with inner components
<Plural
  i18nKey="optionalKey" // optional key
  count={itemsCount3}
  $0={<Trans>There is <strong>no</strong> item.</Trans>}
  one={<Trans>There is <strong>#</strong> item.</Trans>}
  other={<Trans>There are <strong>#</strong> items.</Trans>}
/>
```

#### SelectOrdinal

```jsx
import { SelectOrdinal } from 'react-i18next/icu.macro';

// simple SelectOrdinal
<SelectOrdinal
  i18nKey="optionalKey"
  count={position}
  one="You are #st in line"
  two="You are #nd in line"
  few="You are #rd in line"
  other="You are #th in line"
/>
```

```jsx
import { SelectOrdinal } from 'react-i18next/icu.macro';

// SelectOrdinal with inner components
<SelectOrdinal
  i18nKey="optionalKey"
  count={position}
  one={<Trans>You are <strong>#st in line</strong></Trans>}
  two={<Trans>You are <strong>#nd in line</strong></Trans>}
  few={<Trans>You are <strong>#rd in line</strong></Trans>}
  other={<Trans>You are <strong>#th in line</strong></Trans>}
  $7={<Trans>You are the lucky <strong>#th in line</strong></Trans>}
/>
```

{% hint style="info" %}
The needed plural forms can be looked up in the official unicode cldr table: <http://www.unicode.org/cldr/charts/33/supplemental/language_plural_rules.html>

In addition to the plural forms you can specify results for given number values like show above:

`0="show if zero"`

in ICU it would be `=0 {show if zero}` but `=` is not allowed to be leading char in attributes so we replaced it with `$`
{% endhint %}


# Using with fluent format

i18next itself is flexible enough to support multiple existing i18next formats beside it's own.

{% hint style="info" %}
Find the full working sample here:

<https://github.com/i18next/react-i18next/tree/master/example/react-fluent>
{% endhint %}


# Testing

For testing purpose of your component you should export the pure component without extending with the withTranslation hoc and test that:

```javascript
export MyComponent;
export default withTranslation('ns')(MyComponent);
```

In the test, test the myComponent export passing a t function mock:

```javascript
import { MyComponent } from './myComponent';

<MyComponent t={key => key} />
```

Or use <https://github.com/kadirahq/react-stubber> to stub i18n functionality:

{% tabs %}
{% tab title="JavaScript" %}

```jsx
const tDefault = (key) => key;
const StubbableInterpolate = mayBeStubbed(Interpolate);
const stubInterpolate = function () {
  stub(StubbableInterpolate, (props, context) => {
    const t = (context && context.t) || tDefault;
    return (<span>{t(props.i18nKey)}</span>);
  });
};
```

{% endtab %}

{% tab title="TypeScript" %}

```tsx
const tDefault = (key) => key;
const StubbableInterpolate = mayBeStubbed(Interpolate);
const stubInterpolate = function () {
  stub(StubbableInterpolate, (props, context) => {
    const t = (context && context.t) || tDefault;
    return (<span>{t($ => $[props.i18nKey])}</span>);
  });
};
```

{% endtab %}
{% endtabs %}

Or mock it like:

```javascript
jest.mock('react-i18next', () => ({
  // this mock makes sure any components using the translate HoC receive the t function as a prop
  withTranslation: () => Component => {
    Component.defaultProps = { ...Component.defaultProps, t: (i18nKey) => i18nKey };
    // or with TypeScript:
    //Component.defaultProps = { ...Component.defaultProps, t: (i18nKey: string) => i18nKey };
    return Component;
  },
}));
```

Or, when using the `useTranslation` hook instead of `withTranslation`, mock it like:

```javascript
jest.mock('react-i18next', () => ({
  // this mock makes sure any components using the translate hook can use it without a warning being shown
  useTranslation: () => {
    return {
      t: (i18nKey) => i18nKey,
      // or with TypeScript:
      //t: (i18nKey: string) => i18nKey,
      i18n: {
        changeLanguage: () => new Promise(() => {}),
      },
    };
  },
  initReactI18next: {
    type: '3rdParty',
    init: () => {},
  }
}));
```

or, you can also spy the `t` function:

{% tabs %}
{% tab title="JavaScript" %}

<pre class="language-jsx"><code class="lang-jsx"><strong>// implementation
</strong>import React from 'react';
import { useTranslation } from 'react-i18next';

export default function CustomComponent() {
  const { t } = useTranslation();

  return &#x3C;div>{t('some.key', { some: 'variable' })}&#x3C;/div>;
}

<strong>// test
</strong>import React from 'react';
import { mount } from 'enzyme';
import UseTranslationWithInterpolation from './UseTranslationWithInterpolation';
import { useTranslation } from 'react-i18next';

jest.mock('react-i18next', () => ({
  useTranslation: jest.fn(),
}));

it('test render', () => {
  const useTranslationSpy = useTranslation;
  const tSpy = jest.fn((str) => str);
  useTranslationSpy.mockReturnValue({
    t: tSpy,
    i18n: {
      changeLanguage: () => new Promise(() => {}),
    },
  });

  const mounted = mount(&#x3C;UseTranslationWithInterpolation />);

  // console.log(mounted.debug());
  expect(mounted.contains(&#x3C;div>some.key&#x3C;/div>)).toBe(true);

  // If you want you can also check how the t function has been called,
  // but basically this is testing your mock and not the actual code.
  expect(tSpy).toHaveBeenCalledTimes(1);
  expect(tSpy).toHaveBeenLastCalledWith('some.key', { some: 'variable' });
});
</code></pre>

{% endtab %}

{% tab title="TypeScript" %}

<pre class="language-tsx"><code class="lang-tsx"><strong>// implementation
</strong>import React from 'react';
import { useTranslation } from 'react-i18next';

export default function CustomComponent() {
  const { t } = useTranslation();

  return &#x3C;div>{t($ => $.some.key, { some: 'variable' })}&#x3C;/div>;
}

<strong>// test
</strong>import React from 'react';
import { mount } from 'enzyme';
import UseTranslationWithInterpolation from './UseTranslationWithInterpolation';
import { useTranslation } from 'react-i18next';

jest.mock('react-i18next', () => ({
  useTranslation: jest.fn(),
}));

it('test render', () => {
  const useTranslationSpy = useTranslation;
  const tSpy = jest.fn((str) => str);
  useTranslationSpy.mockReturnValue({
    t: tSpy,
    i18n: {
      changeLanguage: () => new Promise(() => {}),
    },
  });

  const mounted = mount(&#x3C;UseTranslationWithInterpolation />);

  // console.log(mounted.debug());
  expect(mounted.contains(&#x3C;div>some.key&#x3C;/div>)).toBe(true);

  // If you want you can also check how the t function has been called,
  // but basically this is testing your mock and not the actual code.
  expect(tSpy).toHaveBeenCalledTimes(1);
  expect(tSpy).toHaveBeenLastCalledWith('some.key', { some: 'variable' });
});
</code></pre>

{% endtab %}
{% endtabs %}

{% hint style="success" %}
You can find a full sample for testing with jest here: <https://github.com/i18next/react-i18next/tree/master/example/test-jest>
{% endhint %}

## Testing without stubbing

Alternatively, you could also test I18next without stubbing anything, by providing the correct configuration and fully wrapping your container in the provider.

### Example configuration for testing

```javascript
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

i18n
  .use(initReactI18next)
  .init({
    lng: 'en',
    fallbackLng: 'en',

    // have a common namespace used around the full app
    ns: ['translationsNS'],
    defaultNS: 'translationsNS',

    debug: true,

    interpolation: {
      escapeValue: false, // not needed for react!!
    },

    resources: { en: { translationsNS: {} } },
  });

export default i18n;
```

### Example test using this configuration

```javascript
import React from 'react';
import { Provider } from 'react-redux';
import { mount } from 'enzyme';
import { I18nextProvider } from 'react-i18next';
import configureStore from 'redux-mock-store';
import ContactTable from './ContactTable';
import actionTypes from '../constants';
import i18n from '../i18nForTests';

const mockStore = configureStore([]);
const store = mockStore({ contacts: [ ] });

it('dispatches SORT_TABLE', () => {
  const enzymeWrapper = mount(
    <Provider store={store}>
      <I18nextProvider i18n={i18n}>
        <ContactTable />
      </I18nextProvider>
    </Provider>
  );
  enzymeWrapper.find('.sort').simulate('click');
  const actions = store.getActions();
  expect(actions).toEqual([{ type: actionTypes.SORT_TABLE }]);
});
```

As translations aren't provided, `this.props.i18n.language` will be `undefined`. In case your application relies on that value you can mock resources by adding these lines to the object passed to init:

```
i18n
  .init({
    ...
    fallbackLng: 'en',
    resources: {
      en: {},
      de: {}
    }
  })
```

Now in your component `this.props.i18n.language` will return `en`.


# Step by step guide (v9)

{% hint style="warning" %}
This guide is based on an older react-i18next version! Please have a look at [this detailed guide](https://locize.com/blog/react-i18next/) for a newer version.
{% endhint %}

Let's start with the sample created in the [quick start guide](https://react.i18next.com/guides/quick-start) and extend it to be of more use.

{% hint style="info" %}
react-i18next will run in any environment without you having to do changes to your babel or webpack setup.
{% endhint %}

## Initial situation based on quick start

We have installed the needed i18n packages react-i18next and i18next:

```bash
npm install react-i18next@legacy i18next --save
```

Added following files:

**translation.json** (/public/locales/en/translation.json)

```javascript
{
  "Welcome to React": "Welcome to React and react-i18next"
}
```

**i18n.js** (/src/i18n.js)

```javascript
import i18n from "i18next";
import { reactI18nextModule } from "react-i18next";

import translationEN from '../public/locales/en/translation.json';

// the translations
const resources = {
  en: {
    translation: translationEN
  }
};

i18n
  .use(reactI18nextModule) // passes i18n down to react-i18next
  .init({
    resources,
    lng: "en",

    keySeparator: false, // we do not use keys in form messages.welcome

    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

export default i18n;
```

Make sure to import `i18n.js` in **index.js**:

```javascript
import React, { Component } from "react";
import ReactDOM from "react-dom";
import './i18n';
import App from './App';

// append app to dom
ReactDOM.render(
  <App />,
  document.getElementById("root")
);
```

Have **App.js** using the `t` function for translation:

```jsx
import React from 'react';

// the hoc
import { withNamespaces } from 'react-i18next';

function App ({ t }) {
  return <h1>{t('Welcome to React')}</h1>
}

export default withNamespaces()(App);
```

## 1) Adding more languages

### a) Add an additional language file

**translation.json** (/public/locales/**de**/translation.json)

```javascript
{
  "Welcome to React": "Willkommen bei react und react-i18next"
}
```

### b) Add the additional translations on init

in i18n.js:

```javascript
// ...
import translationEN from '../public/locales/en/translation.json';
import translationDE from '../public/locales/de/translation.json';

// the translations
const resources = {
  en: {
    translation: translationEN
  },
  de: {
    translation: translationDE
  }
};

// ...
```

### c) Auto detect the user language

As the language is set on `i18n.init` you either could create some custom code setting the needed language or just use one of the provided language detectors coming with i18next.

For browser usage there is the [i18next-browser-languageDetector](https://github.com/i18next/i18next-browser-languageDetector) which detects language based on:

* cookie
* localStorage
* navigator
* querystring (append `?lng=LANGUAGE` to URL)
* htmlTag
* path
* subdomain

```bash
npm install i18next-browser-languagedetector --save
```

Using it before i18n.init is all needed to get this to work:

```javascript
import i18n from "i18next";
import detector from "i18next-browser-languagedetector";
import { reactI18nextModule } from "react-i18next";

import translationEN from '../public/locales/en/translation.json';
import translationDE from '../public/locales/de/translation.json';

// the translations
const resources = {
  en: {
    translation: translationEN
  },
  de: {
    translation: translationDE
  }
};

i18n
  .use(detector)
  .use(reactI18nextModule) // passes i18n down to react-i18next
  .init({
    resources,
    fallbackLng: "en", // use en if detected lng is not available

    keySeparator: false, // we do not use keys in form messages.welcome

    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

export default i18n;
```

Now we already are able to set language based on the browsers set language or by appending `?lng=LANGUAGE` to the URL.

### d) Let the user toggle the language

Call [i18n.changeLanguage](https://www.i18next.com/overview/api#changelanguage) is all needed to do.

```jsx
import React from 'react';
import i18n from './i18n';
import { withNamespaces } from 'react-i18next';

function App ({ t }) {
  const changeLanguage = (lng) => {
    i18n.changeLanguage(lng);
  }

  return (
    <div>
      <button onClick={() => changeLanguage('de')}>de</button>
      <button onClick={() => changeLanguage('en')}>en</button>
      <h1>{t('Welcome to React')}</h1>
    </div>
  )
}

export default withNamespaces()(App);
```

{% hint style="info" %}
It's essential to have at least your outer page level / container component wrapped with the [withNamespaces](https://react.i18next.com/legacy-v9/withnamespaces) or [NamespacesConsumer](https://react.i18next.com/legacy-v9/namespacesconsumer) as those are bound to the [languageChanged event](https://www.i18next.com/overview/api#onlanguagechanged) and trigger a needed rerender.
{% endhint %}

## 2) Lazy loading translations

We haven't yet started splitting translations into multiple files (which is highly recommended for larger projects) but we already see that adding more languages would result in bundling unneeded translations into the application.

> Why not just use dynamic imports to load the language needed?

This for sure works but comes with one drawback. If you have a change in your translations you will need to rebuild your application and deploy that.

This might not be a problem when starting but at some point you will learn localization is a complete different beast than just adding i18n to your code. You will keep translations as separated from your code as you can - so developers and translators can work as independent as possible.

### a) Adding lazy loading for translations

This will be simpler than you think. All needed to be done is adding another package called [i18next-http-backend](https://github.com/i18next/i18next-http-backend) and using that.

```bash
npm install i18next-http-backend --save
```

**i18n.js**

```javascript
import i18n from "i18next";
import detector from "i18next-browser-languagedetector";
import backend from "i18next-http-backend";
import { reactI18nextModule } from "react-i18next";

// translations are already at
// '../public/locales/en/translation.json'
// which is the default for the xhr backend to load from

i18n
  .use(detector)
  .use(backend)
  .use(reactI18nextModule) // passes i18n down to react-i18next
  .init({
    fallbackLng: "en", // use en if detected lng is not available

    keySeparator: false, // we do not use keys in form messages.welcome

    interpolation: {
      escapeValue: false // react already safes from xss
    }
  });

export default i18n;
```

{% hint style="info" %}
i18next implementation is smart enough to only load needed languages and comes with intelligent deduplications so even multiple load requests for files in different code locations result in one request while notifying all needed requester.
{% endhint %}

### b) Loading multiple translation files

Lets assume your project started to grow and you like to split translations into multiple files.

Without configuration i18next will always load one file (namespace) named `translation`. Learn more about namespaces [here](https://www.i18next.com/principles/namespaces).

You can load them on i18n.init or in code like:

```javascript
i18n.init({
  ns: ['common', 'moduleA', 'moduleB'],
  defaultNS: 'moduleA'
}, (err, t) => {
  i18n.t('myKey'); // key in moduleA namespace (defined default)
  i18n.t('common:myKey'); // key in common namespace
});

// load additional namespaces after initialization
i18n.loadNamespaces('anotherNamespace', (err, t) => { /* ... */ });
```

But that will load all upfront or in some custom code where you would need to handle manually that the translations were loaded. So there is a better way.

#### Use the withNamespaces hoc

As you might guess the withNamespaces hocs role is to lazy load the needed namespaces.

**page2.json Add more translation files:** (/public/locales/en/page2.json)

```javascript
{
  "Welcome on page2": "Welcome on page2"
}
```

**Page2.js** (/src/Page2.js)

```jsx
import React from 'react';

// the hoc
import { withNamespaces } from 'react-i18next';

function Page2 ({ t }) {
  return <h1>{t('Welcome on page2')}</h1>
}

export default withNamespaces('page2')(Page2);
```

### c) Handle rendering while translations are not yet loaded

In the above `Page2` you will notice the initial render will trigger the load for `page2.json` but also render the page without the translations ready. There will be a rerender when the translations where loaded resulting in the page flickering.

#### Using the prop tReady

tReady will be set to true when translations are loaded so you can eg. suspend rendering and show a Spinner or another placeholder:

```jsx
import React from 'react';

// the hoc
import { withNamespaces } from 'react-i18next';

function Page2 ({ t, tReady }) {
  // just to add some more here we load an additional namespace
  // common for "common" used texts and use that namespace
  // be prefixing it in front of the key "common:"
  if (!tReady) return <p>{t('common:loading')}</p>

  return <h1>{t('Welcome on page2')}</h1>
}

export default withNamespaces(['page2', 'common'])(Page2);
```

#### Set the global wait option

You can configure the withNamespaces / NamespacesConsumer to not render the content until needed namespaces are loaded.

**i18n.js:**

```javascript
import i18n from "i18next";
import detector from "i18next-browser-languagedetector";
import backend from "i18next-http-backend";
import { reactI18nextModule } from "react-i18next";

i18n
  .use(detector)
  .use(backend)
  .use(reactI18nextModule) // passes i18n down to react-i18next
  .init({
    fallbackLng: "en", // use en if detected lng is not available

    keySeparator: false, // we do not use keys in form messages.welcome

    interpolation: {
      escapeValue: false // react already safes from xss
    },

    // react-i18next options
    react: {
      wait: true
    }
  });

export default i18n;
```

Now `Page2` will be blank until the needed translation files were loaded.

{% hint style="info" %}
You can set the wait option either globally for all instances or individually like:

`withNamepaces('page2', { wait: true })(Page2);`
{% endhint %}

## 3) Sidequest: natural vs. keybased catalog

### a) natural keys

Until now we had organised translation and keys in natural language.

```jsx
<h1>{t('Welcome on page2')}</h1>
```

Having translation files like:

```javascript
{
  "Welcome on page2": "Welcome on page2"
}
```

This was possible by setting `keySeparator: false` on `i18n.init`

The upside of this the code can be more readable but the content of the key might get soon rather different from the value it reflects. You could even go a step further by disabling any fallback language and [using the key as fallback](https://www.i18next.com/principles/fallback#key-fallback) - but be aware if you have a typo in the key acting as fallback value you will need to change it.

### b) keybased catalog

Some i18n frameworks organise having more technical keys allowing those to be even structured into hierarchies. This is the default in i18next too - so removing `keySeparator: false` on `i18n.init` would enable having catalogs and `t` usage like:

```javascript
{
  "titles": {
    "page2": "Welcome on page2"
  }
}
```

accessed like:

```jsx
<h1>{t('titles.page2')}</h1>
```

If you prefer natural or keybased is a matter of taste...both can be used with react-i18next. Just avoid mixing those styles.

## 4) HOCs are dead - long lives the render props

We won't open a debate over which is better as in our opinion both have their use case and there is no reason to just use one of the two options.

So you already saw before that you can use the [withNamespaces](https://react.i18next.com/legacy-v9/withnamespaces) to decorate your component to pass the `t` function down.

The same works with [a render prop](https://react.i18next.com/legacy-v9/namespacesconsumer):

```jsx
import React from 'react';

// the render prop
import { NamespacesConsumer } from 'react-i18next';

export default function Page2 () {
  (
    <NamespacesConsumer ns={['page2', 'common']}>
      {
        (t, { i18n, ready }) => (
          ready ?
            <h1>{t('Welcome on page2')}</h1> :
            <p>{t('common:loading')}</p>
        )
      }
    </NamespacesConsumer>
  )
}
```

## 5) Translate JSX nodes as one string

Let's translate this:

> Translating content with **formatting** or a [link](#5-translate-jxs-nodes-as-one-string) is a pain.

For this your JSX might look like:

```jsx
<p>
  Translating content with 
  <strong>formatting</strong> 
  or a 
  <a href="#">link</a> 
  is a pain.
</p>
```

So naive approach using the `t` function would result in

```jsx
<p>
  { t('Translating content with ') }
  <strong>t('formatting')</strong> 
  { t(' or a ') }
  <a href="#">t('link')</a> 
  { t(' is a pain.') }
</p>
```

So you end up with 5 keys in your translation file and your translator has no idea about how these 5 keys relate to each other. Further what happens in other languages where the order needs to be changed?!?

So you won't have luck with this approach.

### Using the Trans component

The [Trans component](https://react.i18next.com/legacy-v9/trans-component) enables you to keep this as one sentence by replacing the JSX nodes with indexed pseudo tags.

```jsx
import { Trans } from 'react-i18next';

// ...

<p>
  <Trans>
    Translating content with 
    <strong>formatting</strong> 
    or a 
    <a href="#">link</a> 
    is a pain.
  </Trans>
</p>
```

Resulting in JSON:

```javascript
{
  "Translating content with <1>formatting</1> or a <3>link</3> is a pain.": 
"Translating content with <1>formatting</1> or a <3>link</3> is a pain."
}
```

The `<1>`, `<3>` pseudo tags are based on the index of appearance in `nodes.children`:

```jsx
<Trans>
  Translating content with     // index 0
  <strong>formatting</strong>  // index 1
  or a                         // index 2
  <a href="#">link</a>         // index 3
  is a pain.                   // index 4
</Trans>
```

The Trans component also supports interpolation and plurals just read the [full documentation](https://react.i18next.com/legacy-v9/trans-component) of that component.


# Overview (v9)

react-i18next depends on i18next to provide the localization features. So there are two main things flowing through your render tree:

1. The [i18next instance](https://react.i18next.com/legacy-v9/i18next-instance) (short **i18n**)
2. The [translation function](https://www.i18next.com/overview/api#t) (short **t**)

{% hint style="info" %}
While we primary rely on react context to pass down **i18n** and **t** the components are built to also accept those via props, options or in case of i18n via internal context / reactI18nextModule.
{% endhint %}

## Components

| Component                                                                                                                                    | Props               | Provides            | Consumes        |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------- | --------------- |
| [I18nextProvider](https://react.i18next.com/legacy-v9/i18nextprovider)                                                                       | **i18n,** defaultNS | **i18n,** defaultNs |                 |
| [NamespacesConsumer](https://react.i18next.com/legacy-v9/namespacesconsumer) is a render prop                                                |                     | **t**, i18n         | i18n            |
| [withNamespaces](https://react.i18next.com/legacy-v9/withnamespaces) hoc                                                                     |                     | **t**, i18n         | i18n            |
| [Trans Component](https://react.i18next.com/legacy-v9/trans-component) is used to translate JSX nodes where just using **t** is insufficient |                     |                     | **t**, **i18n** |

This means your tree will look something like this *(assuming you use the options I18nextProvider):*

{% hint style="info" %}
**I18nextProvider** --> **NamespacesConsumer** or **withNamespaces HOC** --> **Trans** or using **t** in your component
{% endhint %}

```javascript
import { I18nextProvider, NamespacesConsumer, Trans, withNamespaces } from 'react-i18next';
import i18n from `./i18n`; // the initialized i18next instance

export default function App () {
  return (
    <I18nextProvider i18n={i18n}>
      <NamespacesConsumer>
        {
          t => <h1>{t('key')}</h1>
        }
      </NamespacesConsumer>
      <MyComponentWithHoc />
    </I18nextProvider>
  )
}

function MyComponent({ t }) {
  return (
    <Trans i18nKey="userMessagesUnread" count={count}>
      Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
    </Trans>
  )
}

const MyComponentWithHoc = withNamespaces()(MyComponent);
```

## Getting the t function

To get the **t** function (providing the translation functionality) down to your component you have two options:

1. Using the [withNamespaces](https://react.i18next.com/legacy-v9/withnamespaces) hoc
2. Using the [NamespacesConsumer](https://react.i18next.com/legacy-v9/namespacesconsumer) render prop

## Getting the i18n function into the flow

You have the following options to pass the [i18next instance](https://react.i18next.com/legacy-v9/i18next-instance) to the hoc, render prop and Trans component:

### Use the [provider](https://react.i18next.com/legacy-v9/i18nextprovider)

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { I18nextProvider } from 'react-i18next';

import App from './App'; // your entry page
import i18n from './i18n'; // initialized i18next instance

ReactDOM.render(
  <I18nextProvider i18n={ i18n }>
    <App />
  </I18nextProvider>,
  document.getElementById('app')
);
```

### Use the reactI18nextModule

```javascript
import i18n from 'i18next';
import { reactI18nextModule } from 'react-i18next';


i18n
  .use(reactI18nextModule) // if not using I18nextProvider
  .init({ /* options */ });

export default i18n;
```


# i18next instance (v9)

The instance is an initialized i18next instance. In the following code snippet, we add a backend to load translations from server and a language detector for detecting user language.

> You can learn more about [i18next](http://i18next.com) and [plugins](https://www.i18next.com/plugins-and-utils.html#plugins) on the i18next website.

{% hint style="info" %}
The instance could be passed to the [I18nextProvider](https://react.i18next.com/legacy-v9/i18nextprovider) or directly to the [translate hoc](https://react.i18next.com/legacy-v9/broken-reference).

The **reactI18nextModule** used below is an alternative to using the [I18nextProvider](https://react.i18next.com/legacy-v9/i18nextprovider) and asserts that components ([render prop](https://react.i18next.com/legacy-v9/broken-reference), [hoc](https://react.i18next.com/legacy-v9/broken-reference)) lower in the element tree get access to the i18n instance.
{% endhint %}

```javascript
import i18n from 'i18next';
import XHR from 'i18next-xhr-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
import { reactI18nextModule } from 'react-i18next';


i18n
  .use(XHR)
  .use(LanguageDetector)
  .use(reactI18nextModule) // if not using I18nextProvider
  .init({
    fallbackLng: 'en',
    debug: true,

    interpolation: {
      escapeValue: false, // not needed for react!!
    },

    // react i18next special options (optional)
    react: {
      wait: false,
      bindI18n: 'languageChanged loaded',
      bindStore: 'added removed',
      nsMode: 'default'
    }
  });


export default i18n;
```

All additional options for react in init options:

| ***options*** | ***default***            | ***description***                                                                                                                                                                                                                                                                                                                                 |
| ------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| wait          | false                    | assert all provided namespaces are loaded before rendering the component (can be set [globally](https://react.i18next.com/legacy-v9/i18next-instance) too); note that rendering will not be blocked again when dynamically updating `ns` on the [render prop component](https://react.i18next.com/legacy-v9/broken-reference) after initial mount |
| nsMode        | 'default'                | *default:* namespaces will be loaded an the first will be set as default or *fallback:* namespaces will be used as fallbacks used in order provided                                                                                                                                                                                               |
| bindI18n      | 'languageChanged loaded' | which events trigger a rerender, can be set to false or string of events                                                                                                                                                                                                                                                                          |
| bindStore     | 'added removed'          | which events on store trigger a rerender, can be set to false or string of events                                                                                                                                                                                                                                                                 |

For more initialization options have look at the [docs](https://www.i18next.com/configuration-options.html).


# I18nextProvider (v9)

The provider is responsible to pass the i18next instance passed in by props down to all the [withNamespaces](https://react.i18next.com/legacy-v9/withnamespaces) hocs or [NamespacesConsumer](https://react.i18next.com/legacy-v9/namespacesconsumer) render prop using react context api.

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { I18nextProvider } from 'react-i18next';

import App from './App'; // your entry page
import i18n from './i18n'; // initialized i18next instance

ReactDOM.render(
  <I18nextProvider i18n={ i18n }>
    <App />
  </I18nextProvider>,
  document.getElementById('app')
);
```

For the i18n instance have a look at the [i18next instance page](https://react.i18next.com/legacy-v9/i18next-instance).

As an alternative you can use the [reactI18nextModule](https://react.i18next.com/legacy-v9/i18next-instance) in the i18n instance.

## The I18nextProvider props:

| ***name***       | **type (*****default)*** | ***description***                                                                                                          |
| ---------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| **i18n**         | object (undefined)       | pass i18next instance the provider will pass it down to translation components by context                                  |
| defaultNS        | string (undefined)       | optionally pass down a default namespace to your translate HOC, I18n render prop (without having to specify it there)      |
| initialI18nStore | object (undefined)       | pass in initial translations (useful for [serverside rendering](https://react.i18next.com/legacy-v9/serverside-rendering)) |
| initialLanguage  | string (undefined)       | pass in initial language (useful for [serverside rendering](https://react.i18next.com/legacy-v9/serverside-rendering))     |


# withI18n (v9)

{% hint style="info" %}
Was introduced in v8.0.0. Not available in older versions.
{% endhint %}

`withI18n` is a basic higher order component which passes mainly the `t` function down to the wrapped component.

```jsx
import React, { Component } from "react";
import { withI18n } from "react-i18next";

class MyComponent extends Component {
  render() {
    const { t } = this.props;

    return <h2>{t('Welcome to React')}</h2>;
  }
}
export default withI18n()(MyComponent);
```

{% hint style="danger" %}
This component won't trigger a rerender on language change. The passed down `t` function will be the same as calling `i18n.t` directly and not be bound to a specific namespace or even trigger a load of a namespace.

If you do **not pass in translations** on `i18n.init` we highly encourage using the [withNamespaces](https://react.i18next.com/legacy-v9/withnamespaces) hoc.
{% endhint %}


# withNamespaces (v9)

{% hint style="info" %}
Was introduced in v8.0.0. Not available in older versions.
{% endhint %}

The withNamespaces [hoc](https://reactjs.org/docs/higher-order-components.html) is responsible for passing the [**t** function](https://www.i18next.com/overview/api#t) to your component. It enables all the translation functionality provided by i18next. Further, it asserts your component gets re-rendered on language change or changes to the translation catalog itself (loaded translations).

```javascript
withNamespaces(namespaces, options)(MyComponent);
```

{% hint style="info" %}
To learn more about using the **t** function have a look at i18next documentation:

* [essentials](https://www.i18next.com/essentials.html)
* [interpolation](https://www.i18next.com/interpolation.html)
* [formatting](https://www.i18next.com/formatting.html)
* [plurals](https://www.i18next.com/plurals.html)
* ...
  {% endhint %}

## Sample

```javascript
import React from 'react';
import { withNamespaces } from 'react-i18next';

function TranslatableView(props) {
  const { t, tReady } = props;
  // tReady is true if translations were loaded.
  // Use wait option to not render before loaded
  // or render placeholder yourself if not tReady=false

  return (
    <div>
      <h1>{t('keyFromDefault')}</h1>
      <p>{t('anotherNamespace:key.from.another.namespace', { /* options t options */ })}</p>
    </div>
  )
}

export default withNamespaces([
  'defaultNamespace',
  'anotherNamespace'
], { /* additional options see below */ })(TranslatableView);

// or: short for only loading one namespace:
export default withNamespaces('defaultNamespace')(TranslatableView);

// or: short for using defaultNS defined in i18next
export default withNamespaces()(TranslatableView);

// or: using a function to return namespaces based on props
export default withNamespaces((props) => props.namespaces)(TranslatableView);
```

If not using the [reactI18nextModule](https://react.i18next.com/legacy-v9/i18next-instance) this hoc should be nested inside a [I18nextProvider](https://react.i18next.com/legacy-v9/i18nextprovider). Alternatively you can pass the i18next instance via prop `i18n`.

## Using with TypeScript

To help you using TypeScript and the @withNamespaces decorator here is a trival example:

```jsx
import * as React from 'react';
import { withNamespaces, WithNamespaces } from 'react-i18next';

class MyComponent extends React.PureComponent<WithNamespaces> {
  public render() {
    const { t } = this.props;
    return (
      <React.Fragment>
        <span>{t('my-component-content')}</span>
      </React.Fragment>
    );
  }
}
export default withNamespaces()(MyComponent);
```

## Set defaults for all used withNamespaces

Most time you like to change those values for every component.

Set those on i18next init:

```javascript
i18n.init({
  // ... other options
  react: {
    wait: false,
    withRef: false,
    bindI18n: 'languageChanged loaded',
    bindStore: 'added removed',
    nsMode: 'default'
  }
});
```

## withNamespaces options:

```javascript
export default withNamespaces(
  'defaultNamespace',
  { wait: true } // <-- options
)(TranslatableView);
```

| ***option***       | ***type (default)***              | ***description***                                                                                                                                                                                                                                           |
| ------------------ | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **wait**           | boolean (false)                   | <p>assert all provided namespaces are loaded before rendering the component (can be set <a href="i18next-instance">globally</a> too)</p><p><strong>In most cases you like to set this to true.</strong> If not handling not ready by evaluating tReady.</p> |
| nsMode             | string ('default')                | <p><em>default:</em> namespaces will be loaded an the first will be set as default or</p><p><em>fallback:</em> namespaces will be used as fallbacks used in order provided</p>                                                                              |
| innerRef           | function or object (undefined)    | <p>either pass in a object React.createRef or a ref function like (c) => this.myRef = c;</p><p><a href="https://gist.github.com/gaearon/1a018a023347fe1c2476073330cc5509">read more</a></p>                                                                 |
| bindI18n           | string ('languageChanged loaded') | which events trigger a rerender, can be set to false or string of events                                                                                                                                                                                    |
| bindStore          | string ('added removed')          | which events on store trigger a rerender, can be set to false or string of events                                                                                                                                                                           |
| omitBoundRerenders | boolean (true)                    | Does not trigger rerenders while state not ready - avoiding unneeded renders on init                                                                                                                                                                        |
| i18n               | object (undefined)                | pass i18next via options (useful for [next.js usage](https://github.com/i18next/react-i18next/tree/v9.x.x/example/nextjs)                                                                                                                                   |
| usePureComponent   | boolean (false)                   | use shallowEqual on props change if set to true                                                                                                                                                                                                             |

## withNamespaces props:

| ***name***       | ***type (default)*** | ***description***                                                                                                              |
| ---------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| i18n             | object (undefined)   | pass i18next instance by props instead of having it on context                                                                 |
| initialI18nStore | object (undefined)   | pass in initial translations (useful for [next.js usage](https://github.com/i18next/react-i18next/tree/v9.x.x/example/nextjs)) |
| initialLanguage  | object (undefined)   | pass in initial language (useful for [next.js usage](https://github.com/i18next/react-i18next/tree/v9.x.x/example/nextjs))     |


# NamespacesConsumer (v9)

{% hint style="info" %}
Was introduced in v8.0.0. Not available in older versions.
{% endhint %}

The NamespacesConsumer is a so called render prop. The component passes the [**t** function](https://www.i18next.com/overview/api#t) to child function and triggers loading the translation files defined. Further it asserts the component gets rerendered on language change or on changes to the translations themselves.

{% hint style="info" %}
To learn more about using the **t** function have a look at i18next documentation:

* [essentials](https://www.i18next.com/translation-function/essentials)
* [interpolation](https://www.i18next.com/translation-function/interpolation)
* [formatting](https://www.i18next.com/translation-function/formatting)
* [plurals](https://www.i18next.com/translation-function/plurals)
* ...
  {% endhint %}

## Sample usage

```javascript
import React from 'react';
import { NamespacesConsumer } from 'react-i18next';

function TranslatableView() {
  return (
    <NamespacesConsumer ns={[
      'defaultNamespace',
      'anotherNamespace'
    ]}>
      {
        (t, { i18n, ready }) => (
          <div>
            <h1>{t('keyFromDefault')}</h1>
            <p>{t('anotherNamespace:key.from.another.namespace', { /* options t options */ })}</p>
          </div>
        )
      }
    </NamespacesConsumer>
  )
}
```

## NamespacesConsumer props

| ***options***      | ***type (default)***              | ***description***                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------ | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **wait**           | boolean (false)                   | <p>assert all provided namespaces are loaded before rendering the component (can be set <a href="i18next-instance">globally</a> too).<br><br><em>Note that rendering will not be blocked again when dynamically updating the <code>ns</code> prop after initial mount.</em></p><p><strong>In most cases you like to set this to true.</strong> If not handling not ready by evaluating ready.</p> |
| nsMode             | string ('default')                | <p><em>default:</em> namespaces will be loaded and the first will be set as default<br><br><em>fallback:</em> namespaces will be used as fallbacks used in order provided</p>                                                                                                                                                                                                                     |
| bindI18n           | string ('languageChanged loaded') | which events trigger a rerender, can be set to false or string of events                                                                                                                                                                                                                                                                                                                          |
| bindStore          | string ('added removed')          | which events on store trigger a rerender, can be set to false or string of events                                                                                                                                                                                                                                                                                                                 |
| omitBoundRerenders | boolean (true)                    | Does not trigger rerenders while state not ready - avoiding unneeded renders on init                                                                                                                                                                                                                                                                                                              |
| i18n               | object (undefined)                | pass i18next via options (useful for [next.js usage](https://github.com/i18next/react-i18next/tree/v9.x.x/example/nextjs))                                                                                                                                                                                                                                                                        |
| initialI18nStore   | object (undefined)                | pass in initial translations (useful for [next.js usage](https://github.com/i18next/react-i18next/tree/v9.x.x/example/nextjs/pages/index.js#L29))                                                                                                                                                                                                                                                 |
| initialLanguage    | string (undefined)                | pass in initial language (useful for [next.js usage](https://github.com/i18next/react-i18next/tree/v9.x.x/example/nextjs/pages/index.js))                                                                                                                                                                                                                                                         |


# Trans Component (v9)

## Important note

While the Trans components gives you a lot of power by letting you interpolate or translate complexer react elements.

The truth is - In most cases you won't need it. **As long you have no react nodes you like to be integrated into a translated text** (text formatting, like `strong`, `i`, ...) **or adding some link component - you won't need it.**

All can be done by using the `t` function you get by the [translate hoc](https://react.i18next.com/legacy-v9/trans-component) or [I18n render prop](https://react.i18next.com/legacy-v9/trans-component).

{% hint style="info" %}
Using the **t** function have a look at i18next documentation:

* [essentials](https://www.i18next.com/translation-function/essentials)
* [interpolation](https://www.i18next.com/translation-function/interpolation)
* [formatting](https://www.i18next.com/translation-function/formatting)
* [plurals](https://www.i18next.com/translation-function/plurals)
* ...
  {% endhint %}

## Sample

So you learned there is no need to use the Trans component everywhere (the plain t function will just do fine in most cases).

This component enables you to nest any react content to be translated as one string. Supports both plural and interpolation.

*Let's say you want to create following html output:*

> Hello **Arthur**, you have 42 unread messages. [Go to messages](https://react.i18next.com/legacy-v9/trans-component).

**Before:** Your react code would have looked something like:

```javascript
<div>
  Hello <strong title="this is your name">{name}</strong>, you have {count} unread message(s). <Link to="/msgs">Go to messages</Link>.
</div>
```

**After:** With the trans component just change it to:

```javascript
<Trans i18nKey="userMessagesUnread" count={count}>
  Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

*Your en.json (translation strings) will look like:*

```javascript
"userMessagesUnread": "Hello <1>{{name}}</1>, you have {{count}} unread message. <5>Go to message</5>.",
"userMessagesUnread_plural": "Hello <1>{{name}}</1>, you have {{count}} unread messages.  <5>Go to messages</5>.",
```

{% hint style="info" %}
[**saveMissing**](https://www.i18next.com/overview/configuration-options#missing-keys) will send a valid defaultValue
{% endhint %}

### Alternative usage

Depending on using [ICU as translation format](https://github.com/i18next/i18next-icu) it is not possible to have the needed syntax as children (invalid jsx). You can alternatively use the component like:

```javascript
<Trans
  defaults="hello <0>{{what}}</0>"
  values={{ what: 'world'}}
  components={[<strong>univers</strong>]}
/>
```

## How to get the correct translation string?

Guessing replacement tags *(<0>\</0>)* of your component right is rather difficult. There are two options to get those translations directly generated by i18next.

1. use `debug = true` in i18next init call and watch your console for the missing key output
2. use the [saveMissing feature](https://www.i18next.com/configuration-options#missing-keys) of i18next to get those translations pushed to your backend or handled by a custom missing key handler.
3. understand how those numbers get generated from child index:

**jsx:**

```javascript
<Trans i18nKey="userMessagesUnread" count={count}>
    Hello <strong title={t('nameTitle')}>{{name}}</strong>, you have {{count}} unread message. <Link to="/msgs">Go to messages</Link>.
</Trans>
```

**results in string:**

```
"Hello <1>{{name}}</1>, you have {{count}} unread message. <5>Go to message</5>."
```

**based on** the node tree\*\*:\*\*

```javascript
Trans.children = [
  'Hello ',                           // index 0: only a string
  { children: [{ name: 'Jan'  }] },   // index 1: element strong -> child object for interpolation
  ', you have',                       // index 2: only a string
  { count: 10 },                      // index 3: just object for interpolation
  ' unread messages. ',               // index 4
  { children: [ 'Go to messages' ] }, // index 5: element link -> child just a string
  '.'
]
```

{% hint style="info" %}
**Rules:**

* child is a string => nothing to wrap just take the string
* child is an object => nothing to do it's used for interpolation
* child is an element: wrap it's children in \<i>\</i> where i is the index of that element position in children and handle it's children with same rules (starting element.children index at 0 again)
  {% endhint %}

## Trans props

| ***name*** | ***type (default)***      | ***description***                                                                                                      |
| ---------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| i18nKey    | string (undefined)        | is optional if you prefer to use text as keys you can omit that and the translation will be used as a key.             |
| count      | integer (undefined)       | optional count if you use a plural                                                                                     |
| parent     | node (undefined)          | a component to wrap the content into (default none, can be globally set on i18next.init) -> needed for **react < v16** |
| i18n       | object (undefined)        | i18next instance to use if not provided via context (using hoc or render props)                                        |
| t          | function (undefined)      | t function to use if not provided via context (using hoc or render props)                                              |
| defaults   | string (undefined)        | use this instead of default content in children (useful when using ICU)                                                |
| values     | object (undefined)        | interpolation values if not provided in children                                                                       |
| components | array\[nodes] (undefined) | components to interpolate based on index of tag <0>\</0>, ...                                                          |

## Additional options on i18next.init

```javascript
i18next.init({
  // ...
  react: {
    // ...
    hashTransKey: function(defaultValue) {
      // return a key based on defaultValue or if you prefer to just remind you should set a key return false and throw an error
    },
    defaultTransParent: 'div' // a valid react element - required before react 16
  }
});
```

{% hint style="warning" %}
Please be aware if you are using **React 15 or below**, you need to set the `defaultTransParent` or `parent` in props.
{% endhint %}


# Interpolate (v9)

{% hint style="danger" %}
Deprecated: We highly recommend having a look at the new [trans component](https://react.i18next.com/legacy-v9/trans-component) as it provides a better experience.&#x20;

This component will be remove in the next major version v9.0.0!!
{% endhint %}

The interpolate component enables you to interpolate react components into translation strings (eg. to use links).

the key:

```javascript
{
  "interpolateSample": "you can interpolate {{value}} or {{component}} via interpolate component!"
}
```

sample:

```javascript
import React from 'react';
import { translate, Interpolate } from 'react-i18next';

function TranslatableView(props) {
  const { t } = props;

  let interpolateComponent = <strong>a interpolated component</strong>;

  return (
    <div>
      <Interpolate i18nKey="ns:interpolateSample" value="some string" component={interpolateComponent} />
      {/*
        =>
        <span>
          you can interpolate "some string" or <strong>a interpolated component</strong> via interpolate component!
        </span>
      */}
    </div>
  )
}
```

You can use [formatting](https://www.i18next.com/formatting.html) as in i18next.

**props**:

* i18nKey: the key to lookup
* options: [options](http://i18next.com/docs/options/#t-options) to use for translation (exclude interpolation variables!)
* parent: optional component to wrap translation into (default 'span')
* useDangerouslySetInnerHTML: allows use of raw html tags in translation values
* dangerouslySetInnerHTMLPartElement: optional component to wrap parts of translation values into (default 'span'), used with `useDangerouslySetInnerHTML={true}` only
* i18n: i18next instance to use if not provided via context (using hoc or render props)
* t: t function to use if not provided via context (using hoc or render props)
* ...props: values to interpolate into found translation (eg. `my value with {{replaceMe}} interpolation`)

## using useDangerouslySetInnerHtml

Allows having html tags inside the translation with a restriction as those get wrapped in spans. You can't have a interpolation value inside a html tag.

the key:

```javascript
{
"interpolateSample": "you <strong>can</strong> interpolate {{value}} or {{component}} via interpolate component!"
}
```

sample:

```javascript
import React from 'react';
import { translate, Interpolate } from 'react-i18next';

function TranslatableView(props) {
  const { t } = props;

  let interpolateComponent = <strong>a interpolated component</strong>;

  return (
    <div>
      <Interpolate i18nKey="ns:interpolateSample" useDangerouslySetInnerHTML={true} value="some string" component={interpolateComponent} />
      {/*
        =>
        <span>
          you <strong>can</strong> interpolate "some string" or <strong>a interpolated component</strong> via interpolate component!
        </span>
      */}
    </div>
  )
}
```

## Alternatives

a) Use standard interpolation of i18next and dangerously insert that:

```javascript
<div dangerouslySetInnerHTML={{ __html: t('my-label', { link: yourURL }) }} />
```

b) use markdown, eg. [react-remarkable](https://github.com/acdlite/react-remarkable) and pass markdown formatted content from translations to the markdown component.


# SSR (v9)

## Using next.js?

You should have a look at [next-i18next](https://github.com/isaachinman/next-i18next) which extends react-i18next to bring it to next.js the easiest way.

## Samples

To learn more you should have a look at our samples:

* [razzle (sample provided by react-i18next)](https://github.com/i18next/react-i18next/tree/v9.x.x/example/razzle-ssr)
* [simpleblack's boilerplate](https://github.com/simpleblack/react-redux-universal-hot-example)

{% hint style="info" %}
The usage of the `reactI18nextModule` for holding the i18n instance is not a valid option (the instance would be set globally). Always use the I18nextProvider like done in the samples above.
{% endhint %}

For further information see this [issue](https://github.com/i18next/react-i18next/issues/375).

## Pass language and translations down to client

Both the [i18nextProvider](https://react.i18next.com/legacy-v9/i18nextprovider) and [translate hoc](https://react.i18next.com/legacy-v9/serverside-rendering) allow to pass in `initialI18nStore` and `initialLanguage`. By doing so the translations won't be loaded and initial clientside render will avoid any flickering or rerender by checksum mismatch.

For details check the docs of those components or **have a look at the examples above**.

## loadNamespaces helper

**loadNamespaces**: Function that will pre-load all namespaces used by your components. Works well with `react-router` `match` function

**props**:

* components: Components that need to have namespaces loaded.
* i18n: the i18n instance to load translations into

```javascript
import { I18nextProvider, loadNamespaces } from 'react-i18next';
import { match } from 'react-router';

match({...matchArguments}, (error, redirectLocation, renderProps) => {
   loadNamespaces({ ...renderProps, i18n: i18nInstance })
   .then(()=>{
      // All i18n namespaces required to render this route are loaded   
   })
});
```

## use the i18next-express-middleware

When using [i18next-express-middleware](https://github.com/i18next/i18next-express-middleware), you can use `req.i18n` as the `i18next` instance for `I18nextProvider` it will assert no request conflicts happen (each request gets it's cloned instance of i18next):

```javascript
import { I18nextProvider } from 'react-i18next';
import i18n from './i18next'; // your own initialized i18next instance
import App from './app';

app.use((req, res) => {
   const component = (
      <I18nextProvider i18n={req.i18n}>
         <App />
      </I18nextProvider>
   );

   // render as desired now ...
});
```


