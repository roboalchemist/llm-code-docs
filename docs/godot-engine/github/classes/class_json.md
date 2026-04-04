:github_url: hide



# JSON

**Inherits:** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Helper class for creating and parsing JSON data.


## Description

The **JSON** class enables all data types to be converted to and from a JSON string. This is useful for serializing data, e.g. to save to a file or send over the network.

\ [stringify()<class_JSON_method_stringify>] is used to convert any data type into a JSON string.

\ [parse()<class_JSON_method_parse>] is used to convert any existing JSON data into a [Variant<class_Variant>] that can be used within Godot. If successfully parsed, use [data<class_JSON_property_data>] to retrieve the [Variant<class_Variant>], and use [@GlobalScope.typeof()<class_@GlobalScope_method_typeof>] to check if the Variant's type is what you expect. JSON Objects are converted into a [Dictionary<class_Dictionary>], but JSON data can be used to store [Array<class_Array>]\ s, numbers, [String<class_String>]\ s and even just a boolean.

::

    var data_to_send = ["a", "b", "c"]
    var json_string = JSON.stringify(data_to_send)
    # Save data
    # ...
    # Retrieve data
    var json = JSON.new()
    var error = json.parse(json_string)
    if error == OK:
        var data_received = json.data
        if typeof(data_received) == TYPE_ARRAY:
            print(data_received) # Prints the array.
        else:
            print("Unexpected data")
    else:
        print("JSON Parse Error: ", json.get_error_message(), " in ", json_string, " at line ", json.get_error_line())

Alternatively, you can parse strings using the static [parse_string()<class_JSON_method_parse_string>] method, but it doesn't handle errors.

::

    var data = JSON.parse_string(json_string) # Returns null if parsing failed.

\ **Note:** Both parse methods do not fully comply with the JSON specification:

- Trailing commas in arrays or objects are ignored, instead of causing a parser error.

- New line and tab characters are accepted in string literals, and are treated like their corresponding escape sequences `\n` and `\t`.

- Numbers are parsed using [String.to_float()<class_String_method_to_float>] which is generally more lax than the JSON specification.

- Certain errors, such as invalid Unicode sequences, do not cause a parser error. Instead, the string is cleaned up and an error is logged to the console.


## Properties

> **TABLE**
> :widths: auto
>
> +-------------------------------+---------------------------------------+----------+
> | :ref:`Variant<class_Variant>` | :ref:`data<class_JSON_property_data>` | ``null`` |
> +-------------------------------+---------------------------------------+----------+
>

## Methods

> **TABLE**
> :widths: auto
>
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`         | :ref:`from_native<class_JSON_method_from_native>`\ (\ variant\: :ref:`Variant<class_Variant>`, full_objects\: :ref:`bool<class_bool>` = false\ ) |static|                                                                                   |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`int<class_int>`                 | :ref:`get_error_line<class_JSON_method_get_error_line>`\ (\ ) |const|                                                                                                                                                                       |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_error_message<class_JSON_method_get_error_message>`\ (\ ) |const|                                                                                                                                                                 |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`get_parsed_text<class_JSON_method_get_parsed_text>`\ (\ ) |const|                                                                                                                                                                     |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Error<enum_@GlobalScope_Error>` | :ref:`parse<class_JSON_method_parse>`\ (\ json_text\: :ref:`String<class_String>`, keep_text\: :ref:`bool<class_bool>` = false\ )                                                                                                           |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`         | :ref:`parse_string<class_JSON_method_parse_string>`\ (\ json_string\: :ref:`String<class_String>`\ ) |static|                                                                                                                               |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`String<class_String>`           | :ref:`stringify<class_JSON_method_stringify>`\ (\ data\: :ref:`Variant<class_Variant>`, indent\: :ref:`String<class_String>` = "", sort_keys\: :ref:`bool<class_bool>` = true, full_precision\: :ref:`bool<class_bool>` = false\ ) |static| |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
> | :ref:`Variant<class_Variant>`         | :ref:`to_native<class_JSON_method_to_native>`\ (\ json\: :ref:`Variant<class_Variant>`, allow_objects\: :ref:`bool<class_bool>` = false\ ) |static|                                                                                         |
> +---------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
>

----


## Property Descriptions



[Variant<class_Variant>] **data** = `null` [🔗<class_JSON_property_data>]


- |void| **set_data**\ (\ value\: [Variant<class_Variant>]\ )
- [Variant<class_Variant>] **get_data**\ (\ )

Contains the parsed JSON data in [Variant<class_Variant>] form.


----


## Method Descriptions



[Variant<class_Variant>] **from_native**\ (\ variant\: [Variant<class_Variant>], full_objects\: [bool<class_bool>] = false\ ) |static| [🔗<class_JSON_method_from_native>]

Converts a native engine type to a JSON-compliant value.

By default, objects are ignored for security reasons, unless `full_objects` is `true`.

You can convert a native value to a JSON string like this:

::

    func encode_data(value, full_objects = false):
        return JSON.stringify(JSON.from_native(value, full_objects))


