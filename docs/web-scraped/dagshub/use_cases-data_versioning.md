# Source: https://dagshub.com/docs/use_cases/data_versioning/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTggMTJoOHYySDh6bTIgOEg2VjRoN3Y1aDV2My4xbDItMlY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNHptLTItMmg0LjFsLjktLjlWMTZIOHptMTIuMi01Yy4xIDAgLjMuMS40LjJsMS4zIDEuM2MuMi4yLjIuNiAwIC44bC0xIDEtMi4xLTIuMSAxLTFjLjEtLjEuMi0uMi40LS4ybTAgMy45TDE0LjEgMjNIMTJ2LTIuMWw2LjEtNi4xeiIgLz48L3N2Zz4=)](https://dagshub.com/DagsHub-Official/dagshub-docs/src/main/docs/use_cases/data_versioning.md "Edit this page")

# Data Versioning - Version Datasets and Data Files[¶](#data-versioning-version-datasets-and-data-files "Permanent link") 

Versioning your datasets and code is a critical component of data science projects that ensures the reproducibility of ML experiments. It provides traceability and enables collaboration among team members with ease.

<figure>
<a href="../assets/data_versioning/data_versioning.png" class="glightbox" data-type="image" data-width="auto" data-height="auto" data-desc-position="bottom"><img src="../assets/data_versioning/data_versioning.png" alt="Dataset Versioning" /></a>
<figcaption>Dataset Version Dropdown</figcaption>
</figure>

Let\'s learn when, and how to version your datasets with DagsHub [Data Engine](../../feature_guide/data_engine/), your data files using [DVC](../../integration_guide/dvc/), and code using Git, and how to manage and host all these components on DagsHub.

## When does versioning make sense?[¶](#when-does-versioning-make-sense "Permanent link")

Versioning makes sense in cases where your datasets might change, and you want to keep track of those changes.

This might be done for various reasons for example:

- Reverting in case of some error or other unexpected event
- Reproducing previous experiment results to verify them or continue working on previous research directions
- Regulatory requirements in certain medical, automotive and other use cases, where an external auditor may require you share your source data as it was when a certain model was trained
- Debugging models that are misbehaving

In most ML projects, it is recommended to version your data.

## Do I need to version datasets, data files or both?[¶](#do-i-need-to-version-datasets-data-files-or-both "Permanent link")

There are 3 main data change scenarios relevant for versioning:

1.  Data never changes (very rare in production ML projects) â€" In this case, perhaps versioning is unnecessary.
2.  Data is add-only, and metadata changes (for example annotations) , but data files themselves don\'t change (**this is the most common use case**) â€" In this case [dataset versioning](../data_engine/version_datasets/) is required.
3.  Data files change (imagine an image where between versions pixels might change) â€" In this case both [dataset versioning](../data_engine/version_datasets/) and [data file versioning](../../quick_start/version_data/) are required.

Select what type of versioning you\'d like to dive into:

- [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAxNiAxNiI+PHBhdGggZD0iTTcuNzUgMTRBMS43NSAxLjc1IDAgMCAxIDYgMTIuMjV2LTguNUM2IDIuNzg0IDYuNzg0IDIgNy43NSAyaDYuNWMuOTY2IDAgMS43NS43ODQgMS43NSAxLjc1djguNUExLjc1IDEuNzUgMCAwIDEgMTQuMjUgMTRabS0uMjUtMS43NWMwIC4xMzguMTEyLjI1LjI1LjI1aDYuNWEuMjUuMjUgMCAwIDAgLjI1LS4yNXYtOC41YS4yNS4yNSAwIDAgMC0uMjUtLjI1aC02LjVhLjI1LjI1IDAgMCAwLS4yNS4yNVpNNC45IDMuNTA4YS43NS43NSAwIDAgMS0uMjc0IDEuMDI1LjI1LjI1IDAgMCAwLS4xMjYuMjE3djYuNWMwIC4wOS4wNDguMTczLjEyNi4yMTdhLjc1Ljc1IDAgMCAxLS43NTIgMS4yOThBMS43NSAxLjc1IDAgMCAxIDMgMTEuMjV2LTYuNWMwLS42NDkuMzUzLTEuMjE0Ljg3NC0xLjUxNmEuNzUuNzUgMCAwIDEgMS4wMjUuMjc0Wk0xLjYyNSA1LjUzM3phLjI1LjI1IDAgMCAwLS4xMjYuMjE3djQuNWMwIC4wOS4wNDguMTczLjEyNi4yMTdhLjc1Ljc1IDAgMCAxLS43NTIgMS4yOThBMS43NSAxLjc1IDAgMCAxIDAgMTAuMjV2LTQuNWExLjc1IDEuNzUgMCAwIDEgLjg3My0xLjUxNi43NS43NSAwIDEgMSAuNzUyIDEuMjk5IiAvPjwvc3ZnPg==)]  **[Version Datasets](../data_engine/version_datasets/)**

  ------------------------------------------------------------------------

  Learn how to version your datasets, metadata, and annotations

