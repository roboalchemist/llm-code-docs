# Source: https://developers.buffer.com/examples/create-image-post.md

Creating a post with an image works in the same way as creating a text post, with the addition of the imageUrl argument. This argument is used to specify the URL of the image that you want to include in the post.
```graphql
mutation CreatePost {
  createPost(input: {
    text: "Hello there, this is another one!",
    channelId: "some_channel_id",
    schedulingType: automatic,
    mode: customSchedule,
    dueAt: "2026-03-26T10:28:47.545Z"
    assets: {
      images:[
        {
          url:"https://images.unsplash.com/photo-1742850541164-8eb59ecb3282?q=80&w=3388&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
        }
      ]
    }
  }) {
    ... on PostActionSuccess {
      post {
        id
        text
        assets {
          id
          mimeType
        }
      }
    }
    ... on MutationError {
      message
    }
  }
}
```
