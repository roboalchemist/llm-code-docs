# Source: https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html

Title: Storage Inspector — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html

Markdown Content:
The Storage Inspector enables you to inspect various types of storage that a web page can use. Currently it can be used to inspect the following storage types:

*   _Cache Storage_ — any DOM caches created using the [Cache API](https://developer.mozilla.org/en-US/docs/Web/API/Cache).

*   _Cookies_ — All the [cookies](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie) created by the page or any iframes inside of the page. Cookies created as a part of response of network calls are also listed, but only for calls that happened while the tool is open.

*   _IndexedDB_ — All [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) databases created by the page or any iframes inside the page, their Object Stores and the items stored in these Object Stores.

*   _Local Storage_ — All [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) items created by the page or any iframes inside the page.

*   _Session Storage_ — All [session storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage) items created by the page or any iframes inside the page.

For the time being, the Storage Inspector only gives you a read-only view of storage. But we’re working to let you edit storage contents in future releases.

Opening the Storage Inspector[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#opening-the-storage-inspector "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can open the Storage Inspector by selecting the _Storage_ panel in the Web Developer Tools, accessible from the Browser Tools submenu

The [Toolbox](https://firefox-source-docs.mozilla.org/devtools-user/tools_toolbox/index.html) will appear at the bottom of the browser window, with the Storage Inspector activated. It’s just called “Storage” in the Developer Toolbox.

![Image 1: ../../_images/storage_inspector.png](https://firefox-source-docs.mozilla.org/_images/storage_inspector.png)
Storage Inspector User Interface[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#storage-inspector-user-interface "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Storage Inspector UI is split into three main components:

*   [Storage tree](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#storage-inspector-storage-tree)

*   [Table Widget](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#storage-inspector-table-widget)

*   [Sidebar](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#storage-inspector-sidebar)

![Image 2: ../../_images/storage_labeled.png](https://firefox-source-docs.mozilla.org/_images/storage_labeled.png)
### Storage tree[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#storage-tree "Link to this heading")

The storage tree lists all the storage types that the Storage Inspector can inspect:

![Image 3: ../../_images/storage_types.png](https://firefox-source-docs.mozilla.org/_images/storage_types.png)
Under each type, objects are organized by origin. For cookies, the protocol does not differentiate the origin. For Indexed DB or local storage an origin is a combination of protocol + hostname. For example, “`http://mozilla.org`” and “`https://mozilla.org`” are two different origins so local storage items cannot be shared between them.

Under “Cache Storage”, objects are organized by origin and then by the name of the cache:

![Image 4: ../../_images/cache_storage.png](https://firefox-source-docs.mozilla.org/_images/cache_storage.png)
IndexedDB objects are organized by origin, then by database name, then by object store name:

![Image 5: ../../_images/indexeddb_storage.png](https://firefox-source-docs.mozilla.org/_images/indexeddb_storage.png)
With the Cookies, Local Storage, and Session Storage types, there’s only one level in the hierarchy, so stored items are listed directly under each origin:

![Image 6: ../../_images/cookie_storage.png](https://firefox-source-docs.mozilla.org/_images/cookie_storage.png)
You can click on each item in the tree to expand or collapse its children. The tree is live, so if a new origin gets added (by adding an iframe, for example), it will be added to each storage type automatically.

Clicking on a tree item will display detailed information about that item in the Table Widget on the right. For example, clicking on an origin which is a child of the Cookies storage type will show all the cookies belonging to that domain.

### Table Widget[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#table-widget "Link to this heading")

The table widget displays a list of all the items corresponding to the selected tree item (be it an origin, or database) are listed. Depending on the storage type and tree item, the number of columns in the table might differ.

All the columns in a Table Widget are resizable. You can hide and show columns by context-clicking on the table header and selecting the columns you want to see:

![Image 7: ../../_images/cookie_context_menu.png](https://firefox-source-docs.mozilla.org/_images/cookie_context_menu.png)
### Search[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#search "Link to this heading")

There’s a search box at the top of the Table Widget:

![Image 8: ../../_images/storage_detail_filter.png](https://firefox-source-docs.mozilla.org/_images/storage_detail_filter.png)
This filters the table to show only items which match the search term. Items match the search term if any of their fields (including fields whose columns you have hidden) contain the search term.

You can use Ctrl + F (Cmd + F on a Mac) to focus the search box.

### Add, clear and refresh storage[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#add-clear-and-refresh-storage "Link to this heading")

You’ll also have buttons available to add a new storage entry, delete all existing entries, or refresh the view of the currently viewed storage type where applicable (you can’t add new entries to IndexedDB or Cache):

![Image 9: ../../_images/storage_detail_add_clear_refresh.png](https://firefox-source-docs.mozilla.org/_images/storage_detail_add_clear_refresh.png)
Working with the Storage Inspector[](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/index.html#working-with-the-storage-inspector "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following articles cover different aspects of using the Storage Inspector:

*   [Cookies](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/cookies/index.html)

*   [Local Storage / Session Storage](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/local_storage_session_storage/index.html)

*   [Cache Storage](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/cache_storage/index.html)

*   [IndexedDB](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/indexeddb/index.html)

*   [Extension Storage](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/extension_storage/index.html)
