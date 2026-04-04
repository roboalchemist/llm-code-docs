# Custom Components in Rich Text

> Learn how to use custom components within rich text blocks.

Custom components in rich text allows you to extend beyond the basic rich text nodes. This can enable you to embed things like:

*   Tweets
    
*   Interactive code blocks
    
*   Callouts, or any other thing you can imagine…
    

In this guide, we’ll walk you through creating a component that fits your need, all the way to rendering it in your website.

### Create the component

To create a new component, we’ll go to somewhere in our editor and write `/component`. We’ll give it a name, and add some data into it.

In this case, we’ll create a “Tweet” component, we’ll add an ID block (required), and therefore Hide this component (to skip the “required” validation. [Learn more](https://help.basehub.com/dashboard/hiding-blocks)).

### Create a Rich Text block, and add our new component to “Component types”

Next, we’ll create a rich text block. You’d typically have this within a collection, but you can also drop it inside a regular document.

In this video, we also go ahead and add a tweet id for the tweet we want to embed.

### Set up the code environment

Let’s get BaseHub connected to a new Next.js App.

```
pnpm create next-app
```

We install basehub:

```
pnpm install basehub
```

Now, we add the basehub scripts so the codegen runs before next dev and next build. In `package.json`:

```
  "scripts": {
    "dev": "basehub dev & next dev --turbopack",
    "build": "basehub && next build",
    "start": "next start",
    "lint": "next lint"
  },
```

note:

Note: this snippet includes just package.json > scripts; you should keep the rest of the file as is.

We then add our `BASEHUB_TOKEN` to `.env.local`:

```
BASEHUB_TOKEN="<grab-this-from-your-dash>"
```

And finally, we run the dev server:

```
pnpm run dev
```

### Query the rich text block, using `blocks`

Let’s now create our first query, using Pump, to get the content in our Rich Text. Over in `app/page.tsx`, let’s replace everything with the following:

```
import { Pump } from "basehub/react-pump";

export default function Home() {
  return (
    <Pump
      queries={[
        {
          indexPage: {
            title: {
              json: {
                content: true,
                blocks: {
                  on_BlockDocument: {
                    __typename: true,
                    _id: true,
                  },
                  on_TweetComponent: {
                    id: true,
                  },
                },
              },
            },
          },
        },
      ]}
    >
      {async ([{ indexPage }]) => {
        "use server";
        return <pre>{JSON.stringify(indexPage, null, 2)}</pre>;
      }}
    </Pump>
  );
}
```

Now, when navigating to `http://localhost:3000`, you should see this in your screen:

![](https://assets.basehub.com/7b31fb4b/35edd3d0a37fafcbc15401509de27184/image?width=3840&quality=90&format=auto)

### Render it using `<RichText />`

Let’s now use the <RichText /> react component to handle our Tweet component. We import the component:

```
import { RichText } from 'basehub/react-rich-text'
```

And use it:

```
async ([{ indexPage }]) => {
  "use server"
  return (
    <RichText
      content={indexPage.title.json.content}
      blocks={indexPage.title.json.blocks}
      components={{
        TweetComponent: ({ id }) => {
          return <div>Render tweet: {id}</div>
        },
      }}
    />
  )
}
```

All together, that file now looks like this:

```
import { Pump } from "basehub/react-pump";
import { RichText } from "basehub/react-rich-text";

export default function Home() {
  return (
    <Pump
      queries={[
        {
          indexPage: {
            title: {
              json: {
                content: true,
                blocks: {
                  on_BlockDocument: {
                    __typename: true,
                    _id: true,
                  },
                  on_TweetComponent: {
                    id: true,
                  },
                },
              },
            },
          },
        },
      ]}
    >
      {async ([{ indexPage }]) => {
        "use server";
        return (
          <RichText
            content={indexPage.title.json.content}
            blocks={indexPage.title.json.blocks}
            components={{
              TweetComponent: ({ id }) => {
                return <div>Render tweet: {id}</div>;
              },
            }}
          />
        );
      }}
    </Pump>
  );
}
```

### Bonus: use `react-tweet` to render the tweet

Up until this point, you can already handle your own custom logic within those components. In our case, we’ll install react-tweet to render our tweet.

```
pnpm i react-tweet
```

And then adjust some things:

```
import { Tweet } from "react-tweet"

// the rest stays as is

TweetComponent: ({ id }) => {
  return <Tweet id={id} />
}
```

And the result is:

![](https://assets.basehub.com/7b31fb4b/99742717a125fe0a5df41efb9d190ed5/image?width=3840&quality=90&format=auto)

Not the prettiest, but a good foundation to build powerful rich texts!

## Wrapping Up

That’s all for this guide! Let us know if you have any questions or suggestions in our [Help Center](https://help.basehub.com?chat=true).

*   Code: [https://github.com/julianbenegas/rich-text-custom-components-demo](https://github.com/julianbenegas/rich-text-custom-components-demo)
    
*   Content: [https://basehub.com/jbtc/rich-text-components-demo](https://basehub.com/jbtc/rich-text-components-demo)