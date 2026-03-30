# Source: https://docs-v3.activeloop.ai/3.1.0/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/3.1.1/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.1.5/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.2.0/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.2.9/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.2.20/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.2.22/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.4.0/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.4.1/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.0/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.1/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.2/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.3/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.8/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.9/how-it-works/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.6.18/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.7.0/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.7.1/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.7.2/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.7.3/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.8.2/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.8.16/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.8.19/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.8.27/technical-details/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/v3.9.0/technical-details/data-format/version-control-and-querying.md

# Source: https://docs-v3.activeloop.ai/technical-details/data-format/version-control-and-querying.md

# Version Control and Querying

## Understanding the Interaction Between Deep Lake's Versions, Queries, and Dataset Views.

Version control is the core of the Deep Lake data format, and it interacts with queries and view as follows:

* Datasets have commits and branches, and they can be traversed or merged using Deep Lake's Python API.&#x20;
* Queries are applied on top of commits, and in order to save a query result as a `view`, the dataset cannot be in an uncommitted state (no changes were performed since the prior commit).&#x20;
* Each saved `view` is associated with a particular commit, and the view itself contains information on which dataset indices satisfied the query condition.

This logical approach was chosen in order to preserve data lineage. Otherwise, it would be possible to change data on which a query was executed, thereby potentially invalidating the saved view, since the indices that satisfied the query condition may no longer be correct after the dataset was changed.&#x20;

**Please check out our** [**Getting Stated Guide**](https://docs-v3.activeloop.ai/examples/dl/guide) **to learn how to use the Python API to** [**version your data**](https://docs-v3.activeloop.ai/examples/dl/guide/dataset-version-control)**,** [**run queries, and save views**](https://docs-v3.activeloop.ai/examples/tql)**.**&#x20;

An example workflow using version control and queries is shown below.&#x20;

<figure><img src="https://content.gitbook.com/content/WOs95B2h3lcO4dwXDRJ3/blobs/895vvEFPvrrpyGuapREz/image.png" alt=""><figcaption></figcaption></figure>

### Version Control HEAD Commit

Unlike Git, Deep Lake's dataset version control does not have a local staging area because all dataset updates are immediately synced with the permanent storage location (cloud or local). Therefore, any changes to a dataset are automatically stored in a HEAD commit on the current branch. This means that the uncommitted changes do not appear on other branches, and uncommitted changes are visible to all users.
