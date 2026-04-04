# Introduction to editor development

# Introduction to editor development
On this page, you will learn:
- Thedesign decisionsbehind the Godot editor.
Thedesign decisionsbehind the Godot editor.
- How to work efficiently on the Godot editor's C++ code.
How to work efficiently on the Godot editor's C++ code.
This guide is aimed at current or future engine contributors.
To create editor plugins in GDScript, seeMaking pluginsinstead.
See also
If you are new to Godot, we recommended you to readGodot's design philosophybefore continuing. Since the Godot editor
is a Godot project written in C++, much of the engine's philosophy applies
to the editor.

## Technical choices
The Godot editor is drawn using Godot's renderer andUI system. It doesnotrely on a toolkit
such as GTK or Qt. This is similar in spirit to software like Blender.
While using toolkits makes it easier to achieve a "native" appearance, they are
also quite heavy and their licensing is not compatible with Godot's.
The editor is fully written in C++. It can't contain any GDScript or C# code.

## Directory structure
The editor's code is fully self-contained in theeditor/folder
of the Godot source repository.
Some editor functionality is also implemented viamodules. Some of these are only enabled in
editor builds to decrease the binary size of export templates. See themodules/folder
in the Godot source repository.
Some important files in the editor are:
- editor/editor_node.cpp:
Main editor initialization file. Effectively the "main scene" of the editor.
editor/editor_node.cpp:
Main editor initialization file. Effectively the "main scene" of the editor.
- editor/project_manager/project_manager.cpp:
Main Project Manager initialization file. Effectively the "main scene" of the Project Manager.
editor/project_manager/project_manager.cpp:
Main Project Manager initialization file. Effectively the "main scene" of the Project Manager.
- editor/scene/canvas_item_editor_plugin.cpp:
The 2D editor viewport and related functionality (toolbar at the top, editing modes, overlaid helpers/panels, …).
editor/scene/canvas_item_editor_plugin.cpp:
The 2D editor viewport and related functionality (toolbar at the top, editing modes, overlaid helpers/panels, …).
- editor/scene/3d/node_3d_editor_plugin.cpp:
The 3D editor viewport and related functionality (toolbar at the top, editing modes, overlaid panels, …).
editor/scene/3d/node_3d_editor_plugin.cpp:
The 3D editor viewport and related functionality (toolbar at the top, editing modes, overlaid panels, …).
- editor/scene/3d/node_3d_editor_gizmos.cpp:
Where the 3D editor gizmos are defined and drawn.
This file doesn't have a 2D counterpart as 2D gizmos are drawn by the nodes themselves.
editor/scene/3d/node_3d_editor_gizmos.cpp:
Where the 3D editor gizmos are defined and drawn.
This file doesn't have a 2D counterpart as 2D gizmos are drawn by the nodes themselves.

## Editor dependencies inscene/files
When working on an editor feature, you may have to modify files in
Godot's GUI nodes, which you can find in thescene/folder.
One rule to keep in mind is that you mustnotintroduce new dependencies toeditor/includes in other folders such asscene/. This applies even if
you use#ifdefTOOLS_ENABLED.
To make the codebase easier to follow and more self-contained, the allowed
dependency order is:
- editor/->scene/->servers/->core/
editor/->scene/->servers/->core/
This means that files ineditor/can depend on includes fromscene/,servers/, andcore/. But, for example, whilescene/can depend on includes
fromservers/andcore/, it cannot depend on includes fromeditor/.
Currently, there are some dependencies toeditor/includes inscene/files, butthey are in the process of being removed.

## Development tips
To iterate quickly on the editor, we recommend to set up a test project andopen it from the command lineafter compiling
the editor. This way, you don't have to go through the Project Manager every
time you start Godot.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.