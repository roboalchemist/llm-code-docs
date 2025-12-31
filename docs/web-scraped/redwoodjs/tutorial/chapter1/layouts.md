# Source: https://docs.redwoodjs.com/docs/tutorial/chapter1/layouts

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 1]
-   [Layouts]

[Version: 8.8]

On this page

<div>

# Layouts

</div>

One way to solve the duplication of the `<header>` would be to create a `<Header>` component and include it in both `HomePage` and `AboutPage`. That works, but is there a better solution? Ideally there should only be one reference to the `<header>` anywhere in our code.

When you look at these two pages what do they really care about? They have some content they want to display. They really shouldn\'t have to care what comes before (like a `<header>`) or after (like a `<footer>`). That\'s where layouts come in: they wrap a page in a component that then renders the page as its child. The layout can contain any content that\'s outside the page itself. Conceptually, the final rendered document will be structured something like:

![Layouts structure diagram](https://user-images.githubusercontent.com/300/70486228-dc874500-1aa5-11ea-81d2-eab69eb96ec0.png)

Let\'s create a layout to hold that `<header>`:

``` 
yarn redwood g layout blog
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

From now on we\'ll use the shorter `g` alias instead of `generate`

That created `web/src/layouts/BlogLayout/BlogLayout.tsx` and associated test and stories files. We\'re calling this the \"blog\" layout because we may have other layouts at some point in the future (an \"admin\" layout, perhaps?).

Cut the `<header>` from both `HomePage` and `AboutPage` and paste it in the layout instead. Let\'s take out the duplicated `<main>` tag as well:

-   JavaScript
-   TypeScript

web/src/layouts/BlogLayout/BlogLayout.jsx

``` 
import  from '@redwoodjs/router'

const BlogLayout = () => >About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main></main>
    </>
  )
}

export default BlogLayout
```

web/src/layouts/BlogLayout/BlogLayout.tsx

``` 
import  from '@redwoodjs/router'

type BlogLayoutProps = 

const BlogLayout = (: BlogLayoutProps) => >About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main></main>
    </>
  )
}

export default BlogLayout
```

-   JavaScript
-   TypeScript

web/src/pages/AboutPage/AboutPage.jsx

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

const AboutPage = () => >Return home</Link>
    </>
  )
}

export default AboutPage
```

web/src/pages/AboutPage/AboutPage.tsx

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/web'

const AboutPage = () => >Return home</Link>
    </>
  )
}

export default AboutPage
```

-   JavaScript
-   TypeScript

web/src/pages/HomePage/HomePage.jsx

``` 
import  from '@redwoodjs/web'

const HomePage = () => 

export default HomePage
```

web/src/pages/HomePage/HomePage.tsx

``` 
import  from '@redwoodjs/web'

const HomePage = () => 

export default HomePage
```

In `BlogLayout.tsx`, `children` is where the magic will happen. Any page content given to the layout will be rendered here. And now the pages are back to focusing on the content they care about (we can remove the import for `Link` and `routes` from `HomePage` since those are in the Layout instead).

To actually render our layout we\'ll need to make a change to our routes files. We\'ll wrap `HomePage` and `AboutPage` with the `BlogLayout`, using a `<Set>`. Unlike pages, we do actually need an `import` statement for layouts:

-   JavaScript
-   TypeScript

web/src/Routes.jsx

``` 
import  from '@redwoodjs/router'
import BlogLayout from 'src/layouts/BlogLayout'

const Routes = () => >
        <Route path="/about" page= name="about" />
        <Route path="/" page= name="home" />
      </Set>
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

web/src/Routes.tsx

``` 
import  from '@redwoodjs/router'
import BlogLayout from 'src/layouts/BlogLayout'

const Routes = () => >
        <Route path="/about" page= name="about" />
        <Route path="/" page= name="home" />
      </Set>
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]The `src` alias

Notice that the import statement uses `src/layouts/BlogLayout` and not `../src/layouts/BlogLayout` or `./src/layouts/BlogLayout`. Being able to use just `src` is a convenience feature provided by Redwood: `src` is an alias to the `src` path in the current workspace. So if you\'re working in `web` then `src` points to `web/src` and in `api` it points to `api/src`.

Back to the browser (you may need to manually refresh) and you should see\...nothing different. But that\'s good, it means our layout is working!

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Why are things named the way they are?

You may have noticed some duplication in Redwood\'s file names. Pages live in a directory called `/pages` and also contain `Page` in their name. Same with Layouts. What\'s the deal?

When you have dozens of files open in your editor it\'s easy to get lost, especially when you have several files with names that are similar or even the same (they happen to be in different directories). Imagine a dozen files named `index.ts` and then trying to find the one you\'re looking for in your open tabs! We\'ve found that the extra duplication in the names of files is worth the productivity benefit when scanning for a specific open file.

If you\'re using the [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en) plugin this also helps disambiguate when browsing through your component stack:

![](https://user-images.githubusercontent.com/300/145901282-e4b6ec92-8cee-42d0-97ea-1ffe99328e53.png)

### Back Home Again[​](#back-home-again "Direct link to Back Home Again") 

A couple more `<Link>`s: let\'s have the title/logo link back to the homepage, and we\'ll add a nav link to Home as well:

-   JavaScript
-   TypeScript

web/src/layouts/BlogLayout/BlogLayout.jsx

``` 
import  from '@redwoodjs/router'

const BlogLayout = () => >Redwood Blog</Link>
        </h1>
        <nav>
          <ul>
            <li>
              <Link to=>Home</Link>
            </li>
            <li>
              <Link to=>About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main></main>
    </>
  )
}

export default BlogLayout
```

web/src/layouts/BlogLayout/BlogLayout.tsx

``` 
import  from '@redwoodjs/router'

type BlogLayoutProps = 

const BlogLayout = (: BlogLayoutProps) => >Redwood Blog</Link>
        </h1>
        <nav>
          <ul>
            <li>
              <Link to=>Home</Link>
            </li>
            <li>
              <Link to=>About</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main></main>
    </>
  )
}

export default BlogLayout
```

And then we can remove the extra \"Return to Home\" link (and Link/routes import) that we had on the About page:

-   JavaScript
-   TypeScript

web/src/pages/AboutPage/AboutPage.jsx

``` 
import  from '@redwoodjs/web'

const AboutPage = () => 

export default AboutPage
```

web/src/pages/AboutPage/AboutPage.tsx

``` 
import  from '@redwoodjs/web'

const AboutPage = () => 

export default AboutPage
```

![image](https://user-images.githubusercontent.com/300/145901020-1c33bb74-78f9-415e-a8c8-c8873bd6630f.png)

Now we\'re getting somewhere! We removed all of that duplication and our header content (logo and navigation) are all in one place.

Everything we\'ve done so far has been on the web side, which is all in the browser. Let\'s start getting the backend involved and see what all the hoopla is about GraphQL, Prisma and databases.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter1/layouts.md)