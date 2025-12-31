# Source: https://ast-grep.github.io/catalog/go.md

---
url: /catalog/go.md
---
# Go

This page curates a list of example ast-grep rules to check and to rewrite Go code.

## Detect problematic defer statements with function calls

* [Playground Link](/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoiZ28iLCJxdWVyeSI6InsgXG4gICAgZGVmZXIgJEEuJEIodCwgZmFpbHBvaW50LiRNKCQkJCkpIFxufSIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoic21hcnQiLCJzZWxlY3RvciI6ImRlZmVyX3N0YXRlbWVudCIsImNvbmZpZyI6InJ1bGU6XG4iLCJzb3VyY2UiOiJmdW5jIFRlc3RJc3N1ZTE2Njk2KHQgKnRlc3RpbmcuVCkge1xuXHRhbGFybVJhdGlvIDo9IHZhcmRlZi5NZW1vcnlVc2FnZUFsYXJtUmF0aW8uTG9hZCgpXG5cdHZhcmRlZi5NZW1vcnlVc2FnZUFsYXJtUmF0aW8uU3RvcmUoMC4wKVxuXHRkZWZlciB2YXJkZWYuTWVtb3J5VXNhZ2VBbGFybVJhdGlvLlN0b3JlKGFsYXJtUmF0aW8pXG5cdHJlcXVpcmUuTm9FcnJvcih0LCBmYWlscG9pbnQuRW5hYmxlKFwiZ2l0aHViLmNvbS9waW5nY2FwL3RpZGIvcGtnL2V4ZWN1dG9yL3NvcnRleGVjL3Rlc3RTb3J0ZWRSb3dDb250YWluZXJTcGlsbFwiLCBcInJldHVybih0cnVlKVwiKSlcblx0ZGVmZXIgcmVxdWlyZS5Ob0Vycm9yKHQsIFxuXHQgICBmYWlscG9pbnQuRGlzYWJsZShcblx0XHRcImdpdGh1Yi5jb20vcGluZ2NhcC90aWRiL3BrZy9leGVjdXRvci9zb3J0ZXhlYy90ZXN0U29ydGVkUm93Q29udGFpbmVyU3BpbGxcIlxuXHQpKVxuXHRyZXF1aXJlLk5vRXJyb3IodCwgXG5cdFx0ZmFpbHBvaW50LkVuYWJsZShcImdpdGh1Yi5jb20vcGluZ2NhcC90aWRiL3BrZy9leGVjdXRvci9qb2luL3Rlc3RSb3dDb250YWluZXJTcGlsbFwiLCBcInJldHVybih0cnVlKVwiKSlcblx0ZGVmZXIgcmVxdWlyZS5Ob0Vycm9yKHQsIFxuXHRcdGZhaWxwb2ludC5EaXNhYmxlKFwiZ2l0aHViLmNvbS9waW5nY2FwL3RpZGIvcGtnL2V4ZWN1dG9yL2pvaW4vdGVzdFJvd0NvbnRhaW5lclNwaWxsXCIpKVxufSJ9)

### Description

This rule detects a common anti-pattern in Go testing code where `defer` statements contain function calls with parameters that are evaluated immediately instead of when the defer executes.

In Go, `defer` schedules a function call to be executed when the surrounding function returns. However, the **arguments to the deferred function are evaluated immediately** when the defer statement is encountered, not when the defer executes.

This is particularly problematic when using assertion libraries in tests. For example:

```go
defer require.NoError(t, failpoint.Disable("some/path"))
```

In this case, `failpoint.Disable("some/path")` is called immediately when the defer statement is reached, not when the function exits. This means the failpoint is disabled right after being enabled, making the test ineffective.

### Pattern

```shell
ast-grep \
  --lang go \
  --pattern '{ defer $A.$B(t, failpoint.$M($$$)) } \
  --selector defer_statement'
```

### Example

```go{6-9,11-12}
func TestIssue16696(t *testing.T) {
	alarmRatio := vardef.MemoryUsageAlarmRatio.Load()
	vardef.MemoryUsageAlarmRatio.Store(0.0)
	defer vardef.MemoryUsageAlarmRatio.Store(alarmRatio)
	require.NoError(t, failpoint.Enable("github.com/pingcap/tidb/pkg/executor/sortexec/testSortedRowContainerSpill", "return(true)"))
	defer require.NoError(t,
	   failpoint.Disable(
		"github.com/pingcap/tidb/pkg/executor/sortexec/testSortedRowContainerSpill"
	))
	require.NoError(t, failpoint.Enable("github.com/pingcap/tidb/pkg/executor/join/testRowContainerSpill", "return(true)"))
	defer require.NoError(t,
		failpoint.Disable("github.com/pingcap/tidb/pkg/executor/join/testRowContainerSpill"))
}
```

