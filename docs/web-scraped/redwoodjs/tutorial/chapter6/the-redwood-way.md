# Source: https://docs.redwoodjs.com/docs/tutorial/chapter6/the-redwood-way

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Tutorial]
-   [Chapter 6]
-   [Building a Component the Redwood Way]

[Version: 8.8]

On this page

<div>

# Building a Component the Redwood Way

</div>

What\'s our blog missing? Comments. Let\'s add a simple comment engine so people can leave their completely rational, well-reasoned comments on our blog posts. It\'s the internet, what could go wrong?

There are two main features we need to build:

1.  Comment form and creation
2.  Comment retrieval and display

Which order we build them in is up to us. To ease into things, let\'s start with the fetching and displaying comments first and then we\'ll move on to more complex work of adding a form and service to create a new comment. Of course, this is Redwood, so even forms and services aren\'t *that* complex!

### Storybook[​](#storybook "Direct link to Storybook") 

Let\'s create a component for the display of a single comment. First up, the generator:

``` 
yarn rw g component Comment
```

Storybook should refresh and our \"Generated\" Comment story will be ready to go:

![image](https://user-images.githubusercontent.com/300/153475744-2e3151f9-b39c-4823-b2ef-539513cd4005.png)

Let\'s think about what we want to ask users for and then display in a comment. How about just their name and the content of the comment itself? And we\'ll throw in the date/time it was created. Let\'s update the **Comment** component to accept a `comment` object with those three properties:

-   JavaScript
-   TypeScript

web/src/components/Comment/Comment.jsx

``` 
const Comment = () => </h2>
      <time dateTime=></time>
      <p></p>
    </div>
  )
}

export default Comment
```

web/src/components/Comment/Comment.tsx

``` 
// Just a temporary type. We'll replace this later
interface Props 
}

const Comment = (: Props) => </h2>
      <time dateTime=></time>
      <p></p>
    </div>
  )
}

export default Comment
```

Once you save that file and Storybook reloads you\'ll see it blow up:

![image](https://user-images.githubusercontent.com/300/153475904-8f53cb09-3798-4e5a-9b6a-1ff1df98f93f.png)

We need to update the story to include that comment object and pass it as a prop:

-   JavaScript
-   TypeScript

web/src/components/Comment/Comment.stories.jsx

``` 
import Comment from './Comment'

export const generated = () => }
    />
  )
}

export default 
```

web/src/components/Comment/Comment.stories.tsx

``` 
import Comment from './Comment'

export const generated = () => }
    />
  )
}

export default 
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

Datetimes will come from GraphQL in [ISO8601 format](https://en.wikipedia.org/wiki/ISO_8601#Times) so we need to return one in that format here.

Storybook will reload and be much happier:

![image](https://user-images.githubusercontent.com/300/153476049-8ac31858-3014-47b5-807c-02b32d5a3ab0.png)

Let\'s add a little bit of styling and date conversion to get this **Comment** component looking like a nice, completed design element:

-   JavaScript
-   TypeScript

web/src/components/Comment/Comment.jsx

``` 
const formattedDate = (datetime) => )
  return `$ $ $`
}

const Comment = () => </h2>
        <time className="text-xs text-gray-500" dateTime=>
          
        </time>
      </header>
      <p className="text-sm mt-2"></p>
    </div>
  )
}

export default Comment
```

web/src/components/Comment/Comment.tsx

``` 
const formattedDate = (datetime: ConstructorParameters<typeof Date>[0]) => )
  return `$ $ $`
}

// Just a temporary type. We'll replace this later
interface Props 
}

const Comment = (: Props) => </h2>
        <time className="text-xs text-gray-500" dateTime=>
          
        </time>
      </header>
      <p className="text-sm mt-2"></p>
    </div>
  )
}

export default Comment
```

![image](https://user-images.githubusercontent.com/300/153476305-017c6cf8-a2dd-4da0-a6ef-487d91a562df.png)

Our component looks great! Now let\'s verify that it does what we want it to do with a test.

### Testing[​](#testing "Direct link to Testing") 

We don\'t want Santa to skip our house so let\'s test our **Comment** component. We could test that the author\'s name and the body of the comment appear, as well as the date it was posted.

The default test that comes with a generated component just makes sure that no errors are thrown, which is the least we could ask of our components!

Let\'s add a sample comment to the test and check that the various parts are being rendered:

-   JavaScript
-   TypeScript

web/src/components/Comment.test.jsx

``` 
import  from '@redwoodjs/testing'

import Comment from './Comment'

describe('Comment', () => 
    render(<Comment comment= />)

    expect(screen.getByText(comment.name)).toBeInTheDocument()
    expect(screen.getByText(comment.body)).toBeInTheDocument()
    const dateExpect = screen.getByText('2 January 2020')
    expect(dateExpect).toBeInTheDocument()
    expect(dateExpect.nodeName).toEqual('TIME')
    expect(dateExpect).toHaveAttribute('datetime', comment.createdAt)
  })
})
```

web/src/components/Comment.test.tsx

``` 
import  from '@redwoodjs/testing'

import Comment from './Comment'

describe('Comment', () => 
    render(<Comment comment= />)

    expect(screen.getByText(comment.name)).toBeInTheDocument()
    expect(screen.getByText(comment.body)).toBeInTheDocument()
    const dateExpect = screen.getByText('2 January 2020')
    expect(dateExpect).toBeInTheDocument()
    expect(dateExpect.nodeName).toEqual('TIME')
    expect(dateExpect).toHaveAttribute('datetime', comment.createdAt)
  })
})
```

Here we\'re testing for both elements of the output `createdAt` timestamp: the actual text that\'s output (similar to how we tested for an article\'s truncated body) but also that the element that wraps that text is a `<time>` tag and that it contains a `datetime` attribute with the raw value of `comment.createdAt`. This might seem like overkill but the point of the `datetime` attribute is to provide a machine-readable timestamp that the browser could (theoretically) hook into and do stuff with. This makes sure that we preserve that ability.

If your tests aren\'t already running in another terminal window, you can start them now:

``` 
yarn rw test
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]What happens if we change the formatted output of the timestamp? Wouldn\'t we have to change the test?

Yes, just like we\'d have to change the truncation text if we changed the length of the truncation. One alternative approach to testing for the formatted output could be to move the date formatting formula into a function that you can export from the `Comment` component. Then you can import that in your test and use it to check the formatted output. Now if you change the formula the test keeps passing because it\'s sharing the function with `Comment`.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/tutorial/chapter6/the-redwood-way.md)