# Source: https://kreya.app/docs/release-notes.md

# Release Notes

Make sure to also check out our what's new [blogposts](/blog.md)!

## 1.19.1 (2026-03-13)

### Features

* **CLI:** add --relative-to CLI path resolution option
* **CLI:** add filename to the JUnit reporter
* **CLI:** automatically detect Kreya projects in parent directories
* **Core:** copy as kreyac option
* **UI:** add delete all user variables quick action
* **UI:** add quick actions to open settings tabs and clear all cookies
* **UI:** add word wrap option

### Bug Fixes

* **CLI:** show correct default values in CLI help
* **gRPC:** improve fallback to v1alpha server reflection importer
* **Linux:** set webkit app id correctly

***

## 1.19.0 (2026-02-25)

### Features

* **Auth:** add support for the oidc device code flow
* **Core:** add insomnia v5 importer
* **Core:** add menu entry to create new project
* **Core:** support session cookies
* **GraphQL:** Initial GraphQL (query, subscriptions, mutations) support including schema importers (file, url and reflection), auth, templating, scripting, subscriptions via SSE and websockets, history, snapshot testing, sending queries via GET, and many more
* **gRPC:** support v1 reflection in addition to v1alpha
* **Scripting:** allow simplified test result reporting
* **UI:** add directory infos
* **UI:** app operation actions
* **UI:** improve environment switcher
* **UI:** improve importer type selection
* **UI:** recent projects are searchable
* **Windows:** sign Kreya executable in addition to MSI installer
* **UI:** show confirm dialog after drag in operation list

### Bug Fixes

* **Auth:** correctly abort authentication updates when it takes too long
* **Auth:** oidc: correctly save the 'Use discovery' state in all cases
* **Core:** allow to save REST responses and previews outside of project sandbox
* **Core:** cancel long running initialization tasks when invoking operation correctly
* **Core:** close websockets without exception if the server closes the connection
* **Core:** correctly parse cookies on curl import
* **Core:** fix a rare bug that resulted in an operation invocation failure
* **Core:** fix keyboard navigation after renaming an operation
* **Core:** handle edge cases during cancellation of running invocation
* **Core:** improve curl bash encoding
* **Core:** improve error handling when invoking operations
* **Core:** passing invalid project path resulted in being unable to close the window
* **Core:** snapshot testing: scrub long timestamps
* **Core:** show system credentials unsupported message correctly
* **gRPC:** correctly accept wrapper types as requests again
* **gRPC:** make empty request bodies in grpc web curl imports work correctly
* **gRPC:** show error detail message again
* **Importers:** do not store createMissingOperations if importer does not support it
* **Importers:** faster operation creation for large imports
* **Linux:** set WEBKIT*DISABLE*DMABUF\_RENDERER=1 by default to work around webkit issues
* **REST:** make multipart requests RFC 7578 compliant
* **UI:** add escape key support for trace message search
* **UI:** adding a new operation with invisible selected node expands the node
* **UI:** allow context menu on 'No operations' label
* **UI:** autocomplete works with dashes in the suggestions
* **UI:** correctly display the 'no operations' label
* **UI:** correctly show files when moving into similarly named directories
* **UI:** disable content type header for multipart requests
* **UI:** do handle esc correctly when context menu is open and do not trigger unknown key sound
* **UI:** do not close context menus when scrolling
* **UI:** do not display auth details if reset inherited is active
* **UI:** do not highlight a different operation node on rename to an existing name
* **UI:** expand hidden operations if start adding node in operation list
* **UI:** fix shortcuts display in quick actions
* **UI:** fixed moving an operation collection or invoker script inside a directory
* **UI:** improve context menu positioning
* **UI:** inline new operation creation
* **UI:** mark sequenced shortcuts as handled correctly
* **UI:** open operation history and collection related operations next to the selected tab
* **UI:** prevent immediate autoclosure of context menus on macos
* **UI:** prevent layout shifting in importer settings during tab switch
* **UI:** prevent opening operations from invoker scripts that failed to load
* **UI:** prevent UI shifting when selecting tabs in directory settings
* **UI:** show PDF previews correctly again
* **UI:** show tab close button only on hover or if tab is active
* **UI:** use correct node for context menu actions when using the context menu on a not-selected tab

***

## 1.18.0 (2025-09-26)

### Features

