### Overview ¶

Package progtest provides utilities for testing subprograms.

This package intentionally has no test file; it is excluded from test
coverage.

### Index ¶

-
        func Elvish(args ...string) []string

-
        func MustWriteFile(name, content string)

-
        func TestError(t *testing.T, f *Fixture, exit int, wantErrSnippet string)

-
          type Fixture

-

-
            func Setup() *Fixture

-

-
            func (f *Fixture) Cleanup()

-
            func (f *Fixture) Fds() [3]*os.File

-
            func (f *Fixture) FeedIn(s string)

-
            func (f *Fixture) TestOut(t *testing.T, fd int, wantOut string)

-
            func (f *Fixture) TestOutSnippet(t *testing.T, fd int, wantOutSnippet string)

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func Elvish ¶
  
    
  

    
    
      

```
func Elvish(args ...string) []string
```

Elvish returns an argument slice starting with "elvish".

####

      func MustWriteFile ¶
  
    
  

    
    
      

```
func MustWriteFile(name, content string)
```

MustWriteFile writes a file with the given name and content. It panics if the
write fails.

####

      func TestError ¶
  
    
  

    
    
      

```
func TestError(t *testing.T, f *Fixture, exit int, wantErrSnippet string)
```

TestError tests the error result of a program.

### Types ¶

####

      type Fixture ¶
  
    
  

    
    
      

```
type Fixture struct {
 // contains filtered or unexported fields
}
```

Fixture is a test fixture suitable for testing programs.

####

      func Setup ¶
  
    
  

    
    
      

```
func Setup() *Fixture
```

Setup sets up a test fixture. The caller is responsible for calling the
Cleanup method of the returned Fixture.

####

      func (*Fixture) Cleanup ¶
  
    
  

    
    
      

```
func (f *Fixture) Cleanup()
```

Cleanup cleans up the test fixture.

####

      func (*Fixture) Fds ¶
  
    
  

    
    
      

```
func (f *Fixture) Fds() [3]*os.File
```

Fds returns the file descriptors in the fixture.

####

      func (*Fixture) FeedIn ¶
  
    
  

    
    
      

```
func (f *Fixture) FeedIn(s string)
```

FeedIn feeds input to the standard input.

####

      func (*Fixture) TestOut ¶
  
    
  

    
    
      

```
func (f *Fixture) TestOut(t *testing.T, fd int, wantOut string)
```

TestOut tests that the output on the given FD matches the given text.

####

      func (*Fixture) TestOutSnippet ¶
  
    
  

    
    
      

```
func (f *Fixture) TestOutSnippet(t *testing.T, fd int, wantOutSnippet string)
```

TestOutSnippet tests that the output on the given FD contains the given text.
