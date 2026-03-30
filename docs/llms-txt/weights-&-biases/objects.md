# Source: https://docs.wandb.ai/weave/guides/tracking/objects.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Track and version objects

> Track and version any JSON-serializable object in W&B Weave

## Objects

An **Object** is versioned, serializable data. Weave automatically versions objects when they change and creates an immutable history. Objects include:

* **Datasets**: Collections of examples for evaluation
* **Models**: Configurations and parameters for your LLM logic
* **Prompts**: Versioned prompt templates

```python lines theme={null}
dataset = weave.Dataset(
    name="test-cases",
    rows=[
        {"input": "What is 2+2?", "expected": "4"},
        {"input": "What is the capital of France?", "expected": "Paris"},
    ]
)
weave.publish(dataset)
```

## Publishing an object

Weave's serialization layer saves and versions objects.

<Tabs>
  <Tab title="Python">
    ```python lines theme={null}
    import weave
    # Initialize tracking to the project 'intro-example'
    weave.init('intro-example')
    # Save a list, giving it the name 'cat-names'
    weave.publish(['felix', 'jimbo', 'billie'], 'cat-names')
    ```
  </Tab>

  <Tab title="TypeScript">
    Publishing in TypeScript is still early, so not all objects are fully supported yet.

    ```typescript lines theme={null}
    import * as weave from 'weave'

    // Initialize tracking to the project 'intro-example'
    const client = await weave.init('intro-example')

    // Save an array, giving it the name 'cat-names'
    client.publish(['felix', 'jimbo', 'billie'], 'cat-names')
    ```
  </Tab>
</Tabs>

When you save an object with a name, Weave creates the first version of that object if it does not exist.

## Get an object back

<Tabs>
  <Tab title="Python">
    `weave.publish` returns a Ref. You can call `.get()` on any Ref to get the object back.

    You can construct a ref and then fetch the object back.

    ```python lines theme={null}
    weave.init('intro-example')
    cat_names = weave.ref('cat-names').get()
    ```
  </Tab>

  <Tab title="TypeScript">
    ```plaintext lines theme={null}
    This feature is not available in TypeScript yet.
    ```
  </Tab>
</Tabs>

## Delete an object

<Tabs>
  <Tab title="Python">
    To delete a version of an object, call `.delete()` on the object ref.

    ```python lines theme={null}
    weave.init('intro-example')
    cat_names_ref = weave.ref('cat-names:v1')
    cat_names_ref.delete()
    ```

    Accessing a deleted object returns an error. Resolving an object that has a reference to a deleted object returns a `DeletedRef` in place of the deleted object.
  </Tab>

  <Tab title="TypeScript">
    ```plaintext  theme={null}
    This feature is not available in TypeScript yet.
    ```
  </Tab>
</Tabs>

## Ref styles

A fully qualified Weave object ref URI looks like this:

```
weave://<entity>/<project>/object/<object_name>:<object_version>
```

* *entity*: wandb entity (username or team)
* *project*: wandb project
* *object\_name*: object name
* *object\_version*: either a version hash, a string like v0, v1..., or an alias like ":latest". All objects have the ":latest" alias.

You can construct refs with a few different styles.

* `weave.ref(<name>)`: requires `weave.init(<project>)` to have been called. Refers to the ":latest" version.
* `weave.ref(<name>:<version>)`: requires `weave.init(<project>)` to have been called.
* `weave.ref(<fully_qualified_ref_uri>)`: can be constructed without calling weave.init.
