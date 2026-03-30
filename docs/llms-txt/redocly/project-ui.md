# Source: https://redocly.com/docs/realm/reunite/project/project-ui.md

# Reunite project interface

Use this document as a reference for the user interface (UI) of pages in Reunite's project workspace.
Learn about the various ways you can utilize the interface controls.

## General interface

Screenshot of a project workspace page in Reunite
All project workspace pages have:

- (1) navigation pane
- (2) top bar


### Reunite navigation pane

Screenshot of the navigation pane in Reunite
Use the navigation pane to:

- (1) access the [organizations and projects menu](#organization-and-projects-menu)
- (2) collapse the navigation pane
- (3) switch between [Reunite workspace pages](/docs/realm/reunite/reunite)
- (4) [access the user profile menu](/docs/realm/reunite/user-profile-menu)


#### Organization and projects menu

Screenshot of Reunite's organization and projects menu
Use the organization and projects menu to:

- (1) create a new organization
- (2) switch between organizations
- (3) return to the organization's **Overview** page
- (4) switch between projects
- (5) [create a new project](/docs/realm/reunite/project/manage-projects#create-a-project)


## Editor

The **Editor** page is the part of Reunite's project workspace where you add, edit, and manage the content of your project.
The page has three parts:

- the file tree pane
- the editing pane
- the webview pane


To best suit your experience, you can adjust the size of the panes or collapse the file tree or the webview pane.

### File tree pane

The file tree pane has three tabs:

- files tab with **Theme components** pane
- search tab
- commit tab with **History** pane


#### Files tab

The files tab displays the file tree of your project, including remote files.
Use this tab to add, modify, or delete files, as well as eject your project's theme components.

Screenshot of the Files tab in Reunite editor
In this tab you can:

- (1) add new content:
  - [add new files and folders](/docs/realm/reunite/project/use-editor#add-files)
  - [add folders from a remote source](/docs/realm/reunite/project/remote-content)
- (2) manage files and folders
- (3) browse, [eject, and customize theme components](/docs/realm/customization/eject-components/eject-components-in-reunite)


#### Search tab

Use the search tab to [lookup text or files in your project](/docs/realm/reunite/project/use-editor#search-in-files).

Screenshot of the Search tab in Reunite editor
In this tab you can:

- (1) expand or collapse the **Replace with** field
- (2) search file content
- (3) find files by name
- (4) filter search results by folder
- (5) toggle case matching
- (6) toggle whole word search
- (7) toggle regex search
- (8) replace all results


#### Commit tab

The commit tab lists all changes to files since the last commit.
Use this tab to commit changes, open pull requests, revert uncommitted changes to files, and view the commit history.

Screenshot of the Commit tab in Reunite editor
In this tab you can:

- (1) [commit latest changes to the current branch](/docs/realm/reunite/project/use-editor#commit-updates)
- (2) [create a pull request](/docs/realm/reunite/project/pull-request/open-pull-request)
- (3) [revert changes to selected files](/docs/realm/reunite/project/use-editor#revert-changes)
- (4) [view commit history relative to the main branch of the project](/docs/realm/reunite/project/use-editor#view-commit-history)


## Webview pane

Reunite editor's webview pane contains two tabs.
The **Webview** live preview tab displays the changes to your project in real time.
The **Docs** tab displays Realm documentation.

If you close a tab, you can reopen it by clicking the plus icon on the right side of the tabs.

### Webview live preview tab

The **Webview** live preview tab renders the currently open Markdown or API description file as it would appear in a published project.

Screenshot of the Webview tab in Reunite editor
- (1) [navigate to previously opened pages](/docs/realm/reunite/project/use-webview#navigate-pages)
- (2) [reload webview](/docs/realm/reunite/project/use-webview#reload)
- (3) view the slug to the file displayed in the webview
- (4) [switch the view between screen sizes](/docs/realm/reunite/project/use-webview#view-different-screen-sizes)
- (5) [open webview in a new browser window or tab](/docs/realm/reunite/project/use-webview#view-different-screen-sizes)
- (6) use the **More actions** menu to:
  - [fully restart webview](/docs/realm/reunite/project/use-webview#full-restart)
  - [disable automatic syncing of changes to files with webview live preview](/docs/realm/reunite/project/use-webview#disable-auto-sync)
- (7) display webview build validation errors
- (8) display the number of pages in the project
- (9) [view webview build logs](/docs/realm/reunite/project/use-webview#access-build-logs-in-the-webview-tab)


### Docs tab

The docs tab displays Realm documentation with full capabilities of a Redocly project.

Screenshot of the Docs tab in Reunite editor
In this tab you can:

- (1) [search the content](https://redocly.com/docs/end-user/use-search)
- (2) [navigate the pages](https://redocly.com/docs/end-user/navigate-project)
- (3) [change the color mode](https://redocly.com/docs/end-user/adjust-project#change-the-color-mode)
- (4) open the displayed page in a new window or tab
- (5) [interact with pages](https://redocly.com/docs/end-user/interact-with-pages)


## Resources

- **[Reunite](/docs/realm/reunite/reunite)** - Learn about Reunite's features
- **[Reunite user profile menu](/docs/realm/reunite/user-profile-menu)** - Step-by-step instructions setting up notifications, color mode, and a Git provider account
- **[Use the Webview](/docs/realm/reunite/project/use-webview)** - View live previews of your content changes while editing for immediate visual feedback
- **[Use the editor](/docs/realm/reunite/project/use-editor)** - Learn to edit content in Reunite's integrated editor with syntax highlighting and collaborative features