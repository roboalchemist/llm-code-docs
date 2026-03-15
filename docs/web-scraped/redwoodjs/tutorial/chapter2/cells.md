# Source: https://docs.redwoodjs.com/docs/tutorial/chapter2/cells

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 2]
-   [Cells]

[Version: 8.8]

On this page

<div>

# Cells

</div>

The features we listed at the end of the last page (loading state, error messaging, blank slate text) are common in most web apps. We wanted to see if there was something we could do to make developers\' lives easier when it comes to adding them to a typical component. We think we\'ve come up with something to help. We call them *Cells*. Cells provide a simpler and more declarative approach to data fetching. ([Read the full documentation about Cells](/docs/cells).)

In addition to these states, cells are also responsible for their own data fetching. This means that rather than fetching data in some parent component and then passing props down to the child components that need them, a cell is completely self-contained and fetches and displays its own data! Let\'s add one to our blog to get a feel for how they work.

When you create a cell you export several specially named constants and then Redwood takes it from there. A typical cell may look something like:

-   JavaScript
-   TypeScript

``` 
export const QUERY = gql`
  query FindPosts 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>No posts yet!</div>

export const Failure = () => (
  <div>Error loading posts: </div>
)

export const Success = () => >
      <h2></h2>
      <div></div>
    </article>
  ))
}
```

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

export const QUERY: TypedDocumentNode<FindPosts, FindPostsVariables> = gql`
  query FindPosts 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>No posts yet!</div>

export const Failure = (: CellFailureProps<FindPostsVariables>) => (
  <div>Error loading posts: </div>
)

export const Success = (: CellSuccessProps<FindPosts, FindPostsVariables>) => >
      <h2></h2>
      <div></div>
    </article>
  ))
}
```

When React renders this component, Redwood will perform the `QUERY` and display the `Loading` component until a response is received.

Once the query returns, it will display one of three states:

-   If there was an error, the `Failure` component
-   If the data return is empty (`null` or empty array), the `Empty` component
-   Otherwise, the `Success` component

There are also some lifecycle helpers like `beforeQuery` (for manipulating any props before being given to the `QUERY`) and `afterQuery` (for manipulating the data returned from GraphQL but before being sent to the `Success` component).

The minimum you need for a cell are the `QUERY` and `Success` exports. If you don\'t export an `Empty` component, empty results will be sent to your `Success` component. If you don\'t provide a `Failure` component, you\'ll get error output sent to the console.

A guideline for when to use cells is if your component needs some data from the database or other service that may be delayed in responding. Let Redwood worry about juggling what is displayed when and you can focus on the happy path of the final, rendered component populated with data.

### Our First Cell[​](#our-first-cell "Direct link to Our First Cell") 

Usually in a blog the homepage will display a list of recent posts. This list is a perfect candidate for our first cell.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Wait, don\'t we already have a home page?

We do, but you will generally want to use a *cell* when you need data from the database. A best practice for Redwood is to create a Page for each unique URL your app has, but that you fetch and display data in Cells. So the existing HomePage will render this new cell as a child.

As you\'ll see repeatedly going forward, Redwood has a generator for this feature! Let\'s call this the \"Articles\" cell, since \"Posts\" was already used by our scaffold generator, and although the names won\'t clash (the scaffold files were created in the `Post` directory), it will be easier to keep them straight in our heads if the names are fairly different from each other. We\'re going to be showing multiple things, so we\'ll use the plural version \"Articles,\" rather than \"Article\":

``` 
yarn rw g cell Articles
```

This command will result in a new file at `/web/src/components/ArticlesCell/ArticlesCell.tsx` (and `test.tsx` `mock.ts` and `stories.tsx` files---more on those in [chapter 5 of the tutorial](/docs/tutorial/chapter5/storybook)!). This file will contain some boilerplate to get you started:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () => ></li>
      })}
    </ul>
  )
}
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

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

export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) => ></li>
      })}
    </ul>
  )
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]Indicating Multiplicity to the Cell Generator

When generating a cell you can use any case you\'d like and Redwood will do the right thing when it comes to naming. These will all create the same filename (`web/src/components/BlogArticlesCell/BlogArticlesCell.tsx`):

``` 
yarn rw g cell blog_articles
yarn rw g cell blog-articles
yarn rw g cell blogArticles
yarn rw g cell BlogArticles
```

You will need *some* kind of indication that you\'re using more than one word: either snake_case (`blog_articles`), kebab-case (`blog-articles`), camelCase (`blogArticles`) or PascalCase (`BlogArticles`).

Calling `yarn redwood g cell blogarticles` (without any indication that we\'re using two words) will generate a file at `web/src/components/BlogarticlesCell/BlogarticlesCell.tsx`.

To get you off and running as quickly as possible the generator assumes you\'ve got a root GraphQL query named the same thing as your cell and gives you the minimum query needed to get something out of the database. In this case the query is named `articles`:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
export const QUERY: TypedDocumentNode<ArticlesQuery, ArticlesQueryVariables> =
  gql`
    query ArticlesQuery 
    }
  `
```

