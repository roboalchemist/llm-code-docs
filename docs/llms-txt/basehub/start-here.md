# Start Here

> Learn how to integrate your Next.js App with BaseHub in a couple of steps.

## Set Up `basehub`

Our official JavaScript/TypeScript library exposes a CLI generator that, when run, will generate a type-safe GraphQL client. Check out [our API Reference](https://docs.basehub.com/api-reference/javascript-sdk) for more information.

### Install

Install with your preferred package manager.

npm

```
npm i basehub
```

### Add the `BASEHUB_TOKEN` Environment Variable

Get it from your BaseHub Repo’s “Connect to Your App” tab.

.env.local

```
BASEHUB_TOKEN="<your-token>"