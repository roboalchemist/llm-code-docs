# GDExtensionManager

# GDExtensionManager
Inherits:Object
Provides access to GDExtension functionality.

## Description
The GDExtensionManager loads, initializes, and keeps track of all availableGDExtensionlibraries in the project.
Note:Do not worry about GDExtension unless you know what you are doing.

## Tutorials
- GDExtension overview
GDExtension overview
- GDExtension example in C++
GDExtension example in C++

## Methods

| GDExtension | get_extension(path:String) |
|---|---|
| PackedStringArray | get_loaded_extensions()const |
| bool | is_extension_loaded(path:String)const |
| LoadStatus | load_extension(path:String) |
| LoadStatus | load_extension_from_function(path:String, init_func:constGDExtensionInitializationFunction*) |
| LoadStatus | reload_extension(path:String) |
| LoadStatus | unload_extension(path:String) |

GDExtension
get_extension(path:String)
PackedStringArray
get_loaded_extensions()const
bool
is_extension_loaded(path:String)const
LoadStatus
load_extension(path:String)
LoadStatus
load_extension_from_function(path:String, init_func:constGDExtensionInitializationFunction*)
LoadStatus
reload_extension(path:String)
LoadStatus
unload_extension(path:String)

## Signals
extension_loaded(extension:GDExtension)🔗
Emitted after the editor has finished loading a new extension.
Note:This signal is only emitted in editor builds.
extension_unloading(extension:GDExtension)🔗
Emitted before the editor starts unloading an extension.
Note:This signal is only emitted in editor builds.
extensions_reloaded()🔗
Emitted after the editor has finished reloading one or more extensions.

## Enumerations
enumLoadStatus:🔗
LoadStatusLOAD_STATUS_OK=0
The extension has loaded successfully.
LoadStatusLOAD_STATUS_FAILED=1
The extension has failed to load, possibly because it does not exist or has missing dependencies.
LoadStatusLOAD_STATUS_ALREADY_LOADED=2
The extension has already been loaded.
LoadStatusLOAD_STATUS_NOT_LOADED=3
The extension has not been loaded.
LoadStatusLOAD_STATUS_NEEDS_RESTART=4
The extension requires the application to restart to fully load.

## Method Descriptions
GDExtensionget_extension(path:String)🔗
Returns theGDExtensionat the given filepath, ornullif it has not been loaded or does not exist.
PackedStringArrayget_loaded_extensions()const🔗
Returns the file paths of all currently loaded extensions.
boolis_extension_loaded(path:String)const🔗
Returnstrueif the extension at the given filepathhas already been loaded successfully. See alsoget_loaded_extensions().
LoadStatusload_extension(path:String)🔗
Loads an extension by absolute file path. Thepathneeds to point to a validGDExtension. ReturnsLOAD_STATUS_OKif successful.
LoadStatusload_extension_from_function(path:String, init_func:constGDExtensionInitializationFunction*)🔗
Loads the extension already in address space via the given path and initialization function. Thepathneeds to be unique and start with"libgodot://". ReturnsLOAD_STATUS_OKif successful.
LoadStatusreload_extension(path:String)🔗
Reloads the extension at the given file path. Thepathneeds to point to a validGDExtension, otherwise this method may return eitherLOAD_STATUS_NOT_LOADEDorLOAD_STATUS_FAILED.
Note:You can only reload extensions in the editor. In release builds, this method always fails and returnsLOAD_STATUS_FAILED.
LoadStatusunload_extension(path:String)🔗
Unloads an extension by file path. Thepathneeds to point to an already loadedGDExtension, otherwise this method returnsLOAD_STATUS_NOT_LOADED.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.