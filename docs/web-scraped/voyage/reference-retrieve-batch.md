# Source: https://docs.voyageai.com/reference/retrieve-batch

JUMP TO

## Voyage API 

- [[Inference]]
  - [[[Text embedding models]][[post]]](/reference/embeddings-api)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Multimodal embedding models]][[post]]](/reference/multimodal-embeddings-api)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Contextualized chunk embedding models]][[post]]](/reference/contextualized-embeddings-api)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Rerankers]][[post]]](/reference/reranker-api)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
- [[Files]]
  - [[[Upload file]][[post]]](/reference/upload-file)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[List files]][[get]]](/reference/list-files)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Retrieve file]][[get]]](/reference/retrieve-file)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Delete file]][[del]]](/reference/delete-file)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Retrieve file content]][[get]]](/reference/retrieve-file-content)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Bulk delete files]][[post]]](/reference/bulk-delete-files)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
- [[Batch]]
  - [[[Create batch]][[post]]](/reference/create-batch)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[List batches]][[get]]](/reference/list-batches)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Retrieve batch]][[get]]](/reference/retrieve-batch)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::
  - [[[Cancel batch]][[post]]](/reference/cancel-batch)

    ::: Sidebar-link-buttonWrapper3hnFHNku8_BJ
    :::

Powered by [](https://readme.com?ref_src=hub&project=voyage-ai)

# Retrieve batch 

[get]

[https://api.voyageai.com/v1/batches/]"}

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJJY29uIEljb24zX0QyeXN4RlpfbGwgSWNvbi1zdmcyTG03ZjZHOUx5NWEiIGRhdGEtbmFtZT0iY29weSIgcm9sZT0iaW1nIiBzdHlsZT0iLS1pY29uLWNvbG9yOmluaGVyaXQ7LS1pY29uLXNpemU6aW5oZXJpdDstLWljb24tc3Ryb2tlLXdpZHRoOjJweCIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0yMCA5aC05YTIgMiAwIDAgMC0yIDJ2OWEyIDIgMCAwIDAgMiAyaDlhMiAyIDAgMCAwIDItMnYtOWEyIDIgMCAwIDAtMi0yWiIgY2xhc3M9Imljb24tc3Ryb2tlLXdpZHRoIiAvPjxwYXRoIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik01IDE1SDRhMiAyIDAgMCAxLTItMlY0YTIgMiAwIDAgMSAyLTJoOWEyIDIgMCAwIDEgMiAydjEiIGNsYXNzPSJpY29uLXN0cm9rZS13aWR0aCIgLz48L3N2Zz4=)]

Returns a batch.

Language

*[][][][][][][][]*Shell

*[][][][][][][][]*Node

*[][][][][][][][]*Ruby

*[][][][][][][][]*PHP

*[][][][][][][][]*Python

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJJY29uIEljb24zX0QyeXN4RlpfbGwgSWNvbi1zdmcyTG03ZjZHOUx5NWEiIGRhdGEtbmFtZT0ibW9yZS12ZXJ0aWNhbCIgcm9sZT0iaW1nIiBzdHlsZT0iLS1pY29uLWNvbG9yOmluaGVyaXQ7LS1pY29uLXNpemU6aW5oZXJpdDstLWljb24tc3Ryb2tlLXdpZHRoOjJweCIgYXJpYS1sYWJlbD0iTW9yZSBlbGxpcHNpcyI+PHBhdGggc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgZD0iTTEyIDEzYTEgMSAwIDEgMCAwLTIgMSAxIDAgMCAwIDAgMlpNMTIgNmExIDEgMCAxIDAgMC0yIDEgMSAwIDAgMCAwIDJaTTEyIDIwYTEgMSAwIDEgMCAwLTIgMSAxIDAgMCAwIDAgMloiIGNsYXNzPSJpY29uLXN0cm9rZS13aWR0aCIgLz48L3N2Zz4=)]

Credentials

Header

Header

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJJY29uIEljb24zX0QyeXN4RlpfbGwgSWNvbi1zdmcyTG03ZjZHOUx5NWEiIGRhdGEtbmFtZT0ibG9jayIgcm9sZT0iaW1nIiBzdHlsZT0iLS1pY29uLWNvbG9yOmluaGVyaXQ7LS1pY29uLXNpemU6aW5oZXJpdDstLWljb24tc3Ryb2tlLXdpZHRoOjJweCIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGQ9Ik0xOSAxMUg1YTIgMiAwIDAgMC0yIDJ2N2EyIDIgMCAwIDAgMiAyaDE0YTIgMiAwIDAgMCAyLTJ2LTdhMiAyIDAgMCAwLTItMlpNNyAxMVY3YTUgNSAwIDEgMSAxMCAwdjQiIGNsYXNzPSJpY29uLXN0cm9rZS13aWR0aCIgLz48L3N2Zz4=)]