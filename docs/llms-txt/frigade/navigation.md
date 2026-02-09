# Source: https://docs.frigade.com/sdk/navigation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Navigation

Frigade supports the ability to route users to different pages in your application through the `primaryButtonUri` and `secondaryButtonUri` props defined in the [Flow configuration](/component/tour#flow-configuration).

By default, Frigade will use the `window.location` object to navigate to the specified URI. This works well for some use cases, but it causes a full page refresh which can be disruptive.

For optimal performance, we recommend overriding this behavior by providing a custom `navigate` function to the `Frigade.Provider` component where you can use your own router for a smoother experience.

# Examples

Overriding the default navigation handler is different depending on your React framework of choice. Below are examples for the most popular Routers:

## Next.js App and Pages Router

```jsx  theme={"system"}
import * as Frigade from '@frigade/react';
import { useRouter } from 'next/navigation'; // or 'next/router' if using Pages Router

const App = () => {
  const router = useRouter();

  return (
    <Frigade.Provider
      navigate={(url, target) => {
        if (target === "_blank") {
          window.open(url, "_blank");
        } else {
          router.push(url);
        }
      }}
    >
      {children}
    </Frigade.Provider>
  );
}
```

## React Router

```jsx  theme={"system"}
import * as Frigade from '@frigade/react';
import { useHistory } from 'react-router-dom';

const App = () => {
  const history = useHistory();

  return (
    <Frigade.Provider
      navigate={(url, target) => {
        if (target === "_blank") {
          window.open(url, "_blank");
        } else {
          history.push(url);
        }
      }}
    >
      {children}
    </Frigade.Provider>
  );
}
```
