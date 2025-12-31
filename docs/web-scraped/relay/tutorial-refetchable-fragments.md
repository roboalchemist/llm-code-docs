# Source: https://relay.dev/docs/tutorial/refetchable-fragments/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Refetchable Fragments]

[Version: v20.1.0]

On this page

<div>

# Refetchable Fragments

</div>

In this section, we\'ll look at how to fetch different data in response to user input.

-   We\'ll build a **filterable friends list**.
-   We\'ll see how to refetch only the necessary data, not an entire query.

------------------------------------------------------------------------

Since Relay encourages you to fetch all of your data in one big query, what happens when you need to refetch some data with different variables?

For example, suppose you were building a filterable list. You would need to fetch new search results when the search input changed.

One way to approach this would be to use a separate, secondary query to fetch the list, much like we did to fetch the hovercard earlier. Then we could change the query variables and refetch the query when the input changed.

However, this isn\'t optimal, because it needlessly uses a second query to fetch the *initial* list, before any user input occurs. The hovercard only appeared in response to a user interaction, but if the filterable list is visible and ready to be filtered, we might as well get its initial contents as part of our big query.

On the other hand, we don\'t want to refetch the *entire big query* whenever the input changes. Not only would this mean retrieving a large amount of data unnecessarily, it could disrupt other parts of the UI. If certain data unrelated to the filterable list has changed on the server, it would appear to randomly change when the query was refetched. Besides, this would mean threading the user input up to the top of the React tree where the query lives, which would not scale very well.

To address these issues, Relay provides *refetchable fragments*. These are fragments that can be refetched with new variables, separately from the rest of the query that they get spread into. They allow us to change a fragment's arguments and fetch new data for the new argument values, just as we can fetch an entire query with new query variables.

But fragments are just that, fragments --- they aren't queries and can't be fetched without being spread into a query and read out from the query results. So how do refetchable fragments actually work? The answer is that the Relay compiler generates a new, separate query just to refetch the fragment. The data is retrieved *initially* as part of whatever larger query the fragment is spread into, but then when it's refetched, the new synthetic query is used.

------------------------------------------------------------------------

To try this out, let\'s add a sidebar to the page with a filterable contacts list. After all, it wouldn\'t feel like a properly cozy newsfeed app without the ability to contact people.

We\'ve already prepared a `Sidebar` component, you just need to drop it into `App.tsx`:

``` 
import Sidebar from './Sidebar';

export default function App(): React.ReactElement >
        <div className="app">
          <Newsfeed />
          <Sidebar />
        </div>
      </React.Suspense>
    </RelayEnvironment>
  );
}
```

You should now see a sidebar with a list of people at the top.

![Contacts list](/assets/images/refetchable-contacts-initial-6f0b18fcbacc45a5673bbfd8a5a92a76.png)

Have a look at `ContactsList.tsx` and you'll find this fragment, which is what selects the list of contacts:

``` 
const ContactsListFragment = graphql`
  fragment ContactsListFragment on Viewer 
  }
`;
```

As it happens, the `contacts` field accepts a `search` argument that filters the list. You can try it out by changing `contacts` in this fragment to `contacts(search: "S")`. If you run `npm run relay` and refresh the page, you should see only those contacts that have the letter S in them.

Our goal, then, will be to hook up a search input so that, when the input changes, we refetch *just this fragment* with a new value for that `search` argument.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

As an optional exercise, try combining the queries of Sidebar and Newsfeed into a single query. There is no need for Sidebar to have its own query separate from Newsfeed; in a real app they would both have fragments and the *entire screen* would have only a single query. We built it with a separate query to simplify the early examples in the tutorial.

### Step 1 --- Add a fragment argument[​](#step-1--add-a-fragment-argument "Direct link to Step 1 — Add a fragment argument") 

First we need to make this fragment accept an argument. With refetchable fragments, fragment arguments become query variables for the refetch query that Relay generates. (They also work like regular fragment arguments, so the parent query can pass in an initial value for the argument.)

``` 
const ContactsListFragment = graphql`
  fragment ContactsListFragment on Viewer
    @argumentDefinitions(
      search: 
    )
  
  }
`;
```

### Step 2 --- Pass the fragment argument as a field argument[​](#step-2--pass-the-fragment-argument-as-a-field-argument "Direct link to Step 2 — Pass the fragment argument as a field argument") 

Pass the fragment argument in as an argument to the `contacts` field.

``` 
const ContactsListFragment = graphql`
  fragment ContactsListFragment on Viewer
    @argumentDefinitions(
      search: 
    )
  
  }
`;
```

Remember, the first `search` here is the name of the argument to `contacts`, while the second `$search` is the variable created by our fragment argument.

### Step 3 --- Add the \@refetchable directive[​](#step-3--add-the-refetchable-directive "Direct link to Step 3 — Add the @refetchable directive") 

Next we\'ll add a `@refetchable` directive. This tells Relay to generate the extra query for refetching it. You have to specify the name of the generated query --- it\'s a good idea to base it on the name of the fragment.

``` 
const ContactsListFragment = graphql`
  fragment ContactsListFragment on Viewer
    @refetchable(queryName: "ContactsListRefetchQuery")
    @argumentDefinitions(
      search: 
    )
  
`;
```

### Step 4 --- Add the search input[​](#step-4--add-the-search-input "Direct link to Step 4 — Add the search input") 

Now we need to actually hook this up to our UI. Take a look at the `ContactsList` component:

