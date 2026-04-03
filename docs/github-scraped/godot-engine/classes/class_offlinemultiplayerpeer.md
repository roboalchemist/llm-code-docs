:github_url: hide



# OfflineMultiplayerPeer

**Inherits:** [MultiplayerPeer<class_MultiplayerPeer>] **<** [PacketPeer<class_PacketPeer>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

A [MultiplayerPeer<class_MultiplayerPeer>] which is always connected and acts as a server.


## Description

This is the default [MultiplayerAPI.multiplayer_peer<class_MultiplayerAPI_property_multiplayer_peer>] for the [Node.multiplayer<class_Node_property_multiplayer>]. It mimics the behavior of a server with no peers connected.

This means that the [SceneTree<class_SceneTree>] will act as the multiplayer authority by default. Calls to [MultiplayerAPI.is_server()<class_MultiplayerAPI_method_is_server>] will return `true`, and calls to [MultiplayerAPI.get_unique_id()<class_MultiplayerAPI_method_get_unique_id>] will return [MultiplayerPeer.TARGET_PEER_SERVER<class_MultiplayerPeer_constant_TARGET_PEER_SERVER>].

