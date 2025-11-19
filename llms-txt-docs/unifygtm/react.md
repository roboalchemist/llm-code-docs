# Source: https://docs.unifygtm.com/developers/intent-client/react.md

# React

> Install the Unify Intent client in a React app.

<CardGroup cols={2}>
  <Card title="Github" icon="github" iconType="solid" href="https://github.com/unifygtm/intent-react" />

  <Card title="npm" icon="npm" iconType="solid" color="#BD0005" href="https://www.npmjs.com/package/@unifygtm/intent-react" />
</CardGroup>

## Installation

You can install the Unify Intent React library with your preferred package manager:

<CodeGroup>
  ```shell npm theme={null}
  npm install @unifygtm/intent-react
  ```

  ```shell yarn theme={null}
  yarn add @unifygtm/intent-react
  ```

  ```shell pnpm theme={null}
  pnpm add @unifygtm/intent-react
  ```
</CodeGroup>

## Usage

First, wrap your React app in a `UnifyIntentProvider`:

```tsx index.tsx theme={null}
import {
  UnifyIntentClient,
  UnifyIntentClientConfig,
  UnifyIntentProvider,
} from '@unifygtm/intent-react';

const writeKey = 'YOUR_PUBLIC_API_KEY';

const config: UnifyIntentClientConfig = {
  autoPage: true,
  autoIdentify: false,
};

const intentClient = new UnifyIntentClient(writeKey, config);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement,
);

root.render(
  <UnifyIntentProvider intentClient={intentClient}>
    <App />
  </UnifyIntentProvider>
);
```

The `UnifyIntentProvider` automatically takes care of mounting and unmounting the client
for you whenever the component mounts and unmounts. So any components rendered in your app
can freely access and use the intent client using the `useUnifyIntent` hook:

```tsx Example.tsx theme={null}
import { useUnifyIntent } from '@unifygtm/intent-react';

const Example = () => {
  // Get the Unify Intent Client
  const unify = useUnifyIntent();

  // However you access the current user...
  const currentUser = useCurrentUser();

  useEffect(() => {
    if (currentUser?.emailAddress) {
      // Log an identify event for the current user
      unify.identify(currentUser.emailAddress);
    }
  }, [currentUser, unify]);

  ...
};

export default Example;
```

You can then use the resulting client instance to log intent data. See the
[Usage](./client-spec) page for more details on how to use the client.
