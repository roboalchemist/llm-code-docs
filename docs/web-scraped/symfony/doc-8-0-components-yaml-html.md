# Source: https://symfony.com/doc/8.0/components/yaml.html

Title: The Yaml Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/yaml.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/components/yaml.rst)

The Symfony Yaml component loads and dumps YAML files. It parses YAML strings into PHP arrays and can also convert PHP arrays back into YAML strings.

[YAML](https://yaml.org/), _YAML Ain't Markup Language_, is a human-friendly data serialization language for all programming languages. It is a popular format for configuration files, balancing readability with advanced features.

[Installation](https://symfony.com/doc/8.0/components/yaml.html#installation "Permalink to this headline")
----------------------------------------------------------------------------------------------------------

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/current/components/using_components.html) for more details.

[Why?](https://symfony.com/doc/8.0/components/yaml.html#why "Permalink to this headline")
-----------------------------------------------------------------------------------------

### [Fast](https://symfony.com/doc/8.0/components/yaml.html#fast "Permalink to this headline")

One of the goals of Symfony Yaml is to find the right balance between speed and features. It supports just the needed features to handle configuration files. Notable lacking features are: document directives, multi-line quoted messages, compact block collections and multi-document files.

### [Real Parser](https://symfony.com/doc/8.0/components/yaml.html#real-parser "Permalink to this headline")

It supports a real parser and is able to parse a large subset of the YAML specification, for all your configuration needs. It also means that the parser is pretty robust, easy to understand, and simple enough to extend.

### [Clear Error Messages](https://symfony.com/doc/8.0/components/yaml.html#clear-error-messages "Permalink to this headline")

Whenever you have a syntax problem with your YAML files, the library outputs a helpful message with the filename and the line number where the problem occurred. It eases the debugging a lot.

### [Dump Support](https://symfony.com/doc/8.0/components/yaml.html#dump-support "Permalink to this headline")

It is also able to dump PHP arrays to YAML with object support, and inline level configuration for pretty outputs.

### [Types Support](https://symfony.com/doc/8.0/components/yaml.html#types-support "Permalink to this headline")

It supports most of the YAML built-in types like dates, integers, octal numbers, booleans, and much more...

### [Full Merge Key Support](https://symfony.com/doc/8.0/components/yaml.html#full-merge-key-support "Permalink to this headline")

Full support for references, aliases, and full merge key. Don't repeat yourself by referencing common configuration bits.

[Using the Symfony YAML Component](https://symfony.com/doc/8.0/components/yaml.html#using-the-symfony-yaml-component "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------

The Symfony Yaml component consists of two main classes: one parses YAML strings ([Parser](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Parser.php "Symfony\Component\Yaml\Parser")), and the other dumps a PHP array to a YAML string ([Dumper](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Dumper.php "Symfony\Component\Yaml\Dumper")).

On top of these two classes, the [Yaml](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Yaml.php "Symfony\Component\Yaml\Yaml") class acts as a thin wrapper that simplifies common uses.

### [Reading YAML Contents](https://symfony.com/doc/8.0/components/yaml.html#reading-yaml-contents "Permalink to this headline")

The [parse()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Yaml.php#:~:text=function%20parse "Symfony\Component\Yaml\Yaml::parse()") method parses a YAML string and converts it to a PHP array:

If an error occurs during parsing, the parser throws a [ParseException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Exception/ParseException.php "Symfony\Component\Yaml\Exception\ParseException") exception indicating the error type and the line in the original YAML string where the error occurred:

### [Reading YAML Files](https://symfony.com/doc/8.0/components/yaml.html#reading-yaml-files "Permalink to this headline")

The [parseFile()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Yaml.php#:~:text=function%20parseFile "Symfony\Component\Yaml\Yaml::parseFile()") method parses the YAML contents of the given file path and converts them to a PHP value:

If an error occurs during parsing, the parser throws a `ParseException` exception.

### [Writing YAML Files](https://symfony.com/doc/8.0/components/yaml.html#writing-yaml-files "Permalink to this headline")

The [dump()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Yaml.php#:~:text=function%20dump "Symfony\Component\Yaml\Yaml::dump()") method dumps any PHP array to its YAML representation:

If an error occurs during the dump, the parser throws a [DumpException](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Exception/DumpException.php "Symfony\Component\Yaml\Exception\DumpException") exception.

#### [Expanded and Inlined Arrays](https://symfony.com/doc/8.0/components/yaml.html#expanded-and-inlined-arrays "Permalink to this headline")

The YAML format supports two kind of representation for arrays, the expanded one, and the inline one. By default, the dumper uses the expanded representation:

The second argument of the [dump()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Yaml.php#:~:text=function%20dump "Symfony\Component\Yaml\Yaml::dump()") method customizes the level at which the output switches from the expanded representation to the inline one:

#### [Indentation](https://symfony.com/doc/8.0/components/yaml.html#indentation "Permalink to this headline")

By default, the YAML component will use 4 spaces for indentation. This can be changed using the third argument as follows:

#### [Numeric Literals](https://symfony.com/doc/8.0/components/yaml.html#numeric-literals "Permalink to this headline")

Long numeric literals, being integer, float or hexadecimal, are known for their poor readability in code and configuration files. That's why YAML files allow adding underscores to improve their readability:

During the parsing of the YAML contents, all the `_` characters are removed from the numeric literal contents, so there is not a limit in the number of underscores you can include or the way you group contents.

[Advanced Usage: Flags](https://symfony.com/doc/8.0/components/yaml.html#advanced-usage-flags "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

### [Object Parsing and Dumping](https://symfony.com/doc/8.0/components/yaml.html#object-parsing-and-dumping "Permalink to this headline")

You can dump objects by using the `DUMP_OBJECT` flag:

And parse them by using the `PARSE_OBJECT` flag:

The YAML component uses PHP's `serialize()` method to generate a string representation of the object.

Danger

Object serialization is specific to this implementation, other PHP YAML parsers will likely not recognize the `php/object` tag and non-PHP implementations certainly won't - use with discretion!

Danger

Parsing `!php/object` tags uses PHP deserialization internally. Never enable `PARSE_OBJECT` for untrusted YAML contents.

### [Parsing and Dumping Objects as Maps](https://symfony.com/doc/8.0/components/yaml.html#parsing-and-dumping-objects-as-maps "Permalink to this headline")

You can dump objects as Yaml maps by using the `DUMP_OBJECT_AS_MAP` flag:

And parse them by using the `PARSE_OBJECT_FOR_MAP` flag:

The YAML component uses PHP's `(array)` casting to generate a string representation of the object as a map.

### [Handling Invalid Types](https://symfony.com/doc/8.0/components/yaml.html#handling-invalid-types "Permalink to this headline")

By default, the parser will encode invalid types as `null`. You can make the parser throw exceptions by using the `PARSE_EXCEPTION_ON_INVALID_TYPE` flag:

Similarly you can use `DUMP_EXCEPTION_ON_INVALID_TYPE` when dumping:

### [Date Handling](https://symfony.com/doc/8.0/components/yaml.html#date-handling "Permalink to this headline")

By default, the YAML parser will convert unquoted strings which look like a date or a date-time into a Unix timestamp; for example `2016-05-27` or `2016-05-27T02:59:43.1Z` ([ISO-8601](https://www.iso.org/iso-8601-date-and-time-format.html)):

You can make it convert to a `DateTime` instance by using the `PARSE_DATETIME` flag:

### [Dumping Multi-line Literal Blocks](https://symfony.com/doc/8.0/components/yaml.html#dumping-multi-line-literal-blocks "Permalink to this headline")

In YAML, multiple lines can be represented as literal blocks. By default, the dumper will encode multiple lines as an inline string:

You can make it use a literal block with the `DUMP_MULTI_LINE_LITERAL_BLOCK` flag:

### [Parsing PHP Constants](https://symfony.com/doc/8.0/components/yaml.html#parsing-php-constants "Permalink to this headline")

By default, the YAML parser treats the PHP constants included in the contents as regular strings. Use the `PARSE_CONSTANT` flag and the special `!php/const` syntax to parse them as proper PHP constants:

Warning

Enabling `PARSE_CONSTANT` allows YAML contents to resolve arbitrary PHP constants and enum cases. Only enable it for trusted input.

### [Parsing PHP Enumerations](https://symfony.com/doc/8.0/components/yaml.html#parsing-php-enumerations "Permalink to this headline")

The YAML parser supports [PHP enumerations](https://www.php.net/manual/en/language.types.enumerations.php), both unit and backed enums. By default, they are parsed as regular strings. Use the `PARSE_CONSTANT` flag and the special `!php/enum` syntax to parse them as proper PHP enums:

You can also use `!php/enum` to get all the enumeration cases by only giving the enumeration FQCN:

### [Parsing and Dumping of Binary Data](https://symfony.com/doc/8.0/components/yaml.html#parsing-and-dumping-of-binary-data "Permalink to this headline")

Non UTF-8 encoded strings are dumped as base64 encoded data:

Binary data is automatically parsed if they include the `!!binary` YAML tag:

### [Parsing and Dumping Custom Tags](https://symfony.com/doc/8.0/components/yaml.html#parsing-and-dumping-custom-tags "Permalink to this headline")

In addition to the built-in support of tags like `!php/const` and `!!binary`, you can define your own custom YAML tags and parse them with the `PARSE_CUSTOM_TAGS` flag:

If the contents to dump contain [TaggedValue](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Tag/TaggedValue.php "Symfony\Component\Yaml\Tag\TaggedValue") objects, they are automatically transformed into YAML tags:

### [Dumping Null Values](https://symfony.com/doc/8.0/components/yaml.html#dumping-null-values "Permalink to this headline")

The official YAML specification uses both `null` and `~` to represent null values. This component uses `null` by default when dumping null values but you can dump them as `~` with the `DUMP_NULL_AS_TILDE` flag:

Another valid representation of the `null` value is an empty string. You can use the `DUMP_NULL_AS_EMPTY` flag to dump null values as empty strings:

### [Dumping Numeric Keys as Strings](https://symfony.com/doc/8.0/components/yaml.html#dumping-numeric-keys-as-strings "Permalink to this headline")

By default, digit-only array keys are dumped as integers. You can use the `DUMP_NUMERIC_KEY_AS_STRING` flag if you want to dump string-only keys:

### [Dumping Double Quotes on Values](https://symfony.com/doc/8.0/components/yaml.html#dumping-double-quotes-on-values "Permalink to this headline")

By default, only unsafe string values are enclosed in double quotes (for example, if they are reserved words or contain newlines and spaces). Use the `DUMP_FORCE_DOUBLE_QUOTES_ON_VALUES` flag to add double quotes to all string values:

### [Dumping Collection of Maps](https://symfony.com/doc/8.0/components/yaml.html#dumping-collection-of-maps "Permalink to this headline")

When the YAML component dumps collections of maps, it uses a hyphen on a separate line as a delimiter:

To produce a more compact output where the delimiter is included within the map, use the `Yaml::DUMP_COMPACT_NESTED_MAPPING` flag:

### [Syntax Validation](https://symfony.com/doc/8.0/components/yaml.html#syntax-validation "Permalink to this headline")

The syntax of YAML contents can be validated through the CLI using the [LintCommand](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Yaml/Command/LintCommand.php "Symfony\Component\Yaml\Command\LintCommand") command.

First, install the Console component:

Create a console application with `lint:yaml` as its only command:

Then, execute the script for validating contents:

The result is written to STDOUT and uses a plain text format by default. Add the `--format` option to get the output in JSON format:

Tip

The linting command will also report any deprecations in the checked YAML files. This may for example be useful for recognizing deprecations of contents of YAML files during automated tests.

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