- [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE0IDJINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoMTJhMiAyIDAgMCAwIDItMlY4em0tMiAxNmMtMi4wNSAwLTMuODEtMS4yNC00LjU4LTNoMS43MWMuNjMuOSAxLjY4IDEuNSAyLjg3IDEuNWEzLjUgMy41IDAgMCAwIDMuNS0zLjVBMy41IDMuNSAwIDAgMCAxMiA5LjVjLTEuMzUgMC0yLjUuNzgtMy4xIDEuOWwxLjYgMS42aC00VjlsMS4zIDEuM0M4LjY5IDguOTIgMTAuMjMgOCAxMiA4YTUgNSAwIDAgMSA1IDUgNSA1IDAgMCAxLTUgNSIgLz48L3N2Zz4=)]  **[Version Data Files](../../quick_start/version_data/)**

  ------------------------------------------------------------------------

  Learn how to version your changing data files

Was this page helpful?

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxME0xMCA5LjVjMCAuOC0uNyAxLjUtMS41IDEuNVM3IDEwLjMgNyA5LjUgNy43IDggOC41IDhzMS41LjcgMS41IDEuNW03IDBjMCAuOC0uNyAxLjUtMS41IDEuNVMxNCAxMC4zIDE0IDkuNSAxNC43IDggMTUuNSA4czEuNS43IDEuNSAxLjVtLTUgNy43M2MtMS43NSAwLTMuMjktLjczLTQuMTktMS44MUw5LjIzIDE0Yy40NS43MiAxLjUyIDEuMjMgMi43NyAxLjIzczIuMzItLjUxIDIuNzctMS4yM2wxLjQyIDEuNDJjLS45IDEuMDgtMi40NCAxLjgxLTQuMTkgMS44MSIgLz48L3N2Zz4=)

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIwIDEyYTggOCAwIDAgMC04LTggOCA4IDAgMCAwLTggOCA4IDggMCAwIDAgOCA4IDggOCAwIDAgMCA4LThtMiAwYTEwIDEwIDAgMCAxLTEwIDEwQTEwIDEwIDAgMCAxIDIgMTIgMTAgMTAgMCAwIDEgMTIgMmExMCAxMCAwIDAgMSAxMCAxMG0tNi41LTRjLjggMCAxLjUuNyAxLjUgMS41cy0uNyAxLjUtMS41IDEuNS0xLjUtLjctMS41LTEuNS43LTEuNSAxLjUtMS41TTEwIDkuNWMwIC44LS43IDEuNS0xLjUgMS41UzcgMTAuMyA3IDkuNSA3LjcgOCA4LjUgOHMxLjUuNyAxLjUgMS41bTIgNC41YzEuNzUgMCAzLjI5LjcyIDQuMTkgMS44MWwtMS40MiAxLjQyQzE0LjMyIDE2LjUgMTMuMjUgMTYgMTIgMTZzLTIuMzIuNS0yLjc3IDEuMjNsLTEuNDItMS40MkM4LjcxIDE0LjcyIDEwLjI1IDE0IDEyIDE0IiAvPjwvc3ZnPg==)

Thanks for your feedback!

Thanks for your feedback! Help us improve this page by creating an [issue in our Docs repo](https://dagshub.com/DAGsHub-Official/dagshub-docs/issues).