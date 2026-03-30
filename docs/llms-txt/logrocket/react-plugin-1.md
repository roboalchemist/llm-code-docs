# Source: https://docs.logrocket.com/reference/react-plugin-1.md

# React Plugin

The LogRocket React plugin allows you to filter for sessions where the user clicks a specific component in your React app. The npm repository can be found [here](https://www.npmjs.com/package/logrocket-react).

<Image align="center" border={false} src="https://files.readme.io/031ae85-Screenshot_2024-07-12_at_8.38.07_AM.png" />

1. Install the LogRocket React package based on your React version.

```shell
// If using React 19
npm i --save logrocket-react@7

// If using React 18
npm i --save logrocket-react@6

// If using React 17
npm i --save logrocket-react@5

// If using React 16.10
npm i --save logrocket-react@4

// If using React 16.5 - 16.9
npm i --save logrocket-react@3

// If using React 16.4
npm i --save logrocket-react@2

// If using React <16.4
npm i --save logrocket-react@1

// If using React 0.14.0 or React 15:
npm i --save logrocket-react@^0.0.5
```

2. For the LogRocket React plugin to work properly, your components will need to have a `.displayName` property on them populated with the component's name - regardless of whether it's a class- or function-based component. This allows our React plugin to find and display a name for the component when JS compilers, such as [Babel](https://babeljs.io/), would otherwise minify and remove the names. There are multiple ways to do this, ranging from manually adding in the properties to finding/creating plugins for the compiler you use. Example plugins follow.
   1. **Babel** Add the [babel-plugin-transform-react-display-name](https://babeljs.io/docs/en/babel-plugin-transform-react-display-name) plugin to your Babel config. This official Babel plugin replaces an [old plugin](https://github.com/opbeat/babel-plugin-add-react-displayname) used for Babel 6.

```shell
npm i --save @babel/plugin-transform-react-display-name
```

```json
{
  presets: [ ... ],
  plugins: ["@babel/plugin-transform-react-display-name"],
}
```

3. Call `LogRocket` with the `logrocket-react` package.

```javascript
import LogRocket from 'logrocket';
import setupLogRocketReact from 'logrocket-react';

// after calling LogRocket.init()
setupLogRocketReact(LogRocket);
```

That's it! You can now filter for sessions which contain clicks on specific React components. See [Understanding User Flows](https://docs.logrocket.com/docs/understanding-user-flows) for more information on using LogRocket to understand your customer experience.

## Compatibility

To use the LogRocket React plugin with a server-side rendering framework, such as [Next.js](https://github.com/zeit/next.js/), you'll need to do the setup in client code. See [Using LogRocket with server-side rendering](https://docs.logrocket.com/docs/using-logrocket-with-server-side-rendering) for more details.