``` 
export default function ContactsList(: Props) >
      <h3>Contacts</h3>
       contact= />
      )}
    </Card>
  );
}
```

First we need to add a search field.

``` 
import SearchInput from './SearchInput';

const  = React;

function ContactsList() ;
  return (
    <Card dim=>
      <h3>Contacts</h3>
      <SearchInput
        value=
        onChange=
      />
       contact= />
      )}
    </Card>
  );
}
```

### Step 5 --- Call useRefetchableFragment[​](#step-5--call-userefetchablefragment "Direct link to Step 5 — Call useRefetchableFragment") 

Now to refetch the fragment when the string changes, we change `useFragment` to `useRefetchableFragment`. This hook returns a `refetch` function which will refetch the fragment with new variables which we provide as an argument.

``` 
import  from 'react-relay';

function ContactsList() );
  };
  return (
    // ...
  );
}
```

You'll notice that Relay gives us a callback for refetching, rather than accepting the new state variables as an argument to the hook and refetching when it is re-rendered with a different value. This means that the fetch begins as soon as the event takes place, saving some time versus waiting until React finishes re-rendering --- the same principle we saw before with preloaded queries. It also gives us more control, for example if we wanted to debounce the refetch.

### Step 6 --- Control loading with useTransition[​](#step-6--control-loading-with-usetransition "Direct link to Step 6 — Control loading with useTransition") 

At this point, when the fragment is refreshed, Relay uses Suspense while the new data is loading, so the entire component is replaced with a spinner! This makes the UI fairly unusable. We would rather just keep the current data on screen until the new data is available.

The way Suspense normally works is this: When a component is missing data that it needs to render (as our component does after we refetch), it tells React to wait. When this happens, React finds the nearest Suspense component in the tree. It then replaces everything under that component with a \"fallback\" loading indicator.

![Component needs data](/assets/images/refetchable-suspense-1-data-needed-05e9379009624a3afdac9e422da834e5.png) ![React finds the nearest Suspense point](/assets/images/refetechable-suspense-2-nearest-suspense-point-be5a2c65ed3a31ad3d32e1fb26c8c0b0.png) ![Renders a fallback at that point until the data is available](/assets/images/refetchable-suspense-3-fallback-d274cf296d7605ea275d4564cf529adf.png)

This makes sense when initially loading a screen, but in this instance there\'s no reason to hide the existing UI and replace it with a spinner. While React is waiting, it can simply continue showing what\'s already there.

To achieve this, we can mark the refetch as a *transition*. Transitions are React state updates that do not need to be immediately responded to --- React can wait until the data is available.

Transitions are marked by wrapping the state change in a call to a function provided by the `useTransition` hook. This is what the code will look like:

``` 
const  = React;

function ContactsList() );
    });
  };
  return (
    <Card dim=>
      <h3>Contacts</h3>
      <SearchInput
        value=
        onChange=
        isPending=
      />
       contact= />
      )}
    </Card>
  );
}
```

While React is waiting for the new data, instead of using a Suspense fallback, React re-renders the component with the `isPending` flag set to true.

We simply pass the `isPending` flag to `SearchInput` (which causes it to show a spinner) while the refetch is happening. Meanwhile, by placing `setSearchString` outside of the transition but `refetch` within it, we tell React to immediately update the search input.

We should now be able to search the contacts list with a nice user experience, showing a spinner but keeping the previous data visible while loading.

![Search input goes from spinner to filtered list](/assets/images/refetchable-transition-search-b916c9e6ffbb26b6e64c9f1e19fd6fd3.png)

Deep dive: What fragments can be refetched?

<div>

To refetch fragments, Relay has to know how to generate a query that lets it refetch just the information from the fragment. That's only possible for fragments that meet certain requirements.

You might imagine that we could, if nothing else, re-run the original query that the fragment was spread into. However, GraphQL doesn't guarantee that the same query will return the same results at different times. For instance, imagine you had a GraphQL field that returned the top trending posts across the site:

``` 
query MyQuery 
  }
}
```

If you wanted to refresh just `PosterFragment` from this query, it wouldn't work to construct a query like this:

``` 
query MyQuery 
  }
}
```

\... because the top trending post could be a different post by the time you refresh it!

Relay needs a way of identifying the specific node in the graph that the fragment ends up on, even if it can no longer be reached by the same path that the original query uses. If the node has a unique and stable ID, then we can just have a convention for querying for "the graph node with some specific ID" like so:

``` 
query RefetchQuery 
}
```

In fact, this is exactly the convention that Relay uses. It expects your server to implement a top-level field called `node` that takes an ID and gives you the graph node with that ID. (We saw `node` earlier with the hovercard example --- there it was used to fetch a specific person given their ID using a secondary query.)

Not every graph node has a stable ID --- some are ephemeral. To be used with `node`, your schema has to declare that its type implements an interface called `Node`:

``` 
type Person implements Node 
```

The `Node` interface simply says it has an ID, but more importantly indicates by convention that that ID is stable and unique:

``` 
interface Node 
```

Besides fragments on types that implement `Node`, you can also refetch fragments that are on `Viewer` (since the viewer is assumed to be stable throughout a session) and that are at the top level of a query (since there's no field above them that could change identity).

</div>

------------------------------------------------------------------------

## Summary[​](#summary "Direct link to Summary") 

Refetchable fragments let us efficiently update specific parts of the UI in response to user input, while initializing them as part of the same query that we use for the entire screen.

Relay\'s pagination features are built on refetchable fragments, too. We\'ll explore those next.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/tutorial/refetchable-fragments.md)