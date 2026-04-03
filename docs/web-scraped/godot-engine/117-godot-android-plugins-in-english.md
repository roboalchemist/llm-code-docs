# Godot Android plugins in English

# Godot Android plugins

## Introduction
Android plugins are powerful tools to extend the capabilities of the Godot engine
by tapping into the functionality provided by Android platforms and ecosystem.
For example in Godot 4, Android plugins are used to support multiple Android-based
XR platforms without encumbering the core codebase with vendor specific code or binaries.

## Android plugin
Version 1 (v1)of the Android plugin system was introduced in Godot 3 and compatible with Godot 4.0 and 4.1.
That version allowed developers to augment the Godot engine with Java, Kotlin and native functionality.
Starting in Godot 4.2, Android plugins built on the v1 architecture are now deprecated.
Instead, Godot 4.2 introduces a newVersion 2 (v2)architecture for Android plugins.

### v2 Architecture
Note
Godot Android plugin leverages theGradle build system.
Building on the previous v1 architecture, Android plugins continue to be derived from theAndroid archive library.
At its core, a Godot Android plugin v2 is an Android library with a dependency on theGodot Android library,
and a custom Android library manifest.
This architecture allows Android plugins to extend the functionality of the engine with:
- Android platform APIs
Android platform APIs
- Android libraries
Android libraries
- Kotlin and Java libraries
Kotlin and Java libraries
- Native libraries (via JNI)
Native libraries (via JNI)
- GDExtension libraries
GDExtension libraries
Each plugin has an init class extending from theGodotPluginclass
which is provided by theGodot Android library.
TheGodotPluginclass provides APIs to access the running Godot instance and hook into its lifecycle. It is loaded at runtime by the Godot engine.

### v2 Packaging format
v1 Android plugins required a customgdapconfiguration file that was used by the Godot Editor to detect and load them.
However this approach had several drawbacks, primary ones being that it lacked flexibility and departed from theexisting
Godot EditorExportPlugin format, delivery and installation flow.
This has been resolved for v2 Android plugins by deprecating thegdappackaging and configuration mechanism in favor of
the existing GodotEditorExportPluginpackaging format.
TheEditorExportPluginAPI in turn has been extended to properly support Android plugins.

