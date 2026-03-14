# Source: https://docs.fiddler.ai/observability/platform/traffic-platform.md

# Traffic

Traffic as a service metric gives you basic insights into the operational health of your model's service in production.

![Example of a Fiddler Chart displaying a model's traffic.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-10d07fcafc0a651c0e88c0cd51c67c4f310b760a%2Fd1b7cdf-image.png?alt=media)

## What is Being Tracked?

* ***Traffic*** — The volume of traffic received by the model over time.

## Why is it Being Tracked?

* Traffic is a basic high-level metric that informs us of the model's output activity.

## What Steps Should I Take When I See an Outlier?

* A dip or spike in traffic needs to be investigated. For example, a dip could be due to a production model server going down; a spike could be an adversarial attack.