### Fix

The correct way to defer a function with parameters is to wrap it in an anonymous function:

```go
defer func() {
    require.NoError(t, failpoint.Disable("some/path"))
}()
```

### Contributed by

Inspired by [YangKeao's tweet](https://x.com/YangKeao/status/1671420857565212672) about this common pitfall in TiDB codebase.

## Find function declarations with names of certain pattern

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImdvIiwicXVlcnkiOiJyJ15bQS1aYS16MC05Xy1dKyciLCJyZXdyaXRlIjoiIiwiY29uZmlnIjoiaWQ6IHRlc3QtZnVuY3Rpb25zXG5sYW5ndWFnZTogZ29cbnJ1bGU6XG4gIGtpbmQ6IGZ1bmN0aW9uX2RlY2xhcmF0aW9uXG4gIGhhczpcbiAgICBmaWVsZDogbmFtZVxuICAgIHJlZ2V4OiBUZXN0LipcbiIsInNvdXJjZSI6InBhY2thZ2UgYWJzXG5pbXBvcnQgXCJ0ZXN0aW5nXCJcbmZ1bmMgVGVzdEFicyh0ICp0ZXN0aW5nLlQpIHtcbiAgICBnb3QgOj0gQWJzKC0xKVxuICAgIGlmIGdvdCAhPSAxIHtcbiAgICAgICAgdC5FcnJvcmYoXCJBYnMoLTEpID0gJWQ7IHdhbnQgMVwiLCBnb3QpXG4gICAgfVxufVxuIn0=)

### Description

ast-grep can find function declarations by their names. But not all names can be matched by a meta variable pattern. For instance, you cannot use a meta variable pattern to find function declarations whose names start with a specific prefix, e.g. `TestAbs` with the prefix `Test`. Attempting `Test$_` will fail because it is not a valid syntax.

