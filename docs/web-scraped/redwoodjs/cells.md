# Source: https://docs.redwoodjs.com/docs/cells

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Cells]

[Version: 8.8]

On this page

<div>

# Cells

</div>

Cells are a declarative approach to data fetching and one of Redwood\'s signature modes of abstraction. By providing conventions around data fetching, Redwood can get in between the request and the response to do things like query optimization and more, all without you ever having to change your code.

While it might seem like there\'s a lot of magic involved, all a Cell really does is execute a GraphQL query and manage its lifecycle. The idea is that, by exporting named constants that declare what you want your UI to look like throughout a query\'s lifecycle, Redwood can assemble these into a component template at build-time using a Babel plugin. All without you having to write a single line of imperative code!

## Generating a Cell[​](#generating-a-cell "Direct link to Generating a Cell") 

You can generate a Cell with Redwood\'s Cell generator:

``` 
yarn rw generate cell <name>
```

This creates a directory named `<name>Cell` in `web/src/components` with four files:

File

Description

`<name>Cell.js`

The actual Cell

`<name>Cell.test.js`

Jest tests for each state of the Cell

`<name>Cell.stories.js`

Storybook stories for each state of the Cell

`<name>Cell.mock.js`

Mock data for both the Jest tests and Storybook stories

### Single Item Cell vs List Cell[​](#single-item-cell-vs-list-cell "Direct link to Single Item Cell vs List Cell") 

Sometimes you want a Cell that renders a single item and other times you want a Cell that renders a list. Redwood\'s Cell generator can do both.

First, it detects if `<name>` is singular or plural. For example, to generate a Cell that renders a list of users, run `yarn rw generate cell users`. Second, for irregular words whose singular and plural are the same, such as \"equipment\" or \"pokemon\", you can pass `--list` to tell Redwood to generate a list Cell explicitly:

``` 
yarn rw generate cell equipment --list
```

## Cells in-depth[​](#cells-in-depth "Direct link to Cells in-depth") 

Cells exports five constants: `QUERY`, `Loading` , `Empty` , `Failure` and `Success`. The root query in `QUERY` is the same as `<name>` so that, if you\'re generating a cell based on a model in your `schema.prisma`, you can get something out of the database right away. But there\'s a good chance you won\'t generate your Cell this way, so if you need to, make sure to change the root query. See the [Cells](/docs/tutorial/chapter2/cells#our-first-cell) section of the Tutorial for a great example of this.

## Usage[​](#usage "Direct link to Usage") 

With Cells, you have a total of seven exports to work with:

Name

Type

Description

`QUERY`

`string,function`

The query to execute

`beforeQuery`

`function`

Lifecycle hook; prepares variables and options for the query

`isEmpty`

`function`

Lifecycle hook; decides if the Cell should render Empty

`afterQuery`

`function`

Lifecycle hook; sanitizes data returned from the query

`Loading`

`component`

If the request is in flight, render this component

`Empty`

`component`

If there\'s no data (`null` or `[]`), render this component

`Failure`

`component`

If something went wrong, render this component

`Success`

`component`

If the data has loaded, render this component

Only `QUERY` and `Success` are required. If you don\'t export `Empty`, empty results are sent to `Success`, and if you don\'t export `Failure`, error is output to the console.

In addition to displaying the right component at the right time, Cells also funnel the right props to the right component. `Loading`, `Empty`, `Failure`, and `Success` all have access to the props passed down from the Cell in good ol\' React fashion, and most of the `useQuery` hook\'s return as a prop called `queryResult`. In addition to all those props, `Empty` and `Success` also get the `data` returned from the query and an `updating` prop indicating whether the Cell is currently fetching new data. `Failure` also gets `updating` and exclusive access to `error` and `errorCode`.

We mentioned above that Cells receive \"most\" of what\'s returned from the `useQuery` hook. You can see exactly what `useQuery` returns in Apollo Client\'s [API reference](https://www.apollographql.com/docs/react/api/react/hooks/#result). Again note that `error` and `data` get some special treatment.

### QUERY[​](#query "Direct link to QUERY") 

`QUERY` can be a string or a function. If `QUERY` is a function, it has to return a valid GraphQL document.

It\'s more-than ok to have more than one root query. Here\'s an example:

