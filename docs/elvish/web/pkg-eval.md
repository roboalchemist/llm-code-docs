### Overview ¶

Package eval handles evaluation of parsed Elvish code and provides runtime
facilities.

### Index ¶

- Constants

- Variables

-
        func GetCompilationError(e interface{}) *diag.Error

-
        func IsUnqualified(name string) bool

-
        func ListenInterrupts() (<-chan struct{}, func())

-
        func MakePipelineError(excs []Exception) error

-
        func MakeVarFromName(name string) vars.Var

-
        func NewExternalCmdExit(name string, ws syscall.WaitStatus, pid int) error

-
        func NewPwdVar(ev *Evaler) vars.Var

-
        func NoSuchVariable(name string) error

-
        func Reason(err error) error

-
        func SplitIncompleteQNameNs(qname string) (ns, name string)

-
        func SplitQName(qname string) (first, rest string)

-
        func SplitQNameSegs(qname string) []string

-
        func SplitSigil(ref string) (sigil string, qname string)

-
          type CallCfg

-
          type Callable

-

-
            func NewExternalCmd(name string) Callable

-
            func NewGoFn(name string, impl interface{}) Callable

-
          type Editor

-
          type EvalCfg

-
          type Evaler

-

-
            func NewEvaler() *Evaler

-

-
            func (ev *Evaler) AddAfterChdir(f func(string))

-
            func (ev *Evaler) AddBeforeChdir(f func(string))

-
            func (ev *Evaler) AddBuiltin(ns *Ns)

-
            func (ev *Evaler) AddGlobal(ns *Ns)

-
            func (ev *Evaler) AddModule(name string, mod *Ns)

-
            func (ev *Evaler) Builtin() *Ns

-
            func (ev *Evaler) Call(f Callable, callCfg CallCfg, evalCfg EvalCfg) error

-
            func (ev *Evaler) Chdir(path string) error

-
            func (ev *Evaler) Check(src parse.Source, w io.Writer) (*parse.Error, *diag.Error)

-
            func (ev *Evaler) CheckTree(tree parse.Tree, w io.Writer) *diag.Error

-
            func (ev *Evaler) DaemonClient() daemon.Client

-
            func (ev *Evaler) Editor() Editor

-
            func (ev *Evaler) Eval(src parse.Source, cfg EvalCfg) error

-
            func (ev *Evaler) Global() *Ns

-
            func (ev *Evaler) PurelyEvalCompound(cn *parse.Compound) (string, bool)

-
            func (ev *Evaler) PurelyEvalPartialCompound(cn *parse.Compound, upto int) (string, bool)

-
            func (ev *Evaler) PurelyEvalPrimary(pn *parse.Primary) interface{}

-
            func (ev *Evaler) SetArgs(args []string)

-
            func (ev *Evaler) SetDaemonClient(client daemon.Client)

-
            func (ev *Evaler) SetLibDir(libDir string)

-
            func (ev *Evaler) ValuePrefix() string

-
          type Exception

-

-
            func NewException(reason error, stackTrace *StackTrace) Exception

-
          type ExternalCmdExit

-

-
            func (exit ExternalCmdExit) Error() string

-
            func (exit ExternalCmdExit) Fields() vals.StructMap

-
          type FailError

-

-
            func (e FailError) Error() string

-
            func (e FailError) Fields() vals.StructMap

-
          type Flow

-

-
            func (f Flow) Error() string

-
            func (f Flow) Fields() vals.StructMap

-
            func (f Flow) Show(string) string

-
          type Frame

-

-
            func (fm *Frame) CaptureOutput(f func(*Frame) error) ([]interface{}, error)

-
            func (fm *Frame) Close() error

-
            func (fm *Frame) Deprecate(msg string, ctx *diag.Context, minLevel int)

-
            func (fm *Frame) ErrorFile() *os.File

-
            func (fm *Frame) Eval(src parse.Source, r diag.Ranger, ns *Ns) (*Ns, error)

-
            func (fm *Frame) InputChan() chan interface{}

-
            func (fm *Frame) InputFile() *os.File

-
            func (fm *Frame) Interrupts() <-chan struct{}

-
            func (fm *Frame) IsInterrupted() bool

