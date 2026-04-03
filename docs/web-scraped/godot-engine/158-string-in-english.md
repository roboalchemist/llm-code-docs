# String in English

# String
A built-in type for strings.

## Description
This is the built-in string Variant type (and the one used by GDScript). Strings may contain any number of Unicode characters, and expose methods useful for manipulating and generating strings. Strings are reference-counted and use a copy-on-write approach (every modification to a string returns a newString), so passing them around is cheap in resources.
Some string methods have corresponding variations. Variations suffixed withn(countn(),findn(),replacen(), etc.) arecase-insensitive(they make no distinction between uppercase and lowercase letters). Method variations prefixed withr(rfind(),rsplit(), etc.) are reversed, and start from the end of the string, instead of the beginning.
To convert anyVariantto or from a string, see@GlobalScope.str(),@GlobalScope.str_to_var(), and@GlobalScope.var_to_str().
Note:In a boolean context, a string will evaluate tofalseif it is empty (""). Otherwise, a string will always evaluate totrue.
Note
There are notable differences when using this API with C#. SeeC# API differences to GDScriptfor more information.

## Tutorials
- GDScript format strings
GDScript format strings

## Constructors

| String | String() |
|---|---|
| String | String(from:String) |
| String | String(from:NodePath) |
| String | String(from:StringName) |

String
String()
String
String(from:String)
String
String(from:NodePath)
String
String(from:StringName)

## Methods

| bool | begins_with(text:String)const |
|---|---|
| PackedStringArray | bigrams()const |
| int | bin_to_int()const |
| String | c_escape()const |
| String | c_unescape()const |
| String | capitalize()const |
| int | casecmp_to(to:String)const |
| String | chr(code:int)static |
| bool | contains(what:String)const |
| bool | containsn(what:String)const |
| int | count(what:String, from:int= 0, to:int= 0)const |
| int | countn(what:String, from:int= 0, to:int= 0)const |
| String | dedent()const |
| bool | ends_with(text:String)const |
| String | erase(position:int, chars:int= 1)const |
| int | filecasecmp_to(to:String)const |
| int | filenocasecmp_to(to:String)const |
| int | find(what:String, from:int= 0)const |
| int | findn(what:String, from:int= 0)const |
| String | format(values:Variant, placeholder:String= "{_}")const |
| String | get_base_dir()const |
| String | get_basename()const |
| String | get_extension()const |
| String | get_file()const |
| String | get_slice(delimiter:String, slice:int)const |
| int | get_slice_count(delimiter:String)const |
| String | get_slicec(delimiter:int, slice:int)const |
| int | hash()const |
| PackedByteArray | hex_decode()const |
| int | hex_to_int()const |
| String | humanize_size(size:int)static |
| String | indent(prefix:String)const |
| String | insert(position:int, what:String)const |
| bool | is_absolute_path()const |
| bool | is_empty()const |
| bool | is_relative_path()const |
| bool | is_subsequence_of(text:String)const |
| bool | is_subsequence_ofn(text:String)const |
| bool | is_valid_ascii_identifier()const |
| bool | is_valid_filename()const |
| bool | is_valid_float()const |
| bool | is_valid_hex_number(with_prefix:bool= false)const |
| bool | is_valid_html_color()const |
| bool | is_valid_identifier()const |
| bool | is_valid_int()const |
| bool | is_valid_ip_address()const |
| bool | is_valid_unicode_identifier()const |
| String | join(parts:PackedStringArray)const |
| String | json_escape()const |
| String | left(length:int)const |
| int | length()const |
| String | lpad(min_length:int, character:String= " ")const |
| String | lstrip(chars:String)const |
| bool | match(expr:String)const |
| bool | matchn(expr:String)const |
| PackedByteArray | md5_buffer()const |
| String | md5_text()const |
| int | naturalcasecmp_to(to:String)const |
| int | naturalnocasecmp_to(to:String)const |
| int | nocasecmp_to(to:String)const |
| String | num(number:float, decimals:int= -1)static |
| String | num_int64(number:int, base:int= 10, capitalize_hex:bool= false)static |
| String | num_scientific(number:float)static |
| String | num_uint64(number:int, base:int= 10, capitalize_hex:bool= false)static |
| String | pad_decimals(digits:int)const |
| String | pad_zeros(digits:int)const |
| String | path_join(path:String)const |
| String | remove_char(what:int)const |
| String | remove_chars(chars:String)const |
| String | repeat(count:int)const |
| String | replace(what:String, forwhat:String)const |
| String | replace_char(key:int, with:int)const |
| String | replace_chars(keys:String, with:int)const |
| String | replacen(what:String, forwhat:String)const |
| String | reverse()const |
| int | rfind(what:String, from:int= -1)const |
| int | rfindn(what:String, from:int= -1)const |
| String | right(length:int)const |
| String | rpad(min_length:int, character:String= " ")const |
| PackedStringArray | rsplit(delimiter:String= "", allow_empty:bool= true, maxsplit:int= 0)const |
| String | rstrip(chars:String)const |
| PackedByteArray | sha1_buffer()const |
| String | sha1_text()const |
| PackedByteArray | sha256_buffer()const |
| String | sha256_text()const |
| float | similarity(text:String)const |
| String | simplify_path()const |
| PackedStringArray | split(delimiter:String= "", allow_empty:bool= true, maxsplit:int= 0)const |
| PackedFloat64Array | split_floats(delimiter:String, allow_empty:bool= true)const |
| String | strip_edges(left:bool= true, right:bool= true)const |
| String | strip_escapes()const |
| String | substr(from:int, len:int= -1)const |
| PackedByteArray | to_ascii_buffer()const |
| String | to_camel_case()const |
| float | to_float()const |
| int | to_int()const |
| String | to_kebab_case()const |
| String | to_lower()const |
| PackedByteArray | to_multibyte_char_buffer(encoding:String= "")const |
| String | to_pascal_case()const |
| String | to_snake_case()const |
| String | to_upper()const |
| PackedByteArray | to_utf8_buffer()const |
| PackedByteArray | to_utf16_buffer()const |
| PackedByteArray | to_utf32_buffer()const |
| PackedByteArray | to_wchar_buffer()const |
| String | trim_prefix(prefix:String)const |
| String | trim_suffix(suffix:String)const |
| int | unicode_at(at:int)const |
| String | uri_decode()const |
| String | uri_encode()const |
| String | uri_file_decode()const |
| String | validate_filename()const |
| String | validate_node_name()const |
| String | xml_escape(escape_quotes:bool= false)const |
| String | xml_unescape()const |

