# PhysicsServer2DManager

# PhysicsServer2DManager
Inherits:Object
A singleton for managingPhysicsServer2Dimplementations.

## Description
PhysicsServer2DManageris the API for registeringPhysicsServer2Dimplementations and for setting the default implementation.
Note:It is not possible to switch physics servers at runtime. This class is only used on startup at the server initialization level, by Godot itself and possibly by GDExtensions.

## Methods

| void | register_server(name:String, create_callback:Callable) |
|---|---|
| void | set_default_server(name:String, priority:int) |

void
register_server(name:String, create_callback:Callable)
void
set_default_server(name:String, priority:int)

## Method Descriptions
voidregister_server(name:String, create_callback:Callable)🔗
Register aPhysicsServer2Dimplementation by passing anameand aCallablethat returns aPhysicsServer2Dobject.
voidset_default_server(name:String, priority:int)🔗
Set the defaultPhysicsServer2Dimplementation to the one identified byname, ifpriorityis greater than the priority of the current default implementation.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.