# Scene Unique Nodes in English

# Scene Unique Nodes

## Introduction

Usingget_node()to reference nodes from a script can sometimes be fragile.
If you move a button in a UI scene from one panel to another, the button's node
path changes, and if a script usesget_node()with a hard-coded node path,
the script will not be able to find the button anymore.
In situations like this, the node can be turned into a scene
unique node to avoid having to update the script every time
the node's path is changed.

## Creation and usage

There are two ways to create a scene unique node.
In the Scene tree dock, right-click on a node and selectAccess as Unique Namein the context menu.
After selecting the option, the node will now have a percent symbol (%) next
to its name in the scene tree:
You can also do this while renaming the node by adding "%" to the beginning of the name.
Once you confirm, the percent symbol will appear next to its name.
You can now use the node in your script. For example, you can reference it with
aget_node()method call by typing the % symbol, followed by the node's
name:

```
get_node("%RedButton").text = "Hello"
%RedButton.text = "Hello" # Shorter syntax
```

```
GetNode<Button>("%RedButton").Text = "Hello";
```

## Same-scene limitation

A scene unique node can only be retrieved by a node inside the same scene. To
demonstrate this limitation, consider this examplePlayerscene that
instances aSwordscene:
Here are the results ofget_node()calls inside thePlayerscript:

- get_node("%Eyes")returns theEyesnode.
get_node("%Eyes")returns theEyesnode.
- get_node("%Hilt")returnsnull.
get_node("%Hilt")returnsnull.
These are the results ofget_node()calls inside theSwordscript:
- get_node("%Eyes")returnsnull.
get_node("%Eyes")returnsnull.
- get_node("%Hilt")returns theHiltnode.
get_node("%Hilt")returns theHiltnode.
If a script has access to a node in another scene, it can callget_node()on
that node to get scene unique nodes from that node's scene. This also works in a
node path, which avoids multipleget_node()calls. Here are two ways to get
theHiltnode from thePlayerscript using scene unique nodes:
- get_node("Hand/Sword").get_node("%Hilt")returns theHiltnode.
get_node("Hand/Sword").get_node("%Hilt")returns theHiltnode.
- get_node("Hand/Sword/%Hilt")also returns theHiltnode.
get_node("Hand/Sword/%Hilt")also returns theHiltnode.
Scene unique names don't only work at the end of a node path. They can be used
in the middle to navigate from one node to another. For example, theSwordnode
is marked as a scene unique node in thePlayerscene, so this is possible:
- get_node("%Sword/%Hilt")returns theHiltnode.
get_node("%Sword/%Hilt")returns theHiltnode.

## Alternatives

Scene unique nodes are a useful tool to navigate a scene. However, there are
some situations where other techniques may be better.
AGroupallows locating a node (or a group of many nodes)
from any other node, no matter what scene the two nodes are located in.
ASingleton (Autoload)is an always loaded node
that can be accessed directly by any node regardless of the scene. These are useful
when some data or functionality is shared globally.
Node.find_child()finds a node by name
without knowing its full path. This seems similar to a scene unique node, but
this method is able to find nodes in nested scenes, and doesn't require marking
the node in the scene editor in any way. However, this method is slow. Scene
unique nodes are cached by Godot and are fast to retrieve, but each time the
method is called,find_child()needs to check every descendant (every child,
grandchild, and so on).

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
