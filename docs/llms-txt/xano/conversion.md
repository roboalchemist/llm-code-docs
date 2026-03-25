# Source: https://docs.xano.com/the-function-stack/filters/conversion.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversion

* [**base64\_decode**](/the-function-stack/filters/conversion#base64_decode) - Decodes the value represented as base64 and returns the result.
* [**base64\_decode\_urlsafe**](/the-function-stack/filters/conversion#base64_decode_urlsafe) - Decodes the value represented as base64 URL safe text and returns the result.
* [**base64\_encode**](/the-function-stack/filters/conversion#base64_encode) - Encodes the value and returns the result as base64 text.
* [**base64\_encode\_urlsafe**](/the-function-stack/filters/conversion#base64_encode_urlsafe) - Encodes the value and returns the result as base64 URL safe text.
* [**base\_convert**](/the-function-stack/filters/conversion#base_convert) - Converts a value between two bases\*.\*
* [**bin2hex**](/the-function-stack/filters/conversion#bin2hex) - Converts a binary value into its hex equivalent.
* [**decbin**](/the-function-stack/filters/conversion#decbin) - Converts a decimal value into its binary string (i.e. 01010) equivalent.
* [**bindec**](/the-function-stack/filters/conversion#bindec) - Converts a binary string (i.e. 01010) into its decimal equivalent.
* [**create\_object**](/the-function-stack/filters/conversion#create_object) - Creates an object based on a list of keys and a list of values.
* [**csv\_decode**](/the-function-stack/filters/conversion#csv_decode) - Decodes the value represented as CSV and returns the result
* [**csv\_encode**](/the-function-stack/filters/conversion#csv_encode) - Encodes the value and returns the result in CSV-formatted text
* [**dechex**](/the-function-stack/filters/conversion#dechex) - Converts a decimal value into its hex equivalent.
* [**decoct**](/the-function-stack/filters/conversion#decoct) - Converts a decimal value into its octal equivalent.
* [**hex2bin**](/the-function-stack/filters/conversion#hex2bin) - Converts a hex value into its binary equivalent.
* [**hexdec**](/the-function-stack/filters/conversion#hexdec) - Converts a hex value into its decimal equivalent.
* [**json\_decode**](/the-function-stack/filters/conversion#json_decode) - Decodes the value represented as json and returns the result.
* [**json\_encode**](/the-function-stack/filters/conversion#json_encode) - Encodes the value and returns the result as json text.
* [**octdec**](/the-function-stack/filters/conversion#octdec) - Converts an octal value into its decimal equivalent.
* [**to\_bool**](/the-function-stack/filters/conversion#to_bool) - Converts text, integer, or decimal types to a bool and returns the result.
* [**to\_dec**](/the-function-stack/filters/conversion#to_decimal) - Converts text, integer, or bool types to a decimal and returns the result.
* [**to\_int**](/the-function-stack/filters/conversion#to_int) - Converts text, integer, or bool types to an integer and returns the result.
* [**to\_text**](/the-function-stack/filters/conversion#to_text) - Converts text, integer, or bool types to text and returns the result.
* [**to\_timestamp**](/the-function-stack/filters/conversion#to_timestamp) - Converts a text expression (now, next Friday) to timestamp comparable format.
* [**url\_decode**](/the-function-stack/filters/conversion#url_decode) - Decodes the value represented as a URL encoded value.
* [**url\_decode\_rfc3986**](/the-function-stack/filters/conversion#url_decode_rfc3986) - Decodes the value represented as a URL encoded value conforming to RFC3986 specifications
* [**url\_encode**](/the-function-stack/filters/conversion#url_encode) - Encodes the value and returns the result as a URL encoded value.
* [**url\_encode\_rfc3986**](/the-function-stack/filters/conversion#url_encode_rfc3986) - Encodes the value and returns the result as a URL encoded value conforming to RFC3986 specifications
* [**yaml\_decode**](/the-function-stack/filters/conversion#yaml_decode) - Decodes the value represented as yaml and returns the result.
* [**yaml\_encode**](/the-function-stack/filters/conversion#yaml_encode) - Encodes the value and returns the result as yaml text.
* [**xml\_decode**](/the-function-stack/filters/conversion#xml_decode) - Decodes the value represented as XML to JSON and returns the result

#### **base64\_decode**:

Decodes the value represented as base64 and returns the result.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/dC3SQWgPCF_-1qn6/images/2f3f1c16-spaces2F2tWsL4o1vHmDGb2UAUDD2Fuploads2FLO1zKfn3CaROglUk1L6a2Fdecode.png?fit=max&auto=format&n=dC3SQWgPCF_-1qn6&q=85&s=9b4a6d65773a54856fddadf857d9a468" data-path="images/2f3f1c16-spaces2F2tWsL4o1vHmDGb2UAUDD2Fuploads2FLO1zKfn3CaROglUk1L6a2Fdecode.png" />
</Frame>

Example: we have a text value of aGVsbG8gd29ybGQ= using the filter base64\_decode we get hello world.

#### **base64\_decode\_urlsafe:**

Decodes the value represented as base64 URL safe text and returns the result.

This filter transforms the base64 URL safe encoded characters `-_.` back to `+/=`.

#### **base64\_encode**:

Encodes the value and returns the result as base64 text.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/23c4f638-spaces2F2tWsL4o1vHmDGb2UAUDD2Fuploads2FbJR8UvOe5hCINYUKWWen2Fencode.png?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=996bfe8c0e92f5feb8ed38e185337870" data-path="images/23c4f638-spaces2F2tWsL4o1vHmDGb2UAUDD2Fuploads2FbJR8UvOe5hCINYUKWWen2Fencode.png" />
</Frame>

Example: we have a text value of hello world using the filter base64\_encode we get aGVsbG8gd29ybGQ= .

#### base64\_encode\_urlsafe:

Encodes the value and returns the result as base64 URL safe text.

In base64 encoding, a URL safe format is not taken into consideration but there's only three characters we need to be cautious of `+/=`. With this filter those characters become `-_.` respectively.

#### base\_convert:

Converts a value between two bases\*.\*

* **frombase**: Specifies the original base of number. Has to be between 2 and 36, inclusive. Digits in numbers with a base higher than 10 will be represented with the letters a-z, with a meaning 10, b meaning 11 and z meaning 35

* **tobase**: Specifies the base to convert to. Has to be between 2 and 36, inclusive. Digits in numbers with a base higher than 10 will be represented with the letters a-z, with a meaning 10, b meaning 11 and z meaning 35

In this example we are converting a hexadecimal number to an octal number:

#### bin2hex:

Converts a binary value into its hex equivalent.

#### decbin:

Converts a decimal value into its binary string (i.e. 01010) equivalent.

#### bindec:

Converts a binary string (i.e. 01010) into its decimal equivalent.

#### create\_object:

Creates an object based on a list of keys and a list of values.

<Frame caption="Keys list is [first_name, company, position]. Values list is [Michael, Xano, Customer Success Lead].">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/e4f0f076-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=9b5ba6ffc781681323f7c7e61dd22e7d" width="599" height="569" data-path="images/e4f0f076-image.jpeg" />
</Frame>

Resulting in a created object:

<Frame caption="The lists of keys and values are combined to create an object.">
  <img src="https://mintcdn.com/xano-997cb9ee/Zmn_DUDgqMkazo6J/images/ea73c632-image.jpeg?fit=max&auto=format&n=Zmn_DUDgqMkazo6J&q=85&s=a82cbdf2639e137e1374ca8b25bbf5cc" width="586" height="284" data-path="images/ea73c632-image.jpeg" />
</Frame>

#### **csv\_decode:**

Decodes the value represented in the CSV format and returns the result.

* **separator** - the field delimiter, one character only (usually a comma)
* **enclosure** - the field enclosure, one character only (usually a quotation mark)
* **escape** - the escape character that allows the enclosure character to be used within a field

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1b745d43-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=671b9e0ed5bf5720415f0b61d86e5867" width="1182" height="468" data-path="images/1b745d43-image.jpeg" />
</Frame>

#### **csv\_encode:**

Encodes the value and returns the result in CSV format

* **separator** - the field delimiter, one character only (usually a comma)
* **enclosure** - the field enclosure, one character only (usually a quotation mark)
* **escape** - the escape character that allows the enclosure character to be used within a field

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0e76163b-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=3b6c55cc440575c0813972eb181415f2" width="2097" height="867" data-path="images/0e76163b-image.jpeg" />
</Frame>

#### **dechex**:

Converts a decimal value into its hex equivalent.

#### decoct:

Converts a decimal value into its octal equivalent.

#### hex2bin:

Converts a hex value into its binary equivalent.

#### hexdec:

Converts a hex value into its decimal equivalent.

#### json\_decode:

Decodes the value represented as json and returns the result. We will decode the json from the json\_encode filter example.

#### json\_encode:

Encodes the value and returns the result as json text. The variable object is: \{ "a":"3", "b":"2", "c":"1" }.

#### octdec:

Converts an octal value into its decimal equivalent.

#### to\_bool:

Converts text, integer, or decimal types to a bool and returns the result. The different conversions that are possible with this filter are: Converting a text/integer/decimal value of 0 to false. Converting a text/integer/decimal value of 1 to true. Converting a text value of "true" to true. Converting a text value of "false" to false.

#### to\_decimal:

Converts text, integer, or bool types to a decimal and returns the result.

#### to\_int:

Converts text, decimal, or bool types to an integer and returns the result.

#### to\_text:

Converts text, decimal, or bool types to text and returns the result.

#### to\_timestamp:

Converts a text expression (now, next Friday) to timestamp comparable format.

#### url\_decode:

Decodes the value represented as a URL encoded value.

#### url\_decode\_rfc3986

Similar to url\_decode, this decodes the value represented as a URL encoded value, but conforming to [rfc3986](https://datatracker.ietf.org/doc/html/rfc3986) standards.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/nsvdyKK4Dg7VUAZs/images/96175166-image.jpeg?fit=max&auto=format&n=nsvdyKK4Dg7VUAZs&q=85&s=aaf0c1a8f33f4dcbeb36174346aaebe6" width="1171" height="341" data-path="images/96175166-image.jpeg" />
</Frame>

#### url\_encode:

Encodes the value and returns the result as a URL encoded value.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/WBQXG-4Ngk82eYAW/images/fbddaace-spaces2F2tWsL4o1vHmDGb2UAUDD2Fuploads2FP5Zgk05JK2rZUlX20TGA2Furlencode.png?fit=max&auto=format&n=WBQXG-4Ngk82eYAW&q=85&s=ea2b7d3a37f03097cdc2fef1ec7c0c93" data-path="images/fbddaace-spaces2F2tWsL4o1vHmDGb2UAUDD2Fuploads2FP5Zgk05JK2rZUlX20TGA2Furlencode.png" />
</Frame>

Example: we have a text value then use the url\_encode filter to change it to Hello+World+%26+Xano.

#### url\_encode\_rfc3986

Similar to url\_encode, this encodes the value and returns the result as a URL encoded value, but conforming to [rfc3986](https://datatracker.ietf.org/doc/html/rfc3986) standards.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/0de6513f-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=1beb69f7542b440e82f76eb6a080abd5" width="1185" height="403" data-path="images/0de6513f-image.jpeg" />
</Frame>

#### yaml\_decode:

Decodes the value represented as yaml and returns the result. For this example, we will use the example from yaml encode and then decode the variable. The variable gets changed into:

```json  theme={null}
{
  "name": "John",
  "age": 30,
  "car": "ford"
}
```

<Frame>
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/xano-997cb9ee/images/04b9f193-file-error.html" />
</Frame>

#### yaml\_encode:

Encodes the value and returns the result as yaml text.

#### xml\_decode:

Decodes the provided data as XML, to JSON, and returns the result.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f0dcf815-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=532faf5d60bcaa2ea6bd3711abadf873" width="1032" height="1322" data-path="images/f0dcf815-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).