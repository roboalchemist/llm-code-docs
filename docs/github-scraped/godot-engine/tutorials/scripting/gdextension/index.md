:allow_comments: False


# The GDExtension system

**GDExtension** is a Godot-specific technology that lets the engine interact with
native [shared libraries ](https://en.wikipedia.org/wiki/Library_(computing)#Shared_libraries)_
at runtime. You can use it to run native code without compiling it with the engine.

> **NOTE**
> :ref:`GDScript <doc_gdscript>`.
>
This section describes how GDExtension works, and is generally aimed at people wanting to make a GDExtension from
scratch, for example to create language bindings. If you want to use existing language bindings, please refer to other
articles instead, such as the articles about [C++ (godot-cpp) <doc_godot_cpp>] or one of the
[community-made ones <doc_what_is_gdnative_third_party_bindings>].

> **TOCTREE**
> :maxdepth: 1
> :name: toc-tutorials-gdextension
>
> what_is_gdextension
> gdextension_file
> gdextension_interface_json_file
> gdextension_c_example
>