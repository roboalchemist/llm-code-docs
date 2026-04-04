# Source: https://docs.verda.com/storage/container-registry/tag-immutability-rules.md

# Tag immutability rules

### Tag immutability

Tag immutability rules allow you to prevent images with specific tags from being overwritten or deleted.

You define patterns for repositories and tags. See [Tag rules syntax](https://docs.verda.com/storage/container-registry/tag-rules-syntax).

#### Why use tag immutability rules?

1. **Guarantee Reproducible Builds**

   Mutable tags cause environment drift, where the same tag might deploy different code over time. Immutability ensures a specific tag always resolves to the exact same image, eliminating "it worked in Staging" inconsistencies.
2. **Prevent "Supply Chain" Attacks**

   Immutability blocks compromised pipelines or actors from overwriting trusted tags with malicious code. This ensures that the image defined in your deployment manifest is exactly what runs in your container.
3. **Ensure Reliable Rollbacks**

   Rollbacks rely on previous versions remaining unchanged. Immutability guarantees that "known good" tags stay exactly as they were when verified, preserving your safety net during deployment failures.
4. **Avoid Caching Issues**

   Overwriting tags causes consistency issues when nodes rely on aggressive caching. Immutability prevents a cluster from running a confusing mix of cached old code and pulled new code under the same tag name.

#### Examples <a href="#example" id="example"></a>

Example 1: To make all tags for all repositories in the project immutable, set the following options:

* Set **Apply to image repositories** to **matching** and enter `**`.
* Set **Tags** to **matching** and enter `**`.

Example 2: To allow the tags `rc`, `test`, and `nightly` to be overwritten but make all other tags immutable, set the following options:

* Set **Apply to image repositories** to **matching** and enter `**`.
* Set **Tags** to **excluding** and enter `rc,test,nightly`.

Example 3: Make [SemVer](https://semver.org/) tags (with optional `v` prefix) immutable for all repositories:

* Set **Apply to image repositories** to **matching** and enter `**`.
* Set **Tags** to **matching** and enter `{v,}[0-9]{,[0-9],[0-9][0-9]}.[0-9]{,[0-9],[0-9][0-9]}.[0-9]{,[0-9],[0-9][0-9]}`
* This will work for SemVer tags up to three decimal digits per section e.g. `999.999.999`
