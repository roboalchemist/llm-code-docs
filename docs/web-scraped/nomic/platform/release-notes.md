# Nomic Documentation

Source: https://docs.nomic.ai/platform/release-notes

## 2025-05-09​

### UMAP Projection Algorithm​

- UMAP is now available as a projection algorithm.
- UMAP is currently the default for datasets with fewer than 50,000 datapoints.
### Additional Updates​

- Logging in with your Nomic API key now determines the organization that operations like dataset loading and map creation will use
- Default organizations are now deprecated.
## 2024-12-04​

### New map filtering workflow​

- Filter map data by categorical fields by clicking on the field in the legend
- Browser detection used to warn users with incompatible browsers
- Table view image rendering improvements
## 2024-11-20​

### Scoped API keys​

- API keys may now be scoped by: user, organization, or individual dataset
- All new API keys will be organization-scoped by default. They were previously user-scoped
- Dataset level user access UI has been updated:  choose exactly which members of your organization have the ability to see, edit, and administer individual maps
- Support for multilingual data mapping has been added to the data upload page
## 2024-11-06​

### Map datapoint previews​

- Atlas maps now show data previews when datapoints are moused over
- Mobile view style improvements for data preview
- Map legend relocated to view settings
## 2024-10-09​

### Map sharing​

- Data maps can now be shared across the internet via the "Share" button in the upper right of the map view. Sharing saves the entire data map state including the current view, coloring, and data selection.
- Dataset table view is now available to beta users.
- Dataset preview improvements: data loading performance improvements and cleaner look
## 2024-09-11​

### Endpoints for Programatic Selections​

- New Atlas API endpoints allow for replicating any map search filter programatically. This includes regex search, kNN search, semantic search and column filters.
- Data map points now have better default sizes.
- Various bug fixes around data map topic labels
## 2024-08-14​

### Tag Manager, Invertible data map selections and RBAC updates​

- Atlas dataset view now has a ‘tags’ tab, allowing for improved collaboration and tagging management on shared datasets
- All map selections are now invertible
- Lasso selections can now be performed on multi-positional maps
- Atlas map data loading performance improvements
- Restrict dataset public/private access settings to admin users only
- Fixed bug so that editors can create Atlas datasets from the dashboard
- Updated Role-Based Access Control (RBAC) and Security documentation
## 2024-07-31​

### Atlas Discovery Hub release​

- Atlas Discovery Hub is now out of beta - browse thousands of public Atlas datasets!
- Bulk tag removal from selected datapoints in the Atlas map interface is now supported
- Topic label improvements: unknown topics are now labeled with numbers e.g. 'topic 3'
## 2024-07-17​

### Maintenance​

- Indexed columns are now visually indicated in the dataset overview
- Map selections with < 100 results will continue fetching more results until all results have been loaded
- Fixed bug so that boolean data types may not be uploaded as a part of a dataset
## 2024-07-03​

### Semantic Search Improvements​

- Semantic search on vision models can now query search
- Document and query search no longer available in embedding projects
- Fixed bug on csv upload with certain reserved column names
- Fixed bug in lasso interaction
## 2024-06-19​

### Maintenance​

- At time of account creation, you can now change the URL slug for your organization as well as the display name
- Updates to the organization member control page
- Stability improvements to the web upload page
- Removed ability to upload files that have been pickled with numpy
## 2024-06-05​

### Nomic Embed Image: Multimodal Embeddings in Atlas​

- Atlas supports mapping image datasets using the Nomic Embed Vision model. Datasets with images can be stored in Atlas using the map_data function from the Nomic Python SDK.
```
map_data
```

- Topics for a highlighted datapoint are now visible in the data sidebar
- Fixed bug in saving topic labels which get updated during session
- Improved reliability of web upload for JSON and JSONL files
- Improvements to lasso selections in non-embedding data spaces
## 2024-05-22​

### Maintenance​

- Improvements to reporting on state of unbuilt maps
- Increase time to loading of 404 pages when non-existent maps are requested
- Improvements to permissions
- Fixed bug in tags created using the lasso tool
## 2024-05-08​

### Semantic Search API for New Users​

- Users can call semantic search via the embeddings API before logging into nomic
- Fixed bug where some dropdown menus contained two copies of some items
- Fixed bug using the lasso tool
## 2024-04-24​

### RBAC, Semantic Search API​

- Role Based Access Control (RBAC) added for users to create API keys and datasets as members of an organization
- Semantic search added to embeddings API
- Faster page loading: removed unneeded build-time dependencies
- Improvements to the appearance of organization and project pages for non-logged-in users
- Fixed bug when selecting individual points in Atlas map
- Default projection algorithm upgraded to nomic-project-2
## 2024-04-12​

### Improved map UI, topic label editing​

- Revamp of the map UI for better use of space and ease of use
- Topic labels can now be edited by map admins from within the map page; changes to topic labels are immediately reflected in the map and propagated to the server
## 2024-04-11​

### Temporarily disabling of updating Atlas indices​

- The ability to update an Atlas index is temporarily deprecated due to critical flaws in it's functionality and data consistency guarantees. Please message support@nomic.ai for details on when the feature will become available again.
## 2024-03-29​

### Range slider improvements, map projection improvements​

- Range Slider now supports zooming in and out for more precision, better UI for settings dates and minor data display updates
- Improved 2D layout — nomic-project-v1 will now auto-infer hyperparameters based on your dataset by default, resulting in layouts that better capture local and global embedding structure.
- Datasets embedded by Nomic now show the embedding model used to create them
- Various bug fixes, including more stability on the data upload page
## 2024-03-05​

### New tagging capabilities, duplicate detection for embedding datasets​

