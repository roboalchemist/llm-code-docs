# Source: https://docs.frigade.com/sdk/advanced/reverse-proxy.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.frigade.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Reverse Proxy and Custom Domains

A reverse proxy allows you to use your own domain when sending data to and from Frigade. To set up a reverse proxy, you need to create a `CNAME` record in your DNS settings.
The `CNAME` record should point to `api.frigade.com` and override the host header to `api.frigade.com`.

For example, if you want to use `api.example.com` as your domain, you should create a `CNAME` record for `api.example.com` that points to `api.frigade.com` and override the Host header to `api.frigade.com`.
Then, when instantiating Frigade in your application with the `<Frigade.Provider />` component, you should set the `apiUrl` to `https://api.example.com`:

For a more in depth guide on how to set up a reverse proxy, check out [this guide](https://posthog.com/docs/advanced/proxy) from Posthog.

```jsx  theme={"system"}
import * as Frigade from '@frigade/react';

const App = () => (
  <Frigade.Provider apiUrl="https://api.example.com">
    <App />
  </Frigade.Provider>
);
```
