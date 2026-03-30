# Source: https://kreya.app/docs/release-notes/alpha.md

# Alpha Release Notes

## 1.19.1-alpha.2 (2026-03-12)

### Bug Fixes

* **UI:** add wordwrap context menu entry

***

## 1.19.1-alpha.1 (2026-03-12)

### Bug Fixes

* **CLI:** add --relative-to cli path resolution option
* **CLI:** add filename to the junit reporter
* **CLI:** automatically detect kreya projects in parent directories
* **CLI:** show correct default values in cli help
* **Core:** copy as kreyac option
* **gRPC:** improve fallback to v1alpha server reflection importer
* **Linux:** set webkit app id correctly
* **UI:** add delete all user variables quick action
* **UI:** add quick actions to open settings tabs and clear all cookies
* **UI:** add word wrap option

***

## 1.19.0-alpha.4 (2026-02-25)

### Bug Fixes

* **UI:** expand hidden operations if start adding node in operatin list
* **UI:** open operation history and collection related operations next to the selected tab
* **UI:** use correct node for context menu actions when using the context menu on a not-selected tab

***

## 1.19.0-alpha.3 (2026-02-24)

### Features

* **Auth:** add support for the oidc device code flow
* **Core:** add insomnia v5 importer
* **Core:** add menu entry to create new project
* **Core:** support session cookies
* **Core:** use device flow to login
* **GraphQL:** add auth options to graphql importers
* **GraphQL:** add graphql schema file importer
* **GraphQL:** add graphql schema url importer
* **GraphQL:** add inline variables option to GraphQL operations
* **GraphQL:** add inline variables quick action
* **GraphQL:** add minify body option to GraphQL operations
* **GraphQL:** add option to automatically create graphql schema importer
* **GraphQL:** enhance schema import and handling logic
* **GraphQL:** history support
* **GraphQL:** include graphql in project setup wizard
* **GraphQL:** support custom scalar types
* **GraphQL:** support directives
* **GraphQL:** support insomnia imports
* **GraphQL:** support postman import
* **UI:** add directory info
* **UI:** app tab actions
* **UI:** improve environment switcher
* **UI:** improve importer type selection
* **Windows:** sign Kreya executable in addition to MSI installer

### Bug Fixes

* **Core:** close websockets without exception if the server closes the connection
* **Core:** expire session cookies correctly, indicate session cookies in the details
* **Core:** fix a rare bug that resulted in an operation invocation failure
* **Core:** scrub long timestamps
* **Core:** show system credentials unsupported message correctly
* **gRPC:** elimate duplicated grpc headers response tab
* **gRPC:** show error detail message again
* **Importers:** do not store createMissingOperations if importer does not support it
* **Importers:** faster operation creation for large imports
* **Importers:** faster operation creation for large imports
* **Linux:** set WEBKIT*DISABLE*DMABUF\_RENDERER=1 by default to work around webkit issues
* **REST:** make multipart requests RFC 7578 compliant
* **UI:** adding a new operation with invisible selected node expands the node
* **UI:** allow context menu on 'No operations' label
* **UI:** correctly display the 'no operations' label
* **UI:** do handle esc correctly when context menu is open and do not trigger unknown key sound
* **UI:** do not display auth details if reset inherited is active
* **UI:** do not highlight a different operation node on rename to an existing name
* **UI:** fix shortcuts in quick actions
* **UI:** improve context menu locations
* **UI:** inline new gRPC and REST operation
* **UI:** mark sequenced shortcuts as handled correctly
* **UI:** prevent immediate autoclose of context menus on macos
* **UI:** prevent opening operations from invoker scripts that failed to load
* **UI:** show PDF previews correctly again

***

## 1.19.0-alpha.2 (2026-01-08)

### Features

* **GraphQL:** add scripting support
* **graphQL:** add subscription support
* **GraphQL:** graphql-ws support
* **graphQL:** initial graphql support
* **graphQL:** introspection importer
* **GraphQL:** response json path support
* **GraphQL:** review fixes
* **GraphQL:** snapshots support
* **GraphQL:** support har imports
* **GraphQL:** support sending operations via GET
* **Scripting:** allow simplified test result reporting

### Bug Fixes

* **Auth:** correctly abort authentication updates when it takes too long
* **Auth:** correctly save the 'Use discovery' state in all cases
* **Core:** cancel long running initialization tasks when invoking operation correctly
* **Core:** correctly parse cookies on curl import
* **Core:** fix keyboard navigation after renaming an operation
* **Core:** improve curl bash encoding
* **Core:** passing invalid project path resulted in being unable to close the window
* **GraphQL:** allow to send operations when introspecting the schema fails
* **GraphQL:** do not show undefined in path segment if no path is set
* **GraphQL:** in graphql introspection importer show clean invalid url error
* **GraphQL:** in new graphql introspection importer set empty endpoint
* **GraphQL:** new graphql operation should be sendable without error
* **gRPC:** correctly accept wrapper types as requests again
* **gRPC:** make empty request bodies in grpc web curl imports work correctly
* **UI:** autocomplete works with dashes in the suggestions
* **UI:** correctly show files when moving into similarly named directories
* **UI:** disable content type header for multipart requests
* **UI:** fixed moving an operation collection or invoker script inside a directory
* **UI:** prevent layout shifting in importer settings during tab switch
* **UI:** show confirm dialog after drag in operation list
* **UI:** show tab close button only on hover or if tab is active

***

## 1.19.0-alpha.1 (2025-10-13)

### Features

* **gRPC:** support v1 reflection in addition to v1alpha
* **UI:** recent projects are searchable

### Bug Fixes

* **Core:** allow to save REST responses and previews outside of project sandbox
* **Core:** handle edge cases during cancellation of running invocation
* **Core:** improve error handling when invoking operations
* **UI:** add escape key for trace message search
* **UI:** do not close context menus when scrolling
* **UI:** prevent UI shifting when selecting tabs in directory settings

