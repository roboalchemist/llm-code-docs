# Source: https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html

Title: Style Editor — Firefox Source Docs documentation

URL Source: https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html

Published Time: Fri, 13 Mar 2026 03:03:00 GMT

Markdown Content:
The Style Editor enables you to:

*   view and edit all the stylesheets associated with a page

*   create new stylesheets from scratch and apply them to the page

*   import existing stylesheets and apply them to the page

To open the Style Editor select the _Style Editor_ panel in the Web Developer Tools, accessible from the Browser Tools submenu

![Image 1: ../../_images/style-editor.png](https://firefox-source-docs.mozilla.org/_images/style-editor.png)
The Style Editor is divided into three main sections:

*   [the style sheet pane on the left](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#style-editor-the-style-sheet-pane)

*   [the editor on the right](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#style-editor-the-editor-pane)

*   [the At-rules sidebar](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#style-editor-the-at-rules-sidebar)

The style sheet pane[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#the-style-sheet-pane "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

The style sheet pane, on the left, lists all the style sheets being used by the current document. You can quickly toggle the use of a given sheet on and off by clicking the eyeball icon to the left of the sheet’s name. You can save any changes you’ve made to the style sheet to your local computer by clicking the Save button in the bottom-right corner of each sheet’s entry in the list.

The style sheet pane also includes a context menu that lets you open the selected style sheet in a new tab.

The editor pane[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#the-editor-pane "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

On the right is the editor pane. This is where the source for the selected style sheet is available for you to read and edit. Any changes you make are immediately applied to the page. This makes it easy to experiment with, revise, and test changes. Once you’re satisfied with your changes, you can save a copy locally by clicking the Save button on the sheet’s entry in the style sheet pane.

The editor provides line numbers and syntax highlighting to help make it easier to read your CSS. It also supports a number of [keyboard shortcuts](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#style-editor-keyboard-shortcuts).

The Style Editor automatically de-minimizes style sheets that it detects, without affecting the original. This makes it much easier to work on pages that have been optimized.

The Style Editor supports autocomplete. Just start typing, and it will offer you a list of suggestions.

![Image 2: ../../_images/style-editor-autocomplete.png](https://firefox-source-docs.mozilla.org/_images/style-editor-autocomplete.png)
You can switch autocomplete off in the [Style Editor settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-style-editor).

Creating and importing style sheets[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#creating-and-importing-style-sheets "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can create a new style sheet by clicking the New button in the toolbar. Then you can just start entering CSS into the new editor and watch as the new styles are applied in real time just like changes to the other sheets.

You can load a style sheet from disk and apply it to the page by clicking the Import button.

Source map support[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#source-map-support "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Web developers often create CSS files using a preprocessor like [Sass](https://sass-lang.com/), [Less](https://lesscss.org/), or [Stylus](https://learnboost.github.io/stylus/). These tools generate CSS files from a richer and more expressive syntax. If you do this, being able to see and edit the generated CSS is not so useful, because the code you maintain is the preprocessor syntax, not the generated CSS. So you’d need to edit the generated CSS, then manually work out how to reapply that to the original source.

Source maps enable the tools to map back from the generated CSS to the original syntax, so they can display, and allow you to edit, files in the original syntax. The Style Editor can understand CSS source maps.

This means that if you use, for example, Sass, then the Style Editor will show you, and allow you to edit, Sass files, rather than the CSS that is generated from them:

![Image 3: ../../_images/style-editor-sourcemap.png](https://firefox-source-docs.mozilla.org/_images/style-editor-sourcemap.png)
For this to work, you must:

*   use a CSS preprocessor that understands the [Source Map Revision 3 proposal](https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit). Currently this means [Sass 3.3.0](https://sass-lang.com/) or above or the [1.5.0 version of Less](http://roots.io/using-less-source-maps/). Other preprocessors are actively working on adding support, or considering it.

*   actually instruct the preprocessor to generate a source map, for example by passing the `--source-map` argument to the Lass command-line tool, but in some preprocessors like Sass, source maps are generated by default and you don’t need to do anything.

### Viewing original sources[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#viewing-original-sources "Link to this heading")

Now, if you check “Show original sources” in the [Style Editor settings](https://firefox-source-docs.mozilla.org/devtools-user/settings/index.html#settings-style-editor), the links next to CSS rules in the [Rules view](https://firefox-source-docs.mozilla.org/devtools-user/page_inspector/ui_tour/index.html#page-inspector-ui-tour-rules-view) will link to the original sources in the Style Editor.

Original sources are displayed by default.

### Editing original sources[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#editing-original-sources "Link to this heading")

You can also edit the original sources in the Style Editor and see the results applied to the page immediately. To get this to work there are two extra steps.

First, set up your preprocessor so it watches the original source and automatically regenerates the CSS when the source changes. With Sass you can do this by passing the `--watch` option:

sass index.scss:index.css --watch

Next, save the original source in the Style Editor by clicking the “Save” button next to the file, and saving it over the original file.

Now when you make changes to the source file in the Style Editor the CSS is regenerated and you can see the changes right away.

Keyboard shortcuts[](https://firefox-source-docs.mozilla.org/devtools-user/style_editor/index.html#keyboard-shortcuts "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

> *   [Source editor shortcuts](https://firefox-source-docs.mozilla.org/devtools-user/keyboard_shortcuts/index.html#keyboard-shortcuts-style-editor)