* **Core:** add scripting preview api
* **Core:** add snapshot testing
* **Core:** add configurable proxy support
* **Core:** add configuration to read product key from environment or file
* **Core:** allow comments in environments
* **Core:** allow to import multiples files at once, e.g. postman collections
* **Core:** macos dmg installer
* **Core:** show selected operation in invoker script screen
* **gRPC:** add status code to tracing message
* **REST:** support OpenAPI 3.1
* **Linux:** upgrade to GTK4
* **Scripting:** unify scripting entry point (`kreya.rest` instead of `kreyaRest`)
* **Scripting:** add clear method to user variables
* **Scripting:** add scripting snapshot assertion api
* **UI:** inline gRPC method chooser
* **UI:** add operations tags in trace tab
* **UI:** add search in trace tab
* **UI:** double click on operation collection entry opens operation
* **UI:** show which tests belong to which operation in collections and scripts
* **Auth:** add OAuth2/OIDC option to disable pushed authorization request

### Bug Fixes

* **Auth:** correctly apply the header prefix to static and OAuth2 authentications
* **Auth:** use redirect URIs as is in authentications, do not modify them
* **CLI:** improve error message when files at specified paths do not exist
* **CLI:** improve summary output
* **CLI:** use stderr for error messages
* **Core:** correctly show Scripts and Collections as failed if operations or test fail
* **Core:** correctly validate user variable contents when editing via UI
* **Core:** delete the operation script file if it is empty
* **Core:** fixed bug where users were logged out when opening multiple Kreya instances
* **Core:** keep state when modifying collections
* **Core:** overwrite existing files when saving responses
* **Core:** show error message when saving an environment with duplicate JSON keys
* **gRPC:** correctly send large numbers when not quoted as a string
* **gRPC:** handle incorrect server reflection implementations that do not specify proto dependencies
* **REST:** improve handling of formatted responses with invalid content
* **REST:** improve resulting project structure from OpenAPI import
* **Scripting:** ensure that the correct suggestions are displayed in the UI
* **Scripting:** provide date.to\_string docs
* **Scripting:** show correct inlined parameter name in piped templated function calls
* **UI:** add preview for advanced auth options
* **UI:** behaviour of a newly created user variable is fixed
* **UI:** display scripting and sandbox exceptions as snackbar
* **UI:** fix theme switching, which failed sometimes before
* **UI:** moving or renaming should not break quick actions
* **Linux:** correctly build snap
* **Linux:** native clipboard support

***

## 1.17.0 (2025-04-30)

### Features

* **Core:** add access to operation name in scripts
* **Core:** add file and path scripting API
* **Core:** add JWT auth provider and option to set header value prefix
* **Core:** add option to use the native browser to authenticate
* **Core:** added Kreya Script to control operation invocation with JavaScript
* **Core:** export as curl
* **Core:** import cookies when importing curl commands
* **Core:** improve Windows installer to allow per-user installs
* **Core:** open imported sample operation after import
* **Core:** support async scripting hooks
* **Core:** support async test hooks in scripting
* **Core:** support CommonJS npm packages in scripting
* **Core:** support HAR file imports
* **Core:** support importing Postman v2.0.0 collections
* **Core:** support type resolution for relative script imports
* **Core:** support unix sockets and named pipe transports
* **Core:** user variables editor
* **gRPC:** add option to copy grpc operations as curl commands to the clipboard
* **gRPC:** show proto files imported documentation in script editor autocompletion
* **REST:** add scripting content autocompletion
* **UI:** add copy operation path and open in file manager quick actions
* **UI:** add option to close tabs on the left and right
* **UI:** add quick action to open the import dialog
* **UI:** add search for operations, directories and collections
* **UI:** allow to add an environment via the environment switcher if none exists
* **UI:** allow to resize/reposition quick actions overlay

### Bug Fixes

