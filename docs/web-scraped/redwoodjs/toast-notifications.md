# Source: https://docs.redwoodjs.com/docs/toast-notifications

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Toast Notifications]

[Version: 8.8]

On this page

<div>

# Toast Notifications

</div>

Did you know that those little popup notifications that you sometimes see at the top of a page after you\'ve performed an action are affectionately known as \"toast\" notifications? Because they pop up like a piece of toast from a toaster!

![Example toast animation](https://user-images.githubusercontent.com/300/110032806-71024680-7ced-11eb-8d69-7f462929815e.gif)

Redwood supports these notifications out of the box thanks to the [react-hot-toast](https://react-hot-toast.com/) package. We\'ll refer you to their [docs](https://react-hot-toast.com/docs) since they\'re very thorough, but here\'s enough to get you going.

### Add the `Toaster` Component[​](#add-the-toaster-component "Direct link to add-the-toaster-component") 

To render toast notifications, start by adding the `Toaster` component. It\'s usually better to add it at the App or Layout-level than the Page:

web/src/layouts/MainLayout/MainLayout.js

``` 
import  from '@redwoodjs/web/toast'

const MainLayout = () => </main>
    </>
  )
}

export default MainLayout
```

### Call the `toast` function[​](#call-the-toast-function "Direct link to call-the-toast-function") 

To render a basic toast notification with default styles, call the `toast` function:

web/src/layouts/MainLayout/MainLayout.js

``` 
import  from '@redwoodjs/web/toast'

// ...

const PostForm = () => ] = useMutation(CREATE_POST_MUTATION)

  const onSubmit = async (data) => })
      toast('Post created')
    }
    catch (e) 
  }

  return (
    // <Form onSubmit=> ... </Form>
  )
})

export default PostForm
```

### Call the `toast` variants[​](#call-the-toast-variants "Direct link to call-the-toast-variants") 

To render a toast notification with default icons and default styles, call the `toast` variants:

web/src/components/PostForm/PostForm.js

``` 
import  from '@redwoodjs/web/toast'

// ...

const PostForm = () => ] = useMutation(CREATE_POST_MUTATION, 
    onError: () => 
  })

  const onSubmit = (data) => })
  }

  return (
    // <Form onSubmit=> ... </Form>
  )
})

export default PostForm
```

or render an async toast by calling the `toast.promise` function:

web/src/components/PostForm/PostForm.js

``` 
import  from '@redwoodjs/web/toast'

// ...

const PostForm = () => ] = useMutation(CREATE_POST_MUTATION)

  const onSubmit = (data) => }), )
  }

  return (
    // <Form onSubmit=> ... </Form>
  )
})

export default PostForm
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]warning

You can\'t use the [onError](https://www.apollographql.com/docs/react/api/react/hooks/#onerror) callback in combination with the `toast.promise` function.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/toast-notifications.md)