-
            func (fm *Frame) IterateInputs(f func(interface{}))

-
            func (fm *Frame) OutputChan() chan<- interface{}

-
            func (fm *Frame) OutputFile() *os.File

-
            func (fm *Frame) PipeOutput(f func(*Frame) error, vCb func(<-chan interface{}), bCb func(*os.File)) error

-
            func (fm *Frame) PrepareEval(src parse.Source, r diag.Ranger, ns *Ns) (*Ns, func() Exception, error)

-
          type Inputs

-
          type Ns

-

-
            func CombineNs(ns1 *Ns, ns2 *Ns) *Ns

-

-
            func (ns *Ns) Equal(rhs interface{}) bool

-
            func (ns *Ns) HasName(k string) bool

-
            func (ns *Ns) Hash() uint32

-
            func (ns *Ns) Index(k interface{}) (interface{}, bool)

-
            func (ns *Ns) IndexName(k string) vars.Var

-
            func (ns *Ns) IterateKeys(f func(interface{}) bool)

-
            func (ns *Ns) IterateNames(f func(string))

-
            func (ns *Ns) Kind() string

-
            func (ns *Ns) Repr(int) string

-
          type NsBuilder

-

-
            func (nb NsBuilder) Add(name string, v vars.Var) NsBuilder

-
            func (nb NsBuilder) AddFn(name string, v Callable) NsBuilder

-
            func (nb NsBuilder) AddGoFn(nsName, name string, impl interface{}) NsBuilder

-
            func (nb NsBuilder) AddGoFns(nsName string, fns map[string]interface{}) NsBuilder

-
            func (nb NsBuilder) AddNs(name string, v *Ns) NsBuilder

-
            func (nb NsBuilder) Ns() *Ns

-
          type PipelineError

-

-
            func (pe PipelineError) Error() string

-
            func (pe PipelineError) Fields() vals.StructMap

-
          type Port

-

-
            func CapturePort() (*Port, func() []interface{}, error)

-
            func FilePort(f *os.File, valuePrefix string) (*Port, func())

-
            func PipePort(vCb func(<-chan interface{}), bCb func(*os.File)) (*Port, func(), error)

-
            func PortsFromFiles(files [3]*os.File, prefix string) ([]*Port, func())

-
            func PortsFromStdFiles(prefix string) ([]*Port, func())

-
            func StringCapturePort() (*Port, func() []string, error)

-
          type RawOptions

-
          type StackTrace

-

-
            func MakeStackTrace(entries ...*diag.Context) *StackTrace

-
          type UnsupportedOptionsError

-

-
            func (er UnsupportedOptionsError) Error() string

- Bugs

### Constants ¶

      View Source
      

```
const (
 // FnSuffix is the suffix for the variable names of functions. Defining a
 // function "foo" is equivalent to setting a variable named "foo~", and vice
 // versa.
 FnSuffix = "~"
 // NsSuffix is the suffix for the variable names of namespaces. Defining a
 // namespace foo is equivalent to setting a variable named "foo:", and vice
 // versa.
 NsSuffix = ":"
)
```

### Variables ¶

      View Source
      

```
var (
 // NoArgs is an empty argument list. It can be used as an argument to Call.
 NoArgs = []interface{}{}
 // NoOpts is an empty option map. It can be used as an argument to Call.
 NoOpts = map[string]interface{}{}
)
```

      View Source
      

```
var (
 ErrBadglobPattern          = errors.New("bad globPattern; elvish bug")
 ErrCannotDetermineUsername = errors.New("cannot determine user name from glob pattern")
)
```

Errors thrown when globbing.

      View Source
      

```
var (
 // ErrExternalCmdOpts is thrown when an external command is passed Elvish
 // options.
 //
 // TODO: Catch this kind of errors at compilation time.
 ErrExternalCmdOpts = errors.New("external commands don't accept elvish options")
 // ErrImplicitCdNoArg is thrown when an implicit cd form is passed arguments.
 ErrImplicitCdNoArg = errors.New("implicit cd accepts no arguments")
)
```

      View Source
      

