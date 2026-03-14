flatpak::application
# Struct FlatpakApplication 
Source 

```
pub struct FlatpakApplication {}
```

## Fields§
§`format: FlatpakManifestFormat`§`app_name: String`

Name of the application.
§`app_id: String`

A string defining the application id.
Both names (app-id and id) are accepted.
§`id: String`§`branch: String`

The branch to use when exporting the application.
If this is unset the defaults come from the default-branch option.

This key overrides both the default-branch key, and the –default-branch commandline option.
Unless you need a very specific branchname (like for a runtime or an extension) it is recommended
to use the default-branch key instead, because you can then override the default using
–default-branch when building for instance a test build.
§`default_branch: String`

The default branch to use when exporting the application. Defaults to master.
This key can be overridden by the –default-branch commandline option.
§`collection_id: String`

The collection ID of the repository, defaults to being unset.
Setting a globally unique collection ID allows the apps in the
repository to be shared over peer to peer systems without needing further configuration.
If building in an existing repository, the collection ID must match the existing
configured collection ID for that repository.
§`runtime: String`

The name of the runtime that the application uses.
§`runtime_version: String`

The version of the runtime that the application uses, defaults to master.
§`sdk: String`

The name of the development runtime that the application builds with.
§`sdk_extensions: Vec<String>`

The name of the development extensions that the application requires to build.
§`var: String`

Initialize the (otherwise empty) writable /var in the build with a copy of this runtime.
§`metadata: String`

Use this file as the base metadata file when finishing.
§`build_runtime: Option<bool>`

Build a new runtime instead of an application.
§`build_extension: Option<bool>`

Whether the manifest describes an extension to be used by other manifests.
Extensions can be used to bundle programming langages and their associated
tools, for example.
§`base: String`

Start with the files from the specified application.
This can be used to create applications that extend another application.
§`base_version: String`

Use this specific version of the application specified in base.
If unspecified, this uses the value specified in branch
§`base_extensions: Vec<String>`

Install these extra extensions from the base application when
initializing the application directory.
§`separate_locales: Option<bool>`

Separate out locale files and translations to an extension runtime. Defaults to true.
§`appstream_compose: Option<bool>`

Run appstream-compose during cleanup phase. Defaults to true.
§`inherit_extensions: Vec<String>`

Inherit these extra extensions points from the base application or
sdk when finishing the build.
§`inherit_sdk_extensions: Vec<String>`

Inherit these extra extensions points from the base application or sdk
when finishing the build, but do not inherit them into the platform.
§`build_options: Option<FlatpakBuildOptions>`

Inherit these extra extensions points from the base application or sdk when finishing the build,
but do not inherit them into the platform.
§`command: Option<String>`

The name of the command that the flatpak should run on execution.
§`tags: Vec<String>`

Add these tags to the metadata file.
§`add_extensions: BTreeMap<String, FlatpakExtension>`

This is a dictionary of extension objects.
The key is the name of the extension.
§`add_build_extensions: BTreeMap<String, FlatpakExtension>`

This is a dictionary of extension objects similar to add-extensions.
The main difference is that the extensions are added early and are
available for use during the build.
§`cleanup: Vec<String>`

An array of file patterns that should be removed at the end.
Patterns starting with / are taken to be full pathnames (without the /app prefix),
otherwise they just match the basename.
§`cleanup_commands: Vec<String>`

An array of commandlines that are run during the cleanup phase.
§`cleanup_platform: Vec<String>`

Extra files to clean up in the platform.
§`cleanup_platform_commands: Vec<String>`

An array of commandlines that are run during the cleanup phase of the platform.
§`prepare_platform_commands: Vec<String>`

An array of commandlines that are run after importing the base platform,
but before applying the new files from the sdk. This is a good place to e.g. delete
things from the base that may conflict with the files added in the sdk.
§`finish_args: Vec<String>`

An array of arguments passed to the flatpak build-finish command.
§`rename_desktop_file: String`

Any desktop file with this name will be renamed to a name
based on id during the cleanup phase.
§`rename_appdata_file: String`

Any appdata file with this name will be renamed to a name based
on id during the cleanup phase.
§`rename_icon: String`

Any icon with this name will be renamed to a name based on id during
the cleanup phase. Note that this is the icon name, not the full filenames,
so it should not include a filename extension.
§`appdata_license: String`

Replace the appdata project-license field with this string.
This is useful as the upstream license is typically only about
the application itself, whereas the bundled app can contain other
licenses too.
§`copy_icon: Option<bool>`

If rename-icon is set, keep a copy of the old icon file.
§`desktop_file_name_prefix: String`

This string will be prefixed to the Name key in the main application desktop file.
§`desktop_file_name_suffix: String`

This string will be suffixed to the Name key in the main application desktop file.
§`modules: Vec<FlatpakModuleItem>`

An array of strings specifying the modules to be built in order.
String members in the array are interpreted as the name of a separate
json or yaml file that contains a module. See below for details.

## Implementations§