* **CLI:** add support for CLI response / flag files (arguments provided in a file with the @-syntax)
* **CLI:** correctly bundle macos kreyac CLI dependencies
* **CLI:** correctly include protoc in Docker
* **CLI:** improve error message reporting
* **Core:** add request Content-Type header in Postman importer if not already present
* **Core:** assign .krproj extension with Kreya application on macos
* **Core:** change kreya.trace Scripting function to accept all data types
* **Core:** correctly handle arrays in Scripting
* **Core:** correctly write scripts of imported operations to separate files
* **Core:** do not show operation as sending when it was aborted due to script errors
* **Core:** fix a rare crash on macos when authenticating with OIDC
* **Core:** fix postman import api key auth
* **Core:** further improve Postman translations
* **Core:** handle encoded curl cookies in curl parser
* **Core:** handle invalid directory characters in Postman and Insomnia imports correctly
* **Core:** improve release process
* **Core:** improve script type imports
* **Core:** return undefined instead of null when getting a non-existent user variable in Scripting
* **Core:** save project settings before duplicating or renaming
* **Core:** update chai testing library to 5.2.0
* **Core:** use correct name for imported curl operations
* **Core:** use relative paths everywhere
* **gRPC:** preselect the current gRPC method when changing the method
* **gRPC:** show input/output types of other packages in proto declaration tab
* **gRPC:** stream keyword was missing in the gRPC service declaration
* **gRPC:** use correct types in gRPC response scripting autocomplete
* **REST:** correctly set multipart request content type and do not require one
* **UI:** abort collection running cleanly after a operation changed
* **UI:** add run importer button to importer settings
* **UI:** allow context menu click in empty space in the operation list
* **UI:** improve autocomplete and input suggestions filter and sort
* **UI:** improve json path/xpath response input
* **UI:** improve open operation search and allow to open collections
* **UI:** improve shortcut responsiveness
* **UI:** improve Windows dark mode
* **UI:** increase panel resizer width
* **UI:** remove tab character when copy pasting key-value entries
* **UI:** save auth details when switching tabs
* **UI:** show dates in user locale format
* **UI:** show scrollbar in big context menus
* **UI:** stop autoscrolling when user scrolled manually
* **UI:** storing an empty user variable should remove it
* **UI:** tab title is updated when a REST operation changes its method type

***

## 1.16.0 (2025-01-16)

### Features

* **Core:** add AWS signature version 4
* **Core:** add cookie management
* **Core:** add custom headers for gRPC server reflection and OpenAPI URL importers
* **Core:** add faker to the Scripting API
* **Core:** add file exclusion list for gRPC proto file importers
* **Core:** automatically translate most of the Postman scripts during the import
* **Core:** improve grpc any handling for unknown types
* **Core:** option to minify xml and json request bodies
* **Core:** send auth configs as query param or with other header names
* **REST:** autocomplete well-known REST headers
* **UI:** add operation collection state filter
* **UI:** show running operations and collections in the operation list
* **UI:** simplify operation creation workflow
* **UI:** update the look and feel of Kreya
* **WebSocket:** add support for WebSockets
* **WebSocket:** support importing WebSocket requests from Insomnia

### Bug Fixes

* **Core:** ask to save unsaved changes before exiting
* **Core:** better error message when a path is outside of the project directory
* **Core:** cancel operation collection run when closing the tab
* **Core:** certificates with key and cert file were invalid on MacOS 15
* **Core:** correctly display suggestions in non-JSON editors
* **Core:** correctly invalidate importer cache in some cases
* **Core:** do not crash when closing immediately after opening
* **Core:** do not import authentications from Postman/Insomnia if they already exist
* **Core:** do not show failed message for resolving scripting modules when none are present
* **Core:** early Scripting messages did not show up when sending a collection in certain cases
* **Core:** fix duplicated entries when searching operations
* **Core:** limit time for background tasks to exit when closing the app
* **Core:** parse server timing duration correctly
* **Core:** postman importer: read request type from Content-Type header as fallback
* **gRPC:** add support for some well known google protobuf types again
* **gRPC:** correct type for gRPC repeated fields in Scripting
* **REST:** allow empty request paths
* **REST:** do not render empty response
* **REST:** treat all status codes < 400 as successful
* **UI:** allow scrolling in project settings with many entries
* **UI:** don't autoclose context menu just after open on some operating systems
* **UI:** entering a full path with endpoint is now possible for REST operations
* **UI:** environment switcher in directory settings is more visible
* **UI:** improve quick action overlay contrast
* **UI:** increase debounce time for combined shortcuts
* **UI:** login state in status bar and operations is refreshed after login
* **UI:** made tab switching shortcuts visible and add different shortcut for MacOS
* **UI:** reorder operation list after renaming an item
* **UI:** show an unique tab name for operations and directories with same name
* **UI:** show operation result state in collection header correctly

***

## 1.15.0 (2024-06-12)

### Features

* **gRPC:** show comments in declaration when imported from proto files
* **gRPC:** support protobuf edition 2023 and proto2
* **UI:** show project, operation, directory and collection paths

