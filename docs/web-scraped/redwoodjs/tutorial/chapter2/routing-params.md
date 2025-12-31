# Source: https://docs.redwoodjs.com/docs/tutorial/chapter2/routing-params

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 2]
-   [Routing Params]

[Version: 8.8]

On this page

<div>

# Routing Params

</div>

Now that we have our homepage listing all the posts, let\'s build the \"detail\" page---a canonical URL that displays a single post. First we\'ll generate the page and route:

``` 
yarn rw g page Article
```

Now let\'s link the title of the post on the homepage to the detail page (and include the `import` for `Link` and `routes`):

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
import  from '@redwoodjs/router'

// QUERY, Loading, Empty and Failure definitions...

export const Success = () => >
          <header>
            <h2>
              <Link to=></Link>
            </h2>
          </header>
          <p></p>
          <div>Posted at: </div>
        </article>
      ))}
    </>
  )
}
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
import  from '@redwoodjs/router'

// QUERY, Loading, Empty and Failure definitions...

export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) => >
          <header>
            <h2>
              <Link to=></Link>
            </h2>
          </header>
          <p></p>
          <div>Posted at: </div>
        </article>
      ))}
    </>
  )
}
```

If you click the link on the title of the blog post you should see the boilerplate text on `ArticlePage`:

![Article page](https://user-images.githubusercontent.com/300/146100107-895a37af-7549-46fe-8802-2628fe6b49ed.png)

But what we really need is to specify *which* post we want to view on this page. It would be nice to be able to specify the ID of the post in the URL with something like `/article/1`. Let\'s tell the `<Route>` to expect another part of the URL, and when it does, give that part a name that we can reference later:

-   JavaScript
-   TypeScript

web/src/Routes.jsx

``` 
<Route path="/article/" page= name="article" />
```

web/src/Routes.tsx

``` 
<Route path="/article/" page= name="article" />
```

Notice the ``. Redwood calls these *route parameters*. They say \"whatever value is in this position in the path, let me reference it by the name inside the curly braces\". And while we\'re in the routes file, lets move the route inside the `Set` with the `BlogLayout`.

-   JavaScript
-   TypeScript

web/src/Routes.jsx

``` 
import  from '@redwoodjs/router'
import ScaffoldLayout from 'src/layouts/ScaffoldLayout'
import BlogLayout from 'src/layouts/BlogLayout'

const Routes = () =>  title="Posts" titleTo="posts" buttonLabel="New Post" buttonTo="newPost">
        <Route path="/posts/new" page= name="newPost" />
        <Route path="/posts//edit" page= name="editPost" />
        <Route path="/posts/" page= name="post" />
        <Route path="/posts" page= name="posts" />
      </Set>
      <Set wrap=>
        <Route path="/article/" page= name="article" />
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
import ScaffoldLayout from 'src/layouts/ScaffoldLayout'
import BlogLayout from 'src/layouts/BlogLayout'

const Routes = () =>  title="Posts" titleTo="posts" buttonLabel="New Post" buttonTo="newPost">
        <Route path="/posts/new" page= name="newPost" />
        <Route path="/posts//edit" page= name="editPost" />
        <Route path="/posts/" page= name="post" />
        <Route path="/posts" page= name="posts" />
      </Set>
      <Set wrap=>
        <Route path="/article/" page= name="article" />
        <Route path="/about" page= name="about" />
        <Route path="/" page= name="home" />
      </Set>
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

Cool, cool, cool. Now we need to construct a link that has the ID of a post in it:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
<h2>
  <Link to=)}></Link>
</h2>
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
<h2>
  <Link to=)}></Link>
</h2>
```

For routes with route parameters, the named route function expects an object where you specify a value for each parameter. If you click on the link now, it will indeed take you to `/article/1` (or `/article/2`, etc, depending on the ID of the post).

You may have noticed that when trying to view the new single-article page that you\'re getting an error. This is because the boilerplate code included with the page when it was generated includes a link to the page itself---a link which now requires an `id`. Remove the link and your page should be working again:

-   JavaScript
-   TypeScript

web/src/pages/ArticlePage.js

``` 
- import  from '@redwoodjs/router'
  import  from '@redwoodjs/web'

  const ArticlePage = () => >Article</Link>`
        */}
      </>
    )
  }

  export default ArticlePage
```

web/src/pages/ArticlePage.tsx

``` 
- import  from '@redwoodjs/router'
  import  from '@redwoodjs/web'

  const ArticlePage = () => >Article</Link>`
        */}
      </>
    )
  }

  export default ArticlePage
