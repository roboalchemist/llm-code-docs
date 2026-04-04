# Core functions and types

# Core functions and types

godot-cpp's API is designed to be as similar as possible to Godot's internal API.
This means that, in general, you can use theEngine detailssection to learn how to
work with godot-cpp. In addition, it can often be useful to browse theengine's codefor examples for how to work with Godot's API.
That being said, there are some differences to be aware of, which are documented here.

## Common functions and macros

Please refer toCommon engine methods and macrosfor information on this. The functions and macros documented
there are also available in godot-cpp.

## Core types

Godot'sCore typesare also available in godot-cpp, and the same recommendations apply
as described in that article. The types are regularly synchronized with the Godot codebase.
In your own code, you can also useC++ STL types, or types from
any library you choose, but they won't be compatible with Godot's APIs.

### Packed arrays

While in Godot, thePacked*Arraytypes are aliases ofVector, in godot-cpp, they're their own types, using the
Godot bindings. This is becausePacked*Arrayare exposed to Godot and limited to only Godot types, whereasVectorcan hold any C++ type which Godot might not be able to understand.
In general, thePacked*Arraytypes work the same way as theirVectoraliases, however, there are some notable
differences.

#### Data access

Vectorkeeps its data entirely within the GDExtension, whereas thePacked*Arraytypes keep their data on the
Godot side. This means that any time aPacked*Arrayis accessed, it needs to call into Godot.
To efficiently read or write a large amount of data into aPacked*Array, you should call.ptr()(for reading)
or.ptrw()(for writing) to get a pointer directly to the array's memory:

```
// BAD!
void my_bad_function(const PackedByteArray &p_array) {
    for (int i = 0; i < p_array.size(); i++) {
        // Each time this runs it needs to call into Godot.
        uint8_t byte = p_array[i];

        // .. do something with the byte.
    }
}

// GOOD :-)
void my_good_function(const PackedByteArray &p_array) {
    const uint8_t *array_ptr = p_array.ptr();
    for (int i = 0; i < p_array.size(); i++) {
        // This directly accesses the memory!
        uint8_t byte = array_ptr[i];

        // .. do something with the byte.
    }
}
```

#### Copying

Variantwrappers forPacked*Arraytreat them as pass-by-reference, while thePacked*Arraytypes themselves are pass-by-value (implemented as copy-on-write).
In addition, it may be of interest that GDScript calls use theVariantcall interface: AnyPacked*Arrayarguments to your functions will be passed in aVariant, and unpacked from there. This can create copies of the
types, so the argument you receive may be a copy of the argument that the function was called with. In practice, this
means you cannot rely on that the argument passed to you can be modified at the caller's site.

## Variant class

Please refer toVariant classto learn about how to work withVariant.
Most importantly, you should be aware that all functions exposed through the GDExtension API must be compatible withVariant.

## Object class

Please refer toObject classto learn how to register and work with your ownObjecttypes.
We are not aware of any major differences between the godot-cppObjectAPI and Godot's internalObjectAPI,
except that some methods are available in Godot's internal API that are not available in godot-cpp.
You should be aware that the pointer to your godot-cppObjectis different from the pointer that Godot uses
internally. This is because the godot-cpp version is an extension instance, allocated separately from the originalObject. However, in practice, this difference is usually not noticeable.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