``` 
export const QUERY = gql`
    authors 
  }
}
```

So in this case, both `posts` and `authors` would be available to `Success`:

``` 
export const Success = () => 
```

Normally queries have variables. Cells are setup to use any props they receive from their parent as variables (things are setup this way in `beforeQuery`). For example, here `BlogPostCell` takes a prop, `numberToShow`, so `numberToShow` is just available to your `QUERY`:

``` 
import BlogPostsCell from 'src/components/BlogPostsCell'

const HomePage = () =>  />
    </div>
  )
}

export default HomePage
```

``` 
export const QUERY = gql`
  query ($numberToShow: Int!) 
  }
`
```

This means you can think backwards about your Cell\'s props from your SDL: whatever the variables in your SDL are, that\'s what your Cell\'s props should be.

### beforeQuery[​](#beforequery "Direct link to beforeQuery") 

`beforeQuery` is a lifecycle hook. The best way to think about it is as a chance to configure [Apollo Client\'s `useQuery` hook](https://www.apollographql.com/docs/react/api/react/hooks#options).

By default, `beforeQuery` gives any props passed from the parent component to `QUERY` so that they\'re available as variables for it. It\'ll also set the fetch policy to `'cache-and-network'` since we felt it matched the behavior users want most of the time:

``` 
export const beforeQuery = (props) => 
}
```

For example, if you wanted to turn on Apollo\'s polling option, and prevent caching, you could export something like this (see Apollo\'s docs on [polling](https://www.apollographql.com/docs/react/data/queries/#polling) and [caching](https://www.apollographql.com/docs/react/data/queries/#setting-a-fetch-policy))

``` 
export const beforeQuery = (props) => 
}
```

You can also use `beforeQuery` to populate variables with data not included in the Cell\'s props (like from React\'s Context API or a global state management library). If you provide a `beforeQuery` function, the Cell will automatically change the type of its props to match the first argument of the function.

``` 
// The Cell will take no props: <Cell />
export const beforeQuery = () =>  = useAuth()

  return ,
  }
}
```

``` 
// The cell will take 1 prop named "word" that is a string: <Cell word="abc">
export const beforeQuery = (: ) => 
   }
}
```

### isEmpty[​](#isempty "Direct link to isEmpty") 

`isEmpty` is an optional lifecycle hook. It returns a boolean to indicate if the Cell should render empty. Use it to override the default check, which checks if the Cell\'s root fields are null or empty arrays.

It receives two parameters: 1) the `data`, and 2) an object that has the default `isEmpty` function, named `isDataEmpty`, so that you can extend the default:

``` 
export const isEmpty = (data, ) => 
```

### afterQuery[​](#afterquery "Direct link to afterQuery") 

`afterQuery` is a lifecycle hook. It runs just before data gets to `Success`. Use it to sanitize data returned from `QUERY` before it gets there.

By default, `afterQuery` just returns the data as it is:

### Loading[​](#loading "Direct link to Loading") 

If there\'s no cached data and the request is in flight, a Cell renders `Loading`.

When you\'re developing locally, you can catch your Cell waiting to hear back for a moment if set your speed in the Inspector\'s **Network** tab to something like \"Slow 3G\".

But why bother with Slow 3G when Redwood comes with Storybook? Storybook makes developing components like `Loading` (and `Failure`) a breeze. We don\'t have to put up with hacky workarounds like Slow 3G or intentionally breaking our app just to develop our components.

### Empty[​](#empty "Direct link to Empty") 

A Cell renders this component if there\'s no data. By no data, we mean if the response is 1) `null` or 2) an empty array (`[]`).

### Failure[​](#failure "Direct link to Failure") 

A Cell renders this component if something went wrong. You can quickly see this in action if you add an untyped field to your `QUERY`:

``` 
const QUERY = gql`
  query 
  }
`
```

But, like `Loading`, Storybook is probably a better place to develop this.

In this example, we use the `errorCode` to conditionally render the error heading title, and we also use it for our translation string.

``` 
export const Failure = (: CellFailureProps) =>  = useTranslation()
  return (
    <div style=}>
      
      Error:  - Code:  - `)}
    </div>
  )
}
```

### Success[​](#success "Direct link to Success") 