***

## 1.18.0-alpha.11 (2025-09-26)

### Bug Fixes

* **UI:** do not remove proxy bypass entry when adding a new one with Enter

***

## 1.18.0-alpha.10 (2025-09-25)

### Features

* **Core:** show selected operation in invoker script screen
* **gRPC:** add status code to tracing message
* **gRPC:** inline gRPC method chooser UI
* **UI:** add operations tags in trace tab
* **UI:** show which tests belong to which operation in collections and scripts

### Bug Fixes

* **CLI:** improve summary output
* **Core:** improve tracing implementation
* **Scripting:** provide date.to\_string docs
* **Scripting:** show correct inlined parameter name in piped templated function calls
* **UI:** moving or renaming should not break quick actions

***

## 1.18.0-alpha.9 (2025-09-01)

### Features

* **Core:** add configuration to read product key from environment or file
* **Core:** allow to import multiples files at once, e.g. postman collections
* **Core:** extend collections with previews and traces
* **REST:** snapshots support
* **REST:** support OpenAPI 3.1
* **Scripting:** add scripting snapshot assertion api
* **UI:** add search in trace tab
* **WebSocket:** add snapshots support

### Bug Fixes

* **CLI:** correctly handle tests from Scripts
* **CLI:** improve error message when files at specified paths do not exist
* **CLI:** use stderr for error messages
* **Core:** correctly show Scripts and Collections as failed if operations or test fail
* **Core:** fixed bug where users were logged out when opening multiple Kreya instances
* **Core:** keep state when modifying collections
* **Core:** refresh previews automatically
* **Core:** show error message when saving an environment with duplicate JSON keys
* **gRPC:** correctly send large numbers when not quoted as a string
* **REST:** improve resulting project structure from OpenAPI import
* **Scripting:** ensure that the correct suggestions are displayed in the UI

***

## 1.18.0-alpha.8 (2025-07-07)

### Bug Fixes

* **gRPC:** handle incorrect server reflection implementations that do not specify proto dependencies
* **Linux:** correctly build snap

***

## 1.18.0-alpha.7 (2025-07-02)

### Bug Fixes

* **Windows:** upgrade WebView2 version

***

## 1.18.0-alpha.6 (2025-07-01)

### Bug Fixes

* **CI:** fix release

***

## 1.18.0-alpha.5 (2025-07-01)

### Features

* **Core:** add configurable proxy support
* **Core:** add snapshot testing
* **Core:** allow comments in environments
* **Linux:** upgrade to GTK4

### Bug Fixes

* **Linux:** native clipboard support

***

## 1.18.0-alpha.4 (2025-06-19)

### Features

* **Core:** create readme when creating a new project
* **Core:** macos dmg
* **Scripting:** add clear method to user variables
* **UI:** double click on operation collection entry opens operation

### Bug Fixes

* **Auth:** correctly apply the header prefix to static and OAuth2 authentications
* **Core:** correctly validate user variable contents when editing via UI
* **Core:** delete the operation script file if it is empty
* **Core:** handle rare error when operation finished
* **Core:** overwrite existing files when saving responses
* **UI:** add preview for advanced auth options
* **UI:** behaviour of a newly created user variable is fixed
* **UI:** fix theme switching, which failed sometimes before

***

## 1.18.0-alpha.3 (2025-05-23)

### Bug Fixes

* **Windows:** correctly handle edge cases on older Windows versions

***

## 1.18.0-alpha.2 (2025-05-22)

### Features

* **Auth:** add OAuth2/OIDC option to disable pushed authorization request
* **Core:** automatically track unexpected errors unless telemetry is disabled
* **Core:** unify entry point

### Bug Fixes

* **REST:** improve handling of formatted responses with invalid content
* **UI:** display scripting and sandbox exceptions as snackbar

***

## 1.18.0-alpha.1 (2025-05-07)

### Features

* **Core:** add scripting preview api

### Bug Fixes

* **Core:** use redirect URIs as is in authentications, do not modify them

***

## 1.17.0-alpha.17 (2025-04-30)

### Bug Fixes

* **CLI:** correctly bundle macos kreac cli dependencies
* **Core:** assign .krproj extension with Kreya application on macos

***

## 1.17.0-alpha.16 (2025-04-28)

### Bug Fixes

* **Core:** improve release process

***

## 1.17.0-alpha.15 (2025-04-28)

### Features

* **Core:** open imported sample operation after import
* **Core:** support async test hooks

### Bug Fixes

* **CLI:** add support for CLI response files (arguments provided in a file with the @-syntax)
* **CLI:** correctly include protoc
* **Core:** handle encoded curl cookies in curl parser
* **Core:** use correct hook type declarations for async scripting hooks
* **Core:** use correct name for imported curl operations
* **gRPC:** stream keyword was missing in the gRPC service declaration
* **UI:** stop autoscrolling when user scrolled manually
* **UI:** storing an empty user variable should remove it

***

## 1.17.0-alpha.14 (2025-04-24)

### Features

* **Core:** add file append scripting api
* **Core:** add file write scripting api
* **Core:** add option to use the native browser to authenticate
* **Core:** add read file scripting api
* **Core:** support async scripting hooks
* **Core:** support CommonJS npm packages in scripting
* **gRPC:** show proto files imported documentation in script editor autocompletion
* **REST:** add scripting content autocompletion

### Bug Fixes

* **CLI:** improve error message reporting
* **Core:** update chai testing library to 5.2.0
* **gRPC:** use correct types in gRPC response scripting autocomplete
* **UI:** improve json path/xpath response input

***

## 1.17.0-alpha.13 (2025-04-04)

### Features

* **Core:** add path scripting module
* **Core:** view operation results directy in scripts

### Bug Fixes

* **Core:** fix a rare crash on macos when authenticating with OIDC
* **Core:** use relative paths everywhere
* **UI:** save auth details when switching tabs

