# Source: https://virustotal.readme.io/reference/comment-object.md

# Comments

comment object

Comments

## Object Attributes

* `attributes`: data about a specific comment.
  * `date`:  <*integer*> when the comment was done.
  * `text`:  <*string*> comment in text.
  * `html`:  <*string*> comment in html format.
  * `votes`: <*dictionary*> unweighted number of total votes from the community, divided in "harmless" and "malicious".
    * `positive`: <*integer*> number of positive votes.
    * `negative`: <*integer*> number of negative votes.
    * `abuse`: <*integer*> number of negative votes.
  * `tags`: <*list of strings*> identificative attributes.
* `id`:  <*string*> resource identifier of the comment.
* `links`: contains "self", with a link to the comment itself.
* `type`:  <*string*> value is "comment", that is the object type.

```json "vote" object
{
  "attributes": {"date": <int:timestamp>,
                 "text": <string>,
                 "html": "<string>",
                 "votes": {
                    "positive": <int>,
                    "negative": <int>,
                    "abuse": <int>
                 },
                 "tags": ["<string>"],
                 },
  "id": "<string>",
  "links": {"self": "<string>"},
  "type": "vote"
}
```

## Relationships

In addition to the previously described attributes, Comment objects contain relationships with other objects in our dataset that can be retrieved as explained in the [Relationships](https://virustotal.readme.io/reference/relationships) section. The available relationships are described in the following table:

| Relationship | Description            | Accessibility | Return object type               |
| :----------- | :--------------------- | :------------ | :------------------------------- |
| author       | Author of the comment. | Everyone.     | Details of the comment's author. |