# http Package Documentation (Deprecated)

**Source:** [pkg.go.dev/github.com/stretchr/testify/http](https://pkg.go.dev/github.com/stretchr/testify/http)

- **Version:** v1.11.1
- **License:** MIT

## Deprecation Notice

**Deprecated: Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.**

This entire package is deprecated. The Go standard library's `net/http/httptest` package provides superior testing utilities.

## Types

### TestResponseWriter

```go
type TestResponseWriter struct {
	// StatusCode is the last int written by the call to WriteHeader(int)
	StatusCode int

	// Output is a string containing the written bytes using the Write([]byte) func.
	Output string
	// contains filtered or unexported fields
}
```

**Deprecated:** Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.

#### (*TestResponseWriter) Header

```go
func (rw *TestResponseWriter) Header() http.Header
```

**Deprecated:** Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.

#### (*TestResponseWriter) Write

```go
func (rw *TestResponseWriter) Write(bytes []byte) (int, error)
```

**Deprecated:** Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.

#### (*TestResponseWriter) WriteHeader

```go
func (rw *TestResponseWriter) WriteHeader(i int)
```

**Deprecated:** Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.

### TestRoundTripper

```go
type TestRoundTripper struct {
	mock.Mock
}
```

**Deprecated:** Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.

#### (*TestRoundTripper) RoundTrip

```go
func (t *TestRoundTripper) RoundTrip(req *http.Request) (*http.Response, error)
```

**Deprecated:** Use [net/http/httptest](https://pkg.go.dev/net/http/httptest) instead.

## Source Files

- [doc.go](https://github.com/stretchr/testify/blob/v1.11.1/http/doc.go)
- [test_response_writer.go](https://github.com/stretchr/testify/blob/v1.11.1/http/test_response_writer.go)
- [test_round_tripper.go](https://github.com/stretchr/testify/blob/v1.11.1/http/test_round_tripper.go)
