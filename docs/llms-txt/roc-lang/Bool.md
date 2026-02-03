# Source: https://www.roc-lang.org/builtins/Bool#is_eq

# Bool - Documentation

Str. Utf8Problem : [ InvalidStartByte, UnexpectedEndOfSequence, ExpectedContinuation, OverlongEncoding, CodepointTooLarge, EncodesSurrogateHalf ]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Str. is_empty : Str -> Bool
---------------------------

Str. concat : Str, Str -> Str
-----------------------------

Str. with_capacity : U64 -> Str
---------------------------------

Str. reserve : Str, U64 -> Str
------------------------------

Str. join_with : List Str, Str -> Str
--------------------------------------

Str. split_on : Str, Str -> List Str
-------------------------------------

Str. repeat : Str, U64 -> Str
------------------------------

Str. len : Str -> [LearnAboutStringsInRoc Str]
-----------------------------------------------

Str. to_utf8 : Str -> List U8
------------------------------

Str. from_utf8 : List U8 -> Result Str [ BadUtf8 { problem : Utf8Problem, index : U64 } ]
------------------------------------------------------------------------------------------------

Str. from_utf8_lossy : List U8 -> Str
--------------------------------------

Str. from_utf16 : List U16 -> Result Str [ BadUtf16 { problem : Utf8Problem, index : U64 } ]
--------------------------------------------------------------------------------------------------

Str. from_utf16_lossy : List U16 -> Str
--------------------------------------

Str. from_utf32 : List U32 -> Result Str [ BadUtf32 { problem : Utf8Problem, index : U64 } ]
--------------------------------------------------------------------------------------------------

Str. from_utf32_lossy : List U32 -> Str
--------------------------------------

Str. starts_with : Str, Str -> Bool
-------------------------------------

Str. ends_with : Str, Str -> Bool
-----------------------------------

Str. trim : Str -> Str
-----------------------

Str. trim_start : Str -> Str
----------------------------

Str. trim_end : Str -> Str
----------------------------

Str. to_dec : Str -> Result Dec [InvalidNumStr]
------------------------------------------------

Str. to_f64 : Str -> Result F64 [InvalidNumStr]
------------------------------------------------

Str. to_f32 : Str -> Result F32 [InvalidNumStr]
------------------------------------------------

Str. to_u128 : Str -> Result U128 [InvalidNumStr]
--------------------------------------------------

Str. to_i128 : Str -> Result I128 [InvalidNumStr]
--------------------------------------------------

Str. to_u64 : Str -> Result U64 [InvalidNumStr]
--------------------------------------------------

Str. to_i64 : Str -> Result I64 [InvalidNumStr]
--------------------------------------------------

Str. to_u32 : Str -> Result U32 [InvalidNumStr]
--------------------------------------------------

Str. to_i32 : Str -> Result I32 [InvalidNumStr]
--------------------------------------------------

Str. to_u16 : Str -> Result U16 [InvalidNumStr]
--------------------------------------------------

Str. to_i16 : Str -> Result I16 [InvalidNumStr]
--------------------------------------------------

Str. to_u8 : Str -> Result U8 [InvalidNumStr]
------------------------------------------------

Str. to_dec : Str -> Result Dec [InvalidNumStr]
------------------------------------------------

Str. to_f64 : Str -> Result F64 [InvalidNumStr]
------------------------------------------------

Str. to_f32 : Str -> Result F32 [InvalidNumStr]
------------------------------------------------

Str. to_u128 : Str -> Result U128 [InvalidNumStr]
--------------------------------------------------

Str. to_i128 : Str -> Result I128 [InvalidNumStr]
--------------------------------------------------

Str. to_u64 : Str -> Result U64 [InvalidNumStr]
--------------------------------------------------

Str. to_i64 : Str -> Result I64 [InvalidNumStr]
--------------------------------------------------

Str. to_u32 : Str -> Result U32 [InvalidNumStr]
--------------------------------------------------

Str. to_i32 : Str -> Result I32 [InvalidNumStr]
--------------------------------------------------

Str. to_u16 : Str -> Result U16 [InvalidNumStr]
--------------------------------------------------

Str. to_i16 : Str -> Result I16 [InvalidNumStr]
--------------------------------------------------

Str. to_u8 : Str -> Result U8 [InvalidNumStr]
------------------------------------------------

Str. to_dec : Str -> Result Dec [InvalidNumStr]
------------------------------------------------

Str. to_f64 : Str -> Result F64 [InvalidNumStr]
------------------------------------------------

Str. to_f32 : Str -> Result F32 [InvalidNumStr]
------------------------------------------------

Str. to_u128 : Str -> Result U128 [InvalidNumStr]
--------------------------------------------------

Str. to_i128 : Str -> Result I128 [InvalidNumStr]
--------------------------------------------------

Str. to_u64 : Str -> Result U64 [InvalidNumStr]
--------------------------------------------------

Str. to_i64 : Str -> Result I64 [InvalidNumStr]
--------------------------------------------------

Str. to_u32 : Str -> Result U32 [InvalidNumStr]
--------------------------------------------------

Str. to_i32 : Str -> Result I3