## Building a v2 Android plugin
A github project templateis providedathttps://github.com/m4gr3d/Godot-Android-Plugin-Templateas aquickstart for building
Godot Android plugins for Godot 4.2+.
You can follow thetemplate READMEto set up your own Godot Android plugin project.
To provide further understanding, here is a break-down of the steps used to create the project template:
- Create an Android library module usingthese instructions
Create an Android library module usingthese instructions
- Add the Godot Android library as a dependency by updating the module'sgradlebuild file:dependencies {
    implementation("org.godotengine:godot:4.2.0.stable")
}
Add the Godot Android library as a dependency by updating the module'sgradlebuild file:
> dependencies {
    implementation("org.godotengine:godot:4.2.0.stable")
}
```
dependencies {
    implementation("org.godotengine:godot:4.2.0.stable")
}
```
> The Godot Android library ishosted on MavenCentral, and updated for each release.
The Godot Android library ishosted on MavenCentral, and updated for each release.
- CreateGodotAndroidPlugin, an init class for the plugin extendingGodotPlugin.If the plugin exposes Kotlin or Java methods to be called from GDScript, they must be annotated with@UsedByGodot. The name called from GDScriptmust match the method name exactly. There isnocoercingsnake_casetocamelCase. For example, from GDScript:ifEngine.has_singleton("MyPlugin"):varsingleton=Engine.get_singleton("MyPlugin")print(singleton.myPluginFunction("World"))If the plugin usessignals, the init class must return the set of signals used by overridingGodotPlugin::getPluginSignals(). To emit signals, the plugin can use theGodotPlugin::emitSignal(...) method.
CreateGodotAndroidPlugin, an init class for the plugin extendingGodotPlugin.
> If the plugin exposes Kotlin or Java methods to be called from GDScript, they must be annotated with@UsedByGodot. The name called from GDScriptmust match the method name exactly. There isnocoercingsnake_casetocamelCase. For example, from GDScript:ifEngine.has_singleton("MyPlugin"):varsingleton=Engine.get_singleton("MyPlugin")print(singleton.myPluginFunction("World"))If the plugin usessignals, the init class must return the set of signals used by overridingGodotPlugin::getPluginSignals(). To emit signals, the plugin can use theGodotPlugin::emitSignal(...) method.
- If the plugin exposes Kotlin or Java methods to be called from GDScript, they must be annotated with@UsedByGodot. The name called from GDScriptmust match the method name exactly. There isnocoercingsnake_casetocamelCase. For example, from GDScript:ifEngine.has_singleton("MyPlugin"):varsingleton=Engine.get_singleton("MyPlugin")print(singleton.myPluginFunction("World"))
If the plugin exposes Kotlin or Java methods to be called from GDScript, they must be annotated with@UsedByGodot. The name called from GDScriptmust match the method name exactly. There isnocoercingsnake_casetocamelCase. For example, from GDScript:
> ifEngine.has_singleton("MyPlugin"):varsingleton=Engine.get_singleton("MyPlugin")print(singleton.myPluginFunction("World"))
```
if Engine.has_singleton("MyPlugin"):
    var singleton = Engine.get_singleton("MyPlugin")
    print(singleton.myPluginFunction("World"))
```
- If the plugin usessignals, the init class must return the set of signals used by overridingGodotPlugin::getPluginSignals(). To emit signals, the plugin can use theGodotPlugin::emitSignal(...) method.
If the plugin usessignals, the init class must return the set of signals used by overridingGodotPlugin::getPluginSignals(). To emit signals, the plugin can use theGodotPlugin::emitSignal(...) method.
- Update the pluginAndroidManifest.xmlfilewith the following meta-data:<meta-dataandroid:name="org.godotengine.plugin.v2.[PluginName]"android:value="[plugin.init.ClassFullName]"/>
Update the pluginAndroidManifest.xmlfilewith the following meta-data:
> <meta-dataandroid:name="org.godotengine.plugin.v2.[PluginName]"android:value="[plugin.init.ClassFullName]"/>
```
<meta-data
    android:name="org.godotengine.plugin.v2.[PluginName]"
    android:value="[plugin.init.ClassFullName]" />
```
> Where:PluginNameis the name of the pluginplugin.init.ClassFullNameis the full component name (package + class name) of the plugin init class (e.g:org.godotengine.plugin.android.template.GodotAndroidPlugin).
Where:
> PluginNameis the name of the pluginplugin.init.ClassFullNameis the full component name (package + class name) of the plugin init class (e.g:org.godotengine.plugin.android.template.GodotAndroidPlugin).
- PluginNameis the name of the plugin
PluginNameis the name of the plugin
- plugin.init.ClassFullNameis the full component name (package + class name) of the plugin init class (e.g:org.godotengine.plugin.android.template.GodotAndroidPlugin).
plugin.init.ClassFullNameis the full component name (package + class name) of the plugin init class (e.g:org.godotengine.plugin.android.template.GodotAndroidPlugin).
- Create theEditorExportPlugin configurationto package the plugin. The steps used to create the configuration can be seen in thePackaging a v2 Android pluginsection.
Create theEditorExportPlugin configurationto package the plugin. The steps used to create the configuration can be seen in thePackaging a v2 Android pluginsection.

### Building a v2 Android plugin with GDExtension capabilities
Similar to GDNative support in v1 Android plugins, v2 Android plugins support the ability to integrate GDExtension capabilities.
A github project template is provided athttps://github.com/m4gr3d/GDExtension-Android-Plugin-Templateas a quickstart for building
GDExtension Android plugins for Godot 4.2+.
You can follow thetemplate's READMEto set up your own Godot Android plugin project.

