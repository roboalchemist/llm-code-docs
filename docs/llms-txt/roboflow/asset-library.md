# Source: https://docs.roboflow.com/roboflow/roboflow-ko/workspaces/asset-library.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/workspaces/asset-library.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/workspaces/asset-library.md

# Source: https://docs.roboflow.com/workspaces/asset-library.md

# Asset Library

Asset Library allows users to find and manage images across an entire Workspace in one place.&#x20;

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FIp24b4A8KYSZrCvCPUsn%2Fasset-library.png?alt=media&#x26;token=55ae2d42-7bc1-4bb8-831c-db685953854a" alt=""><figcaption><p>Using semantic search ("boxes") to find images across all projects in a Workspace</p></figcaption></figure>

### Finding images

Asset Library features a powerful searching capabilities that combine:

* Semantic search, so you can describe an image, eg. `boxes` and it will return all images of boxes
* [Similarity search](https://docs.roboflow.com/annotate/use-roboflow-annotate/similarity-search-and-settings), to find similar images, eg. `like-image:61JNhXnwbNqNxux5Acnk`
* [Traditional Dataset filtering](https://docs.roboflow.com/datasets/manage-datasets/dataset-search), eg. `class:helmet AND NOT (tag:v1 OR tag:v2)`&#x20;
* [Metadata search](https://docs.roboflow.com/datasets/adding-data/image-metadata#searching-by-metadata), eg. `metadata:author=John`

### Managing images

After you find images based on your search settings, you can select them (manually or select all), and:

* Add tags to selected images, so you can later find them easier (search by tag)
* Create a New Project with selected images
* Add selected images to an Existing Project

<figure><img src="https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2FObvGOsi476boH5JU00xD%2Fimage.png?alt=media&#x26;token=cfe80243-d92e-485a-8eea-8b55b38c601e" alt=""><figcaption></figcaption></figure>
