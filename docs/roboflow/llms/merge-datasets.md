# Source: https://docs.roboflow.com/roboflow/roboflow-ko/datasets/merge-datasets.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/datasets/merge-datasets.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/datasets/merge-datasets.md

# Source: https://docs.roboflow.com/datasets/merge-datasets.md

# Merge Projects

You can combine different projects together to make a single project in which you can train a model.

If you have Project A and Project B and merge them to create Project C, Project C will be composed of the unique images joined from Projects A and B. Projects A and B will also still exist in the Workspace, not be eliminated.

## **How to Merge Projects**

To merge projects:

1. Hover your mouse on the three dots on the right side of one of the datasets you wish to include the merged dataset. Click the highlighted button (three horizontal dots), and select "Merge Datasets."
2. Select the datasets you wish to merge by clicking the checkboxes on the right side of each dataset.
3. Click "Merge Datasets" in the upper-right corner.
4. Name your new dataset and new annotation group click "Merge Datasets."

The merged dataset will contain the images (and any associated annotations) *present at the time of merging*.

![](https://662926385-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M6S9nPJhEX9FYH6clfW%2Fuploads%2Fgit-blob-5ed052fc1e997d0dd3a282e99878c0e714df7a76%2FMerge%20Projects.gif?alt=media)

In addition to the merged dataset, you retain the original datasets. In the above example, there are three datasets: the two originals and the newly merged dataset.

The best part is, because the merged dataset consists of copies of other photos, you aren't charged for extra images!
