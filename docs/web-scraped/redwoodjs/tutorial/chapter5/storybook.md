# Source: https://docs.redwoodjs.com/docs/tutorial/chapter5/storybook

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 5]
-   [Introduction to Storybook]

[Version: 8.8]

<div>

# Introduction to Storybook

</div>

Let\'s see what this Storybook thing is all about. Run this command to start up the Storybook server (you could stop your dev or test runners and then run this, or start another new terminal instance):

``` 
yarn rw storybook
```

After some compiling you should get a message saying that Storybook has started and it\'s available at [http://localhost:7910](http://localhost:7910)

![image](https://user-images.githubusercontent.com/300/153311732-21a62ee8-5bdf-45b7-b163-35a5ec0ce318.png)

If you poke around at the file tree on the left you\'ll see all of the components, cells, layouts and pages we created during the tutorial. Where did they come from? You may recall that every time we generated a new page/cell/component we actually created at least *three* files:

-   `Article.tsx`
-   `Article.stories.tsx`
-   `Article.test.tsx`

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

If you generated a cell then you also got a `.mock.ts` file (more on those later).

Those `.stories.tsx` files are what makes the tree on the left side of the Storybook browser possible! From their [homepage](https://storybook.js.org/), Storybook describes itself as:

*\"\...an open source tool for developing UI components in isolation for React, Vue, Angular, and more. It makes building stunning UIs organized and efficient.\"*

So, the idea here is that you can build out your components/cells/pages in isolation, get them looking the way you want and displaying the correct data, then plug them into your full application.

When Storybook opened it should have opened **Components \> Article \> Generated** which is the generated component we created to display a single blog post. If you open `web/src/components/Article/Article.stories.tsx` you\'ll see what it takes to explain this component to Storybook, and it isn\'t much:

-   JavaScript
-   TypeScript

web/src/components/Article/Article.stories.jsx

``` 
import Article from './Article'

export const generated = () => }
    />
  )
}

export default 
```

web/src/components/Article/Article.stories.tsx

``` 
import Article from './Article'

export const generated = () => }
    />
  )
}

export default 
```

You import the component you want to use and then all of the named exports in the file will be a single \"story\" as displayed in Storybook. In this case the generator named it \"generated\" which shows as the \"Generated\" story in the tree view:

``` 
Components
└── Article
    └── Generated
```

This makes it easy to create variants of your component and have them all displayed together.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Where did that sample blog post data come from?

In your actual app you\'d use this component like so:

-   JavaScript
-   TypeScript

``` 
<Article article= />
```

``` 
<Article article= />
```

Where the `article` in that prop comes from somewhere outside of this component. Here in Storybook there is no \"outside\" of this component, so we just send the article object into the prop directly.

**But where did the pre-filled article data come from?**

We (the Redwood team) added that to the story in the `redwood-tutorial` repo to show you what a story might look like after you hook up some sample data. Several of the stories need data like this, some inline and some in those `.mock.ts` files. The rest of the tutorial will be showing you how to do this yourself with new components as you create them.

**Where did the *actual* text in the body come from?**

[Hipster Ipsum](https://hipsum.co/), a fun alternative to Lorem Ipsum filler text!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter5/storybook.md)