```
var (
 ErrMustFollowWildcard    = errors.New("must follow wildcard")
 ErrModifierMustBeString  = errors.New("modifier must be string")
 ErrWildcardNoMatch       = errors.New("wildcard has no match")
 ErrMultipleTypeModifiers = errors.New("only one type modifier allowed")
 ErrUnknownTypeModifier   = errors.New("unknown type modifier")
)
```

      View Source
      

```
var (
 // ErrArgs is thrown when a Go function gets erroneous arguments.
 //
 // TODO(xiaq): Replace this single error type with multiple types that carry
 // richer error information.
 ErrArgs = errors.New("args error")
 // ErrNoOptAccepted is thrown when a Go function that does not accept any
 // options gets passed options.
 ErrNoOptAccepted = errors.New("function does not accept any options")
)
```

      View Source
      

```
var (
 // ClosedChan is a closed channel, suitable as a placeholder input channel.
 ClosedChan = getClosedChan()
 // BlackholeChan is a channel that absorbs all values written to it,
 // suitable as a placeholder output channel.
 BlackholeChan = getBlackholeChan()
 // DevNull is /dev/null, suitable as a placeholder file for either input or
 // output.
 DevNull = getDevNull()

 // DummyInputPort is a port made up from DevNull and ClosedChan, suitable as
 // a placeholder input port.
 DummyInputPort = &Port{File: DevNull, Chan: ClosedChan}
 // DummyOutputPort is a port made up from DevNull and BlackholeChan,
 // suitable as a placeholder output port.
 DummyOutputPort = &Port{File: DevNull, Chan: BlackholeChan}
)
```

      View Source
      

```
var ErrBadBase = errors.New("bad base")
```

ErrBadBase is thrown by the "base" builtin if the base is smaller than 2 or
greater than 36.

      View Source
      

```
var ErrInputOfEawkMustBeString = errors.New("input of eawk must be string")
```

ErrInputOfEawkMustBeString is thrown when eawk gets a non-string input.

      View Source
      

```
var ErrInterrupted = errors.New("interrupted")
```

ErrInterrupted is thrown when the execution is interrupted by a signal.

      View Source
      

```
var ErrNonExistentEnvVar = errors.New("non-existent environment variable")
```

ErrNonExistentEnvVar is raised by the get-env command when the environment
variable does not exist.

      View Source
      

```
var ErrNotInSameProcessGroup = errors.New("not in the same process group")
```

ErrNotInSameProcessGroup is thrown when the process IDs passed to fg are not
in the same process group.

      View Source
      

```
var ErrStoreNotConnected = errors.New("store not connected")
```

ErrStoreNotConnected is thrown by dir-history when the store is not connected.

      View Source
      

```
var ErrUncomparable = errs.BadValue{
 What:  `inputs to "order"`,
 Valid: "comparable values", Actual: "uncomparable values"}
```

ErrUncomparable is raised by the order command when inputs contain
uncomparable values.

      View Source
      

```
var Getwd func() (string, error) = os.Getwd
```

Getwd allows for unit test error injection.

      View Source
      

```
var IsBuiltinSpecial = map[string]bool{}
```

IsBuiltinSpecial is the set of all names of builtin special forms. It is
intended for external consumption, e.g. the syntax highlighter.

      View Source
      

```
var OK = &exception{}
```

OK is a pointer to a special value of Exception that represents the absence
of exception.

      View Source
      

```
var TimeAfter = func(fm *Frame, d time.Duration) <-chan time.Time {
 return time.After(d)
}
```

TimeAfter is used by the sleep command to obtain a channel that is delivered
a value after the specified time.

It is a variable to allow for unit tests to efficiently test the behavior of
the `sleep` command, both by eliminating an actual sleep and verifying the
duration was properly parsed.

### Functions ¶

####

      func GetCompilationError ¶
  
    
  

    
    
      

```
func GetCompilationError(e interface{}) *diag.Error
```

GetCompilationError returns a *diag.Error if the given value is a compilation
error. Otherwise it returns nil.

####

      func IsUnqualified ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func IsUnqualified(name string) bool
```

IsUnqualified returns whether name is an unqualified variable name.

####

      func ListenInterrupts ¶
  
    
      added in
      v0.14.0
    
  

    
    
      

```
func ListenInterrupts() (<-chan struct{}, func())
```

ListenInterrupts returns a channel that is closed when SIGINT or SIGQUIT
has been received by the process. It also returns a function that should be
called when the channel is no longer needed.

####

      func MakePipelineError ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func MakePipelineError(excs []Exception) error
```