Instead, you can use a [YAML rule](/reference/rule.html) to use the [`regex`](/guide/rule-config/atomic-rule.html#regex) atomic rule.

### YAML

```yaml
id: test-functions
language: go
rule:
  kind: function_declaration
  has:
    field: name
    regex: Test.*
```

### Example

```go{3-8}
package abs
import "testing"
func TestAbs(t *testing.T) {
    got := Abs(-1)
    if got != 1 {
        t.Errorf("Abs(-1) = %d; want 1", got)
    }
}
```

### Contributed by

[kevinkjt2000](https://twitter.com/kevinkjt2000) on [Discord](https://discord.com/invite/4YZjf6htSQ).

## Match Function Call in Golang

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImdvIiwicXVlcnkiOiJhd2FpdCAkQSIsInJld3JpdGUiOiJ0cnkge1xuICAgIGF3YWl0ICRBXG59IGNhdGNoKGUpIHtcbiAgICAvLyB0b2RvXG59IiwiY29uZmlnIjoicnVsZTpcbiAgcGF0dGVybjpcbiAgICBjb250ZXh0OiAnZnVuYyB0KCkgeyBmbXQuUHJpbnRsbigkJCRBKSB9J1xuICAgIHNlbGVjdG9yOiBjYWxsX2V4cHJlc3Npb25cbiIsInNvdXJjZSI6ImZ1bmMgbWFpbigpIHtcbiAgICBmbXQuUHJpbnRsbihcIk9LXCIpXG59In0=)

### Description

One of the common questions of ast-grep is to match function calls in Golang.

A plain pattern like `fmt.Println($A)` will not work. This is because Golang syntax also allows type conversions, e.g. `int(3.14)`, that look like function calls. Tree-sitter, ast-grep's parser, will prefer parsing `func_call(arg)` as a type conversion instead of a call expression.

To avoid this ambiguity, ast-grep lets us write a [contextual pattern](/guide/rule-config/atomic-rule.html#pattern), which is a pattern inside a larger code snippet.
We can use `context` to write a pattern like this: `func t() { fmt.Println($A) }`. Then, we can use the selector `call_expression` to match only function calls.

Please also read the [deep dive](/advanced/pattern-parse.html) on [ambiguous pattern](/advanced/pattern-parse.html#ambiguous-pattern-code).

### YAML

```yaml
id: match-function-call
language: go
rule:
  pattern:
    context: 'func t() { fmt.Println($A) }'
    selector: call_expression
```

### Example

```go{2}
func main() {
    fmt.Println("OK")
}
```

### Contributed by

Inspired by [QuantumGhost](https://github.com/QuantumGhost) from [ast-grep/ast-grep#646](https://github.com/ast-grep/ast-grep/issues/646)

## Match package import in Golang

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImdvIiwicXVlcnkiOiIiLCJyZXdyaXRlIjoiIiwic3RyaWN0bmVzcyI6InNtYXJ0Iiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogbWF0Y2gtcGFja2FnZS1pbXBvcnRcbmxhbmd1YWdlOiBnb1xucnVsZTpcbiAga2luZDogaW1wb3J0X3NwZWNcbiAgaGFzOlxuICAgIHJlZ2V4OiBnaXRodWIuY29tL2dvbGFuZy1qd3Qvand0Iiwic291cmNlIjoicGFja2FnZSBtYWluXG5cbmltcG9ydCAoXG5cdFwiZm10XCJcblx0XCJnaXRodWIuY29tL2dvbGFuZy1qd3Qvand0XCIgIC8vIFRoaXMgbWF0Y2hlcyB0aGUgQVNUIHJ1bGVcbilcblxuZnVuYyBtYWluKCkge1xuXHQvLyBDcmVhdGUgYSBuZXcgdG9rZW5cblx0dG9rZW4gOj0gand0Lk5ldyhqd3QuU2lnbmluZ01ldGhvZEhTMjU2KVxuXHRcblx0Ly8gQWRkIHNvbWUgY2xhaW1zXG5cdHRva2VuLkNsYWltcyA9IGp3dC5NYXBDbGFpbXN7XG5cdFx0XCJ1c2VyXCI6IFwiYWxpY2VcIixcblx0XHRcInJvbGVcIjogXCJhZG1pblwiLFxuXHR9XG5cdFxuXHQvLyBTaWduIHRoZSB0b2tlblxuXHR0b2tlblN0cmluZywgZXJyIDo9IHRva2VuLlNpZ25lZFN0cmluZyhbXWJ5dGUoXCJteS1zZWNyZXRcIikpXG5cdGlmIGVyciAhPSBuaWwge1xuXHRcdGZtdC5QcmludGYoXCJFcnJvciBzaWduaW5nIHRva2VuOiAldlxcblwiLCBlcnIpXG5cdFx0cmV0dXJuXG5cdH1cblx0XG5cdGZtdC5QcmludGYoXCJHZW5lcmF0ZWQgdG9rZW46ICVzXFxuXCIsIHRva2VuU3RyaW5nKVxufSJ9)

### Description

A generic rule template for detecting imports of specific packages in Go source code. This rule can be customized to match any package by modifying the regex pattern, making it useful for security auditing, dependency management, and compliance checking.

This rule identifies Go import statements based on the configured regex pattern, including:

Direct imports: `import "package/name"`\
Versioned imports: `import "package/name/v4"`\
Subpackage imports: `import "package/name/subpkg"`\
Grouped imports within `import () blocks`

### YAML

```yaml
id: match-package-import
language: go
rule:
  kind: import_spec
  has:
    regex: PACKAGE_PATTERN_HERE
```

### Example

JWT Library Detection

```go{5}
package main

import (
	"fmt"
	"github.com/golang-jwt/jwt" // This matches the AST rule
)

func main() {
	token := jwt.New(jwt.SigningMethodHS256) // Create a new token
	// Add some claims
	token.Claims = jwt.MapClaims{"user": "alice", "role": "admin"}
	tokenString, err := token.SignedString([]byte("my-secret")) // Sign the token
	if err != nil {
		fmt.Printf("Error signing token: %v\n", err)
		return
	}
	fmt.Printf("Generated token: %s\n", tokenString)
}
```

### Contributed by

[Sudesh Gutta](https://github.com/sudeshgutta)

## Detect problematic JSON tags with dash prefix

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImdvIiwicXVlcnkiOiJgJFRBR2AiLCJyZXdyaXRlIjoiIiwic3RyaWN0bmVzcyI6InNtYXJ0Iiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogdW5tYXJzaGFsLXRhZy1pcy1kYXNoXG5zZXZlcml0eTogZXJyb3Jcbm1lc3NhZ2U6IFN0cnVjdCBmaWVsZCBjYW4gYmUgZGVjb2RlZCB3aXRoIHRoZSBgLWAga2V5IGJlY2F1c2UgdGhlIEpTT04gdGFnXG4gIHN0YXJ0cyB3aXRoIGEgYC1gIGJ1dCBpcyBmb2xsb3dlZCBieSBhIGNvbW1hLlxucnVsZTpcbiAgcGF0dGVybjogJ2AkVEFHYCdcbiAgaW5zaWRlOlxuICAgIGtpbmQ6IGZpZWxkX2RlY2xhcmF0aW9uXG5jb25zdHJhaW50czpcbiAgVEFHOiBcbiAgICByZWdleDoganNvbjpcIi0sLipcIiIsInNvdXJjZSI6InBhY2thZ2UgbWFpblxuXG50eXBlIFRlc3RTdHJ1Y3QxIHN0cnVjdCB7XG5cdC8vIG9rOiB1bm1hcnNoYWwtdGFnLWlzLWRhc2hcblx0QSBzdHJpbmcgYGpzb246XCJpZFwiYFxufVxuXG50eXBlIFRlc3RTdHJ1Y3QyIHN0cnVjdCB7XG5cdC8vIHJ1bGVpZDogdW5tYXJzaGFsLXRhZy1pcy1kYXNoXG5cdEIgc3RyaW5nIGBqc29uOlwiLSxvbWl0ZW1wdHlcImBcbn1cblxudHlwZSBUZXN0U3RydWN0MyBzdHJ1Y3Qge1xuXHQvLyBydWxlaWQ6IHVubWFyc2hhbC10YWctaXMtZGFzaFxuXHRDIHN0cmluZyBganNvbjpcIi0sMTIzXCJgXG59XG5cbnR5cGUgVGVzdFN0cnVjdDQgc3RydWN0IHtcblx0Ly8gcnVsZWlkOiB1bm1hcnNoYWwtdGFnLWlzLWRhc2hcblx0RCBzdHJpbmcgYGpzb246XCItLFwiYFxufSJ9)

### Description

This rule detects a security vulnerability in Go's JSON unmarshaling. When a struct field has a JSON tag that starts with `-,`, it can be unexpectedly unmarshaled with the `-` key.

According to the [Go documentation](https://pkg.go.dev/encoding/json#Marshal), if the field tag is `-`, the field should be omitted. However, a field with name `-` can still be unmarshaled using the tag `-,`.

This creates a security issue where developers think they are preventing a field from being unmarshaled (like `IsAdmin` in authentication), but attackers can still set that field by providing the `-` key in JSON input.

```go
type User struct {
    Username string `json:"username,omitempty"`
    Password string `json:"password,omitempty"`
    IsAdmin  bool   `json:"-,omitempty"`  // Intended to prevent marshaling
}

// This still works and sets IsAdmin to true!
json.Unmarshal([]byte(`{"-": true}`), &user)
// Result: main.User{Username:"", Password:"", IsAdmin:true}
```

### YAML

```yaml
id: unmarshal-tag-is-dash
severity: error
message: Struct field can be decoded with the `-` key because the JSON tag
  starts with a `-` but is followed by a comma.
rule:
  pattern: '`$TAG`'
  inside:
    kind: field_declaration
constraints:
  TAG:
    regex: json:"-,.*"
```

### Example

```go{8,12,16}
package main

type TestStruct1 struct {
	A string `json:"id"` // ok
}

type TestStruct2 struct {
	B string `json:"-,omitempty"` // wrong
}

type TestStruct3 struct {
	C string `json:"-,123"` // wrong
}

type TestStruct4 struct {
	D string `json:"-,"` // wrong
}
```

### Fix

To properly omit a field from JSON marshaling/unmarshaling, use just `-` without a comma:

```go
type User struct {
    Username string `json:"username,omitempty"`
    Password string `json:"password,omitempty"`
    IsAdmin  bool   `json:"-"`  // Correctly prevents marshaling/unmarshaling
}
```

### Contributed by

Inspired by [Trail of Bits blog post](https://blog.trailofbits.com/2025/06/17/unexpected-security-footguns-in-gos-parsers/) and their [public Semgrep rule](https://semgrep.dev/playground/r/trailofbits.go.unmarshal-tag-is-dash).
