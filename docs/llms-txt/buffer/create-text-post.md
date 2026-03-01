# Source: https://developers.buffer.com/examples/create-text-post.md

Text posts can be created using the createPost mutation. When creating a post, there are several required arguments:

- The channel ID that the post is being created for

- The scheduling type to be used for the post (automatic or notification)

- The sharing mode to be used for the post (add the post to the queue, share it now or share it next)

- The text to be used when creating the Post

When performing the mutation, the PostActionSuccess type can be used to retrieve the information for the Post that was created. Similarly, the MutationError will provide you with information on the error that was triggered when trying to create the post.

```graphql
mutation CreatePost {
  createPost(input: {
    text: "Hello there, this is another one!",
    channelId: "some_channel_id",
    schedulingType: automatic,
    mode: customSchedule,
    dueAt: "2026-03-26T10:28:47.545Z"
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