```

### Using the Param[​](#using-the-param "Direct link to Using the Param") 

Ok, so the ID is in the URL. What do we need next in order to display a specific post? It sounds like we\'ll be doing some data retrieval from the database, which means we want a cell. Note the singular `Article` here since we\'re only displaying one:

``` 
yarn rw g cell Article
```

And then we\'ll use that cell in `ArticlePage`:

-   JavaScript
-   TypeScript

web/src/pages/ArticlePage/ArticlePage.jsx

``` 
import  from '@redwoodjs/web'
import ArticleCell from 'src/components/ArticleCell'

const ArticlePage = () => 

export default ArticlePage
```

web/src/pages/ArticlePage/ArticlePage.tsx

``` 
import  from '@redwoodjs/web'
import ArticleCell from 'src/components/ArticleCell'

const ArticlePage = () => 

export default ArticlePage
```

Now over to the cell, we need access to that `` route param so we can look up the ID of the post in the database. Let\'s alias the real query name `post` to `article` and retrieve some more fields:

-   JavaScript
-   TypeScript

web/src/components/ArticleCell/ArticleCell.jsx

``` 
export const QUERY = gql`
  query FindArticleQuery($id: Int!) 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () => </div>
}
```

web/src/components/ArticleCell/ArticleCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

export const QUERY: TypedDocumentNode<
  FindArticleQuery,
  FindArticleQueryVariables
> = gql`
  query FindArticleQuery($id: Int!) 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = (: CellFailureProps<FindArticleQueryVariables>) => (
  <div style=}>Error: </div>
)

export const Success = (: CellSuccessProps<FindArticleQuery, FindArticleQueryVariables>) => </div>
}
```

Okay, we\'re getting closer. Still, where will that `$id` come from? Redwood has another trick up its sleeve. Whenever you put a route param in a route, that param is automatically made available to the page that route renders. Which means we can update `ArticlePage` to look like this:

-   JavaScript
-   TypeScript

web/src/pages/ArticlePage/ArticlePage.jsx

``` 
import  from '@redwoodjs/web'
import ArticleCell from 'src/components/ArticleCell'

const ArticlePage = () =>  />
    </>
  )
}

export default ArticlePage
```

web/src/pages/ArticlePage/ArticlePage.tsx

``` 
import  from '@redwoodjs/web'
import ArticleCell from 'src/components/ArticleCell'

interface Props 

const ArticlePage = (: Props) =>  />
    </>
  )
}

export default ArticlePage
```

`id` already exists since we named our route param ``. Thanks Redwood! But how does that `id` end up as the `$id` GraphQL parameter? If you\'ve learned anything about Redwood by now, you should know it\'s going to take care of that for you. By default, any props you give to a cell will automatically be turned into variables and given to the query. \"No way,\" you\'re saying. Way.

We can prove it! Try going to the detail page for a post in the browser and---uh oh. Hmm:

![Article error message](https://user-images.githubusercontent.com/300/146100555-cea8806a-70aa-43e5-b2b4-d49d84014c4e.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

This error message you\'re seeing is thanks to the `Failure` section of our Cell!

``` 
Error: Variable "$id" got invalid value "1"; Int cannot represent non-integer value: "1"
```

It turns out that route params are extracted as strings from the URL, but GraphQL wants an integer for the `id`. We could use `parseInt()` to convert it to a number before passing it into `ArticleCell`, but we can do better than that.

### Route Param Types[​](#route-param-types "Direct link to Route Param Types") 

What if you could request the conversion right in the route\'s path? Introducing **route param types**. It\'s as easy as adding `:Int` to our existing route param:

-   JavaScript
-   TypeScript

web/src/Routes.jsx

``` 
<Route path="/article/" page= name="article" />
```

web/src/Routes.tsx

``` 
<Route path="/article/" page= name="article" />
```

Voilà! Not only will this convert the `id` param to a number before passing it to your Page, it will prevent the route from matching unless the `id` path segment consists entirely of digits. If any non-digits are found, the router will keep trying other routes, eventually showing the `NotFoundPage` if no routes match.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]What if I want to pass some other prop to the cell that I don\'t need in the query, but do need in the Success/Loader/etc. components?

All of the props you give to the cell will be automatically available as props in the render components. Only the ones that match the GraphQL variables list will be given to the query. You get the best of both worlds! In our post display above, if you wanted to display some random number along with the post (for some contrived, tutorial-like reason), just pass that prop:

-   JavaScript
-   TypeScript

