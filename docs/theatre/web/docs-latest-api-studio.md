# Source: https://www.theatrejs.com/docs/latest/api/studio

Title: @theatre/studio – Theatre.js

URL Source: https://www.theatrejs.com/docs/latest/api/studio

Markdown Content:
`import studio from '@theatre/studio'`

#studio.initialize()
--------------------

Initializes the studio. Call it once in your index.js/index.ts module. It silently ignores subsequent calls.

#studio.transaction(fn)
-----------------------

Runs an undo-able transaction. Creates a single undo level for all the operations inside the transaction.

Will roll back if an error is thrown.

`studio.transaction(({ set, unset }) => {  set(obj.props.x, 10) // set the value of obj.props.x to 10  unset(obj.props.y) // unset the override at obj.props.y})`

### #api.set(pointer, value)

Set the value of a prop by its [pointer](https://www.theatrejs.com/docs/latest/api/core#pointers). If the prop is sequenced, the value will be a keyframe at the current sequence position.

`const obj = sheet.object('box', { x: 0, y: 0 })studio.transaction(({ set }) => {  // set a specific prop's value  set(obj.props.x, 10) // New value is {x: 10, y: 0}  // values are set partially  set(obj.props, { y: 11 }) // New value is {x: 10, y: 11}  // this throw an error, as there is no such prop as 'z'  set(obj.props.z, 10)})`

### #api.unset(pointer, value)

Unsets the value of a prop by its [pointer](https://www.theatrejs.com/docs/latest/api/core#pointers).

`const obj = sheet.object('box', { x: 0, y: 0 })studio.transaction(({ set }) => {  // set props.x to its default value  unset(obj.props.x)  // set all props to their default value  set(obj.props)})`

#studio.scrub()
---------------

Creates a scrub, which is just like a transaction, except you can run it multiple times without creating extra undo levels.

`const scrub = studio.scrub()scrub.capture(({ set }) => {  set(obj.props.x, 10) // set the value of obj.props.x to 10})// half a second later...scrub.capture(({ set }) => {  set(obj.props.y, 11) // set the value of obj.props.y to 11  // note that since we're not setting obj.props.x, its value reverts back to its old value (ie. not 10)})// then either:scrub.commit() // commits the scrub and creates a single undo level// or:scrub.reset() // clears all the ops in the scrub so we can run scrub.capture() again// or:scrub.discard() // clears the ops and destroys it (ie. can't call scrub.capture() anymore)`

#studio.extend(extension)
-------------------------

Registers an extension. Extensions enable you to extend the Studio's UI and/or extend the functionality of Studio. Read more about working with extensions in the ["Authoring extensions" manual](https://www.theatrejs.com/docs/latest/manual/authoring-extensions).

`import { extension } from './myExtension'studio.extend(extension)`

#studio.createContentOfSaveFile(projectId)
------------------------------------------

Creates a JSON object that contains the state of the project. You can use this to programmatically save the state of your projects to the storage system of your choice, rather than [manually clicking on the "Export" button in the UI](https://www.theatrejs.com/docs/latest/manual/projects#docs-manual-projects-export-project).

`const projectId = 'project'const json = studio.createContentOfSaveFile(projectId)const string = JSON.stringify(json)fetch(`/projects/${projectId}/state`, { method: 'POST', body: string }).then(() => {  console.log('Saved')})`

#studio.createPane(paneClass)
-----------------------------

Creates a new pane. Takes a string as its argument specifying a pane class previously registered by an extension.

`studio.createPane('snapshot')`

#studio.getStudioProject()
--------------------------

Returns the [Theatre.js project](https://www.theatrejs.com/docs/latest/api/core#project) that contains the studio's [sheets](https://www.theatrejs.com/docs/latest/api/core#sheet) and [objects](https://www.theatrejs.com/docs/latest/api/core#object).

It is useful if you'd like to have sheets/objects that are present only when the studio is present.

#studio.selection
-----------------

The current selection, consisting of [sheets](https://www.theatrejs.com/docs/latest/api/core#sheet) and [sheet objects](https://www.theatrejs.com/docs/latest/api/core#object).

`console.log(studio.selection) // [ISheetObject, ISheet]`

#studio.onSelectionChange(callback)
-----------------------------------

Let's you subscribe to selection changes. Calls the provided callback with the current selection every time the selection changes.

`return studio.onSelectionChange((newSelection) => {  console.log(newSelection) // [ISheetObject]})`

#studio.setSelection(selection)
-------------------------------

Sets the current selection.

`studio.setSelection([someSheet, someObject])`

#studio.ui
----------

Exposes utilities to manipulate the Studio UI.

### #studio.ui.hide()

Hides the Studio.

`studio.ui.hide()`

### #studio.ui.restore()

Shows the Studio.

`studio.ui.restore()`

### #studio.ui.isHidden

`true` if Studio is hidden currently.

`if (studio.ui.isHidden) {  // Do something}`

### #studio.ui.renderToolset(toolsetId, container)

Let's you render a toolset previously defined by an extension into a dom node of your choice.

`studio.ui.renderToolset('my-toolbar', toolbarContainerNode)`

* * *

Was this article helpful to you?

Last edited on February 01, 2024.

[Edit this page](https://github.com/theatre-js/website/blob/main/content/docs/0.5/500-api/200-studio.mdx)
