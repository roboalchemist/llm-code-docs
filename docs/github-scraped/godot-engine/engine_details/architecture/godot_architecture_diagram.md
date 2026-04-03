
# Godot's architecture overview

The following diagram describes the most important aspects of Godot's architecture.
It's not designed to be exhaustive, with the purpose of just giving a high-level overview of
the main components and their relationships to each other.

> **FIGURE**
> :alt: Diagram of Godot's Architecture; divided into three layers (from top to bottom: Scene layer, Server layer, and Drivers & Platform interface layer), with Core and Main separated on the right side since they interact with all layers.
>
> Credit: `Hendrik Brucker <https://github.com/Geometror/godot-architecture-diagram>`__
>
### Scene Layer

The Scene layer is the highest level of Godot's architecture, providing the scene system, which is the main way to build and structure your applications or games.
See [class_SceneTree] / [doc_scene_tree] and [class_Node] for more information.

Corresponding source code: [/scene/* ](https://github.com/godotengine/godot/tree/master/scene)_

### Server Layer

Server components implement most of Godot's subsystems (rendering, audio, physics, etc.). They are singleton objects initialized at engine startup.

[Why does Godot use servers and RIDs? ](https://godotengine.org/article/why-does-godot-use-servers-and-rids)_

Corresponding source code: [/servers/* ](https://github.com/godotengine/godot/tree/master/servers)_

### Drivers / Platform Interface

This layer abstracts low-level platform-specific details, containing drivers for graphics APIs, audio backends and operating system interfaces
(all platform-specific [class_OS] and [class_DisplayServer] implementations).

Corresponding source code: [/drivers/* ](https://github.com/godotengine/godot/tree/master/drivers)_ and [/platform/* ](https://github.com/godotengine/godot/tree/master/platform)_

### Core

The Engine's core contains essential functionality and data structures used throughout the engine,
like [class_Object] and [class_ClassDB], [memory management <doc_core_types>], [containers <doc_core_types>], file I/O, [Variant <doc_variant_class>], and [other utilities <doc_common_engine_methods_and_macros>].

Corresponding source code: [/core/* ](https://github.com/godotengine/godot/tree/master/core)_

### Main

The Main component is responsible for initializing and managing the engine lifecycle, including startup, shutdown, and the main loop. See [class_MainLoop] for more details.

Corresponding source code: [/main/* ](https://github.com/godotengine/godot/tree/master/main)_

