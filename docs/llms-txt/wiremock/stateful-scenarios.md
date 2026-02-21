# Source: https://docs.wiremock.io/dynamic-state/stateful-scenarios.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Stateful Mocking and Scenarios

> Return different responses based on a state machine

Some testing activities require that different responses be served for a sequence of identical requests. For instance if you are testing a to-do list application [such as this one](../samples/exploratory-testing-tutorial/) you may wish to start with no to-do list items, post a new item, then see the item appear in the list.

Assuming there is a "list to-do items" API call used to fetch the list, this must be called twice during the above test, returning no items on the first invocation, and the newly added item on the second. Since both of these requests will be identical (same URL, method, request headers), something additional is required for WireMock Cloud to differentiate the first and
second cases.

WireMock Cloud's Scenarios solve this problem by providing finite state machines that can be used as additional stub matching conditions.

They allow more than one definition of an otherwise identical stub with different responses based on the current state of the machine.

## Stateful mocking vs. Scenarios

WireMock Cloud provides scenarios as a way to create advanced, pre-defined testing conditions. Alternatively, you can use our [dynamic states feature](../dynamic-state/overview) for truly stateful mocking that allows you to define operations and context to use in dynamic test sessions concurrently.

## Example

To implement the above case, you would declare that the stub returning the empty list is only matched when the scenario state is "Started",
while the stub returning the list with one item is only matched when the scenario state is "First item added".

Start by creating the empty list stub, which is matched only when the scenario named "To do list" is in the "Started" state:

<img title="Empty to-do list stub" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=1f57f39fbd52d23553fe4ef5fb1f4559" data-og-width="836" width="836" data-og-height="1001" height="1001" data-path="images/screenshots/scenarios-empty-list-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=9021a3e6582d553b53c96b585d1e1992 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=a279aebee5d872b795826460758d18bc 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=ac13a55b2f5c25542c45a3d03d761545 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=0c0ac0874660afecfbeeac7c5fd6bc7f 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=308ac12818fa516eb7313310e06ba7c0 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-empty-list-stub.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=64b440e667cd4a22254d80f4998ce531 2500w" />

Then create a stub to handle posting of the first list item. When triggered this stub will move the scenario state to "First item added":

<img title="To-do list POST stub" src="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=113248b5685262b82a49873ff6927ace" data-og-width="822" width="822" data-og-height="969" height="969" data-path="images/screenshots/scenarios-post-item-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?w=280&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=3b4728bc38f096d0a454d38c0318af61 280w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?w=560&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=d084d948616b5339bd592133cd44a889 560w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?w=840&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=5916945c36ab3f3ce3c3475840655080 840w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?w=1100&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=03fd9d8d5bccbc3ac8bf1a9f4d12af38 1100w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?w=1650&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=16bba92b4ddd7b251667d4b1366e0c7b 1650w, https://mintcdn.com/wiremockinc/0mURIwCv-YEN_f3M/images/screenshots/scenarios-post-item-stub.png?w=2500&fit=max&auto=format&n=0mURIwCv-YEN_f3M&q=85&s=2cec5c981630d1fe22ee74217c3c922e 2500w" />

Finally, create a stub to return the list containing one item, which is matched only when the scenario is in the "First item added" state:

<img title="Single item to-do list stub" src="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=b05b34b71cee681da4bc0602d7b3c6df" data-og-width="833" width="833" data-og-height="957" height="957" data-path="images/screenshots/scenario-single-item-stub.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?w=280&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=98937e79cd1c67207ea11ca28a1b3a94 280w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?w=560&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=374e8d1eb7e47df7155bd8e99d3e3f8a 560w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?w=840&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=e1163a244a5851a208cb9e5fdc8e548d 840w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?w=1100&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=22da36619b0d819217f6b91e0f30b3cf 1100w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?w=1650&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=ed81462382c9ae5d9d37209c6c60c686 1650w, https://mintcdn.com/wiremockinc/EDBJX-5Afnmcqt0d/images/screenshots/scenario-single-item-stub.png?w=2500&fit=max&auto=format&n=EDBJX-5Afnmcqt0d&q=85&s=3ef19b4212478abc62cd0ec9aa3de58e 2500w" />

## Testing

First, make a `GET` request to fetch the list, which should be empty. You should be able to do this any number of times
without the result changing:

```
$ curl http://example.wiremockapi.cloud/todo-items
{
  "items": []
}
```

Now `POST` a new item (it actually doesn't matter what the request body contains, since we didn't specify a body matcher in the stub):

```
$ curl http://example.wiremockapi.cloud/todo-items -X POST
```

This should now have moved the scenario state to "First item added". Getting the list of items again should now return one item:

```
$ curl http://example.wiremockapi.cloud/todo-items
{
  "items": [
    {
      "id": "1",
      "description": "Read all about Scenarios"
    }
  ]
}
```

## Scenario reset

All scenarios can be reset to their "Started" state by clicking Reset.