***

## 1.17.0-alpha.12 (2025-03-31)

### Features

* **Core:** add access to operation name in scripts
* **Core:** add script name to script api
* **Core:** support type resolution for relative script imports
* **UI:** add option to close tabs on the left and right

### Bug Fixes

* **Core:** fix postman import api key auth
* **Core:** store operation script correctly
* **UI:** abort collection running cleanly after a operation changed
* **UI:** add run importer button to importer settings
* **UI:** allow context menu click in empty space in the operation list
* **UI:** improve autocomplete and input suggestions filter and sort
* **UI:** show scrollbar in big context menus

***

## 1.17.0-alpha.11 (2025-03-21)

### Features

* **Core:** added Kreya Script to control operation invocation with JavaScript
* **Core:** support importing Postman v2.0.0 collections
* **UI:** add search for operations, directories and collections

### Bug Fixes

* **Core:** correctly handle arrays in Scripting
* **Core:** improve script type imports
* **UI:** increase panel resizer width
* **UI:** remove tab character when copy pasting key-value entries

***

## 1.17.0-alpha.10 (2025-03-04)

### Bug Fixes

* **Core:** fix release deployments

***

## 1.17.0-alpha.9 (2025-03-03)

### Bug Fixes

* **Core:** handle invalid directory characters in Postman and Insomnia imports correctly
* **gRPC:** show input/output types of other packages in proto declaration tab

***

## 1.17.0-alpha.8 (2025-02-20)

### Bug Fixes

* **Core:** fix Windows installer

***

## 1.17.0-alpha.7 (2025-02-14)

### Features

* **Core:** improve Windows installer to allow per-user installs

***

## 1.17.0-alpha.6 (2025-02-12)

### Features

* **Core:** support har file imports

***

## 1.17.0-alpha.5 (2025-02-12)

### Bug Fixes

* **Core:** add request Content-Type header in Postman importer if not already present
* **Core:** change kreya.trace Scripting function to accept all data types
* **Core:** correctly write Scripts of imported operations to separate files
* **Core:** do not show operation as sending when it was aborted due to Script errors
* **Core:** return undefined instead of null when getting a non-existent user variable in Scripting
* **Core:** save project settings before duplicating or renaming
* **UI:** improve Windows dark mode
* **UI:** show dates in user locale format

***

## 1.17.0-alpha.4 (2025-01-29)

### Features

* **Core:** export as curl
* **Core:** import cookies when importing curl commands
* **gRPC:** add option to copy grpc operations as curl commands to the clipboard
* **UI:** add copy operation path and open in file manager quick actions
* **UI:** add quick action to open the import dialog

***

## 1.17.0-alpha.3 (2025-01-24)

### Features

* **Core:** support unix sockets and named pipe transports
* **UI:** allow to resize/reposition quick actions overlay

### Bug Fixes

* **UI:** improve open operation search and allow to open collections
* **UI:** tab title is updated when a REST operation changes its method type

***

## 1.17.0-alpha.2 (2025-01-23)

### Bug Fixes

* **Core:** further improve Postman translations

***

## 1.17.0-alpha.1 (2025-01-22)

### Features

* **Core:** add jwt auth provider and option to set header value prefix
* **Core:** user variables editor
* **UI:** allow to add an environment via the environment switcher if none exists

### Bug Fixes

* **gRPC:** preselect the current grpc method when changing the method
* **REST:** correctly set multipart request content type and do not require one
* **UI:** improve shortcut responsiveness

***

## 1.16.0-alpha.8 (2025-01-16)

### Features

* **Core:** option to minify xml and json request bodies

### Bug Fixes

* **REST:** allow empty request paths

***

## 1.16.0-alpha.7 (2025-01-13)

### Features

* **Core:** add AWS signature version 4
* **Core:** automatically translate most of the Postman scripts during the import

### Bug Fixes

* **Core:** do not import authentications from Postman/Insomnia if they already exist
* **UI:** login state in status bar and operations is refreshed after login

***

## 1.16.0-alpha.6 (2025-01-09)

### Features

* **Core:** add cookie management

### Bug Fixes

* **Core:** cancel operation collection run when closing the tab
* **UI:** don't autoclose context menu just after open on some operating systems
* **UI:** reorder operation list after renaming an item

***

## 1.16.0-alpha.5 (2024-12-20)

### Bug Fixes

* **Core:** early Scripting messages did not show up when sending a collection in certain cases
* **gRPC:** correct type for gRPC repeated fields in Scripting
* **REST:** treat all status codes < 400 as successful
* **UI:** allow scrolling in project settings with many entries
* **UI:** show operation result state in collection header correctly

***

## 1.16.0-alpha.4 (2024-12-16)

### Features

* **Core:** add file exclusion list for gRPC proto file importers

### Bug Fixes

* **UI:** environment switcher in directory settings is more visible
* **UI:** improve quick action overlay contrast
* **UI:** increase debounce time for combined shortcuts

***

## 1.16.0-alpha.3 (2024-12-09)

### Bug Fixes

* **Core:** correctly display suggestions in non-JSON editors

***

## 1.16.0-alpha.2 (2024-12-06)

### Features

* **Core:** add faker to the Scripting API
* **UI:** add operation collection state filter
* **UI:** simplify operation creation workflow
* **UI:** update the look and feel of Kreya
* **WebSocket:** add support for WebSockets
* **WebSocket:** support importing WebSocket requests from Insomnia

### Bug Fixes

* **Core:** better error message when a path is outside of the project directory
* **Core:** correctly invalidate importer cache in some cases
* **Core:** do not show failed message for resolving scripting modules when none are present
* **Core:** fix duplicated entries when searching operations
* **Core:** limit time for background tasks to exit when closing the app
* **Core:** parse server timing duration correctly
* **Core:** postman importer: read request type from Content-Type header as fallback
* **REST:** do not render empty response
* **UI:** entering a full path with endpoint is now possible for REST operations

