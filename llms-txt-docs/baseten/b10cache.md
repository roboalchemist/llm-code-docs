# Source: https://docs.baseten.co/development/model/b10cache.md

# b10cache 🆕

> Persist data across replicas or deployments

<Warning>
  ### Early Access

  Please contact our [support team](mailto:support@baseten.co) for access to b10cache.
</Warning>

Deployments sometimes have cache or other files that are useful to other replicas. Using `torch.compile` results in a cache that can speed up future `torch.compile` on the same function. This can speed up other replicas' cold start times.

**These files can be stored via b10cache**. b10cache is a volume mounted over the network onto each of your pods. There are two ways files can be stored:

#### 1. `/cache/org/`

This directory is shared, and can be written to or accessed by every pod you deploy. Simply move a file into here and it will be accessible.

#### 2. `/cache/model/`

This directory is shared by every pod within the scope of your deployment. This is excellent for keeping filesystems clean and limiting access.

<Danger>
  ### Not a persistent object storage

  While b10cache is very reliable, it should not be used as a persistent object storage or database. **It should be considered a cache** that can be shared by deployments, meaning there should always be a fallback plan if the b10cache path does not exist.
</Danger>

See two features built on b10cache:

1. [*model cache*](/development/model/model-cache)
2. [*torch compile cache*](/development/model/torch-compile-cache)
