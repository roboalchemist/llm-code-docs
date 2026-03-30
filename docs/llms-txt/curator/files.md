# Source: https://docs.curator.interworks.com/site_content_design/files/files.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Files

> Manage file uploads and downloads with group-based access controls and search functionality for document management.

The system supports adding downloadable files and linking to them using the regular navigation menu process. File access
can be restricted based on Groups from the Tableau Server. Search keywords are also provided to help narrow down your
options when searching.

***To manage files:***

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Content** > **Files** section from the left-hand menu.
3. Add, modify, or delete files as desired.

## Hidden Settings

In Curator, there are two general use-cases for uploading files: **Images** and **Documents**.  By default, the
file-features are configured for Images since this is a much more common scenario.  See configuration items below that
describe treating files as images or documents:

**Hidden**: For images, for example a logo, it may cause confusion to surface the logo in search or inside of a
["recently viewed" Tiles](/site_content_design/pages/tiles) page-element.
In this scenario, hiding the file ensures the logo only shows up on the page you explicitly added it to.
However, you may want to show a PDF inside of the search results, or add it as a link to a tile selection.
*In this case, make sure to un-check the Hidden toggle on the edit-file page*.
