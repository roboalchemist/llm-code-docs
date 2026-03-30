# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html

Title: kombu.compression — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.compression.html).

Compression utilities.

*   [Encoding/decoding](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#encoding-decoding)

*   [Registry](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#registry)

[Encoding/decoding](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#id3)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#encoding-decoding "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

kombu.compression.compress(_body_, _content\_type_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compression.html#compress)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#kombu.compression.compress "Link to this definition")
Compress text.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#arguments "Link to this heading")

> body (AnyStr): The text to compress. content_type (str): mime-type of compression method to use.

kombu.compression.decompress(_body_, _content\_type_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compression.html#decompress)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#kombu.compression.decompress "Link to this definition")
Decompress compressed text.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#id1 "Link to this heading")

> body (AnyStr): Previously compressed text to uncompress. content_type (str): mime-type of compression method used.

[Registry](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#id4)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#registry "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

kombu.compression.encoders()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compression.html#encoders)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#kombu.compression.encoders "Link to this definition")
Return a list of available compression methods.

kombu.compression.get_encoder(_t_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compression.html#get_encoder)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#kombu.compression.get_encoder "Link to this definition")
Get encoder by alias name.

kombu.compression.get_decoder(_t_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compression.html#get_decoder)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#kombu.compression.get_decoder "Link to this definition")
Get decoder by alias name.

kombu.compression.register(_encoder_, _decoder_, _content\_type_, _aliases=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/compression.html#register)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#kombu.compression.register "Link to this definition")
Register new compression method.

### Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.compression.html#id2 "Link to this heading")

> encoder (Callable): Function used to compress text. decoder (Callable): Function used to decompress previously
> 
> 
> > compressed text.
> 
> content_type (str): The mime type this compression method
> identifies as.
> 
> aliases (Sequence[str]): A list of names to associate with
> this compression method.