However, this is not a valid query name for our existing Posts SDL (`api/src/graphql/posts.sdl.ts`) and Service (`api/src/services/posts/posts.ts`). (To see where these files come from, go back to the [Creating a Post Editor section](/docs/tutorial/chapter2/getting-dynamic#creating-a-post-editor) in the *Getting Dynamic* part.) Redwood names the query elements after the cell itself for convenience (more often than not you\'ll be creating a cell for a specific model), but in this case our cell name doesn\'t match our model name so we\'ll need to make some manual tweaks.

We\'ll have to rename them to `posts` in both the query name and in the prop name in `Success`:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () => ></li>
      })}
    </ul>
  )
}
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
import type  from 'types/graphql'

import type  from '@redwoodjs/web'

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

export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) => ></li>
      })}
    </ul>
  )
}
```

Let\'s plug this cell into our `HomePage` and see what happens:

-   JavaScript
-   TypeScript

web/src/pages/HomePage/HomePage.jsx

``` 
import  from '@redwoodjs/web'

import ArticlesCell from 'src/components/ArticlesCell'

const HomePage = () => 

export default HomePage
```

web/src/pages/HomePage/HomePage.tsx

``` 
import  from '@redwoodjs/web'

import ArticlesCell from 'src/components/ArticlesCell'

const HomePage = () => 

export default HomePage
```

The browser should actually show the `id` and a GraphQL-specific `__typename` properties for any posts in the database. If you just see \"Empty\" then return to the scaffold we created [last time](/docs/tutorial/chapter2/getting-dynamic#creating-a-post-editor) and add a couple. Neat!

![Showing articles in the database](https://user-images.githubusercontent.com/300/145910525-6a9814d1-0808-4f7e-aeab-303bd5dbac5e.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

**In the `Success` component, where did `posts` come from?**

In the `QUERY` statement, the query we\'re calling is `posts`. Whatever the name of this query is, that\'s the name of the prop that will be available in `Success` with your data.

-   JavaScript
-   TypeScript

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`
```

``` 
export const QUERY: TypedDocumentNode<ArticlesQuery, ArticlesQueryVariables> =
  gql`
    query ArticlesQuery 
    }
  `
```

You can also alias the name of the variable containing the result of the GraphQL query, and that will be the name of the prop:

-   JavaScript
-   TypeScript

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`
```

``` 
export const QUERY: TypedDocumentNode<ArticlesQuery, ArticlesQueryVariables> =
  gql`
    query ArticlesQuery 
    }
`
```

Now `articles` will be available in `Success` instead of `posts`:

-   JavaScript
-   TypeScript

``` 
export const Success = () => 
```

``` 
export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) => 
```

In fact, let\'s use the aforementioned alias so that the name of our cell, and the data we\'re iterating over, is consistent:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>Empty</div>

export const Failure = () => (
  <div style=}>Error: </div>
)

export const Success = () => ></li>
      })}
    </ul>
  )
}
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
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

export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) => ></li>
      })}
    </ul>
  )
}
```

In addition to the `id` that was added to the `query` by the generator, let\'s get the `title`, `body`, and `createdAt` values as well:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
export const QUERY = gql`
  query ArticlesQuery 
  }
`
```

web/src/components/ArticlesCell/ArticlesCell.tsx

``` 
export const QUERY: TypedDocumentNode<ArticlesQuery, ArticlesQueryVariables> =
  gql`
    query ArticlesQuery 
    }
`
```

The page should now show a dump of all the data you created for any blog posts you scaffolded:

![Articles with all DB values](https://user-images.githubusercontent.com/300/145911009-b83fd07f-0412-489c-a088-4e89faceea1c.png)

Now we\'re in the realm of good ol\' React components, so just build out the `Success` component to display the blog post in a nicer format:

-   JavaScript
-   TypeScript

web/src/components/ArticlesCell/ArticlesCell.jsx

``` 
export const Success = () => >
          <header>
            <h2></h2>
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
export const Success = (: CellSuccessProps<ArticlesQuery, ArticlesQueryVariables>) => >
          <header>
            <h2></h2>
          </header>
          <p></p>
          <div>Posted at: </div>
        </article>
      ))}
    </>
  )
}
```

And just like that we have a blog! It may be the most basic blog that ever graced the internet, but it\'s something! You can create/edit/delete posts and the world can view them on the homepage. (Don\'t worry, we\'ve got more features to add.)

![Nicely formatted blog articles](https://user-images.githubusercontent.com/300/145911342-b3a4bb44-e635-4bc5-8df7-a824661b2714.png)

### Summary[​](#summary "Direct link to Summary") 

To recap, what did we actually do to get this far?

1.  Generate the homepage
2.  Generate the blog layout
3.  Define the database schema
4.  Run migrations to update the database and create a table
5.  Scaffold a CRUD interface to the database table
6.  Create a cell to load the data and take care of loading/empty/failure/success states
7.  Add the cell to the page

The last few steps will become a standard lifecycle of new features as you build a Redwood app.

So far, other than a little HTML, we haven\'t had to do much by hand. And we especially didn\'t have to write a bunch of plumbing just to move data from one place to another. It makes web development a little more enjoyable, don\'t you think?

We\'re going to add some more features to our app, but first let\'s take a detour to learn about how Redwood accesses our database and what these SDL and services files are for.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter2/cells.md)