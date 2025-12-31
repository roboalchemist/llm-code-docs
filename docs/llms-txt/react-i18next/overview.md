# Source: https://react.i18next.com/legacy-v9/overview.md

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