### Migrating a v1 Android plugin to v2
Use the following steps if you have a v1 Android plugin you want to migrate to v2:
- Update the plugin's manifest file:Change theorg.godotengine.plugin.v1prefix toorg.godotengine.plugin.v2
Update the plugin's manifest file:
> Change theorg.godotengine.plugin.v1prefix toorg.godotengine.plugin.v2
- Change theorg.godotengine.plugin.v1prefix toorg.godotengine.plugin.v2
Change theorg.godotengine.plugin.v1prefix toorg.godotengine.plugin.v2
- Update the Godot Android library build dependency:You can continue using thegodot-lib.<version>.<status>.aarbinary fromGodot's download pageif that's your preference. Make sure it's updated to the latest stable version.Or you can switch to the MavenCentral provided dependency:
Update the Godot Android library build dependency:
> You can continue using thegodot-lib.<version>.<status>.aarbinary fromGodot's download pageif that's your preference. Make sure it's updated to the latest stable version.Or you can switch to the MavenCentral provided dependency:
- You can continue using thegodot-lib.<version>.<status>.aarbinary fromGodot's download pageif that's your preference. Make sure it's updated to the latest stable version.
You can continue using thegodot-lib.<version>.<status>.aarbinary fromGodot's download pageif that's your preference. Make sure it's updated to the latest stable version.
- Or you can switch to the MavenCentral provided dependency:
Or you can switch to the MavenCentral provided dependency:
```
dependencies {
    implementation("org.godotengine:godot:4.2.0.stable")
}
```
- After updating the Godot Android library dependency, sync or build the plugin and resolve any compile errors:TheGodotinstance provided byGodotPlugin::getGodot()no longer has access to anandroid.content.Contextreference. UseGodotPlugin::getActivity()instead.
After updating the Godot Android library dependency, sync or build the plugin and resolve any compile errors:
> TheGodotinstance provided byGodotPlugin::getGodot()no longer has access to anandroid.content.Contextreference. UseGodotPlugin::getActivity()instead.
- TheGodotinstance provided byGodotPlugin::getGodot()no longer has access to anandroid.content.Contextreference. UseGodotPlugin::getActivity()instead.
TheGodotinstance provided byGodotPlugin::getGodot()no longer has access to anandroid.content.Contextreference. UseGodotPlugin::getActivity()instead.
- Delete thegdapconfiguration file(s) and follow the instructions in thePackaging a v2 Android pluginsection to set up the plugin configuration.
Delete thegdapconfiguration file(s) and follow the instructions in thePackaging a v2 Android pluginsection to set up the plugin configuration.

## Packaging a v2 Android plugin
As mentioned, a v2 Android plugin is now provided to the Godot Editor as anEditorExportPluginplugin, so it shares a lot of thesame packaging steps.
- Add the plugin output binaries within the plugin directory (e.g: inaddons/<plugin_name>/)
Add the plugin output binaries within the plugin directory (e.g: inaddons/<plugin_name>/)
- Add thetool scriptfor the export functionality within the plugin directory (e.g: inaddons/<plugin_name>/)The created script must be a@toolscript, or else it will not work properlyThe export tool script is used to configure the Android plugin and hook it within the Godot Editor's export process. It should look something like this:
Add thetool scriptfor the export functionality within the plugin directory (e.g: inaddons/<plugin_name>/)
> The created script must be a@toolscript, or else it will not work properlyThe export tool script is used to configure the Android plugin and hook it within the Godot Editor's export process. It should look something like this:
- The created script must be a@toolscript, or else it will not work properly
The created script must be a@toolscript, or else it will not work properly
- The export tool script is used to configure the Android plugin and hook it within the Godot Editor's export process. It should look something like this:
The export tool script is used to configure the Android plugin and hook it within the Godot Editor's export process. It should look something like this:
```
@tool
extends EditorPlugin

# A class member to hold the editor export plugin during its lifecycle.
var export_plugin : AndroidExportPlugin

func _enter_tree():
    # Initialization of the plugin goes here.
    export_plugin = AndroidExportPlugin.new()
    add_export_plugin(export_plugin)

func _exit_tree():
    # Clean-up of the plugin goes here.
    remove_export_plugin(export_plugin)
    export_plugin = null

class AndroidExportPlugin extends EditorExportPlugin:
    # Plugin's name.
    var _plugin_name = "<plugin_name>"

    # Specifies which platform is supported by the plugin.
    func _supports_platform(platform):
        if platform is EditorExportPlatformAndroid:
            return true
        return false

    # Return the paths of the plugin's AAR binaries relative to the 'addons' directory.
    func _get_android_libraries(platform, debug):
        if debug:
            return PackedStringArray(["<paths_to_debug_android_plugin_aar_binaries>"])
        else:
            return PackedStringArray(["<paths_to_release_android_plugin_aar_binaries>"])

    # Return the plugin's name.
    func _get_name():
        return _plugin_name

- Here are the set of `EditorExportPlugin APIs <https://docs.godotengine.org/en/stable/classes/class_editorexportplugin.html>`_ most relevant to use in this tool script:

    - `_supports_platform <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-supports-platform>`_: returns ``true`` if the plugin supports the given platform. For Android plugins, this must return ``true`` when ``platform`` is `EditorExportPlatformAndroid <https://docs.godotengine.org/en/stable/classes/class_editorexportplatformandroid.html>`_
    - `_get_android_libraries <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-libraries>`_: retrieve the local paths of the Android libraries binaries (AAR files) provided by the plugin
    - `_get_android_dependencies <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-dependencies>`_: retrieve the set of Android maven dependencies (e.g: `org.godot.example:my-plugin:0.0.0`) provided by the plugin
    - `_get_android_dependencies_maven_repos <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-dependencies-maven-repos>`_: retrieve the urls of the maven repos for the android dependencies provided by ``_get_android_dependencies``
    - `_get_android_manifest_activity_element_contents <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-manifest-activity-element-contents>`_: update the contents of the `<activity>` element in the generated Android manifest
    - `_get_android_manifest_application_element_contents <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-manifest-application-element-contents>`_: update the contents of the `<application>` element in the generated Android manifest
    - `_get_android_manifest_element_contents <https://docs.godotengine.org/en/latest/classes/class_editorexportplugin.html#class-editorexportplugin-method-get-android-manifest-element-contents>`_: update the contents of the `<manifest>` element in the generated Android manifest

    The ``_get_android_manifest_*`` methods allow the plugin to automatically provide changes
    to the app's manifest which are preserved when the Godot Editor is updated, resolving a long standing issue with v1 Android plugins.
