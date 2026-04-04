# NavigationServer2DManager in English

# NavigationServer2DManager

Inherits:Object
A singleton for managingNavigationServer2Dimplementations.

## Description

NavigationServer2DManageris the API for registeringNavigationServer2Dimplementations and setting the default implementation.
Note:It is not possible to switch servers at runtime. This class is only used on startup at the server initialization level.

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
Registers aNavigationServer2Dimplementation by passing anameand aCallablethat returns aNavigationServer2Dobject.
voidset_default_server(name:String, priority:int)🔗
Sets the defaultNavigationServer2Dimplementation to the one identified byname, ifpriorityis greater than the priority of the current default implementation.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
