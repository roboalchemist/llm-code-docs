# Source: https://docs.logrocket.com/reference/vuex.md

# Vuex

The LogRocket Vuex plugin logs Vuex mutations to the LogRocket console:

![858](https://files.readme.io/00591d0-687474703a2f2f692e696d6775722e636f6d2f6a3049327856572e706e67.png "687474703a2f2f692e696d6775722e636f6d2f6a3049327856572e706e67.png")

First, install with npm: `npm i --save logrocket-vuex`.

```javascript
import createPlugin from 'logrocket-vuex';

const logrocketPlugin = createPlugin(LogRocket);

const store = new Vuex.Store({
  // ...
  plugins: [logrocketPlugin]
});
```

If you'd like to scrub sensitive data from mutations, or prevent some types of mutations from being logged, you can pass a sanitizer function as the second argument to `createPlugin`.

The sanitizer function should take mutation and return a new object to log. If the sanitizer returns `null`, the mutation will not be logged.

```javascript Ignore Mutation
const logrocketPlugin = createPlugin(LogRocket, function(mutation) {
  if (mutation.type === 'SET_SECRET_TOKEN') {
    return null;
  }
  
  return mutation;
})
```

```javascript Scrub Mutation
const logrocketPlugin = createPlugin(LogRocket, function(mutation) {
  if (mutation.type === 'SET_SECRET_TOKEN') {
    return {
      ...mutation,
      removeThisKey: undefined,
    };
  }
  
  return mutation;
})
```

> 🚧 Session Filtering
>
> There currently is no way to filter over sessions containing a given Vuex mutation. They will appear as log entries in your sessions.