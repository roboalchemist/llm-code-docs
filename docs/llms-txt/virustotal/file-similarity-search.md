# Source: https://virustotal.readme.io/docs/file-similarity-search.md

# File similarity search

For the time being the main file similarity search is based on a structural feature hash developed in-house at VirusTotal for the following file types: Portable Executables, PDFs, Office documents, RTFs and Flash SWF files. This hash has not been computed for the whole sample collection, it was introduced in August 2012 starting with portable executables and so only samples sent from then onwards will be searcheable via this feature. Ssdeep similarity search is also available, allowing you to parametrize the similarity threshold, please refer to the [modifiers table](https://virustotal.readme.io/docs/search-modifiers-full-list) to learn more about it.

![File Similarity Search Icon](https://storage.googleapis.com/vtdocresources/guides/vt-intelligence/similaritysearch_icon_20231110.png)

You can click on the waves icon on a given search result sample row in order to search samples similar to the one under consideration.

Please note that this feature is only available if the file has the structural feature hash available. We plan to continue developing a similar hash for other file types.