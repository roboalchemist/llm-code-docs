# Source: https://rspack.dev/api/loader-api/inline.md

CC 4.0 License> The content of this section is derived from the content of the following links and is subject to the CC BY 4.0 license.
> 
> - [https://webpack.js.org/concepts/loaders/#inline](https://webpack.js.org/concepts/loaders/#inline)
> 
> The following contents can be assumed to be the result of modifications and deletions based on the original contents if not specifically stated.
> 
> 


# Inline loaders

It's possible to specify loaders in an `import` statement, or any equivalent "importing" method. Separate loaders from the resource with `!`. Each part is resolved relative to the current directory.

```js
import Styles from 'style-loader!css-loader?modules!./styles.css';
```

It's possible to override any loaders, preLoaders and postLoaders from the configuration by prefixing the inline `import` statement:

- Prefixing with `!` will disable all configured normal loaders

  ```js
  import Styles from '!style-loader!css-loader?modules!./styles.css';
  ```

- Prefixing with `!!` will disable all configured loaders (preLoaders, loaders, postLoaders)

  ```js
  import Styles from '!!style-loader!css-loader?modules!./styles.css';
  ```

- Prefixing with `-!` will disable all configured preLoaders and loaders but not postLoaders

  ```js
  import Styles from '-!style-loader!css-loader?modules!./styles.css';
  ```

Options can be passed with a query parameter, e.g. `?key=value&foo=bar`, or a JSON object, e.g. `?{"key":"value","foo":"bar"}`.