### Bug Fixes

* **Core:** add protoc dependecies to macos app build
* **Core:** handle invalid refresh token during authentication
* **Core:** purge selected caches correctly and remove cache purger preselection
* **Core:** recognize templated endpoints during Postman and Insomnia imports
* **Core:** renew Windows code signing certificate
* **Core:** upgrade scriban to include new template helpers
* **gRPC:** correctly terminate operation on timeout when sending requests manually
* **REST:** automatically encode path param values
* **REST:** rest operation with multipart body was not rendered
* **REST:** saving a raw response failed if destination file already existed
* **UI:** add only button for check box groups

***

## 1.14.0 (2024-04-18)

### Features

* **CLI:** add junit reporter
* **CLI:** allow to invoke multiple collections in the CLI
* **Core:** add Insomnia project importer
* **Core:** add sleep in scripting
* **Core:** allow to filter test results
* **Core:** environment access in scripting
* **Core:** improve rest error handling and display correct errors
* **Core:** run directories as collection
* **Core:** show merged environment and import system environment variables
* **Core:** templating environment name access
* **UI:** add filter for trace messages
* **UI:** add operations to collection via drag and drop
* **UI:** added context menu entry to open items in file manager

### Bug Fixes

* **CLI:** add fallback console where colorful terminal is not supported
* **Core:** allow to open project containing read only files
* **Core:** collections should continue running if an operation fails to load
* **Core:** improve operation collection ui
* **Core:** move and rename operation update relative paths correctly
* **Core:** replace invalid file name characters during postman collection import
* **Core:** stop long running Scripting tasks when cancelling
* **Core:** upgrade dependencies
* **REST:** apply Scriban template to REST endpoint and path before replacing path params
* **REST:** parse custom content types correctly
* **UI:** correctly show add operation popup in collection on button click
* **UI:** do not override monaco editor shortcuts
* **UI:** do not show empty window title
* **UI:** empty metadata, headers and query params are not stored in directory settings
* **UI:** improve operation search
* **UI:** improve typography and higher contrast for light theme buttons
* **UI:** improve welcome screen on lower screen widths
* **UI:** improved button visibility
* **UI:** operation state icons cut off fixed
* **UI:** perform operation rename etc. on blur instead of cancelling
* **UI:** selecting text when renaming nodes now works
* **UI:** show correct message in quick actions when no actions are available
* **UI:** show error when entering invalid file name during rename
* **UI:** show status messages for concurrent invocations and collections

***

## 1.13.1 (2024-02-12)

### Bug Fixes

* **Core:** correctly display open source licenses again
* **gRPC:** better error message for invalid endpoint schemes
* **UI:** correctly account for monitors with different DPI
* **UI:** ensure that UI panels resize properly
* **UI:** optimize operation search threshold for a better result

***

## 1.13.0 (2024-01-29)

### Features

* **CLI:** add collection invoke command to CLI
* **CLI:** add create project command
* **Core:** add Postman importer
* **Core:** Collections
* **gRPC:** add declaration tab to show proto declaration of a gRPC method
* **gRPC:** resolve file descriptor set well known types automatically
* **gRPC:** show request comments when imported from a file descriptor set with included source info
* **REST:** show trace message when redirection occurs
* **REST:** add authorization header for importer API

### Bug Fixes

* **CLI:** allow absolute operation paths to be invoked
* **Core:** correctly open projects with spaces in their name via CLI arguments
* **Core:** correctly support proxies with authentication
* **Core:** don't cache auth state when using scripting variables
* **Core:** fixes jwt profile authentication when invoked multiple times in a short period
* **Core:** improve stability on macOS
* **Core:** make auto-updater work on macOS and linux for paths with spaces
* **Core:** move Kreya data files to new location on macOS
* **Core:** show errors during refresh flow correctly
* **UI:** add renaming shortcut and add shortcut information to context menus
* **UI:** multiple responses sometimes not expanded
* **UI:** remove method not imported toast
* **UI:** show operation type hint for open operation quick action

***

## 1.12.0 (2023-11-06)

### Features