***

## 1.16.0-alpha.1 (2024-11-11)

### Features

* **Core:** add custom headers for gRPC server reflection and OpenAPI URL importers
* **Core:** improve grpc any handling for unknown types
* **Core:** send auth configs as query param or with other header names
* **REST:** autocomplete well-known REST headers
* **UI:** show running operations and collections in the operation list

### Bug Fixes

* **Core:** certificates with key and cert file were invalid on MacOS 15
* **UI:** made tab switching shortcuts visible and add different shortcut for MacOS
* **UI:** show an unique tab name for operations and directories with same name

***

## 1.15.1-alpha.1 (2024-06-21)

### Bug Fixes

* **Core:** ask to save unsaved changes before exiting
* **Core:** do not crash when closing immediately after opening
* **gRPC:** add support for some well known google protobuf types again

***

## 1.15.0-alpha.3 (2024-06-12)

### Features

* **gRPC:** support protobuf edition 2023 and proto2

### Bug Fixes

* **Core:** add protoc dependecies to macos app build
* **UI:** add only button for check box groups

***

## 1.15.0-alpha.2 (2024-05-29)

### Bug Fixes

* **REST:** rest operation with multipart body was not rendered
* **REST:** saving a raw response failed if destination file already existed

***

## 1.15.0-alpha.1 (2024-05-16)

### Features

* **gRPC:** show comments in declaration when imported from proto files
* **UI:** show project, operation, directory and collection paths

### Bug Fixes

* **Core:** handle invalid refresh token during authentication
* **Core:** purge selected caches correctly and remove cache purger preselection
* **Core:** recognize templated endpoints during Postman and Insomnia imports
* **Core:** renew Windows code signing certificate
* **gRPC:** correctly terminate operation on timeout when sending requests manually
* **REST:** automatically encode path param values

***

## 1.14.1-alpha.1 (2024-04-19)

### Bug Fixes

* **Core:** upgrade scriban to include new template helpers

***

## 1.14.0-alpha.6 (2024-04-17)

### Bug Fixes

* **UI:** operation state icons cut off fixed

***

## 1.14.0-alpha.5 (2024-04-12)

### Features

* **Core:** allow to filter test results
* **UI:** add filter for trace messages

### Bug Fixes

* **UI:** perform operation rename etc. on blur instead of cancelling

***

## 1.14.0-alpha.4 (2024-04-10)

### Features

* **CLI:** add junit reporter
* **Core:** add Insomnia project importer
* **Core:** improve rest error handling and display correct errors
* **Core:** show merged environment and import system environment variables

### Bug Fixes

* **Core:** allow to open project containing read only files
* **Core:** collections should continue running if an operation fails to load
* **Core:** improve operation collection ui
* **UI:** empty metadata, headers and query params are not stored in directory settings
* **UI:** improved button visibility
* **UI:** show correct message in quick actions when no actions are available
* **UI:** show status messages for concurrent invocations and collections

***

## 1.14.0-alpha.3 (2024-03-13)

### Features

* **CLI:** allow to invoke multiple collections in the CLI
* **UI:** add operations to collection via drag and drop
* **UI:** added context menu entry to open items in file manager

### Bug Fixes

* **CLI:** add fallback console where colorful terminal is not supported
* **Core:** move and rename operation update relative paths correctly
* **Core:** stop long running Scripting tasks when cancelling
* **UI:** correctly show add operation popup in collection on button click
* **UI:** do not show empty window title
* **UI:** improve typography and higher contrast for light theme buttons
* **UI:** improve welcome screen on lower screen widths
* **UI:** show error when entering invalid file name during rename

***

## 1.14.0-alpha.2 (2024-02-27)

### Bug Fixes

* **Core:** upgrade dependencies

***

## 1.14.0-alpha.1 (2024-02-27)

### Features

* **Core:** add sleep in scripting
* **Core:** environment access in scripting
* **Core:** run directories as collection
* **Core:** templating environment name access

### Bug Fixes

* **Core:** replace invalid file name characters during postman collection import
* **REST:** apply Scriban template to REST endpoint and path before replacing path params
* **REST:** parse custom content types correctly"
* **UI:** do not override monaco editor shortcuts
* **UI:** improve operation search
* **UI:** selecting text when renaming nodes now works

***

## 1.13.1-alpha.3 (2024-02-12)

### Bug Fixes

* **gRPC:** better error message for invalid endpoint schemes

***

## 1.13.1-alpha.2 (2024-02-09)

### Bug Fixes

* **Core:** correctly display open source licenses again

***

## 1.13.1-alpha.1 (2024-02-09)

### Bug Fixes

* **UI:** correctly account for monitors with different DPI
* **UI:** ensure that UI panels resize properly
* **UI:** optimize operation search threshold for a better result

***

## 1.13.0-alpha.8 (2024-01-29)

### Bug Fixes

* **Core:** fix macOS auto update

***

## 1.13.0-alpha.7 (2024-01-29)

### Bug Fixes

* **Core:** macOS update installer

***

## 1.13.0-alpha.6 (2024-01-29)

### Bug Fixes

* **Core:** correctly move macOS data to new storage location

***

## 1.13.0-alpha.5 (2024-01-29)

### Bug Fixes

* **Core:** make auto-updater work on macos and linux for paths with spaces

***

## 1.13.0-alpha.4 (2024-01-26)

### Bug Fixes

* **Core:** release 1.13

***

## 1.13.0-alpha.3 (2024-01-26)

### Bug Fixes

* **Core:** move Kreya data files to new location on macOS

***

## 1.13.0-alpha.2 (2024-01-26)

### Features

* **CLI:** add collection invoke command to CLI

***

## 1.13.0-alpha.1 (2024-01-15)

### Features

