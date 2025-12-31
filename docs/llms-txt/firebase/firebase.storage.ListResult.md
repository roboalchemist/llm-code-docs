# Source: https://firebase.google.com/docs/reference/node/firebase.storage.ListResult.md.txt

# Source: https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListResult.md.txt

# ListResult | JavaScript SDK

# - [firebase](https://firebase.google.com/docs/reference/js/v8/firebase).
- [storage](https://firebase.google.com/docs/reference/js/v8/firebase.storage).
- ListResult

Result returned by list().

## Index

### Properties

- [items](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListResult#items)
- [nextPageToken](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListResult#nextpagetoken)
- [prefixes](https://firebase.google.com/docs/reference/js/v8/firebase.storage.ListResult#prefixes)

## Properties

### items

items: [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)\[\]  
Objects in this directory.
You can call getMetadata() and getDownloadUrl() on them.

### nextPageToken

nextPageToken: string \| null  
If set, there might be more results for this list. Use this token to resume the list.

### prefixes

prefixes: [Reference](https://firebase.google.com/docs/reference/js/v8/firebase.storage.Reference)\[\]  
References to prefixes (sub-folders). You can call list() on them to
get its contents.

Folders are implicit based on '/' in the object paths.
For example, if a bucket has two objects '/a/b/1' and '/a/b/2', list('/a')
will return '/a/b' as a prefix.