* **Core:** add resolve unimported operations dialog after import run
* **Core:** adding nested operations is now possible
* **Core:** directories can now be duplicated with the context menu, quick action and copy paste
* **Core:** inherited headers, query params and metadata can be ignored
* **Core:** visualize operation and server timing
* **Core:** windows ARM64 support
* **REST:** add option to disable ssl server certificate validation for open api url importer
* **REST:** add option to specify the http version to use
* **REST:** show partial text responses
* **REST:** support HTTP/3
* **REST:** support new-line delimited streamed JSON
* **REST:** support new-line delimited streamed xml
* **REST:** support server sent events
* **UI:** add keyboard shortcuts for operation list
* **UI:** added drag and drop to rearrange tabs
* **UI:** multiple operations and directories can be selected
* **UI:** remember last window size and position
* **UI:** use virtual scrolling to handle large amount of gRPC responses

### Bug Fixes

* **Core:** correctly handle environment files modified by other processes
* **Core:** correctly update operation tree after file system directory changes
* **Core:** dont fail to import when a prefix directory, but no project subdirectory is defined
* **Core:** resolved bugs in operation search result highlighting
* **gRPC:** do not create server reflection import operations automatically
* **gRPC:** do not fail on very large responses
* **REST:** adjust relative file paths when moving or duplicating REST operations
* **UI:** alignment of gRPC operation icon
* **UI:** center Kreya on first launch on macOS
* **UI:** change operation duplication to inline
* **UI:** enable mouse wheel zoom for request and reponse view
* **UI:** expand directories on drag and drop
* **UI:** gRPC method edit button is visible for long method names
* **UI:** indentation of directories and operations in operation list
* **UI:** inline auth token update button and login button spinner layout
* **UI:** larger max width for toasts
* **UI:** test results layout
* **UI:** theme switcher label
* **UI:** toast background in light theme is not dark

***

## 1.11.1 (2023-08-23)

### Bug Fixes

* **Core:** correctly load dependencies to prevent crashes on startup for new MacOS installations

***

## 1.11.0 (2023-08-21)

### Features

* **Core:** add option to purge user variables
* **Core:** add tour for new users
* **Core:** build linux arm
* **Core:** linux arm snapcraft support
* **UI:** add possibility to duplicate importers
* **UI:** add possibility to show messages to kreya users

### Bug Fixes

* **CLI:** load scripting dependency correctly in docker kreyac
* **CLI:** make browser authentication cancellable
* **CLI:** make environment configurations work
* **CLI:** only run required importers when invoking operations via cli
* **CLI:** show detailed messages
* **Core:** about window can now be opened during fullscreen on macos
* **Core:** correct windows installation path
* **Core:** correctly reevaluate inherited, templated operation settings
* **Core:** delete of operations and directories with unsaved changes
* **Core:** do not try to store relative paths for resources on a different drive
* **Core:** improve Windows installer and WebView2 detection
* **Core:** resolve scripting type definitions correctly when switching operation tabs
* **Core:** show error details in the ui for well known exceptions
* **UI:** changed history shortcut to primary+shift+h
* **UI:** correctly handle shortcuts when switching tabs
* **UI:** fix Windows DPI issues
* **UI:** improve welcome screen with quick links and tips
* **UI:** improvments of dialog buttons
* **UI:** inherited rest path params placeholders are now visible on operation load
* **UI:** new folders and renaming operation indentations fixed
* **UI:** renamed delete action for directories
* **UI:** renaming folders with dots
* **UI:** select directories and operations on right click
* **UI:** show quick actions if no tab is open
* **UI:** update welcome screen message based on user subscription

***

### 1.10.1 (2023-03-23)

### Bug Fixes

* **Core:** add removable-media snapcraft plug
* **Core:** correctly handle operation invocation failures
* **Core:** fix account login on snapcraft linux installations
* **Core:** oauth refresh token support
* **Core:** specify correct linux dependency versions
* **gRPC:** response time could be delayed up to 3s
* **UI:** macOS icon size and add corner radius
* **UI:** type hint vertical alignment to center

***

## 1.10.0 (2023-02-28)

### Features

* **Core:** add CLI
* **Core:** add history for operations
* **Core:** add option to reset inherited auth to none
* **Core:** add option to reset inherited client certificate to none
* **Core:** add option to trim prefix when creating operations from importers
* **Core:** add static authorization header value provider
* **Core:** allow simultaneous invocation of operations
* **Core:** rework 'reset requests' to 'reset operation'
* **gRPC:** add option to export response to file
* **gRPC:** import grpcurl commands from clipboard
* **gRPC:** option to add authorization to server reflection importers
* **REST:** add option to export response to file
* **REST:** add response preview for HTML and SVG
* **REST:** option to add authorization to openapi importers
* **REST:** path variables
* **UI:** add tabs for open operations
* **UI:** improved new project wizard
* **UI:** keyboard navigation in operation list

