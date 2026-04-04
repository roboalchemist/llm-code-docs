# Source: https://relay.dev/docs/tutorial/interfaces-polymorphism/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Interfaces & Polymorphism]

[Version: v20.1.0]

On this page

<div>

# GraphQL Types, Interfaces, and Polymorphism

</div>

In this section, we'll see how to treat different types of nodes differently. You might notice that some of the newsfeed stories in the example app are posted by people, while others are posted by organizations. In this example, we\'ll enhance our hovercard by writing a fragment that selects people-specific information about people and organization-specific information about organizations.

------------------------------------------------------------------------

We've alluded to the fact that GraphQL nodes aren't just random bags of fields --- they have types. Your GraphQL schema defines what fields each type has. For instance, it might define the `Story` type like this:

``` 
type Story 
```

Here, some of the fields are scalars (like `String` and `ID`). Others are types defined elsewhere in the schema, like `Image` --- these fields are edges to nodes of those specific types. The `!` on `ID!` means that field is non-nullable. In GraphQL, fields are normally nullable and non-nullability is the exception.

Fragments are always "on" a particular type. In our example above, `StoryFragment` is defined `on Story`. This means that you can only spread it into places in a query where a `Story` node is expected. And it means that the fragment can select just those fields that exist on the `Story` type.

Of particular interest is the `Actor` type used for the `poster` field. This type is an *interface*. That means that the `poster` of a story can be a Person, a Page, an Organization, or any other type of entity that meets the specifications for being an "Actor".

The GraphQL schema in our example app defines an Actor as follows:

``` 
interface Actor 
```

Not coincidentally this is exactly the information that we're displaying here. There are two types in the schema that *implement* Actor, meaning that they include all the fields defined in Actor. They are declared as such:

``` 
type Person implements Actor 

type Organization implements Actor 
```

Both of these types have `name` , `profilePicture`, and `joined`, so they can both declare that they implement Actor and thus can be used wherever an Actor is called for in the schema and in fragments. They also have other fields that are distinct to each particular type.

Let's see how to work with interfaces more by extending the `PosterDetailsHovercardContentsBody` component to display the location of a `Person` or the organization kind of an `Organization`. These are fields that are only present on those specific types, not on the `Actor` interface.

Right now, if you've followed along so far, it should have a fragment defined like this (in `PosterDetailsHovercardContents.tsx`):

``` 
fragment PosterDetailsHovercardContentsBodyFragment on Actor 
}
```

If you try to add a field like `organizationKind` to this fragment, you'll get an error from the Relay compiler:

``` 
✖︎ The type `Actor` has no field organizationKind
```

This is because when we define a fragment as being on an interface, we can only use fields from that interface. To use fields from a specific type that implements the interface, we use a *type refinement* to tell GraphQL we're selecting fields from that type:

``` 
fragment PosterDetailsHovercardContentsBodyFragment on Actor 
  ... on Organization 
}
```

Go ahead and add this now. You can also add a type refinement for `Person`:

``` 
fragment PosterDetailsHovercardContentsBodyFragment on Actor 
  ... on Organization 
  ... on Person 
  }
}
```

When you select a field that's only present on some of the types that implement an interface, and the node you're dealing with is of a different type, then you simply get `null` for the value of that field when you read it out. With that in mind, we can modify the `PosterDetailsHovercardContentsBody` component to show the location of people and organization kind of organizations:

``` 
import OrganizationKind from './OrganizationKind';

function PosterDetailsHovercardContentsBody(: Props): React.ReactElement  width= height= className="posterHovercard__image" />
      <div className="posterHovercard__name"></div>
      <ul className="posterHovercard__details">
         <li>Joined <Timestamp time= /></li>
         </li>
         )}
         /></li>
         )}
      </ul>
    </>
  );
}
```

You should now see the location of people, and the organization kind for organizations:

![An organization hovercard](/assets/images/interfaces-organization-screenshot-3614512165c0726ffd8c8b5e30a8ee6a.png) ![A person hovercard](/assets/images/interfaces-person-screenshot-4926f665a489443785ec6223110fe725.png)

By the way, we can now understand why we had `... on Actor` in the example earlier. The `node` field can return a node of any type because any ID could be given at runtime. So the type that it gives us is `Node`, a very generic interface that can be implemented by anything that has an `id` field. We needed a type refinement to use fields from the `Actor` interface.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

In the GraphQL spec and other sources, type refinements are called *inline fragments*. We call them "type refinements" instead because this terminology is more descriptive and less confusing.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

If you need to do something totally different depending on what type it is, you can select a field called `__typename`, which returns a string with the name of the concrete type that you got (e.g., `"Person"` or `"Organization"`). This is a built-in feature of GraphQL.

## Summary[​](#summary "Direct link to Summary") 

The `... on Type ` syntax allows us to select fields that are only present in a specific type that implements an interface.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/tutorial/interfaces-polymorphism.md)