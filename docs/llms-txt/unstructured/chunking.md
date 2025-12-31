# Source: https://docs.unstructured.io/ui/chunking.md

# Source: https://docs.unstructured.io/open-source/core-functionality/chunking.md

# Source: https://docs.unstructured.io/open-source/best-practices/chunking.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/chunking.md

# Source: https://docs.unstructured.io/ui/chunking.md

# Source: https://docs.unstructured.io/open-source/core-functionality/chunking.md

# Source: https://docs.unstructured.io/open-source/best-practices/chunking.md

# Source: https://docs.unstructured.io/api-reference/legacy-api/partition/chunking.md

# Source: https://docs.unstructured.io/ui/chunking.md

# Source: https://docs.unstructured.io/open-source/core-functionality/chunking.md

# Source: https://docs.unstructured.io/open-source/best-practices/chunking.md

# Source: https://docs.unstructured.io/api-reference/partition/chunking.md

# Chunking strategies

Chunking functions use metadata and document elements detected with partition functions to split a document into
appropriately-sized chunks for uses cases such as retrieval-augmented generation (RAG).

If you are familiar with chunking methods that split long text documents into smaller chunks, you'll notice that
Unstructured methods slightly differ, since the partitioning step already divides an entire document into its structural elements.

Individual elements will only be split if they exceed the desired maximum chunk size. Two or more consecutive text elements
that will together fit within `max_characters` will be combined. After chunking, you will only have elements of the
following types:

* `CompositeElement`: Any text element will become a `CompositeElement` after chunking. A composite element can be a
  combination of two or more original text elements that together fit within the maximum chunk size. It can also be a single
  element that doesn't leave room in the chunk for any others but fits by itself. Or it can be a fragment of an original
  text element that was too big to fit in one chunk and required splitting.
* `Table`:  A table element is not combined with other elements and if it fits within `max_characters` it will remain as is.
* `TableChunk`: large tables that exceed `max_characters` chunk size are split into special `TableChunk` elements.

### "basic" chunking strategy

* The basic strategy combines sequential elements to maximally fill each chunk while respecting both the specified `max_characters` (hard-max) and `new_after_n_chars` (soft-max) option values.

* A single element that by itself exceeds the hard-max is isolated (never combined with another element) and then divided into two or more chunks using text-splitting.

* A `Table` element is always isolated and never combined with another element. A `Table` can be oversized, like any other text element, and in that case is divided into two or more `TableChunk` elements using text-splitting.

* If specified, `overlap` is applied between chunks formed by splitting oversized elements and is also applied between other chunks when `overlap_all` is `True`.

### "by\_title" chunking strategy

The `by_title` chunking strategy preserves section boundaries and optionally page boundaries as well. “Preserving” here means that a single chunk will never contain text that occurred in two different sections. When a new section starts, the existing chunk is closed and a new one started, even if the next element would fit in the prior chunk.

In addition to the behaviors of the `basic` strategy above, the `by_title` strategy has the following behaviors:

* **Detect section headings.** A `Title` element is considered to start a new section. When a `Title` element is encountered, the prior chunk is closed and a new chunk started, even if the `Title` element would fit in the prior chunk.

* **Respect page boundaries.** Page boundaries can optionally also be respected using the `multipage_sections` argument. This defaults to `True` meaning that a page break does *not* start a new chunk. Setting this to `False` will separate elements that occur on different pages into distinct chunks.

* **Combine small sections.** In certain documents, partitioning may identify a list-item or other short paragraph as a `Title` element even though it does not serve as a section heading. This can produce chunks substantially smaller than desired. This behavior can be mitigated using the `combine_text_under_n_chars` argument. This defaults to the same value as `max_characters` such that sequential small sections are combined to maximally fill the chunking window. Setting this to `0` will disable section combining.

### "by\_page" chunking strategy

Only available in the Unstructured UI and API.

The `by_page` chunking strategy ensures the content from different pages do not end up in the same chunk.
When a new page is detected, the existing chunk is completed and a new one is started, even if the next element would fit in the
prior chunk.

### "by\_similarity" chunking strategy

Only available in Unstructured API and Platform.

The `by_similarity` chunking strategy employs the `sentence-transformers/multi-qa-mpnet-base-dot-v1` embedding model to
identify topically similar sequential elements and combine them into chunks.

As with other strategies, chunks will never exceed the hard-maximum chunk size set by `max_characters`. For this reason,
not all elements that share a topic will necessarily appear in the same chunk. However, with this strategy you can
guarantee that two elements with low similarity will not be combined in a single chunk.

You can control the level of topic similarity you require for elements to have by setting the `similarity_threshold` parameter.
`similarity_threshold` expects a value between 0.0 and 1.0 specifying the minimum similarity text in consecutive elements
must have to be included in the same chunk. The default is 0.5.

###

## Learn more

<Icon icon="blog" />  [Chunking for RAG: best practices](https://unstructured.io/blog/chunking-for-rag-best-practices)