### Bug Fixes

* **Core:** correctly apply default settings for environments
* **Core:** correctly open project when an absolute path is provided
* **Core:** curl clipboard importer use post http method if any data flag is set
* **Core:** enhance debug infos in about window
* **Core:** if one importer fails, other importers should still run
* **Core:** merge environment data and user data correctly
* **Core:** resolve blank screen bug
* **Core:** save changes when another tab is opened
* **gRPC:** do not share imported information between import streams
* **gRPC:** remove default gRPC user agent
* **UI:** disable tooltip interactivity
* **UI:** fix blank screen on older macos versions
* **UI:** fix scrollbar issues in REST settings
* **UI:** improve open operation fuzzy search

***

## 1.9.0 (2022-11-04)

### Features

* **Core:** add variable support for scripting and templating
* **gRPC:** import grpc web operations via curl commands
* **REST:** import rest operations via curl commands

### Bug Fixes

* **Core:** fix crashes on macos 13
* **Core:** remove deprecated environment entries from templating suggestions
* **Core:** remove empty key value entries on save
* **Core:** show whitespace in inherited headers
* **gRPC:** allow creation of operation if a grpc service only contains one rpc
* **gRPC:** parse protobuf files correctly
* **REST:** do not set a JSON schema for operations without a request definition
* **REST:** match suffixed media types correctly

***

### 1.8.1 (2022-08-12)

### Bug Fixes

* correctly refresh auth details when changing the active environment
* **gRPC:** remove default timeout of 100s
* make response headers and trailers selectable
* show a nice error message when an URL does not contain a scheme
* some external links opened twice

***

## 1.8.0 (2022-07-11)

### Features

* add option to decode access token claims
* add purge caches option
* improve sample value generator by using suffix matching and better synonyms
* macos arm build
* option to create missing operations in importers in a subdirectory of the project
* test scripting and response assertions in JavaScript
* select first environment automatically
* status bar to show tasks in progress
* system credentials auth provider
* use random sample values
* add kreya customer account login
* **REST**: add initial support
* **gRPC** deadline support
* **gRPC:** support binary request metadata

### Bug Fixes

* add tabs overflow support
* use correct openid options and allow ignored additional params
* bugfix for moving a newly created directory
* build scriban documentation correctly if references are used
* consistent overflow-y where content can overflow
* copy debug infos tooltip covered button
* handle grpc-status-details-bin header correctly in all circumstances
* hide certificate selector at the project setup dialog
* improve file watchers when many file system events happen at once
* inconsistent protobuf imports caused importers to fail
* key value editor improvements
* linux: fixed rare exception on startup
* render ui even if initialization fails to display errors
* response text is now copyable
* shortcuts could be registered and executed multiple times
* show an error message box if Kreya fails to start
* show error dialog when a file descriptor set cannot be found in a proto file set importer
* Tracing: match trace messages to operation invocations
* window layouting

***

## 1.7.0 (2021-11-09)

### Features

* add faker data to be accessible via scriban templates
* add light mode and an option to switch between color themes
* add templating parameter hints
* add what's new page to the snackbar after update
* cache importer results for much better performance
* make auth configurations available through scriban templating
* show environment variable content in templated expressions on mouse hover
* show function signature information for scriban function calls in the request editor
* show parameter type hints in scriban function calls

### Bug Fixes

* add quick actions to send requests manually
* deleting an operation caused errors when invoking other operations
* display trace messages correctly if an auth provider is used
* display unknown grpc status correctly
* fixed a bug where importing and generating example messages for the Google API didn't work
* free ressources correctly after app termination
* improve error messages and error reporting
* improve suggestions ui in settings
* improve UX for running importers
* load suggestion icons correctly
* suggestions from environment should override scriban api's provided by kreya
* trace log timestamps should show timestamps in local time instead of utc

***

## 1.6.0 (2021-09-11)

### Features

* add setting for max gRPC message size and remove default limit
* support all well known types in Any messages
* new file descriptor set importer
* add project initial setup and example project
* support system environment variables in some paths

### Bug Fixes

