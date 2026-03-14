### Index ¶

- Constants

- Variables

-
        func CmdExit(v eval.ExternalCmdExit) error

-
        func ErrorWithMessage(msg string) error

-
        func ErrorWithType(v error) error

-
        func Test(t *testing.T, tests ...TestCase)

-
        func TestWithSetup(t *testing.T, setup func(*eval.Evaler), tests ...TestCase)

-
          type Approximately

-
          type Result

-
          type TestCase

-

-
            func That(lines ...string) TestCase

-

-
            func (t TestCase) DoesNotCompile() TestCase

-
            func (t TestCase) DoesNothing() TestCase

-
            func (t TestCase) Prints(s string) TestCase

-
            func (t TestCase) PrintsStderrWith(s string) TestCase

-
            func (t TestCase) Puts(vs ...interface{}) TestCase

-
            func (t TestCase) Then(lines ...string) TestCase

-
            func (t TestCase) Throws(reason error, stacks ...string) TestCase

### Constants ¶

      View Source
      

```
const ApproximatelyThreshold = 1e-15
```

ApproximatelyThreshold defines the threshold for matching float64 values when
using Approximately.

### Variables ¶

      View Source
      

```
var AnyError = anyError{}
```

AnyError is an error that can be passed to TestCase.Throws to match any
non-nil error.

### Functions ¶

####

      func CmdExit ¶
  
    
  

    
    
      

```
func CmdExit(v eval.ExternalCmdExit) error
```

CmdExit returns an error that can be passed to TestCase.Throws to match an
eval.ExternalCmdExit ignoring the Pid field.

####

      func ErrorWithMessage ¶
  
    
  

    
    
      

```
func ErrorWithMessage(msg string) error
```

ErrorWithMessage returns an error that can be passed to TestCase.Throws to
match any error with the given message.

####

      func ErrorWithType ¶
  
    
  

    
    
      

```
func ErrorWithType(v error) error
```

ErrorWithType returns an error that can be passed to the TestCase.Throws
to match any error with the same type as the argument.

####

      func Test ¶
  
    
  

    
    
      

```
func Test(t *testing.T, tests ...TestCase)
```

Test runs test cases. For each test case, a new Evaler is created with
NewEvaler.

####

      func TestWithSetup ¶
  
    
  

    
    
      

```
func TestWithSetup(t *testing.T, setup func(*eval.Evaler), tests ...TestCase)
```

TestWithSetup runs test cases. For each test case, a new Evaler is created
with NewEvaler and passed to the setup function.

### Types ¶

####

      type Approximately ¶
  
    
  

    
    
      

```
type Approximately struct{ F float64 }
```

Approximately can be passed to TestCase.Puts to match a float64 within the
threshold defined by ApproximatelyThreshold.

####

      type Result ¶
  
    
  

    
    
      

```
type Result struct {
 ValueOut  []interface{}
 BytesOut  []byte
 StderrOut []byte

 CompilationError error
 Exception        error
}
```
