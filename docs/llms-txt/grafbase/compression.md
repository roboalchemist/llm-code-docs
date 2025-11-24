# Source: https://grafbase.com/docs/gateway/performance/compression.md

# Compression

Grafbase Gateway supports compression for:

- the body of responses from the Gateway (using the standard `Accept-Encoding` header)
- the body of responses from subgraphs for requests issued by the Gateway (using the standard `Accept-Encoding` header)

All the common compression algorithms are supported: gzip, deflate, br (brotli) and zstd.