* **CLI:** add create project command
* **Core:** add Postman importer
* **Core:** operation collections
* **gRPC:** add declaration tab to show proto declaration of a grpc method
* **gRPC:** resolve file descriptor set well known types automatically
* **gRPC:** show request comments when imported from a file descriptor set with included source info
* **REST:** show trace message when redirection occurs

### Bug Fixes

* **CLI:** allow absolute operation paths to be invoked
* **Core:** correctly open projects with spaces in their name via CLI arguments
* **Core:** correctly support proxies with authentication
* **Core:** don't cache auth state when using scripting variables
* **Core:** fixes jwt profile authentication when invoked multiple times in a short period
* **Core:** improve stability on macOS
* **Core:** show errors during refresh flow correctly
* **REST:** add authorization header for importer api
* **UI:** add renaming shortcut and add shortcut information to context menus
* **UI:** multiple responses sometimes not expanded
* **UI:** remove method not imported toast
* **UI:** show operation type hint for open operation quick action

***

## 1.12.0-alpha.4 (2023-11-06)

### Bug Fixes

* **UI:** center Kreya on first launch on macOS

***

## 1.12.0-alpha.3 (2023-11-03)

### Features

* **REST:** support HTTP/3
* **UI:** remember last window size and position

### Bug Fixes

* **REST:** adjust relative file paths when moving or duplicating REST operations
* **UI:** enable mouse wheel zoom for request and reponse view

***

## 1.12.0-alpha.2 (2023-10-26)

### Features

* **Core:** directories can now be duplicated with the context menu, quick action and copy paste
* **Core:** windows ARM64 support
* **UI:** add keyboard shortcuts for operation list

***

## 1.12.0-alpha.1 (2023-10-17)

### Features

* **Core:** add resolve unimported operations dialog after import run
* **Core:** adding nested operations is now possible
* **Core:** inherited headers, query params and metadata can be ignored
* **Core:** visualize operation and server timing
* **REST:** add option to disable ssl server certificate validation for open api url importer
* **REST:** add option to specify the http version to use
* **REST:** show partial text responses
* **REST:** support new-line delimited streamed JSON
* **REST:** support new-line delimited streamed xml
* **REST:** support server sent events
* **UI:** added drag and drop to rearrange tabs
* **UI:** multiple operations and directories can be selected
* **UI:** use virtual scrolling to handle large amount of gRPC responses

### Bug Fixes

* **Core:** correctly handle environment files modified by other processes
* **Core:** correctly update operation tree after file system directory changes
* **Core:** dont fail to import when a prefix directory, but no project subdirectory is defined
* **Core:** resolved bugs in operation search result highlighting
* **gRPC:** do not create server reflection import operations automatically
* **gRPC:** do not fail on very large responses
* **UI:** alignment of gRPC operation icon
* **UI:** change operation duplication to inline
* **UI:** expand directories on drag and drop
* **UI:** gRPC method edit button is visible for long method names
* **UI:** indentation of directories and operations in operation list
* **UI:** inline auth token update button and login button spinner layout
* **UI:** larger max width for toasts
* **UI:** test results layout
* **UI:** theme switcher label
* **UI:** toast background in light theme is not dark

***

## 1.11.1-alpha.1 (2023-08-23)

### Bug Fixes

* **Core:** correctly load dependencies to prevent crashes on startup for new MacOS installations

***

## 1.11.0-alpha.3 (2023-08-17)

### Bug Fixes

* **Core:** correct windows installation path

***

## 1.11.0-alpha.2 (2023-08-17)

### Features

* **Core:** build linux arm
* **Core:** linux arm snapcraft support
* **UI:** add possibility to duplicate importers

### Bug Fixes

* **CLI:** make browser authentication cancellable
* **CLI:** make environment configurations work
* **CLI:** only run required importers when invoking operations via cli
* **CLI:** show detailed messages
* **UI:** fix Windows DPI issues

***

## 1.11.0-alpha.1 (2023-07-19)

### Features

* add possibility to show messages to kreya users
* **Core:** add option to purge user variables
* **Core:** add tour for new users

### Bug Fixes

* **CLI:** load scripting dependency correctly in docker kreyac
* **Core:** about window can now be opened during fullscreen on macos
* **Core:** correctly reevaluate inherited, templated operation settings
* **Core:** delete of operations and directories with unsaved changes
* **Core:** do not try to store relative paths for resources on a different drive
* **Core:** improve Windows installer and WebView2 detection
* **Core:** resolve scripting type definitions correctly when switching operation tabs
* **Core:** show error details in the ui for well known exceptions
* improve welcome screen with quick links and tips
* **UI:** changed history shortcut to primary+shift+h
* **UI:** correctly handle shortcuts when switching tabs
* **UI:** improvments of dialog buttons
* **UI:** inherited rest path params placeholders are now visible on operation load
* **UI:** new folders and renaming operation indentations fixed
* **UI:** renamed delete action for directories
* **UI:** renaming folders with dots
* **UI:** select directories and operations on right click
* **UI:** show quick actions if no tab is open
* **UI:** update welcome screen message based on user subscription

***

### 1.10.1-alpha.2 (2023-03-23)

### Bug Fixes

* **Core:** add removable-media snapcraft plug
* **Core:** correctly handle operation invocation failures
* **Core:** oauth refresh token support
* **Core:** specify correct linux dependency versions
* **gRPC:** response time could be delayed up to 3s
* **UI:** type hint vertical alignment to center

***

### 1.10.1-alpha.1 (2023-03-02)

### Bug Fixes

* **Core:** fix account login on snapcraft linux installations
* **Core:** macOS icon size and add corner radius

***

## 1.10.0-alpha.5 (2023-02-28)

### Bug Fixes

* **UI:** fix scrollbar issues in REST settings

***

## 1.10.0-alpha.4 (2023-02-27)

### Bug Fixes

* **Core:** curl clipboard importer use post http method if any data flag is set
* **Core:** save changes when another tab is opened

***

## 1.10.0-alpha.3 (2023-02-14)

### Features

