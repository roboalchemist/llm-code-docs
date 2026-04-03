:github_url: hide



# WebRTCPeerConnectionExtension

**Inherits:** [WebRTCPeerConnection<class_WebRTCPeerConnection>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

> **CONTAINER**
>
	There is currently no description for this class. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                             | :ref:`_add_ice_candidate<class_WebRTCPeerConnectionExtension_private_method__add_ice_candidate>`\ (\ p_sdp_mid_name\: :ref:`String<class_String>`, p_sdp_mline_index\: :ref:`int<class_int>`, p_sdp_name\: :ref:`String<class_String>`\ ) |virtual| |required| |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                                                            | :ref:`_close<class_WebRTCPeerConnectionExtension_private_method__close>`\ (\ ) |virtual| |required|                                                                                                                                                            |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`WebRTCDataChannel<class_WebRTCDataChannel>`                 | :ref:`_create_data_channel<class_WebRTCPeerConnectionExtension_private_method__create_data_channel>`\ (\ p_label\: :ref:`String<class_String>`, p_config\: :ref:`Dictionary<class_Dictionary>`\ ) |virtual| |required|                                         |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                             | :ref:`_create_offer<class_WebRTCPeerConnectionExtension_private_method__create_offer>`\ (\ ) |virtual| |required|                                                                                                                                              |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`ConnectionState<enum_WebRTCPeerConnection_ConnectionState>` | :ref:`_get_connection_state<class_WebRTCPeerConnectionExtension_private_method__get_connection_state>`\ (\ ) |virtual| |required| |const|                                                                                                                      |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`GatheringState<enum_WebRTCPeerConnection_GatheringState>`   | :ref:`_get_gathering_state<class_WebRTCPeerConnectionExtension_private_method__get_gathering_state>`\ (\ ) |virtual| |required| |const|                                                                                                                        |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`SignalingState<enum_WebRTCPeerConnection_SignalingState>`   | :ref:`_get_signaling_state<class_WebRTCPeerConnectionExtension_private_method__get_signaling_state>`\ (\ ) |virtual| |required| |const|                                                                                                                        |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                             | :ref:`_initialize<class_WebRTCPeerConnectionExtension_private_method__initialize>`\ (\ p_config\: :ref:`Dictionary<class_Dictionary>`\ ) |virtual| |required|                                                                                                  |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                             | :ref:`_poll<class_WebRTCPeerConnectionExtension_private_method__poll>`\ (\ ) |virtual| |required|                                                                                                                                                              |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                             | :ref:`_set_local_description<class_WebRTCPeerConnectionExtension_private_method__set_local_description>`\ (\ p_type\: :ref:`String<class_String>`, p_sdp\: :ref:`String<class_String>`\ ) |virtual| |required|                                                 |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>`                             | :ref:`_set_remote_description<class_WebRTCPeerConnectionExtension_private_method__set_remote_description>`\ (\ p_type\: :ref:`String<class_String>`, p_sdp\: :ref:`String<class_String>`\ ) |virtual| |required|                                               |
> +-------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



[Error<enum_@GlobalScope_Error>] **_add_ice_candidate**\ (\ p_sdp_mid_name\: [String<class_String>], p_sdp_mline_index\: [int<class_int>], p_sdp_name\: [String<class_String>]\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__add_ice_candidate>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



|void| **_close**\ (\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__close>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[WebRTCDataChannel<class_WebRTCDataChannel>] **_create_data_channel**\ (\ p_label\: [String<class_String>], p_config\: [Dictionary<class_Dictionary>]\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__create_data_channel>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Error<enum_@GlobalScope_Error>] **_create_offer**\ (\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__create_offer>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[ConnectionState<enum_WebRTCPeerConnection_ConnectionState>] **_get_connection_state**\ (\ ) |virtual| |required| |const| [🔗<class_WebRTCPeerConnectionExtension_private_method__get_connection_state>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[GatheringState<enum_WebRTCPeerConnection_GatheringState>] **_get_gathering_state**\ (\ ) |virtual| |required| |const| [🔗<class_WebRTCPeerConnectionExtension_private_method__get_gathering_state>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[SignalingState<enum_WebRTCPeerConnection_SignalingState>] **_get_signaling_state**\ (\ ) |virtual| |required| |const| [🔗<class_WebRTCPeerConnectionExtension_private_method__get_signaling_state>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Error<enum_@GlobalScope_Error>] **_initialize**\ (\ p_config\: [Dictionary<class_Dictionary>]\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__initialize>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Error<enum_@GlobalScope_Error>] **_poll**\ (\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__poll>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Error<enum_@GlobalScope_Error>] **_set_local_description**\ (\ p_type\: [String<class_String>], p_sdp\: [String<class_String>]\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__set_local_description>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!


----



[Error<enum_@GlobalScope_Error>] **_set_remote_description**\ (\ p_type\: [String<class_String>], p_sdp\: [String<class_String>]\ ) |virtual| |required| [🔗<class_WebRTCPeerConnectionExtension_private_method__set_remote_description>]

> **CONTAINER**
>
	There is currently no description for this method. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

