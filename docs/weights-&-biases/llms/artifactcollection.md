# Source: https://docs.wandb.ai/models/ref/python/public-api/artifactcollection.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ArtifactCollection

export const GitHubLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="github-source-link">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
      <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z" />
    </svg>
    GitHub source
  </a>;

<GitHubLink url="https://github.com/wandb/wandb/blob/main/wandb/apis/public/artifacts.py" />

## <kbd>class</kbd> `ArtifactCollection`

An artifact collection that represents a group of related artifacts.

**Args:**

* `client`:  The client instance to use for querying W\&B.
* `entity`:  The entity (user or team) that owns the project.
* `project`:  The name of the project to query for artifact collections.
* `name`:  The name of the artifact collection.
* `type`:  The type of the artifact collection (e.g., "dataset", "model").
* `organization`:  Optional organization name if applicable.
* `attrs`:  Optional mapping of attributes to initialize the artifact collection.  If not provided, the object will load its attributes from W\&B upon  initialization.

### <kbd>property</kbd> ArtifactCollection.aliases

The aliases for all artifact versions contained in this collection.

**Returns:**

* `list[str]`: The aliases property value.

***

### <kbd>property</kbd> ArtifactCollection.created\_at

The creation date of the artifact collection.

**Returns:**

* `str`: The created\_at property value.

***

### <kbd>property</kbd> ArtifactCollection.description

A description of the artifact collection.

**Returns:**

* `str | None`: The description property value.

***

### <kbd>property</kbd> ArtifactCollection.entity

The entity (user or team) that owns the project.

**Returns:**

* `str`: The entity property value.

***

### <kbd>property</kbd> ArtifactCollection.id

The unique identifier of the artifact collection.

**Returns:**

* `str`: The id property value.

***

### <kbd>property</kbd> ArtifactCollection.name

The name of the artifact collection.

**Returns:**

* `str`: The name property value.

***

### <kbd>property</kbd> ArtifactCollection.project

The project that contains the artifact collection.

**Returns:**

* `str`: The project property value.

***

### <kbd>property</kbd> ArtifactCollection.tags

The tags associated with the artifact collection.

**Returns:**

* `list[str]`: The tags property value.

***

### <kbd>property</kbd> ArtifactCollection.type

Returns the type of the artifact collection.

***

### <kbd>property</kbd> ArtifactCollection.updated\_at

The date at which the artifact collection was last updated.

**Returns:**

* `str | None`: The updated\_at property value.

***

### <kbd>method</kbd> `ArtifactCollection.artifacts`

```python  theme={null}
artifacts(per_page: 'int' = 50) → Artifacts
```

Get all artifacts in the collection.

***

### <kbd>method</kbd> `ArtifactCollection.change_type`

```python  theme={null}
change_type(new_type: 'str') → None
```

Deprecated, change type directly with `save` instead.

***

### <kbd>method</kbd> `ArtifactCollection.delete`

```python  theme={null}
delete() → None
```

Delete the entire artifact collection.

***

### <kbd>method</kbd> `ArtifactCollection.is_sequence`

```python  theme={null}
is_sequence() → bool
```

Return whether the artifact collection is a sequence.

***

### <kbd>method</kbd> `ArtifactCollection.save`

```python  theme={null}
save() → None
```

Persist any changes made to the artifact collection.
