:github_url: hide



# AudioEffectInstance

**Inherits:** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

**Inherited By:** [AudioEffectSpectrumAnalyzerInstance<class_AudioEffectSpectrumAnalyzerInstance>]

Manipulates the audio it receives for a given effect.


## Description

An audio effect instance manipulates the audio it receives for a given effect. This instance is automatically created by an [AudioEffect<class_AudioEffect>] when it is added to a bus, and should usually not be created directly. If necessary, it can be fetched at run-time with [AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>].


## Tutorials

- [../tutorials/audio/audio_buses](Audio buses .md)


## Methods

> **TABLE**
> :widths: auto
>
> +-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | |void|                  | :ref:`_process<class_AudioEffectInstance_private_method__process>`\ (\ src_buffer\: ``const void*``, dst_buffer\: ``AudioFrame*``, frame_count\: :ref:`int<class_int>`\ ) |virtual| |required| |
> +-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`bool<class_bool>` | :ref:`_process_silence<class_AudioEffectInstance_private_method__process_silence>`\ (\ ) |virtual| |const|                                                                                     |
> +-------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Method Descriptions



|void| **_process**\ (\ src_buffer\: `const void*`, dst_buffer\: `AudioFrame*`, frame_count\: [int<class_int>]\ ) |virtual| |required| [🔗<class_AudioEffectInstance_private_method__process>]

Called by the [AudioServer<class_AudioServer>] to process this effect. When [_process_silence()<class_AudioEffectInstance_private_method__process_silence>] is not overridden or it returns `false`, this method is called only when the bus is active.

\ **Note:** It is not useful to override this method in GDScript or C#. Only GDExtension can take advantage of it.


----



[bool<class_bool>] **_process_silence**\ (\ ) |virtual| |const| [🔗<class_AudioEffectInstance_private_method__process_silence>]

Override this method to customize the processing behavior of this effect instance.

Should return `true` to force the [AudioServer<class_AudioServer>] to always call [_process()<class_AudioEffectInstance_private_method__process>], even if the bus has been muted or cannot otherwise be heard.

