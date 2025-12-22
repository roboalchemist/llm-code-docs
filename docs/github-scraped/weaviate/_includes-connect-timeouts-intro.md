# Source: https://github.com/weaviate/docs/blob/main/_includes/connect/timeouts-intro.mdx

The Python client v4 and TypeScript client v3 use [gRPC](/weaviate/api/grpc). The gRPC protocol is sensitive to network delay. If you encounter connection timeouts, adjust the timeout values for initialization, queries, and insertions.