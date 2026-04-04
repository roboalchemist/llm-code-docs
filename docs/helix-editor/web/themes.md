# Source: https://docs.helix-editor.com/themes.html

## Themes

To use a theme addtheme = "<name>"to the top of yourconfig.tomlfile, or select it during runtime using:theme <name>.

## Creating a theme

Create a file with the name of your theme as the file name (i.emytheme.toml) and place it in yourthemesdirectory (i.e~/.config/helix/themesor%AppData%\helix\themeson Windows). The directory might have to be created beforehand.
> 💡 The names "default" and "base16_default" are reserved for built-in themes
and cannot be overridden by user-defined themes.

### Overview

Each line in the theme file is specified as below:

```
key = { fg = "#ffffff", bg = "#000000", underline = { color = "#ff0000", style = "curl"}, modifiers = ["bold", "italic"] }
```

Wherekeyrepresents what you want to style,fgspecifies the foreground color,bgthe background color,underlinethe underlinestyle/color, andmodifiersis a list of style modifiers.bg,underlineandmodifierscan be omitted to defer to the defaults.
To specify only the foreground color:

```
key = "#ffffff"
```

If the key contains a dot'.', it must be quoted to prevent it being parsed as adotted key.

```
"key.key" = "#ffffff"
```

For inspiration, you can find the defaulttheme.tomlhereand
user-submitted themeshere.

## The details of theme creation

### Color palettes

It's recommended to define a palette of named colors, and refer to them in the
configuration values in your theme. To do this, add a table calledpaletteto your theme file:

```
"ui.background" = "white"
"ui.text" = "black"

[palette]
white = "#ffffff"
black = "#000000"
```

Keep in mind that the[palette]table includes all keys after its header,
so it should be defined after the normal theme options.
The default palette uses the terminal's default 16 colors, and the colors names
are listed below. The[palette]section in the config file takes precedence
over it and is merged into the default palette.
Color Namedefaultblackredgreenyellowbluemagentacyangraylight-redlight-greenlight-yellowlight-bluelight-magentalight-cyanlight-graywhite

### Modifiers

The following values may be used as modifier, provided they are supported by
your terminal emulator.
Modifierbolddimitalicunderlinedslow_blinkrapid_blinkreversedhiddencrossed_out
> 💡 Theunderlinedmodifier is deprecated and only available for backwards compatibility.
Its behavior is equivalent to settingunderline.style="line".

### Underline style

One of the following values may be used as a value forunderline.style, providing it is
supported by your terminal emulator.
Modifierlinecurldasheddotteddouble_line

### Inheritance

Extend other themes by setting theinheritsproperty to an existing theme.

```
inherits = "boo_berry"

# Override the theming for "keyword"s:
"keyword" = { fg = "gold" }

# Override colors in the palette:
[palette]
berry = "#2A2A4D"
```

### Scopes

The following is a list of scopes available to use for styling:

#### Syntax highlighting