* **Core:** add history for operations
* **Core:** add option to reset inherited auth to none
* **Core:** add option to reset inherited client certificate to none
* **Core:** add option to trim prefix when creating operations from importers
* **Core:** add static authorization header value provider
* **Core:** allow simultaneous invocation of operations
* **gRPC:** add option to export response to file
* **gRPC:** import grpcurl commands from clipboard
* **gRPC:** option to add authorization to server reflection importers
* **REST:** add option to export response to file
* **REST:** option to add authorization to openapi importers
* **REST:** path variables
* **UI:** add tabs for open operations
* **UI:** improved new project wizard
* **UI:** keyboard navigation in operation list

### Bug Fixes

* **Core:** correctly open project when an absolute path is provided
* **Core:** enhance debug infos in about window
* **Core:** if one importer fails, other importers should still run
* **UI:** improve open operation fuzzy search

***

## 1.10.0-alpha.2 (2023-01-05)

### Features

* **Core:** rework 'reset requests' to 'reset operation'
* **REST:** add response preview for HTML and SVG

### Bug Fixes

* **UI:** fix blank screen on older macos versions

***

## 1.10.0-alpha.1 (2022-12-21)

### Bug Fixes

* **Core:** correctly apply default settings for environments
* **Core:** merge environment data and user data correctly
* **Core:** resolve blank screen bug
* **gRPC:** do not share imported information between import streams
* **gRPC:** remove default gRPC user agent
* **UI:** disable tooltip interactivity

***

## 1.9.0-alpha.4 (2022-11-04)

### Bug Fixes

* **gRPC:** parse protobuf files correctly

***

## 1.9.0-alpha.3 (2022-11-03)

### Bug Fixes

* **Core:** fix crashes on macos 13

***

## 1.9.0-alpha.2 (2022-10-27)

### Features

* **Core:** add variable support for scripting and templating

### Bug Fixes

* **Core:** random crashes on macos

***

## 1.9.0-alpha.1 (2022-10-13)

### Features

* **gRPC:** import grpc web operations via curl commands
* **REST:** import rest operations via curl commands

### Bug Fixes

* **grpc:** allow creation of operation if a grpc service only contains one rpc
* remove deprecated environment entries from templating suggestions
* remove empty key value entries on save
* **REST:** do not set a JSON schema for operations without a request definition
* **REST:** match suffixed media types correctly
* show whitespace in inherited headers

***

### 1.8.1-alpha.2 (2022-08-12)

### Bug Fixes

* correctly refresh auth details when changing the active environment
* **gRPC:** remove default timeout of 100s

***

### 1.8.1-alpha.1 (2022-08-05)

### Bug Fixes

* make response headers and trailers selectable
* show a nice error message when an URL does not contain a scheme
* some external links opened twice

***

## 1.8.0-alpha.9 (2022-07-11)

### Features

* improve sample value generator by using suffix matching and better synonyms

### Bug Fixes

* **scripting:** ignore reflection types and ignore ambigous methods

***

## 1.8.0-alpha.8 (2022-06-24)

### Bug Fixes

* telemetry app started fix version property naming

***

## 1.8.0-alpha.7 (2022-06-24)

### Bug Fixes

* scripting docs link

***

## 1.8.0-alpha.6 (2022-06-23)

### Features

* add kreya customer account login
* add option to decode access token claims
* **gRPC:** support binary request metadata
* **REST:** example content should use templated expressions where appropriate
* status bar to show tasks in progress
* use open api example values if possible
* use random sample values

### Bug Fixes

* **auth:** use correct openid options and allow ignored additional params
* rename an operation also rename the js script
* **REST:** add Content-Type header to newly created operations
* **rest:** correct operation name generation for root paths
* **REST:** do not reset Content-Type when opening an operation
* **REST:** handle OpenAPI importer edge cases
* **REST:** map application/hal+json to JSON response type
* **Scripting:** handle headers and trailers with same keys

***

## 1.8.0-alpha.5 (2022-04-28)

### Features

* generate REST example requests and json schema

### Bug Fixes

* bugfix for moving a newly created directory
* copy debug infos tooltip covered button
* response text is now copyable
* **rest:** adjust type hint colors
* **rest:** automatically detect mime type from file extension
* **rest:** improve visibility of optional rest operation
* **rest:** limit rest response viewer to 30 mb
* **rest:** remove default timeout

***

## 1.8.0-alpha.4 (2022-03-25)

### Bug Fixes

* **rest:** rest data directory improvements

***

## 1.8.0-alpha.3 (2022-03-24)

### Bug Fixes

* autoupdate

***

## 1.8.0-alpha.2 (2022-03-23)

### Bug Fixes

* show error dialog when a file descriptor set cannot be found in a proto file set importer

***

## 1.8.0-alpha.1 (2022-03-23)

### Features

* add purge caches option
* add support for REST
* gRPC deadline support
* macOS arm build
* option to create missing operations in importers in a subdirectory of the project
* scripting support
* select first environment automatically if none is selected
* system credentials auth provider

### Bug Fixes

* add tabs overflow support
* build scriban documentation correctly if references are used
* do not encode non-ascii characters in JSON where applicable
* handle grpc-status-details-bin header correctly in all circumstances
* hide certificate selector at the project setup dialog
* improve file watchers when many file system events happen at once
* inconsistent protobuf imports caused importers to fail
* key value editor improvements
* **Linux:** fixed rare exception on startup
* render ui even if initialization fails to display errors
* shortcuts could be registered and executed multiple times
* show an error message box if Kreya fails to start
* **Tracing:** match trace messages to operation invocations

***

## 1.7.0-alpha.6 (2021-11-09)

### Features

* add what's new page to the snackbar after update

***

## 1.7.0-alpha.5 (2021-11-02)

### Bug Fixes

* deleting an operation caused errors when invoking other operations

***

## 1.7.0-alpha.4 (2021-10-29)

### Features

