# Source: https://virustotal.readme.io/reference/saved-search-object.md

# Saved Searches

Saved Searches are designed to store complex or frequently executed threat intelligence searches for reuse against our database of Indicators of Compromise (IoCs).

## Object Attributes

A saved search object contains the following attributes:

* `creation_date`: <*int:timestamp*> saved search object creation date (UTC timestamp).
* `last_modification_date`: <*int:timestamp*> last time when the saved search's information was updated (UTC timestamp).
* `last_execution_date`: <*int:timestamp*> last time the saved search was run (UTC timestamp or 0).
* `name`: <*string*> saved search's name.
* `description`: <*string*> saved search's description.
* `search_query`: <*string*> saved search's query/logic.
* `private`: <*boolean*> whether the saved search is private or not.
* `origin`: <*string*> saved search's origin. Available options are: Crowdsourced and Partner.
* `tags`: <*list of strings*> saved search's associated tags.

The `context_attributes` define the specific relationship between the user who requested the object and the object itself.

```json Saved Search object
{
    "attributes": {
        "creation_date": <_int:timestamp_>,
        "description": "<_string_>",
        "last_execution_date": \<_int:timestamp_>,
        "last_modification_date": \<_int:timestamp_>,
        "name": "<_string_>",
        "origin": "<_string_>",
        "private": <_boolean_>,
        "search_query": "<_string_>",
        "tags": <_list of strings_>
    },
    "context_attributes": {
        "role": "<_string_>",
        "shared_with_me": <_boolean_>
    },
    "id": "<_string_>",
    "links": {
        "self": "https://www.virustotal.com/api/v3/saved_searches/<_string_>"
    },
    "type": "saved_search"
}
```

# Relationships

In addition to the previously described attributes, Saved Searches objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/introduction-relationships) section.

The following table shows a summary of available relationships.

| Relationship | Return object type                                                                                               | Allowed Methods |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | --------------- |
| owner        | [User](https://virustotal.readme.io/reference/user-object)  who created the object.                                                                 | GET             |
| editors      | List of [users](https://virustotal.readme.io/reference/user-object) that can edit the object (only available to the owner or editor of the object). | GET, POST       |
| viewers      | List of [users](https://virustotal.readme.io/reference/user-object) that can view the object (only available to the owner or editor of the object). | GET, POST       |