These keys matchtree-sitter scopes.
When determining styling for a highlight, the longest matching theme key will be used. For example, if the highlight isfunction.builtin.static, the keyfunction.builtinwill be used instead offunction.
We use a similar set of scopes asSublime Text. See alsoTextMatescopes.
- attribute- Class attributes, HTML tag attributes
- type- Typesbuiltin- Primitive types provided by the language (int,usize)parameter- Generic type parameters (T)enumvariant
- constructor
- constant(TODO: constant.other.placeholder for%v)builtinSpecial constants provided by the language (true,false,niletc)booleancharacterescapenumeric(numbers)integerfloat
- string(TODO: string.quoted.{single, double}, string.raw/.unquoted)?regexp- Regular expressionsspecialpathurlsymbol- Erlang/Elixir atoms, Ruby symbols, Clojure keywords
- comment- Code commentsline- Single line comments (//)documentation- Line documentation comments (e.g.///in Rust)block- Block comments (e.g. (/* */)documentation- Block documentation comments (e.g./** */in Rust)unused- Unused variables and patterns, e.g._and_foo
- variable- Variablesbuiltin- Reserved language variables (self,this,super, etc.)parameter- Function parametersothermember- Fields of composite data types (e.g. structs, unions)private- Private fields that use a unique syntax (currently just ECMAScript-based languages)
- label-.class,#idin CSS, etc.
- punctuationdelimiter- Commas, colonsbracket- Parentheses, angle brackets, etc.special- String interpolation brackets.
- keywordcontrolconditional-if,elserepeat-for,while,loopimport-import,exportreturnexceptionoperator-or,indirective- Preprocessor directives (#ifin C)function-fn,funcstorage- Keywords describing how things are storedtype- The type of something,class,function,var,let, etc.modifier- Storage modifiers likestatic,mut,const,ref, etc.
- operator-||,+=,>
- functionbuiltinmethodprivate- Private methods that use a unique syntax (currently just ECMAScript-based languages)macrospecial(preprocessor in C)
- tag- Tags (e.g.<body>in HTML)builtin
- namespace
- special-derivein Rust, etc.
- markupheadingmarker1,2,3,4,5,6- heading text for h1 through h6listunnumberednumberedcheckeduncheckedbolditalicstrikethroughlinkurl- URLs pointed to by linkslabel- non-URL link referencestext- URL and image descriptions in linksquoterawinlineblock
- diff- version control changesplus- additionsgutter- gutter indicatorminus- deletionsgutter- gutter indicatordelta- modificationsmoved- renamed or moved files/changesconflict- merge conflictsgutter- gutter indicator

#### Interface

These scopes are used for theming the editor interface:
- markupnormalcompletion- for completion doc popup UIhover- for hover popup UIheadingcompletion- for completion doc popup UIhover- for hover popup UIrawinlinecompletion- for completion doc popup UIhover- for hover popup UI
KeyNotesui.backgroundui.background.separatorPicker separator below input lineui.cursorui.cursor.normalui.cursor.insertui.cursor.selectui.cursor.matchMatching bracket etc.ui.cursor.primaryCursor with primary selectionui.cursor.primary.normalui.cursor.primary.insertui.cursor.primary.selectui.debug.breakpointBreakpoint indicator, found in the gutterui.debug.activeIndicator for the line at which debugging execution is paused at, found in the gutterui.gutterGutterui.gutter.selectedGutter for the line the cursor is onui.linenrLine numbersui.linenr.selectedLine number for the line the cursor is onui.statuslineStatuslineui.statusline.inactiveStatusline (unfocused document)ui.statusline.normalStatusline mode during normal mode (only ifeditor.color-modesis enabled)ui.statusline.insertStatusline mode during insert mode (only ifeditor.color-modesis enabled)ui.statusline.selectStatusline mode during select mode (only ifeditor.color-modesis enabled)ui.statusline.separatorSeparator character in statuslineui.bufferlineStyle for the buffer lineui.bufferline.activeStyle for the active buffer in buffer lineui.bufferline.backgroundStyle for bufferline backgroundui.popupDocumentation popups (e.g. Space + k)ui.popup.infoPrompt for multiple key optionsui.picker.headerHeader row area in pickers with multiple columnsui.picker.header.columnColumn names in pickers with multiple columnsui.picker.header.column.activeThe column name in pickers with multiple columns where the cursor is entering into.ui.windowBorderlines separating splitsui.helpDescription box for commandsui.textDefault text style, command prompts, popup text, etc.ui.text.focusThe currently selected line in the pickerui.text.inactiveSame asui.textbut when the text is inactive (e.g. suggestions)ui.text.infoThe key: command text inui.popup.infoboxesui.text.directoryDirectory names in prompt completionui.virtual.rulerRuler columns (see theeditor.rulersconfig)ui.virtual.whitespaceVisible whitespace charactersui.virtual.indent-guideVertical indent width guidesui.virtual.inlay-hintDefault style for inlay hints of all kindsui.virtual.inlay-hint.parameterStyle for inlay hints of kindparameter(language servers are not required to set a kind)ui.virtual.inlay-hint.typeStyle for inlay hints of kindtype(language servers are not required to set a kind)ui.virtual.wrapSoft-wrap indicator (see theeditor.soft-wrapconfig)ui.virtual.jump-labelStyle for virtual jump labelsui.menuCode and command completion menusui.menu.selectedSelected autocomplete itemui.menu.scrollfgsets thumb color,bgsets track color of scrollbarui.selectionFor selections in the editing areaui.selection.primaryui.highlightHighlighted lines in the picker previewui.highlight.framelineLine at which debugging execution is paused atui.cursorline.primaryThe line of the primary cursor (if cursorline is enabled)ui.cursorline.secondaryThe lines of any other cursors (if cursorline is enabled)ui.cursorcolumn.primaryThe column of the primary cursor (if cursorcolumn is enabled)ui.cursorcolumn.secondaryThe columns of any other cursors (if cursorcolumn is enabled)warningDiagnostics warning (gutter)errorDiagnostics error (gutter)infoDiagnostics info (gutter)hintDiagnostics hint (gutter)diagnosticDiagnostics fallback style (editing area)diagnostic.hintDiagnostics hint (editing area)diagnostic.infoDiagnostics info (editing area)diagnostic.warningDiagnostics warning (editing area)diagnostic.errorDiagnostics error (editing area)diagnostic.unnecessaryDiagnostics with unnecessary tag (editing area)diagnostic.deprecatedDiagnostics with deprecated tag (editing area)tabstopSnippet placeholder