MakePipelineError builds an error from the execution results of multiple
commands in a pipeline.

If all elements are either nil or OK, it returns nil. If there is exactly
non-nil non-OK Exception, it returns it. Otherwise, it return a PipelineError
built from the slice, with nil items turned into OK's for easier access from
Elvish code.

####

      func MakeVarFromName ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func MakeVarFromName(name string) vars.Var
```

MakeVarFromName creates a Var with a suitable type constraint inferred from
the name.

####

      func NewExternalCmdExit ¶
  
    
  

    
    
      

```
func NewExternalCmdExit(name string, ws syscall.WaitStatus, pid int) error
```

NewExternalCmdExit constructs an error for representing a non-zero exit from
an external command.

####

      func NewPwdVar ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func NewPwdVar(ev *Evaler) vars.Var
```

NewPwdVar returns a variable who value is synchronized with the path of the
current working directory.

####

      func NoSuchVariable ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func NoSuchVariable(name string) error
```

NoSuchVariable returns an error representing that a variable can't be found.

####

      func Reason ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func Reason(err error) error
```

Reason returns the Reason field if err is an Exception. Otherwise it returns
err itself.

####

      func SplitIncompleteQNameNs ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func SplitIncompleteQNameNs(qname string) (ns, name string)
```

SplitIncompleteQNameNs splits an incomplete qualified variable name into the
namespace part and the name part.

####

      func SplitQName ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func SplitQName(qname string) (first, rest string)
```

SplitQName splits a qualified name into the first namespace segment and the
rest.

####

      func SplitQNameSegs ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func SplitQNameSegs(qname string) []string
```

SplitQNameSegs splits a qualified name into namespace segments.

####

      func SplitSigil ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func SplitSigil(ref string) (sigil string, qname string)
```

SplitSigil splits any leading sigil from a qualified variable name.

### Types ¶

####

      type CallCfg ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
type CallCfg struct {
 // Arguments to pass to the the function.
 Args []interface{}
 // Options to pass to the function.
 Opts map[string]interface{}
 // The name of the internal source that is calling the function.
 From string
}
```

CallCfg keeps configuration for the (*Evaler).Call method.

####

      type Callable ¶
  
    
  

    
    
      

```
type Callable interface {
 // Call calls the receiver in a Frame with arguments and options.
 Call(fm *Frame, args []interface{}, opts map[string]interface{}) error
}
```

Callable wraps the Call method.

####

      func NewExternalCmd ¶
  
    
      added in
      v0.15.0
    
  

    
    
      

```
func NewExternalCmd(name string) Callable
```

NewExternalCmd returns a callable that executes the named external command.

An external command converts all arguments to strings, and does not accept
any option.

####

      func NewGoFn ¶
  
    
  

    
    
      

```
func NewGoFn(name string, impl interface{}) Callable
```

NewGoFn wraps a Go function into an Elvish function using reflection.

Parameters are passed following these rules:

1. If the first parameter of function has type *Frame, it gets the current
call frame.

2. After the potential *Frame argument, the first parameter has type
RawOptions, it gets a map of option names to their values.

Alternatively, this parameter may be a (non-pointer) struct whose pointer
type implements a SetDefaultOptions method that takes no arguments and has no
return value. In this case, a new instance of the struct is constructed, the
SetDefaultOptions method is called, and any option passed to the Elvish
function is used to populate the fields of the struct. Field names are mapped
to option names using strutil.CamelToDashed, unless they have a field tag
"name", in which case the tag is preferred.

If the function does not declare that it accepts options via either method
described above, it accepts no options.

1. If the last parameter is non-variadic and has type Inputs, it represents
an optional parameter that contains the input to this function. If the
argument is not supplied, the input channel of the Frame will be used to
supply the inputs.

2. Other parameters are converted using vals.ScanToGo.

Return values go to the channel part of the stdout port, after being
converted using vals.FromGo. If the last return value has type error and is
not nil, it is turned into an exception and no outputting happens. If the
last return value is a nil error, it is ignored.
