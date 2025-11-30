# Source: https://dagshub.com/docs/feature_guide/dagshub_diffing/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/feature_guide/dagshub_diffing.md "Edit this page")

# DagsHub Diffing[¶](#dagshub-diffing "Permanent link")

DagsHub Diffing is a file comparison tool incorporated into DagsHubâ€™s repositories. It supports diffing of popular open formats, such as notebooks, CSVs, images, and more. It is based on Git commits and enables diffing files versioned by both Git and DVC. It works similarly to code diffing, and since it\'s entirely web-based, no configuration or setup is involved.

If you have a request for a custom diff view please visit our [suggestions channel Discord](https://discord.gg/X6ugUwcPAs) and share your request.

## How does DagsHub Diffing work?[¶](#how-does-dagshub-diffing-work "Permanent link")

DagsHub Diffing is based on Git commits and enables diffing files versioned by both Git and DVC. For Git-tracked files, it simply shows the version of the files under the selected Git commit. The real magic happens with files tracked by DVC. DagsHub Diffing uses the pointers files (`.dvc` or `dvc.lock`) held under the selected Git commit, parses the remote storage for the matching files, and presents them as part of the diff.

## How to use DagsHub Diffing?[¶](#how-to-use-dagshub-diffing "Permanent link")

1.  Select the **base branch.** This is generally the trunk branch, containing deployment-ready code.
2.  Select the **comparison branch.** This is generally the dev branch, containing experimental updates.
3.  Once within diffing mode, **File Compare** allows you a sharper perspective on the changes made through the commit.

Create a DagsHub Diff

\

~Create\ a\ DagsHub\ Diff~

\

### Extra Capabilities[¶](#extra-capabilities "Permanent link")

1.  **Unified View** merges changes made between the two files.
2.  **Diff Stats** provides a contextual point-of-reference for changes made through the commit, supplementing directory diffs.
3.  **View left file / View right file** displays the full file pertaining to the base / comparison commit respectively.

Use Additional Diffing Capabilities

\

~Use\ Additional\ Diffing\ Capabilities~

\

It is also possible to compare commits. Click on the commit history, find the desired commit for comparison, and copy its hash to the comparison bar. Next, choose a branch or another commit in the second bar, and DagsHub Diffing will take care of the rest.

Use DagsHub Diffing on a Commit

\

~Use\ DagsHub\ Diffing\ on\ a\ Commit~

\

## What types of formats does DagsHub Diffing support?[¶](#what-types-of-formats-does-dagshub-diffing-support "Permanent link")

DagsHub Diffing supports code, notebook, CSV, images, and directory diffing. Letâ€™s take a quick look at how DagsHub Diffing works for each format.

For your convenience, each comparison header links to the example on the repository, so you can take a better look.

### [Directory Diffing](https://dagshub.com/nirbarazida/CheXNet/diff/heatmaps?compare=training&file_diff=false&page=0&path=)[¶](#directory-diffing "Permanent link")

We consider the directory diff a bird\'s eye view, indicating which directories were modified to understand the overall changes. It uses the same color format as text diff (green - new directory, white - no changes, yellow - modified, red - deleted) but refers to files within the directory. DagsHub Diffing will use the same color format for files placed at the same tree level (e.g., `dvc.yaml`).

[![Folder Diff](../assets/dagshub_diffing/folder_diff.png)](../assets/dagshub_diffing/folder_diff.png)

~Folder\ Diff~

### [Code Diffing](https://dagshub.com/nirbarazida/CheXNet/commit/0b369704d60d7c01677c424d3dcf7aad2d44ee00)[¶](#code-diffing "Permanent link")

Having both versions alongside their associated changes allows contextualizing the various changes. In the following example, the additional function and its subsequent implementation:

[![Code Diff](../assets/dagshub_diffing/code_diff.png)](../assets/dagshub_diffing/code_diff.png)

~Code\ Diff~

### [Notebook Diffing](https://dagshub.com/OperationSavta/SavtaDepth/diff/master?compare=epoch_testing&page=0&path=Notebooks%2FSavtaDepth_Colab.ipynb)[¶](#notebook-diffing "Permanent link")

DagsHub Diffing also renders notebook diffs, highlighting changes in cell inputs, outputs as well as notebook metadata.

[![Notebook Diff](../assets/dagshub_diffing/notebook-diff.png)](../assets/dagshub_diffing/notebook-diff.png)

~Notebook\ Diff~

### [Image Diffing](https://dagshub.com/nirbarazida/CheXNet/diff/master?compare=heatmaps&path=evaluating%2Fheatmap_eval%2Fcams_0.png)[¶](#image-diffing "Permanent link")

DagsHub relies on a context-focused approach for image diffing. Placing images side-by-side allows you to visually *view and* compare changes.

Additionally, DagsHub utilizes the metadata it stores about the images and shows their diff. It provides extra factors for the reviewer to consider that may be crucial to the task.

[![Image Diff](../assets/dagshub_diffing/image_diff.png)](../assets/dagshub_diffing/image_diff.png)

~Image\ Diff~

### [CSV Diffing](https://dagshub.com/Simon/world_mortality/commit/c6fc79b51e524358947a2289ac520065e6830a46)[¶](#csv-diffing "Permanent link")

DagsHub Diffing parses the CSV file, showing it in a table view, and presents the changes using a color format (green - new, white - no changes, yellow - modified, red - deleted). For modified cells, it shows the cell\'s previous and new values.

[![CSV Diff](../assets/dagshub_diffing/csv_diff.png)](../assets/dagshub_diffing/csv_diff.png)

~CSV\ Diff~

DagsHub also features SQL-like dataset filtering, enabling acute comparisons between diffs. By setting conditional parameters for column values, it allows you to swiftly compare changes across subsets of data.

[![](../assets/dagshub_diffing/csv_diff_deaths.png)](../assets/dagshub_diffing/csv_diff_deaths.png)\
~Filtering\ queries\ for\ CSV\ diffing~

## [Discussions](https://dagshub.com/nirbarazida/CheXNet/src/8ad02b57561dd8b4a854444d114892214b479b4b/data_labeling/data/images_001/images/00000001_001.png#comment-1)[¶](#discussions "Permanent link")

[DagsHub Discussions](../dagshub_discussions/) is also available in diffing modes. You can communicate over file diffs by leaving a note in the comment section. Once created, the new discussion is linked to the relevant diff and is sharable with DagsHub\'s URL.

[![Discussing a file diff](../assets/dagshub_diffing/discussion_diff.png)](../assets/dagshub_diffing/discussion_diff.png)

~Discussing\ a\ file\ diff~

# Known Issues, Limitations & Restrictions[¶](#known-issues-limitations-restrictions "Permanent link")

- CSV diffing is affected by poorly formatted CSV data, and may default to false-negative differences. Weâ€™re working on a fix!

[![](../assets/dagshub_diffing/csv_bug_raw.png)](../assets/dagshub_diffing/csv_bug_raw.png)\
~An\ example\ of\ a\ heading\ that\ breaks\ csv\ diffs~

- When diffing images, it is not possible to use Bounding Boxes to mark sections in the image and comment on them.

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).