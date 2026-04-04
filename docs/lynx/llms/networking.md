# Source: https://lynxjs.org/guide/interaction/networking.md

# Networking

Many mobile apps need to load resources from remote URLs. You might want to make a POST request to a REST API or fetch a large amount of static content from another server.

## Using Fetch

:::tip

This feature depends on the HTTP service provided by the integrated [Lynx Service](/guide/start/integrate-with-existing-apps.md).

:::

Lynx provides a [Fetch API](/api/lynx-api/global/fetch.md) that is compatible with the standard Web API. You can refer to the MDN guide on [Using Fetch](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) for more information.

This example app fetches and displays user posts from the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/). It initializes with a loading state and triggers a Fetch API request to retrieve posts upon mounting. The fetched data is then displayed in a scrollable list, showing each post's ID and title. A "Loading..." message appears if the request is still in progress.


**This is an example below:  networking**

**Entry:** `src/fetch`
**Bundle:** `dist/fetch.lynx.bundle`

```tsx
import { root, useEffect, useState } from "@lynx-js/react";
import "./index.scss";

interface Post {
  userId: number;
  id: number;
  title: string;
  body: string;
}

const App = () => {
  const [isFetching, setFetching] = useState(true);
  const [posts, setPosts] = useState<Post[]>([]);

  const getPosts = async () => {
    try {
      const json = await fetch(
        "https://jsonplaceholder.typicode.com/posts",
      ).then((res) => res.json());
      setPosts(json);
    } catch (error) {
      console.error(error);
    } finally {
      setFetching(false);
    }
  };

  useEffect(() => {
    getPosts();
  }, []);

  return (
    <scroll-view scroll-y className="scroll-view">
      {isFetching ? <text className="scroll-view__loading">Loading...</text> : (
        posts.map((post) => (
          <view id={`${post.id}`} className="scroll-view__post">
            <text>{`${post.id} : ${post.title}`}</text>
          </view>
        ))
      )}
    </scroll-view>
  );
};

root.render(<App />);

if (import.meta.webpackHot) {
  import.meta.webpackHot.accept();
}

```



### Making Requests

To fetch content from an arbitrary `URL`, you can pass the `URL` to `fetch`:

```typescript
fetch('https://jsonplaceholder.typicode.com/todos/1');
```

`fetch` also takes an optional second argument that allows you to customize the HTTP request. You may want to specify additional `headers`, make a `POST` request, or provide a JSON `body`:

```typescript
fetch('https://jsonplaceholder.typicode.com/todos/1', {
  method: 'POST',
  headers: {
    'some-header': 'header',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    firstParam: 'yourValue',
    secondParam: 'yourOtherValue',
  }),
});
```

Take a look at the [Fetch Request](/api/lynx-api/global/fetch.md#request) for the properties supported by Lynx.

### Handling the Response

The above examples show how you can make a request. In many cases, you will want to do something with the response.

Networking is an inherently asynchronous operation. The `fetch` method returns a `Promise`, which makes it straightforward to write code that works asynchronously. You can use the `async/await` syntax to await the promise's resolution:

```typescript
const getDataFromApiAsync = async () => {
  try {
    const response = await fetch(
      'https://jsonplaceholder.typicode.com/todos/1',
    );
    const json = await response.json();
    return json;
  } catch (error) {
    console.error(error);
  }
};
```

Take a look at the [Fetch Response](/api/lynx-api/global/fetch.md#response) for the properties supported by Lynx.

Don't forget to catch any errors that `fetch` may throw; otherwise, they will be silently ignored.

## Using TextCodecHelper

Due to the lack of `TextEncoder`/`TextDecoder` support in `PrimJS`, Lynx provides
`TextCodecHelper` for basic encoding and decoding operations. This class
supports `UTF-8` conversions between `string` and `arraybuffer`.

Usage:

Convert `arraybuffer` to `string`:

```typescript
const str = TextCodecHelper.decode(arraybuffer);
```

Convert `string` to `arraybuffer`:

```typescript
const arraybuffer = TextCodecHelper.encode(str);
```

## Using Other Networking Libraries

The Fetch API is built into Lynx, which means you can use third-party libraries that rely on it.

It is important to note that Lynx's Fetch API has subtle differences compared to the [Web Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). You can check the [Fetch API Reference - Compatibility](/api/lynx-api/global/fetch.md#compatibility) section to learn more about these differences. As a result, you may need to adapt libraries from the web ecosystem to ensure compatibility. If you encounter any issues with the Lynx Fetch API, you are welcome to submit feature requests or [contribute](https://github.com/lynx-family/lynx/blob/develop/CONTRIBUTING.md) to help Lynx better support the web ecosystem.

For front-end framework-specific data fetching solutions, such as using [TanStack Query (React Query)](https://tanstack.com/query/latest) in ReactLynx, you can refer to the [Data Fetching](/react/data-fetching.md) chapter of the ReactLynx guide.
