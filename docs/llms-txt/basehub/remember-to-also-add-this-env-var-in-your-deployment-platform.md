# Remember to also add this ^ env var in your deployment platform
```

### Configure Node Scripts

In order to generate the BaseHub SDK, we recommend running `basehub dev` in parallel to running the development server, and `basehub` right before building the app.

package.json

```
"scripts": {
  "dev": "basehub dev & next dev",
  "build": "basehub && next build",
  "start": "next start",
  "lint": "next lint"
},
```

info:

Using Windows? You might need to use something like `concurrently` instead of using the `&` to run a parallel node process. So:

`concurrently \”basehub dev\” \”next dev\”`

### Start the Dev Server

Give it a go to make sure the set up went correctly.

npm

```
npm run dev
```

Now, let’s go ahead and query some content!

## Your First Query

The recommended way to query content from BaseHub is with `<Pump />`, a React Server Component that enables a Fast Refresh-like experience.

app/page.tsx

```
import { Pump } from "basehub/react-pump"

const Page = () => {
  return (
    <Pump queries={[{ _sys: { id: true } }]}>
      {async ([data]) => {
        "use server"

        return (
          <pre>
            <code>{JSON.stringify(data, null, 2)}</code>
          </pre>
        )
      }}
    </Pump>
  )
}

export default Page
```

Notice we’re using Next.js’ `draftMode` and passing it down to Pump. You’ll learn more in the next section, but put briefly: when `draft === true`, Pump will subscribe to changes in real time from your Repo, and so keep your UI up-to-date. This is ideal for previewing content before pushing it to production. When `draft === false`, Pump will hit the Query API directly.