----



[int<class_int>] **get_error_line**\ (\ ) |const| [🔗<class_JSON_method_get_error_line>]

Returns `0` if the last call to [parse()<class_JSON_method_parse>] was successful, or the line number where the parse failed.


----



[String<class_String>] **get_error_message**\ (\ ) |const| [🔗<class_JSON_method_get_error_message>]

Returns an empty string if the last call to [parse()<class_JSON_method_parse>] was successful, or the error message if it failed.


----



[String<class_String>] **get_parsed_text**\ (\ ) |const| [🔗<class_JSON_method_get_parsed_text>]

Return the text parsed by [parse()<class_JSON_method_parse>] (requires passing `keep_text` to [parse()<class_JSON_method_parse>]).


----



[Error<enum_@GlobalScope_Error>] **parse**\ (\ json_text\: [String<class_String>], keep_text\: [bool<class_bool>] = false\ ) [🔗<class_JSON_method_parse>]

Attempts to parse the `json_text` provided.

Returns an [Error<enum_@GlobalScope_Error>]. If the parse was successful, it returns [@GlobalScope.OK<class_@GlobalScope_constant_OK>] and the result can be retrieved using [data<class_JSON_property_data>]. If unsuccessful, use [get_error_line()<class_JSON_method_get_error_line>] and [get_error_message()<class_JSON_method_get_error_message>] to identify the source of the failure.

Non-static variant of [parse_string()<class_JSON_method_parse_string>], if you want custom error handling.

The optional `keep_text` argument instructs the parser to keep a copy of the original text. This text can be obtained later by using the [get_parsed_text()<class_JSON_method_get_parsed_text>] function and is used when saving the resource (instead of generating new text from [data<class_JSON_property_data>]).


----



[Variant<class_Variant>] **parse_string**\ (\ json_string\: [String<class_String>]\ ) |static| [🔗<class_JSON_method_parse_string>]

Attempts to parse the `json_string` provided and returns the parsed data. Returns `null` if parse failed.


----



[String<class_String>] **stringify**\ (\ data\: [Variant<class_Variant>], indent\: [String<class_String>] = "", sort_keys\: [bool<class_bool>] = true, full_precision\: [bool<class_bool>] = false\ ) |static| [🔗<class_JSON_method_stringify>]

Converts a [Variant<class_Variant>] var to JSON text and returns the result. Useful for serializing data to store or send over the network.

\ **Note:** The JSON specification does not define integer or float types, but only a *number* type. Therefore, converting a Variant to JSON text will convert all numerical values to [float<class_float>] types.

\ **Note:** If `full_precision` is `true`, when stringifying floats, the unreliable digits are stringified in addition to the reliable digits to guarantee exact decoding.

The `indent` parameter controls if and how something is indented; its contents will be used where there should be an indent in the output. Even spaces like `"   "` will work. `\t` and `\n` can also be used for a tab indent, or to make a newline for each indent respectively.

\ **Warning:** Non-finite numbers are not supported in JSON. Any occurrences of [@GDScript.INF<class_@GDScript_constant_INF>] will be replaced with `1e99999`, and negative [@GDScript.INF<class_@GDScript_constant_INF>] will be replaced with `-1e99999`, but they will be interpreted correctly as infinity by most JSON parsers. [@GDScript.NAN<class_@GDScript_constant_NAN>] will be replaced with `null`, and it will not be interpreted as NaN in JSON parsers. If you expect non-finite numbers, consider passing your data through [from_native()<class_JSON_method_from_native>] first.

\ **Example output:**\ 

::

    ## JSON.stringify(my_dictionary)
    {"name":"my_dictionary","version":"1.0.0","entities":[{"name":"entity_0","value":"value_0"},{"name":"entity_1","value":"value_1"}]}

    ## JSON.stringify(my_dictionary, "\t")
    {
        "name": "my_dictionary",
        "version": "1.0.0",
        "entities": [
            {
                "name": "entity_0",
                "value": "value_0"
            },
            {
                "name": "entity_1",
                "value": "value_1"
## }
    }

    ## JSON.stringify(my_dictionary, "...")
    {
    ..."name": "my_dictionary",
    ..."version": "1.0.0",
    ..."entities": [
    ......{
    ........."name": "entity_0",
    ........."value": "value_0"
    ......},
    ......{
    ........."name": "entity_1",
    ........."value": "value_1"
    ......}
    ...]
    }


----



[Variant<class_Variant>] **to_native**\ (\ json\: [Variant<class_Variant>], allow_objects\: [bool<class_bool>] = false\ ) |static| [🔗<class_JSON_method_to_native>]

Converts a JSON-compliant value that was created with [from_native()<class_JSON_method_from_native>] back to native engine types.

By default, objects are ignored for security reasons, unless `allow_objects` is `true`.

You can convert a JSON string back to a native value like this:

::

    func decode_data(string, allow_objects = false):
        return JSON.to_native(JSON.parse_string(string), allow_objects)

