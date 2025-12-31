# Source: https://firebase.google.com/docs/reference/node/firebase.storage.ListOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListOptions.md.txt

# Source: https://firebase.google.com/docs/reference/node/firebase.storage.ListOptions.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListOptions.md.txt

# ListOptions | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage).
- ListOptions

The options `list()` accepts.

## Index

### Properties

- [maxResults](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListOptions#maxresults)
- [pageToken](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListOptions#pagetoken)

## Properties

### Optional maxResults

maxResults: number \| null  
If set, limits the total number of `prefixes` and `items` to return.
The default and maximum maxResults is 1000.

### Optional pageToken

pageToken: string \| null  
The `nextPageToken` from a previous call to `list()`. If provided,
listing is resumed from the previous position.