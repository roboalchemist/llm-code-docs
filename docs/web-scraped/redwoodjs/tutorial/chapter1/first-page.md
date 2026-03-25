# Source: https://docs.redwoodjs.com/docs/tutorial/chapter1/first-page

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 1]
-   [Our First Page]

[Version: 8.8]

On this page

<div>

# Our First Page

</div>

Let\'s give our users something to look at besides the (awesome) Redwood welcome page (thanks [\@alicelovescake](https://github.com/alicelovescake)!). We\'ll use the `redwood` command line tool to create a page for us:

``` 
yarn redwood generate page home /
```

The command above does four things:

-   Creates `web/src/pages/HomePage/HomePage.tsx`. Redwood takes the name you specified as the first argument after `page` and [PascalCases](https://techterms.com/definition/pascalcase) it, then appends \"Page\" to construct your new page component. So \"home\" becomes \"HomePage\".
-   Creates a test file to go along with this new page component at `web/src/pages/HomePage/HomePage.test.tsx` with a single, passing test. You *do* write tests for your components, *don\'t you??*
-   Creates a Storybook file for this component at `web/src/pages/HomePage/HomePage.stories.tsx`. Storybook is a wonderful tool for efficiently developing and organizing UI components. (If you want to take a peek ahead, we learn about Storybook in [chapter 5 of the tutorial](/docs/tutorial/chapter5/storybook)).
-   Adds a `<Route>` in `web/src/Routes.tsx` that maps the path `/` to the new *HomePage* page.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Automatic import of pages in the Routes file

If you look in Routes you\'ll notice that we\'re referencing a component, `HomePage`, that isn\'t imported anywhere. Redwood automatically imports all pages in the Routes file since we\'re going to need to reference them all anyway. It saves a potentially huge `import` declaration from cluttering up the routes file.

In case you didn\'t notice, this page is already live (your browser automatically reloaded):

![Default HomePage render](https://user-images.githubusercontent.com/300/148600239-6a147031-74bb-43e8-b4ef-776b4e2a2cc5.png)

It\'s not pretty, but it\'s a start! Open the page in your editor, change some text and save. Your browser should reload with your new text.

### Routing[​](#routing "Direct link to Routing") 

Open up `web/src/Routes.tsx` and take a look at the route that was created:

-   JavaScript
-   TypeScript

web/src/Routes.jsx

``` 
import  from '@redwoodjs/router'

const Routes = () =>  name="home" />
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

web/src/Routes.tsx

``` 
import  from '@redwoodjs/router'

const Routes = () =>  name="home" />
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

As long as you have a route with path `/`, you\'ll never see the initial Redwood splash screen again.

When no route can be found that matches the requested URL, Redwood will render the `NotFoundPage`.

Try changing the route to something like:

-   JavaScript
-   TypeScript

``` 
<Route path="/hello" page= name="home" />
```

``` 
<Route path="/hello" page= name="home" />
```

The splash screen is available again at [http://localhost:8910/](http://localhost:8910/), giving you a list of all the available URLs in your app.

![Redwood Splash Screen](https://user-images.githubusercontent.com/17789536/160120107-1157af8e-4cbd-4ec8-b3aa-8adb28ea6eaf.png)

Go to `/hello` and you should see the homepage again.

Change the route path back to `/` before continuing!

### Simple Styles[​](#simple-styles "Direct link to Simple Styles") 

Previous versions of this tutorial had you build everything without any styling, so we could really focus on the code, but let\'s face it: an unstyled site is pretty ugly. Let\'s add a really simple stylesheet that will just make things a *little* easier on the eyes as we build out the site. Paste the following into `web/src/index.css`:

web/src/index.css

``` 
body 
ul 
li 
h1 > a 
button,
input,
label,
textarea 
label 
.error 
input.error,
textarea.error 
.form-error 
.form-error ul 
.form-error li 
.flex-between 
.flex-between button 
```

These styles will switch to whatever your OS\'s system font is, put a little margin between things, and just generally clean things up. Feel free to tweak it to your liking (or ignore these styles completely and stick with the browser default) but keep in mind that the following screenshots are made against this base stylesheet so your experience may vary.

![Default homepage with custom styles](https://user-images.githubusercontent.com/300/148600516-f8e048aa-451f-46f0-9749-078d63fe7b07.png)

Looking better already!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter1/first-page.md)