bool
begins_with(text:String)const
PackedStringArray
bigrams()const
bin_to_int()const
String
c_escape()const
String
c_unescape()const
String
capitalize()const
casecmp_to(to:String)const
String
chr(code:int)static
bool
contains(what:String)const
bool
containsn(what:String)const
count(what:String, from:int= 0, to:int= 0)const
countn(what:String, from:int= 0, to:int= 0)const
String
dedent()const
bool
ends_with(text:String)const
String
erase(position:int, chars:int= 1)const
filecasecmp_to(to:String)const
filenocasecmp_to(to:String)const
find(what:String, from:int= 0)const
findn(what:String, from:int= 0)const
String
format(values:Variant, placeholder:String= "{_}")const
String
get_base_dir()const
String
get_basename()const
String
get_extension()const
String
get_file()const
String
get_slice(delimiter:String, slice:int)const
get_slice_count(delimiter:String)const
String
get_slicec(delimiter:int, slice:int)const
hash()const
PackedByteArray
hex_decode()const
hex_to_int()const
String
humanize_size(size:int)static
String
indent(prefix:String)const
String
insert(position:int, what:String)const
bool
is_absolute_path()const
bool
is_empty()const
bool
is_relative_path()const
bool
is_subsequence_of(text:String)const
bool
is_subsequence_ofn(text:String)const
bool
is_valid_ascii_identifier()const
bool
is_valid_filename()const
bool
is_valid_float()const
bool
is_valid_hex_number(with_prefix:bool= false)const
bool
is_valid_html_color()const
bool
is_valid_identifier()const
bool
is_valid_int()const
bool
is_valid_ip_address()const
bool
is_valid_unicode_identifier()const
String
join(parts:PackedStringArray)const
String
json_escape()const
String
left(length:int)const
length()const
String
lpad(min_length:int, character:String= " ")const
String
lstrip(chars:String)const
bool
match(expr:String)const
bool
matchn(expr:String)const
PackedByteArray
md5_buffer()const
String
md5_text()const
naturalcasecmp_to(to:String)const
naturalnocasecmp_to(to:String)const
nocasecmp_to(to:String)const
String
num(number:float, decimals:int= -1)static
String
num_int64(number:int, base:int= 10, capitalize_hex:bool= false)static
String
num_scientific(number:float)static
String
num_uint64(number:int, base:int= 10, capitalize_hex:bool= false)static
String
pad_decimals(digits:int)const
String
pad_zeros(digits:int)const
String
path_join(path:String)const
String
remove_char(what:int)const
String
remove_chars(chars:String)const
String
repeat(count:int)const
String
replace(what:String, forwhat:String)const
String
replace_char(key:int, with:int)const
String
replace_chars(keys:String, with:int)const
String
replacen(what:String, forwhat:String)const
String
reverse()const
rfind(what:String, from:int= -1)const
rfindn(what:String, from:int= -1)const
String
right(length:int)const
String
rpad(min_length:int, character:String= " ")const
PackedStringArray
rsplit(delimiter:String= "", allow_empty:bool= true, maxsplit:int= 0)const
String
rstrip(chars:String)const
PackedByteArray
sha1_buffer()const
String
sha1_text()const
PackedByteArray
sha256_buffer()const
String
sha256_text()const
float
similarity(text:String)const
String
simplify_path()const
PackedStringArray
split(delimiter:String= "", allow_empty:bool= true, maxsplit:int= 0)const
PackedFloat64Array
split_floats(delimiter:String, allow_empty:bool= true)const
String
strip_edges(left:bool= true, right:bool= true)const
String
strip_escapes()const
String
substr(from:int, len:int= -1)const
PackedByteArray
to_ascii_buffer()const
String
to_camel_case()const
float
to_float()const
to_int()const
String
to_kebab_case()const
String
to_lower()const
PackedByteArray
to_multibyte_char_buffer(encoding:String= "")const
String
to_pascal_case()const
String
to_snake_case()const
String
to_upper()const
PackedByteArray
to_utf8_buffer()const
PackedByteArray
to_utf16_buffer()const
PackedByteArray
to_utf32_buffer()const
PackedByteArray
to_wchar_buffer()const
String
trim_prefix(prefix:String)const
String
trim_suffix(suffix:String)const
unicode_at(at:int)const
String
uri_decode()const
String
uri_encode()const
String
uri_file_decode()const
String
validate_filename()const
String
validate_node_name()const
String
xml_escape(escape_quotes:bool= false)const
String
xml_unescape()const

## Operators

| bool | operator !=(right:String) |
|---|---|
| bool | operator !=(right:StringName) |
| String | operator %(right:Variant) |
| String | operator +(right:String) |
| String | operator +(right:StringName) |
| bool | operator <(right:String) |
| bool | operator <=(right:String) |
| bool | operator ==(right:String) |
| bool | operator ==(right:StringName) |
| bool | operator >(right:String) |
| bool | operator >=(right:String) |
| String | operator [](index:int) |

bool
operator !=(right:String)
bool
operator !=(right:StringName)
String
operator %(right:Variant)
String
operator +(right:String)
String
operator +(right:StringName)
bool
operator <(right:String)
bool
operator <=(right:String)
bool
operator ==(right:String)
bool
operator ==(right:StringName)
bool
operator >(right:String)
bool
operator >=(right:String)
String
operator [](index:int)

## Constructor Descriptions
StringString()🔗
Constructs an emptyString("").
StringString(from:String)
Constructs aStringas a copy of the givenString.
StringString(from:NodePath)
Constructs a newStringfrom the givenNodePath.
StringString(from:StringName)
Constructs a newStringfrom the givenStringName.