- Tagging capabilties now scale to 10 million points, includes improved collaborative capabilities and selection based exports.
- Duplicate detection capabilities are now enabled for embedding modality datasets. Set a low duplicate detection threshold for effective use.
- Sets nomic-embed-text-v1.5 as default model for text modality datasets.
- Miscellaneous bug fixes.
## 2024-02-14​

### Nomic Embed v1.5, Data interface: topic editing, column reordering, CSV export​

- Launch of Nomic Embed v1.5, a text embedding model that supports variable output size.
- Allows reordering data in the preview window, so users can choose which metadata fields are most visible.
- Allow full dataset export as CSV from the map title bar for map owners and editors.
- Allow including Nomic topic labels in selection downloads and full dataset export.
- Miscellaneous small fixes.
## 2024-02-01​

### Nomic Embed, Topic Label Improvements​

- Nomic Embed: The flagship Nomic Atlas embedding model is now launched as an inference endpoint and as the default embedding model in Nomic Atlas.
- Topic Label Generation Improvements: The topics labels assigned to detected topics in your datasets have been improved for quality, consistency and relevance. Remember, you can access topics and labels programatically with the Nomic Python Client.
- Embedding Inference Optimizations: Lowered P75 latency of embedding inference to 200ms at batch size 100 and seq length 2048.
- Various minor bug patches.
## 2024-01-24​

### Browser Data Upload Improvements, access to points, new URLs​

- Browser Data Upload: Columns are now editable, patched several case bugs involving duplicate names, etc.
- It's now easier to isolate a single point on the map--just click and you'll get
immediate access to the most important information about your point,
with the full information available on the left. There's also a handy way to
add it to the current selection--watch here for more operations on
individual items in your dataset!
- Atlas uses slugs instead of UUIDs even for maps--the default place to view your dataset
map is now at https://atlas.nomic.ai/my_org/my_project/map. If you've built multiple maps,
they're still accessed by UUID: but most users share just the most recent map they have,
and this makes it easier to understand your links and work with them from the python client.
- The in-browser project creation interface is now more reliable and
returns better information about errors in uploaded CSVs.
## 2024-01-15​

### Stability and Scale​

- Infrastructure upgrades towards making tagging scale to 10 million point datasets in the browser
- Patches to edge cases introduced by the introduction human-readable slugs in URLs
- Non-critical security patches as detected by latest external penetration test.
- Infrastructure stability improvements in response to edge cases detected in dataset indexing.
- Atlas API endpoint to update topic labels
## 2023-12-01​

### Unstructure Data Interface Composable Selection​

- Composable Selection: All Nomic Atlas data selections are now composable at the ten's of million points scale. Build highly expressive selections over your datasets in the web browser with metadata filtering, regex search and semantic region lasso'ing. Try searching your Atlas dataset, and combine it with a lasso over some of the results.
## 2023-11-10​

### Multiple filters​

- Atlas now allows you to combine multiple searches together at the same time--lassos, regular expressions searches, and/or
categorical filters. Choose whether to use "any" or "all" to combine multiple filters together.
## 2023-11-01​

### Core Algorithm Improvements​

- Nomic Projection Algorithm Latency: The Nomic Projection algorithm can now build a 2D projection of 1M points in five minutes.
- 2025-05-09UMAP Projection AlgorithmAdditional Updates
- UMAP Projection Algorithm
- Additional Updates
- 2024-12-04New map filtering workflow
- New map filtering workflow
- 2024-11-20Scoped API keys
- Scoped API keys
- 2024-11-06Map datapoint previews
- Map datapoint previews
- 2024-10-09Map sharing
- Map sharing
- 2024-09-11Endpoints for Programatic Selections
- Endpoints for Programatic Selections
- 2024-08-14Tag Manager, Invertible data map selections and RBAC updates
- Tag Manager, Invertible data map selections and RBAC updates
- 2024-07-31Atlas Discovery Hub release
- Atlas Discovery Hub release
- 2024-07-17Maintenance
- Maintenance
- 2024-07-03Semantic Search Improvements
- Semantic Search Improvements
- 2024-06-19Maintenance
- Maintenance
- 2024-06-05Nomic Embed Image: Multimodal Embeddings in Atlas
- Nomic Embed Image: Multimodal Embeddings in Atlas
- 2024-05-22Maintenance
- Maintenance
- 2024-05-08Semantic Search API for New Users
- Semantic Search API for New Users
- 2024-04-24RBAC, Semantic Search API
- RBAC, Semantic Search API
- 2024-04-12Improved map UI, topic label editing
- Improved map UI, topic label editing
- 2024-04-11Temporarily disabling of updating Atlas indices
- Temporarily disabling of updating Atlas indices
- 2024-03-29Range slider improvements, map projection improvements
- Range slider improvements, map projection improvements
- 2024-03-05New tagging capabilities, duplicate detection for embedding datasets
- New tagging capabilities, duplicate detection for embedding datasets
- 2024-02-14Nomic Embed v1.5, Data interface: topic editing, column reordering, CSV export
- Nomic Embed v1.5, Data interface: topic editing, column reordering, CSV export
- 2024-02-01Nomic Embed, Topic Label Improvements
- Nomic Embed, Topic Label Improvements
- 2024-01-24Browser Data Upload Improvements, access to points, new URLs
- Browser Data Upload Improvements, access to points, new URLs
- 2024-01-15Stability and Scale
- Stability and Scale
- 2023-12-01Unstructure Data Interface Composable Selection
- Unstructure Data Interface Composable Selection
- 2023-11-10Multiple filters
- Multiple filters
- 2023-11-01Core Algorithm Improvements
- Core Algorithm Improvements