``` 
<ArticleCell id= rand= />
```

``` 
<ArticleCell id= rand= />
```

And get it, along with the query result (and even the original `id` if you want) in the component:

-   JavaScript
-   TypeScript

``` 
export const Success = () => 
```

``` 
interface Props
  extends CellSuccessProps<FindArticleQuery, FindArticleQueryVariables> 

export const Success = (: Props) => 
```

Thanks again, Redwood!

### Displaying a Blog Post[​](#displaying-a-blog-post "Direct link to Displaying a Blog Post") 

Now let\'s display the actual post instead of just dumping the query result. We could copy the display from the articles on the homepage, but that\'s not very reusable! This is the perfect place for a good old fashioned component---define the display once and then reuse the component on the homepage and the article display page. Both `ArticlesCell` and `ArticleCell` will display our new component. Let\'s Redwood-up a component (I just invented that phrase):

``` 
yarn rw g component Article
```

Which creates `web/src/components/Article/Article.tsx` (and corresponding test and more!) as a super simple React component:

-   JavaScript
-   TypeScript

web/src/components/Article/Article.jsx

``` 
const Article = () => </h2>
      <p></p>
    </div>
  )
}

export default Article
```

web/src/components/Article/Article.tsx

``` 
const Article = () => </h2>
      <p></p>
    </div>
  )
}

export default Article
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You may notice we don\'t have any explicit `import` statements for `React` itself. We (the Redwood dev team) got tired of constantly importing it over and over again in every file so we automatically import it for you!

Let\'s copy the `<article>` section from `ArticlesCell` and put it here instead, taking the `article` itself in as a prop:

-   JavaScript
-   TypeScript

web/src/components/Article/Article.jsx

``` 
import  from '@redwoodjs/router'

const Article = () => )}></Link>
        </h2>
      </header>
      <div></div>
      <div>Posted at: </div>
    </article>
  )
}

export default Article
```

web/src/components/Article/Article.tsx

``` 
import  from '@redwoodjs/router'

import type  from 'types/graphql'

interface Props 

const Article = (: Props) => )}></Link>
        </h2>
      </header>
      <div></div>
      <div>Posted at: </div>
    </article>
  )
}

export default Article
```

And update `ArticlesCell` to use this new component instead:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
import Article from 'src/components/Article'

export const QUERY = gql`
  query ArticlesQuery 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () =>  article= />
      ))}
    </>
  )
}
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

import Article from 'src/components/Article'

export const QUERY: TypedDocumentNode<ArticlesQuery, ArticlesQueryVariables> =
  gql`
    query ArticlesQuery 
    }
  `

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = (: CellFailureProps<ArticlesQueryVariables>) => (
  <div style=}>Error: </div>
)

export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) =>  article= />
      ))}
    </>
  )
}
```

Last but not least we can update the `ArticleCell` to properly display our blog posts as well:

-   JavaScript
-   TypeScript

web/src/components/ArticleCell/ArticleCell.jsx

``` 
import Article from 'src/components/Article'

export const QUERY = gql`
  query FindArticleQuery($id: Int!) 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () =>  />
}
```

web/src/components/ArticleCell/ArticleCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

import Article from 'src/components/Article'

export const QUERY: TypedDocumentNode<
  FindArticleQuery,
  FindArticleQueryVariables
> = gql`
  query FindArticleQuery($id: Int!) 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = (: CellFailureProps<FindArticleQueryVariables>) => (
  <div style=}>Error: </div>
)

export const Success = (: CellSuccessProps<FindArticleQuery, FindArticleQueryVariables>) =>  />
}
```

And there we go! We should be able to move back and forth between the homepage and the detail page. If you\'ve only got one blog post then the homepage and single-article page will be identical! Head to the posts admin and create a couple more, won\'t you?

![Article page showing an article](https://user-images.githubusercontent.com/300/146101296-f1d43812-45df-4f1e-a3da-4f6a085bfc08.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

If you like what you\'ve been seeing from the router, you can dive deeper into the [Redwood Router](/docs/router) guide.

### Summary[​](#summary "Direct link to Summary") 

To recap:

1.  We created a new page to show a single post (the \"detail\" page).
2.  We added a route to handle the `id` of the post and turn it into a route param, even coercing it into an integer.
3.  We created a cell to fetch and display the post.
4.  Redwood made the world a better place by making that `id` available to us at several key junctions in our code and even turning it into a number automatically.
5.  We turned the actual post display into a standard React component and used it in both the homepage and new detail page.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter2/routing-params.md)