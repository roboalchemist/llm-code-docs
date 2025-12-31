# Source: https://relay.dev/docs/tutorial/arrays-lists/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Arrays and Lists]

[Version: v20.1.0]

On this page

<div>

# Arrays and Lists

</div>

So far we've only dealt with components that have a single instance of the components they're composed from. For example, we're only showing a single Newsfeed story, and within that story there's just a single author with a single profile picture. Let's look at how to handle more than one of something.

GraphQL includes support for arrays, which in GraphQL are called *lists.* A field can be not only a single scalar value but an array of them, or not only a single edge but an array of edges. The schema specifies whether each field is a list or not, but, oddly, the GraphQL query syntax doesn't distinguish between selecting a singular field and selecting a list --- a quirky exception to the design principle that a GraphQL response should have the same shape as the query.

Request:

``` 
query MyQuery 
  }
}
```

Response:

``` 
,
      
    ]
  }
}
```

As it happens, the schema in our example app has a `topStories` field that returns a list of Stories, as opposed to the `topStory` field we\'re currently using that returns just one.

To show multiple stories on our newsfeed, we just need to modify `Newsfeed.tsx` to use `topStories`.

### Step 1 --- Select a list in the fragment[​](#step-1--select-a-list-in-the-fragment "Direct link to Step 1 — Select a list in the fragment") 

Open `Newsfeed.tsx` and find `NewsfeedQuery`. Replace `topStory` with `topStories`, and run `npm run relay`.

``` 
const NewsfeedQuery = graphql`
  query NewsfeedQuery 
  }
`;
```

### Step 2 --- Map over the list in the component[​](#step-2--map-over-the-list-in-the-component "Direct link to Step 2 — Map over the list in the component") 

In the `Newsfeed` component, `data.topStories` will now be an array of fragment refs, each of which can be passed to a `Story` child component to render that story:

``` 
export default function Newsfeed() );
  const stories = data.topStories;
  return (
    <div className="newsfeed">
       />)}
    </div>
  );
}
```

### Step 3 --- Add a React key based on the node ID[​](#step-3--add-a-react-key-based-on-the-node-id "Direct link to Step 3 — Add a React key based on the node ID") 

At this point, you should see multiple stories on the screen! It\'s beginning to look like a proper newsfeed app.

![Multiple stories](/assets/images/arrays-top-stories-screenshot-ba4541cbe06c7d58e74097e07d065508.png)

However, we\'re also getting a React warning that we\'re rendering an array of components without [providing a key attribute](https://reactjs.org/docs/lists-and-keys.html).

![React missing key warning](/assets/images/arrays-keys-warning-screenshot-4e615af12bcb73307b06f9fcb09bf6e2.png)

It\'s always important to heed this warning, and more specifically to base keys on the identity of the things being displayed, rather than simply their indices in the array. This allows React to handle reordering and deleting items from the list correctly, since it knows which items are which even if their order changes.

Luckily, GraphQL nodes generally have IDs. We can simply select the `id` field of `story` and use it as a key:

``` 
const NewsfeedQuery = graphql`
  query NewsfeedQuery 
  }
`;

...

export default function Newsfeed() );
  const stories = data.topStories;
  return (
    <div className="newsfeed">
      
          story=
        />
      ))}
    </div>
  );
}
```

With that, we\'ve got a collection of Stories on the screen. It\'s worth pointing out that here we\'re mixing individual fields with fragment spreads in the same place in our query. This means that Newsfeed can read the fields it cares about (directly from `useLazyLoadQuery`) while Story can read the fields it cares about (via `useFragment`). The *same object* both contains Newsfeed\'s selected field `id` and is also a fragment key for `StoryFragment`.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

GraphQL Lists are only the most basic way of dealing with collections of things. We'll build on them to do pagination and infinite scrolling later in the tutorial, using a special system called Connections. You'll want to use Connections in most situations where you have a collection of items --- although you'll still use GraphQL Lists as a building block.

Onward!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/tutorial/arrays-lists.md)