* allow trailing commas in request json
* correctly display scrollbars when many requests or responses are present
* do not show errors for trailing commas and comments in json requests
* improve auto updater
* layout editor suggestions correctly
* switch complete button to cancel button when client streaming request was manually completed
* be more foregiveable if an imported proto contains errors

***

## 1.5.0 (2021-07-08)

### Features

* add operation menu entry to overwrite the requests of an operation
* add proto3 optional support
* operation list-, request- and response-view are now resizable

### Bug Fixes

* add missing operation type to telemetry events for operation invocation
* add new kreya webpage urls for release notes
* allow comments in request json
* enable high DPI support on windows
* handle responses with invalid struct values
* handle service errors correctly when sending requests one by one
* improve autocomplete selection for create and change operation
* improve ui if there are lots of requests/responses
* load proto dependencies correctly in server reflection importer
* prevent a crash when the file watchers cannot be registered
* refresh request view correctly when first request is deleted
* register .krproj file extension with Kreya for windows
* resolve duplicate app infos error on startup
* resolve strange ui behavior when adding a request
* scroll requests into view after creation

***

## 1.4.0 (2021-04-30)

### Features

* add client tls certificates
* add option to send streamed requests one by one
* add telemetry and telemetry opt-out option
* changing grpc method within operation
* duplicate environments and authentications
* support paths in grpc endpoints

### Bug Fixes

* abort the request as soon as the external auth window is opened
* add trace log for cancelling a request
* changing the type of an existing importer didn't work
* correctly serialize int64, sfixed64 and sint64 values
* don't allow to send a request for unsupported operation types
* dont allow duplicated names for operations, directories and setting entries
* ensure environment data is valid json
* fixes a crash on macos when \~/.config does not exist
* improve error handling for oidc authentications
* improve grpc error logging
* invalid endpoint doesn't abort the request
* nest open operation under an open operation quick action
* select created importer after save
* set release channel after version update
* show exception details if a template runtime exception occured
* sign windows MSI
* templated expressions in grpc operation metadata should evaluate before each call

***

### 1.3.1 (2021-04-12)

### Bug Fixes

* autocomplete should not consume backdrop pointer events
* don't try to show an autocomplete suggestions overlay if there aren't any suggestions
* fixes a weird bug which prevented saving an environment under certain conditions
* unsaved changes dialog in settings should not appear on delete

***

## 1.3.0 (2021-04-09)

### Features

* add OpenID-Connect / OAuth2.0 client credentials and password grant types support
* open recent project via quick action
* open recent projects via menu
* option to disable TLS/SSL validation
* option to disable TLS/SSL validation on grpc server reflection importers
* show response count in response tab
* specify default settings on directory levels
* store latest response

### Bug Fixes

* autocomplete replace selected text
* calling a non-grpc host fails
* delete operations with unsaved changes correctly
* fuzzy search to open an operation via quick actions
* hide no operation msg on initial folder creation
* immediately remove directory from the ui on delete
* improve file watchers
* improve handling of operations with a referenced method which is not imported
* improve the save/cancel behaviour in the settings
* key manager active item reference cleanup on item changes
* help menu: add feadback and release notes entries
* only save operations when changes were made
* operation and directory selection after manual create
* operations created by importers don't show up immediately
* remove directory from operation list after manual delete
* rename authorization configurations to authentications
* store operation content correctly after duplicating or moving it

***

### 1.2.1 (2021-02-24)

### Bug Fixes

* creation of an importer failed

***

## 1.2.0 (2021-02-24)

### Features

* option to create all possible operations from importer
* response json path support
* delete operation quick action
* duplicate operation via context menu and quick action
* decode rich errors (status.proto)
* serialize enums as names
* support unknown any types in responses
* support for the well known type field mask

### Bug Fixes

* allow creation of grpc requests for services without a package
* handle oidc auth without a client secret correctly
* show error message when oidc discovery document fails to load
* store relative paths with forward slashes in project files
* encode and decode repeated wrapper values correctly

***

## 1.1.0 (2021-02-06)

### Features

* linux support
* show changelog link on update

### Bug Fixes

* simplify menu
* truncate response status detail instead of overflowing
* use the correct release channel of the binary
* **windows:** also apply custom scrollbar style in modals
* catch exception when update loop gets cancelled

***

## 1.0.1 (2021-01-26)

### Bug Fixes

* **macos:** fix blurry font

***

## 1.0.0 (2021-01-18)

Initial Release

***
