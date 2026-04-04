# runtime/pprof API Reference

Source: https://pkg.go.dev/runtime/pprof

## Package Overview

Package `pprof` writes runtime profiling data in the format expected by the pprof visualization tool. It enables CPU profiling, memory profiling, and custom profiling through stack traces.

## CPU Profiling Functions

### StartCPUProfile

```go
func StartCPUProfile(w io.Writer) error
```

Enables CPU profiling, buffering profile output to the provided writer. Only one profile can be active at a time. Returns an error if profiling is already enabled.

**Parameters:**
- `w io.Writer` - Writer to buffer CPU profile output

**Returns:**
- Error if profiling is already enabled; nil on success

**Example:**
```go
f, err := os.Create("cpu.prof")
if err != nil {
	log.Fatal(err)
}
defer f.Close()

if err := pprof.StartCPUProfile(f); err != nil {
	log.Fatal("could not start CPU profile: ", err)
}
defer pprof.StopCPUProfile()

// ... program runs and collects profile data ...
```

### StopCPUProfile

```go
func StopCPUProfile()
```

Stops the running CPU profile and waits for all writes to complete. Must be called after StartCPUProfile.

**Example:**
```go
pprof.StartCPUProfile(f)
defer pprof.StopCPUProfile()
```

## Memory Profiling Functions

### WriteHeapProfile

```go
func WriteHeapProfile(w io.Writer) error
```

Shorthand for `Lookup("heap").WriteTo(w, 0)`. Writes a heap profile snapshot to the provided writer. Preserved for backwards compatibility.

**Parameters:**
- `w io.Writer` - Writer to buffer heap profile output

**Returns:**
- Error if write fails; nil on success

**Example:**
```go
f, err := os.Create("heap.prof")
if err != nil {
	log.Fatal(err)
}
defer f.Close()

if err := pprof.WriteHeapProfile(f); err != nil {
	log.Fatal("could not write heap profile: ", err)
}
```

## Profile Type

### Type Definition

```go
type Profile struct {
	// contains filtered or unexported fields
}
```

A Profile is a collection of stack traces showing the call sequences that led to instances of allocation/blocking/etc.

### Profile Functions

#### Lookup

```go
func Lookup(name string) *Profile
```

Returns the profile with the given name, creating it if necessary. Returns nil if the name is not recognized.

**Predefined profile names:**
- `goroutine` - Stack traces of all current goroutines
- `heap` - Sampling of live object allocations
- `allocs` - Sampling of all past allocations
- `threadcreate` - Stack traces that led to the creation of new OS threads
- `block` - Stack traces that led to blocking on synchronization primitives
- `mutex` - Stack traces of holders of contended mutexes

**Parameters:**
- `name string` - Name of the profile

**Returns:**
- Pointer to Profile, or nil if name is not recognized

**Example:**
```go
heapProfile := pprof.Lookup("heap")
goroutineProfile := pprof.Lookup("goroutine")
```

#### NewProfile

```go
func NewProfile(name string) *Profile
```

Creates a new profile with the given name. Panics if a profile with that name already exists.

**Parameters:**
- `name string` - Unique name for the new profile

**Returns:**
- Pointer to the new Profile

**Panics:**
- If a profile with the given name already exists

**Example:**
```go
requestsProfile := pprof.NewProfile("requests")
```

#### Profiles

```go
func Profiles() []*Profile
```

Returns a slice of all known profiles, sorted by name.

**Returns:**
- Slice of pointers to all known profiles

**Example:**
```go
allProfiles := pprof.Profiles()
for _, profile := range allProfiles {
	fmt.Println(profile.Name())
}
```

### Profile Methods

#### Name

```go
func (p *Profile) Name() string
```

Returns the profile's name.

**Returns:**
- String name of the profile

**Example:**
```go
name := heapProfile.Name() // "heap"
```

#### Count

```go
func (p *Profile) Count() int
```

Returns the number of execution stacks currently in the profile.

**Returns:**
- Integer count of stacks

**Example:**
```go
count := goroutineProfile.Count()
fmt.Printf("Current goroutines: %d\n", count)
```

#### Add

```go
func (p *Profile) Add(value any, skip int)
```

Adds the current execution stack associated with a value to the profile. The caller can use `skip` to skip the stack frames from the profiling code itself.

**Parameters:**
- `value any` - Any value to associate with this stack
- `skip int` - Number of stack frames to skip (0 means include Add itself)

**Example:**
```go
type Request struct{}

var requestsProfile = pprof.NewProfile("requests")

func handleRequest(req *Request) {
	requestsProfile.Add(req, 1)
	defer requestsProfile.Remove(req)
	// ... handle request ...
}
```

#### Remove

```go
func (p *Profile) Remove(value any)
```

Removes the execution stack for a value from the profile. Does nothing if the value is not in the profile.

**Parameters:**
- `value any` - The value to remove

**Example:**
```go
defer requestsProfile.Remove(req)
```

