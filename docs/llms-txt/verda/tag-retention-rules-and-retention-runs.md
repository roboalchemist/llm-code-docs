# Source: https://docs.verda.com/storage/container-registry/tag-retention-rules-and-retention-runs.md

# Tag retention rules & retention runs

### Tag retention

Tag retention rules determine how long images (tags) are kept before deletion. Rules can be based on age, tag patterns, and repository patterns.

Retention runs are the events in which images are deleted or retained, based on the defined retention rules. If an image matches any of the retention rules (or one of its tags matches a rule) then it will be retained.

Runs can be triggered manually or scheduled.\
We recommend testing your tag retention rules by manually triggering a dry run to see which images would have been retained (or deleted):

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FP3tc8WW44nVK4c03aMH5%2FRetention%20runs.png?alt=media&#x26;token=94f6f879-eee4-44c6-88a7-e372498bf872" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Immutable tags (defined under tag immutability rules) won't be deleted during a retention run, even if they don't explicitly have a retention rule.
{% endhint %}

**Why use tag retention rules?**

1. **Minimize Storage Costs**

   Container registries grow indefinitely if left unchecked. Retention rules automatically identify and delete old or unused artifacts—such as stale nightly builds or overwritten tags—preventing expensive storage bills and quota exhaustion.
2. **Automate Repository Cleanup**

   Manual cleanup is tedious and prone to human error. Retention policies automate the lifecycle management of your images, systematically pruning ephemeral tags (like `feature-branch-v1`) while ensuring stable release tags remain untouched.
3. **Improve Registry Performance**

   Bloated registries with thousands of stale images suffer from slower indexing and search speeds. Aggressively pruning old data ensures your CI/CD pipelines maintain fast, reliable interactions with the registry.

#### Examples

Example 1: Retain all images in all repositories for a year:

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2FWdTN269bGRKqKLBU10Nv%2FRetention%20example%201.png?alt=media&#x26;token=7cce94ec-09c6-41f3-a691-18383c2fc540" alt=""><figcaption></figcaption></figure>

Example 2: Delete all images (exclude all tags (\*\*) is equivalent to retain none) in repository ending in `playground`

<figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2F6triPZzGokQLcI3nGV8T%2FRetention%20example%202.png?alt=media&#x26;token=d92b3c42-5c39-461f-8148-9d165c25e705" alt=""><figcaption></figcaption></figure>
