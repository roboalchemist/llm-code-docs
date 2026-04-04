# Source: https://docs.rs/tower-http/latest/tower_http/body/

[tower_http](../index.html)
# Module body Copy item path

[Source](../../src/tower_http/body.rs.html#1-121)
Available on
**crate features catch-panic or decompression-br or decompression-deflate or decompression-gzip or decompression-zstd or fs or limit**
only.
Expand description
Body types.

All these are wrappers around other body types. You shouldn’t have to use them in your code.
Use http-body-util instead.

They exist because we don’t want to expose types from http-body-util in tower-https public
API.

## Structs§

[Full](struct.Full.html)
[Limited](struct.Limited.html)
[UnsyncBoxBody](struct.UnsyncBoxBody.html)