#### WriteTo

```go
func (p *Profile) WriteTo(w io.Writer, debug int) error
```

Writes a pprof-formatted snapshot of the profile to the given writer.

**Parameters:**
- `w io.Writer` - Writer to output profile data
- `debug int` - Debug level (0=binary format, >0=plaintext human-readable format)

**Returns:**
- Error if write fails; nil on success

**Example:**
```go
f, err := os.Create("goroutine.prof")
if err != nil {
	log.Fatal(err)
}
defer f.Close()

if err := goroutineProfile.WriteTo(f, 0); err != nil {
	log.Fatal("could not write profile: ", err)
}
```

## Label-Based Profiling (Go 1.9+)

Labels allow associating profiling samples with additional context information, useful for grouping samples by request ID, user ID, etc.

### Label

```go
func Label(ctx context.Context, key string) (string, bool)
```

Returns the label value for the given key in the context. The boolean indicates whether the label was present.

**Parameters:**
- `ctx context.Context` - Context to check for labels
- `key string` - Label key to look up

**Returns:**
- `string` - Label value (empty if not present)
- `bool` - True if label exists, false otherwise

**Example:**
```go
val, ok := pprof.Label(ctx, "user_id")
if ok {
	fmt.Printf("User ID: %s\n", val)
}
```

### Labels

```go
func Labels(args ...string) LabelSet
```

Creates a LabelSet from an even number of key-value string pairs. Panics if odd number of arguments.

**Parameters:**
- `args ...string` - Key-value pairs (k1, v1, k2, v2, ...)

**Returns:**
- LabelSet - New label set

**Example:**
```go
labels := pprof.Labels("user_id", "123", "request_id", "abc-def")
```

### WithLabels

```go
func WithLabels(ctx context.Context, labels LabelSet) context.Context
```

Returns a new context with the provided labels added. New goroutines spawned will inherit these labels.

**Parameters:**
- `ctx context.Context` - Base context
- `labels LabelSet` - Labels to add

**Returns:**
- context.Context - New context with labels

**Example:**
```go
ctx := context.Background()
labels := pprof.Labels("user_id", "123")
newCtx := pprof.WithLabels(ctx, labels)
```

### Do

```go
func Do(ctx context.Context, labels LabelSet, f func(context.Context))
```

Calls function f with the augmented label context. All profiling samples taken during f execution are tagged with the given labels. Any goroutines spawned from f will inherit the labels.

**Parameters:**
- `ctx context.Context` - Base context
- `labels LabelSet` - Labels to apply
- `f func(context.Context)` - Function to execute with labeled context

**Example:**
```go
labels := pprof.Labels("user_id", "123", "endpoint", "/api/users")
pprof.Do(ctx, labels, func(ctx context.Context) {
	handleRequest(ctx, req)
})
```

### ForLabels

```go
func ForLabels(ctx context.Context, f func(key, value string) bool)
```

Invokes the provided function for each label in the context. The invoked function should return true to continue iteration or false to stop.

**Parameters:**
- `ctx context.Context` - Context containing labels
- `f func(key, value string) bool` - Callback function for each label

**Example:**
```go
pprof.ForLabels(ctx, func(key, value string) bool {
	fmt.Printf("%s=%s\n", key, value)
	return true // continue
})
```

### SetGoroutineLabels

```go
func SetGoroutineLabels(ctx context.Context)
```

Sets the current goroutine's labels to match the labels in the context. Lower-level than Do(), used when you can't wrap the entire operation in Do().

**Parameters:**
- `ctx context.Context` - Context with labels to apply

**Example:**
```go
ctx := pprof.WithLabels(context.Background(), pprof.Labels("request_id", "xyz"))
pprof.SetGoroutineLabels(ctx)
// Current goroutine now has "request_id" label
```

## LabelSet Type

```go
type LabelSet struct {
	// contains filtered or unexported fields
}
```

A LabelSet is an immutable set of labels created by the Labels function.

## Complete Example: Custom Profiling with Labels

```go
package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"runtime/pprof"
)

var customProfile = pprof.NewProfile("requests")

func main() {
	// Write profile when done
	f, err := os.Create("custom.prof")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()
	defer func() {
		if err := customProfile.WriteTo(f, 0); err != nil {
			log.Fatal("could not write profile: ", err)
		}
	}()

	// Process requests with labels
	ctx := context.Background()
	for i := 1; i <= 5; i++ {
		labels := pprof.Labels("request_id", fmt.Sprintf("req-%d", i))
		pprof.Do(ctx, labels, func(ctx context.Context) {
			// Simulated request handling
			processRequest(ctx, i)
		})
	}
}

func processRequest(ctx context.Context, id int) {
	// Request processing logic
	fmt.Printf("Processing request %d\n", id)
}
```

Then analyze with pprof:
```bash
go tool pprof custom.prof
(pprof) top
(pprof) list processRequest
```