```
- Create aplugin.cfg. This is an INI file with metadata about your plugin:
Create aplugin.cfg. This is an INI file with metadata about your plugin:
```
[plugin]

name="<plugin_name>"
description="<plugin_description>"
author="<plugin_author>"
version="<plugin_version>"
script="<relative_path_to_the_export_tool_script>"
```
For reference, here is thefolder structure for the Godot Android plugin project template.
At build time, the contents of theexport_scripts_templatedirectory as well as the generated plugin binaries are copied to theaddons/<plugin_name>directory:
```
export_scripts_template/
|
+--export_plugin.gd         # export plugin tool script
|
+--plugin.cfg               # plugin INI file
```

### Packaging a v2 Android plugin with GDExtension capabilities
For GDExtension, we follow the same steps as forPackaging a v2 Android pluginand add theGDExtension config filein
the same location asplugin.cfg.
For reference, here is thefolder structure for the GDExtension Android plugin project template.
At build time, the contents of theexport_scripts_templatedirectory as well as the generated plugin binaries are copied to theaddons/<plugin_name>directory:
```
export_scripts_template/
|
+--export_plugin.gd         # export plugin tool script
|
+--plugin.cfg               # plugin INI file
|
+--plugin.gdextension       # GDExtension config file
```
Here is what theplugin.gdextensionconfig file should look like:
```
[configuration]

entry_symbol = "plugin_library_init"
compatibility_minimum = "4.2"
android_aar_plugin = true

[libraries]