If everything went well, a Cell renders `Success`.

As mentioned, Success gets exclusive access to the `data` prop. But if you try to destructure it from `props`, you\'ll notice that it doesn\'t exist. This is because Redwood adds a layer of convenience: Redwood spreads `data` into `Success` so that you can just destructure whatever data you were expecting from your `QUERY` directly.

So, if you\'re querying for `posts` and `authors`, instead of doing:

``` 
export const Success = () =>  = data

  // ...
}
```

Redwood lets you do:

``` 
export const Success = () => 
```

Note that you can still pass any other props to `Success`. After all, it\'s just a React component.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Looking for info on how TypeScript works with Cells? Check out the [Utility Types](/docs/typescript/utility-types#cells) doc.

### When should I use a Cell?[​](#when-should-i-use-a-cell "Direct link to When should I use a Cell?") 

Whenever you want to fetch data. Let Redwood juggle what\'s displayed when. You just focus on what those things should look like.

While you can use a Cell whenever you want to fetch data, it\'s important to note that you don\'t have to. You can do anything you want! For example, for one-off queries, there\'s always `useApolloClient`. This hook returns the client, which you can use to execute queries, among other things:

``` 
// In a react component...

client = useApolloClient()

client.query()
```

### Can I Perform a Mutation in a Cell?[​](#can-i-perform-a-mutation-in-a-cell "Direct link to Can I Perform a Mutation in a Cell?") 

Absolutely. We do so in our [example todo app](https://github.com/redwoodjs/example-todo/blob/f29069c9dc89fa3734c6f99816442e14dc73dbf7/web/src/components/TodoListCell/TodoListCell.js#L26-L44). We also don\'t think it\'s an anti-pattern to do so. Far from it---your cells might end up containing a lot of logic and really serve as the hub of your app in many ways.

It\'s also important to remember that, besides exporting certain things with certain names, there aren\'t many rules around Cells---everything you can do in a regular component still goes.

## How Does Redwood Know a Cell is a Cell?[​](#how-does-redwood-know-a-cell-is-a-cell "Direct link to How Does Redwood Know a Cell is a Cell?") 

You just have to end a filename in \"Cell\" right? Well, while that\'s basically correct, there is one other thing you should know.

Redwood looks for all files ending in \"Cell\" (so if you want your component to be a Cell, its filename does have to end in \"Cell\"), but if the file 1) doesn\'t export a const named `QUERY` and 2) has a default export, then it\'ll be skipped.

When would you want to do this? If you just want a file to end in \"Cell\" for some reason. Otherwise, don\'t worry about it!

## Advanced Example: Implementing a Cell Yourself[​](#advanced-example-implementing-a-cell-yourself "Direct link to Advanced Example: Implementing a Cell Yourself") 

If we didn\'t do all that build-time stuff for you, how might you go about implementing a Cell yourself?

Consider the [example from the Tutorial](/docs/tutorial/chapter2/cells#our-first-cell) where we\'re fetching posts:

``` 
export const QUERY = gql`
  query 
  }
`

export const Loading = () => <div>Loading...</div>

export const Empty = () => <div>No posts yet!</div>

export const Failure = () => (
  <div>Error loading posts: </div>
)

export const Success = () => </h2>
      <div></div>
    </article>
  ))
}
```

And now let\'s say that Babel isn\'t going to come along and assemble our exports. What might we do?

We\'d probably do something like this:

``` 
const QUERY = gql`
  query 
  }
`

const Loading = () => <div>Loading...</div>

const Empty = () => <div>No posts yet!</div>

const Failure = () => (
  <div>Error loading posts: </div>
)

const Success = () => </h2>
      <div></div>
    </article>
  ))
}

const isEmpty = (data) => 

export const Cell = () => >
      ) =>  />
          } else 
        } else if (loading)  else if (data)  else  />
          }
        } else 
      }}
    </Query>
  )
}
```

That\'s a lot of code. A lot of imperative code too.

We\'re basically just dumping the contents of [createCell.tsx](https://github.com/redwoodjs/redwood/blob/main/packages/web/src/components/cell/createCell.tsx) into this file. Can you imagine having to do this every time you wanted to fetch data that might be delayed in responding? Yikes.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/cells.md)