* add light mode and an option to switch between color themes

### Bug Fixes

* trace log timestamps should show timestamps in local time instead of utc

***

## 1.7.0-alpha.3 (2021-10-22)

### Features

* make auth configurations available through scriban templating

### Bug Fixes

* add quick actions to send requests manually
* display trace messages correctly if an auth provider is used
* display unknown grpc status correctly
* load suggestion icons correctly
* suggestions from environment should override scriban api's provided by kreya

***

## 1.7.0-alpha.2 (2021-10-19)

### Features

* show environment variable content in templated expressions on mouse hover
* show function signature information for scriban function calls in the request editor
* show parameter type hints in scriban function calls

### Bug Fixes

* improve suggestions ui in settings
* improve UX for running importers

***

## 1.7.0-alpha.1 (2021-10-14)

### Features

* add faker data to be accessible via scriban templates
* add templating parameter hints
* cache importer results for much better performance

### Bug Fixes

* fixed a bug where importing and generating example messages for the Google API didn't work
* free ressources correctly after app termination
* improve error messages and error reporting

***

## 1.6.0-alpha.6 (2021-09-10)

### Features

* add setting for max gRPC message size and remove default limit

### Bug Fixes

* correctly display scrollbars when many requests or responses are present

***

## 1.6.0-alpha.5 (2021-09-09)

### Bug Fixes

* improve auto updater

***

## 1.6.0-alpha.4 (2021-09-09)

### Bug Fixes

* layout editor suggestions correctly

***

## 1.6.0-alpha.3 (2021-09-08)

### Bug Fixes

* do not show errors for trailing commas and comments in json requests

***

## 1.6.0-alpha.2 (2021-09-07)

### Features

* support all well known types in Any messages

### Bug Fixes

* switch complete button to cancel button when client streaming request was manually completed

***

## 1.6.0-alpha.1 (2021-09-02)

### Features

* new file descriptor set importer
* add project initial setup and example project
* support system environment variables in some paths

### Bug Fixes

* allow trailing commas in request json
* be more foregiveable if an imported proto contains errors

***

## 1.5.0-alpha.6 (2021-07-08)

### Bug Fixes

* handle service errors correctly when sending requests one by one
* resolve strange ui behavior when adding a request

***

## 1.5.0-alpha.5 (2021-07-07)

### Bug Fixes

* refresh request view correctly when first request is deleted

***

## 1.5.0-alpha.4 (2021-07-07)

### Bug Fixes

* scroll requests into view after creation

***

## 1.5.0-alpha.3 (2021-07-06)

### Features

* add operation menu entry to overwrite the requests of an operation
* add proto3 optional support

### Bug Fixes

* handle responses with invalid struct values
* improve ui if there are lots of requests/responses
* load proto dependencies correctly in server reflection importer
* resolve duplicate app infos error on startup

***

## 1.5.0-alpha.2 (2021-06-09)

### Features

* register .krproj file extension with Kreya for windows

### Bug Fixes

* allow comments in request json
* improve autocomplete selection for create and change operation

***

## 1.5.0-alpha.1 (2021-05-12)

### Features

* operation list-, request- and response-view are now resizable

### Bug Fixes

* enable high DPI support on windows
* prevent a crash when the file watchers cannot be registered

***

## 1.4.0-alpha.7 (2021-04-30)

### Bug Fixes

* sign windows MSI

***

## 1.4.0-alpha.6 (2021-04-29)

### Bug Fixes

* abort the request as soon as the external auth window is opened
* add trace log for cancelling a request
* don't allow to send a request for unsupported operation types
* dont allow duplicated names for operations, directories and setting entries
* select created importer after save
* show exception details if a template runtime exception occured
* templated expressions in grpc operation metadata should evaluate before each call

***

## 1.4.0-alpha.5 (2021-04-27)

### Features

* add client tls certificates

### Bug Fixes

* fixes a crash on macos when \~/.config does not exist

***

## 1.4.0-alpha.4 (2021-04-23)

### Features

* add telemetry and telemetry opt-out option
* changing grpc method within operation

### Bug Fixes

* invalid endpoint doesn't abort the request
* nest open operation under an open operation quick action
* set release channel after version update

***

## 1.4.0-alpha.3 (2021-04-20)

### Features

* duplicate environments and authentications
* support paths in grpc endpoints

### Bug Fixes

* changing the type of an existing importer didn't work
* ensure environment data is valid json

***

## 1.4.0-alpha.2 (2021-04-14)

### Bug Fixes

* correctly serialize int64, sfixed64 and sint64 values
* improve grpc error logging

***

## 1.4.0-alpha.1 (2021-04-14)

### Features

* add option to send streamed requests one by one

### Bug Fixes

* improve error handling for oidc authentications

***

### 1.3.1-alpha.2 (2021-04-12)

### Bug Fixes

* autocomplete should not consume backdrop pointer events
* don't try to show an autocomplete suggestions overlay if there aren't any suggestions
* unsaved changes dialog in settings should not appear on delete

***

### 1.3.1-alpha.1 (2021-04-09)

### Bug Fixes

* fixes a weird bug which prevented saving an environment under certain conditions

***

## 1.3.0-alpha.6 (2021-04-09)

### Bug Fixes

* menu help

***

## 1.3.0-alpha.5 (2021-04-07)

### Features

* option to disable TLS/SSL validation on grpc server reflection importers

### Bug Fixes

* improve the save/cancel behaviour in the settings
* store operation content correctly after duplicating or moving it

***

## 1.3.0-alpha.4 (2021-04-01)

### Bug Fixes

* immediately remove directory from the ui on delete
* improve file watchers

***

## 1.3.0-alpha.3 (2021-03-26)

### Bug Fixes

* delete operations with unsaved changes correctly
* only save operations when changes were made
* operations created by importers don't show up immediately

***

## 1.3.0-alpha.2 (2021-03-25)

### Features

* specify default settings on directory levels

