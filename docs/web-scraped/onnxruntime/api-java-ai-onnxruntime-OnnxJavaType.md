# Source: https://onnxruntime.ai/docs/api/java/ai/onnxruntime/OnnxJavaType.html

[Package] [ai.onnxruntime](package-summary.html)

## Enum OnnxJavaType 

- java.lang.Object
- - java.lang.Enum\<[OnnxJavaType](OnnxJavaType.html "enum in ai.onnxruntime")\>
  - - ai.onnxruntime.OnnxJavaType

- 

  All Implemented Interfaces:
  :   `java.io.Serializable`, `java.lang.Comparable<`[`OnnxJavaType`](OnnxJavaType.html "enum in ai.onnxruntime")`>`

  ------------------------------------------------------------------------

      public enum OnnxJavaType
      extends java.lang.Enum<OnnxJavaType>

  ::: block
  An enum representing ONNX Runtime supported Java primitive types (and String).
  :::

- ::: section
  - []

    ### Enum Constant Summary

    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | Enum Constant                              | Description                                                                       |
    +============================================+===================================================================================+
    | [[`BFLOAT16`](#BFLOAT16)] | ::: block                                                                         |
    |                                            | A non-IEEE 16-bit floating point value, with 8 exponent bits and 7 mantissa bits. |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`BOOL`](#BOOL)]         | ::: block                                                                         |
    |                                            | A boolean value stored in a single byte.                                          |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`DOUBLE`](#DOUBLE)]     | ::: block                                                                         |
    |                                            | A 64-bit floating point value.                                                    |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`FLOAT`](#FLOAT)]       | ::: block                                                                         |
    |                                            | A 32-bit floating point value.                                                    |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`FLOAT16`](#FLOAT16)]   | ::: block                                                                         |
    |                                            | A IEEE 16-bit floating point value.                                               |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`INT16`](#INT16)]       | ::: block                                                                         |
    |                                            | A 16-bit signed integer value.                                                    |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`INT32`](#INT32)]       | ::: block                                                                         |
    |                                            | A 32-bit signed integer value.                                                    |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`INT64`](#INT64)]       | ::: block                                                                         |
    |                                            | A 64-bit signed integer value.                                                    |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`INT8`](#INT8)]         | ::: block                                                                         |
    |                                            | An 8-bit signed integer value.                                                    |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`STRING`](#STRING)]     | ::: block                                                                         |
    |                                            | A UTF-8 string.                                                                   |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`UINT8`](#UINT8)]       | ::: block                                                                         |
    |                                            | A 8-bit unsigned integer value.                                                   |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+
    | [[`UNKNOWN`](#UNKNOWN)]   | ::: block                                                                         |
    |                                            | An unknown type used as an error condition or a sentinel.                         |
    |                                            | :::                                                                               |
    +--------------------------------------------+-----------------------------------------------------------------------------------+

    : Enum Constants[ ]
  :::

  ::: section
  - []

    ### Field Summary

    +-----------------------+--------------------------------------+----------------------------------------------------------+
    | Modifier and Type     | Field                                | Description                                              |
    +=======================+======================================+==========================================================+
    | `java.lang.Class<?>`  | [[`clazz`](#clazz)] | ::: block                                                |
    |                       |                                      | The Java side type used as the carrier.                  |
    |                       |                                      | :::                                                      |
    +-----------------------+--------------------------------------+----------------------------------------------------------+
    | `int`                 | [[`size`](#size)]   | ::: block                                                |
    |                       |                                      | The number of bytes used by a single value of this type. |
    |                       |                                      | :::                                                      |
    +-----------------------+--------------------------------------+----------------------------------------------------------+
    | `int`                 | [[`value`](#value)] | ::: block                                                |
    |                       |                                      | The native value of the enum.                            |
    |                       |                                      | :::                                                      |
    +-----------------------+--------------------------------------+----------------------------------------------------------+

    : Fields[ ]
  :::

  ::: section
  - []

    ### Method Summary

    +---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | Modifier and Type                                                         | Method                                                                                                                                                                                                               | Description                                                                                                                                                                        |
    +===========================================================================+======================================================================================================================================================================================================================+====================================================================================================================================================================================+
    | `static `[`OnnxJavaType`](OnnxJavaType.html "enum in ai.onnxruntime")     | [[`mapFromClass`](#mapFromClass(java.lang.Class))]`​(java.lang.Class<?> clazz)`                                                                                                                      | ::: block                                                                                                                                                                          |
    |                                                                           |                                                                                                                                                                                                                      | Maps from a Java class object into the enum type, returning [`UNKNOWN`](#UNKNOWN) for unsupported types.                                                                           |
    |                                                                           |                                                                                                                                                                                                                      | :::                                                                                                                                                                                |
    +---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `static `[`OnnxJavaType`](OnnxJavaType.html "enum in ai.onnxruntime")     | [[`mapFromInt`](#mapFromInt(int))]`​(int value)`                                                                                                                                                     | ::: block                                                                                                                                                                          |
    |                                                                           |                                                                                                                                                                                                                      | Maps from an int in native land into an OnnxJavaType instance.                                                                                                                     |
    |                                                                           |                                                                                                                                                                                                                      | :::                                                                                                                                                                                |
    +---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `static `[`OnnxJavaType`](OnnxJavaType.html "enum in ai.onnxruntime")     | [[`mapFromOnnxTensorType`](#mapFromOnnxTensorType(ai.onnxruntime.TensorInfo.OnnxTensorType))]`​(`[`TensorInfo.OnnxTensorType`](TensorInfo.OnnxTensorType.html "enum in ai.onnxruntime")` onnxValue)` | ::: block                                                                                                                                                                          |
    |                                                                           |                                                                                                                                                                                                                      | Maps from the [`TensorInfo.OnnxTensorType`](TensorInfo.OnnxTensorType.html "enum in ai.onnxruntime") enum to the corresponding OnnxJavaType enum, converting types as appropriate. |
    |                                                                           |                                                                                                                                                                                                                      | :::                                                                                                                                                                                |
    +---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `static `[`OnnxJavaType`](OnnxJavaType.html "enum in ai.onnxruntime")     | [[`valueOf`](#valueOf(java.lang.String))]`​(java.lang.String name)`                                                                                                                                  | ::: block                                                                                                                                                                          |
    |                                                                           |                                                                                                                                                                                                                      | Returns the enum constant of this type with the specified name.                                                                                                                    |
    |                                                                           |                                                                                                                                                                                                                      | :::                                                                                                                                                                                |
    +---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    | `static `[`OnnxJavaType`](OnnxJavaType.html "enum in ai.onnxruntime")`[]` | [[`values`](#values())]`()`                                                                                                                                                                         | ::: block                                                                                                                                                                          |
    |                                                                           |                                                                                                                                                                                                                      | Returns an array containing the constants of this enum type, in the order they are declared.                                                                                       |
    |                                                                           |                                                                                                                                                                                                                      | :::                                                                                                                                                                                |
    +---------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

    : [All Methods[ ]][[Static Methods](javascript:show(1);)[ ]][[Concrete Methods](javascript:show(8);)[ ]]

    - []

      ### Methods inherited from class java.lang.Enum

      `clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

    <!-- -->

    - []

      ### Methods inherited from class java.lang.Object

      `getClass, notify, notifyAll, wait, wait, wait`
  :::

- ::: section
  - []

    ### Enum Constant Detail

    []

    - #### FLOAT

          public static final OnnxJavaType FLOAT

      ::: block
      A 32-bit floating point value.
      :::

    []

    - #### DOUBLE

          public static final OnnxJavaType DOUBLE

      ::: block
      A 64-bit floating point value.
      :::

    []

    - #### INT8

          public static final OnnxJavaType INT8

      ::: block
      An 8-bit signed integer value.
      :::

    []

    - #### INT16

          public static final OnnxJavaType INT16

      ::: block
      A 16-bit signed integer value.
      :::

    []

    - #### INT32

          public static final OnnxJavaType INT32

      ::: block
      A 32-bit signed integer value.
      :::

    []

    - #### INT64

          public static final OnnxJavaType INT64

      ::: block
      A 64-bit signed integer value.
      :::

    []

    - #### BOOL

          public static final OnnxJavaType BOOL

      ::: block
      A boolean value stored in a single byte.
      :::

    []

    - #### STRING

          public static final OnnxJavaType STRING

      ::: block
      A UTF-8 string.
      :::

    []

    - #### UINT8

          public static final OnnxJavaType UINT8

      ::: block
      A 8-bit unsigned integer value.
      :::

    []

    - #### FLOAT16

          public static final OnnxJavaType FLOAT16

      ::: block
      A IEEE 16-bit floating point value.
      :::

    []

    - #### BFLOAT16

          public static final OnnxJavaType BFLOAT16

      ::: block
      A non-IEEE 16-bit floating point value, with 8 exponent bits and 7 mantissa bits.
      :::

    []

    - #### UNKNOWN

          public static final OnnxJavaType UNKNOWN

      ::: block
      An unknown type used as an error condition or a sentinel.
      :::
  :::

  ::: section
  - []

    ### Field Detail

    []

    - #### value

          public final int value

      ::: block
      The native value of the enum.
      :::

    []

    - #### clazz

          public final java.lang.Class<?> clazz

      ::: block
      The Java side type used as the carrier.
      :::

    []

    - #### size

          public final int size

      ::: block
      The number of bytes used by a single value of this type.
      :::
  :::

  ::: section
  - []

    ### Method Detail

    []

    - #### values

      ``` methodSignature
      public static OnnxJavaType[] values()
      ```

      ::: block
      Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:

          for (OnnxJavaType c : OnnxJavaType.values())
              System.out.println(c);
      :::

      [Returns:]
      :   an array containing the constants of this enum type, in the order they are declared

    []

    - #### valueOf

      ``` methodSignature
      public static OnnxJavaType valueOf​(java.lang.String name)
      ```

      ::: block
      Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
      :::

      [Parameters:]
      :   `name` - the name of the enum constant to be returned.

      [Returns:]
      :   the enum constant with the specified name

      [Throws:]
      :   `java.lang.IllegalArgumentException` - if this enum type has no constant with the specified name
      :   `java.lang.NullPointerException` - if the argument is null

    []

    - #### mapFromInt

      ``` methodSignature
      public static OnnxJavaType mapFromInt​(int value)
      ```

      ::: block
      Maps from an int in native land into an OnnxJavaType instance.
      :::

      [Parameters:]
      :   `value` - The value to lookup.

      [Returns:]
      :   The enum instance.

    []

    - #### mapFromOnnxTensorType

      ``` methodSignature
      public static OnnxJavaType mapFromOnnxTensorType​(TensorInfo.OnnxTensorType onnxValue)
      ```

      ::: block
      Maps from the [`TensorInfo.OnnxTensorType`](TensorInfo.OnnxTensorType.html "enum in ai.onnxruntime") enum to the corresponding OnnxJavaType enum, converting types as appropriate.
      Must match the values from OrtJniUtil.c.
      :::

      [Parameters:]
      :   `onnxValue` - The native value type.

      [Returns:]
      :   A OnnxJavaType instance representing the Java type

    []

    - #### mapFromClass

      ``` methodSignature
      public static OnnxJavaType mapFromClass​(java.lang.Class<?> clazz)
      ```

      ::: block
      Maps from a Java class object into the enum type, returning [`UNKNOWN`](#UNKNOWN) for unsupported types.
      :::

      [Parameters:]
      :   `clazz` - The class to use.

      [Returns:]
      :   An OnnxJavaType instance.
  :::