## Method Descriptions
boolbegins_with(text:String)const🔗
Returnstrueif the string begins with the giventext. See alsoends_with().
PackedStringArraybigrams()const🔗
Returns an array containing the bigrams (pairs of consecutive characters) of this string.
```
print("Get up!".bigrams()) # Prints ["Ge", "et", "t ", " u", "up", "p!"]
```
intbin_to_int()const🔗
Converts the string representing a binary number into anint. The string may optionally be prefixed with"0b", and an additional-prefix for negative numbers.
```
print("101".bin_to_int())   # Prints 5
print("0b101".bin_to_int()) # Prints 5
print("-0b10".bin_to_int()) # Prints -2
```
```
GD.Print("101".BinToInt());   // Prints 5
GD.Print("0b101".BinToInt()); // Prints 5
GD.Print("-0b10".BinToInt()); // Prints -2
```
Stringc_escape()const🔗
Returns a copy of the string with special characters escaped using the C language standard.
Stringc_unescape()const🔗
Returns a copy of the string with escaped characters replaced by their meanings. Supported escape sequences are\',\",\\,\a,\b,\f,\n,\r,\t,\v.
Note:Unlike the GDScript parser, this method doesn't support the\uXXXXescape sequence.
Stringcapitalize()const🔗
Changes the appearance of the string: replaces underscores (_) with spaces, adds spaces before uppercase letters in the middle of a word, converts all letters to lowercase, then converts the first one and each one following a space to uppercase.
```
"move_local_x".capitalize()   # Returns "Move Local X"
"sceneFile_path".capitalize() # Returns "Scene File Path"
"2D, FPS, PNG".capitalize()   # Returns "2d, Fps, Png"
```
```
"move_local_x".Capitalize();   // Returns "Move Local X"
"sceneFile_path".Capitalize(); // Returns "Scene File Path"
"2D, FPS, PNG".Capitalize();   // Returns "2d, Fps, Png"
```
intcasecmp_to(to:String)const🔗
Performs a case-sensitive comparison to another string. Returns-1if less than,1if greater than, or0if equal. "Less than" and "greater than" are determined by theUnicode code pointsof each string, which roughly matches the alphabetical order.
If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor:1will be returned if this string is longer than thetostring, or-1if shorter. Note that the length of empty strings is always0.
To get aboolresult from a string comparison, use the==operator instead. See alsonocasecmp_to(),filecasecmp_to(), andnaturalcasecmp_to().
Stringchr(code:int)static🔗
Returns a single Unicode character from the integercode. You may useunicodelookup.comorunicode.orgas points of reference.
```
print(String.chr(65))     # Prints "A"
print(String.chr(129302)) # Prints "🤖" (robot face emoji)
```
See alsounicode_at(),@GDScript.char(), and@GDScript.ord().
boolcontains(what:String)const🔗
Returnstrueif the string containswhat. In GDScript, this corresponds to theinoperator.
```
print("Node".contains("de")) # Prints true
print("team".contains("I"))  # Prints false
print("I" in "team")         # Prints false
```
```
GD.Print("Node".Contains("de")); // Prints True
GD.Print("team".Contains("I"));  // Prints False
```
If you need to know wherewhatis within the string, usefind(). See alsocontainsn().
boolcontainsn(what:String)const🔗
Returnstrueif the string containswhat,ignoring case.
If you need to know wherewhatis within the string, usefindn(). See alsocontains().
intcount(what:String, from:int= 0, to:int= 0)const🔗
Returns the number of occurrences of the substringwhatbetweenfromandtopositions. Iftois 0, the search continues until the end of the string.
intcountn(what:String, from:int= 0, to:int= 0)const🔗
Returns the number of occurrences of the substringwhatbetweenfromandtopositions,ignoring case. Iftois 0, the search continues until the end of the string.
Stringdedent()const🔗
Returns a copy of the string with indentation (leading tabs and spaces) removed. See alsoindent()to add indentation.
boolends_with(text:String)const🔗
Returnstrueif the string ends with the giventext. See alsobegins_with().
Stringerase(position:int, chars:int= 1)const🔗
Returns a string withcharscharacters erased starting fromposition. Ifcharsgoes beyond the string's length given the specifiedposition, fewer characters will be erased from the returned string. Returns an empty string if eitherpositionorcharsis negative. Returns the original string unmodified ifcharsis0.
intfilecasecmp_to(to:String)const🔗
Likenaturalcasecmp_to()but prioritizes strings that begin with periods (.) and underscores (_) before any other character. Useful when sorting folders or file names.
To get aboolresult from a string comparison, use the==operator instead. See alsofilenocasecmp_to(),naturalcasecmp_to(), andcasecmp_to().
intfilenocasecmp_to(to:String)const🔗
Likenaturalnocasecmp_to()but prioritizes strings that begin with periods (.) and underscores (_) before any other character. Useful when sorting folders or file names.
To get aboolresult from a string comparison, use the==operator instead. See alsofilecasecmp_to(),naturalnocasecmp_to(), andnocasecmp_to().
intfind(what:String, from:int= 0)const🔗
Returns the index of thefirstoccurrence ofwhatin this string, or-1if there are none. The search's start can be specified withfrom, continuing to the end of the string.
```
print("Team".find("I")) # Prints -1

print("Potato".find("t"))    # Prints 2
print("Potato".find("t", 3)) # Prints 4
print("Potato".find("t", 5)) # Prints -1
```
```
GD.Print("Team".Find("I")); // Prints -1

GD.Print("Potato".Find("t"));    // Prints 2
GD.Print("Potato".Find("t", 3)); // Prints 4
GD.Print("Potato".Find("t", 5)); // Prints -1
```
Note:If you just want to know whether the string containswhat, usecontains(). In GDScript, you may also use theinoperator.
Note:A negative value offromis converted to a starting index by counting back from the last possible index with enough space to findwhat.
intfindn(what:String, from:int= 0)const🔗
Returns the index of thefirstcase-insensitiveoccurrence ofwhatin this string, or-1if there are none. The starting search index can be specified withfrom, continuing to the end of the string.
Stringformat(values:Variant, placeholder:String= "{_}")const🔗
Formats the string by replacing all occurrences ofplaceholderwith the elements ofvalues.
valuescan be aDictionary, anArray, or anObject. Any underscores inplaceholderwill be replaced with the corresponding keys in advance. Array elements use their index as keys.
```
# Prints "Waiting for Godot is a play by Samuel Beckett, and Godot Engine is named after it."
var use_array_values = "Waiting for {0} is a play by {1}, and {0} Engine is named after it."
print(use_array_values.format(["Godot", "Samuel Beckett"]))

# Prints "User 42 is Godot."
print("User {id} is {name}.".format({"id": 42, "name": "Godot"}))
```
Some additional handling is performed whenvaluesis anArray. Ifplaceholderdoes not contain an underscore, the elements of thevaluesarray will be used to replace one occurrence of the placeholder in order; If an element ofvaluesis another 2-element array, it'll be interpreted as a key-value pair.
```
# Prints "User 42 is Godot."
print("User {} is {}.".format([42, "Godot"], "{}"))
print("User {id} is {name}.".format([["id", 42], ["name", "Godot"]]))
```
When passing anObject, the property names fromObject.get_property_list()are used as keys.
```
# Prints "Visible true, position (0, 0)"
var node = Node2D.new()
print("Visible {visible}, position {position}".format(node))
```
See also theGDScript format stringtutorial.
Note:Each replacement is done sequentially for each element ofvalues,notall at once. This means that if any element is inserted and it contains another placeholder, it may be changed by the next replacement. While this can be very useful, it often causes unexpected results. If not necessary, make surevalues's elements do not contain placeholders.
```
print("{0} {1}".format(["{1}", "x"]))           # Prints "x x"
print("{0} {1}".format(["x", "{0}"]))           # Prints "x {0}"
print("{a} {b}".format({"a": "{b}", "b": "c"})) # Prints "c c"
print("{a} {b}".format({"b": "c", "a": "{b}"})) # Prints "{b} c"
```
Note:In C#, it's recommended tointerpolate strings with "$", instead.
Stringget_base_dir()const🔗
If the string is a valid file path, returns the base directory name.
```
var dir_path = "/path/to/file.txt".get_base_dir() # dir_path is "/path/to"
```
Stringget_basename()const🔗
If the string is a valid file path, returns the full file path, without the extension.
```
var base = "/path/to/file.txt".get_basename() # base is "/path/to/file"
```
Stringget_extension()const🔗
If the string is a valid file name or path, returns the file extension without the leading period (.). Otherwise, returns an empty string.
```
var a = "/path/to/file.txt".get_extension() # a is "txt"
var b = "cool.txt".get_extension()          # b is "txt"
var c = "cool.font.tres".get_extension()    # c is "tres"
var d = ".pack1".get_extension()            # d is "pack1"

var e = "file.txt.".get_extension()  # e is ""
var f = "file.txt..".get_extension() # f is ""
var g = "txt".get_extension()        # g is ""
var h = "".get_extension()           # h is ""
```
Stringget_file()const🔗
If the string is a valid file path, returns the file name, including the extension.
```
var file = "/path/to/icon.png".get_file() # file is "icon.png"
```
Stringget_slice(delimiter:String, slice:int)const🔗
Splits the string using adelimiterand returns the substring at indexslice. Returns the original string ifdelimiterdoes not occur in the string. Returns an empty string if theslicedoes not exist.
This is faster thansplit(), if you only need one or two substrings.
```
print("i/am/example/hi".get_slice("/", 2)) # Prints "example"
```
intget_slice_count(delimiter:String)const🔗
Returns the total number of slices when the string is split with the givendelimiter(seesplit()).
Useget_slice()to extract a specific slice.
```
print("i/am/example/string".get_slice_count("/")) # Prints '4'.
print("i am example string".get_slice_count("/")) # Prints '1'.
```
Stringget_slicec(delimiter:int, slice:int)const🔗
Splits the string using a Unicode character with codedelimiterand returns the substring at indexslice. Returns an empty string if theslicedoes not exist.
This is faster thansplit(), if you only need one or two substrings.
This is a Unicode version ofget_slice().
inthash()const🔗
Returns the 32-bit hash value representing the string's contents.
Note:Strings with equal hash values arenotguaranteed to be the same, as a result of hash collisions. On the contrary, strings with different hash values are guaranteed to be different.
PackedByteArrayhex_decode()const🔗
Decodes a hexadecimal string as aPackedByteArray.
```
var text = "hello world"
var encoded = text.to_utf8_buffer().hex_encode() # outputs "68656c6c6f20776f726c64"
print(encoded.hex_decode().get_string_from_utf8())
```
```
var text = "hello world";
var encoded = text.ToUtf8Buffer().HexEncode(); // outputs "68656c6c6f20776f726c64"
GD.Print(encoded.HexDecode().GetStringFromUtf8());
```
inthex_to_int()const🔗
Converts the string representing a hexadecimal number into anint. The string may be optionally prefixed with"0x", and an additional-prefix for negative numbers.
```
print("0xff".hex_to_int()) # Prints 255
print("ab".hex_to_int())   # Prints 171
```
```
GD.Print("0xff".HexToInt()); // Prints 255
GD.Print("ab".HexToInt());   // Prints 171
```
Stringhumanize_size(size:int)static🔗
Convertssizewhich represents a number of bytes into a human-readable form.
The result is inIEC prefix format, which may end in either"B","KiB","MiB","GiB","TiB","PiB", or"EiB".
Stringindent(prefix:String)const🔗
Indents every line of the string with the givenprefix. Empty lines are not indented. See alsodedent()to remove indentation.
For example, the string can be indented with two tabulations using"\t\t", or four spaces using"".
Stringinsert(position:int, what:String)const🔗
Insertswhatat the givenpositionin the string.
boolis_absolute_path()const🔗
Returnstrueif the string is a path to a file or directory, and its starting point is explicitly defined. This method is the opposite ofis_relative_path().
This includes all paths starting with"res://","user://","C:\","/", etc.
boolis_empty()const🔗
Returnstrueif the string's length is0(""). See alsolength().
boolis_relative_path()const🔗
Returnstrueif the string is a path, and its starting point is dependent on context. The path could begin from the current directory, or the currentNode(if the string is derived from aNodePath), and may sometimes be prefixed with"./". This method is the opposite ofis_absolute_path().
boolis_subsequence_of(text:String)const🔗
Returnstrueif all characters of this string can be found intextin their original order. This is not the same ascontains().
```
var text = "Wow, incredible!"

print("inedible".is_subsequence_of(text)) # Prints true
print("Word!".is_subsequence_of(text))    # Prints true
print("Window".is_subsequence_of(text))   # Prints false
print("".is_subsequence_of(text))         # Prints true
```
boolis_subsequence_ofn(text:String)const🔗
Returnstrueif all characters of this string can be found intextin their original order,ignoring case. This is not the same ascontainsn().
boolis_valid_ascii_identifier()const🔗
Returnstrueif this string is a valid ASCII identifier. A valid ASCII identifier may contain only letters, digits, and underscores (_), and the first character may not be a digit.
```
print("node_2d".is_valid_ascii_identifier())    # Prints true
print("TYPE_FLOAT".is_valid_ascii_identifier()) # Prints true
print("1st_method".is_valid_ascii_identifier()) # Prints false
print("MyMethod#2".is_valid_ascii_identifier()) # Prints false
```
See alsois_valid_unicode_identifier().
boolis_valid_filename()const🔗
Returnstrueif this string is a valid file name. A valid file name cannot be empty, begin or end with space characters, or contain characters that are not allowed (:/\?*"|%<>).
boolis_valid_float()const🔗
Returnstrueif this string represents a valid floating-point number. A valid float may contain only digits, one decimal point (.), and the exponent letter (e). It may also be prefixed with a positive (+) or negative (-) sign. Any valid integer is also a valid float (seeis_valid_int()). See alsoto_float().
```
print("1.7".is_valid_float())   # Prints true
print("24".is_valid_float())    # Prints true
print("7e3".is_valid_float())   # Prints true
print("Hello".is_valid_float()) # Prints false
```
boolis_valid_hex_number(with_prefix:bool= false)const🔗
Returnstrueif this string is a valid hexadecimal number. A valid hexadecimal number only contains digits or lettersAtoF(either uppercase or lowercase), and may be prefixed with a positive (+) or negative (-) sign.
Ifwith_prefixistrue, the hexadecimal number needs to prefixed by"0x"to be considered valid.
```
print("A08E".is_valid_hex_number())    # Prints true
print("-AbCdEf".is_valid_hex_number()) # Prints true
print("2.5".is_valid_hex_number())     # Prints false

print("0xDEADC0DE".is_valid_hex_number(true)) # Prints true
```
boolis_valid_html_color()const🔗
Returnstrueif this string is a valid color in hexadecimal HTML notation. The string must be a hexadecimal value (seeis_valid_hex_number()) of either 3, 4, 6 or 8 digits, and may be prefixed by a hash sign (#). Other HTML notations for colors, such as names orhsl(), are not considered valid. See alsoColor.html().
boolis_valid_identifier()const🔗
Deprecated:Useis_valid_ascii_identifier()instead.
Returnstrueif this string is a valid identifier. A valid identifier may contain only letters, digits and underscores (_), and the first character may not be a digit.
```
print("node_2d".is_valid_identifier())    # Prints true
print("TYPE_FLOAT".is_valid_identifier()) # Prints true
print("1st_method".is_valid_identifier()) # Prints false
print("MyMethod#2".is_valid_identifier()) # Prints false
```
boolis_valid_int()const🔗
Returnstrueif this string represents a valid integer. A valid integer only contains digits, and may be prefixed with a positive (+) or negative (-) sign. See alsoto_int().
```
print("7".is_valid_int())    # Prints true
print("1.65".is_valid_int()) # Prints false
print("Hi".is_valid_int())   # Prints false
print("+3".is_valid_int())   # Prints true
print("-12".is_valid_int())  # Prints true
```
boolis_valid_ip_address()const🔗
Returnstrueif this string represents a well-formatted IPv4 or IPv6 address. This method considersreserved IP addressessuch as"0.0.0.0"and"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff"as valid.
boolis_valid_unicode_identifier()const🔗
Returnstrueif this string is a valid Unicode identifier.
A valid Unicode identifier must begin with a Unicode character of classXID_Startor"_", and may contain Unicode characters of classXID_Continuein the other positions.
```
print("node_2d".is_valid_unicode_identifier())      # Prints true
print("1st_method".is_valid_unicode_identifier())   # Prints false
print("MyMethod#2".is_valid_unicode_identifier())   # Prints false
print("állóképesség".is_valid_unicode_identifier()) # Prints true
print("выносливость".is_valid_unicode_identifier()) # Prints true
print("体力".is_valid_unicode_identifier())         # Prints true
```
See alsois_valid_ascii_identifier().
Note:This method checks identifiers the same way as GDScript. SeeTextServer.is_valid_identifier()for more advanced checks.
Stringjoin(parts:PackedStringArray)const🔗
Returns the concatenation ofparts' elements, with each element separated by the string calling this method. This method is the opposite ofsplit().
```
var fruits = ["Apple", "Orange", "Pear", "Kiwi"]

print(", ".join(fruits))  # Prints "Apple, Orange, Pear, Kiwi"
print("---".join(fruits)) # Prints "Apple---Orange---Pear---Kiwi"
```
```
string[] fruits = ["Apple", "Orange", "Pear", "Kiwi"];

// In C#, this method is static.
GD.Print(string.Join(", ", fruits));  // Prints "Apple, Orange, Pear, Kiwi"
GD.Print(string.Join("---", fruits)); // Prints "Apple---Orange---Pear---Kiwi"
```
Stringjson_escape()const🔗
Returns a copy of the string with special characters escaped using the JSON standard. Because it closely matches the C standard, it is possible to usec_unescape()to unescape the string, if necessary.
Stringleft(length:int)const🔗
Returns the firstlengthcharacters from the beginning of the string. Iflengthis negative, strips the lastlengthcharacters from the string's end.
```
print("Hello World!".left(3))  # Prints "Hel"
print("Hello World!".left(-4)) # Prints "Hello Wo"
```
intlength()const🔗
Returns the number of characters in the string. Empty strings ("") always return0. See alsois_empty().
Stringlpad(min_length:int, character:String= " ")const🔗
Formats the string to be at leastmin_lengthlong by addingcharacters to the left of the string, if necessary. See alsorpad().
Stringlstrip(chars:String)const🔗
Removes a set of characters defined incharsfrom the string's beginning. See alsorstrip().
Note:charsis not a prefix. Usetrim_prefix()to remove a single prefix, rather than a set of characters.
boolmatch(expr:String)const🔗
Does a simple expression match (also called "glob" or "globbing"), where*matches zero or more arbitrary characters and?matches any single character except a period (.). An empty string or empty expression always evaluates tofalse.
boolmatchn(expr:String)const🔗
Does a simplecase-insensitiveexpression match, where*matches zero or more arbitrary characters and?matches any single character except a period (.). An empty string or empty expression always evaluates tofalse.
PackedByteArraymd5_buffer()const🔗
Returns theMD5 hashof the string as aPackedByteArray.
Stringmd5_text()const🔗
Returns theMD5 hashof the string as anotherString.
intnaturalcasecmp_to(to:String)const🔗
Performs acase-sensitive,natural ordercomparison to another string. Returns-1if less than,1if greater than, or0if equal. "Less than" or "greater than" are determined by theUnicode code pointsof each string, which roughly matches the alphabetical order.
When used for sorting, natural order comparison orders sequences of numbers by the combined value of each digit as is often expected, instead of the single digit's value. A sorted sequence of numbered strings will be["1","2","3",...], not["1","10","2","3",...].
If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor:1will be returned if this string is longer than thetostring, or-1if shorter. Note that the length of empty strings is always0.
To get aboolresult from a string comparison, use the==operator instead. See alsonaturalnocasecmp_to(),filecasecmp_to(), andnocasecmp_to().
intnaturalnocasecmp_to(to:String)const🔗
Performs acase-insensitive,natural ordercomparison to another string. Returns-1if less than,1if greater than, or0if equal. "Less than" or "greater than" are determined by theUnicode code pointsof each string, which roughly matches the alphabetical order. Internally, lowercase characters are converted to uppercase for the comparison.
When used for sorting, natural order comparison orders sequences of numbers by the combined value of each digit as is often expected, instead of the single digit's value. A sorted sequence of numbered strings will be["1","2","3",...], not["1","10","2","3",...].
If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor:1will be returned if this string is longer than thetostring, or-1if shorter. Note that the length of empty strings is always0.
To get aboolresult from a string comparison, use the==operator instead. See alsonaturalcasecmp_to(),filenocasecmp_to(), andcasecmp_to().
intnocasecmp_to(to:String)const🔗
Performs acase-insensitivecomparison to another string. Returns-1if less than,1if greater than, or0if equal. "Less than" or "greater than" are determined by theUnicode code pointsof each string, which roughly matches the alphabetical order. Internally, lowercase characters are converted to uppercase for the comparison.
If the character comparison reaches the end of one string, but the other string contains more characters, then it will use length as the deciding factor:1will be returned if this string is longer than thetostring, or-1if shorter. Note that the length of empty strings is always0.
To get aboolresult from a string comparison, use the==operator instead. See alsocasecmp_to(),filenocasecmp_to(), andnaturalnocasecmp_to().
Stringnum(number:float, decimals:int= -1)static🔗
Converts afloatto a string representation of a decimal number, with the number of decimal places specified indecimals.
Ifdecimalsis-1as by default, the string representation may only have up to 14 significant digits, with digits before the decimal point having priority over digits after.
Trailing zeros are not included in the string. The last digit is rounded, not truncated.
```
String.num(3.141593)     # Returns "3.141593"
String.num(3.141593, 3)  # Returns "3.142"
String.num(3.14159300)   # Returns "3.141593"

# Here, the last digit will be rounded up,
# which reduces the total digit count, since trailing zeros are removed:
String.num(42.129999, 5) # Returns "42.13"

# If `decimals` is not specified, the maximum number of significant digits is 14:
String.num(-0.0000012345432123454321)     # Returns "-0.00000123454321"
String.num(-10000.0000012345432123454321) # Returns "-10000.0000012345"
```
Stringnum_int64(number:int, base:int= 10, capitalize_hex:bool= false)static🔗
Converts the givennumberto a string representation, with the givenbase.
By default,baseis set to decimal (10). Other common bases in programming include binary (2),octal(8), hexadecimal (16).
Ifcapitalize_hexistrue, digits higher than 9 are represented in uppercase.
Stringnum_scientific(number:float)static🔗
Converts the givennumberto a string representation, in scientific notation.
```
var n = -5.2e8
print(n)                        # Prints -520000000
print(String.num_scientific(n)) # Prints -5.2e+08
```
```
// This method is not implemented in C#.
// Use `string.ToString()` with "e" to achieve similar results.
var n = -5.2e8f;
GD.Print(n);                // Prints -520000000
GD.Print(n.ToString("e1")); // Prints -5.2e+008
```
Note:In C#, this method is not implemented. To achieve similar results, see C#'sStandard numeric format strings.
Stringnum_uint64(number:int, base:int= 10, capitalize_hex:bool= false)static🔗
Converts the given unsignedintto a string representation, with the givenbase.
By default,baseis set to decimal (10). Other common bases in programming include binary (2),octal(8), hexadecimal (16).
Ifcapitalize_hexistrue, digits higher than 9 are represented in uppercase.
Stringpad_decimals(digits:int)const🔗
Formats the string representing a number to have an exact number ofdigitsafterthe decimal point.
Stringpad_zeros(digits:int)const🔗
Formats the string representing a number to have an exact number ofdigitsbeforethe decimal point.
Stringpath_join(path:String)const🔗
Concatenatespathat the end of the string as a subpath, adding/if necessary.
Example:"this/is".path_join("path")=="this/is/path".
Stringremove_char(what:int)const🔗
Removes all occurrences of the Unicode character with codewhat. Faster version ofreplace()when the key is only one character long and the replacement is"".
Stringremove_chars(chars:String)const🔗
Removes all occurrences of the characters inchars. See alsoremove_char().
Stringrepeat(count:int)const🔗
Repeats this string a number of times.countneeds to be greater than0. Otherwise, returns an empty string.
Stringreplace(what:String, forwhat:String)const🔗
Replaces all occurrences ofwhatinside the string with the givenforwhat.
Stringreplace_char(key:int, with:int)const🔗
Replaces all occurrences of the Unicode character with codekeywith the Unicode character with codewith. Faster version ofreplace()when the key is only one character long. To get a single character use"X".unicode_at(0)(note that some strings, like compound letters and emoji, can be composed of multiple unicode codepoints, and will not work with this method, uselength()to make sure).
Stringreplace_chars(keys:String, with:int)const🔗
Replaces any occurrence of the characters inkeyswith the Unicode character with codewith. See alsoreplace_char().
Stringreplacen(what:String, forwhat:String)const🔗
Replaces allcase-insensitiveoccurrences ofwhatinside the string with the givenforwhat.
Stringreverse()const🔗
Returns the copy of this string in reverse order. This operation works on unicode codepoints, rather than sequences of codepoints, and may break things like compound letters or emojis.
intrfind(what:String, from:int= -1)const🔗
Returns the index of thelastoccurrence ofwhatin this string, or-1if there are none. The search's start can be specified withfrom, continuing to the beginning of the string. This method is the reverse offind().
Note:A negative value offromis converted to a starting index by counting back from the last possible index with enough space to findwhat.
Note:A value offromthat is greater than the last possible index with enough space to findwhatis considered out-of-bounds, and returns-1.
intrfindn(what:String, from:int= -1)const🔗
Returns the index of thelastcase-insensitiveoccurrence ofwhatin this string, or-1if there are none. The starting search index can be specified withfrom, continuing to the beginning of the string. This method is the reverse offindn().
Stringright(length:int)const🔗
Returns the lastlengthcharacters from the end of the string. Iflengthis negative, strips the firstlengthcharacters from the string's beginning.
```
print("Hello World!".right(3))  # Prints "ld!"
print("Hello World!".right(-4)) # Prints "o World!"
```
Stringrpad(min_length:int, character:String= " ")const🔗
Formats the string to be at leastmin_lengthlong, by addingcharacters to the right of the string, if necessary. See alsolpad().
PackedStringArrayrsplit(delimiter:String= "", allow_empty:bool= true, maxsplit:int= 0)const🔗
Splits the string using adelimiterand returns an array of the substrings, starting from the end of the string. The splits in the returned array appear in the same order as the original string. Ifdelimiteris an empty string, each substring will be a single character.
Ifallow_emptyisfalse, empty strings between adjacent delimiters are excluded from the array.
Ifmaxsplitis greater than0, the number of splits may not exceedmaxsplit. By default, the entire string is split, which is mostly identical tosplit().
```
var some_string = "One,Two,Three,Four"
var some_array = some_string.rsplit(",", true, 1)

print(some_array.size()) # Prints 2
print(some_array[0])     # Prints "One,Two,Three"
print(some_array[1])     # Prints "Four"
```
```
// In C#, there is no String.RSplit() method.
```
Stringrstrip(chars:String)const🔗
Removes a set of characters defined incharsfrom the string's end. See alsolstrip().
Note:charsis not a suffix. Usetrim_suffix()to remove a single suffix, rather than a set of characters.
PackedByteArraysha1_buffer()const🔗
Returns theSHA-1hash of the string as aPackedByteArray.
Stringsha1_text()const🔗
Returns theSHA-1hash of the string as anotherString.
PackedByteArraysha256_buffer()const🔗
Returns theSHA-256hash of the string as aPackedByteArray.
Stringsha256_text()const🔗
Returns theSHA-256hash of the string as anotherString.
floatsimilarity(text:String)const🔗
Returns the similarity index (Sørensen-Dice coefficient) of this string compared to another. A result of1.0means totally similar, while0.0means totally dissimilar.
```
print("ABC123".similarity("ABC123")) # Prints 1.0
print("ABC123".similarity("XYZ456")) # Prints 0.0
print("ABC123".similarity("123ABC")) # Prints 0.8
print("ABC123".similarity("abc123")) # Prints 0.4
```
Stringsimplify_path()const🔗
If the string is a valid file path, converts the string into a canonical path. This is the shortest possible path, without"./", and all the unnecessary".."and"/".
```
var simple_path = "./path/to///../file".simplify_path()
print(simple_path) # Prints "path/file"
```
PackedStringArraysplit(delimiter:String= "", allow_empty:bool= true, maxsplit:int= 0)const🔗
Splits the string using adelimiterand returns an array of the substrings. Ifdelimiteris an empty string, each substring will be a single character. This method is the opposite ofjoin().
Ifallow_emptyisfalse, empty strings between adjacent delimiters are excluded from the array.
Ifmaxsplitis greater than0, the number of splits may not exceedmaxsplit. By default, the entire string is split.
```
var some_array = "One,Two,Three,Four".split(",", true, 2)

print(some_array.size()) # Prints 3
print(some_array[0])     # Prints "One"
print(some_array[1])     # Prints "Two"
print(some_array[2])     # Prints "Three,Four"
```
```
// C#'s `Split()` does not support the `maxsplit` parameter.
var someArray = "One,Two,Three".Split(",");

GD.Print(someArray[0]); // Prints "One"
GD.Print(someArray[1]); // Prints "Two"
GD.Print(someArray[2]); // Prints "Three"
```
Note:If you only need one substring from the array, consider usingget_slice()which is faster. If you need to split strings with more complex rules, use theRegExclass instead.
PackedFloat64Arraysplit_floats(delimiter:String, allow_empty:bool= true)const🔗
Splits the string into floats by using adelimiterand returns aPackedFloat64Array.
Ifallow_emptyisfalse, empty or invalidfloatconversions between adjacent delimiters are excluded.
```
var a = "1,2,4.5".split_floats(",")         # a is [1.0, 2.0, 4.5]
var c = "1| ||4.5".split_floats("|")        # c is [1.0, 0.0, 0.0, 4.5]
var b = "1| ||4.5".split_floats("|", false) # b is [1.0, 4.5]
```
Stringstrip_edges(left:bool= true, right:bool= true)const🔗
Strips all non-printable characters from the beginning and the end of the string. These include spaces, tabulations (\t), and newlines (\n\r).
Ifleftisfalse, ignores the string's beginning. Likewise, ifrightisfalse, ignores the string's end.
Stringstrip_escapes()const🔗
Strips all escape characters from the string. These include all non-printable control characters of the first page of the ASCII table (values from 0 to 31), such as tabulation (\t) and newline (\n,\r) characters, butnotspaces.
Stringsubstr(from:int, len:int= -1)const🔗
Returns part of the string from the positionfromwith lengthlen. Iflenis-1(as by default), returns the rest of the string starting from the given position.
PackedByteArrayto_ascii_buffer()const🔗
Converts the string to anASCII/Latin-1 encodedPackedByteArray. This method is slightly faster thanto_utf8_buffer(), but replaces all unsupported characters with spaces. This is the inverse ofPackedByteArray.get_string_from_ascii().
Stringto_camel_case()const🔗
Returns the string converted tocamelCase.
floatto_float()const🔗
Converts the string representing a decimal number into afloat. This method stops on the first non-number character, except the first decimal point (.) and the exponent letter (e). See alsois_valid_float().
```
var a = "12.35".to_float()  # a is 12.35
var b = "1.2.3".to_float()  # b is 1.2
var c = "12xy3".to_float()  # c is 12.0
var d = "1e3".to_float()    # d is 1000.0
var e = "Hello!".to_float() # e is 0.0
```
intto_int()const🔗
Converts the string representing an integer number into anint. This method removes any non-number character and stops at the first decimal point (.). See alsois_valid_int().
```
var a = "123".to_int()    # a is 123
var b = "x1y2z3".to_int() # b is 123
var c = "-1.2.3".to_int() # c is -1
var d = "Hello!".to_int() # d is 0
```
Stringto_kebab_case()const🔗
Returns the string converted tokebab-case.
Note:Numbers followed by asingleletter are not separated in the conversion to keep some words (such as "2D") together.
```
"Node2D".to_kebab_case()               # Returns "node-2d"
"2nd place".to_kebab_case()            # Returns "2-nd-place"
"Texture3DAssetFolder".to_kebab_case() # Returns "texture-3d-asset-folder"
```
```
"Node2D".ToKebabCase();               // Returns "node-2d"
"2nd place".ToKebabCase();            // Returns "2-nd-place"
"Texture3DAssetFolder".ToKebabCase(); // Returns "texture-3d-asset-folder"
```
Stringto_lower()const🔗
Returns the string converted tolowercase.
PackedByteArrayto_multibyte_char_buffer(encoding:String= "")const🔗
Converts the string to system multibyte code page encodedPackedByteArray. If conversion fails, empty array is returned.
The values permitted forencodingare system dependent. Ifencodingis empty string, system default encoding is used.
- For Windows, seeCode Page Identifiers.NET names.
For Windows, seeCode Page Identifiers.NET names.
- For macOS and Linux/BSD, seelibiconvlibrary documentation andiconv--listfor a list of supported encodings.
For macOS and Linux/BSD, seelibiconvlibrary documentation andiconv--listfor a list of supported encodings.
Stringto_pascal_case()const🔗
Returns the string converted toPascalCase.
Stringto_snake_case()const🔗
Returns the string converted tosnake_case.
Note:Numbers followed by asingleletter are not separated in the conversion to keep some words (such as "2D") together.
```
"Node2D".to_snake_case()               # Returns "node_2d"
"2nd place".to_snake_case()            # Returns "2_nd_place"
"Texture3DAssetFolder".to_snake_case() # Returns "texture_3d_asset_folder"
```
```
"Node2D".ToSnakeCase();               // Returns "node_2d"
"2nd place".ToSnakeCase();            // Returns "2_nd_place"
"Texture3DAssetFolder".ToSnakeCase(); // Returns "texture_3d_asset_folder"
```
Stringto_upper()const🔗
Returns the string converted toUPPERCASE.
PackedByteArrayto_utf8_buffer()const🔗
Converts the string to aUTF-8encodedPackedByteArray. This method is slightly slower thanto_ascii_buffer(), but supports all UTF-8 characters. For most cases, prefer using this method. This is the inverse ofPackedByteArray.get_string_from_utf8().
PackedByteArrayto_utf16_buffer()const🔗
Converts the string to aUTF-16encodedPackedByteArray. This is the inverse ofPackedByteArray.get_string_from_utf16().
PackedByteArrayto_utf32_buffer()const🔗
Converts the string to aUTF-32encodedPackedByteArray. This is the inverse ofPackedByteArray.get_string_from_utf32().
PackedByteArrayto_wchar_buffer()const🔗
Converts the string to awide character(wchar_t, UTF-16 on Windows, UTF-32 on other platforms) encodedPackedByteArray. This is the inverse ofPackedByteArray.get_string_from_wchar().
Stringtrim_prefix(prefix:String)const🔗
Removes the givenprefixfrom the start of the string, or returns the string unchanged.
Stringtrim_suffix(suffix:String)const🔗
Removes the givensuffixfrom the end of the string, or returns the string unchanged.
intunicode_at(at:int)const🔗
Returns the character code at positionat.
See alsochr(),@GDScript.char(), and@GDScript.ord().
Stringuri_decode()const🔗
Decodes the string from its URL-encoded format. This method is meant to properly decode the parameters in a URL when receiving an HTTP request. See alsouri_encode().
```
var url = "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
print(url.uri_decode()) # Prints "$DOCS_URL/?highlight=Godot Engine:docs"
```
```
var url = "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
GD.Print(url.URIDecode()) // Prints "$DOCS_URL/?highlight=Godot Engine:docs"
```
Note:This method decodes+as space.
Stringuri_encode()const🔗
Encodes the string to URL-friendly format. This method is meant to properly encode the parameters in a URL when sending an HTTP request. See alsouri_decode().
```
var prefix = "$DOCS_URL/?highlight="
var url = prefix + "Godot Engine:docs".uri_encode()

print(url) # Prints "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
```
```
var prefix = "$DOCS_URL/?highlight=";
var url = prefix + "Godot Engine:docs".URIEncode();

GD.Print(url); // Prints "$DOCS_URL/?highlight=Godot%20Engine%3%docs"
```
Stringuri_file_decode()const🔗
Decodes the file path from its URL-encoded format. Unlikeuri_decode()this method leaves+as is.
Stringvalidate_filename()const🔗
Returns a copy of the string with all characters that are not allowed inis_valid_filename()replaced with underscores.
Stringvalidate_node_name()const🔗
Returns a copy of the string with all characters that are not allowed inNode.name(.:@/"%) replaced with underscores.
Stringxml_escape(escape_quotes:bool= false)const🔗
Returns a copy of the string with special characters escaped using the XML standard. Ifescape_quotesistrue, the single quote (') and double quote (") characters are also escaped.
Stringxml_unescape()const🔗
Returns a copy of the string with escaped characters replaced by their meanings according to the XML standard.

## Operator Descriptions
booloperator !=(right:String)🔗
Returnstrueif both strings do not contain the same sequence of characters.
booloperator !=(right:StringName)🔗
Returnstrueif thisStringis not equivalent to the givenStringName.
Stringoperator %(right:Variant)🔗
Formats theString, replacing the placeholders with one or more parameters. To pass multiple parameters,rightneeds to be anArray.
```
print("I caught %d fishes!" % 2) # Prints "I caught 2 fishes!"

var my_message = "Travelling to %s, at %2.2f km/h."
var location = "Deep Valley"
var speed = 40.3485
print(my_message % [location, speed]) # Prints "Travelling to Deep Valley, at 40.35 km/h."
```
For more information, see theGDScript format stringstutorial.
Note:In C#, this operator is not available. Instead, seehow to interpolate strings with "$".
Stringoperator +(right:String)🔗
Appendsrightat the end of thisString, also known as a string concatenation.
Stringoperator +(right:StringName)🔗
Appendsrightat the end of thisString, returning aString. This is also known as a string concatenation.
booloperator <(right:String)🔗
Returnstrueif the leftStringcomes beforerightinUnicode order, which roughly matches the alphabetical order. Useful for sorting.
booloperator <=(right:String)🔗
Returnstrueif the leftStringcomes beforerightinUnicode order, which roughly matches the alphabetical order, or if both are equal.
booloperator ==(right:String)🔗
Returnstrueif both strings contain the same sequence of characters.
booloperator ==(right:StringName)🔗
Returnstrueif thisStringis equivalent to the givenStringName.
booloperator >(right:String)🔗
Returnstrueif the leftStringcomes afterrightinUnicode order, which roughly matches the alphabetical order. Useful for sorting.
booloperator >=(right:String)🔗
Returnstrueif the leftStringcomes afterrightinUnicode order, which roughly matches the alphabetical order, or if both are equal.
Stringoperator [](index:int)🔗
Returns a newStringthat only contains the character atindex. Indices start from0. Ifindexis greater or equal to0, the character is fetched starting from the beginning of the string. Ifindexis a negative value, it is fetched starting from the end. Accessing a string out-of-bounds will cause a run-time error, pausing the project execution if run from the editor.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.