android.debug.arm64 = "res://addons/GDExtensionAndroidPluginTemplate/bin/debug/arm64-v8a/libGDExtensionAndroidPluginTemplate.so"
android.release.arm64 = "res://addons/GDExtensionAndroidPluginTemplate/bin/release/arm64-v8a/libGDExtensionAndroidPluginTemplate.so"
...
```
Of note is theandroid_aar_pluginfield that specifies this GDExtension module is provided as part of a v2 Android plugin.
During the export process, this will indicate to the Godot Editor that the GDExtension native shared libraries are exported by the Android plugin AAR binaries.
For GDExtension Android plugins, the plugin init class must overrideGodotPlugin::getPluginGDExtensionLibrariesPaths(),
and return the paths to the bundled GDExtension libraries config files (*.gdextension).
The paths must be relative to the Android library'sassetsdirectory.
At runtime, the plugin will provide these paths to the Godot engine which will use them to load and initialize the bundled GDExtension libraries.

## Using a v2 Android plugin
Note
- Godot 4.2 or higher is required
Godot 4.2 or higher is required
- v2 Android plugin requires the use of theGradle build process.
v2 Android plugin requires the use of theGradle build process.
- The provided github project templates include demo Godot projects for quick testing.
The provided github project templates include demo Godot projects for quick testing.
- Copy the plugin's output directory (addons/<plugin_name>) to the target Godot project's directory
Copy the plugin's output directory (addons/<plugin_name>) to the target Godot project's directory
- Open the project in the Godot Editor; the Editor should detect the plugin
Open the project in the Godot Editor; the Editor should detect the plugin
- Navigate toProject->ProjectSettings...->Plugins, and ensure the plugin is enabled
Navigate toProject->ProjectSettings...->Plugins, and ensure the plugin is enabled
- Install the Godot Android build template by clicking onProject->InstallAndroidBuildTemplate...
Install the Godot Android build template by clicking onProject->InstallAndroidBuildTemplate...
- Navigate toProject->Export...
Navigate toProject->Export...
- In theExportwindow, create anAndroidexportpreset
In theExportwindow, create anAndroidexportpreset
- In theAndroidexportpreset, scroll toGradleBuildand setUseGradleBuildtotrue
In theAndroidexportpreset, scroll toGradleBuildand setUseGradleBuildtotrue
- Update the project's scripts as needed to access the plugin's functionality. For example:
Update the project's scripts as needed to access the plugin's functionality. For example:
```
if Engine.has_singleton("MyPlugin"):
        var singleton = Engine.get_singleton("MyPlugin")
        print(singleton.myPluginFunction("World"))
```
- Connect an Android device to your machine and run the project on it
Connect an Android device to your machine and run the project on it

### Using a v2 Android plugin as an Android library
Since they are also Android libraries, Godot v2 Android plugins can be stripped from theirEditorExportPluginpackaging and provided as rawAARbinaries for use as libraries alongside theGodot Android libraryby Android apps.
If targeting this use-case, make sure to include additional instructions for how theAARbinaries should be included (e.g: custom additions to the Android app's manifest).

## Reference implementations
- Godot Android Plugins Samples
Godot Android Plugins Samples
- Godot Android Plugin Template
Godot Android Plugin Template
- GDExtension Android Plugin Template
GDExtension Android Plugin Template
- Godot OpenXR Loaders
Godot OpenXR Loaders

## Tips and Guidelines

### Simplify access to the exposed Java / Kotlin APIs
To make it easier to access the exposed Java / Kotlin APIs in the Godot Editor, it's recommended to
provide one (or multiple) gdscript wrapper class(es) for your plugin users to interface with.
For example:
```
class_name PluginInterface extends Object

## Interface used to access the functionality provided by this plugin.

var _plugin_name = "GDExtensionAndroidPluginTemplate"
var _plugin_singleton

func _init():
    if Engine.has_singleton(_plugin_name):
        _plugin_singleton = Engine.get_singleton(_plugin_name)
    else:
        printerr("Initialization error: unable to access the java logic")

## Print a 'Hello World' message to the logcat.
func helloWorld():
    if _plugin_singleton:
        _plugin_singleton.helloWorld()
    else:
        printerr("Initialization error")
```

### Support using the GDExtension functionality in the Godot Editor
If planning to use the GDExtension functionality in the Godot Editor, it is recommended that the
GDExtension's native binaries are compiled not just for Android, but also for the OS onto which
developers / users intend to run the Godot Editor. Not doing so may prevent developers /
users from writing code that accesses the plugin from within the Godot Editor.
This may involve creating dummy plugins for the host OS just so the API is published to the
editor. You can use thegodot-cpp-templategithub template for reference on how to do so.

### Supported data types
All data types are supported. Common types are mapped to their Godot equivalents
(for example,String[]is mapped toPackedStringArray()), but for other types, you can useJavaClassWrapperto access it.

### Godot crashes upon load
Checkadb logcatfor possible problems.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.