# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html

Title: String Encoding Utilities - kombu.utils.encoding — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.encoding.html).

Text encoding utilities.

Utilities to encode text, and to safely emit text from running applications without crashing from the infamous [`UnicodeDecodeError`](https://docs.python.org/dev/library/exceptions.html#UnicodeDecodeError "(in Python v3.15)") exception.

kombu.utils.encoding.bytes_to_str(_s_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#bytes_to_str)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.bytes_to_str "Link to this definition")
Convert bytes to str.

kombu.utils.encoding.default_encode(_obj_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#default_encode)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.default_encode "Link to this definition")
Encode using default encoding.

kombu.utils.encoding.default_encoding(_file=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#default_encoding)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.default_encoding "Link to this definition")
Get default encoding.

kombu.utils.encoding.default_encoding_file _=None_[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.default_encoding_file "Link to this definition")
safe_str takes encoding from this file by default. [`set_default_encoding_file()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.set_default_encoding_file "kombu.utils.encoding.set_default_encoding_file") can used to set the default output file.

kombu.utils.encoding.ensure_bytes(_s_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#ensure_bytes)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.ensure_bytes "Link to this definition")
Ensure s is bytes, not str.

kombu.utils.encoding.from_utf8(_s_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#from_utf8)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.from_utf8 "Link to this definition")
Get str from utf-8 encoding.

kombu.utils.encoding.get_default_encoding_file()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#get_default_encoding_file)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.get_default_encoding_file "Link to this definition")
Get file used to get codec information.

kombu.utils.encoding.safe_repr(_o_, _errors='replace'_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#safe_repr)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.safe_repr "Link to this definition")
Safe form of repr, void of Unicode errors.

kombu.utils.encoding.safe_str(_s_, _errors='replace'_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#safe_str)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.safe_str "Link to this definition")
Safe form of str(), void of unicode errors.

kombu.utils.encoding.set_default_encoding_file(_file_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#set_default_encoding_file)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.set_default_encoding_file "Link to this definition")
Set file used to get codec information.

kombu.utils.encoding.str_to_bytes(_s_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/encoding.html#str_to_bytes)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.encoding.html#kombu.utils.encoding.str_to_bytes "Link to this definition")
Convert str to bytes.
