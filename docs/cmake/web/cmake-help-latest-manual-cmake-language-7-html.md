# Source: https://cmake.org/cmake/help/latest/manual/cmake-language.7.html

Title: cmake-language(7) — CMake 4.3.0-rc3 Documentation

URL Source: https://cmake.org/cmake/help/latest/manual/cmake-language.7.html

Markdown Content:
Contents

*   [cmake-language(7)](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#cmake-language-7)

    *   [Organization](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#organization)

        *   [Directories](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#directories)

        *   [Scripts](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#scripts)

        *   [Modules](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#modules)

    *   [Syntax](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#syntax)

        *   [Encoding](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#encoding)

        *   [Source Files](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#source-files)

        *   [Command Invocations](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-invocations)

        *   [Command Arguments](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-arguments)

            *   [Bracket Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#bracket-argument)

            *   [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument)

            *   [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument)

        *   [Escape Sequences](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#escape-sequences)

        *   [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references)

        *   [Comments](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#comments)

            *   [Bracket Comment](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#bracket-comment)

            *   [Line Comment](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#line-comment)

    *   [Control Structures](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#control-structures)

        *   [Conditional Blocks](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#conditional-blocks)

        *   [Loops](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#loops)

        *   [Command Definitions](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-definitions)

    *   [Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables)

    *   [Environment Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#environment-variables)

    *   [Lists](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#lists)

[Organization](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id10)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#organization "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

CMake input files are written in the "CMake Language" in source files named `CMakeLists.txt` or ending in a `.cmake` file name extension. The term _listfile_ is a general name for any such source file containing CMake commands that the tool processes.

CMake Language source files in a project are organized into:

*   [Directories](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#directories) (`CMakeLists.txt`),

*   [Scripts](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#scripts) (`<script>.cmake`), and

*   [Modules](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#modules) (`<module>.cmake`).

### [Directories](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id11)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#directories "Link to this heading")

When CMake processes a project source tree, the entry point is a source file called `CMakeLists.txt` in the top-level source directory. This file may contain the entire build specification or use the [`add_subdirectory()`](https://cmake.org/cmake/help/latest/command/add_subdirectory.html#command:add_subdirectory "add_subdirectory") command to add subdirectories to the build. Each subdirectory added by the command must also contain a `CMakeLists.txt` file as the entry point to that directory. For each source directory whose `CMakeLists.txt` file is processed CMake generates a corresponding directory in the build tree to act as the default working and output directory.

### [Scripts](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id12)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#scripts "Link to this heading")

An individual `<script>.cmake` source file may be processed in _script mode_ by using the [`cmake(1)`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#manual:cmake(1) "cmake(1)") command-line tool with the [`-P`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-P) option. Script mode simply runs the commands in the given CMake Language source file and does not generate a build system. It does not allow CMake commands that define build targets or actions.

### [Modules](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id13)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#modules "Link to this heading")

CMake Language code in either [Directories](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#directories) or [Scripts](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#scripts) may use the [`include()`](https://cmake.org/cmake/help/latest/command/include.html#command:include "include") command to load a `<module>.cmake` source file in the scope of the including context. See the [`cmake-modules(7)`](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html#manual:cmake-modules(7) "cmake-modules(7)") manual page for documentation of modules included with the CMake distribution. Project source trees may also provide their own modules and specify their location(s) in the [`CMAKE_MODULE_PATH`](https://cmake.org/cmake/help/latest/variable/CMAKE_MODULE_PATH.html#variable:CMAKE_MODULE_PATH "CMAKE_MODULE_PATH") variable.

[Syntax](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id14)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#syntax "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Encoding](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id15)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#encoding "Link to this heading")

A CMake Language source file may be written in 7-bit ASCII text for maximum portability across all supported platforms. Newlines may be encoded as either `\n` or `\r\n` but will be converted to `\n` as input files are read.

Note that the implementation is 8-bit clean so source files may be encoded as UTF-8 on platforms with system APIs supporting this encoding. In addition, CMake 3.2 and above support source files encoded in UTF-8 on Windows (using UTF-16 to call system APIs). Furthermore, CMake 3.0 and above allow a leading UTF-8 [Byte-Order Mark](https://en.wikipedia.org/wiki/Byte_order_mark) in source files.

Added in version 4.3: The [`cmake_host_system_information()`](https://cmake.org/cmake/help/latest/command/cmake_host_system_information.html#command:cmake_host_system_information "cmake_host_system_information") command's `LOCALE_CHARSET` query returns the expected character set encoding.

### [Source Files](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id16)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#source-files "Link to this heading")

A CMake Language source file consists of zero or more [Command Invocations](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-invocations) separated by newlines and optionally spaces and [Comments](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#comments):

**file**         ::= [`file_element`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-file_element)*
**file_element** ::= [`command_invocation`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-command_invocation) [`line_ending`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-line_ending) |
                 ([`bracket_comment`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_comment)|[`space`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-space))* [`line_ending`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-line_ending)
**line_ending**  ::= [`line_comment`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-line_comment)? [`newline`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-newline)
**space**        ::= <match '[ \t]+'>
**newline**      ::= <match '\n'>

Note that any source file line not inside [Command Arguments](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-arguments) or a [Bracket Comment](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#bracket-comment) can end in a [Line Comment](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#line-comment).

### [Command Invocations](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id17)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-invocations "Link to this heading")

A _command invocation_ is a name followed by paren-enclosed arguments separated by whitespace:

**command_invocation**  ::= [`space`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-space)* [`identifier`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-identifier) [`space`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-space)* '(' [`arguments`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-arguments) ')'
**identifier**          ::= <match '[A-Za-z_][A-Za-z0-9_]*'>
**arguments**           ::= [`argument`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-argument)? [`separated_arguments`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-separated_arguments)*
**separated_arguments** ::= [`separation`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-separation)+ [`argument`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-argument)? |
                        [`separation`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-separation)* '(' [`arguments`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-arguments) ')'
**separation**          ::= [`space`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-space) | [`line_ending`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-line_ending)

For example:

add_executable(hello world.c)

Command names are case-insensitive. Nested unquoted parentheses in the arguments must balance. Each `(` or `)` is given to the command invocation as a literal [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument). This may be used in calls to the [`if()`](https://cmake.org/cmake/help/latest/command/if.html#command:if "if") command to enclose conditions. For example:

if(FALSE AND (FALSE OR TRUE)) # evaluates to FALSE

Note

CMake versions prior to 3.0 require command name identifiers to be at least 2 characters.

CMake versions prior to 2.8.12 silently accept an [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument) or a [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument) immediately following a [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument) and not separated by any whitespace. For compatibility, CMake 2.8.12 and higher accept such code but produce a warning.

### [Command Arguments](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id18)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-arguments "Link to this heading")

There are three types of arguments within [Command Invocations](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-invocations):

**argument** ::= [`bracket_argument`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_argument) | [`quoted_argument`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-quoted_argument) | [`unquoted_argument`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-unquoted_argument)

#### [Bracket Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id19)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#bracket-argument "Link to this heading")

A _bracket argument_, inspired by [Lua](https://www.lua.org/) long bracket syntax, encloses content between opening and closing "brackets" of the same length:

**bracket_argument** ::= [`bracket_open`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_open) [`bracket_content`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_content) [`bracket_close`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_close)
**bracket_open**     ::= '[' '='* '['
**bracket_content**  ::= <any text not containing a [`bracket_close`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_close) with
                     the same number of '=' as the [`bracket_open`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-bracket_open)>
**bracket_close**    ::= ']' '='* ']'

An opening bracket is written `[` followed by zero or more `=` followed by `[`. The corresponding closing bracket is written `]` followed by the same number of `=` followed by `]`. Brackets do not nest. A unique length may always be chosen for the opening and closing brackets to contain closing brackets of other lengths.

Bracket argument content consists of all text between the opening and closing brackets, except that one newline immediately following the opening bracket, if any, is ignored. No evaluation of the enclosed content, such as [Escape Sequences](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#escape-sequences) or [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references), is performed. A bracket argument is always given to the command invocation as exactly one argument.

For example:

message([=[
This is the first line in a bracket argument with bracket length 1.
No \-escape sequences or ${variable} references are evaluated.
This is always one argument even though it contains a ; character.
The text does not end on a closing bracket of length 0 like ]].
It does end in a closing bracket of length 1.
]=])

Note

CMake versions prior to 3.0 do not support bracket arguments. They interpret the opening bracket as the start of an [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument).

#### [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id20)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument "Link to this heading")

A _quoted argument_ encloses content between opening and closing double-quote characters:

**quoted_argument**     ::= '"' [`quoted_element`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-quoted_element)* '"'
**quoted_element**      ::= <any character except '\' or '"'> |
                        [`escape_sequence`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-escape_sequence) |
                        [`quoted_continuation`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-quoted_continuation)
**quoted_continuation** ::= '\' [`newline`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-newline)

Quoted argument content consists of all text between opening and closing quotes. Both [Escape Sequences](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#escape-sequences) and [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references) are evaluated. A quoted argument is always given to the command invocation as exactly one argument.

For example:

message("This is a quoted argument containing multiple lines.
This is always one argument even though it contains a ; character.
Both \\-escape sequences and ${variable} references are evaluated.
The text does not end on an escaped double-quote like \".
It does end in an unescaped double quote.
")

The final `\` on any line ending in an odd number of backslashes is treated as a line continuation and ignored along with the immediately following newline character. For example:

message("\
This is the first line of a quoted argument. \
In fact it is the only line but since it is long \
the source code uses line continuation.\
")

Note

CMake versions prior to 3.0 do not support continuation with `\`. They report errors in quoted arguments containing lines ending in an odd number of `\` characters.

#### [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id21)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument "Link to this heading")

An _unquoted argument_ is not enclosed by any quoting syntax. It may not contain any whitespace, `(`, `)`, `#`, `"`, or `\` except when escaped by a backslash:

**unquoted_argument** ::= [`unquoted_element`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-unquoted_element)+ | [`unquoted_legacy`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-unquoted_legacy)
**unquoted_element**  ::= <any character except whitespace or one of '()#"\'> |
                      [`escape_sequence`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-escape_sequence)
**unquoted_legacy**   ::= <see note in text>

Unquoted argument content consists of all text in a contiguous block of allowed or escaped characters. Both [Escape Sequences](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#escape-sequences) and [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references) are evaluated. The resulting value is divided in the same way [Lists](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#lists) divide into elements. Each non-empty element is given to the command invocation as an argument. Therefore an unquoted argument may be given to a command invocation as zero or more arguments.

For example:

foreach(arg
 NoSpace
 Escaped\ Space
 This;Divides;Into;Five;Arguments
 Escaped\;Semicolon
 )
 message("${arg}")
endforeach()

Note

To support legacy CMake code, unquoted arguments may also contain double-quoted strings (`"..."`, possibly enclosing horizontal whitespace), and make-style variable references (`$(MAKEVAR)`).

Unescaped double-quotes must balance, may not appear at the beginning of an unquoted argument, and are treated as part of the content. For example, the unquoted arguments `-Da="b c"`, `-Da=$(v)`, and `a" "b"c"d` are each interpreted literally. They may instead be written as quoted arguments `"-Da=\"b c\""`, `"-Da=$(v)"`, and `"a\" \"b\"c\"d"`, respectively.

Make-style references are treated literally as part of the content and do not undergo variable expansion. They are treated as part of a single argument (rather than as separate `$`, `(`, `MAKEVAR`, and `)` arguments).

The above "unquoted_legacy" production represents such arguments. We do not recommend using legacy unquoted arguments in new code. Instead use a [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument) or a [Bracket Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#bracket-argument) to represent the content.

### [Escape Sequences](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id22)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#escape-sequences "Link to this heading")

An _escape sequence_ is a `\` followed by one character:

**escape_sequence**  ::= [`escape_identity`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-escape_identity) | [`escape_encoded`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-escape_encoded) | [`escape_semicolon`](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#grammar-token-escape_semicolon)
**escape_identity**  ::= '\' <match '[^A-Za-z0-9;]'>
**escape_encoded**   ::= '\t' | '\r' | '\n'
**escape_semicolon** ::= '\;'

A `\` followed by a non-alphanumeric character simply encodes the literal character without interpreting it as syntax. A `\t`, `\r`, or `\n` encodes a tab, carriage return, or newline character, respectively. A `\;` outside of any [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references) encodes itself but may be used in an [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument) to encode the `;` without dividing the argument value on it. A `\;` inside [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references) encodes the literal `;` character. (See also policy [`CMP0053`](https://cmake.org/cmake/help/latest/policy/CMP0053.html#policy:CMP0053 "CMP0053") documentation for historical considerations.)

### [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id23)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references "Link to this heading")

A _variable reference_ has the form `${<variable>}` and is evaluated inside a [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument) or an [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument). A variable reference is replaced by the value of the specified variable or cache entry, or if neither is set, by the empty string. Variable references can nest and are evaluated from the inside out, e.g. `${outer_${inner_variable}_variable}`.

Literal variable references may consist of alphanumeric characters, the characters `/_.+-`, and [Escape Sequences](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#escape-sequences). Nested references may be used to evaluate variables of any name. See also policy [`CMP0053`](https://cmake.org/cmake/help/latest/policy/CMP0053.html#policy:CMP0053 "CMP0053") documentation for historical considerations and reasons why the `$` is also technically permitted but is discouraged.

The [Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables) section documents the scope of variable names and how their values are set.

An _environment variable reference_ has the form `$ENV{<variable>}`. See the [Environment Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#environment-variables) section for more information.

A _cache variable reference_ has the form `$CACHE{<variable>}`, and is replaced by the value of the specified cache entry without checking for a normal variable of the same name. If the cache entry does not exist, it is replaced by the empty string. See [`CACHE`](https://cmake.org/cmake/help/latest/variable/CACHE.html#variable:CACHE "CACHE") for more information.

The [`if()`](https://cmake.org/cmake/help/latest/command/if.html#command:if "if") command has a special condition syntax that allows for variable references in the short form `<variable>` instead of `${<variable>}`. However, environment variables always need to be referenced as `$ENV{<variable>}`.

[Control Structures](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id27)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#control-structures "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### [Conditional Blocks](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id28)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#conditional-blocks "Link to this heading")

The [`if()`](https://cmake.org/cmake/help/latest/command/if.html#command:if "if")/[`elseif()`](https://cmake.org/cmake/help/latest/command/elseif.html#command:elseif "elseif")/[`else()`](https://cmake.org/cmake/help/latest/command/else.html#command:else "else")/[`endif()`](https://cmake.org/cmake/help/latest/command/endif.html#command:endif "endif") commands delimit code blocks to be executed conditionally.

### [Loops](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id29)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#loops "Link to this heading")

The [`foreach()`](https://cmake.org/cmake/help/latest/command/foreach.html#command:foreach "foreach")/[`endforeach()`](https://cmake.org/cmake/help/latest/command/endforeach.html#command:endforeach "endforeach") and [`while()`](https://cmake.org/cmake/help/latest/command/while.html#command:while "while")/[`endwhile()`](https://cmake.org/cmake/help/latest/command/endwhile.html#command:endwhile "endwhile") commands delimit code blocks to be executed in a loop. Inside such blocks the [`break()`](https://cmake.org/cmake/help/latest/command/break.html#command:break "break") command may be used to terminate the loop early whereas the [`continue()`](https://cmake.org/cmake/help/latest/command/continue.html#command:continue "continue") command may be used to start with the next iteration immediately.

### [Command Definitions](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id30)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-definitions "Link to this heading")

The [`macro()`](https://cmake.org/cmake/help/latest/command/macro.html#command:macro "macro")/[`endmacro()`](https://cmake.org/cmake/help/latest/command/endmacro.html#command:endmacro "endmacro"), and [`function()`](https://cmake.org/cmake/help/latest/command/function.html#command:function "function")/[`endfunction()`](https://cmake.org/cmake/help/latest/command/endfunction.html#command:endfunction "endfunction") commands delimit code blocks to be recorded for later invocation as commands.

[Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id31)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Variables are the basic unit of storage in the CMake Language. Their values are always of string type, though some commands may interpret the strings as values of other types. The [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") and [`unset()`](https://cmake.org/cmake/help/latest/command/unset.html#command:unset "unset") commands explicitly set or unset a variable, but other commands have semantics that modify variables as well. Variable names are case-sensitive and may consist of almost any text, but we recommend sticking to names consisting only of alphanumeric characters plus `_` and `-`.

Variables have dynamic scope. Each variable "set" or "unset" creates a binding in the current scope:

Block Scope
The [`block()`](https://cmake.org/cmake/help/latest/command/block.html#command:block "block") command may create a new scope for variable bindings.

Function Scope
[Command Definitions](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#command-definitions) created by the [`function()`](https://cmake.org/cmake/help/latest/command/function.html#command:function "function") command create commands that, when invoked, process the recorded commands in a new variable binding scope. A variable "set" or "unset" binds in this scope and is visible for the current function and any nested calls within it, but not after the function returns.

Directory Scope
Each of the [Directories](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#directories) in a source tree has its own variable bindings. Before processing the `CMakeLists.txt` file for a directory, CMake copies all variable bindings currently defined in the parent directory, if any, to initialize the new directory scope. CMake [Scripts](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#scripts), when processed with [`cmake -P`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-P), bind variables in one "directory" scope.

A variable "set" or "unset" not inside a function call binds to the current directory scope.

Persistent Cache
CMake stores a separate set of "cache" variables, or "cache entries", whose values persist across multiple runs within a project build tree. Cache entries have an isolated binding scope modified only by explicit request, such as by the `CACHE` option of the [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") and [`unset()`](https://cmake.org/cmake/help/latest/command/unset.html#command:unset "unset") commands.

When evaluating [Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references), CMake first searches the function call stack, if any, for a binding and then falls back to the binding in the current directory scope, if any. If a "set" binding is found, its value is used. If an "unset" binding is found, or no binding is found, CMake then searches for a cache entry. If a cache entry is found, its value is used. Otherwise, the variable reference evaluates to an empty string. The `$CACHE{VAR}` syntax can be used to do direct cache entry lookups.

The [`cmake-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html#manual:cmake-variables(7) "cmake-variables(7)") manual documents the many variables that are provided by CMake or have meaning to CMake when set by project code.

Note

CMake reserves identifiers that:

*   begin with `CMAKE_` (upper-, lower-, or mixed-case), or

*   begin with `_CMAKE_` (upper-, lower-, or mixed-case), or

*   begin with `_` followed by the name of any [`CMake Command`](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html#manual:cmake-commands(7) "cmake-commands(7)").

[Environment Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id32)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#environment-variables "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Environment Variables are like ordinary [Variables](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variables), with the following differences:

Scope
Environment variables have global scope in a CMake process. They are never cached.

References
[Variable References](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#variable-references) have the form `$ENV{<variable>}`, using the [`ENV`](https://cmake.org/cmake/help/latest/variable/ENV.html#variable:ENV "ENV") operator.

Initialization
Initial values of the CMake environment variables are those of the calling process. Values can be changed using the [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") and [`unset()`](https://cmake.org/cmake/help/latest/command/unset.html#command:unset "unset") commands. These commands only affect the running CMake process, not the system environment at large. Changed values are not written back to the calling process, and they are not seen by subsequent build or test processes.

See the [`cmake -E env`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-env) command-line tool to run a command in a modified environment.

Inspection
See the [`cmake -E environment`](https://cmake.org/cmake/help/latest/manual/cmake.1.html#cmdoption-cmake-E-arg-environment) command-line tool to display all current environment variables.

The [`cmake-env-variables(7)`](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html#manual:cmake-env-variables(7) "cmake-env-variables(7)") manual documents environment variables that have special meaning to CMake.

[Lists](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#id33)[¶](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#lists "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Although all values in CMake are stored as strings, a string may be treated as a list in certain contexts, such as during evaluation of an [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument). In such contexts, a string is divided into list elements by splitting on `;` characters not following an unequal number of `[` and `]` characters and not immediately preceded by a `\`. The sequence `\;` does not divide a value but is replaced by `;` in the resulting element.

A list of elements is represented as a string by concatenating the elements separated by `;`. For example, the [`set()`](https://cmake.org/cmake/help/latest/command/set.html#command:set "set") command stores multiple values into the destination variable as a list:

set(srcs a.c b.c c.c) # sets "srcs" to "a.c;b.c;c.c"

Lists are meant for simple use cases such as a list of source files and should not be used for complex data processing tasks. Most commands that construct lists do not escape `;` characters in list elements, thus flattening nested lists:

set(x a "b;c") # sets "x" to "a;b;c", not "a;b\;c"

In general, lists do not support elements containing `;` characters. To avoid problems, consider the following advice:

*   The interfaces of many CMake commands, variables, and properties accept semicolon-separated lists. Avoid passing lists with elements containing semicolons to these interfaces unless they document either direct support or some way to escape or encode semicolons.

*   When constructing a list, substitute an otherwise-unused placeholder for `;` in elements when. Then substitute `;` for the placeholder when processing list elements. For example, the following code uses `|` in place of `;` characters:

set(mylist a "b|c")
foreach(entry IN LISTS mylist)
 string(REPLACE "|" ";" entry "${entry}")
 # use "${entry}" normally
endforeach() 
The [`ExternalProject`](https://cmake.org/cmake/help/latest/module/ExternalProject.html#module:ExternalProject "ExternalProject") module's `LIST_SEPARATOR` option is an example of an interface built using this approach.

*   In lists of [`generator expressions`](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#manual:cmake-generator-expressions(7) "cmake-generator-expressions(7)"), use the [`$<SEMICOLON>`](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html#genex:SEMICOLON "SEMICOLON") generator expression.

*   In command calls, use [Quoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#quoted-argument) syntax whenever possible. The called command will receive the content of the argument with semicolons preserved. An [Unquoted Argument](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html#unquoted-argument) will be split on semicolons.

*   In [`function()`](https://cmake.org/cmake/help/latest/command/function.html#command:function "function") implementations, avoid `ARGV` and `ARGN`, which do not distinguish semicolons in values from those separating values. Instead, prefer using named positional arguments and the `ARGC` and `ARGV#` variables. When using [`cmake_parse_arguments()`](https://cmake.org/cmake/help/latest/command/cmake_parse_arguments.html#command:cmake_parse_arguments "cmake_parse_arguments") to parse arguments, prefer its `PARSE_ARGV` signature, which uses the `ARGV#` variables.

Note that this approach does not apply to [`macro()`](https://cmake.org/cmake/help/latest/command/macro.html#command:macro "macro") implementations because they reference arguments using placeholders, not real variables.
