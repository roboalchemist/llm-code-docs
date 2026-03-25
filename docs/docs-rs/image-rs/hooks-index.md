image
# Module hooks 
Source 
## Structs§
GenericReaderA wrapper around a type-erased trait object that implements `Read` and `Seek`.
## Functions§
decoding_hook_registeredReturns whether a decoding hook has been registered for the given format.register_decoding_hookRegister a new decoding hook or returns false if one already exists for the given format.register_format_detection_hookRegisters a format detection hook.
## Type Aliases§
DecodingHookA function to produce an `ImageDecoder` for a given image format.