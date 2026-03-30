# Crate cursive 
Source 
## Modules§
alignTools to control view alignment.backendDefine the backend trait for actual terminal interaction.backendsDefine backends using common libraries.bufferOutput bufferbuilderBuild views from configuration.directionDirection-related structures.eventUser-input events and their effects.loggerLogging utilities.menuBuild menu trees.reexportsRe-export crates used in the public APIstyleHandle colors and styles in the UI.themeTheming support for a consistent UI.traitsCommonly used traits bundled for easy import.utilsToolbox to make text layout easier.vecPoints on the 2D character grid.viewBase elements required to build views.viewsVarious views to use when creating the layout.
## Macros§
fn_blueprint`builder`Define a macro for a variable builder.immut1Macro to wrap a `FnMut` with 1 argument into a `Fn`.immut2Macro to wrap a `FnMut` with 2 arguments into a `Fn`.immut3Macro to wrap a `FnMut` with 3 arguments into a `Fn`.impl_enabledA macro to help with creating toggleable views.impl_scrollerImplements the `Scroller` trait for any type.inner_gettersConvenient macro to implement the getters for inner `View` in
`ViewWrapper`.manual_blueprint`builder`Define a blueprint to manually build this view from a config file.once1Macro to wrap a `FnOnce` with 1 argument into a `FnMut`.submitEnter an element into the plugin registry corresponding to its type.wrap_implConvenient macro to implement the `ViewWrapper` trait.
## Structs§
CursiveCentral part of the cursive library.CursiveRunnableA runnable wrapper around `Cursive`, bundling the backend initializer.CursiveRunnerEvent loop runner for a cursive instance.DumpRepresents a dump of everything from a `Cursive` instance.PrinterConvenient interface to draw on a subset of the screen.RectA non-empty rectangle on the 2D grid.XYA generic structure with a value for each axis.
## Traits§
CursiveExtExtension trait for the `Cursive` root to simplify initialization.ViewMain trait defining a view behaviour.WithGeneric trait to enable chainable API
## Functions§
crossterm`crossterm-backend`Creates a new Cursive root using a crossterm backend.defaultCreates a new Cursive root using one of the enabled backends.dummyCreates a new Cursive root using a dummy backend.pancurses`pancurses-backend`Creates a new Cursive root using a pancurses backend.termion`termion-backend`Creates a new Cursive root using a termion backend.
## Type Aliases§
CbSinkConvenient alias to the result of `Cursive::cb_sink`.ScreenIdIdentifies a screen in the cursive root.Vec2Simple 2D size, in cells.
## Attribute Macros§
blueprintDefines a blueprint for creating a view from config.callback_helpersGenerate two helper functions to help working with cursive blueprints.