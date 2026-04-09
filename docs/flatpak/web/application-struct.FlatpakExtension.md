flatpak::application
# Struct FlatpakExtension 
Source 

```
pub struct FlatpakExtension {}
```

## Fields§
§`extension_directory: String`

The directory where the extension is mounted. If the extension point is for an application,
this path is relative to /app, otherwise it is relative to /usr.
§`bundle: Option<bool>`

If this is true, then the data created in the extension directory is omitted from the result,
and instead packaged in a separate extension.
§`remove_after_build: Option<bool>`

If this is true, the extension is removed during when finishing.
This is only interesting for extensions in the add-build-extensions property.
§`autodelete: Option<bool>`

Whether to automatically delete extensions matching this extension point
when deleting a ‘related’ application or runtime.
§`no_autodownload: Option<bool>`

Whether to automatically download extensions matching this extension point
when updating or installing a ‘related’ application or runtime.
§`subdirectories: Option<bool>`

If this key is set to true, then flatpak will look for extensions whose name is a
prefix of the extension point name, and mount them at the corresponding
name below the subdirectory.
§`add_ld_path: Option<String>`

A path relative to the extension point directory that will be appended to LD_LIBRARY_PATH.
§`download_if: Option<String>`

A list of conditions, separated by semi-colons, that must be true for the extension
to be auto-downloaded.
These are the supported conditions:
active-gl-driver
Is true if the name of the active GL driver matches the extension point basename.
active-gtk-theme
Is true if the name of the current GTK theme (via org.gnome.desktop.interface GSetting)
matches the extension point basename.
have-intel-gpu
Is true if the i915 kernel module is loaded.
on-xdg-desktop-*
Is true if the suffix (case-insensitively) is in the XDG_CURRENT_DESKTOP env var.
For example on-xdg-desktop-GNOME-classic.
§`enable_if: Option<String>`

A list of conditions, separated by semi-colons, that must be true for the extension to be
enabled. See download_if for available conditions.
§`merge_dirs: Option<String>`

A list of relative paths of directories below the extension point directory that will be merged.
§`subdirectory_suffix: Option<String>`

A suffix that gets appended to the directory name.
This is very useful when the extension point naming scheme is “reversed”.
For example, an extension point for GTK+ themes would be /usr/share/themes/$NAME/gtk-3.0,
which could be achieved using subdirectory-suffix=gtk-3.0.
§`locale_subset: Option<bool>`

If set, then the extensions are partially downloaded by default, based on the currently
configured locales. This means that the extension contents should be
a set of directories with the language code as name.
§`version: Option<String>`

The branch to use when looking for the extension.
If this is not specified, it defaults to the branch of the application or
runtime that the extension point is for.
§`versions: Option<String>`

The branches to use when looking for the extension.
If this is not specified, it defaults to the branch of the application or
runtime that the extension point is for.

## Trait Implementations§