### Bug Fixes

* autocomplete replace selected text
* calling a non-grpc host fails
* hide no operation msg on initial folder creation
* key manager active item reference cleanup on item changes
* operation and directory selection after manual create
* remove directory from operation list after manual delete

***

## 1.3.0-alpha.1 (2021-03-15)

### Features

* add OpenID-Connect / OAuth2.0 client credentials and password grant types support
* open recent project via quick action
* open recent projects via menu
* option to disable TLS/SSL validation
* show response count in response tab
* store latest response

### Bug Fixes

* fuzzy search to open an operation via quick actions
* improve handling of operations with a referenced method which is not imported
* rename authorization configurations to authentications

***

### 1.2.1-alpha.1 (2021-02-24)

### Bug Fixes

* creation of an importer failed

***

## 1.2.0-alpha.3 (2021-02-24)

### Bug Fixes

* encode and decode repeated wrapper values correctly
* store relative paths with forward slashes in project files

***

## 1.2.0-alpha.2 (2021-02-18)

### Features

* option to create all possible operations from importer
* response json path support

### Bug Fixes

* handle oidc auth without a client secret correctly
* show error message when oidc discovery document fails to load

***

## 1.2.0-alpha.1 (2021-02-17)

### Features

* delete operation quick action
* duplicate operation via context menu and quick action
* decode rich errors (status.proto)
* serialize enums as names
* support unknown any types in responses
* support for the well known type field mask

### Bug Fixes

* allow creation of grpc requests for services without a package
* validate well known type NullValue correctly

***

## 1.1.0-alpha.5 (2021-02-06)

### Bug Fixes

* truncate response status detail instead of overflowing

***

## 1.1.0-alpha.4 (2021-02-06)

### Features

* **linux:** add snapcraft

### Bug Fixes

* simplify menu
* use the correct release channel of the binary
* **linux:** lowercase executable name

***

## 1.1.0-alpha.3 (2021-02-04)

### Features

* show changelog link on update

### Bug Fixes

* **windows:** also apply custom scrollbar style in modals

***

## 1.1.0-alpha.2 (2021-02-02)

### Bug Fixes

* catch exception when update loop gets cancelled

***

## 1.1.0-alpha.1 (2021-02-02)

### Features

* linux support

***

## 1.0.1-alpha.3 (2021-01-26)

### Bug Fixes

* **macos:** updates should update .app

***

## 1.0.1-alpha.2 (2021-01-26)

### Bug Fixes

* **macos:** blurry font
* **macos:** bundle ci macos

***

## 1.0.1-alpha.1 (2021-01-25)

### Bug Fixes

* **macos:** blurry font

***

## 1.0.0-alpha.16 (2021-01-18)

Update some dependencies

***

## 1.0.0-alpha.15 (2021-01-18)

### Bug Fixes

* show WebView2 installer progress during windows install
* disallow invalid scriban variable names in environment json schema
* environments in quick-actions weren't refreshed
* metadata editor suggestions
* update operation when metadata item is edited
* **grpc-json-schema:** fix oneofs in json schema
* **recent-projects:** disable typeahead while creating project

### Features

* calculate windows & macos bundle checksum
* timing stats

***

## 1.0.0-alpha.14 (2021-01-13)

### Bug Fixes

* add details button to expected errors, if there are more infos
* input suggestion autocomplete trigger
* **filewatcher:** ignore events of ignored files
* **grpc:** handle call completed correctly
* **ui:** request hover height should not change

### Features

* **auth:** allow oidc custom params
* **grpc:** grpc web support
* **operations:** move oeprations
* **ui:** operation list collapse / expand all buttons

***

## 1.0.0-alpha.13 (2021-01-11)

### Bug Fixes

* **spidereye:** upgrade

***

## 1.0.0-alpha.12 (2021-01-08)

### Bug Fixes

* **auth:** read options only if needed
* **json-editor:** indent with 2 spaces

***

## 1.0.0-alpha.11 (2021-01-08)

### Bug Fixes

* **about-screen:** add copy debug info button
* **auth:** allow google service account auth, also fixes suggestion builder json deserialization
* **auth:** try to fix a random crash on macos when an auth window is closed
* **grpc:** grpc operation icon tooltip
* **invokers:** don't throw if an invoker to be canceled doesn't exists anymore
* **launch-screen:** improve launch screen
* **suggestions:** improve ux
* open project correctly after creation
* **ui:** add tooltips for icon-only buttons, where the functionality may not be obvious

### Features

* **auth:** add google service account auth
* show update-ready notification
* **importers:** manually run importers
* **proto-importer:** discover proto files

***

## 1.0.0-alpha.10 (2021-01-06)

### Bug Fixes

* improve publish size

***

## 1.0.0-alpha.9 (2021-01-05)

### Bug Fixes

* user agent for http client
* **launch-window:** fix double click error

### Features

* handle expected expections differently

***

## 1.0.0-alpha.8 (2020-12-23)

### Bug Fixes

* **auto-updater:** run updater on exit via menu

***

## 1.0.0-alpha.7 (2020-12-23)

### Bug Fixes

* set correct windows auto update arguments

***

## 1.0.0-alpha.6 (2020-12-23)

### Bug Fixes

* **grpc:** correct json schema for value well known type

***

## 1.0.0-alpha.5 (2020-12-23)

### Bug Fixes

* correctly invoke windows msi during auto-update
* input suggestion autocomplete scroll

### Features

* filewatchers
* server reflection importer
* **autocomplete:** add environment autocomplete

***

## 1.0.0-alpha.4 (2020-12-22)

### Bug Fixes

* update dependencies

***

## 1.0.0-alpha.3 (2020-12-15)

### Bug Fixes

* correctly package windows version

***

## 1.0.0-alpha.2 (2020-12-15)

### Bug Fixes

* Release pipeline

***

## 1.0.0-alpha.1 (2020-12-15)

Initial release

***
