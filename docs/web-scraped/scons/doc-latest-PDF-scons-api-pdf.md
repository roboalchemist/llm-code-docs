# Source: https://scons.org/doc/latest/PDF/scons-api.pdf

Title: scons-api.pdf

URL Source: https://scons.org/doc/latest/PDF/scons-api.pdf

Published Time: Sun, 16 Nov 2025 22:19:30 GMT

Number of Pages: 273

Markdown Content:

# SCons API Docs

# version 4.10.1

SCons Project

November 16, 2025 Contents

SCons API Documentation 1

SCons package 1

Module contents 1

Submodules 1

SCons.Action module 1

SCons.Builder module 8

SCons.CacheDir module 13

SCons.Conftest module 14

SCons.Debug module 17

SCons.Defaults module 18

SCons.Environment module 20

SCons.Errors module 36

SCons.Executor module 37

SCons.Memoize module 40

SCons.PathList module 42

SCons.SConf module 42

SCons.SConsign module 48

SCons.Subst module 49

SCons.Warnings module 53

SCons.cpp module 56

SCons.dblite module 59

SCons.exitfuncs module 62

SConsDoc documentation module 62

SCons Documentation Processing module

62

SConsExamples documentation module

66

SCons Example Generator 66

SCons.compat package 68

Module contents 68

SCons.Node package 69

Module contents 69

Submodules 77

SCons.Node.Alias module 77

SCons.Node.FS module 83

SCons.Node.Python module 128

SCons.Platform package 134

Module contents 134

Submodules 135

SCons.Platform.aix module 135

SCons.Platform.cygwin module 136

SCons.Platform.darwin module 136

SCons.Platform.hpux module 136

SCons.Platform.irix module 136

SCons.Platform.mingw module 136

SCons.Platform.os2 module 136

SCons.Platform.posix module 136

SCons.Platform.sunos module 137

SCons.Platform.virtualenv module 137

SCons.Platform.win32 module 137

SCons.Scanner package 138

Module contents 138

Submodules 141

SCons.Scanner.C module 141

SCons.Scanner.D module 144

SCons.Scanner.Dir module 145

SCons.Scanner.Fortran module 145

SCons.Scanner.IDL module 146

SCons.Scanner.Java module 146

SCons.Scanner.LaTeX module 146

SCons.Scanner.Prog module 148

SCons.Scanner.RC module 148

SCons.Scanner.SWIG module 148

SCons.Script package 148

Module contents 148

Submodules 149

SCons.Script.Interactive module 149

SCons.Script.Main module 151

SCons.Script.SConsOptions module 157

SCons.Script.SConscript module 163

SCons.Taskmaster package 171

Module contents 171

Submodules 178

SCons.Taskmaster.Job module 178

SCons.Tool package 182

Module contents 182

SCons.Util package 184

Module contents 184

Submodules 191

SCons.Util.envs module 191

SCons.Util.filelock module 193

SCons.Util.hashes module 194

SCons.Util.sctypes module 195

SCons.Util.stats module 197

SCons.Variables package 198 Module contents 198

Submodules 201

SCons.Variables.BoolVariable module

201

SCons.Variables.EnumVariable module

201

SCons.Variables.ListVariable module

202

SCons.Variables.PackageVariable module

204

SCons.Variables.PathVariable module

205

Indices and Tables 206

Index 207

Python Module Index 269 SCons API Documentation

# Attention

This is the internal API Documentation for SCons. It is generated automatically from code docstrings using the Sphinx documentation generator, and covers much more than the Public API. If you were looking for the Public API - the interfaces that have long-term consistency guarantees, which you can reliably use when writing a build system for a project - see the SCons Reference Manual. Note that what is Public API and what is not is often not clearly delineated in these API Docs. The target audience is developers contributing to SCons itself, and those writing external Tools, Builders, and other related functionality for their project, who may need to reach beyond the Public API to accomplish their tasks. Reaching into internals is fine, but comes with the usual risks of “things here could change, it’s up to you to keep your code working”. Any missing/incomplete information is due to shortcomings in the docstrings in the code. Without being flippant, filling in all the docstrings has not always been a priority across the two-plus decades SCons has been in existence. Contributions improving the docstring front are welcome. It is often useful when making some larger change to fill in docstrings and suitable type annotations in the code being modified, “leaving the world a better place”, as it were. Note that the Sphinx configuration is limited, still a work in progress. SCons classes which inherit from Python standard library classes (e.g. UserList , UserDict , UserString ), may be allowed to show inherited mmembers; the Python standard library occasionally has little to no helpful docstring information. Inherited interfaces from outside SCons code can be identified by the lack of a [source] button to the right of the method signature. Such classes should be evaluated case-by-case and possibly switched to not show inherited members, depending on which way seems to provide the more useful result.

# SCons package

# Module contents

# Submodules

# SCons.Action module

SCons Actions.

Information about executing any sort of action that can build one or more target Nodes (typically files) from one or more source Nodes (also typically files) given a specific Environment.

The base class here is ActionBase. The base class supplies just a few utility methods and some generic methods for displaying information about an Action in response to the various commands that control printing.

A second-level base class is _ActionAction. This extends ActionBase by providing the methods that can be used to show and perform an action. True Action objects will subclass_ActionAction; Action factory class objects will subclass ActionBase.

The heavy lifting is handled by subclasses for the different types of actions we might execute:

CommandAction CommandGeneratorAction FunctionAction ListAction

The subclasses supply the following public interface methods used by other modules:

__call__()

SCons API Documentation

1THE public interface, “calling” an Action object executes the command or Python function. This also takes care of printing a pre-substitution command for debugging purposes.

get_contents()

Fetches the “contents” of an Action for signature calculation plus the varlist. This is what gets checksummed to decide if a target needs to be rebuilt because its action changed.

genstring()

Returns a string representation of the Action without command substitution, but allows aCommandGeneratorAction to generate the right action based on the specified target, source and env. This is used by the Signature subsystem (through the Executor) to obtain an (imprecise) representation of the Action operation for informative purposes.

Subclasses also supply the following methods for internal use within this module:

__str__()

Returns a string approximation of the Action; no variable substitution is performed.

execute()

The internal method that really, truly, actually handles the execution of a command or Python function. This is used so that the __call__() methods can take care of displaying any pre-substitution representations, and then

execute an action without worrying about the specific Actions involved.

get_presig()

Fetches the “contents” of a subclass for signature calculation. The varlist is added to this to produce the Action’s contents. TODO(?): Change this to always return bytes and not str?

strfunction()

Returns a substituted string representation of the Action. This is used by the _ActionAction.show() command to display the command/function that will be executed to generate the target(s).

There is a related independent ActionCaller class that looks like a regular Action, and which serves as a wrapper for arbitrary functions that we want to let the user specify the arguments to now, but actually execute later (when an out-of-date check determines that it’s needed to be executed, for example). Objects of this class are returned by an ActionFactory class that provides a __call__() method as a convenient way for wrapping up the functions.

SCons.Action.Action ( act , *args , **kw )

A factory for action objects.

class SCons.Action.ActionBase

Bases: ABC

Base class for all types of action objects that can be held by other objects (Builders, Executors, etc.) This provides the common methods for manipulating and combining those actions.

_abc_impl = <_abc._abc_data object>

batch_key ( env , target , source )

genstring ( target , source , env , executor: Executor | None = None) → str

get_contents ( target , source , env )

abstractmethod get_implicit_deps ( target , source , env , executor: Executor | None = None)

abstractmethod get_presig ( target , source , env , executor: Executor | None = None)

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

presub_lines ( env )

class SCons.Action.ActionCaller ( parent , args , kw )

Bases: object

A class for delaying calling an Action function with specific (positional and keyword) arguments until the Action is actually executed.

This class looks to the rest of the world like a normal Action object, but what it’s really doing is hanging on to the arguments until we have a target, source and env to use for the expansion.

get_contents ( target , source , env )

SCons API Documentation

2strfunction ( target , source , env )

subst ( s, target , source , env )

subst_args ( target , source , env )

subst_kw ( target , source , env )

class SCons.Action.ActionFactory ( actfunc , strfunc , convert=<function ActionFactory.<lambda>> )

Bases: object

A factory class that will wrap up an arbitrary function as an SCons-executable Action object.

The real heavy lifting here is done by the ActionCaller class. We just collect the (positional and keyword) arguments that we’re called with and give them to the ActionCaller object we create, so it can hang onto them until it needs them.

class SCons.Action.CommandAction ( cmd , **kw )

Bases: _ActionAction

Class for command-execution actions.

_abc_impl = <_abc._abc_data object>

_get_implicit_deps_heavyweight ( target , source , env , executor: Executor | None , icd_int )

Heavyweight dependency scanning involves scanning more than just the first entry in an action string. The exact behavior depends on the value of icd_int. Only files are taken as implicit dependencies; directories are ignored.

If icd_int is an integer value, it specifies the number of entries to scan for implicit dependencies. Action strings are also scanned after a &&. So for example, if icd_int=2 and the action string is “cd <some_dir> && $PYTHON $SCRIPT_PATH <another_path>”, the implicit dependencies would be the path to the python binary and the path to the script.

If icd_int is None, all entries are scanned for implicit dependencies.

_get_implicit_deps_lightweight ( target , source , env , executor: Executor | None )

Lightweight dependency scanning involves only scanning the first entry in an action string, even if it contains &&.

batch_key ( env , target , source )

execute ( target , source , env , executor: Executor | None = None)

Execute a command action.

This will handle lists of commands as well as individual commands, because construction variable substitution may turn a single “command” into a list. This means that this class can actually handle lists of commands, even though that’s not how we use it externally.

genstring ( target , source , env , executor: Executor | None = None) → str

get_contents ( target , source , env )

get_implicit_deps ( target , source , env , executor: Executor | None = None)

Return the implicit dependencies of this action’s command line.

get_presig ( target , source , env , executor: Executor | None = None)

Return the signature contents of this action’s command line.

This strips $(-$) and everything in between the string, since those parts don’t affect signatures.

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

presub_lines ( env )

print_cmd_line ( s, target , source , env ) → None

In python 3, and in some of our tests, sys.stdout is a String io object, and it takes unicode strings only This code assumes s is a regular string.

process ( target , source , env , executor: Executor | None = None, overrides: dict | None =

None) → tuple [list , bool , bool ]

strfunction ( target , source , env , executor: Executor | None = None, overrides: dict | None =

None) → str

class SCons.Action.CommandGeneratorAction ( generator , kw )

Bases: ActionBase

Class for command-generator actions.

_abc_impl = <_abc._abc_data object>

_generate ( target , source , env , for_signature , executor: Executor | None = None)

batch_key ( env , target , source )

genstring ( target , source , env , executor: Executor | None = None) → str

SCons API Documentation

3get_contents ( target , source , env )

get_implicit_deps ( target , source , env , executor: Executor | None = None)

get_presig ( target , source , env , executor: Executor | None = None)

Return the signature contents of this action’s command line.

This strips $(-$) and everything in between the string, since those parts don’t affect signatures.

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

presub_lines ( env )

class SCons.Action.FunctionAction ( execfunction , kw )

Bases: _ActionAction

Class for Python function actions.

_abc_impl = <_abc._abc_data object>

batch_key ( env , target , source )

execute ( target , source , env , executor: Executor | None = None)

function_name ()

genstring ( target , source , env , executor: Executor | None = None) → str

get_contents ( target , source , env )

get_implicit_deps ( target , source , env , executor: Executor | None = None)

get_presig ( target , source , env , executor: Executor | None = None)

Return the signature contents of this callable action.

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

presub_lines ( env )

print_cmd_line ( s, target , source , env ) → None

In python 3, and in some of our tests, sys.stdout is a String io object, and it takes unicode strings only This code assumes s is a regular string.

strfunction ( target , source , env , executor: Executor | None = None)

class SCons.Action.LazyAction ( var , kw )

Bases: CommandGeneratorAction, CommandAction

A LazyAction is a kind of hybrid generator and command action for strings of the form “$VAR”. These strings normally expand to other strings (think “$CCCOM” to “$CC -c -o $TARGET $SOURCE”), but we also want to be able to replace them with functions in the construction environment. Consequently, we want lazy evaluation and creation of an Action in the case of the function, but that’s overkill in the more normal case of expansion to other strings.

So we do this with a subclass that’s both a generator and a command action. The overridden methods all do a quick check of the construction variable, and if it’s a string we just call the corresponding CommandAction method to do the heavy lifting. If not, then we call the same-named CommandGeneratorAction method. The CommandGeneratorAction methods work by using the overridden _generate() method, that is, our own way of handling “generation” of an action based on what’s in the construction variable.

_abc_impl = <_abc._abc_data object>

_generate ( target , source , env , for_signature , executor: Executor | None = None)

_generate_cache ( env )

_get_implicit_deps_heavyweight ( target , source , env , executor: Executor | None , icd_int )

Heavyweight dependency scanning involves scanning more than just the first entry in an action string. The exact behavior depends on the value of icd_int. Only files are taken as implicit dependencies; directories are ignored.

If icd_int is an integer value, it specifies the number of entries to scan for implicit dependencies. Action strings are also scanned after a &&. So for example, if icd_int=2 and the action string is “cd <some_dir> && $PYTHON $SCRIPT_PATH <another_path>”, the implicit dependencies would be the path to the python binary and the path to the script.

If icd_int is None, all entries are scanned for implicit dependencies.

_get_implicit_deps_lightweight ( target , source , env , executor: Executor | None )

Lightweight dependency scanning involves only scanning the first entry in an action string, even if it contains &&.

batch_key ( env , target , source )

SCons API Documentation

4execute ( target , source , env , executor: Executor | None = None)

Execute a command action.

This will handle lists of commands as well as individual commands, because construction variable substitution may turn a single “command” into a list. This means that this class can actually handle lists of commands, even though that’s not how we use it externally.

genstring ( target , source , env , executor: Executor | None = None) → str

get_contents ( target , source , env )

get_implicit_deps ( target , source , env , executor: Executor | None = None)

Return the implicit dependencies of this action’s command line.

get_parent_class ( env )

get_presig ( target , source , env , executor: Executor | None = None)

Return the signature contents of this action’s command line.

This strips $(-$) and everything in between the string, since those parts don’t affect signatures.

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

presub_lines ( env )

print_cmd_line ( s, target , source , env ) → None

In python 3, and in some of our tests, sys.stdout is a String io object, and it takes unicode strings only This code assumes s is a regular string.

process ( target , source , env , executor: Executor | None = None, overrides: dict | None =

None) → tuple [list , bool , bool ]

strfunction ( target , source , env , executor: Executor | None = None, overrides: dict | None =

None) → str

class SCons.Action.ListAction ( actionlist )

Bases: ActionBase

Class for lists of other actions.

_abc_impl = <_abc._abc_data object>

batch_key ( env , target , source )

genstring ( target , source , env , executor: Executor | None = None) → str

get_contents ( target , source , env )

get_implicit_deps ( target , source , env , executor: Executor | None = None)

get_presig ( target , source , env , executor: Executor | None = None)

Return the signature contents of this action list.

Simple concatenation of the signatures of the elements.

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

presub_lines ( env )

class SCons.Action._ActionAction ( cmdstr=<class 'SCons.Action._null'> , strfunction=<class 'SCons.Action._null'> , varlist=() , presub=<class 'SCons.Action._null'> , chdir=None ,

exitstatfunc=None , batch_key=None , targets: str = '$TARGETS' , **kw )

Bases: ActionBase

Base class for actions that create output objects.

_abc_impl = <_abc._abc_data object>

batch_key ( env , target , source )

genstring ( target , source , env , executor: Executor | None = None) → str

get_contents ( target , source , env )

get_implicit_deps ( target , source , env , executor: Executor | None = None)

get_presig ( target , source , env , executor: Executor | None = None)

get_targets ( env , executor: Executor | None )

Returns the type of targets ($TARGETS, $CHANGED_TARGETS) used by this action.

get_varlist ( target , source , env , executor: Executor | None = None)

no_batch_key ( env , target , source )

SCons API Documentation

5presub_lines ( env )

print_cmd_line ( s, target , source , env ) → None

In python 3, and in some of our tests, sys.stdout is a String io object, and it takes unicode strings only This code assumes s is a regular string.

SCons.Action._actionAppend ( act1 , act2 )

Joins two actions together.

Mainly, it handles ListActions by concatenating into a single ListAction.

SCons.Action._callable_contents ( obj ) → bytearray

Return the signature contents of a callable Python object.

SCons.Action._code_contents ( code , docstring= None) → bytearray

Return the signature contents of a code object.

By providing direct access to the code object of the function, Python makes this extremely easy. Hooray!

Unfortunately, older versions of Python include line number indications in the compiled byte code. Boo! So we remove the line number byte codes to prevent recompilations from moving a Python function.

See:

• https://docs.python.org/3/library/inspect.html

• http://python-reference.readthedocs.io/en/latest/docs/code/index.html

For info on what each co_ variable provides

The signature is as follows (should be byte/chars): co_argcount, len(co_varnames), len(co_cellvars), len(co_freevars), ( comma separated signature for each object in co_consts ), ( comma separated signature for each object in co_names ), ( The bytecode with line number bytecodes removed from co_code )

co_argcount - Returns the number of positional arguments (including arguments with default values). co_varnames -Returns a tuple containing the names of the local variables (starting with the argument names). co_cellvars - Returns a tuple containing the names of local variables that are referenced by nested functions. co_freevars - Returns a tuple containing the names of free variables. (?) co_consts - Returns a tuple containing the literals used by the bytecode. co_names - Returns a tuple containing the names used by the bytecode. co_code - Returns a string representing the sequence of bytecode instructions.

SCons.Action._do_create_action ( act , kw )

The internal implementation for the Action factory method.

This handles the fact that passing lists to Action() itself has different semantics than passing lists as elements of lists. The former will create a ListAction, the latter will create a CommandAction by converting the inner list elements to strings.

SCons.Action._do_create_keywords ( args , kw )

This converts any arguments after the action argument into their equivalent keywords and adds them to the kw argument.

SCons.Action._do_create_list_action ( act , kw ) → ListAction

A factory for list actions.

Convert the input list act into Actions and then wrap them in a ListAction. If act has only a single member, return that member, not a ListAction . This is intended to allow a contained list to specify a command action without being processed into a list action.

SCons.Action._function_contents ( func ) → bytearray

Return the signature contents of a function.

The signature is as follows (should be byte/chars): < _code_contents (see above) from func.__code__ > ,( comma separated _object_contents for function argument defaults) ,( comma separated _object_contents for any closure contents )

See also: https://docs.python.org/3/reference/datamodel.html

• func.__code__ - The code object representing the compiled function body.

• func.__defaults__ - A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value

• func.__closure__ - None or a tuple of cells that contain bindings for the function’s free variables.

class SCons.Action._null

Bases: object

SCons API Documentation

6SCons.Action._object_contents ( obj ) → bytearray

Return the signature contents of any Python object.

We have to handle the case where object contains a code object since it can be pickled directly.

SCons.Action._object_instance_content ( obj )

Returns consistant content for a action class or an instance thereof

Parameters: • obj Should be either and action class or an instance thereof

Returns: bytearray or bytes representing the obj suitable for generating a signature from.

SCons.Action._resolve_shell_env ( env , target , source )

Returns a resolved execution environment.

First get the execution environment. Then if SHELL_ENV_GENERATORS is set and is iterable, call each function to allow it to alter the created execution environment, passing each the returned execution environment from the previous call.

Added in version 4.4.

SCons.Action._string_from_cmd_list ( cmd_list )

Takes a list of command line arguments and returns a pretty representation for printing.

SCons.Action._subproc ( scons_env , cmd , error= 'ignore', **kw )

Wrapper for subprocess.Popen which pulls from construction env.

Use for calls to subprocess which need to interpolate values from an SCons construction environment into the environment passed to subprocess. Adds an an error-handling argument. Adds ability to specify std{in,out,err} with “‘devnull’” tag.

Deprecated since version 4.6.

SCons.Action.default_exitstatfunc ( s)

SCons.Action.get_default_ENV ( env )

Returns an execution environment.

If there is one in env , just use it, else return the Default Environment, insantiated if necessary.

A fiddlin’ little function that has an import SCons.Environment which cannot be moved to the top level without creating an import loop. Since this import creates a local variable named SCons , it blocks access to the global variable, so we move it here to prevent complaints about local variables being used uninitialized.

SCons.Action.rfile ( n)

SCons.Action.scons_subproc_run ( scons_env , *args , **kwargs ) → CompletedProcess

Run an external command using an SCons execution environment.

SCons normally runs external build commands using subprocess, but does not harvest any output from such commands. This function is a thin wrapper around subprocess.run() allowing running a command in an SCons context (i.e. uses an “execution environment” rather than the user’s existing environment), and provides the ability to return any output in a subprocess.CompletedProcess instance (this must be selected by setting stdout and/or

stderr to PIPE , or setting capture_output=True - see Keyword Arguments). Typical use case is to run a tool’s “version” option to find out the installed version.

If supplied, the env keyword argument provides an execution environment to process into appropriate form before it is supplied to subprocess; if omitted, scons_env is used to derive a suitable default. The other keyword arguments are passed through, except that the SCons legacy error keyword is remapped to the subprocess check keyword; if both are omitted check=False will be passed. The caller is responsible for setting up the desired arguments for subprocess.run().

This function retains the legacy behavior of returning something vaguely usable even in the face of complete failure, unless check=True (in which case an error is allowed to be raised): it synthesizes a CompletedProcess instance in this case.

A subset of interesting keyword arguments follows; see the Python documentation of subprocess for the complete list.

SCons API Documentation

7Keyword Arguments: • stdout – (and stderr , stdin ) if set to subprocess.PIPE. send input to or collect output from the relevant stream in the subprocess; the default None does no redirection (i.e. output or errors may go to the console or log file, but is not captured); if set to subprocess.DEVNULL they are explicitly thrown away. capture_output=True is a synonym for setting both stdout and stderr to PIPE.

• text – open stdin , stdout , stderr in text mode. Default is binary mode.

universal_newlines is a synonym.

• encoding – specifies an encoding. Changes to text mode.

• errors – specified error handling. Changes to text mode.

• input – a byte sequence to be passed to stdin , unless text mode is enabled, in which case it must be a string.

• shell – if true, the command is executed through the shell.

• check – if true and the subprocess exits with a non-zero exit code, raise asubprocess.CalledProcessError exception. Otherwise (the default) in case of an OSError, report the exit code in the CompletedProcess instance.

Added in version 4.6.

# SCons.Builder module

SCons.Builder

Builder object subsystem.

A Builder object is a callable that encapsulates information about how to execute actions to create a target Node (file) from source Nodes (files), and how to create those dependencies for tracking.

The main entry point here is the Builder() factory method. This provides a procedural interface that creates the right underlying Builder object based on the keyword arguments supplied and the types of the arguments.

The goal is for this external interface to be simple enough that the vast majority of users can create new Builders as necessary to support building new types of files in their configurations, without having to dive any deeper into this subsystem.

The base class here is BuilderBase. This is a concrete base class which does, in fact, represent the Builder objects that we (or users) create.

There is also a proxy that looks like a Builder:

CompositeBuilder This proxies for a Builder with an action that is actually a dictionary that knows how to map file suffixes to a specific action. This is so that we can invoke different actions (compilers, compile options) for different flavors of source files.

Builders and their proxies have the following public interface methods used by other modules:

• __call__()

THE public interface. Calling a Builder object (with the use of internal helper methods) sets up the target and source dependencies, appropriate mapping to a specific action, and the environment manipulation necessary for overridden construction variable. This also takes care of warning about possible mistakes in keyword arguments.

• add_emitter()

Adds an emitter for a specific file suffix, used by some Tool modules to specify that (for example) a yacc invocation on a .y can create a .h and a .c file.

• add_action()

SCons API Documentation

8Adds an action for a specific file suffix, heavily used by Tool modules to add their specific action(s) for turning a source file into an object file to the global static and shared object file Builders.

There are the following methods for internal use within this module:

• _execute()

The internal method that handles the heavily lifting when a Builder is called. This is used so that the __call__() methods can set up warning about possible mistakes in keyword-argument overrides, and

then execute all of the steps necessary so that the warnings only occur once.

• get_name()

Returns the Builder’s name within a specific Environment, primarily used to try to return helpful information in error messages.

• adjust_suffix()

• get_prefix()

• get_suffix()

• get_src_suffix()

• set_src_suffix()

Miscellaneous stuff for handling the prefix and suffix manipulation we use in turning source file names into target file names.

SCons.Builder.Builder ( **kw )

A factory for builder objects.

class SCons.Builder.BuilderBase ( action=None , prefix: str = '' , suffix: str = '' , src_suffix: str = '' , target_factory=None , source_factory=None , target_scanner=None , source_scanner=None ,

emitter=None , multi: bool = False , env=None , single_source: bool = False , name=None ,

chdir=<class 'SCons.Builder._Null'> , is_explicit: bool = True , src_builder=None ,

ensure_suffix: bool = False , **overrides )

Bases: object

Base class for Builders, objects that create output nodes (files) from input nodes (files).

_adjustixes ( files , pre , suf , ensure_suffix: bool = False)

_create_nodes ( env , target= None, source= None)

Create and return lists of target and source nodes.

_execute ( env , target , source , overwarn= {}, executor_kw= {})

_get_sdict ( env )

Returns a dictionary mapping all of the source suffixes of all src_builders of this Builder to the underlying Builder that should be called first.

This dictionary is used for each target specified, so we save a lot of extra computation by memoizing it for each construction environment.

Note that this is re-computed each time, not cached, because there might be changes to one of our source Builders (or one of their source Builders, and so on, and so on…) that we can’t “see.”

The underlying methods we call cache their computed values, though, so we hope repeatedly aggregating them into a dictionary like this won’t be too big a hit. We may need to look for a better way to do this if performance data show this has turned into a significant bottleneck.

_get_src_builders_key ( env )

_subst_src_suffixes_key ( env )

add_emitter ( suffix , emitter ) → None

Add a suffix-emitter mapping to this Builder.

This assumes that emitter has been initialized with an appropriate dictionary type, and will throw a TypeError if not, so the caller is responsible for knowing that this is an appropriate method to call for the Builder in question.

add_src_builder ( builder ) → None

Add a new Builder to the list of src_builders.

This requires wiping out cached values so that the computed lists of source suffixes get re-calculated.

adjust_suffix ( suff )

get_name ( env )

SCons API Documentation

9Attempts to get the name of the Builder.

Look at the BUILDERS variable of env, expecting it to be a dictionary containing this Builder, and return the key of the dictionary. If there’s no key, then return a directly-configured name (if there is one) or the name of the class (by default).

get_prefix ( env , sources= [])

get_src_builders ( env )

Returns the list of source Builders for this Builder.

This exists mainly to look up Builders referenced as strings in the ‘BUILDER’ variable of the construction environment and cache the result.

get_src_suffix ( env )

Get the first src_suffix in the list of src_suffixes.

get_suffix ( env , sources= [])

set_src_suffix ( src_suffix ) → None

set_suffix ( suffix ) → None

splitext ( path , env= None)

src_builder_sources ( env , source , overwarn= {})

src_suffixes ( env )

Returns the list of source suffixes for all src_builders of this Builder.

This is essentially a recursive descent of the src_builder “tree.” (This value isn’t cached because there may be changes in a src_builder many levels deep that we can’t see.)

subst_src_suffixes ( env )

The suffix list may contain construction variable expansions, so we have to evaluate the individual strings. To avoid doing this over and over, we memoize the results for each construction environment.

class SCons.Builder.CallableSelector

Bases: Selector

A callable dictionary that will, in turn, call the value it finds if it can.

clear () → None. Remove all items from D.

copy () → a shallow copy of D

classmethod fromkeys ( iterable , value= None, /)

Create a new dictionary with keys from iterable and values set to value.

get ( key , default= None, /)

Return the value for key if key is in the dictionary, else default.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem ()

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault ( key , default= None, /)

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update ([, E], **F ) → None. Update D from dict/iterable E and F.

If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

values () → an object providing a view on D's values

class SCons.Builder.CompositeBuilder ( builder , cmdgen )

Bases: Proxy

A Builder Proxy whose main purpose is to always have a DictCmdGenerator as its action, and to provide access to the DictCmdGenerator’s add_action() method.

__getattr__ ( name )

Retrieve an attribute from the wrapped object.

Raises: AttributeError – if attribute name doesn’t exist.

add_action ( suffix , action ) → None

get ()

SCons API Documentation

10 Retrieve the entire wrapped object

class SCons.Builder.DictCmdGenerator ( mapping= None, source_ext_match: bool = True)

Bases: Selector

This is a callable class that can be used as a command generator function. It holds on to a dictionary mapping file suffixes to Actions. It uses that dictionary to return the proper action based on the file suffix of the source file.

add_action ( suffix , action ) → None

Add a suffix-action pair to the mapping.

clear () → None. Remove all items from D.

copy () → a shallow copy of D

classmethod fromkeys ( iterable , value= None, /)

Create a new dictionary with keys from iterable and values set to value.

get ( key , default= None, /)

Return the value for key if key is in the dictionary, else default.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem ()

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault ( key , default= None, /)

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

src_suffixes ()

update ([, E], **F ) → None. Update D from dict/iterable E and F.

If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

values () → an object providing a view on D's values

class SCons.Builder.DictEmitter

Bases: Selector

A callable dictionary that maps file suffixes to emitters. When called, it finds the right emitter in its dictionary for the suffix of the first source file, and calls that emitter to get the right lists of targets and sources to return. If there’s no emitter for the suffix in its dictionary, the original target and source are returned.

clear () → None. Remove all items from D.

copy () → a shallow copy of D

classmethod fromkeys ( iterable , value= None, /)

Create a new dictionary with keys from iterable and values set to value.

get ( key , default= None, /)

Return the value for key if key is in the dictionary, else default.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem ()

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault ( key , default= None, /)

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update ([, E], **F ) → None. Update D from dict/iterable E and F.

If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

values () → an object providing a view on D's values

class SCons.Builder.EmitterProxy ( var )

Bases: object

SCons API Documentation

11 This is a callable class that can act as a Builder emitter. It holds on to a string that is a key into an Environment dictionary, and will look there at actual build time to see if it holds a callable. If so, we will call that as the actual emitter.

class SCons.Builder.ListEmitter ( initlist= None)

Bases: UserList

A callable list of emitters that calls each in sequence, returning the result.

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

class SCons.Builder.OverrideWarner ( mapping )

Bases: UserDict

A class for warning about keyword arguments that we use as overrides in a Builder call.

This class exists to handle the fact that a single Builder call can actually invoke multiple builders. This class only emits the warnings once, no matter how many Builders are invoked.

_abc_impl = <_abc._abc_data object>

clear () → None. Remove all items from D.

copy ()

classmethod fromkeys ( iterable , value= None)

get ( k[, d]) → D[k] if k in D, else d. d defaults to None.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

popitem () → (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

setdefault ( k[, d]) → D.get(k,d), also set D[k]=d if k not in D

update ([, E], **F ) → None. Update D from mapping/iterable E and F.

If E present and has a .keys() method, does: for k in E: D[k] = E[k] If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v In either case, this is followed by: for k, v in F.items(): D[k] = v

values () → an object providing a view on D's values

warn () → None

class SCons.Builder._Null

Bases: object

SCons.Builder._node_errors ( builder , env , tlist , slist )

Validate that the lists of target and source nodes are legal for this builder and environment. Raise errors or issue warnings as appropriate.

SCons.Builder._null

alias of _Null

SCons.Builder.is_a_Builder ( obj ) → bool

SCons API Documentation

12 “Returns True if the specified obj is one of our Builder classes.

The test is complicated a bit by the fact that CompositeBuilder is a proxy, not a subclass of BuilderBase.

SCons.Builder.match_splitext ( path , suffixes= [])

# SCons.CacheDir module

CacheDir support

class SCons.CacheDir.CacheDir ( path )

Bases: object

CacheDebug ( fmt , target , cachefile ) → None

_add_config ( path: str ) → None

Create the cache config file in path .

Locking isn’t necessary in the normal case - when the cachedir is being created - because it’s written to a unique directory first, before the directory is renamed. But it is legal to call CacheDir with an existing directory, which may be missing the config file, and in that case we do need locking. Simpler to always lock.

_mkdir_atomic ( path: str ) → bool

Create cache directory at path .

Uses directory renaming to avoid races. If we are actually creating the dir, populate it with the metadata files at the same time as that’s the safest way. But it’s not illegal to point CacheDir at an existing directory that wasn’t a cache previously, so we may have to do that elsewhere, too.

Returns: True if it we created the dir, False if already existed,

Raises: SConsEnvironmentError – if we tried and failed to create the cache.

_readconfig ( path: str ) → None

Read the cache config from path .

If directory or config file do not exist, create and populate.

cachepath ( node ) → tuple

Return where to cache a file.

Given a Node, obtain the configured cache directory and the path to the cached file, which is generated from the node’s build signature. If caching is not enabled for the None, return a tuple of None.

classmethod copy_from_cache ( env , src , dst ) → str

Copy a file from cache.

classmethod copy_to_cache ( env , src , dst ) → str

Copy a file to cache.

Just use the FS copy2 (“with metadata”) method, except do an additional check and if necessary a chmod to ensure the cachefile is writeable, to forestall permission problems if the cache entry is later updated.

get_cachedir_csig ( node ) → str

property hit_ratio : float

is_enabled () → bool

is_readonly () → bool

property misses : int

push ( node )

push_if_forced ( node )

retrieve ( node ) → bool

Retrieve a node from cache.

Returns True if a successful retrieval resulted.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Note that there’s a special trick here with the execute flag (one that’s not normally done for other actions). Basically if the user requested a no_exec (-n) build, then SCons.Action.execute_actions is set to 0 and when any action is called, it does its showing but then just returns zero instead of actually calling the action execution operation. The problem for caching is that if the file does NOT exist in cache then the CacheRetrieveString won’t return anything to show for the task, but the Action.__call__ won’t call CacheRetrieveFunc; instead it just returns zero, which makes the code below think that the file was successfully retrieved from the cache, therefore it doesn’t do any subsequent building. However, the CacheRetrieveString didn’t print anything because it didn’t actually exist in the cache, and no more build actions will be performed, so the user just sees nothing. The fix is to tell Action.__call__

SCons API Documentation

13 to always execute the CacheRetrieveFunc and then have the latter explicitly check SCons.Action.execute_actions itself.

SCons.CacheDir.CachePushFunc ( target , source , env ) → None

SCons.CacheDir.CacheRetrieveFunc ( target , source , env ) → int

SCons.CacheDir.CacheRetrieveString ( target , source , env ) → str

# SCons.Conftest module

Autoconf-like configuration support

The purpose of this module is to define how a check is to be performed.

A context class is used that defines functions for carrying out the tests, logging and messages. The following methods and members must be present:

context.Display(msg)

Function called to print messages that are normally displayed for the user. Newlines are explicitly used. The text should also be written to the logfile!

context.Log(msg)

Function called to write to a log file.

context.BuildProg(text, ext)

Function called to build a program, using “ext” for the file extension. Must return an empty string for success, an error message for failure. For reliable test results building should be done just like an actual program would be build, using the same command and arguments (including configure results so far).

context.CompileProg(text, ext)

Function called to compile a program, using “ext” for the file extension. Must return an empty string for success, an error message for failure. For reliable test results compiling should be done just like an actual source file would be compiled, using the same command and arguments (including configure results so far).

context.AppendLIBS(lib_name_list)

Append “lib_name_list” to the value of LIBS. “lib_namelist” is a list of strings. Return the value of LIBS before changing it (any type can be used, it is passed to SetLIBS() later.)

context.PrependLIBS(lib_name_list)

Prepend “lib_name_list” to the value of LIBS. “lib_namelist” is a list of strings. Return the value of LIBS before changing it (any type can be used, it is passed to SetLIBS() later.)

context.SetLIBS(value)

Set LIBS to “value”. The type of “value” is what AppendLIBS() returned. Return the value of LIBS before changing it (any type can be used, it is passed to SetLIBS() later.)

context.headerfilename

Name of file to append configure results to, usually “confdefs.h”. The file must not exist or be empty when starting. Empty or None to skip this (some tests will not work!).

context.config_h (may be missing).

If present, must be a string, which will be filled with the contents of a config_h file.

context.vardict

Dictionary holding variables used for the tests and stores results from the tests, used for the build commands. Normally contains “CC”, “LIBS”, “CPPFLAGS”, etc.

context.havedict

Dictionary holding results from the tests that are to be used inside a program. Names often start with “HAVE_”. These are zero (feature not present) or one (feature present). Other variables may have any value, e.g., “PERLVERSION” can be a number and “SYSTEMNAME” a string.

SCons.Conftest.CheckBuilder ( context , text= None, language= None)

Configure check to see if the compiler works. Note that this uses the current value of compiler and linker flags, make sure $CFLAGS, $CPPFLAGS and $LIBS are set correctly. “language” should be “C” or “C++” and is used to select

SCons API Documentation

14 the compiler. Default is “C”. “text” may be used to specify the code to be build. Returns an empty string for success, an error message for failure.

SCons.Conftest.CheckCC ( context )

Configure check for a working C compiler.

This checks whether the C compiler, as defined in the $CC construction variable, can compile a C source file. It uses the current $CCCOM value too, so that it can test against non working flags.

SCons.Conftest.CheckCXX ( context )

Configure check for a working CXX compiler.

This checks whether the CXX compiler, as defined in the $CXX construction variable, can compile a CXX source file. It uses the current $CXXCOM value too, so that it can test against non working flags.

SCons.Conftest.CheckDeclaration ( context , symbol , includes= None, language= None)

Checks whether symbol is declared.

Use the same test as autoconf, that is test whether the symbol is defined as a macro or can be used as an r-value.

Parameters: • symbol – str the symbol to check

• includes – str Optional “header” can be defined to include a header file.

• language – str only C and C++ supported.

Returns: boolTrue if the check failed, False if succeeded.

Return type: status

SCons.Conftest.CheckFunc ( context , function_name , header= None, language= None, funcargs= None)

Configure check for a function “function_name”. “language” should be “C” or “C++” and is used to select the compiler. Default is “C”. Optional “header” can be defined to define a function prototype, include a header file or anything else that comes before main(). Optional “funcargs” can be defined to define an argument list for the generated function invocation. Sets HAVE_function_name in context.havedict according to the result. Note that this uses the current value of compiler and linker flags, make sure $CFLAGS, $CPPFLAGS and $LIBS are set correctly. Returns an empty string for success, an error message for failure.

Changed in version 4.7.0: The funcargs parameter was added.

SCons.Conftest.CheckHeader ( context , header_name , header= None, language= None,

include_quotes= None)

Configure check for a C or C++ header file “header_name”. Optional “header” can be defined to do something before including the header file (unusual, supported for consistency). “language” should be “C” or “C++” and is used to select the compiler. Default is “C”. Sets HAVE_header_name in context.havedict according to the result. Note that this uses the current value of compiler and linker flags, make sure $CFLAGS and $CPPFLAGS are set correctly. Returns an empty string for success, an error message for failure.

SCons.Conftest.CheckLib ( context , libs , func_name= None, header= None, extra_libs= None, call= None,

language= None, autoadd: int = 1, append: bool = True, unique: bool = False)

Configure check for a C or C++ libraries “libs”. Searches through the list of libraries, until one is found where the test succeeds. Tests if “func_name” or “call” exists in the library. Note: if it exists in another library the test succeeds anyway! Optional “header” can be defined to include a header file. If not given a default prototype for “func_name” is added. Optional “extra_libs” is a list of library names to be added after “lib_name” in the build command. To be used for libraries that “lib_name” depends on. Optional “call” replaces the call to “func_name” in the test code. It must consist of complete C statements, including a trailing “;”. Both “func_name” and “call” arguments are optional, and in that case, just linking against the libs is tested. “language” should be “C” or “C++” and is used to select the compiler. Default is “C”. Note that this uses the current value of compiler and linker flags, make sure $CFLAGS, $CPPFLAGS and $LIBS are set correctly. Returns an empty string for success, an error message for failure.

SCons.Conftest.CheckMember ( context , aggregate_member , header= None, language= None)

Configure check for a C or C++ member “aggregate_member”. Optional “header” can be defined to include a header file. “language” should be “C” or “C++” and is used to select the compiler. Default is “C”. Note that this uses the current value of compiler and linker flags, make sure $CFLAGS, $CPPFLAGS and $LIBS are set correctly.

Parameters: • aggregate_member – str the member to check. For example, ‘struct tm.tm_gmtoff’.

• includes – str Optional “header” can be defined to include a header file.

• language – str only C and C++ supported.

SCons API Documentation

15 Returns the status (0 or False = Passed, True/non-zero = Failed).

SCons.Conftest.CheckProg ( context , prog_name )

Configure check for a specific program.

Check whether program prog_name exists in path. If it is found, returns the path for it, otherwise returns None.

SCons.Conftest.CheckSHCC ( context )

Configure check for a working shared C compiler.

This checks whether the C compiler, as defined in the $SHCC construction variable, can compile a C source file. It uses the current $SHCCCOM value too, so that it can test against non working flags.

SCons.Conftest.CheckSHCXX ( context )

Configure check for a working shared CXX compiler.

This checks whether the CXX compiler, as defined in the $SHCXX construction variable, can compile a CXX source file. It uses the current $SHCXXCOM value too, so that it can test against non working flags.

SCons.Conftest.CheckType ( context , type_name , fallback= None, header= None, language= None)

Configure check for a C or C++ type “type_name”. Optional “header” can be defined to include a header file. “language” should be “C” or “C++” and is used to select the compiler. Default is “C”. Sets HAVE_type_name in context.havedict according to the result. Note that this uses the current value of compiler and linker flags, make sure $CFLAGS, $CPPFLAGS and $LIBS are set correctly. Returns an empty string for success, an error message for failure.

SCons.Conftest.CheckTypeSize ( context , type_name , header= None, language= None, expect= None)

This check can be used to get the size of a given type, or to check whether the type is of expected size.

Parameters: • type (-) – str the type to check

• includes (-) – sequence list of headers to include in the test code before testing the type

• language (-) – str ‘C’ or ‘C++’

• expect (-) – int if given, will test wether the type has the given number of bytes. If not given, will automatically find the size.

• Returns – statusint0 if the check failed, or the found size of the type if the check succeeded.

SCons.Conftest._Have ( context , key , have , comment= None) → None

Store result of a test in context.havedict and context.headerfilename.

Parameters: • key - is a “HAVE_abc” name. It is turned into all CAPITALS and non-alphanumerics are replaced by an underscore.

• have - value as it should appear in the header file, include quotes when desired and escape special characters!

• comment is the C comment to add above the line defining the symbol (the comment is automatically put inside a /**/). If None, no comment is added.

The value of “have” can be:

• 1 - Feature is defined, add “#define key”.

• 0 - Feature is not defined, add “/*#undef key*/”. Adding “undef” is what autoconf does. Not useful for the compiler, but it shows that the test was done.

• number - Feature is defined to this number “#define key have”. Doesn’t work for 0 or 1, use a string then.

• string - Feature is defined to this string “#define key have”.

SCons.Conftest._LogFailed ( context , text , msg ) → None

Write to the log about a failed program. Add line numbers, so that error messages can be understood.

SCons.Conftest._YesNoResult ( context , ret , key , text , comment= None) → None

Handle the result of a test with a “yes” or “no” result.

SCons API Documentation

16 Parameters: • ret is the return value: empty if OK, error message when not.

• key is the name of the symbol to be defined (HAVE_foo).

• text is the source code of the program used for testing.

• comment is the C comment to add above the line defining the symbol (the comment is automatically put inside a /**/). If None, no comment is added.

SCons.Conftest._check_empty_program ( context , comp , text , language , use_shared: bool = False)

Return 0 on success, 1 otherwise.

SCons.Conftest._lang2suffix ( lang )

Convert a language name to a suffix. When “lang” is empty or None C is assumed. Returns a tuple (lang, suffix, None) when it works. For an unrecognized language returns (None, None, msg).

Where:

• lang = the unified language name

• suffix = the suffix, including the leading dot

• msg = an error message

# SCons.Debug module

Code for debugging SCons internal things.

Shouldn’t be needed by most users. Quick shortcuts:

from SCons.Debug import caller_trace caller_trace()

SCons.Debug.Trace ( msg , tracefile= None, mode: str = 'w', tstamp: bool = False) → None

Write a trace message.

Write messages when debugging which do not interfere with stdout. Useful in tests, which monitor stdout and would break with unexpected output. Trace messages can go to the console (which is opened as a file), or to a disk file; the tracefile argument persists across calls unless overridden.

Parameters: • tracefile – file to write trace message to. If omitted, write to the previous trace file (default: console).

• mode – file open mode (default: ‘w’)

• tstamp – write relative timestamps with trace. Outputs time since scons was started, and time since last trace (default: False)

SCons.Debug._dump_one_caller ( key , file , level: int = 0) → None

SCons.Debug.caller_stack ()

return caller’s stack

SCons.Debug.caller_trace ( back: int = 0) → None

Trace caller stack and save info into global dicts, which are printed automatically at the end of SCons execution.

SCons.Debug.countLoggedInstances ( classes , file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'> ) → None

SCons.Debug.dumpLoggedInstances ( classes , file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'> ) → None

SCons.Debug.dump_caller_counts ( file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'> ) → None

SCons.Debug.fetchLoggedInstances ( classes: str = '*')

SCons.Debug.func_shorten ( func_tuple )

SCons.Debug.listLoggedInstances ( classes , file=<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'> ) → None

SCons.Debug.logInstanceCreation ( instance , name= None) → None

SCons API Documentation

17 SCons.Debug.memory () → int

SCons.Debug.string_to_classes ( s)

# SCons.Defaults module

Builders and other things for the local site.

Here’s where we’ll duplicate the functionality of autoconf until we move it into the installation procedure or use something like qmconf.

The code that reads the registry to find MSVC components was borrowed from distutils.msvccompiler.

SCons.Defaults.DefaultEnvironment ( *args , **kwargs )

Construct the global (“default”) construction environment.

The environment is provisioned with the values from kwargs .

After the environment is created, this function is replaced with a reference to _fetch_DefaultEnvironment() which efficiently returns the initialized default construction environment without checking for its existence.

Historically, some parts of the code held references to this function. Thus it still has the existence check for _default_env rather than just blindly creating the environment and overwriting itself.

class SCons.Defaults.NullCmdGenerator ( cmd )

Bases: object

Callable class for use as a no-effect command generator.

The __call__ method for this class simply returns the thing you instantiated it with. Example usage:

env["DO_NOTHING"] = NullCmdGenerator env["LINKCOM"] = "${DO_NOTHING('$LINK $SOURCES $TARGET')}"

SCons.Defaults.SharedFlagChecker ( source , target , env )

SCons.Defaults.SharedObjectEmitter ( target , source , env )

SCons.Defaults.StaticObjectEmitter ( target , source , env )

class SCons.Defaults.Variable_Method_Caller ( variable , method )

Bases: object

A class for finding a construction variable on the stack and calling one of its methods.

Used to support “construction variables” appearing in string

eval``s that actually stand in for methods--specifically, the use of "RDirs" in a call to :func:`_concat` that should actually execute the``TARGET.RDirs method.

Historical note: This was formerly supported by creating a little “build dictionary” that mapped RDirs to the method, but this got in the way of Memoizing construction environments, because we had to create new environment objects to hold the variables.

SCons.Defaults.__lib_either_version_flag ( env , version_var1 , version_var2 , flags_var )

if $version_var1 or $version_var2 is not empty, returns env[flags_var], otherwise returns None :param env: :param version_var1: :param version_var2: :param flags_var: :return:

SCons.Defaults.__libversionflags ( env , version_var , flags_var )

if version_var is not empty, returns env[flags_var], otherwise returns None :param env: :param version_var: :param flags_var: :return:

SCons.Defaults._concat ( prefix , items_iter , suffix , env , f=<function <lambda>> , target=None ,

source=None , affect_signature: bool = True )

Creates a new list from ‘items_iter’ by first interpolating each element in the list using the ‘env’ dictionary and then calling f on the list, and finally calling_concat_ixes to concatenate ‘prefix’ and ‘suffix’ onto each element of the list.

SCons.Defaults._concat_ixes ( prefix , items_iter , suffix , env )

Creates a new list from ‘items_iter’ by concatenating the ‘prefix’ and ‘suffix’ arguments onto each element of the list. A trailing space on ‘prefix’ or leading space on ‘suffix’ will cause them to be put into separate list elements rather than being concatenated.

SCons.Defaults._defines ( prefix , defs , suffix , env , target=None , source=None , c=<function _concat_ixes> )

A wrapper around _concat_ixes() that turns a list or string into a list of C preprocessor command-line definitions.

SCons.Defaults._fetch_DefaultEnvironment ( *args , **kwargs )

SCons API Documentation

18 Returns the already-created default construction environment.

SCons.Defaults._stripixes ( prefix: str , items , suffix: str , stripprefixes: list[str] ,

stripsuffixes: list[str] , env , literal_prefix: str = '', c: Callable[[list], list] = None) →

list

Returns a list with text added to items after first stripping them.

A companion to _concat_ixes(), used by tools (like the GNU linker) that need to turn something like libfoo.a into

-lfoo . stripprefixes and stripsuffixes are stripped from items . Calls function c to postprocess the result.

Parameters: • prefix – string to prepend to elements

• items – string or iterable to transform

• suffix – string to append to elements

• stripprefixes – prefix string(s) to strip from elements

• stripsuffixes – suffix string(s) to strip from elements

• env – construction environment for variable interpolation

• c – optional function to perform a transformation on the list. The default is None , which will select _concat_ixes().

SCons.Defaults.chmod_func ( dest , mode ) → None

Implementation of the Chmod action function.

mode can be either an integer (normally expressed in octal mode, as in 0o755) or a string following the syntax of the POSIX chmod command (for example “ugo+w”). The latter must be converted, since the underlying Python only takes the numeric form.

SCons.Defaults.chmod_strfunc ( dest , mode ) → str

strfunction for the Chmod action function.

SCons.Defaults.copy_func ( dest , src , symlinks: bool = True) → int

Implementation of the Copy action function.

Copies src to dest . If src is a list, dest must be a directory, or not exist (will be created).

Since Python shutil methods, which know nothing about SCons Nodes, will be called to perform the actual copying, args are converted to strings first.

If symlinks evaluates true, then a symbolic link will be shallow copied and recreated as a symbolic link; otherwise, copying a symbolic link will be equivalent to copying the symbolic link’s final target regardless of symbolic link depth.

SCons.Defaults.copy_strfunc ( dest , src , symlinks: bool = True) → str

strfunction for the Copy action function.

SCons.Defaults.delete_func ( dest , must_exist: bool = False) → None

Implementation of the Delete action function.

Lets the Python os.unlink() raise an error if dest does not exist, unless must_exist evaluates false (the default).

SCons.Defaults.delete_strfunc ( dest , must_exist: bool = False) → str

strfunction for the Delete action function.

SCons.Defaults.get_paths_str ( dest ) → str

Generates a string from dest for use in a strfunction.

If dest is a list, manually converts each elem to a string.

SCons.Defaults.mkdir_func ( dest ) → None

Implementation of the Mkdir action function.

SCons.Defaults.move_func ( dest , src ) → None

Implementation of the Move action function.

SCons.Defaults.processDefines ( defs ) → list [str ]

Return list of strings for preprocessor defines from defs .

Resolves the different forms CPPDEFINES can be assembled in: if the Append/Prepend routines are used beyond a initial setting it will be a deque, but if written to only once (Environment initializer, or direct write) it can be a multitude of types.

Any prefix/suffix is handled elsewhere (usually _concat_ixes()).

Changed in version 4.5.0: Bare tuples are now treated the same as tuple-in-sequence, assumed to describe a valued macro. Bare strings are now split on space. A dictionary is no longer sorted before handling.

SCons.Defaults.touch_func ( dest ) → None

SCons API Documentation

19 Implementation of the Touch action function.

# SCons.Environment module

Base class for construction Environments.

These are the primary objects used to communicate dependency and construction information to the build engine.

Keyword arguments supplied when the construction Environment is created are construction variables used to initialize the Environment.

class SCons.Environment.Base ( platform= None, tools= None, toolpath= None, variables= None,

parse_flags= None, **kw )

Bases: SubstitutionEnvironment

Base class for “real” construction Environments.

These are the primary objects used to communicate dependency and construction information to the build engine.

Keyword arguments supplied when the construction Environment is created are construction variables used to initialize the Environment.

Action ( *args , **kw )

AddMethod ( function , name= None) → None

Adds the specified function as a method of this construction environment with the specified name. If the name is omitted, the default name is the name of the function itself.

AddPostAction ( files , action )

AddPreAction ( files , action )

Alias ( target , source= [], action= None, **kw )

AlwaysBuild ( *targets )

Append ( **kw ) → None

Append values to construction variables in an Environment.

The variable is created if it is not already present.

AppendENVPath ( name , newpath , envname: str = 'ENV', sep= ':', delete_existing: bool = False) →

None

Append path elements to the path name in the envname dictionary for this environment. Will only add any particular path once, and will normpath and normcase all paths to help assure this. This can also handle the case where the env variable is a list instead of a string.

If delete_existing is False, a newpath element already in the path will not be moved to the end (it will be left where it is).

AppendUnique ( delete_existing: bool = False, **kw ) → None

Append values uniquely to existing construction variables.

Similar to Append(), but the result may not contain duplicates of any values passed for each given key (construction variable), so an existing list may need to be pruned first, however it may still contain other duplicates.

If delete_existing is true, removes existing values first, so values move to the end; otherwise (the default) values are skipped if already present.

Builder ( **kw )

CacheDir ( path , custom_class= None) → None

Clean ( targets , files ) → None

Mark additional files for cleaning.

files will be removed if any of targets are selected for cleaning - that is, the combination of target selection and -c clean mode.

Parameters: • targets (files or nodes ) – targets to associate files with.

• files (files or nodes ) – items to remove if targets are selected.

Clone ( tools= [], toolpath= None, variables= None, parse_flags= None, **kw )

Return a copy of a construction Environment.

The copy is like a Python “deep copy”: independent copies are made recursively of each object, except that a reference is copied when an object is not deep-copyable (like a function). There are no references to any mutable objects in the original environment.

Unrecognized keyword arguments are taken as construction variable assignments.

SCons API Documentation

20 Parameters: • tools – list of tools to initialize.

• toolpath – list of paths to search for tools.

• variables – a Variables object to use to populate construction variables from command-line variables.

• parse_flags – option strings to parse into construction variables.

Added in version 4.8.0: The optional variables parameter was added.

Command ( target , source , action , **kw )

Set up a one-off build command.

Builds target from source using action , which may be be any type that the Builder factory will accept for an action. Generates an anonymous builder and calls it, to add the details to the build graph. The builder is not named, added to BUILDERS , or otherwise saved.

Recognizes the Builder() keywords source_scanner , target_scanner , source_factory and

target_factory . All other arguments from kw are passed on to the builder when it is called.

Configure ( *args , **kw )

Decider ( function )

Depends ( target , dependency )

Explicity specify that target depends on dependency .

Detect ( progs )

Return the first available program from one or more possibilities.

Parameters: progs (str or list ) – one or more command names to check for

Dictionary ( *args: str , as_dict: bool = False)

Return construction variables from an environment.

Parameters: • args (optional ) – construction variable names to select. If omitted, all variables are selected and returned as a dict.

• as_dict – if true, and args is supplied, return the variables and their values in a dict. If false (the default), return a single value as a scalar, or multiple values in a list.

Returns: A dictionary of construction variables, or a single value or list of values.

Raises: KeyError – if any of args is not in the construction environment.

Changed in version 4.9.0: Added the as_dict keyword arg to specify always returning a dict.

Dir ( name , *args , **kw )

Dump ( *key: str , format: str = 'pretty') → str

Return string of serialized construction variables.

Produces a “pretty” output of a dictionary of selected construction variables, or all of them. The display format is selectable. The result is intended for human consumption (e.g, to print), mainly when debugging. Objects that cannot directly be represented get a placeholder like <function foo at 0x123456> (pretty-print) or

<<non-serializable: function>> (JSON).

Parameters: • key – variables to format together with their values. If omitted, format the whole dict of variables,

• format – specify the format to serialize to. "pretty" generates a pretty-printed string,

"json" a JSON-formatted string.

Raises: ValueError – format is not a recognized serialization format.

Changed in version 4.9.0: key is no longer limited to a single construction variable name. If key is supplied, a formatted dictionary is generated like the no-arg case - previously a single key displayed just the value.

Entry ( name , *args , **kw )

Environment ( **kw )

Execute ( action , *args , **kw )

Directly execute an action through an Environment

File ( name , *args , **kw )

FindFile ( file , dirs )

SCons API Documentation

21 FindInstalledFiles ()

returns the list of all targets of the Install and InstallAs Builder.

FindIxes ( paths: Sequence[str] , prefix: str , suffix: str ) → str | None

Search paths for a path that has prefix and suffix .

Returns on first match.

Parameters: • paths – the list of paths or nodes.

• prefix – construction variable for the prefix.

• suffix – construction variable for the suffix.

Returns: The matched path or None

FindSourceFiles ( node: str = '.') → list

Return a list of all source files.

Flatten ( sequence )

GetBuildPath ( files )

Glob ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False, exclude= None)

Ignore ( target , dependency )

Ignore a dependency.

Literal ( string )

Local ( *targets )

MergeFlags ( args , unique: bool = True) → None

Merge flags into construction variables.

Merges the flags from args into this construction environent. If args is not a dict, it is first converted to one with flags distributed into appropriate construction variables. See ParseFlags().

As a side effect, if unique is true, a new object is created for each modified construction variable by the loop at the end. This is silently expected by the Override() parse_flags functionality, which does not want to share the list (or whatever) with the environment being overridden.

Parameters: • args – flags to merge

• unique – merge flags rather than appending (default: True). When merging, path variables are retained from the front, other construction variables from the end.

NoCache ( *targets )

Tag target(s) so that it will not be cached.

NoClean ( *targets ) → list

Tag targets to not be removed in clean mode.

Override ( overrides )

Create an override environment from the current environment.

Produces a modified environment where the current variables are overridden by any same-named variables from the overrides dict.

An override is much more efficient than doing Clone() or creating a new Environment because it doesn’t copy the construction environment dictionary, it just wraps the underlying construction environment, and doesn’t even create a wrapper object if there are no overrides.

Using this method is preferred over directly instantiating an OverrideEnvirionment because extra checks are performed, substitution takes place, and there is special handling for a parse_flags keyword argument.

This method is not currently exposed as part of the public API, but is invoked internally when things like builder calls have keyword arguments, which are then passed as overrides here. Some tools also call this explicitly.

Returns: A proxy environment of type OverrideEnvironment. or the current environment if overrides is empty.

ParseConfig ( command , function= None, unique: bool = True)

Parse the result of running a command to update construction vars.

Use function to parse the output of running command in order to modify the current environment.

SCons API Documentation

22 Parameters: • command – a string or a list of strings representing a command and its arguments.

• function – called to process the result of command , which will be passed as args . If

function is omitted or None , MergeFlags() is used. Takes 3 args

(env, args, unique)

• unique – whether no duplicate values are allowed (default true)

ParseDepends ( filename , must_exist= None, only_one: bool = False)

Parse a mkdep-style file for explicit dependencies. This is completely abusable, and should be unnecessary in the “normal” case of proper SCons configuration, but it may help make the transition from a Make hierarchy easier for some people to swallow. It can also be genuinely useful when using a tool that can write a .d file, but for which writing a scanner would be too complicated.

ParseFlags ( *flags ) → dict

Return a dict of parsed flags.

Parse flags and return a dict with the flags distributed into the appropriate construction variable names. The flags are treated as a typical set of command-line flags for a GNU-style toolchain, such as might have been generated by one of the {foo}-config scripts, and used to populate the entries based on knowledge embedded in this method -the choices are not expected to be portable to other toolchains.

If one of the flags strings begins with a bang (exclamation mark), it is assumed to be a command and the rest of the string is executed; the result of that evaluation is then added to the dict.

Platform ( platform )

Precious ( *targets )

Mark targets as precious: do not delete before building.

Prepend ( **kw ) → None

Prepend values to construction variables in an Environment.

The variable is created if it is not already present.

PrependENVPath ( name , newpath , envname: str = 'ENV', sep= ':', delete_existing: bool = True) →

None

Prepend path elements to the path name in the envname dictionary for this environment. Will only add any particular path once, and will normpath and normcase all paths to help assure this. This can also handle the case where the env variable is a list instead of a string.

If delete_existing is False, a newpath component already in the path will not be moved to the front (it will be left where it is).

PrependUnique ( delete_existing: bool = False, **kw ) → None

Prepend values uniquely to existing construction variables.

Similar to Prepend(), but the result may not contain duplicates of any values passed for each given key (construction variable), so an existing list may need to be pruned first, however it may still contain other duplicates.

If delete_existing is true, removes existing values first, so values move to the front; otherwise (the default) values are skipped if already present.

Pseudo ( *targets )

Mark targets as pseudo: must not exist.

PyPackageDir ( modulename )

RemoveMethod ( function ) → None

Removes the specified function’s MethodWrapper from the added_methods list, so we don’t re-bind it when making a clone.

Replace ( **kw ) → None

Replace existing construction variables in an Environment with new construction variables and/or values.

ReplaceIxes ( path , old_prefix , old_suffix , new_prefix , new_suffix )

Replace old_prefix with new_prefix and old_suffix with new_suffix.

env - Environment used to interpolate variables. path - the path that will be modified. old_prefix - construction variable for the old prefix. old_suffix - construction variable for the old suffix. new_prefix - construction variable for the new prefix. new_suffix - construction variable for the new suffix.

Repository ( *dirs , **kw ) → None

Specify Repository directories to search.

Requires ( target , prerequisite )

Specify that prerequisite must be built before target .

SCons API Documentation

23 Creates an order-only relationship, not a full dependency. prerequisite must exist before target can be built, but a change to prerequisite does not trigger a rebuild of target .

SConsignFile ( name= '.sconsign', dbm_module= None) → None

Scanner ( *args , **kw )

SetDefault ( **kw ) → None

SideEffect ( side_effect , target )

Tell scons that side_effects are built as side effects of building targets.

Split ( arg )

This function converts a string or list into a list of strings or Nodes. This makes things easier for users by allowing files to be specified as a white-space separated list to be split.

The input rules are:

• A single string containing names separated by spaces. These will be split apart at the spaces.

• A single Node instance

• A list containing either strings or Node instances. Any strings in the list are not split at spaces.

In all cases, the function returns a list of Nodes and strings.

Tool ( tool: str | Callable , toolpath: Collection[str] | None = None, **kwargs ) → Callable

Find and run tool module tool .

tool is generally a string, but can also be a callable object, in which case it is just called, without any of the setup. The skipped setup includes storing kwargs into the created Tool instance, which is extracted and used when the instance is called, so in the skip case, the called object will not get the kwargs .

Changed in version 4.2: returns the tool object rather than None .

Value ( value , built_value= None, name= None)

Return a Value (Python expression) node.

Changed in version 4.0: the name parameter was added.

VariantDir ( variant_dir , src_dir , duplicate: int = 1) → None

WhereIs ( prog , path= None, pathext= None, reject= None)

Find prog in the path.

__eq__ ( other )

Compare two environments.

This is used by checks in Builder to determine if duplicate targets have environments that would cause the same result. The more reliable way (respecting the admonition to avoid poking at _dict directly) would be to use

Dictionary so this is sure to work even if one or both are are instances of OverrideEnvironment. However an actual SubstitutionEnvironment doesn’t have a Dictionary method That causes problems for unit tests written to excercise SubsitutionEnvironment directly, although nobody else seems to ever instantiate one. We count on OverrideEnvironment to fake the _dict to make things work.

__getattr__ ( name )

Handle missing attribute in an environment.

Assume this is a builder that’s not instantiated, becasue that has been a common failure mode. Could also be a typo. Emit a message about this to try to help. We can’t get too clever, other parts of SCons depend on seeing the AttributeError that triggers this call, so all we do is produce our own message.

Added in version 4.10.0.

_canonicalize ( path )

Allow Dirs and strings beginning with # for top-relative.

Note this uses the current env’s fs (in self).

_changed_build ( dependency , target , prev_ni , repo_node= None) → bool

_changed_content ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_match ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_newer ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_then_content ( dependency , target , prev_ni , repo_node= None) → bool

_find_toolpath_dir ( tp )

_gsm ()

_init_special () → None

Initial the dispatch tables for special handling of special construction variables.

_update ( other ) → None

SCons API Documentation

24 Private method to update an environment’s consvar dict directly.

Bypasses the normal checks that occur when users try to set items.

_update_onlynew ( other ) → None

Private method to add new items to an environment’s consvar dict.

Only adds items from other whose keys do not already appear in the existing dict; values from other are not used for replacement. Bypasses the normal checks that occur when users try to set items.

arg2nodes ( args , node_factory=<class 'SCons.Environment._Null'> , lookup_list=<class 'SCons.Environment._Null'> , **kw )

Converts args to a list of nodes.

Parameters: • just (args - filename strings or nodes to convert; nodes are ) – added to the list without further processing.

• not (node_factory - optional factory to create the nodes; if ) – specified, will use this environment’s fs.File method.

• to (lookup_list - optional list of lookup functions to call ) – attempt to find the file referenced by each args .

• add. (kw - keyword arguments that represent additional nodes to )

backtick ( command ) → str

Emulate command substitution.

Provides behavior conceptually like POSIX Shell notation for running a command in backquotes (backticks) by running command and returning the resulting output string.

This is not really a public API any longer, it is provided for the use of ParseFlags() (which supports it using a syntax of !command) and ParseConfig().

Raises: OSError – if the external command returned non-zero exit status.

get ( key , default= None)

Emulates the get() method of dictionaries.

get_CacheDir ()

get_builder ( name )

Fetch the builder with the specified name from the environment.

get_factory ( factory , default: str = 'File')

Return a factory function for creating Nodes for this construction environment.

get_scanner ( skey )

Find the appropriate scanner given a key (usually a file suffix).

gvars ()

items ()

Emulates the items() method of dictionaries.

keys ()

Emulates the keys() method of dictionaries.

lvars ()

scanner_map_delete ( kw= None) → None

Delete the cached scanner map (if we need to).

setdefault ( key , default= None)

Emulates the setdefault() method of dictionaries.

subst ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None =

None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

subst_kw ( kw , raw: int = 0, target= None, source= None)

subst_list ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Calls through to SCons.Subst.scons_subst_list().

See the documentation for that function.

SCons API Documentation

25 subst_path ( path , target= None, source= None)

Substitute a path list.

Turns EntryProxies into Nodes, leaving Nodes (and other objects) as-is.

subst_target_source ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

validate_CacheDir_class ( custom_class= None)

Validate the passed custom CacheDir class, or if no args are passed, validate the custom CacheDir class from the environment.

values ()

Emulates the values() method of dictionaries.

class SCons.Environment.BuilderDict ( mapping , env )

Bases: UserDict

This is a dictionary-like class used by an Environment to hold the Builders. We need to do this because every time someone changes the Builders in the Environment’s BUILDERS dictionary, we must update the Environment’s attributes.

_abc_impl = <_abc._abc_data object>

clear () → None. Remove all items from D.

copy ()

classmethod fromkeys ( iterable , value= None)

get ( k[, d]) → D[k] if k in D, else d. d defaults to None.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

popitem () → (k, v), remove and return some (key, value) pair

as a 2-tuple; but raise KeyError if D is empty.

setdefault ( k[, d]) → D.get(k,d), also set D[k]=d if k not in D

update ([, E], **F ) → None. Update D from mapping/iterable E and F.

If E present and has a .keys() method, does: for k in E: D[k] = E[k] If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v In either case, this is followed by: for k, v in F.items(): D[k] = v

values () → an object providing a view on D's values

class SCons.Environment.BuilderWrapper ( obj: Any , method: Callable , name: str | None = None)

Bases: MethodWrapper

A MethodWrapper subclass that that associates an environment with a Builder.

This mainly exists to wrap the __call__() function so that all calls to Builders can have their argument lists massaged in the same way (treat a lone argument as the source, treat two arguments as target then source, make sure both target and source are lists) without having to have cut-and-paste code to do it.

As a bit of obsessive backwards compatibility, we also intercept attempts to get or set the “env” or “builder” attributes, which were the names we used before we put the common functionality into the MethodWrapper base class. We’ll keep this around for a while in case people shipped Tool modules that reached into the wrapper (like the Tool/qt.py module does, or did). There shouldn’t be a lot attribute fetching or setting on these, so a little extra work shouldn’t hurt.

clone ( new_object )

Returns an object that re-binds the underlying “method” to the specified new object.

SCons.Environment.NoSubstitutionProxy ( subject )

An entry point for returning a proxy subclass instance that overrides the subst*() methods so they don’t actually perform construction variable substitution. This is specifically intended to be the shim layer in between global function calls (which don’t want construction variable substitution) and the DefaultEnvironment() (which would substitute variables if left to its own devices).

We have to wrap this in a function that allows us to delay definition of the class until it’s necessary, so that when it subclasses Environment it will pick up whatever Environment subclass the wrapper interface might have assigned to SCons.Environment.Environment.

SCons API Documentation

26 class SCons.Environment.OverrideEnvironment ( subject , overrides: dict | None = None)

Bases: Base

A proxy that implements override environments.

Returns attributes/methods and construction variables from the base environment subject , except that same-named construction variables from overrides are returned on read access; assignment to a construction variable creates an override entry - subject is not modified. This is a much lighter weight approach for limited-use setups than cloning an environment, for example to handle a builder call with keyword arguments that make a temporary change to the current environment:

env.Program(target="foo", source=sources, DEBUG=True)

While the majority of methods are proxied from the underlying environment class, enough plumbing is defined in this class for it to behave like an ordinary Environment without the caller needing to know it is “special” in some way. We don’t call the initializer of the class we’re proxying, rather depend on it already being properly set up.

Deletion is handled specially, if a variable was explicitly deleted, it should no longer appear to be in the env, but we also don’t want to modify the subject environment.

OverrideEnvironment can nest arbitratily, subject can be an existing instance. Although instances can be instantiated directly, the expected use is to call the Override() method as a factory.

Note Python does not give us a way to assure the subject environment is not modified. Assigning to a variable creates a new entry in the override, but moditying a variable will first fetch the one from the subject, and if mutable, it will just be modified in place. For example: over_env.Append(CPPDEFINES="-O") , where CPPDEFINES is an existing list or CLVar, will successfully append to CPPDEFINES in the subject env. To avoid such leakage, clients such as Scanners, Emitters and Action functions called by a Builder using override syntax must take care if modifying an env (which is not advised anyway) in case they were passed an OverrideEnvironment .

Action ( *args , **kw )

AddMethod ( function , name= None) → None

Adds the specified function as a method of this construction environment with the specified name. If the name is omitted, the default name is the name of the function itself.

AddPostAction ( files , action )

AddPreAction ( files , action )

Alias ( target , source= [], action= None, **kw )

AlwaysBuild ( *targets )

Append ( **kw ) → None

Append values to construction variables in an Environment.

The variable is created if it is not already present.

AppendENVPath ( name , newpath , envname: str = 'ENV', sep= ':', delete_existing: bool = False) →

None

Append path elements to the path name in the envname dictionary for this environment. Will only add any particular path once, and will normpath and normcase all paths to help assure this. This can also handle the case where the env variable is a list instead of a string.

If delete_existing is False, a newpath element already in the path will not be moved to the end (it will be left where it is).

AppendUnique ( delete_existing: bool = False, **kw ) → None

Append values uniquely to existing construction variables.

Similar to Append(), but the result may not contain duplicates of any values passed for each given key (construction variable), so an existing list may need to be pruned first, however it may still contain other duplicates.

If delete_existing is true, removes existing values first, so values move to the end; otherwise (the default) values are skipped if already present.

Builder ( **kw )

CacheDir ( path , custom_class= None) → None

Clean ( targets , files ) → None

Mark additional files for cleaning.

files will be removed if any of targets are selected for cleaning - that is, the combination of target selection and -c clean mode.

SCons API Documentation

27 Parameters: • targets (files or nodes ) – targets to associate files with.

• files (files or nodes ) – items to remove if targets are selected.

Clone ( tools= [], toolpath= None, variables= None, parse_flags= None, **kw )

Return a copy of a construction Environment.

The copy is like a Python “deep copy”: independent copies are made recursively of each object, except that a reference is copied when an object is not deep-copyable (like a function). There are no references to any mutable objects in the original environment.

Unrecognized keyword arguments are taken as construction variable assignments.

Parameters: • tools – list of tools to initialize.

• toolpath – list of paths to search for tools.

• variables – a Variables object to use to populate construction variables from command-line variables.

• parse_flags – option strings to parse into construction variables.

Added in version 4.8.0: The optional variables parameter was added.

Command ( target , source , action , **kw )

Set up a one-off build command.

Builds target from source using action , which may be be any type that the Builder factory will accept for an action. Generates an anonymous builder and calls it, to add the details to the build graph. The builder is not named, added to BUILDERS , or otherwise saved.

Recognizes the Builder() keywords source_scanner , target_scanner , source_factory and

target_factory . All other arguments from kw are passed on to the builder when it is called.

Configure ( *args , **kw )

Decider ( function )

Depends ( target , dependency )

Explicity specify that target depends on dependency .

Detect ( progs )

Return the first available program from one or more possibilities.

Parameters: progs (str or list ) – one or more command names to check for

Dictionary ( *args , as_dict: bool = False)

Return construction variables from an environment.

Behavior is as described for SubstitutionEnvironment.Dictionary but understanda about the override.

Raises: KeyError – if any of args is not in the construction environment.

Dir ( name , *args , **kw )

Dump ( *key: str , format: str = 'pretty') → str

Return string of serialized construction variables.

Produces a “pretty” output of a dictionary of selected construction variables, or all of them. The display format is selectable. The result is intended for human consumption (e.g, to print), mainly when debugging. Objects that cannot directly be represented get a placeholder like <function foo at 0x123456> (pretty-print) or

<<non-serializable: function>> (JSON).

Parameters: • key – variables to format together with their values. If omitted, format the whole dict of variables,

• format – specify the format to serialize to. "pretty" generates a pretty-printed string,

"json" a JSON-formatted string.

Raises: ValueError – format is not a recognized serialization format.

Changed in version 4.9.0: key is no longer limited to a single construction variable name. If key is supplied, a formatted dictionary is generated like the no-arg case - previously a single key displayed just the value.

Entry ( name , *args , **kw )

Environment ( **kw )

Execute ( action , *args , **kw )

SCons API Documentation

28 Directly execute an action through an Environment

File ( name , *args , **kw )

FindFile ( file , dirs )

FindInstalledFiles ()

returns the list of all targets of the Install and InstallAs Builder.

FindIxes ( paths: Sequence[str] , prefix: str , suffix: str ) → str | None

Search paths for a path that has prefix and suffix .

Returns on first match.

Parameters: • paths – the list of paths or nodes.

• prefix – construction variable for the prefix.

• suffix – construction variable for the suffix.

Returns: The matched path or None

FindSourceFiles ( node: str = '.') → list

Return a list of all source files.

Flatten ( sequence )

GetBuildPath ( files )

Glob ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False, exclude= None)

Ignore ( target , dependency )

Ignore a dependency.

Literal ( string )

Local ( *targets )

MergeFlags ( args , unique: bool = True) → None

Merge flags into construction variables.

Merges the flags from args into this construction environent. If args is not a dict, it is first converted to one with flags distributed into appropriate construction variables. See ParseFlags().

As a side effect, if unique is true, a new object is created for each modified construction variable by the loop at the end. This is silently expected by the Override() parse_flags functionality, which does not want to share the list (or whatever) with the environment being overridden.

Parameters: • args – flags to merge

• unique – merge flags rather than appending (default: True). When merging, path variables are retained from the front, other construction variables from the end.

NoCache ( *targets )

Tag target(s) so that it will not be cached.

NoClean ( *targets ) → list

Tag targets to not be removed in clean mode.

Override ( overrides )

Create an override environment from the current environment.

Produces a modified environment where the current variables are overridden by any same-named variables from the overrides dict.

An override is much more efficient than doing Clone() or creating a new Environment because it doesn’t copy the construction environment dictionary, it just wraps the underlying construction environment, and doesn’t even create a wrapper object if there are no overrides.

Using this method is preferred over directly instantiating an OverrideEnvirionment because extra checks are performed, substitution takes place, and there is special handling for a parse_flags keyword argument.

This method is not currently exposed as part of the public API, but is invoked internally when things like builder calls have keyword arguments, which are then passed as overrides here. Some tools also call this explicitly.

Returns: A proxy environment of type OverrideEnvironment. or the current environment if overrides is empty.

ParseConfig ( command , function= None, unique: bool = True)

Parse the result of running a command to update construction vars.

Use function to parse the output of running command in order to modify the current environment.

SCons API Documentation

29 Parameters: • command – a string or a list of strings representing a command and its arguments.

• function – called to process the result of command , which will be passed as args . If

function is omitted or None , MergeFlags() is used. Takes 3 args

(env, args, unique)

• unique – whether no duplicate values are allowed (default true)

ParseDepends ( filename , must_exist= None, only_one: bool = False)

Parse a mkdep-style file for explicit dependencies. This is completely abusable, and should be unnecessary in the “normal” case of proper SCons configuration, but it may help make the transition from a Make hierarchy easier for some people to swallow. It can also be genuinely useful when using a tool that can write a .d file, but for which writing a scanner would be too complicated.

ParseFlags ( *flags ) → dict

Return a dict of parsed flags.

Parse flags and return a dict with the flags distributed into the appropriate construction variable names. The flags are treated as a typical set of command-line flags for a GNU-style toolchain, such as might have been generated by one of the {foo}-config scripts, and used to populate the entries based on knowledge embedded in this method -the choices are not expected to be portable to other toolchains.

If one of the flags strings begins with a bang (exclamation mark), it is assumed to be a command and the rest of the string is executed; the result of that evaluation is then added to the dict.

Platform ( platform )

Precious ( *targets )

Mark targets as precious: do not delete before building.

Prepend ( **kw ) → None

Prepend values to construction variables in an Environment.

The variable is created if it is not already present.

PrependENVPath ( name , newpath , envname: str = 'ENV', sep= ':', delete_existing: bool = True) →

None

Prepend path elements to the path name in the envname dictionary for this environment. Will only add any particular path once, and will normpath and normcase all paths to help assure this. This can also handle the case where the env variable is a list instead of a string.

If delete_existing is False, a newpath component already in the path will not be moved to the front (it will be left where it is).

PrependUnique ( delete_existing: bool = False, **kw ) → None

Prepend values uniquely to existing construction variables.

Similar to Prepend(), but the result may not contain duplicates of any values passed for each given key (construction variable), so an existing list may need to be pruned first, however it may still contain other duplicates.

If delete_existing is true, removes existing values first, so values move to the front; otherwise (the default) values are skipped if already present.

Pseudo ( *targets )

Mark targets as pseudo: must not exist.

PyPackageDir ( modulename )

RemoveMethod ( function ) → None

Removes the specified function’s MethodWrapper from the added_methods list, so we don’t re-bind it when making a clone.

Replace ( **kw ) → None

Replace existing construction variables in an Environment with new construction variables and/or values.

ReplaceIxes ( path , old_prefix , old_suffix , new_prefix , new_suffix )

Replace old_prefix with new_prefix and old_suffix with new_suffix.

env - Environment used to interpolate variables. path - the path that will be modified. old_prefix - construction variable for the old prefix. old_suffix - construction variable for the old suffix. new_prefix - construction variable for the new prefix. new_suffix - construction variable for the new suffix.

Repository ( *dirs , **kw ) → None

Specify Repository directories to search.

Requires ( target , prerequisite )

Specify that prerequisite must be built before target .

SCons API Documentation

30 Creates an order-only relationship, not a full dependency. prerequisite must exist before target can be built, but a change to prerequisite does not trigger a rebuild of target .

SConsignFile ( name= '.sconsign', dbm_module= None) → None

Scanner ( *args , **kw )

SetDefault ( **kw ) → None

SideEffect ( side_effect , target )

Tell scons that side_effects are built as side effects of building targets.

Split ( arg )

This function converts a string or list into a list of strings or Nodes. This makes things easier for users by allowing files to be specified as a white-space separated list to be split.

The input rules are:

• A single string containing names separated by spaces. These will be split apart at the spaces.

• A single Node instance

• A list containing either strings or Node instances. Any strings in the list are not split at spaces.

In all cases, the function returns a list of Nodes and strings.

Tool ( tool: str | Callable , toolpath: Collection[str] | None = None, **kwargs ) → Callable

Find and run tool module tool .

tool is generally a string, but can also be a callable object, in which case it is just called, without any of the setup. The skipped setup includes storing kwargs into the created Tool instance, which is extracted and used when the instance is called, so in the skip case, the called object will not get the kwargs .

Changed in version 4.2: returns the tool object rather than None .

Value ( value , built_value= None, name= None)

Return a Value (Python expression) node.

Changed in version 4.0: the name parameter was added.

VariantDir ( variant_dir , src_dir , duplicate: int = 1) → None

WhereIs ( prog , path= None, pathext= None, reject= None)

Find prog in the path.

__contains__ ( key ) → bool

Emulates the contains method of dictionaries.

Backfills from the subject environment if key is not in the override and not deleted.

__delitem__ ( key ) → None

Delete key from override.

Makes key not visible in the override. Previously implemented by deleting from overrides and from __subject ,which keeps __getitem__() from filling it back in next time. However, that approach was a form of leak, as the subject environment was modified. So instead we log that it’s deleted and use that to make decisions elsewhere.

__eq__ ( other )

Compare two environments.

This is used by checks in Builder to determine if duplicate targets have environments that would cause the same result. The more reliable way (respecting the admonition to avoid poking at _dict directly) would be to use

Dictionary so this is sure to work even if one or both are are instances of OverrideEnvironment. However an actual SubstitutionEnvironment doesn’t have a Dictionary method That causes problems for unit tests written to excercise SubsitutionEnvironment directly, although nobody else seems to ever instantiate one. We count on OverrideEnvironment to fake the _dict to make things work.

__getitem__ ( key )

Return the visible value of key .

Backfills from the subject env if key doesn’t have an entry in the override, and is not explicity deleted.

_canonicalize ( path )

Allow Dirs and strings beginning with # for top-relative.

Note this uses the current env’s fs (in self).

_changed_build ( dependency , target , prev_ni , repo_node= None) → bool

_changed_content ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_match ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_newer ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_then_content ( dependency , target , prev_ni , repo_node= None) → bool

SCons API Documentation

31 _find_toolpath_dir ( tp )

_gsm ()

_init_special () → None

Initial the dispatch tables for special handling of special construction variables.

_update ( other ) → None

Private method to update an environment’s consvar dict directly.

Bypasses the normal checks that occur when users try to set items.

_update_onlynew ( other ) → None

Update a dict with new keys.

Unlike the .update method, if the key is already present, it is not replaced.

arg2nodes ( args , node_factory=<class 'SCons.Environment._Null'> , lookup_list=<class 'SCons.Environment._Null'> , **kw )

Converts args to a list of nodes.

Parameters: • just (args - filename strings or nodes to convert; nodes are ) – added to the list without further processing.

• not (node_factory - optional factory to create the nodes; if ) – specified, will use this environment’s fs.File method.

• to (lookup_list - optional list of lookup functions to call ) – attempt to find the file referenced by each args .

• add. (kw - keyword arguments that represent additional nodes to )

backtick ( command ) → str

Emulate command substitution.

Provides behavior conceptually like POSIX Shell notation for running a command in backquotes (backticks) by running command and returning the resulting output string.

This is not really a public API any longer, it is provided for the use of ParseFlags() (which supports it using a syntax of !command) and ParseConfig().

Raises: OSError – if the external command returned non-zero exit status.

get ( key , default= None)

Emulates the get method of dictionaries.

Backfills from the subject environment if key is not in the override and not deleted.

get_CacheDir ()

get_builder ( name )

Fetch the builder with the specified name from the environment.

get_factory ( factory , default: str = 'File')

Return a factory function for creating Nodes for this construction environment.

get_scanner ( skey )

Find the appropriate scanner given a key (usually a file suffix).

gvars ()

items ()

Emulates the items method of dictionaries.

keys ()

Emulates the keys method of dictionaries.

lvars ()

scanner_map_delete ( kw= None) → None

Delete the cached scanner map (if we need to).

setdefault ( key , default= None)

Emulates the setdefault method of dictionaries.

subst ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None =

None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

SCons API Documentation

32 subst_kw ( kw , raw: int = 0, target= None, source= None)

subst_list ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Calls through to SCons.Subst.scons_subst_list().

See the documentation for that function.

subst_path ( path , target= None, source= None)

Substitute a path list.

Turns EntryProxies into Nodes, leaving Nodes (and other objects) as-is.

subst_target_source ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

validate_CacheDir_class ( custom_class= None)

Validate the passed custom CacheDir class, or if no args are passed, validate the custom CacheDir class from the environment.

values ()

Emulates the values method of dictionaries.

class SCons.Environment.SubstitutionEnvironment ( **kw )

Bases: object

Base class for different flavors of construction environments.

This class contains a minimal set of methods that handle construction variable expansion and conversion of strings to Nodes, which may or may not be actually useful as a stand-alone class. Which methods ended up in this class is pretty arbitrary right now. They’re basically the ones which we’ve empirically determined are common to the different construction environment subclasses, and most of the others that use or touch the underlying dictionary of construction variables.

Eventually, this class should contain all the methods that we determine are necessary for a “minimal” interface to the build engine. A full “native Python” SCons environment has gotten pretty heavyweight with all of the methods and Tools and construction variables we’ve jammed in there, so it would be nice to have a lighter weight alternative for interfaces that don’t need all of the bells and whistles. (At some point, we’ll also probably rename this class “Base,” since that more reflects what we want this class to become, but because we’ve released comments that tell people to subclass Environment.Base to create their own flavors of construction environment, we’ll save that for a future refactoring when this class actually becomes useful.)

Special note: methods here and in actual child classes might be called via proxy from an OverrideEnvironment, which isn’t in the class inheritance chain. Take care that methods called with a self that’s really an

OverrideEnvironment don’t make bad assumptions.

AddMethod ( function , name= None) → None

Adds the specified function as a method of this construction environment with the specified name. If the name is omitted, the default name is the name of the function itself.

MergeFlags ( args , unique: bool = True) → None

Merge flags into construction variables.

Merges the flags from args into this construction environent. If args is not a dict, it is first converted to one with flags distributed into appropriate construction variables. See ParseFlags().

As a side effect, if unique is true, a new object is created for each modified construction variable by the loop at the end. This is silently expected by the Override() parse_flags functionality, which does not want to share the list (or whatever) with the environment being overridden.

Parameters: • args – flags to merge

• unique – merge flags rather than appending (default: True). When merging, path variables are retained from the front, other construction variables from the end.

Override ( overrides )

Create an override environment from the current environment.

Produces a modified environment where the current variables are overridden by any same-named variables from the overrides dict.

SCons API Documentation

33 An override is much more efficient than doing Clone() or creating a new Environment because it doesn’t copy the construction environment dictionary, it just wraps the underlying construction environment, and doesn’t even create a wrapper object if there are no overrides.

Using this method is preferred over directly instantiating an OverrideEnvirionment because extra checks are performed, substitution takes place, and there is special handling for a parse_flags keyword argument.

This method is not currently exposed as part of the public API, but is invoked internally when things like builder calls have keyword arguments, which are then passed as overrides here. Some tools also call this explicitly.

Returns: A proxy environment of type OverrideEnvironment. or the current environment if overrides is empty.

ParseFlags ( *flags ) → dict

Return a dict of parsed flags.

Parse flags and return a dict with the flags distributed into the appropriate construction variable names. The flags are treated as a typical set of command-line flags for a GNU-style toolchain, such as might have been generated by one of the {foo}-config scripts, and used to populate the entries based on knowledge embedded in this method -the choices are not expected to be portable to other toolchains.

If one of the flags strings begins with a bang (exclamation mark), it is assumed to be a command and the rest of the string is executed; the result of that evaluation is then added to the dict.

RemoveMethod ( function ) → None

Removes the specified function’s MethodWrapper from the added_methods list, so we don’t re-bind it when making a clone.

__eq__ ( other )

Compare two environments.

This is used by checks in Builder to determine if duplicate targets have environments that would cause the same result. The more reliable way (respecting the admonition to avoid poking at _dict directly) would be to use

Dictionary so this is sure to work even if one or both are are instances of OverrideEnvironment. However an actual SubstitutionEnvironment doesn’t have a Dictionary method That causes problems for unit tests written to excercise SubsitutionEnvironment directly, although nobody else seems to ever instantiate one. We count on OverrideEnvironment to fake the _dict to make things work.

_init_special () → None

Initial the dispatch tables for special handling of special construction variables.

arg2nodes ( args , node_factory=<class 'SCons.Environment._Null'> , lookup_list=<class 'SCons.Environment._Null'> , **kw )

Converts args to a list of nodes.

Parameters: • just (args - filename strings or nodes to convert; nodes are ) – added to the list without further processing.

• not (node_factory - optional factory to create the nodes; if ) – specified, will use this environment’s fs.File method.

• to (lookup_list - optional list of lookup functions to call ) – attempt to find the file referenced by each args .

• add. (kw - keyword arguments that represent additional nodes to )

backtick ( command ) → str

Emulate command substitution.

Provides behavior conceptually like POSIX Shell notation for running a command in backquotes (backticks) by running command and returning the resulting output string.

This is not really a public API any longer, it is provided for the use of ParseFlags() (which supports it using a syntax of !command) and ParseConfig().

Raises: OSError – if the external command returned non-zero exit status.

get ( key , default= None)

Emulates the get() method of dictionaries.

gvars ()

items ()

Emulates the items() method of dictionaries.

SCons API Documentation

34 keys ()

Emulates the keys() method of dictionaries.

lvars ()

setdefault ( key , default= None)

Emulates the setdefault() method of dictionaries.

subst ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None =

None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

subst_kw ( kw , raw: int = 0, target= None, source= None)

subst_list ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Calls through to SCons.Subst.scons_subst_list().

See the documentation for that function.

subst_path ( path , target= None, source= None)

Substitute a path list.

Turns EntryProxies into Nodes, leaving Nodes (and other objects) as-is.

subst_target_source ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

values ()

Emulates the values() method of dictionaries.

class SCons.Environment._Null

Bases: object

SCons.Environment._add_cppdefines ( env_dict: dict , val , prepend: bool = False, unique: bool =

False, delete_existing: bool = False) → None

Adds to CPPDEFINES , using the rules for C preprocessor macros.

This is split out from regular construction variable addition because these entries can express either a macro with a replacement value or one without. A macro with replacement value can be supplied as val in three ways: as a combined string "name=value" ; as a tuple (name, value) , or as an entry in a dictionary {"name": value} . A list argument with multiple macros can also be given.

Additions can be unconditional (duplicates allowed) or uniquing (no dupes).

Note if a replacement value is supplied, unique requires a full match to decide uniqueness - both the macro name and the replacement. The inner _is_in() is used to figure that out.

Parameters: • env_dict – the dictionary containing the CPPDEFINES to be modified.

• val – the value to add, can be string, sequence or dict

• prepend – whether to put val in front or back.

• unique – whether to add val if it already exists.

• delete_existing – if unique is true, add val after removing previous.

Added in version 4.5.0.

SCons.Environment._del_SCANNERS ( env , key ) → None

SCons.Environment._delete_duplicates ( l, keep_last )

Delete duplicates from a sequence, keeping the first or last.

SCons.Environment._null

alias of _Null

SCons.Environment._set_BUILDERS ( env , key , value )

SCons.Environment._set_SCANNERS ( env , key , value ) → None

SCons.Environment._set_future_reserved ( env , key , value ) → None

SCons API Documentation

35 SCons.Environment._set_reserved ( env , key , value ) → None

SCons.Environment.alias_builder ( env , target , source ) → None

SCons.Environment.apply_tools ( env , tools , toolpath ) → None

SCons.Environment.copy_non_reserved_keywords ( dict )

SCons.Environment.default_copy_from_cache ( env , src , dst )

SCons.Environment.default_copy_to_cache ( env , src , dst )

SCons.Environment.default_decide_source ( dependency , target , prev_ni , repo_node= None)

SCons.Environment.default_decide_target ( dependency , target , prev_ni , repo_node= None)

# SCons.Errors module

SCons exception classes.

Used to handle internal and user errors in SCons.

exception SCons.Errors.BuildError ( node= None, errstr: str = 'Unknown error', status: int = 2,

exitstatus: int = 2, filename= None, executor: Executor | None = None, action= None,

command= None, exc_info= (None, None, None))

Bases: Exception

SCons Errors that can occur while building.

A BuildError exception contains information both about the erorr itself, and what caused the error.

Variables: • node – ( cause ) the error occurred while building this target node(s)

• errstr – ( info ) a description of the error message

• status – ( info ) the return code of the action that caused the build error. Must be set to a non-zero value even if the build error is not due to an action returning a non-zero returned code.

• exitstatus – ( info ) SCons exit status due to this build error. Must be nonzero unless due to an explicit Exit() call. Not always the same as status , since actions return a status code that should be respected, but SCons typically exits with 2 irrespective of the return value of the failed action.

• filename – ( info ) The name of the file or directory that caused the build error. Set to None

if no files are associated with this error. This might be different from the target being built. For example, failure to create the directory in which the target file will appear. It can be

None if the error is not due to a particular filename.

• executor – ( cause ) the executor that caused the build to fail (might be None if the build failures is not due to the executor failing)

• action – ( cause ) the action that caused the build to fail (might be None if the build failures is not due to the an action failure)

• command – ( cause ) the command line for the action that caused the build to fail (might be None if the build failures is not due to the an action failure)

• exc_info – (info ) Info about exception that caused the build error. Set to

(None, None, None) if this build error is not due to an exception.

exception SCons.Errors.ExplicitExit ( node= None, status= None, *args )

Bases: Exception

exception SCons.Errors.InternalError

Bases: Exception

exception SCons.Errors.MSVCError

Bases: OSError

exception SCons.Errors.SConsEnvironmentError

Bases: Exception

exception SCons.Errors.StopError

Bases: Exception

exception SCons.Errors.UserError

SCons API Documentation

36 Bases: Exception

SCons.Errors.convert_to_BuildError ( status , exc_info= None)

Convert a return code to a BuildError Exception.

The buildError.status we set here will normally be used as the exit status of the “scons” process.

Parameters: • status – can either be a return code or an Exception.

• exc_info (tuple, optional ) – explicit exception information.

# SCons.Executor module

Execute actions with specific lists of target and source Nodes.

SCons.Executor.AddBatchExecutor ( key: str , executor: Executor ) → None

class SCons.Executor.Batch ( targets= [], sources= [])

Bases: object

Remembers exact association between targets and sources of executor.

sources

targets

class SCons.Executor.Executor ( action , env= None, overridelist= [{}], targets= [], sources= [],

builder_kw= {})

Bases: object

A class for controlling instances of executing an action.

This largely exists to hold a single association of an action, environment, list of environment override dictionaries, targets and sources for later processing as needed.

_do_execute

_execute_str

_get_changed_sources ( *args , **kw )

_get_changed_targets ( *args , **kw )

_get_changes () → None

Populate all the changed/unchanged lists.

Changed in version 4.10.0: _changed_sources , _changed_targets , _unchanged_sources and

_unchanged_targets are no longer separate instance attributes, but rather saved in the _memo dict.

_get_source ( *args , **kw )

_get_sources ( *args , **kw )

_get_target ( *args , **kw )

_get_targets ( *args , **kw )

_get_unchanged_sources ( *args , **kw )

_get_unchanged_targets ( *args , **kw )

_get_unignored_sources_key ( node , ignore= ())

_memo

action_list

add_batch ( targets , sources ) → None

Add pair of associated target and source to this Executor’s list. This is necessary for “batch” Builders that can be called repeatedly to build up a list of matching target and source files that will be used in order to update multiple target files at once from multiple corresponding source files, for tools like MSVC that support it.

add_post_action ( action ) → None

add_pre_action ( action ) → None

add_sources ( sources ) → None

Add source files to this Executor’s list. This is necessary for “multi” Builders that can be called repeatedly to build up a source file list for a given target.

batches

builder_kw

cleanup () → None

env

get_action_list ()

get_action_side_effects ()

Returns all side effects for all batches of this Executor used by the underlying Action.

SCons API Documentation

37 get_action_targets ()

get_all_children ()

Returns all unique children (dependencies) for all batches of this Executor.

The Taskmaster can recognize when it’s already evaluated a Node, so we don’t have to make this list unique for its intended canonical use case, but we expect there to be a lot of redundancy (long lists of batched .cc files #including the same .h files over and over), so removing the duplicates once up front should save the Taskmaster a lot of work.

get_all_prerequisites ()

Returns all unique (order-only) prerequisites for all batches of this Executor.

get_all_sources ()

Returns all sources for all batches of this Executor.

get_all_targets ()

Returns all targets for all batches of this Executor.

get_build_env ()

Fetch or create the appropriate build Environment for this Executor.

get_build_scanner_path ( scanner )

Fetch the scanner path for this executor’s targets and sources.

get_contents ()

Fetch the signature contents. This is the main reason this class exists, so we can compute this once and cache it regardless of how many target or source Nodes there are.

Returns bytes

get_implicit_deps ()

Return the executor’s implicit dependencies, i.e. the nodes of the commands to be executed.

get_kw ( kw= {})

get_lvars ()

get_sources ()

get_timestamp () → int

Fetch a time stamp for this Executor. We don’t have one, of course (only files do), but this is the interface used by the timestamp module.

get_unignored_sources ( node , ignore= ())

lvars

nullify () → None

overridelist

post_actions

pre_actions

prepare ()

Preparatory checks for whether this Executor can go ahead and (try to) build its targets.

scan ( scanner , node_list ) → None

Scan a list of this Executor’s files (targets or sources) for implicit dependencies and update all of the targets with them. This essentially short-circuits an N*M scan of the sources for each individual target, which is a hell of a lot more efficient.

scan_sources ( scanner ) → None

scan_targets ( scanner ) → None

set_action_list ( action )

SCons.Executor.GetBatchExecutor ( key: str ) → Executor

class SCons.Executor.Null ( *args , **kw )

Bases: object

A null Executor, with a null build Environment, that does nothing when the rest of the methods call it.

This might be able to disappear when we refactor things to disassociate Builders from Nodes entirely, so we’re not going to worry about unit tests for this–at least for now.

Note the slots have to match Executor exactly, or the _morph() will fail.

_do_execute

_execute_str

_memo

_morph () → None

Morph this Null executor to a real Executor object.

SCons API Documentation

38 action_list

add_post_action ( action ) → None

add_pre_action ( action ) → None

batches

builder_kw

cleanup () → None

env

get_action_list ()

get_action_side_effects ()

get_action_targets ()

get_all_children ()

get_all_prerequisites ()

get_all_sources ()

get_all_targets ()

get_build_env ()

get_build_scanner_path ()

get_contents () → str

get_unignored_sources ( *args , **kw )

lvars

overridelist

post_actions

pre_actions

prepare () → None

set_action_list ( action ) → None

class SCons.Executor.NullEnvironment ( *args , **kwargs )

Bases: Null

SCons = <module 'SCons' from '/Users/bdbaddog/devel/scons/git/as_scons/SCons/__init__.py'>

_CacheDir = <SCons.CacheDir.CacheDir object>

_CacheDir_path = None

get_CacheDir ()

class SCons.Executor.TSList ( func )

Bases: UserList

A class that implements $TARGETS or $SOURCES expansions by wrapping an executor Method. This class is used in the Executor.lvars() to delay creation of NodeList objects until they’re needed.

Note that we subclass collections.UserList purely so that the is_Sequence() function will identify an object of this class as a list during variable expansion. We’re not really using any collections.UserList methods in practice.

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

SCons API Documentation

39 class SCons.Executor.TSObject ( func )

Bases: object

A class that implements $TARGET or $SOURCE expansions by wrapping an Executor method.

SCons.Executor.execute_action_list ( obj , target , kw )

Actually execute the action list.

SCons.Executor.execute_actions_str ( obj )

SCons.Executor.execute_nothing ( obj , target , kw ) → int

SCons.Executor.execute_null_str ( obj ) → str

SCons.Executor.get_NullEnvironment ()

Use singleton pattern for Null Environments.

SCons.Executor.rfile ( node )

A function to return the results of a Node’s rfile() method, if it exists, and the Node itself otherwise (if it’s a Value Node, e.g.).

# SCons.Memoize module

Decorator-based memoizer to count caching stats.

A decorator-based implementation to count hits and misses of the computed values that various methods cache in memory.

Use of this modules assumes that wrapped methods be coded to cache their values in a consistent way. In particular, it requires that the class uses a dictionary named “_memo” to store the cached values.

Here is an example of wrapping a method that returns a computed value, with no input parameters:

@SCons.Memoize.CountMethodCall def foo(self): try: # Memoization return self._memo['foo'] # Memoization except KeyError: # Memoization pass # Memoization result = self.compute_foo_value() self._memo['foo'] = result # Memoization return result

Here is an example of wrapping a method that will return different values based on one or more input arguments:

def _bar_key(self, argument): # Memoization return argument # Memoization @SCons.Memoize.CountDictCall(_bar_key) def bar(self, argument): memo_key = argument # Memoization try: # Memoization memo_dict = self._memo['bar'] # Memoization except KeyError: # Memoization memo_dict = {} # Memoization self._memo['dict'] = memo_dict # Memoization else: # Memoization try: # Memoization return memo_dict[memo_key] # Memoization

SCons API Documentation

40 except KeyError: # Memoization pass # Memoization result = self.compute_bar_value(argument) memo_dict[memo_key] = result # Memoization return result

Deciding what to cache is tricky, because different configurations can have radically different performance tradeoffs, and because the tradeoffs involved are often so non-obvious. Consequently, deciding whether or not to cache a given method will likely be more of an art than a science, but should still be based on available data from this module. Here are some VERY GENERAL guidelines about deciding whether or not to cache return values from a method that’s being called a lot:

– The first question to ask is, “Can we change the calling code

so this method isn’t called so often?” Sometimes this can be done by changing the algorithm. Sometimes the

caller should be memoized, not the method you’re looking at. The memoized function should be timed with multiple configurations to make sure it doesn’t inadvertently slow down some other configuration.

– When memoizing values based on a dictionary key composed of

input arguments, you don’t need to use all of the arguments if some of them don’t affect the return values.

class SCons.Memoize.CountDict ( cls_name , method_name , keymaker )

Bases: Counter

A counter class for memoized values stored in a dictionary, with keys based on the method’s input arguments.

A CountDict object is instantiated in a decorator for each of the class’s methods that memoizes its return value in a dictionary, indexed by some key that can be computed from one or more of its input arguments.

count ( *args , **kw ) → None

Counts whether the computed key value is already present in the memoization dictionary (a hit) or not (a miss).

display () → None

key ()

SCons.Memoize.CountDictCall ( keyfunc )

Decorator for counting memoizer hits/misses while accessing dictionary values with a key-generating function. Like CountMethodCall above, it wraps the given method fn and uses a CountDict object to keep track of the caching statistics. The dict-key function keyfunc has to get passed in the decorator call and gets stored in the CountDict instance. Wrapping gets enabled by calling EnableMemoization().

SCons.Memoize.CountMethodCall ( fn )

Decorator for counting memoizer hits/misses while retrieving a simple value in a class method. It wraps the given method fn and uses a CountValue object to keep track of the caching statistics. Wrapping gets enabled by calling EnableMemoization().

class SCons.Memoize.CountValue ( cls_name , method_name )

Bases: Counter

A counter class for simple, atomic memoized values.

A CountValue object should be instantiated in a decorator for each of the class’s methods that memoizes its return value by simply storing the return value in its _memo dictionary.

count ( *args , **kw ) → None

Counts whether the memoized value has already been set (a hit) or not (a miss).

display () → None

key ()

class SCons.Memoize.Counter ( cls_name , method_name )

Bases: object

Base class for counting memoization hits and misses.

We expect that the initialization in a matching decorator will fill in the correct class name and method name that represents the name of the function being counted.

SCons API Documentation

41 display () → None

key ()

SCons.Memoize.Dump ( title= None) → None

Dump the hit/miss count for all the counters collected so far.

SCons.Memoize.EnableMemoization () → None

# SCons.PathList module

Handle lists of directory paths.

These are the path lists that get set as CPPPATH , LIBPATH , etc.) with as much caching of data and efficiency as we can, while still keeping the evaluation delayed so that we Do the Right Thing (almost) regardless of how the variable is specified.

SCons.PathList.PathList ( pathlist , split= True)

Entry point for getting PathLists.

Returns the cached _PathList object for the specified pathlist, creating and caching a new object as necessary.

class SCons.PathList._PathList ( pathlist , split= True)

Bases: object

An actual PathList object.

Initializes a PathList object, canonicalizing the input and pre-processing it for quicker substitution later.

The stored representation of the PathList is a list of tuples containing (type, value), where the “type” is one of the

TYPE_* variables defined above. We distinguish between:

• Strings that contain no $ and therefore need no delayed-evaluation string substitution (we expect that there will be many of these and that we therefore get a pretty big win from avoiding string substitution)

• Strings that contain $ and therefore need substitution (the hard case is things like ${TARGET.dir}/include ,which require re-evaluation for every target + source)

• Other objects (which may be something like an EntryProxy that needs a method called to return a Node)

Pre-identifying the type of each element in the PathList up-front and storing the type in the list of tuples is intended to reduce the amount of calculation when we actually do the substitution over and over for each target.

subst_path ( env , target , source )

Performs construction variable substitution on a pre-digested PathList for a specific target and source.

SCons.PathList.node_conv ( obj )

This is the “string conversion” routine that we have our substitutions use to return Nodes, not strings. This relies on the fact that an EntryProxy object has a get() method that returns the underlying Node that it wraps, which is a bit of architectural dependence that we might need to break or modify in the future in response to additional requirements.

# SCons.SConf module

Autoconf-like configuration support.

In other words, SConf allows to run tests on the build machine to detect capabilities of system and do some things based on result: generate config files, header files for C/C++, update variables in environment.

Tests on the build system can detect if compiler sees header files, if libraries are installed, if some command line options are supported etc.

SCons.SConf.CheckCC ( context ) → bool

SCons.SConf.CheckCHeader ( context , header , include_quotes: str = '""')

A test for a C header file.

SCons.SConf.CheckCXX ( context ) → bool

SCons.SConf.CheckCXXHeader ( context , header , include_quotes: str = '""')

A test for a C++ header file.

class SCons.SConf.CheckContext ( sconf )

Bases: object

Provides a context for configure tests. Defines how a test writes to the screen and log file.

A typical test is just a callable with an instance of CheckContext as first argument:

SCons API Documentation

42 def CheckCustom(context, …):

context.Message(‘Checking my weird test … ‘) ret = myWeirdTestFunction(…) context.Result(ret)

Often, myWeirdTestFunction will be one of context.TryCompile/context.TryLink/context.TryRun. The results of those are cached, for they are only rebuild, if the dependencies have changed.

AppendLIBS ( lib_name_list , unique: bool = False)

BuildProg ( text , ext ) → bool

CompileProg ( text , ext ) → bool

CompileSharedObject ( text , ext ) → bool

Display ( msg ) → None

Log ( msg ) → None

Message ( text ) → None

Inform about what we are doing right now, e.g. ‘Checking for SOMETHING … ‘

PrependLIBS ( lib_name_list , unique: bool = False)

Result ( res ) → None

Inform about the result of the test. If res is not a string, displays ‘yes’ or ‘no’ depending on whether res is evaluated as true or false. The result is only displayed when self.did_show_result is not set.

RunProg ( text , ext )

SetLIBS ( val )

TryAction ( *args , **kw )

TryBuild ( *args , **kw )

TryCompile ( *args , **kw )

TryLink ( *args , **kw )

TryRun ( *args , **kw )

SCons.SConf.CheckDeclaration ( context , declaration , includes: str = '', language= None) → bool

SCons.SConf.CheckFunc ( context , function_name , header= None, language= None, funcargs= None) → bool

SCons.SConf.CheckHeader ( context , header , include_quotes: str = '<>', language= None) → bool

A test for a C or C++ header file.

SCons.SConf.CheckLib ( context , library= None, symbol: str = 'main', header= None, language= None,

extra_libs= None, autoadd: bool = True, append: bool = True, unique: bool = False) → bool

A test for a library. See also CheckLibWithHeader(). Note that library may also be None to test whether the given symbol compiles without flags.

Changed in version 4.9.0: Added the extra_libs keyword parameter. The actual implementation is in SCons.Conftest.CheckLib() which already accepted this parameter, so this is only exposing existing functionality.

SCons.SConf.CheckLibWithHeader ( context , libs , header , language , extra_libs= None, call= None,

autoadd: bool = True, append: bool = True, unique: bool = False) → bool

Another (more sophisticated) test for a library. Checks, if library and header is available for language (may be ‘C’ or ‘CXX’). Call maybe be a valid expression _with_ a trailing ‘;’. As in CheckLib(), we support library=None, to test if the call compiles without extra link flags.

Changed in version 4.9.0: Added the extra_libs keyword parameter. The actual implementation is in SCons.Conftest.CheckLib() which already accepted this parameter, so this is only exposing existing functionality.

SCons.SConf.CheckMember ( context , aggregate_member , header= None, language= None) → bool

Returns the status (False : failed, True : ok).

SCons.SConf.CheckProg ( context , prog_name )

Simple check if a program exists in the path. Returns the path for the application, or None if not found.

SCons.SConf.CheckSHCC ( context ) → bool

SCons.SConf.CheckSHCXX ( context ) → bool

SCons.SConf.CheckType ( context , type_name , includes: str = '', language= None) → bool

SCons.SConf.CheckTypeSize ( context , type_name , includes: str = '', language= None, expect= None)

exception SCons.SConf.ConfigureCacheError ( target )

Bases: SConfError

Raised when a use explicitely requested the cache feature, but the test is run the first time.

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

SCons API Documentation

43 exception SCons.SConf.ConfigureDryRunError ( target )

Bases: SConfError

Raised when a file or directory needs to be updated during a Configure process, but the user requested a dry-run

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

SCons.SConf.CreateConfigHBuilder ( env ) → None

Called if necessary just before the building targets phase begins.

SCons.SConf.NeedConfigHBuilder () → bool

SCons.SConf.SConf ( *args , **kw )

class SCons.SConf.SConfBase ( env , custom_tests= {}, conf_dir: str = '$CONFIGUREDIR', log_file: str = '$CONFIGURELOG', config_h= None,_depth: int = 0)

Bases: object

This is simply a class to represent a configure context. After creating a SConf object, you can call any tests. After finished with your tests, be sure to call the Finish() method, which returns the modified environment. Some words about caching: In most cases, it is not necessary to cache Test results explicitly. Instead, we use the scons dependency checking mechanism. For example, if one wants to compile a test program (SConf.TryLink), the compiler is only called, if the program dependencies have changed. However, if the program could not be compiled in a former SConf run, we need to explicitly cache this error.

AddTest ( test_name , test_instance ) → None

Adds test_class to this SConf instance. It can be called with self.test_name(…)

AddTests ( tests ) → None

Adds all the tests given in the tests dictionary to this SConf instance

BuildNodes ( nodes )

Tries to build the given nodes immediately. Returns 1 on success, 0 on error.

Define ( name , value= None, comment= None) → None

Define a pre processor symbol name, with the optional given value in the current config header.

If value is None (default), then #define name is written. If value is not none, then #define name value is written.

comment is a string which will be put as a C comment in the header, to explain the meaning of the value (appropriate C comments will be added automatically).

Finish ()

Call this method after finished with your tests: env = sconf.Finish()

class TestWrapper ( test , sconf )

Bases: object

A wrapper around Tests (to ensure sanity)

TryAction ( action , text= None, extension: str = '')

Tries to execute the given action with optional source file contents <text> and optional source file extension <extension>, Returns the status (0 : failed, 1 : ok) and the contents of the output file.

TryBuild ( builder , text= None, extension: str = '')

Low level TryBuild implementation. Normally you don’t need to call that - you can use TryCompile / TryLink / TryRun instead

TryCompile ( text , extension )

Compiles the program given in text to an env.Object, using extension as file extension (e.g. ‘.c’). Returns 1, if compilation was successful, 0 otherwise. The target is saved in self.lastTarget (for further processing).

TryLink ( text , extension )

Compiles the program given in text to an executable env.Program, using extension as file extension (e.g. ‘.c’). Returns 1, if compilation was successful, 0 otherwise. The target is saved in self.lastTarget (for further processing).

TryRun ( text , extension )

Compiles and runs the program given in text, using extension as file extension (e.g. ‘.c’). Returns (1, outputStr) on success, (0, ‘’) otherwise. The target (a file containing the program’s stdout) is saved in self.lastTarget (for further processing).

_createDir ( node )

_shutdown ()

Private method. Reset to non-piped spawn

SCons API Documentation

44 _startup () → None

Private method. Set up logstream, and set the environment variables necessary for a piped build

pspawn_wrapper ( sh , escape , cmd , args , env )

Wrapper function for handling piped spawns.

This looks to the calling interface (in Action.py) like a “normal” spawn, but associates the call with the PSPAWN variable from the construction environment and with the streams to which we want the output logged. This gets slid into the construction environment as the SPAWN variable so Action.py doesn’t have to know or care whether it’s spawning a piped command or not.

class SCons.SConf.SConfBuildInfo

Bases: FileBuildInfo

Special build info for targets of configure tests. Additional members are result (did the builder succeed last time?) and string, which contains messages of the original build phase.

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state.

bact

bactsig : str | None

bdepends

bdependsigs : list [BuildInfoBase ]

bimplicit

bimplicitsigs : list [BuildInfoBase ]

bsources

bsourcesigs : list [BuildInfoBase ]

convert_from_sconsign ( dir , name ) → None

Converts a newly-read FileBuildInfo object for in-SCons use

For normal up-to-date checking, we don’t have any conversion to perform–but we’re leaving this method here to make that clear.

convert_to_sconsign () → None

Converts this FileBuildInfo object for writing to a .sconsign file

This replaces each Node in our various dependency lists with its usual string representation: relative to the top-level SConstruct directory, or an absolute path if it’s outside.

current_version_id = 2

dependency_map

format ( names: int = 0)

merge ( other: BuildInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

prepare_dependencies () → None

Prepares a FileBuildInfo object for explaining what changed

The bsources, bdepends and bimplicit lists have all been stored on disk as paths relative to the top-level SConstruct directory. Convert the strings to actual Nodes (for use by the –debug=explain code and –implicit-cache).

result

set_build_result ( result , string ) → None

string

class SCons.SConf.SConfBuildTask ( tm , targets , top , node )

Bases: AlwaysTask

This is almost the same as SCons.Script.BuildTask. Handles SConfErrors correctly and knows about the current cache_mode.

LOGGER = None

_abc_impl = <_abc._abc_data object>

_exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

SCons API Documentation

45 _no_exception_to_raise () → None

collect_node_states () → tuple [bool , bool , bool ]

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

display_cached_string ( bi ) → None

Logs the original builder messages, given the SConfBuildInfo instance bi.

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute ()

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

executed () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed ()

Default action when a task fails: stop the build.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

get_target ()

Fetch the target being built or updated by this task.

make_ready () → None

SCons API Documentation

46 Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current () → None

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

needs_execute () → bool

Always returns True (indicating this Task should always be executed).

Subclasses that need this behavior (as opposed to the default of only executing Nodes that are out of date w.r.t. their dependencies) can use this as follows:

class MyTaskSubclass(SCons.Taskmaster.Task):

needs_execute = SCons.Taskmaster.AlwaysTask.needs_execute

non_sconf_nodes = {}

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare () → None

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

trace_message ( node , description: str = 'node') → None

exception SCons.SConf.SConfError ( msg )

Bases: UserError

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

exception SCons.SConf.SConfWarning

Bases: SConsWarning

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

SCons.SConf.SetBuildType ( buildtype ) → None

SCons.SConf.SetCacheMode ( mode )

Set the Configure cache mode. mode must be one of “auto”, “force”, or “cache”.

SCons.SConf.SetProgressDisplay ( display ) → None

Set the progress display to use (called from SCons.Script)

class SCons.SConf.Streamer ( orig )

Bases: object

‘Sniffer’ for a file-like writable object. Similar to the unix tool tee.

flush () → None

getvalue ()

Return everything written to orig since the Streamer was created.

write ( str ) → None

writelines ( lines ) → None

SCons.SConf._createConfigH ( target , source , env ) → None

SCons.SConf._createSource ( target , source , env ) → None

SCons API Documentation

47 SCons.SConf._set_conftest_node ( node ) → None

SCons.SConf._stringConfigH ( target , source , env )

SCons.SConf._stringSource ( target , source , env )

SCons.SConf.createIncludesFromHeaders ( headers , leaveLast , include_quotes: str = '""')

# SCons.SConsign module

Operations on signature database files (.sconsign).

class SCons.SConsign.Base

Bases: object

This is the controlling class for the signatures for the collection of entries associated with a specific directory. The actual directory association will be maintained by a subclass that is specific to the underlying storage method. This class provides a common set of methods for fetching and storing the individual bits of information that make up signature entry.

do_not_set_entry ( filename , obj ) → None

do_not_store_info ( filename , node ) → None

get_entry ( filename )

Fetch the specified entry attribute.

merge () → None

set_entry ( filename , obj ) → None

Set the entry.

store_info ( filename , node ) → None

class SCons.SConsign.DB ( dir )

Bases: Base

A Base subclass that reads and writes signature information from a global .sconsign.db* file–the actual file suffix is determined by the database module.

do_not_set_entry ( filename , obj ) → None

do_not_store_info ( filename , node ) → None

get_entry ( filename )

Fetch the specified entry attribute.

merge () → None

set_entry ( filename , obj ) → None

Set the entry.

store_info ( filename , node ) → None

write ( sync: int = 1) → None

class SCons.SConsign.Dir ( fp= None, dir= None)

Bases: Base

do_not_set_entry ( filename , obj ) → None

do_not_store_info ( filename , node ) → None

get_entry ( filename )

Fetch the specified entry attribute.

merge () → None

set_entry ( filename , obj ) → None

Set the entry.

store_info ( filename , node ) → None

class SCons.SConsign.DirFile ( dir )

Bases: Dir

Encapsulates reading and writing a per-directory .sconsign file.

do_not_set_entry ( filename , obj ) → None

do_not_store_info ( filename , node ) → None

get_entry ( filename )

Fetch the specified entry attribute.

merge () → None

set_entry ( filename , obj ) → None

Set the entry.

store_info ( filename , node ) → None

SCons API Documentation

48 write ( sync: int = 1) → None

Write the .sconsign file to disk.

Try to write to a temporary file first, and rename it if we succeed. If we can’t write to the temporary file, it’s probably because the directory isn’t writable (and if so, how did we build anything in this directory, anyway?), so try to write directly to the .sconsign file as a backup. If we can’t rename, try to copy the temporary contents back to the .sconsign file. Either way, always try to remove the temporary file at the end.

SCons.SConsign.File ( name , dbm_module= None) → None

Arrange for all signatures to be stored in a global .sconsign.db* file.

SCons.SConsign.ForDirectory

alias of DB

SCons.SConsign.Get_DataBase ( dir )

SCons.SConsign.Reset () → None

Reset global state. Used by unit tests that end up using SConsign multiple times to get a clean slate for each test.

class SCons.SConsign.SConsignEntry

Bases: object

Wrapper class for the generic entry in a .sconsign file. The Node subclass populates it with attributes as it pleases.

XXX As coded below, we do expect a ‘.binfo’ attribute to be added, but we’ll probably generalize this in the next refactorings.

binfo

convert_from_sconsign ( dir , name ) → None

convert_to_sconsign () → None

current_version_id = 2

ninfo

SCons.SConsign.corrupt_dblite_warning ( filename ) → None

SCons.SConsign.current_sconsign_filename ()

SCons.SConsign.write () → None

# SCons.Subst module

SCons string substitution.

class SCons.Subst.CmdStringHolder ( cmd , literal: bool = False)

Bases: UserString

Holder for substituted strings intended for the command line.

Holds strings generated by scons_subst(), scons_subst_list(). Defines an escape() method which allows supplying platform-specific escape and quote functions. The contained string will be escaped, quoted, or neither depending on the value of literal and the string contents.

_abc_impl = <_abc._abc_data object>

capitalize ()

casefold ()

center ( width , *args )

count ( value ) → integer -- return number of occurrences of value

encode ( encoding= 'utf-8', errors= 'strict')

endswith ( suffix , start= 0, end= 9223372036854775807)

escape ( escape_func , quote_func=<function quote_spaces> ) → str

Escape the string with the supplied function. The function is expected to take an arbitrary string, then return it with all special characters escaped and ready for passing to the command interpreter.

After calling this function, the next call to str() will return the escaped string.

expandtabs ( tabsize= 8)

find ( sub , start= 0, end= 9223372036854775807)

format ( *args , **kwds )

format_map ( mapping )

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

is_literal () → bool

isalnum ()

SCons API Documentation

49 isalpha ()

isascii ()

isdecimal ()

isdigit ()

isidentifier ()

islower ()

isnumeric ()

isprintable ()

isspace ()

istitle ()

isupper ()

join ( seq )

ljust ( width , *args )

lower ()

lstrip ( chars= None)

maketrans ()

Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

partition ( sep )

removeprefix ( prefix , /)

removesuffix ( suffix , /)

replace ( old , new , maxsplit= -1)

rfind ( sub , start= 0, end= 9223372036854775807)

rindex ( sub , start= 0, end= 9223372036854775807)

rjust ( width , *args )

rpartition ( sep )

rsplit ( sep= None, maxsplit= -1)

rstrip ( chars= None)

split ( sep= None, maxsplit= -1)

splitlines ( keepends= False)

startswith ( prefix , start= 0, end= 9223372036854775807)

strip ( chars= None)

swapcase ()

title ()

translate ( *args )

upper ()

zfill ( width )

class SCons.Subst.ListSubber ( env , mode , conv , gvars )

Bases: UserList

A class to construct the results of a scons_subst_list() call.

Like StringSubber, this class binds a specific construction environment, mode, target and source with two methods (substitute() and expand()) that handle the expansion.

In addition, however, this class is used to track the state of the result(s) we’re gathering so we can do the appropriate thing whenever we have to append another word to the result–start a new line, start a new word, append to the current word, etc. We do this by setting the “append” attribute to the right method so that our wrapper methods only need ever call ListSubber.append(), and the rest of the object takes care of doing the right thing internally.

_abc_impl = <_abc._abc_data object>

add_new_word ( x) → None

add_to_current_word ( x) → None

Append the string x to the end of the current last word in the result. If that is not possible, then just add it as a new word. Make sure the entire concatenated string inherits the object attributes of x (in particular, the escape function) by wrapping it as CmdStringHolder.

SCons API Documentation

50 append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

close_strip ( x) → None

Handle the “close strip” $) token.

copy ()

count ( value ) → integer -- return number of occurrences of value

expand ( s, lvars , within_list )

Expand a single “token” as necessary, appending the expansion to the current result.

This handles expanding different types of things (strings, lists, callables) appropriately. It calls the wrapper substitute() method to re-expand things as necessary, so that the results of expansions of side-by-side strings still get re-evaluated separately, not smushed together.

expanded ( s) → bool

Determines if the string s requires further expansion.

Due to the implementation of ListSubber expand will call itself 2 additional times for an already expanded string. This method is used to determine if a string is already fully expanded and if so exit the loop early to prevent these recursive calls.

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

literal ( x)

next_line () → None

Arrange for the next word to start a new line. This is like starting a new word, except that we have to append another line to the result.

next_word () → None

Arrange for the next word to start a new word.

open_strip ( x) → None

Handle the “open strip” $( token.

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

substitute ( args , lvars , within_list ) → None

Substitute expansions in an argument or list of arguments.

This serves as a wrapper for splitting up a string into separate tokens.

this_word () → None

Arrange for the next word to append to the end of the current last word in the result.

class SCons.Subst.Literal ( lstr )

Bases: object

A string wrapper for a string to prevent expansion.

If you use this object wrapped around a string, then it will be interpreted as literal. When passed to the command interpreter, all special characters will be escaped.

escape ( escape_func )

for_signature ()

is_literal () → bool

class SCons.Subst.NLWrapper ( list , func )

Bases: object

A wrapper class that delays turning a list of sources or targets into a NodeList until it’s needed. The specified function supplied when the object is initialized is responsible for turning raw nodes into proxies that implement the special

SCons API Documentation

51 attributes like .abspath, .source, etc. This way, we avoid creating those proxies just “in case” someone is going to use $TARGET or the like, and only go through the trouble if we really have to.

In practice, this might be a wash performance-wise, but it’s a little cleaner conceptually…

_create_nodelist ()

_gen_nodelist ()

_return_nodelist ()

class SCons.Subst.NullNodeList ( *args , **kwargs )

Bases: NullSeq

_instance

SCons.Subst.SetAllowableExceptions ( *excepts ) → None

class SCons.Subst.SpecialAttrWrapper ( lstr , for_signature= None)

Bases: object

This is a wrapper for what we call a ‘Node special attribute.’ This is any of the attributes of a Node that we can reference from Environment variable substitution, such as $TARGET.abspath or $SOURCES[1].filebase. We implement the same methods as Literal so we can handle special characters, plus a for_signature method, such that we can return some canonical string during signature calculation to avoid unnecessary rebuilds.

escape ( escape_func )

for_signature ()

is_literal () → bool

class SCons.Subst.StringSubber ( env , mode , conv , gvars )

Bases: object

A class to construct the results of a scons_subst() call.

This binds a specific construction environment, mode, target and source with two methods (substitute() and expand()) that handle the expansion.

expand ( s, lvars )

Expand a single “token” as necessary, returning an appropriate string containing the expansion.

This handles expanding different types of things (strings, lists, callables) appropriately. It calls the wrapper substitute() method to re-expand things as necessary, so that the results of expansions of side-by-side strings still get re-evaluated separately, not smushed together.

substitute ( args , lvars )

Substitute expansions in an argument or list of arguments.

This serves as a wrapper for splitting up a string into separate tokens.

class SCons.Subst.Target_or_Source ( nl )

Bases: object

A class that implements $TARGET or $SOURCE expansions by in turn wrapping a NLWrapper. This class handles the different methods used to access an individual proxy Node, calling the NLWrapper to create a proxy on demand.

class SCons.Subst.Targets_or_Sources ( nl )

Bases: UserList

A class that implements $TARGETS or $SOURCES expansions by in turn wrapping a NLWrapper. This class handles the different methods used to access the list, calling the NLWrapper to create proxies on demand.

Note that we subclass UserList purely so that the is_Sequence() function will identify an object of this class as a list during variable expansion. We’re not really using any UserList methods in practice.

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

SCons API Documentation

52 Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

SCons.Subst._remove_list ( list )

SCons.Subst._rm_list ( list )

SCons.Subst.escape_list ( mylist , escape_func ) → list [str ]

Escape a list of arguments by running the specified escape_func on every object in the list that has an escape() method.

SCons.Subst.quote_spaces ( arg )

Generic function for putting double quotes around any string that has white space in it.

SCons.Subst.raise_exception ( exception , target , s)

SCons.Subst.scons_subst ( strSubst , env , mode= 1, target= None, source= None, gvars= {}, lvars= {},

conv= None, overrides: dict | None = None)

Expand a string or list containing construction variable substitutions.

This is the work-horse function for substitutions in file names and the like. The companion scons_subst_list() function (below) handles separating command lines into lists of arguments, so see that function if that’s what you’re looking for.

SCons.Subst.scons_subst_list ( strSubst , env , mode= 1, target= None, source= None, gvars= {}, lvars= {},

conv= None, overrides: dict | None = None)

Substitute construction variables in a string (or list or other object) and separate the arguments into a command list.

The companion scons_subst() function (above) handles basic substitutions within strings, so see that function instead if that’s what you’re looking for.

SCons.Subst.scons_subst_once ( strSubst , env , key )

Perform single (non-recursive) substitution of a single construction variable keyword.

This is used when setting a variable when copying or overriding values in an Environment. We want to capture (expand) the old value before we override it, so people can do things like:

env2 = env.Clone(CCFLAGS = ‘$CCFLAGS -g’)

We do this with some straightforward, brute-force code here…

SCons.Subst.subst_dict ( target , source )

Create a dictionary for substitution of special construction variables.

This translates the following special arguments:

target - the target (object or array of objects),

used to generate the TARGET and TARGETS construction variables

source - the source (object or array of objects),

used to generate the SOURCES and SOURCE construction variables

# SCons.Warnings module

The SCons Warnings framework.

Enables issuing warnings in situations where it is useful to alert the user of a condition that does not warrant raising an exception that could terminate the program.

A new warning class should inherit (perhaps indirectly) from one of two base classes: SConsWarning or WarningOnByDefault, which are the same except warnings derived from the latter will start out in an enabled state. Enabled warnings cause a message to be printed when called, disabled warnings are silent.

There is also a hierarchy for indicating deprecations and future changes: for these, derive from DeprecatedWarning, MandatoryDeprecatedWarning, FutureDeprecatedWarning or FutureReservedVariableWarning.

Whether or not to display warnings, beyond those that are on by default, is controlled through the command line (--warn ) or through SetOption('warn') . The names used there use a different naming style than the warning class names. process_warn_strings() converts the names before enabling/disabling.

SCons API Documentation

53 The behavior of issuing only a message (for “enabled” warnings) can be toggled to raising an exception instead by calling the warningAsException() function.

For new/removed warnings, the manpage needs to be kept in sync. Any warning class defined here is accepted, but we don’t want to make people have to dig around to find the names. Warnings do not have to be defined in this file, though it is preferred: those defined elsewhere cannot use the enable/disable functionality unless they monkeypatch the warning into this module’s namespace.

You issue a warning, either in SCons code or in a build project’s SConscripts, by calling the warn() function defined in this module. Raising directly with an instance of a warning class bypasses the framework and it will behave like an ordinary exception.

exception SCons.Warnings.CacheCleanupErrorWarning

Bases: SConsWarning

Problems removing retrieved target prior to rebuilding.

exception SCons.Warnings.CacheVersionWarning

Bases: WarningOnByDefault

The derived-file cache directory has an out of date config.

exception SCons.Warnings.CacheWriteErrorWarning

Bases: SConsWarning

Problems writing a derived file to the cache.

exception SCons.Warnings.CorruptSConsignWarning

Bases: WarningOnByDefault

Problems decoding the contents of the sconsign database.

exception SCons.Warnings.DependencyWarning

Bases: SConsWarning

A scanner identified a dependency but did not add it.

exception SCons.Warnings.DeprecatedDebugOptionsWarning

Bases: MandatoryDeprecatedWarning

Option-arguments to –debug that are deprecated.

exception SCons.Warnings.DeprecatedOptionsWarning

Bases: MandatoryDeprecatedWarning

Options that are deprecated.

exception SCons.Warnings.DeprecatedWarning

Bases: SConsWarning

Base class for deprecated features, will be removed in future.

exception SCons.Warnings.DevelopmentVersionWarning

Bases: WarningOnByDefault

Use of a deprecated feature.

exception SCons.Warnings.DuplicateEnvironmentWarning

Bases: WarningOnByDefault

A target appears in more than one consenv with identical actions.

A duplicate target with different rules cannot be built; with the same rule it can, but this could indicate a problem in the build configuration.

exception SCons.Warnings.FortranCxxMixWarning

Bases: LinkWarning

Fortran and C++ objects appear together in a link line.

Some compilers support this, others do not.

exception SCons.Warnings.FutureDeprecatedWarning

Bases: SConsWarning

Base class for features that will become deprecated in a future release.

exception SCons.Warnings.FutureReservedVariableWarning

Bases: WarningOnByDefault

Setting a variable marked to become reserved in a future release.

exception SCons.Warnings.LinkWarning

Bases: WarningOnByDefault

Base class for linker warnings.

exception SCons.Warnings.MandatoryDeprecatedWarning

SCons API Documentation

54 Bases: DeprecatedWarning

Base class for deprecated features where warning cannot be disabled.

exception SCons.Warnings.MisleadingKeywordsWarning

Bases: WarningOnByDefault

Use of possibly misspelled kwargs in Builder calls.

exception SCons.Warnings.MissingSConscriptWarning

Bases: WarningOnByDefault

The script specified in an SConscript() call was not found.

TODO: this is now an error, so no need for a warning. Left in for a while in case anyone is using, remove eventually.

Manpage entry removed in 4.6.0.

exception SCons.Warnings.NoObjectCountWarning

Bases: WarningOnByDefault

Object counting (debug mode) could not be enabled.

exception SCons.Warnings.NoParallelSupportWarning

Bases: WarningOnByDefault

Fell back to single-threaded build, as no thread support found.

exception SCons.Warnings.PythonVersionWarning

Bases: DeprecatedWarning

SCons was run with a deprecated Python version.

exception SCons.Warnings.ReservedVariableWarning

Bases: WarningOnByDefault

Attempt to set reserved construction variable names.

exception SCons.Warnings.SConsWarning

Bases: UserError

Base class for all SCons warnings.

SCons.Warnings.SConsWarningOnByDefault

alias of WarningOnByDefault

exception SCons.Warnings.StackSizeWarning

Bases: WarningOnByDefault

Requested thread stack size could not be set.

exception SCons.Warnings.TargetNotBuiltWarning

Bases: SConsWarning

A target build indicated success but the file is not found.

exception SCons.Warnings.ToolQtDeprecatedWarning

Bases: DeprecatedWarning

exception SCons.Warnings.VisualCMissingWarning

Bases: WarningOnByDefault

Requested MSVC version not found and policy is to not fail.

exception SCons.Warnings.VisualStudioMissingWarning

Bases: SConsWarning

exception SCons.Warnings.VisualVersionMismatch

Bases: WarningOnByDefault

MSVC_VERSION and MSVS_VERSION do not match.

Note MSVS_VERSION is deprecated, use MSVC_VERSION .

exception SCons.Warnings.WarningOnByDefault

Bases: SConsWarning

Base class for SCons warnings that are enabled by default.

SCons.Warnings.enableWarningClass ( clazz ) → None

Enables all warnings of type clazz or derived from clazz .

SCons.Warnings.process_warn_strings ( arguments: Sequence[str] ) → None

Process requests to enable/disable warnings.

The requests come from the option-argument string passed to the --warn command line option or as the value passed to the SetOption function with a first argument of warn ;

The arguments are expected to be as documented in the SCons manual page for the --warn option, in the style

some-type , which is converted here to a camel-case name like SomeTypeWarning , to try to match the warning classes defined here, which are then passed to enableWarningClass() or suppressWarningClass().

SCons API Documentation

55 For example, a string``”deprecated”`` enables the DeprecatedWarning class, while a string``”no-dependency”`` disables the DependencyWarning class.

As a special case, the string "all" disables all warnings and a the string "no-all" disables all warnings.

SCons.Warnings.suppressWarningClass ( clazz ) → None

Suppresses all warnings of type clazz or derived from clazz .

SCons.Warnings.warn ( clazz , *args ) → None

Issue a warning, accounting for SCons rules.

Check if warnings for this class are enabled. If warnings are treated as exceptions, raise exception. Use the global warning emitter _warningOut, which allows selecting different ways of presenting a traceback (see Script/Main.py).

SCons.Warnings.warningAsException ( flag: bool = True) → bool

Sets global _warningAsExeption flag.

If true, any enabled warning will cause an exception to be raised.

Parameters: flag – new value for warnings-as-exceptions.

Returns: The previous value.

# SCons.cpp module

SCons C Pre-Processor module

SCons.cpp.CPP_to_Python ( s)

Converts a C pre-processor expression into an equivalent Python expression that can be evaluated.

SCons.cpp.CPP_to_Python_Ops_Sub ( m)

SCons.cpp.Cleanup_CPP_Expressions ( ts )

class SCons.cpp.DumbPreProcessor ( *args , **kw )

Bases: PreProcessor

A preprocessor that ignores all #if/#elif/#else/#endif directives and just reports back all of the #include files (like the classic SCons scanner did).

This is functionally equivalent to using a regular expression to find all of the #include lines, only slower. It exists mainly as an example of how the main PreProcessor class can be sub-classed to tailor its behavior.

__call__ ( file )

Pre-processes a file.

This is the main public entry point.

_do_if_else_condition ( condition ) → None

Common logic for evaluating the conditions on #if, #ifdef and #ifndef lines.

_match_tuples ( tuples )

_parse_tuples ( contents )

_process_tuples ( tuples , file= None)

all_include ( t) → None

do_define ( t) → None

Default handling of a #define line.

do_elif ( t) → None

Default handling of a #elif line.

do_else ( t) → None

Default handling of a #else line.

do_endif ( t) → None

Default handling of a #endif line.

do_if ( t) → None

Default handling of a #if line.

do_ifdef ( t) → None

Default handling of a #ifdef line.

do_ifndef ( t) → None

Default handling of a #ifndef line.

do_import ( t) → None

Default handling of a #import line.

do_include ( t) → None

Default handling of a #include line.

SCons API Documentation

56 do_include_next ( t) → None

Default handling of a #include line.

do_nothing ( t) → None

Null method for when we explicitly want the action for a specific preprocessor directive to do nothing.

do_undef ( t) → None

Default handling of a #undef line.

eval_constant_expression ( s)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

Returns None if the eval() result is not an integer.

eval_expression ( t)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

finalize_result ( fname )

find_include_file ( t)

Finds the #include file for a given preprocessor tuple.

initialize_result ( fname ) → None

process_contents ( contents )

Pre-processes a file contents.

Is used by tests

process_file ( file )

Pre-processes a file.

This is the main internal entry point.

read_file ( file ) → str

resolve_include ( t)

Resolve a tuple-ized #include line.

This handles recursive expansion of values without “” or <> surrounding the name until an initial “ or < is found, to handle #include FILE where FILE is a #define somewhere else.

restore () → None

Pops the previous dispatch table off the stack and makes it the current one.

save () → None

Pushes the current dispatch table on the stack and re-initializes the current dispatch table to the default.

scons_current_file ( t) → None

start_handling_includes ( t= None) → None

Causes the PreProcessor object to start processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates True, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated False.

stop_handling_includes ( t= None) → None

Causes the PreProcessor object to stop processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates False, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated True.

tupleize ( contents )

Turns the contents of a file into a list of easily-processed tuples describing the CPP lines in the file.

The first element of each tuple is the line’s preprocessor directive (#if, #include, #define, etc., minus the initial ‘#’). The remaining elements are specific to the type of directive, as pulled apart by the regular expression.

class SCons.cpp.FunctionEvaluator ( name , args , expansion )

Bases: object

Handles delayed evaluation of a #define function call.

__call__ ( *values )

Evaluates the expansion of a #define macro function called with the specified values.

class SCons.cpp.PreProcessor ( current= '.', cpppath= (), dict= {}, all: int = 0, depth= -1)

Bases: object

The main workhorse class for handling C pre-processing.

__call__ ( file )

SCons API Documentation

57 Pre-processes a file.

This is the main public entry point.

_do_if_else_condition ( condition ) → None

Common logic for evaluating the conditions on #if, #ifdef and #ifndef lines.

_match_tuples ( tuples )

_parse_tuples ( contents )

_process_tuples ( tuples , file= None)

all_include ( t) → None

do_define ( t) → None

Default handling of a #define line.

do_elif ( t) → None

Default handling of a #elif line.

do_else ( t) → None

Default handling of a #else line.

do_endif ( t) → None

Default handling of a #endif line.

do_if ( t) → None

Default handling of a #if line.

do_ifdef ( t) → None

Default handling of a #ifdef line.

do_ifndef ( t) → None

Default handling of a #ifndef line.

do_import ( t) → None

Default handling of a #import line.

do_include ( t) → None

Default handling of a #include line.

do_include_next ( t) → None

Default handling of a #include line.

do_nothing ( t) → None

Null method for when we explicitly want the action for a specific preprocessor directive to do nothing.

do_undef ( t) → None

Default handling of a #undef line.

eval_constant_expression ( s)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

Returns None if the eval() result is not an integer.

eval_expression ( t)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

finalize_result ( fname )

find_include_file ( t)

Finds the #include file for a given preprocessor tuple.

initialize_result ( fname ) → None

process_contents ( contents )

Pre-processes a file contents.

Is used by tests

process_file ( file )

Pre-processes a file.

This is the main internal entry point.

read_file ( file ) → str

resolve_include ( t)

Resolve a tuple-ized #include line.

This handles recursive expansion of values without “” or <> surrounding the name until an initial “ or < is found, to handle #include FILE where FILE is a #define somewhere else.

SCons API Documentation

58 restore () → None

Pops the previous dispatch table off the stack and makes it the current one.

save () → None

Pushes the current dispatch table on the stack and re-initializes the current dispatch table to the default.

scons_current_file ( t) → None

start_handling_includes ( t= None) → None

Causes the PreProcessor object to start processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates True, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated False.

stop_handling_includes ( t= None) → None

Causes the PreProcessor object to stop processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates False, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated True.

tupleize ( contents )

Turns the contents of a file into a list of easily-processed tuples describing the CPP lines in the file.

The first element of each tuple is the line’s preprocessor directive (#if, #include, #define, etc., minus the initial ‘#’). The remaining elements are specific to the type of directive, as pulled apart by the regular expression.

# SCons.dblite module

dblite.py module contributed by Ralf W. Grosse-Kunstleve. Extended for Unicode by Steven Knight.

This is a very simple-minded “database” used for saved signature information, with an interface modeled on the Python dbm database interface module.

class SCons.dblite._Dblite ( file_base_name , flag= 'r', mode= 438)

Bases: object

Lightweight signature database class.

Behaves like a dict when in memory, loads from a pickled disk file on open and writes back out to it on close.

Open the database file using a path derived from file_base_name . The optional flag argument can be:

Value Meaning

'r' Open existing database for reading only (default)

'w' Open existing database for reading and writing

'c' Open database for reading and writing, creating it if it doesn’t exist

'n' Always create a new, empty database, open for reading and writing

The optional mode argument is the POSIX mode of the file, used only when the database has to be created. It defaults to octal 0o666 .

_check_writable ()

static _open ( file , mode= 'r', buffering= -1, encoding= None, errors= None, newline= None,

closefd= True, opener= None)

Open file and return a stream. Raise OSError upon failure.

file is either a text or byte string giving the name (and the path if the file isn’t in the current working directory) of the file to be opened or an integer file descriptor of the file to be wrapped. (If a file descriptor is given, it is closed when the returned I/O object is closed, unless closefd is set to False.)

mode is an optional string that specifies the mode in which the file is opened. It defaults to ‘r’ which means open for reading in text mode. Other common values are ‘w’ for writing (truncating the file if it already exists), ‘x’ for creating and writing to a new file, and ‘a’ for appending (which on some Unix systems, means that all writes append to the end of the file regardless of the current seek position). In text mode, if encoding is not specified the encoding used is platform dependent: locale.getencoding() is called to get the current locale encoding. (For reading and writing raw bytes use binary mode and leave encoding unspecified.) The available modes are:

Character Meaning ‘r’ open for reading (default) ‘w’ open for writing, truncating the file first

SCons API Documentation

59 ‘x’ create a new file and open it for writing ‘a’ open for writing, appending to the end of the file if it exists ‘b’ binary mode ‘t’ text mode (default) ‘+’ open a disk file for updating (reading and writing)

The default mode is ‘rt’ (open for reading text). For binary random access, the mode ‘w+b’ opens and truncates the file to 0 bytes, while ‘r+b’ opens the file without truncation. The ‘x’ mode implies ‘w’ and raises an FileExistsError if the file already exists.

Python distinguishes between files opened in binary and text modes, even when the underlying operating system doesn’t. Files opened in binary mode (appending ‘b’ to the mode argument) return contents as bytes objects without any decoding. In text mode (the default, or when ‘t’ is appended to the mode argument), the contents of the file are returned as strings, the bytes having been first decoded using a platform-dependent encoding or using the specified encoding if given.

buffering is an optional integer used to set the buffering policy. Pass 0 to switch buffering off (only allowed in binary mode), 1 to select line buffering (only usable in text mode), and an integer > 1 to indicate the size of a fixed-size chunk buffer. When no buffering argument is given, the default buffering policy works as follows:

• Binary files are buffered in fixed-size chunks; the size of the buffer is chosen using a heuristic trying to determine the underlying device’s “block size” and falling back on io.DEFAULT_BUFFER_SIZE . On many systems, the buffer will typically be 4096 or 8192 bytes long.

• “Interactive” text files (files for which isatty() returns True) use line buffering. Other text files use the policy described above for binary files.

encoding is the name of the encoding used to decode or encode the file. This should only be used in text mode. The default encoding is platform dependent, but any encoding supported by Python can be passed. See the codecs module for the list of supported encodings.

errors is an optional string that specifies how encoding errors are to be handled—this argument should not be used in binary mode. Pass ‘strict’ to raise a ValueError exception if there is an encoding error (the default of None has the same effect), or pass ‘ignore’ to ignore errors. (Note that ignoring encoding errors can lead to data loss.) See the documentation for codecs.register or run ‘help(codecs.Codec)’ for a list of the permitted encoding error strings.

newline controls how universal newlines works (it only applies to text mode). It can be None, ‘’, ‘n’, ‘r’, and ‘rn’. It works as follows:

• On input, if newline is None, universal newlines mode is enabled. Lines in the input can end in ‘n’, ‘r’, or ‘rn’, and these are translated into ‘n’ before being returned to the caller. If it is ‘’, universal newline mode is enabled, but line endings are returned to the caller untranslated. If it has any of the other legal values, input lines are only terminated by the given string, and the line ending is returned to the caller untranslated.

• On output, if newline is None, any ‘n’ characters written are translated to the system default line separator, os.linesep. If newline is ‘’ or ‘n’, no translation takes place. If newline is any of the other legal values, any ‘n’ characters written are translated to the given string.

If closefd is False, the underlying file descriptor will be kept open when the file is closed. This does not work when a file name is given and must be True in that case.

A custom opener can be used by passing a callable as opener . The underlying file descriptor for the file object is then obtained by calling opener with ( file , flags ). opener must return an open file descriptor (passing os.open as

opener results in functionality similar to passing None).

open() returns a file object whose type depends on the mode, and through which the standard file operations such as reading and writing are performed. When open() is used to open a file in a text mode (‘w’, ‘r’, ‘wt’, ‘rt’, etc.), it returns a TextIOWrapper. When used to open a file in a binary mode, the returned class varies: in read binary mode, it returns a BufferedReader; in write binary and append binary modes, it returns a BufferedWriter, and in read/write mode, it returns a BufferedRandom.

It is also possible to use a string or bytearray as a file for both reading and writing. For strings StringIO can be used like a file opened in a text mode, and for bytes a BytesIO can be used like a file opened in a binary mode.

static _os_chmod ( path , mode , *, dir_fd= None, follow_symlinks= True)

Change the access permissions of a file.

SCons API Documentation

60 path

Path to be modified. May always be specified as a str, bytes, or a path-like object. On some platforms, path may also be specified as an open file descriptor. If this functionality is unavailable, using it raises an exception.

mode

Operating-system mode bitfield.

dir_fd

If not None, it should be a file descriptor open to a directory, and path should be relative; path will then be relative to that directory.

follow_symlinks

If False, and the last element of the path is a symbolic link, chmod will modify the symbolic link itself instead of the file the link points to.

It is an error to use dir_fd or follow_symlinks when specifying path as

an open file descriptor.

dir_fd and follow_symlinks may not be implemented on your platform.

If they are unavailable, using them will raise a NotImplementedError.

static _os_chown ( path , uid , gid , *, dir_fd= None, follow_symlinks= True)

Change the owner and group id of path to the numeric uid and gid.

path

Path to be examined; can be string, bytes, a path-like object, or open-file-descriptor int.

dir_fd

If not None, it should be a file descriptor open to a directory, and path should be relative; path will then be relative to that directory.

follow_symlinks

If False, and the last element of the path is a symbolic link, stat will examine the symbolic link itself instead of the file the link points to.

path may always be specified as a string. On some platforms, path may also be specified as an open file descriptor.

If this functionality is unavailable, using it raises an exception.

If dir_fd is not None, it should be a file descriptor open to a directory,

and path should be relative; path will then be relative to that directory.

If follow_symlinks is False, and the last element of the path is a symbolic

link, chown will modify the symbolic link itself instead of the file the link points to.

It is an error to use dir_fd or follow_symlinks when specifying path as

an open file descriptor.

dir_fd and follow_symlinks may not be implemented on your platform.

If they are unavailable, using them will raise a NotImplementedError.

static _os_replace ( src , dst , *, src_dir_fd= None, dst_dir_fd= None)

Rename a file or directory, overwriting the destination.

If either src_dir_fd or dst_dir_fd is not None, it should be a file

descriptor open to a directory, and the respective path string (src or dst) should be relative; the path will then be relative to that directory.

src_dir_fd and dst_dir_fd, may not be implemented on your platform.

If they are unavailable, using them will raise a NotImplementedError.

static _pickle_dump ( obj , file , protocol= None, *, fix_imports= True, buffer_callback= None)

Write a pickled representation of obj to the open file object file.

This is equivalent to Pickler(file, protocol).dump(obj) , but may be more efficient.

SCons API Documentation

61 The optional protocol argument tells the pickler to use the given protocol; supported protocols are 0, 1, 2, 3, 4 and 5. The default protocol is 4. It was introduced in Python 3.4, and is incompatible with previous versions.

Specifying a negative protocol version selects the highest protocol version supported. The higher the protocol used, the more recent the version of Python needed to read the pickle produced.

The file argument must have a write() method that accepts a single bytes argument. It can thus be a file object opened for binary writing, an io.BytesIO instance, or any other custom object that meets this interface.

If fix_imports is True and protocol is less than 3, pickle will try to map the new Python 3 names to the old module names used in Python 2, so that the pickle data stream is readable with Python 2.

If buffer_callback is None (the default), buffer views are serialized into file as part of the pickle stream. It is an error if buffer_callback is not None and protocol is None or smaller than 5.

_pickle_protocol = 4

static _shutil_copyfile ( src , dst , *, follow_symlinks= True)

Copy data from src to dst in the most efficient way possible.

If follow_symlinks is not set and src is a symbolic link, a new symlink will be created instead of copying the file it points to.

static _time_time ()

time() -> floating point number

Return the current time in seconds since the Epoch. Fractions of a second may be present if the system clock provides them.

close () → None

items ()

keys ()

opener ( path , flags )

Database open helper when creation may be needed.

The high-level Python open() function cannot specify a file mode for creation. Using this as the opener with the saved mode lets us do that.

sync () → None

Flush the database to disk.

This routine must succeed, since the in-memory and on-disk copies are out of sync as soon as we do anything that changes the in-memory version. Thus, to be cautious, flush to a temporary file and then move it over with some error handling.

values ()

SCons.dblite._exercise ()

SCons.dblite.open ( file , flag= 'r', mode: int = 438)

# SCons.exitfuncs module

Register functions which are executed when SCons exits for any reason.

SCons.exitfuncs._run_exitfuncs () → None

run any registered exit functions

_exithandlers is traversed in reverse order so functions are executed last in, first out.

SCons.exitfuncs.register ( func , *targs , **kargs ) → None

register a function to be executed upon normal program termination

func - function to be called at exit targs - optional arguments to pass to func kargs - optional keyword arguments to pass to func

# SConsDoc documentation module

This module is NOT part of the SCons build tool itself. It is supporting tooling, invoked by tools used to build documentation components.

SCons Documentation Processing module

This module parses home-brew XML files that document important SCons components. Currently it handles Builders, Environment functions/methods, Construction Variables, and Tools (further expansion is possible). These documentation snippets are turned into files with content and reference tags that can be included into the manpage and/or user guide, which prevents a lot of duplication.

SCons API Documentation

62 In general, you can use any DocBook tag in the input, and this module just adds processing various home-brew tags to try to make life a little easier.

Builder example:

<builder name="BUILDER" >

<summary>

<para> This is the summary description of an SCons Builder. It will get placed in the man page, and in the appropriate User's Guide appendix. The name of this builder may be interpolated anywhere in the document by specifying the

&b-BUILDER; element. A link to this definition may be interpolated by specifying the &b-link-BUILDER; element.

</para>

Unlike vanilla DocBook, blank lines are significant in these descriptions and serve to separate paragraphs. They'll get replaced in DocBook output with appropriate tags to indicate a new paragraph.

<example>

print("this is example code, it will be offset and indented")

</example>

</summary>

</builder>

Function example:

<scons_function name="FUNCTION" >

<arguments signature="SIGTYPE" >

(arg1, arg2, key=value)

</arguments>

<summary>

<para> This is the summary description of an SCons function. It will get placed in the man page, and in the appropriate User's Guide appendix. If the "signature" attribute is specified, SIGTYPE may be one of "global", "env" or "both" (the default if omitted is "both"), to indicate the signature applies to the global form or the environment form, or to generate both with the same signature (excepting the insertion of "env."). This allows for the cases of describing that only one signature should be generated, or both signatures should be generated and they differ, or both signatures should be generated and they are the same. The name of this function may be interpolated anywhere in the document by specifying the

&f-FUNCTION; element or the &f-env-FUNCTION; element. Links to this definition may be interpolated by specifying the &f-link-FUNCTION; or &f-link-env-FUNCTION; element.

</para>

<example>

print("this is example code, it will be offset and indented")

SCons API Documentation

63 </example>

</summary>

</scons_function>

Construction variable example:

<cvar name="VARIABLE" >

<summary>

<para> This is the summary description of a construction variable. It will get placed in the man page, and in the appropriate User's Guide appendix. The name of this construction variable may be interpolated anywhere in the document by specifying the

&cv-VARIABLE; element. A link to this definition may be interpolated by specifying the &cv-link-VARIABLE; element.

</para>

<example>

print("this is example code, it will be offset and indented")

</example>

</summary>

</cvar>

Tool example:

<tool name="TOOL" >

<summary>

<para> This is the summary description of an SCons Tool. It will get placed in the man page, and in the appropriate User's Guide appendix. The name of this tool may be interpolated anywhere in the document by specifying the

&t-TOOL; element. A link to this definition may be interpolated by specifying the &t-link-TOOL; element.

</para>

<example>

print("this is example code, it will be offset and indented")

</example>

</summary>

</tool>

class bin.SConsDoc.Arguments ( signature , body= None)

Bases: object

append ( data )

class bin.SConsDoc.Builder ( name )

Bases: Item

cmp_name ( name )

class bin.SConsDoc.ConstructionVariable ( name )

Bases: Item

cmp_name ( name )

class bin.SConsDoc.DoctypeDeclaration ( name_= None)

Bases: object

addEntity ( name , uri )

SCons API Documentation

64 createDoctype ()

class bin.SConsDoc.DoctypeEntity ( name_, uri_ )

Bases: object

getEntityString () → str

class bin.SConsDoc.Function ( name )

Bases: Item

cmp_name ( name )

class bin.SConsDoc.Item ( name )

Bases: object

cmp_name ( name )

class bin.SConsDoc.Libxml2ValidityHandler

Bases: object

error ( msg , data )

warning ( msg , data )

class bin.SConsDoc.SConsDocHandler

Bases: object

parseContent ( content , include_entities= True)

Parse the given content as XML.

This method is used when we generate the basic lists of entities for the builders, tools and functions. So we usually don’t bother about namespaces and resolving entities here… this is handled in parseXmlFile below (step 2 of the overall process).

parseDomtree ( root , xpath_context= None, nsmap= None, include_entities= True)

parseInstance ( domelem , map , Class , xpath_context , nsmap , include_entities= True)

parseItems ( domelem , xpath_context , nsmap )

parseUsesSets ( domelem , xpath_context , nsmap )

parseXmlFile ( fpath )

class bin.SConsDoc.SConsDocTree

Bases: object

parseContent ( content , include_entities= True)

Parses the given text content as XML

This is the setup portion, called from parseContent in an SConsDocHandler instance - see the notes there.

parseXmlFile ( fpath )

class bin.SConsDoc.Tool ( name )

Bases: Item

cmp_name ( name )

class bin.SConsDoc.TreeFactory

Bases: object

static appendCvLink ( root , key , lntail )

static appendNode ( parent , child )

static convertElementTree ( root )

Convert the given tree of etree.Element entries to a list of tree nodes for the current XML toolkit.

static copyNode ( node )

static decorateWithHeader ( root )

static findAll ( root , tag , ns= None, xp_ctxt= None, nsmap= None)

static findAllChildrenOf ( root , tag , ns= None, xp_ctxt= None, nsmap= None)

static getAttribute ( node , att )

static getTail ( root )

static getText ( root )

static hasAttribute ( node , att )

static newEtreeNode ( tag , init_ns= False, **kwargs )

static newNode ( tag , **kwargs )

static newSubNode ( parent , tag , **kwargs )

newXmlTree ( root )

Return a XML file tree with the correct namespaces set, the element root as top entry and the given header comment.

static prettyPrintFile ( fpath )

SCons API Documentation

65 static setAttribute ( node , att , value )

static setTail ( root , txt )

static setText ( root , txt )

static validateXml ( fpath , xmlschema_context )

static writeGenTree ( root , fp )

static writeTree ( root , fpath )

xmlschema = None

bin.SConsDoc.importfile ( path )

Import a Python source file or compiled file given its path.

bin.SConsDoc.isSConsXml ( fpath )

Check whether the given file is an SCons XML file.

It is SCons XML if it contains the default target namespace definition described by dbxsdpat

bin.SConsDoc.remove_entities ( content )

bin.SConsDoc.validate_all_xml ( dpaths , xsdfile= 'doc/xsd/scons.xsd')

# SConsExamples documentation module

This module is NOT part of the SCons build tool itself. It is supporting tooling, invoked by tools used to build documentation components.

SCons Example Generator

Generate example outputs for the SCons documentation (primarily the User Guide) by processing custom XML tags that describe example SCons projects. The generator automates tasks that would otherwise require considerable manual effort: verifying that example projects run correctly, and capturing their output for documentation. Conceptually this is a bit like Python doctest , but file-based rather than snippet-based.

An example consists of three parts:

1. Project files ( scons_example tag)

2. Build commands ( scons_output_command tag)

3. Generated output ( scons_output tag)

Here’s a minimal example project:

<scons_example name="ex1" >

<file name="SConstruct" printme="1" >

env = Environment() env.Program('foo')

</file>

<file name="foo.c" >

int main(void) { printf("foo.c\n"); }

</file>

</scons_example>

The example project’s name attribute provides a handle for later associating the output with this project.

Each file tag describes the contents of a file to be created when setting up the project, and each directory tag describes a directory to be created. Both take a name attribute. The optional chmod attribute can be used if the created file or directory needs something other than default permissions, usually to make a file executable. The printme

attribute indicates whether a file’s contents should be shown in the documentation. Any file with a printme value of 1

will have contents generated for inclusion; SConstruct and other SConscript files will normally set this. The default is to not show, since often the contents of the source files is needed to make the build work, but is not often not that interesting when illustrating an SCons concept.

To show just an SConstruct file, use the shorthand sconstruct tag:

SCons API Documentation

66 <sconstruct>

env = Environment() env.Program('foo')

</sconstruct>

This is equivalent to:

<scons_example>

<file name="SConstruct" printme="1" >

...contents...

</file>

</scons_example>

The scons_example_file tag allows you to display the contents of a file outside the context of its definition in

scons_example . This looks like:

<scons_example_file example="example1" name="hello.h" />

Link an example project to its output using the scons_output tag:

<scons_output example="ex1" os="posix" >

<scons_output_command> scons -Q foo </scons_output_command>

</scons_output>

The example attribute associates the project of that name with the output. The os attribute can be used to indicate a specific platform (for example, to display a suitable shell prompt). The default is posix . The suffix attribute allows tracking outputs from multiple ways of running a project. The optional tools attribute gives a non-default tool list for this run.

An scons_output_command tag inside an scons_output contains the instructions to build the project. There can be several build commands defined for a given example project:

<scons_output example="ex1" os="posix" suffix="1" >

<scons_output_command> scons -Q foo </scons_output_command>

</scons_output>

<scons_output example="ex1" os="posix" suffix="2" >

<scons_output_command> scons -Q --option foo </scons_output_command>

</scons_output>

The command’s environment attribute can be used to set environment variables before the command is run. The

output attribute can be used to emit commentary in the output display that is not produced by the command itself, for example:

<scons_output_command output="[CHANGE THE CONTENTS OF hello.h]" >edit hello.h </scons_output_co

The actual command text has some special recognized values:

• scons - to run scons

• touch - to update the file change time

• edit - to change a file’s contents without changing its behavior (works for C / C++)

• ls - generate a directory listing

• sleep - delay for a while

SCons API Documentation

67 The generator will: 1. Show the OS-appropriate command prompt 2. Execute the command in a temporary directory 3. Capture SCons standard output for the documentation 4. Pass through error output for troubleshooting

class bin.SConsExamples.ExampleCommand

Bases: object

class bin.SConsExamples.ExampleFile ( type_= 0)

Bases: object

isFileRef ()

class bin.SConsExamples.ExampleFolder

Bases: object

class bin.SConsExamples.ExampleInfo

Bases: object

getFileContents ( fname )

class bin.SConsExamples.ExampleOutput

Bases: object

bin.SConsExamples.ExecuteCommand ( args , c, t, values )

bin.SConsExamples.collectSConsExampleNames ( fpath )

Return a set() of example names, used in the given file fpath.

bin.SConsExamples.command_edit ( args , c, test , values )

bin.SConsExamples.command_ls ( args , c, test , values )

bin.SConsExamples.command_scons ( args , command , test , values )

Fake scons command

bin.SConsExamples.command_sleep ( args , c, test , values )

bin.SConsExamples.command_touch ( args , command , test , values )

bin.SConsExamples.createAllExampleOutputs ( dpath )

Scan for XML files in the given directory and creates all output files for every example in the ‘generated/examples’ folder.

bin.SConsExamples.create_scons_output ( e)

The real raison d’etre for this script, this is where we actually execute SCons to fetch the output.

bin.SConsExamples.ensureExampleOutputsExist ( dpath )

Scan for XML files in the given directory and ensure that for every example output we have a corresponding output file in the ‘generated/examples’ folder.

bin.SConsExamples.exampleNamesAreUnique ( dpath )

Scan for XML files in the given directory and check whether the scons_example names are unique.

bin.SConsExamples.readAllExampleInfos ( dpath )

Scan for XML files in the given directory and collect together all relevant infos (files/folders, output commands) in a map, which gets returned.

bin.SConsExamples.readExampleInfos ( fpath , examples )

Add the example infos for the file fpath to the global dictionary examples.

# SCons.compat package

# Module contents

SCons compatibility package for old Python versions

This subpackage holds modules that provide backwards-compatible implementations of various things from newer Python versions that we cannot count on because SCons still supported older Pythons.

Other code will not generally reference things in this package through the SCons.compat namespace. The modules included here add things to the builtins namespace or the global module list so that the rest of our code can use the objects and names imported here regardless of Python version. As a result, if this module is used, it should violate the normal convention for imports (standard library imports first, then program-specific imports, each ordered aplhabetically) and needs to be listed first.

The rest of the things here will be in individual compatibility modules that are either: 1) suitably modified copies of the future modules that we want to use; or 2) backwards compatible re-implementations of the specific portions of a future module’s API that we want to use.

SCons.compat package

68 GENERAL WARNINGS: Implementations of functions in the SCons.compat modules are NOT guaranteed to be fully compliant with these functions in later versions of Python. We are only concerned with adding functionality that we actually use in SCons, so be wary if you lift this code for other uses. (That said, making these more nearly the same as later, official versions is still a desirable goal, we just don’t need to be obsessive about it.)

We name the compatibility modules with an initial ‘_scons_’ (for example, _scons_subprocess.py is our compatibility module for subprocess) so that we can still try to import the real module name and fall back to our compatibility module if we get an ImportError. The import_as() function defined below loads the module as the “real” name (without the ‘_scons’), after which all of the “import {module}” statements in the rest of our code will find our pre-loaded compatibility module.

class SCons.compat.NoSlotsPyPy ( name , bases , dct )

Bases: type

Metaclass for PyPy compatitbility.

PyPy does not work well with __slots__ and __class__ assignment.

mro ()

Return a type’s method resolution order.

SCons.compat.rename_module ( new , old ) → bool

Attempt to import the old module and load it under the new name. Used for purely cosmetic name changes in Python 3.x.

# SCons.Node package

# Module contents

The Node package for the SCons software construction utility.

This is, in many ways, the heart of SCons.

A Node is where we encapsulate all of the dependency information about any thing that SCons can build, or about any thing which SCons can use to build some other thing. The canonical “thing,” of course, is a file, but a Node can also represent something remote (like a web page) or something completely abstract (like an Alias).

Each specific type of “thing” is specifically represented by a subclass of the Node base class: Node.FS.File for files, Node.Alias for aliases, etc. Dependency information is kept here in the base class, and information specific to files/aliases/etc. is in the subclass. The goal, if we’ve done this correctly, is that any type of “thing” should be able to depend on any other type of “thing.”

SCons.Node.Annotate ( node ) → None

class SCons.Node.BuildInfoBase

Bases: object

The generic base class for build information for a Node.

This is what gets stored in a .sconsign file for each target file. It contains a NodeInfo instance for this node (signature information that’s specific to the type of Node) and direct attributes for the generic build stuff we have to track: sources, explicit dependencies, implicit dependencies, and action information.

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state.

bact

bactsig : str | None

bdepends

bdependsigs : list [BuildInfoBase ]

bimplicit

bimplicitsigs : list [BuildInfoBase ]

bsources

bsourcesigs : list [BuildInfoBase ]

current_version_id = 2

SCons.Node package

69 merge ( other: BuildInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

class SCons.Node.Node

Bases: object

The base Node class, for entities that we know how to build, or use to build other Nodes.

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of BuildInfoBase

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of NodeInfoBase

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_children_get () → list [Node ]

_children_reset () → None

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_memo

_specific_sources

_tags : dict [str , Any ] | None

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

Return a list of alternate targets for this Node.

always_build

SCons.Node package

70 attributes

binfo

build ( **kw ) → None

Actually build the node.

This is called by the Taskmaster after it’s decided that the Node is out-of-date and must be rebuilt, and after the prepare() method has gotten everything, uh, prepared.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

disambiguate ( must_exist: bool = False)

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists () → bool

Reports whether node exists.

explain ()

for_signature () → str

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to

SCons.Node package

71 return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

get_abspath () → str

Return an absolute path to the Node. This will return simply str(Node) by default, but for Node types that have a concept of relative path, this might return something different.

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents () → bytes | str

Fetch the contents of the entry.

get_csig () → str

get_env () → Environment

get_env_scanner ( env: Environment , kw: dict[str, Any] | None = {}) → ScannerBase | None

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env: Environment , scanner: ScannerBase | None , path ) → list [Node ]

Return the scanned include lines (implicit dependencies) found in this node.

The default is no implicit dependencies. We expect this method to be overridden by any subclass that can be scanned for implicit dependencies.

get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_ninfo () → NodeInfoBase

get_source_scanner ( node: Node ) → ScannerBase | None

Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a

SCons.Node package

72 tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix () → str

get_target_scanner () → ScannerBase | None

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_up_to_date () → bool

Default check for whether the Node is current: unknown Node subtypes are always out of date, so they will always get built.

linked

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare () → None

Prepare for this Node to be built.

SCons.Node package

73 This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

ref_count

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

remove () → None

Remove this Node: no-op by default.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists () → bool

Does this node exist locally or in a repository?

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key () → str | None

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_state ( state: int ) → None

side_effect

SCons.Node package

74 side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

state

store_info

target_peers

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

wkids : list [Node ] | None

class SCons.Node.NodeInfoBase

Bases: object

The generic base class for signature information for a Node.

Node subclasses should subclass NodeInfoBase to provide their own logic for dealing with their own Node-specific signature information.

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state. The version is discarded.

convert ( node , val ) → None

current_version_id = 2

format ( field_list: list[str] | None = None, names: bool = False)

merge ( other: NodeInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

update ( node: Node ) → None

class SCons.Node.NodeList ( initlist= None)

Bases: UserList

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

class SCons.Node.Walker (node: ~SCons.Node.Node, kids_func: ~typing.Callable[[~SCons.Node.Node, ~SCons.Node.Node | None], list[~SCons.Node.Node]] = <function get_children>, cycle_func: ~typing.Callable[[~SCons.Node.Node, list[~SCons.Node.Node]], None] = <function ignore_cycle>, eval_func: ~typing.Callable[[~SCons.Node.Node, ~SCons.Node.Node | None], None] = <function do_nothing>)

Bases: object

SCons.Node package

75 An iterator for walking a Node tree.

This is depth-first, children are visited before the parent. The Walker object can be initialized with any node, and returns the next node on the descent with each get_next() call. get the children of a node instead of calling ‘children’. ‘cycle_func’ is an optional function that will be called when a cycle is detected.

This class does not get caught in node cycles caused, for example, by C header file include loops.

get_next ()

Return the next node for this walk of the tree.

This function is intentionally iterative, not recursive, to sidestep any issues of stack size limitations.

is_done () → bool

SCons.Node.changed_since_last_build_alias ( node , target , prev_ni , repo_node= None) → bool

SCons.Node.changed_since_last_build_entry ( node , target , prev_ni , repo_node= None) → bool

SCons.Node.changed_since_last_build_node ( node , target , prev_ni , repo_node= None) → bool

Must be overridden in a specific subclass to return True if this Node (a dependency) has changed since the last time it was used to build the specified target. prev_ni is this Node’s state (for example, its file timestamp, length, maybe content signature) as of the last time the target was built.

Note that this method is called through the dependency, not the target, because a dependency Node must be able to use its own logic to decide if it changed. For example, File Nodes need to obey if we’re configured to use timestamps, but Python Value Nodes never use timestamps and always use the content. If this method were called through the target, then each Node’s implementation of this method would have to have more complicated logic to handle all the different Node types on which it might depend.

SCons.Node.changed_since_last_build_python ( node , target , prev_ni , repo_node= None) → bool

SCons.Node.changed_since_last_build_state_changed ( node , target , prev_ni , repo_node= None) → bool

SCons.Node.classname ( obj )

SCons.Node.decide_source ( node , target , prev_ni , repo_node= None) → bool

SCons.Node.decide_target ( node , target , prev_ni , repo_node= None) → bool

SCons.Node.do_nothing ( node: Node , parent: Node | None ) → None

SCons.Node.do_nothing_node ( node ) → None

SCons.Node.exists_always ( node ) → bool

SCons.Node.exists_base ( node ) → bool

SCons.Node.exists_entry ( node ) → bool

Return if the Entry exists. Check the file system to see what we should turn into first. Assume a file if there’s no directory.

SCons.Node.exists_file ( node ) → bool

SCons.Node.exists_none ( node ) → bool

SCons.Node.get_children ( node: Node , parent: Node | None ) → list [Node ]

SCons.Node.get_contents_dir ( node )

Return content signatures and names of all our children separated by new-lines. Ensure that the nodes are sorted.

SCons.Node.get_contents_entry ( node )

Fetch the contents of the entry. Returns the exact binary contents of the file.

SCons.Node.get_contents_file ( node ) → bytes

SCons.Node.get_contents_none ( node )

SCons.Node.ignore_cycle ( node: Node , stack: list[Node] ) → None

SCons.Node.is_derived_node ( node ) → bool

Returns true if this node is derived (i.e. built).

SCons.Node.is_derived_none ( node )

SCons.Node.rexists_base ( node )

SCons.Node.rexists_node ( node )

SCons.Node.rexists_none ( node )

SCons.Node.store_info_file ( node ) → None

SCons.Node.store_info_pass ( node ) → None

SCons.Node.target_from_source_base ( node , prefix , suffix , splitext )

SCons.Node.target_from_source_none ( node , prefix , suffix , splitext )

SCons.Node package

76 Submodules

# SCons.Node.Alias module

Alias nodes.

This creates a hash of global Aliases (dummy targets).

class SCons.Node.Alias.Alias ( name )

Bases: Node

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of AliasBuildInfo

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of AliasNodeInfo

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_children_get () → list [Node ]

_children_reset () → None

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_memo

_specific_sources

_tags : dict [str , Any ] | None

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

SCons.Node package

77 Return a list of alternate targets for this Node.

always_build

attributes

binfo

build ( **kw ) → None

A “builder” for aliases.

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

convert () → None

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

disambiguate ( must_exist: bool = False)

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists () → bool

Reports whether node exists.

explain ()

for_signature () → str

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

SCons.Node package

78 get_abspath () → str

Return an absolute path to the Node. This will return simply str(Node) by default, but for Node types that have a concept of relative path, this might return something different.

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents ()

The contents of an alias is the concatenation of the content signatures of all its sources.

get_csig ()

Generate a node’s content signature, the digested signature of its content.

node - the node cache - alternate node to use for the signature cache returns - the content signature

get_env () → Environment

get_env_scanner ( env: Environment , kw: dict[str, Any] | None = {}) → ScannerBase | None

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env: Environment , scanner: ScannerBase | None , path ) → list [Node ]

Return the scanned include lines (implicit dependencies) found in this node.

The default is no implicit dependencies. We expect this method to be overridden by any subclass that can be scanned for implicit dependencies.

get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_ninfo () → NodeInfoBase

get_source_scanner ( node: Node ) → ScannerBase | None

Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a

SCons.Node package

79 tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix () → str

get_target_scanner () → ScannerBase | None

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

is_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

linked

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

SCons.Node package

80 prepare () → None

Prepare for this Node to be built.

This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

really_build ( **kw ) → None

Actually build the node.

This is called by the Taskmaster after it’s decided that the Node is out-of-date and must be rebuilt, and after the prepare() method has gotten everything, uh, prepared.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

ref_count

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

remove () → None

Remove this Node: no-op by default.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists () → bool

Does this node exist locally or in a repository?

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key () → str | None

sconsign () → None

An Alias is not recorded in .sconsign files

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_nocache ( nocache: bool = True) → None

SCons.Node package

81 Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

state

store_info

str_for_display ()

target_peers

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

wkids : list [Node ] | None

class SCons.Node.Alias.AliasBuildInfo

Bases: BuildInfoBase

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state.

bact

bactsig : str | None

bdepends

bdependsigs : list [BuildInfoBase ]

bimplicit

bimplicitsigs : list [BuildInfoBase ]

bsources

bsourcesigs : list [BuildInfoBase ]

current_version_id = 2

merge ( other: BuildInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

class SCons.Node.Alias.AliasNameSpace ( dict= None, /, **kwargs )

Bases: UserDict

Alias ( name , **kw )

_abc_impl = <_abc._abc_data object>

clear () → None. Remove all items from D.

copy ()

classmethod fromkeys ( iterable , value= None)

get ( k[, d]) → D[k] if k in D, else d. d defaults to None.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

lookup ( name , **kw )

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If key is not found, d is returned if given, otherwise KeyError is raised.

popitem () → (k, v), remove and return some (key, value) pair

SCons.Node package

82 as a 2-tuple; but raise KeyError if D is empty.

setdefault ( k[, d]) → D.get(k,d), also set D[k]=d if k not in D

update ([, E], **F ) → None. Update D from mapping/iterable E and F.

If E present and has a .keys() method, does: for k in E: D[k] = E[k] If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v In either case, this is followed by: for k, v in F.items(): D[k] = v

values () → an object providing a view on D's values

class SCons.Node.Alias.AliasNodeInfo

Bases: NodeInfoBase

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state. The version is discarded.

convert ( node , val ) → None

csig

current_version_id = 2

field_list = ['csig']

format ( field_list: list[str] | None = None, names: bool = False)

merge ( other: NodeInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

str_to_node ( s)

update ( node: Node ) → None

# SCons.Node.FS module

File system nodes.

These Nodes represent the canonical external objects that people think of when they think of building software: files and directories.

This holds a “default_fs” variable that should be initialized with an FS that can be used by scripts or modules looking for the canonical default.

class SCons.Node.FS.Base ( name , directory , fs )

Bases: Node

A generic class for file system entries. This class is for when we don’t know yet whether the entry being looked up is a file or a directory. Instances of this class can morph into either Dir or File objects by a later, more precise lookup.

Note: this class does not define __cmp__ and __hash__ for efficiency reasons. SCons does a lot of comparing of Node.FS.{Base,Entry,File,Dir} objects, so those operations must be as fast as possible, which means we want to use Python’s built-in object identity comparisons.

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of BuildInfoBase

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of NodeInfoBase

RDirs ( pathlist )

Search for a list of directories in the Repository list.

Rfindalldirs ( pathlist )

SCons.Node package

83 Return all of the directories for a given path list, including corresponding “backing” directories in any repositories.

The Node lookups are relative to this Node (typically a directory), so memoizing result saves cycles from looking up the same path for each target in a given directory.

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_Rfindalldirs_key ( pathlist )

__getattr__ ( attr )

Together with the node_bwcomp dict defined below, this method provides a simple backward compatibility layer for the Node attributes ‘abspath’, ‘labspath’, ‘path’, ‘tpath’, ‘suffix’ and ‘path_elements’. These Node attributes used to be directly available in v2.3 and earlier, but have been replaced by getter methods that initialize the single variables lazily when required, in order to save memory. The redirection to the getters lets older Tools and SConstruct continue to work without any additional changes, fully transparent to the user. Note, that __getattr__ is only called as fallback when the requested attribute can’t be found, so there should be no speed performance penalty involved for standard builds.

__lt__ ( other )

less than operator used by sorting on py3

__str__ () → str

A Node.FS.Base object’s string representation is its path name.

_abspath

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_children_get () → list [Node ]

_children_reset () → None

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_sconsign

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_get_str ()

_glob1 ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False)

_labspath

_local

_memo

_path

_path_elements

_proxy

_save_str ()

_specific_sources

_tags : dict [str , Any ] | None

_tpath

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

SCons.Node package

84 add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

Return a list of alternate targets for this Node.

always_build

attributes

binfo

build ( **kw ) → None

Actually build the node.

This is called by the Taskmaster after it’s decided that the Node is out-of-date and must be rebuilt, and after the prepare() method has gotten everything, uh, prepared.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

cwd

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

dir

disambiguate ( must_exist: bool = False)

duplicate

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

SCons.Node package

85 executor_cleanup () → None

Let the executor clean up any cached information.

exists ()

Reports whether node exists.

explain ()

for_signature ()

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

fs

Reference to parent Node.FS object

get_abspath ()

Get the absolute path of the file.

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents () → bytes | str

Fetch the contents of the entry.

get_csig () → str

get_dir ()

get_env () → Environment

get_env_scanner ( env: Environment , kw: dict[str, Any] | None = {}) → ScannerBase | None

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env: Environment , scanner: ScannerBase | None , path ) → list [Node ]

Return the scanned include lines (implicit dependencies) found in this node.

The default is no implicit dependencies. We expect this method to be overridden by any subclass that can be scanned for implicit dependencies.

get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_internal_path ()

get_labspath ()

Get the absolute path of the file.

get_ninfo () → NodeInfoBase

get_path ( dir= None)

Return path relative to the current working directory of the Node.FS.Base object that owns us.

get_path_elements ()

get_relpath ()

Get the path of the file relative to the root SConstruct file’s directory.

get_source_scanner ( node: Node ) → ScannerBase | None

SCons.Node package

86 Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix ()

get_target_scanner () → ScannerBase | None

get_tpath ()

getmtime ()

getsize ()

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

is_up_to_date () → bool

SCons.Node package

87 Default check for whether the Node is current: unknown Node subtypes are always out of date, so they will always get built.

isdir () → bool

isfile () → bool

islink () → bool

linked

lstat ()

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

must_be_same ( klass )

This node, which already existed, is being looked up as the specified klass. Raise an exception if it isn’t.

name

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare () → None

Prepare for this Node to be built.

This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

ref_count

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

remove () → None

Remove this Node: no-op by default.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

rentry ()

SCons.Node package

88 reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists ()

Does this node exist locally or in a repository?

rfile ()

rstr () → str

A Node.FS.Base object’s string representation is its path name.

sbuilder

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key () → str | None

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_local () → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_src_builder ( builder ) → None

Set the source code builder for this node.

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

src_builder ()

Fetch the source code builder for this node.

If there isn’t one, we cache the source code builder specified for the directory (which in turn will cache the value from its parent directory, and so on up to the file system root).

srcnode ()

If this node is in a build path, return the node corresponding to its source file. Otherwise, return ourself.

stat ()

state

store_info

str_for_display ()

target_from_source ( prefix , suffix , splitext=<function splitext> )

Generates a target entry that corresponds to this entry (usually a source file) with the specified prefix and suffix.

Note that this method can be overridden dynamically for generated files that need different behavior. See Tool/swig.py for an example.

SCons.Node package

89 target_peers

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

wkids : list [Node ] | None

class SCons.Node.FS.Dir ( name , directory , fs )

Bases: Base

A class for directories in a file system.

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of DirBuildInfo

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

Dir ( name , create: bool = True)

Looks up or creates a directory node named ‘name’ relative to this directory.

Entry ( name )

Looks up or creates an entry node named ‘name’ relative to this directory.

File ( name )

Looks up or creates a file node named ‘name’ relative to this directory.

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of DirNodeInfo

RDirs ( pathlist )

Search for a list of directories in the Repository list.

Rfindalldirs ( pathlist )

Return all of the directories for a given path list, including corresponding “backing” directories in any repositories.

The Node lookups are relative to this Node (typically a directory), so memoizing result saves cycles from looking up the same path for each target in a given directory.

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_Rfindalldirs_key ( pathlist )

__clearRepositoryCache ( duplicate= None) → None

Called when we change the repository(ies) for a directory. This clears any cached information that is invalidated by changing the repository.

__getattr__ ( attr )

Together with the node_bwcomp dict defined below, this method provides a simple backward compatibility layer for the Node attributes ‘abspath’, ‘labspath’, ‘path’, ‘tpath’, ‘suffix’ and ‘path_elements’. These Node attributes used to be directly available in v2.3 and earlier, but have been replaced by getter methods that initialize the single variables lazily when required, in order to save memory. The redirection to the getters lets older Tools and SConstruct continue to work without any additional changes, fully transparent to the user. Note, that __getattr__ is only called as fallback when the requested attribute can’t be found, so there should be no speed performance penalty involved for standard builds.

__lt__ ( other )

less than operator used by sorting on py3

__resetDuplicate ( node ) → None

__str__ () → str

A Node.FS.Base object’s string representation is its path name.

_abspath

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

SCons.Node package

90 _children_get () → list [Node ]

_children_reset () → None

_create ()

Create this directory, silently and without worrying about whether the builder is the default or not.

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_sconsign

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_get_str ()

_glob1 ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False)

Globs for and returns a list of entry names matching a single pattern in this directory.

This searches any repositories and source directories for corresponding entries and returns a Node (or string) relative to the current directory if an entry is found anywhere.

TODO: handle pattern with no wildcard. Python’s glob.glob uses a separate _glob0 function to do this.

_labspath

_local

_memo

_morph () → None

Turn a file system Node (either a freshly initialized directory object or a separate Entry object) into a proper directory object.

Set up this directory’s entries and hook it into the file system tree. Specify that directories (this Node) don’t use signatures for calculating whether they’re current.

_path

_path_elements

_proxy

_rel_path_key ( other )

_save_str ()

_sconsign

_specific_sources

_srcdir_find_file_key ( filename )

_tags : dict [str , Any ] | None

_tpath

addRepository ( dir ) → None

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

SCons.Node package

91 Return any corresponding targets in a variant directory.

always_build

attributes

binfo

build ( **kw ) → None

A null “builder” for directories.

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

cachedir_csig

cachesig

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

contentsig

cwd

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

dir

dir_on_disk ( name )

dirname

disambiguate ( must_exist: bool = False)

diskcheck_match () → None

do_duplicate ( src ) → None

duplicate

entries

entry_abspath ( name )

entry_exists_on_disk ( name )

Searches through the file/dir entries of the current directory, and returns True if a physical entry with the given name could be found.

@see rentry_exists_on_disk

SCons.Node package

92 entry_labspath ( name )

entry_path ( name )

entry_tpath ( name )

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists ()

Reports whether node exists.

explain ()

file_on_disk ( name )

for_signature ()

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

fs

Reference to parent Node.FS object

getRepositories ()

Returns a list of repositories for this directory.

get_abspath () → str

Get the absolute path of the file.

get_all_rdirs ()

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents ()

Return content signatures and names of all our children separated by new-lines. Ensure that the nodes are sorted.

get_csig ()

Compute the content signature for Directory nodes. In general, this is not needed and the content signature is not stored in the DirNodeInfo. However, if get_contents on a Dir node is called which has a child directory, the child directory should return the hash of its contents.

get_dir ()

get_env () → Environment

get_env_scanner ( env , kw= {})

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env , scanner , path )

Return this directory’s implicit dependencies.

We don’t bother caching the results because the scan typically shouldn’t be requested more than once (as opposed to scanning .h file contents, which can be requested as many times as the files is #included by other files).

SCons.Node package

93 get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_internal_path ()

get_labspath () → str

Get the absolute path of the file.

get_ninfo () → NodeInfoBase

get_path ( dir= None)

Return path relative to the current working directory of the Node.FS.Base object that owns us.

get_path_elements ()

get_relpath ()

Get the path of the file relative to the root SConstruct file’s directory.

get_source_scanner ( node: Node ) → ScannerBase | None

Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix ()

get_target_scanner ()

get_text_contents ()

We already emit things in text, so just return the binary version.

get_timestamp () → int

Return the latest timestamp from among our children

get_tpath ()

getmtime ()

getsize ()

glob ( pathname , ondisk: bool = True, source: bool = False, strings: bool = False, exclude= None)

→ list

Returns a list of Nodes (or strings) matching a pathname pattern.

Pathname patterns follow POSIX shell syntax:

* matches everything ? matches any single character [seq] matches any character in seq (ranges allowed) [!seq] matches any char not in seq

SCons.Node package

94 The wildcard characters can be escaped by enclosing in brackets. A leading dot is not matched by a wildcard, and needs to be explicitly included in the pattern to be matched. Matches also do not span directory separators.

The matches take into account Repositories, returning a local Node if a corresponding entry exists in a Repository (either an in-memory Node or something on disk).

The underlying algorithm is adapted from a rather old version of glob.glob() function in the Python standard library (heavily modified), and uses fnmatch.fnmatch() under the covers.

This is the internal implementation of the external Glob API.

Parameters: • pattern – pathname pattern to match.

• ondisk – if false, restricts matches to in-memory Nodes. By defafult, matches entries that exist on-disk in addition to in-memory Nodes.

• source – if true, corresponding source Nodes are returned if globbing in a variant directory. The default behavior is to return Nodes local to the variant directory.

• strings – if true, returns the matches as strings instead of Nodes. The strings are path names relative to this directory.

• exclude – if not None , must be a pattern or a list of patterns following the same POSIX shell semantics. Elements matching at least one pattern from exclude will be excluded from the result.

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

is_up_to_date () → bool

If any child is not up-to-date, then this directory isn’t, either.

isdir () → bool

isfile () → bool

islink () → bool

link ( srcdir , duplicate ) → None

Set this directory as the variant directory for the supplied source directory.

linked

SCons.Node package

95 lstat ()

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder ()

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

must_be_same ( klass )

This node, which already existed, is being looked up as the specified klass. Raise an exception if it isn’t.

name

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

on_disk_entries

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare () → None

Prepare for this Node to be built.

This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

rdir ()

ref_count

rel_path ( other )

Return a path to “other” relative to this directory.

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

released_target_info

remove () → None

Remove this Node: no-op by default.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

rentry ()

rentry_exists_on_disk ( name )

SCons.Node package

96 Searches through the file/dir entries of the current and all its remote directories (repos), and returns True if a physical entry with the given name could be found. The local directory (self) gets searched first, so repositories take a lower precedence regarding the searching order.

@see entry_exists_on_disk

repositories

reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists ()

Does this node exist locally or in a repository?

rfile ()

root

rstr () → str

A Node.FS.Base object’s string representation is its path name.

sbuilder

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key ()

A directory does not get scanned.

scanner_paths

sconsign ()

Return the .sconsign file info for this directory.

searched

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_local () → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_src_builder ( builder ) → None

Set the source code builder for this node.

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

src_builder ()

Fetch the source code builder for this node.

SCons.Node package

97 If there isn’t one, we cache the source code builder specified for the directory (which in turn will cache the value from its parent directory, and so on up to the file system root).

srcdir

srcdir_duplicate ( name )

srcdir_find_file ( filename )

srcdir_list ()

srcnode ()

Dir has a special need for srcnode()…if we have a srcdir attribute set, then that is our srcnode.

stat ()

state

store_info

str_for_display ()

target_from_source ( prefix , suffix , splitext=<function splitext> )

Generates a target entry that corresponds to this entry (usually a source file) with the specified prefix and suffix.

Note that this method can be overridden dynamically for generated files that need different behavior. See Tool/swig.py for an example.

target_peers

up ()

variant_dirs

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

walk ( func , arg ) → None

Walk this directory tree by calling the specified function for each directory in the tree.

This behaves like the os.path.walk() function, but for in-memory Node.FS.Dir objects. The function takes the same arguments as the functions passed to os.path.walk():

func(arg, dirname, fnames)

Except that “dirname” will actually be the directory Node , not the string. The ‘.’ and ‘..’ entries are excluded from fnames. The fnames list may be modified in-place to filter the subdirectories visited or otherwise impose a specific order. The “arg” argument is always passed to func() and may be used in any way (or ignored, passing None is common).

wkids : list [Node ] | None

class SCons.Node.FS.DirBuildInfo

Bases: BuildInfoBase

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state.

bact

bactsig : str | None

bdepends

bdependsigs : list [BuildInfoBase ]

bimplicit

bimplicitsigs : list [BuildInfoBase ]

bsources

bsourcesigs : list [BuildInfoBase ]

current_version_id = 2

merge ( other: BuildInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

class SCons.Node.FS.DirNodeInfo

Bases: NodeInfoBase

__getstate__ () → dict [str , Any ]

SCons.Node package

98 Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state. The version is discarded.

convert ( node , val ) → None

current_version_id = 2

format ( field_list: list[str] | None = None, names: bool = False)

fs = None

merge ( other: NodeInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

str_to_node ( s)

update ( node: Node ) → None

class SCons.Node.FS.DiskChecker ( disk_check_type , do_check_function , ignore_check_function )

Bases: object

Implement disk check variation.

This Class will hold functions to determine what this particular disk checking implementation should do when enabled or disabled.

enable ( disk_check_type_list ) → None

If the current object’s disk_check_type matches any in the list passed :param disk_check_type_list: List of disk checks to enable :return:

class SCons.Node.FS.Entry ( name , directory , fs )

Bases: Base

This is the class for generic Node.FS entries–that is, things that could be a File or a Dir, but we’re just not sure yet. Consequently, the methods in this class really exist just to transform their associated object into the right class when the time comes, and then call the same-named method in the transformed class.

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of BuildInfoBase

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of NodeInfoBase

RDirs ( pathlist )

Search for a list of directories in the Repository list.

Rfindalldirs ( pathlist )

Return all of the directories for a given path list, including corresponding “backing” directories in any repositories.

The Node lookups are relative to this Node (typically a directory), so memoizing result saves cycles from looking up the same path for each target in a given directory.

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_Rfindalldirs_key ( pathlist )

__getattr__ ( attr )

Together with the node_bwcomp dict defined below, this method provides a simple backward compatibility layer for the Node attributes ‘abspath’, ‘labspath’, ‘path’, ‘tpath’, ‘suffix’ and ‘path_elements’. These Node attributes used to be directly available in v2.3 and earlier, but have been replaced by getter methods that initialize the single variables lazily when required, in order to save memory. The redirection to the getters lets older Tools and SConstruct continue to work without any additional changes, fully transparent to the user. Note, that __getattr__ is

SCons.Node package

99 only called as fallback when the requested attribute can’t be found, so there should be no speed performance penalty involved for standard builds.

__lt__ ( other )

less than operator used by sorting on py3

__str__ () → str

A Node.FS.Base object’s string representation is its path name.

_abspath

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_children_get () → list [Node ]

_children_reset () → None

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_sconsign

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_get_str ()

_glob1 ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False)

_labspath

_local

_memo

_path

_path_elements

_proxy

_save_str ()

_sconsign

_specific_sources

_tags : dict [str , Any ] | None

_tpath

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

Return a list of alternate targets for this Node.

always_build

attributes

binfo

build ( **kw ) → None

SCons.Node package

100 Actually build the node.

This is called by the Taskmaster after it’s decided that the Node is out-of-date and must be rebuilt, and after the prepare() method has gotten everything, uh, prepared.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

cachedir_csig

cachesig

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

contentsig

cwd

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

dir

dirname

disambiguate ( must_exist= False)

diskcheck_match () → None

duplicate

entries

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists ()

Reports whether node exists.

explain ()

SCons.Node package

101 for_signature ()

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

fs

Reference to parent Node.FS object

get_abspath ()

Get the absolute path of the file.

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents ()

Fetch the contents of the entry. Returns the exact binary contents of the file.

get_csig () → str

get_dir ()

get_env () → Environment

get_env_scanner ( env: Environment , kw: dict[str, Any] | None = {}) → ScannerBase | None

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env: Environment , scanner: ScannerBase | None , path ) → list [Node ]

Return the scanned include lines (implicit dependencies) found in this node.

The default is no implicit dependencies. We expect this method to be overridden by any subclass that can be scanned for implicit dependencies.

get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_internal_path ()

get_labspath ()

Get the absolute path of the file.

get_ninfo () → NodeInfoBase

get_path ( dir= None)

Return path relative to the current working directory of the Node.FS.Base object that owns us.

get_path_elements ()

get_relpath ()

Get the path of the file relative to the root SConstruct file’s directory.

get_source_scanner ( node: Node ) → ScannerBase | None

Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

SCons.Node package

102 get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix ()

get_target_scanner () → ScannerBase | None

get_text_contents () → str

Fetch the decoded text contents of a Unicode encoded Entry.

Since this should return the text contents from the file system, we check to see into what sort of subclass we should morph this Entry.

get_tpath ()

getmtime ()

getsize ()

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

is_up_to_date () → bool

SCons.Node package

103 Default check for whether the Node is current: unknown Node subtypes are always out of date, so they will always get built.

isdir () → bool

isfile () → bool

islink () → bool

linked

lstat ()

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

must_be_same ( klass ) → None

Called to make sure a Node is a Dir. Since we’re an Entry, we can morph into one.

name

new_binfo () → BuildInfoBase

new_ninfo ()

ninfo : NodeInfoBase | None

nocache

noclean

on_disk_entries

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare () → None

Prepare for this Node to be built.

This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

ref_count

rel_path ( other )

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

released_target_info

remove () → None

Remove this Node: no-op by default.

SCons.Node package

104 render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

rentry ()

repositories

reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists ()

Does this node exist locally or in a repository?

rfile ()

We’re a generic Entry, but the caller is actually looking for a File at this point, so morph into one.

root

rstr () → str

A Node.FS.Base object’s string representation is its path name.

sbuilder

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key ()

scanner_paths

searched

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_local () → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_src_builder ( builder ) → None

Set the source code builder for this node.

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

src_builder ()

Fetch the source code builder for this node.

If there isn’t one, we cache the source code builder specified for the directory (which in turn will cache the value from its parent directory, and so on up to the file system root).

srcdir

srcnode ()

SCons.Node package

105 If this node is in a build path, return the node corresponding to its source file. Otherwise, return ourself.

stat ()

state

store_info

str_for_display ()

target_from_source ( prefix , suffix , splitext=<function splitext> )

Generates a target entry that corresponds to this entry (usually a source file) with the specified prefix and suffix.

Note that this method can be overridden dynamically for generated files that need different behavior. See Tool/swig.py for an example.

target_peers

variant_dirs

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

wkids : list [Node ] | None

class SCons.Node.FS.EntryProxy ( subject )

Bases: Proxy

__get_abspath ()

__get_base_path ()

Return the file’s directory and file name, with the suffix stripped.

__get_dir ()

__get_file ()

__get_filebase ()

__get_posix_path ()

Return the path with / as the path separator, regardless of platform.

__get_relpath ()

__get_rsrcdir ()

Returns the directory containing the source node linked to this node via VariantDir(), or the directory of this node if not linked.

__get_rsrcnode ()

__get_srcdir ()

Returns the directory containing the source node linked to this node via VariantDir(), or the directory of this node if not linked.

__get_srcnode ()

__get_suffix ()

__get_windows_path ()

Return the path with as the path separator, regardless of platform.

dictSpecialAttrs = {'abspath': <function EntryProxy.__get_abspath>, 'base': <function EntryProxy.__get_base_path>, 'dir': <function EntryProxy.__get_dir>, 'file': <function EntryProxy.__get_file>, 'filebase': <function EntryProxy.__get_filebase>, 'posix': <function EntryProxy.__get_posix_path>, 'relpath': <function EntryProxy.__get_relpath>, 'rsrcdir': <function EntryProxy.__get_rsrcdir>, 'rsrcpath': <function EntryProxy.__get_rsrcnode>, 'srcdir': <function EntryProxy.__get_srcdir>, 'srcpath': <function EntryProxy.__get_srcnode>, 'suffix': <function EntryProxy.__get_suffix>, 'win32': <function EntryProxy.__get_windows_path>, 'windows': <function EntryProxy.__get_windows_path>}

get ()

Retrieve the entire wrapped object

exception SCons.Node.FS.EntryProxyAttributeError ( entry_proxy , attribute )

Bases: AttributeError

An AttributeError subclass for recording and displaying the name of the underlying Entry involved in an AttributeError exception.

add_note ()

Exception.add_note(note) – add a note to the exception

args

name

attribute name

SCons.Node package

106 obj

object

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

class SCons.Node.FS.FS ( path= None)

Bases: LocalFS

Dir ( name , directory= None, create: bool = True)

Look up or create a Dir node with the specified name. If the name is a relative path (begins with ./, ../, or a file name), then it is looked up relative to the supplied directory node, or to the top level directory of the FS (supplied at construction time) if no directory is supplied.

This method will raise TypeError if a normal file is found at the specified path.

Entry ( name , directory= None, create: bool = True)

Look up or create a generic Entry node with the specified name. If the name is a relative path (begins with ./, ../, or a file name), then it is looked up relative to the supplied directory node, or to the top level directory of the FS (supplied at construction time) if no directory is supplied.

File ( name , directory= None, create: bool = True)

Look up or create a File node with the specified name. If the name is a relative path (begins with ./, ../, or a file name), then it is looked up relative to the supplied directory node, or to the top level directory of the FS (supplied at construction time) if no directory is supplied.

This method will raise TypeError if a directory is found at the specified path.

Glob ( pathname , ondisk: bool = True, source: bool = True, strings: bool = False, exclude= None,

cwd= None)

Globs

This is mainly a shim layer

PyPackageDir ( modulename ) → Dir | None

Locate the directory of Python module modulename .

For example ‘SCons’ might resolve to Windows: C:Python311Libsite-packagesSCons Linux: /usr/lib64/python3.11/site-packages/SCons

Can be used to determine a toolpath based on a Python module name.

This is the backend called by the public API function PyPackageDir().

Repository ( *dirs ) → None

Specify Repository directories to search.

VariantDir ( variant_dir , src_dir , duplicate: int = 1)

Link the supplied variant directory to the source directory for purposes of building files.

_lookup ( p, directory , fsclass , create: bool = True)

The generic entry point for Node lookup with user-supplied data.

This translates arbitrary input into a canonical Node.FS object of the specified fsclass. The general approach for strings is to turn it into a fully normalized absolute path and then call the root directory’s lookup_abs() method for the heavy lifting.

If the path name begins with ‘#’, it is unconditionally interpreted relative to the top-level directory of this FS. ‘#’ is treated as a synonym for the top-level SConstruct directory, much like ‘~’ is treated as a synonym for the user’s home directory in a UNIX shell. So both ‘#foo’ and ‘#/foo’ refer to the ‘foo’ subdirectory underneath the top-level SConstruct directory.

If the path name is relative, then the path is looked up relative to the specified directory, or the current directory (self._cwd, typically the SConscript directory) if the specified directory is None.

chdir ( dir , change_os_dir: bool = False)

Change the current working directory for lookups. If change_os_dir is true, we will also change the “real” cwd to match.

chmod ( path , mode )

copy ( src , dst )

copy2 ( src , dst )

exists ( path )

get_max_drift ()

get_root ( drive )

Returns the root directory for the specified drive, creating it if necessary.

getcwd ()

SCons.Node package

107 getmtime ( path )

getsize ( path )

isdir ( path ) → bool

isfile ( path ) → bool

islink ( path ) → bool

link ( src , dst )

listdir ( path )

lstat ( path )

makedirs ( path , mode: int = 511, exist_ok: bool = False)

mkdir ( path , mode: int = 511)

open ( path )

readlink ( file ) → str

rename ( old , new )

scandir ( path )

set_SConstruct_dir ( dir ) → None

set_max_drift ( max_drift ) → None

stat ( path )

symlink ( src , dst )

unlink ( path )

variant_dir_target_climb ( orig , dir , tail )

Create targets in corresponding variant directories

Climb the directory tree, and look up path names relative to any linked variant directories we find.

Even though this loops and walks up the tree, we don’t memoize the return value because this is really only used to process the command-line targets.

class SCons.Node.FS.File ( name , directory , fs )

Bases: Base

A class for files in a file system.

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of FileBuildInfo

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

Dir ( name , create: bool = True)

Create a directory node named ‘name’ relative to the directory of this file.

Dirs ( pathlist )

Create a list of directories relative to the SConscript directory of this file.

Entry ( name )

Create an entry node named ‘name’ relative to the directory of this file.

File ( name )

Create a file node named ‘name’ relative to the directory of this file.

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of FileNodeInfo

RDirs ( pathlist )

Search for a list of directories in the Repository list.

Rfindalldirs ( pathlist )

Return all of the directories for a given path list, including corresponding “backing” directories in any repositories.

The Node lookups are relative to this Node (typically a directory), so memoizing result saves cycles from looking up the same path for each target in a given directory.

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

SCons.Node package

108 _Rfindalldirs_key ( pathlist )

__dmap_cache = {}

__dmap_sig_cache = {}

__getattr__ ( attr )

Together with the node_bwcomp dict defined below, this method provides a simple backward compatibility layer for the Node attributes ‘abspath’, ‘labspath’, ‘path’, ‘tpath’, ‘suffix’ and ‘path_elements’. These Node attributes used to be directly available in v2.3 and earlier, but have been replaced by getter methods that initialize the single variables lazily when required, in order to save memory. The redirection to the getters lets older Tools and SConstruct continue to work without any additional changes, fully transparent to the user. Note, that __getattr__ is only called as fallback when the requested attribute can’t be found, so there should be no speed performance penalty involved for standard builds.

__lt__ ( other )

less than operator used by sorting on py3

__str__ () → str

A Node.FS.Base object’s string representation is its path name.

_abspath

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_add_strings_to_dependency_map ( dmap )

In the case comparing node objects isn’t sufficient, we’ll add the strings for the nodes to the dependency map :return:

_build_dependency_map ( binfo )

Build mapping from file -> signature

Parameters: • self (self -)

• considered (binfo - buildinfo from node being )

Returns: dictionary of file->signature mappings

_children_get () → list [Node ]

_children_reset () → None

_createDir () → None

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_sconsign

_func_target_from_source

_get_found_includes_key ( env , scanner , path )

_get_previous_signatures ( dmap )

Return a list of corresponding csigs from previous build in order of the node/files in children.

Parameters: • self (self -)

• csig (dmap - Dictionary of file -> )

Returns: List of csigs for provided list of children

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_get_str ()

_glob1 ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False)

_labspath

_local

_memo

_morph () → None

Turn a file system node into a File object.

_path

_path_elements

SCons.Node package

109 _proxy

_rmv_existing ()

_save_str ()

_sconsign

_specific_sources

_tags : dict [str , Any ] | None

_tpath

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

Return any corresponding targets in a variant directory.

always_build

attributes

binfo

build ( **kw ) → None

Actually build the node.

This is called by the Taskmaster after it’s decided that the Node is out-of-date and must be rebuilt, and after the prepare() method has gotten everything, uh, prepared.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

builder

builder_set ( builder ) → None

built () → None

Called just after this File node is successfully built.

Just like for ‘release_target_info’ we try to release some more target node attributes in order to minimize the overall memory consumption.

@see: release_target_info

cached

cachedir_csig

cachesig

changed ( node= None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built.

For File nodes this is basically a wrapper around Node.changed(), but we allow the return value to get cached after the reference to the Executor got released in release_target_info().

@see: Node.changed()

changed_content ( target , prev_ni , repo_node= None) → bool

changed_since_last_build

changed_state ( target , prev_ni , repo_node= None) → bool

changed_timestamp_match ( target , prev_ni , repo_node= None) → bool

SCons.Node package

110 Return True if the timestamps don’t match or if there is no previous timestamp :param target: :param prev_ni: Information about the node from the previous build :return:

changed_timestamp_newer ( target , prev_ni , repo_node= None) → bool

changed_timestamp_then_content ( target , prev_ni , node= None) → bool

Used when decider for file is Timestamp-MD5

NOTE: If the timestamp hasn’t changed this will skip md5’ing the

file and just copy the prev_ni provided. If the prev_ni is wrong. It will propagate it. See: https://github.com/SCons/scons/issues/2980

Parameters: • dependency (self -)

• target (target -)

• .sconsign (prev_ni - The NodeInfo object loaded from previous builds )

• existence/timestamp (node - Node instance. Check this node for file ) – if specified.

Returns: Boolean - Indicates if node(File) has changed.

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

contentsig

convert_copy_attrs = ['bsources', 'bimplicit', 'bdepends', 'bact', 'bactsig', 'ninfo']

convert_old_entry ( old_entry )

convert_sig_attrs = ['bsourcesigs', 'bimplicitsigs', 'bdependsigs']

cwd

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

dir

dirname

disambiguate ( must_exist: bool = False)

diskcheck_match () → None

do_duplicate ( src )

Create a duplicate of this file from the specified source.

duplicate

entries

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists ()

Reports whether node exists.

explain ()

find_repo_file ()

SCons.Node package

111 For this node, find if there exists a corresponding file in one or more repositories :return: list of corresponding files in repositories

find_src_builder ()

for_signature ()

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

fs

Reference to parent Node.FS object

get_abspath ()

Get the absolute path of the file.

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_bsig ()

Return the signature for a cached file, including its children.

It adds the path of the cached file to the cache signature, because multiple targets built by the same action will all have the same build signature, and we have to differentiate them somehow.

Signature should normally be string of hex digits.

get_cachedir_csig ()

Fetch a Node’s content signature for purposes of computing another Node’s cachesig.

This is a wrapper around the normal get_csig() method that handles the somewhat obscure case of using CacheDir with the -n option. Any files that don’t exist would normally be “built” by fetching them from the cache, but the normal get_csig() method will try to open up the local file, which doesn’t exist because the -n option meant we didn’t actually pull the file from cachedir. But since the file does actually exist in the cachedir, we can use its contents for the csig.

get_content_hash () → str

Compute and return the hash for this file.

get_contents () → bytes

Return the contents of the file as bytes.

get_contents_sig ()

A helper method for get_cachedir_bsig.

It computes and returns the signature for this node’s contents.

get_csig () → str

Generate a node’s content signature.

get_dir ()

get_env () → Environment

get_env_scanner ( env: Environment , kw: dict[str, Any] | None = {}) → ScannerBase | None

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env , scanner , path )

Return the included implicit dependencies in this file. Cache results so we only scan the file once per path regardless of how many times this information is requested.

SCons.Node package

112 get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_internal_path ()

get_labspath ()

Get the absolute path of the file.

get_max_drift_csig () → str | None

Returns the content signature currently stored for this node if it’s been unmodified longer than the max_drift value, or the max_drift value is 0. Returns None otherwise.

get_ninfo () → NodeInfoBase

get_path ( dir= None)

Return path relative to the current working directory of the Node.FS.Base object that owns us.

get_path_elements ()

get_relpath ()

Get the path of the file relative to the root SConstruct file’s directory.

get_size () → int

get_source_scanner ( node: Node ) → ScannerBase | None

Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit ()

Fetch the stored implicit dependencies

get_stored_info ()

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix ()

get_target_scanner () → ScannerBase | None

get_text_contents () → str

Return the contents of the file as text.

get_timestamp () → int

get_tpath ()

getmtime ()

getsize ()

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

SCons.Node package

113 Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

has_src_builder () → bool

Return whether this Node has a source builder or not.

If this Node doesn’t have an explicit source code builder, this is where we figure out, on the fly, if there’s a transparent source code builder for it.

Note that if we found a source builder, we also set the self.builder attribute, so that all of the methods that actually

build this file don’t have to do anything different.

hash_chunksize = 65536

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

is_up_to_date () → bool

Check for whether the Node is current.

In all cases self is the target we’re checking to see if it’s up to date

isdir () → bool

isfile () → bool

islink () → bool

linked

lstat ()

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

must_be_same ( klass )

This node, which already existed, is being looked up as the specified klass. Raise an exception if it isn’t.

name

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

on_disk_entries

SCons.Node package

114 postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare ()

Prepare for this file to be created.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push the node into a cache

ref_count

rel_path ( other )

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

We’d like to remove a lot more attributes like self.sources and self.sources_set, but they might get used in a next build step. For example, during configuration the source files for a built E{*}.o file are used to figure out which linker to use for the resulting Program (gcc vs. g++)! That’s why we check for the ‘keep_targetinfo’ attribute, config Nodes and the Interactive mode just don’t allow an early release of most variables.

In the same manner, we can’t simply remove the self.attributes here. The smart linking relies on the shared flag, and some parts of the java Tool use it to transport information about nodes…

@see: built() and Node.release_target_info()

released_target_info

remove ()

Remove this file.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

rentry ()

repositories

reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns True if the node was successfully retrieved.

rexists ()

Does this node exist locally or in a repository?

rfile ()

root

rstr ()

A Node.FS.Base object’s string representation is its path name.

sbuilder

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key ()

scanner_paths

searched

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

SCons.Node package

115 set_explicit ( is_explicit: bool ) → None

set_local () → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_src_builder ( builder ) → None

Set the source code builder for this node.

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

src_builder ()

Fetch the source code builder for this node.

If there isn’t one, we cache the source code builder specified for the directory (which in turn will cache the value from its parent directory, and so on up to the file system root).

srcdir

srcnode ()

If this node is in a build path, return the node corresponding to its source file. Otherwise, return ourself.

stat ()

state

store_info

str_for_display ()

target_from_source ( prefix , suffix , splitext=<function splitext> )

Generates a target entry that corresponds to this entry (usually a source file) with the specified prefix and suffix.

Note that this method can be overridden dynamically for generated files that need different behavior. See Tool/swig.py for an example.

target_peers

variant_dirs

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

wkids : list [Node ] | None

class SCons.Node.FS.FileBuildInfo

Bases: BuildInfoBase

This is info loaded from sconsign.

Attributes unique to FileBuildInfo:

dependency_map : Caches file->csig mapping

for all dependencies. Currently this is only used when using MD5-timestamp decider. It’s used to ensure that we copy the correct csig from the previous build to be written to .sconsign when current build is done. Previously the matching of csig to file was strictly by order they appeared in bdepends, bsources, or bimplicit, and so a change in order or count of any of these could yield writing wrong csig, and then false positive rebuilds

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

SCons.Node package

116 Restore the attributes from a pickled state.

bact

bactsig : str | None

bdepends

bdependsigs : list [BuildInfoBase ]

bimplicit

bimplicitsigs : list [BuildInfoBase ]

bsources

bsourcesigs : list [BuildInfoBase ]

convert_from_sconsign ( dir , name ) → None

Converts a newly-read FileBuildInfo object for in-SCons use

For normal up-to-date checking, we don’t have any conversion to perform–but we’re leaving this method here to make that clear.

convert_to_sconsign () → None

Converts this FileBuildInfo object for writing to a .sconsign file

This replaces each Node in our various dependency lists with its usual string representation: relative to the top-level SConstruct directory, or an absolute path if it’s outside.

current_version_id = 2

dependency_map

format ( names: int = 0)

merge ( other: BuildInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

prepare_dependencies () → None

Prepares a FileBuildInfo object for explaining what changed

The bsources, bdepends and bimplicit lists have all been stored on disk as paths relative to the top-level SConstruct directory. Convert the strings to actual Nodes (for use by the –debug=explain code and –implicit-cache).

exception SCons.Node.FS.FileBuildInfoFileToCsigMappingError

Bases: Exception

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

class SCons.Node.FS.FileFinder

Bases: object

_find_file_key ( filename , paths , verbose= None)

filedir_lookup ( p, fd= None)

A helper method for find_file() that looks up a directory for a file we’re trying to find. This only creates the Dir Node if it exists on-disk, since if the directory doesn’t exist we know we won’t find any files in it… :-)

It would be more compact to just use this as a nested function with a default keyword argument (see the commented-out version below), but that doesn’t work unless you have nested scopes, so we define it here just so this work under Python 1.5.2.

find_file ( filename , paths , verbose= None)

Find a node corresponding to either a derived file or a file that exists already.

Only the first file found is returned, and none is returned if no file is found.

filename: A filename to find paths: A list of directory path nodes to search in. Can be represented as a list, a tuple, or a callable that is called with no arguments and returns the list or tuple.

returns The node created from the found file.

class SCons.Node.FS.FileNodeInfo

Bases: NodeInfoBase

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

SCons.Node package

117 __setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state. The version is discarded.

convert ( node , val ) → None

csig

current_version_id = 2

field_list = ['csig', 'timestamp', 'size']

format ( field_list: list[str] | None = None, names: bool = False)

fs = None

merge ( other: NodeInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

size

str_to_node ( s)

timestamp

update ( node: Node ) → None

SCons.Node.FS.LinkFunc ( target , source , env ) → int

Relative paths cause problems with symbolic links, so we use absolute paths, which may be a problem for people who want to move their soft-linked src-trees around. Those people should use the ‘hard-copy’ mode, softlinks cannot be used for that; at least I have no idea how …

class SCons.Node.FS.LocalFS

Bases: object

This class implements an abstraction layer for operations involving a local file system. Essentially, this wraps any function in the os, os.path or shutil modules that we use to actually go do anything with or to the local file system.

Note that there’s a very good chance we’ll refactor this part of the architecture in some way as we really implement the interface(s) for remote file system Nodes. For example, the right architecture might be to have this be a subclass instead of a base class. Nevertheless, we’re using this as a first step in that direction.

We’re not using chdir() yet because the calling subclass method needs to use os.chdir() directly to avoid recursion. Will we really need this one?

chmod ( path , mode )

copy ( src , dst )

copy2 ( src , dst )

exists ( path )

getmtime ( path )

getsize ( path )

isdir ( path ) → bool

isfile ( path ) → bool

islink ( path ) → bool

link ( src , dst )

listdir ( path )

lstat ( path )

makedirs ( path , mode: int = 511, exist_ok: bool = False)

mkdir ( path , mode: int = 511)

open ( path )

readlink ( file ) → str

rename ( old , new )

scandir ( path )

stat ( path )

symlink ( src , dst )

unlink ( path )

SCons.Node.FS.LocalString ( target , source , env ) → str

SCons.Node.FS.MkdirFunc ( target , source , env ) → int

class SCons.Node.FS.RootDir ( drive , fs )

Bases: Dir

A class for the root directory of a file system.

This is the same as a Dir class, except that the path separator (‘/’ or ‘') is actually part of the name, so we don’t need to add a separator when creating the path names of entries within this directory.

SCons.Node package

118 class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of DirBuildInfo

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

Dir ( name , create: bool = True)

Looks up or creates a directory node named ‘name’ relative to this directory.

Entry ( name )

Looks up or creates an entry node named ‘name’ relative to this directory.

File ( name )

Looks up or creates a file node named ‘name’ relative to this directory.

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of DirNodeInfo

RDirs ( pathlist )

Search for a list of directories in the Repository list.

Rfindalldirs ( pathlist )

Return all of the directories for a given path list, including corresponding “backing” directories in any repositories.

The Node lookups are relative to this Node (typically a directory), so memoizing result saves cycles from looking up the same path for each target in a given directory.

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_Rfindalldirs_key ( pathlist )

__getattr__ ( attr )

Together with the node_bwcomp dict defined below, this method provides a simple backward compatibility layer for the Node attributes ‘abspath’, ‘labspath’, ‘path’, ‘tpath’, ‘suffix’ and ‘path_elements’. These Node attributes used to be directly available in v2.3 and earlier, but have been replaced by getter methods that initialize the single variables lazily when required, in order to save memory. The redirection to the getters lets older Tools and SConstruct continue to work without any additional changes, fully transparent to the user. Note, that __getattr__ is only called as fallback when the requested attribute can’t be found, so there should be no speed performance penalty involved for standard builds.

__lt__ ( other )

less than operator used by sorting on py3

_abspath

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_children_get () → list [Node ]

_children_reset () → None

_create ()

Create this directory, silently and without worrying about whether the builder is the default or not.

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_sconsign

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_get_str ()

_glob1 ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False)

Globs for and returns a list of entry names matching a single pattern in this directory.

SCons.Node package

119 This searches any repositories and source directories for corresponding entries and returns a Node (or string) relative to the current directory if an entry is found anywhere.

TODO: handle pattern with no wildcard. Python’s glob.glob uses a separate _glob0 function to do this.

_labspath

_local

_lookupDict

_lookup_abs ( p, klass , create: bool = True)

Fast (?) lookup of a normalized absolute path.

This method is intended for use by internal lookups with already-normalized path data. For general-purpose lookups, use the FS.Entry(), FS.Dir() or FS.File() methods.

The caller is responsible for making sure we’re passed a normalized absolute path; we merely let Python’s dictionary look up and return the One True Node.FS object for the path.

If a Node for the specified “p” doesn’t already exist, and “create” is specified, the Node may be created after recursive invocation to find or create the parent directory or directories.

_memo

_morph () → None

Turn a file system Node (either a freshly initialized directory object or a separate Entry object) into a proper directory object.

Set up this directory’s entries and hook it into the file system tree. Specify that directories (this Node) don’t use signatures for calculating whether they’re current.

_path

_path_elements

_proxy

_rel_path_key ( other )

_save_str ()

_sconsign

_specific_sources

_srcdir_find_file_key ( filename )

_tags : dict [str , Any ] | None

_tpath

abspath

addRepository ( dir ) → None

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

Return any corresponding targets in a variant directory.

always_build

attributes

binfo

build ( **kw ) → None

SCons.Node package

120 A null “builder” for directories.

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

cachedir_csig

cachesig

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

contentsig

cwd

del_binfo () → None

Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

dir

dir_on_disk ( name )

dirname

disambiguate ( must_exist: bool = False)

diskcheck_match () → None

do_duplicate ( src ) → None

duplicate

entries

entry_abspath ( name )

entry_exists_on_disk ( name )

Searches through the file/dir entries of the current directory, and returns True if a physical entry with the given name could be found.

@see rentry_exists_on_disk

entry_labspath ( name )

entry_path ( name )

entry_tpath ( name )

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

SCons.Node package

121 executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists ()

Reports whether node exists.

explain ()

file_on_disk ( name )

for_signature ()

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

fs

Reference to parent Node.FS object

getRepositories ()

Returns a list of repositories for this directory.

get_abspath () → str

Get the absolute path of the file.

get_all_rdirs ()

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents ()

Return content signatures and names of all our children separated by new-lines. Ensure that the nodes are sorted.

get_csig ()

Compute the content signature for Directory nodes. In general, this is not needed and the content signature is not stored in the DirNodeInfo. However, if get_contents on a Dir node is called which has a child directory, the child directory should return the hash of its contents.

get_dir ()

get_env () → Environment

get_env_scanner ( env , kw= {})

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env , scanner , path )

Return this directory’s implicit dependencies.

We don’t bother caching the results because the scan typically shouldn’t be requested more than once (as opposed to scanning .h file contents, which can be requested as many times as the files is #included by other files).

get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_internal_path ()

SCons.Node package

122 get_labspath () → str

Get the absolute path of the file.

get_ninfo () → NodeInfoBase

get_path ( dir= None)

Return path relative to the current working directory of the Node.FS.Base object that owns us.

get_path_elements ()

get_relpath ()

Get the path of the file relative to the root SConstruct file’s directory.

get_source_scanner ( node: Node ) → ScannerBase | None

Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix ()

get_target_scanner ()

get_text_contents ()

We already emit things in text, so just return the binary version.

get_timestamp () → int

Return the latest timestamp from among our children

get_tpath ()

getmtime ()

getsize ()

glob ( pathname , ondisk: bool = True, source: bool = False, strings: bool = False, exclude= None)

→ list

Returns a list of Nodes (or strings) matching a pathname pattern.

Pathname patterns follow POSIX shell syntax:

* matches everything ? matches any single character [seq] matches any character in seq (ranges allowed) [!seq] matches any char not in seq

The wildcard characters can be escaped by enclosing in brackets. A leading dot is not matched by a wildcard, and needs to be explicitly included in the pattern to be matched. Matches also do not span directory separators.

The matches take into account Repositories, returning a local Node if a corresponding entry exists in a Repository (either an in-memory Node or something on disk).

The underlying algorithm is adapted from a rather old version of glob.glob() function in the Python standard library (heavily modified), and uses fnmatch.fnmatch() under the covers.

SCons.Node package

123 This is the internal implementation of the external Glob API.

Parameters: • pattern – pathname pattern to match.

• ondisk – if false, restricts matches to in-memory Nodes. By defafult, matches entries that exist on-disk in addition to in-memory Nodes.

• source – if true, corresponding source Nodes are returned if globbing in a variant directory. The default behavior is to return Nodes local to the variant directory.

• strings – if true, returns the matches as strings instead of Nodes. The strings are path names relative to this directory.

• exclude – if not None , must be a pattern or a list of patterns following the same POSIX shell semantics. Elements matching at least one pattern from exclude will be excluded from the result.

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

is_up_to_date () → bool

If any child is not up-to-date, then this directory isn’t, either.

isdir () → bool

isfile () → bool

islink () → bool

link ( srcdir , duplicate ) → None

Set this directory as the variant directory for the supplied source directory.

linked

lstat ()

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

SCons.Node package

124 multiple_side_effect_has_builder ()

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

must_be_same ( klass ) → None

This node, which already existed, is being looked up as the specified klass. Raise an exception if it isn’t.

name

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

on_disk_entries

path

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare () → None

Prepare for this Node to be built.

This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

rdir ()

ref_count

rel_path ( other )

Return a path to “other” relative to this directory.

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

released_target_info

remove () → None

Remove this Node: no-op by default.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

rentry ()

rentry_exists_on_disk ( name )

Searches through the file/dir entries of the current and all its remote directories (repos), and returns True if a physical entry with the given name could be found. The local directory (self) gets searched first, so repositories take a lower precedence regarding the searching order.

@see entry_exists_on_disk

repositories

SCons.Node package

125 reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists ()

Does this node exist locally or in a repository?

rfile ()

root

rstr () → str

A Node.FS.Base object’s string representation is its path name.

sbuilder

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key ()

A directory does not get scanned.

scanner_paths

sconsign ()

Return the .sconsign file info for this directory.

searched

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_local () → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_src_builder ( builder ) → None

Set the source code builder for this node.

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

src_builder ()

Fetch the source code builder for this node.

If there isn’t one, we cache the source code builder specified for the directory (which in turn will cache the value from its parent directory, and so on up to the file system root).

srcdir

srcdir_duplicate ( name )

srcdir_find_file ( filename )

srcdir_list ()

SCons.Node package

126 srcnode ()

Dir has a special need for srcnode()…if we have a srcdir attribute set, then that is our srcnode.

stat ()

state

store_info

str_for_display ()

target_from_source ( prefix , suffix , splitext=<function splitext> )

Generates a target entry that corresponds to this entry (usually a source file) with the specified prefix and suffix.

Note that this method can be overridden dynamically for generated files that need different behavior. See Tool/swig.py for an example.

target_peers

up ()

variant_dirs

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

walk ( func , arg ) → None

Walk this directory tree by calling the specified function for each directory in the tree.

This behaves like the os.path.walk() function, but for in-memory Node.FS.Dir objects. The function takes the same arguments as the functions passed to os.path.walk():

func(arg, dirname, fnames)

Except that “dirname” will actually be the directory Node , not the string. The ‘.’ and ‘..’ entries are excluded from fnames. The fnames list may be modified in-place to filter the subdirectories visited or otherwise impose a specific order. The “arg” argument is always passed to func() and may be used in any way (or ignored, passing None is common).

wkids : list [Node ] | None

SCons.Node.FS.UnlinkFunc ( target , source , env ) → int

class SCons.Node.FS._Null

Bases: object

SCons.Node.FS._classEntry

alias of Entry

SCons.Node.FS._copy_func ( fs , src , dest ) → None

SCons.Node.FS._hardlink_func ( fs , src , dst ) → None

SCons.Node.FS._my_normcase ( x)

SCons.Node.FS._softlink_func ( fs , src , dst ) → None

SCons.Node.FS.diskcheck_types ()

SCons.Node.FS.do_diskcheck_match ( node , predicate , errorfmt )

SCons.Node.FS.find_file ( filename , paths , verbose= None)

Find a node corresponding to either a derived file or a file that exists already.

Only the first file found is returned, and none is returned if no file is found.

filename: A filename to find paths: A list of directory path nodes to search in. Can be represented as a list, a tuple, or a callable that is called with no arguments and returns the list or tuple.

returns The node created from the found file.

SCons.Node.FS.get_MkdirBuilder ()

SCons.Node.FS.get_default_fs ()

SCons.Node.FS.has_glob_magic ( s) → bool

SCons.Node.FS.ignore_diskcheck_match ( node , predicate , errorfmt ) → None

SCons.Node.FS.initialize_do_splitdrive () → None

Set up splitdrive usage.

Avoid unnecessary function calls by recording a flag that tells us whether or not os.path.splitdrive() actually does anything on this system, and therefore whether we need to bother calling it when looking up path names in various methods below.

If do_splitdrive is True,_my_splitdrive() will be a real function which we can call. As all supported Python versions’ ntpath module now handle UNC paths correctly, we no longer special-case that.

SCons.Node package

127 Deferring the setup of _my_splitdrive also lets unit tests do their thing and test UNC path handling on a POSIX host.

SCons.Node.FS.invalidate_node_memos ( targets ) → None

Invalidate the memoized values of all Nodes (files or directories) that are associated with the given entries. Has been added to clear the cache of nodes affected by a direct execution of an action (e.g. Delete/Copy/Chmod). Existing Node caches become inconsistent if the action is run through Execute(). The argument targets can be a single Node object or filename, or a sequence of Nodes/filenames.

SCons.Node.FS.needs_normpath_match ( string , pos= 0, endpos= 9223372036854775807)

Matches zero or more characters at the beginning of the string.

SCons.Node.FS.save_strings ( val ) → None

SCons.Node.FS.sconsign_dir ( node )

Return the .sconsign file info for this directory, creating it first if necessary.

SCons.Node.FS.sconsign_none ( node )

SCons.Node.FS.set_diskcheck ( enabled_checkers ) → None

SCons.Node.FS.set_duplicate ( duplicate )

# SCons.Node.Python module

Python nodes.

class SCons.Node.Python.Value ( value , built_value= None, name= None)

Bases: Node

A Node class for values represented by Python expressions.

Values are typically passed on the command line or generated by a script, but not from a file or some other source.

Changed in version 4.0: the name parameter was added.

class Attrs

Bases: object

A generic place to store extra information about the Node.

Defines __slots__ for performance, but different consumers define their own attributes, so to avoid having to collect them all here, we add a __dict__ slot to get dynamic attributes.

shared

BuildInfo

alias of ValueBuildInfo

Decider ( function: Callable[[Node, Node, NodeInfoBase, Node | None], bool] ) → None

GetTag ( key: str ) → Any | None

Return a user-defined tag.

NodeInfo

alias of ValueNodeInfo

Tag ( key: str , value: Any | None ) → None

Add a user-defined tag.

_add_child ( collection: list[Node] , set: set[Node] , child: list[Node] ) → None

Adds ‘child’ to ‘collection’, first checking ‘set’ to see if it’s already present.

_children_get () → list [Node ]

_children_reset () → None

_func_exists

_func_get_contents

_func_is_derived

_func_rexists

_func_target_from_source

_get_scanner ( env: Environment , initial_scanner: ScannerBase | None , root_node_scanner: ScannerBase | None , kw: dict[str, Any] | None ) → ScannerBase | None

_memo

_specific_sources

_tags : dict [str , Any ] | None

add_dependency ( depend: list[Node] ) → None

Adds dependencies.

add_ignore ( depend: list[Node] ) → None

SCons.Node package

128 Adds dependencies to ignore.

add_prerequisite ( prerequisite: list[Node] ) → None

Adds prerequisites

add_source ( source: list[Node] ) → None

Adds sources.

add_to_implicit ( deps: list[Node] ) → None

add_to_waiting_parents ( node: Node ) → int

Returns the number of nodes added to our waiting parents list: 1 if we add a unique waiting parent, 0 if not. (Note that the returned values are intended to be used to increment a reference count, so don’t think you can “clean up” this function by using True and False instead…)

add_to_waiting_s_e ( node: Node ) → None

add_wkid ( wkid: Node ) → None

Add a node to the list of kids waiting to be evaluated

all_children ( scan: bool = True) → list [Node ]

Return a list of all the node’s direct children.

alter_targets ()

Return a list of alternate targets for this Node.

always_build

attributes

binfo

build ( **kw ) → None

Actually build the node.

This is called by the Taskmaster after it’s decided that the Node is out-of-date and must be rebuilt, and after the prepare() method has gotten everything, uh, prepared.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

builder

builder_set ( builder: BuilderBase | None ) → None

built () → None

Called just after this node is successfully built.

cached

changed ( node: Node | None = None, allowcache: bool = False) → bool

Returns if the node is up-to-date with respect to the BuildInfo stored last time it was built. The default behavior is to compare it against our own previously stored BuildInfo, but the stored BuildInfo from another Node (typically one in a Repository) can be used instead.

Note that we now always check every dependency. We used to short-circuit the check by returning as soon as we detected any difference, but we now rely on checking every dependency to make sure that any necessary Node information (for example, the content signature of an #included .h file) is updated.

The allowcache option was added for supporting the early release of the executor/builder structures, right after a File target was built. When set to true, the return value of this changed method gets cached for File nodes. Like this, the executor isn’t needed any longer for subsequent calls to changed().

@see: FS.File.changed(), FS.File.release_target_info()

changed_since_last_build

check_attributes ( name: str ) → Any | None

Simple API to check if the node.attributes for name has been set

children ( scan: bool = True) → list [Node ]

Return a list of the node’s direct children, minus those that are ignored by this node.

children_are_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

clear () → None

Completely clear a Node of all its cached state (so that it can be re-evaluated by interfaces that do continuous integration builds).

clear_memoized_values () → None

del_binfo () → None

SCons.Node package

129 Delete the build info from this node.

depends : list [Node ]

depends_set : set [Node ]

disambiguate ( must_exist: bool = False)

env : Environment | None

env_set ( env: Environment , safe: bool = False) → None

executor

executor_cleanup () → None

Let the executor clean up any cached information.

exists () → bool

Reports whether node exists.

explain ()

for_signature () → str

Return a string representation of the Node that will always be the same for this particular Node, no matter what. This is by contrast to the __str__() method, which might, for instance, return a relative path for a file Node. The purpose of this method is to generate a value to be used in signature calculation for the command line used to build a target, and we use this method instead of str() to avoid unnecessary rebuilds. This method does not need to return something that would actually work in a command line; it can return any kind of nonsense, so long as it does not change.

get_abspath () → str

Return an absolute path to the Node. This will return simply str(Node) by default, but for Node types that have a concept of relative path, this might return something different.

get_binfo () → BuildInfoBase

Fetch a node’s build information.

node - the node whose sources will be collected cache - alternate node to use for the signature cache returns - the build signature

This no longer handles the recursive descent of the node’s children’s signatures. We expect that they’re already built and updated by someone else, if that’s what’s wanted.

get_build_env () → Environment

Fetch the appropriate Environment to build this node.

get_build_scanner_path ( scanner: ScannerBase )

Fetch the appropriate scanner path for this node.

get_builder ( default_builder: BuilderBase | None = None) → BuilderBase | None

Return the set builder, or a specified default value

get_cachedir_csig () → str

get_contents () → bytes

Get contents for signature calculations.

get_csig ( calc= None)

Because we’re a Python value node and don’t have a real timestamp, we get to ignore the calculator and just use the value contents.

Returns string. Ideally string of hex digits. (Not bytes)

get_env () → Environment

get_env_scanner ( env: Environment , kw: dict[str, Any] | None = {}) → ScannerBase | None

get_executor ( create: bool = True) → Executor

Fetch the action executor for this node. Create one if there isn’t already one, and requested to do so.

get_found_includes ( env: Environment , scanner: ScannerBase | None , path ) → list [Node ]

Return the scanned include lines (implicit dependencies) found in this node.

The default is no implicit dependencies. We expect this method to be overridden by any subclass that can be scanned for implicit dependencies.

get_implicit_deps ( env: Environment , initial_scanner: ScannerBase | None , path_func , kw= {}) →

list [Node ]

Return a list of implicit dependencies for this node.

This method exists to handle recursive invocation of the scanner on the implicit dependencies returned by the scanner, if the scanner’s recursive flag says that we should.

get_ninfo () → NodeInfoBase

get_source_scanner ( node: Node ) → ScannerBase | None

SCons.Node package

130 Fetch the source scanner for the specified node

NOTE: “self” is the target being built, “node” is the source file for which we want to fetch the scanner.

Implies self.has_builder() is true; again, expect to only be called from locations where this is already verified.

This function may be called very often; it attempts to cache the scanner found to improve performance.

get_state () → int

get_stored_implicit () → list [Node ] | None

Fetch the stored implicit dependencies

get_stored_info () → SConsignEntry | None

get_string ( for_signature: bool ) → str

This is a convenience function designed primarily to be used in command generators (i.e., CommandGeneratorActions or Environment variables that are callable), which are called with a for_signature argument that is nonzero if the command generator is being called to generate a signature for the command line, which determines if we should rebuild or not.

Such command generators should use this method in preference to str(Node) when converting a Node to a string, passing in the for_signature parameter, such that we will call Node.for_signature() or str(Node) properly, depending on whether we are calculating a signature or actually constructing a command line.

get_subst_proxy ()

This method is expected to return an object that will function exactly like this Node, except that it implements any additional special features that we would like to be in effect for Environment variable substitution. The principle use is that some Nodes would like to implement a __getattr__() method, but putting that in the Node type itself has a tendency to kill performance. We instead put it in a proxy and return it from this method. It is legal for this method to return self if no new functionality is needed for Environment substitution.

get_suffix () → str

get_target_scanner () → ScannerBase | None

get_text_contents () → str

By the assumption that the node.built_value is a deterministic product of the sources, the contents of a Value are the concatenation of all the contents of its sources. As the value need not be built when get_contents() is called, we cannot use the actual node.built_value.

has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

has_explicit_builder () → bool

Return whether this Node has an explicit builder.

This allows an internal Builder created by SCons to be marked non-explicit, so that it can be overridden by an explicit builder that the user supplies (the canonical example being directories).

ignore : list [Node ]

ignore_set : set [Node ]

implicit : list [Node ] | None

implicit_set

includes : list [str ] | None

is_conftest () → bool

Returns true if this node is an conftest node

is_derived () → bool

Returns true if this node is derived (i.e. built).

This should return true only for nodes whose path should be in the variant directory when duplicate=0 and should contribute their build signatures when they are used as source files to other derived files. For example: source with source builders are not derived in this sense, and hence should not return true.

is_explicit

is_literal () → bool

Always pass the string representation of a Node to the command interpreter literally.

is_sconscript () → bool

Returns true if this node is an sconscript

is_under ( dir ) → bool

SCons.Node package

131 is_up_to_date () → bool

Alternate check for whether the Node is current: If all of our children were up-to-date, then this Node was up-to-date, too.

The SCons.Node.Alias and SCons.Node.Python.Value subclasses rebind their current() method to this method.

linked

make_ready () → None

Get a Node ready for evaluation.

This is called before the Taskmaster decides if the Node is up-to-date or not. Overriding this method allows for a Node subclass to be disambiguated if necessary, or for an implicit source builder to be attached.

missing () → bool

multiple_side_effect_has_builder () → bool

Return whether this Node has a builder or not.

In Boolean tests, this turns out to be a lot more efficient than simply examining the builder attribute directly (“if node.builder: …”). When the builder attribute is examined directly, it ends up calling __getattr__ for both the __len__ and __bool__ attributes on instances of our Builder Proxy class(es), generating a bazillion extra calls and slowing things down immensely.

new_binfo () → BuildInfoBase

new_ninfo () → NodeInfoBase

ninfo : NodeInfoBase | None

nocache

noclean

postprocess () → None

Clean up anything we don’t need to hang onto after we’ve been built.

precious

prepare () → None

Prepare for this Node to be built.

This is called after the Taskmaster has decided that the Node is out-of-date and must be rebuilt, but before actually calling the method to build the Node.

This default implementation checks that explicit or implicit dependencies either exist or are derived, and initializes the BuildInfo structure that will hold the information about how this node is, uh, built.

(The existence of source files is checked separately by the Executor, which aggregates checks for all of the targets built by a specific action.)

Overriding this method allows for for a Node subclass to remove the underlying file from the file system. Note that subclass methods should call this base class method to get the child check and the BuildInfo structure.

prerequisites : UniqueList | None

pseudo

push_to_cache () → bool

Try to push a node into a cache

read ()

Return the value. If necessary, the value is built.

ref_count

release_target_info () → None

Called just after this node has been marked up-to-date or was built completely.

This is where we try to release as many target node infos as possible for clean builds and update runs, in order to minimize the overall memory consumption.

By purging attributes that aren’t needed any longer after a Node (=File) got built, we don’t have to care that much how many KBytes a Node actually requires…as long as we free the memory shortly afterwards.

@see: built() and File.release_target_info()

remove () → None

Remove this Node: no-op by default.

render_include_tree ()

Return a text representation, suitable for displaying to the user, of the include tree for the sources of this node.

reset_executor () → None

Remove cached executor; forces recompute when needed.

retrieve_from_cache () → bool

Try to retrieve the node’s content from a cache

SCons.Node package

132 This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in built().

Returns true if the node was successfully retrieved.

rexists () → bool

Does this node exist locally or in a repository?

scan () → None

Scan this node’s dependents for implicit dependencies.

scanner_key () → str | None

select_scanner ( scanner: ScannerBase ) → ScannerBase | None

Selects a scanner for this Node.

This is a separate method so it can be overridden by Node subclasses (specifically, Node.FS.Dir) that must use their own Scanner and don’t select one the Scanner.Selector that’s configured for the target.

set_always_build ( always_build: bool = True) → None

Set the Node’s always_build value.

set_executor ( executor: Executor ) → None

Set the action executor for this node.

set_explicit ( is_explicit: bool ) → None

set_nocache ( nocache: bool = True) → None

Set the Node’s nocache value.

set_noclean ( noclean: bool = True) → None

Set the Node’s noclean value.

set_precious ( precious: bool = True) → None

Set the Node’s precious value.

set_pseudo ( pseudo: bool = True) → None

Set the Node’s pseudo value.

set_specific_source ( source: list[Node] ) → None

set_state ( state: int ) → None

side_effect

side_effects : list [Node ]

sources : list [Node ]

sources_set : set [Node ]

state

store_info

str_for_display ()

target_peers

visited () → None

Called just after this node has been visited (with or without a build).

waiting_parents : set [Node ]

waiting_s_e : set [Node ]

wkids : list [Node ] | None

write ( built_value ) → None

Set the value of the node.

class SCons.Node.Python.ValueBuildInfo

Bases: BuildInfoBase

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state.

bact

bactsig : str | None

bdepends

bdependsigs : list [BuildInfoBase ]

bimplicit

bimplicitsigs : list [BuildInfoBase ]

SCons.Node package

133 bsources

bsourcesigs : list [BuildInfoBase ]

current_version_id = 2

merge ( other: BuildInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

class SCons.Node.Python.ValueNodeInfo

Bases: NodeInfoBase

__getstate__ () → dict [str , Any ]

Return all fields that shall be pickled. Walk the slots in the class hierarchy and add those to the state dictionary. If a ‘__dict__’ slot is available, copy all entries to the dictionary. Also include the version id, which is fixed for all instances of a class.

__setstate__ ( state: dict[str, Any] ) → None

Restore the attributes from a pickled state. The version is discarded.

convert ( node , val ) → None

csig

current_version_id = 2

field_list = ['csig']

format ( field_list: list[str] | None = None, names: bool = False)

merge ( other: NodeInfoBase ) → None

Merge the fields of another object into this object. Already existing information is overwritten by the other instance’s data. WARNING: If a ‘__dict__’ slot is added, it should be updated instead of replaced.

str_to_node ( s)

update ( node: Node ) → None

SCons.Node.Python.ValueWithMemo ( value , built_value= None, name= None)

Memoized Value node factory.

Changed in version 4.0: the name parameter was added.

# SCons.Platform package

# Module contents

SCons platform selection.

Looks for modules that define a callable object that can modify a construction environment as appropriate for a given platform.

Note that we take a more simplistic view of “platform” than Python does. We’re looking for a single string that determines a set of tool-independent variables with which to initialize a construction environment. Consequently, we’ll examine both sys.platform and os.name (and anything else that might come in to play) in order to return some specification which is unique enough for our purposes.

Note that because this subsystem just selects a callable that can modify a construction environment, it’s possible for people to define their own “platform specification” in an arbitrary callable function. No one needs to use or tie in to this subsystem in order to roll their own platform definition.

SCons.Platform.DefaultToolList ( platform , env )

Select a default tool list for the specified platform.

SCons.Platform.Platform ( name= 'darwin')

Select a canned Platform specification.

class SCons.Platform.PlatformSpec ( name , generate )

Bases: object

class SCons.Platform.TempFileMunge ( cmd , cmdstr= None)

Bases: object

Convert long command lines to use a temporary file.

You can set an Environment variable (usually TEMPFILE ) to this, then call it with a string argument, and it will perform temporary file substitution on it. This is used to circumvent limitations on the length of command lines. Example:

SCons.Platform package

134 env["TEMPFILE"] = TempFileMunge env["LINKCOM"] = "${TEMPFILE('$LINK $TARGET $SOURCES', '$LINKCOMSTR')}"

By default, the name of the temporary file used begins with a prefix of ‘@’. This may be configured for other tool chains by setting the TEMPFILEPREFIX variable. Example:

env["TEMPFILEPREFIX"] = '-@' # diab compiler env["TEMPFILEPREFIX"] = '-via' # arm tool chain env["TEMPFILEPREFIX"] = '' # (the empty string) PC Lint

You can configure the extension of the temporary file through the TEMPFILESUFFIX variable, which defaults to ‘.lnk’ (see comments in the code below). Example:

env["TEMPFILESUFFIX"] = '.lnt' # PC Lint

Entries in the temporary file are separated by the value of the TEMPFILEARGJOIN variable, which defaults to an OS-appropriate value.

A default argument escape function is SCons.Subst.quote_spaces . If you need to apply extra operations on a command argument before writing to a temporary file(fix Windows slashes, normalize paths, etc.), please set

TEMPFILEARGESCFUNC variable to a custom function. Example:

import sys import re from SCons.Subst import quote_spaces WINPATHSEP_RE = re.compile(r"\([^"'\]|$)") def tempfile_arg_esc_func(arg): arg = quote_spaces(arg) if sys.platform != "win32": return arg # GCC requires double Windows slashes, let's use UNIX separator return WINPATHSEP_RE.sub(r"/ n", arg) env["TEMPFILEARGESCFUNC"] = tempfile_arg_esc_func

_print_cmd_str ( target , source , env , cmdstr ) → None

SCons.Platform.platform_default ()

Return the platform string for our execution environment.

The returned value should map to one of the SCons/Platform/*.py files. Since scons is architecture independent, though, we don’t care about the machine architecture.

SCons.Platform.platform_module ( name= 'darwin')

Return the imported module for the platform.

This looks for a module name that matches the specified argument. If the name is unspecified, we fetch the appropriate default for our execution environment.

# Submodules

# SCons.Platform.aix module

Platform-specific initialization for IBM AIX systems.

SCons.Platform package

135 There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.aix.generate ( env ) → None

SCons.Platform.aix.get_xlc ( env , xlc= None, packages= [])

# SCons.Platform.cygwin module

Platform-specific initialization for Cygwin systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.cygwin.generate ( env ) → None

# SCons.Platform.darwin module

Platform-specific initialization for Mac OS X systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.darwin.generate ( env ) → None

# SCons.Platform.hpux module

Platform-specific initialization for HP-UX systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.hpux.generate ( env ) → None

# SCons.Platform.irix module

Platform-specific initialization for SGI IRIX systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.irix.generate ( env ) → None

# SCons.Platform.mingw module

Platform-specific initialization for the MinGW system.

# SCons.Platform.os2 module

Platform-specific initialization for OS/2 systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.os2.generate ( env ) → None

# SCons.Platform.posix module

Platform-specific initialization for POSIX (Linux, UNIX, etc.) systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.posix.escape ( arg )

escape shell special characters

SCons.Platform.posix.exec_popen3 ( l, env , stdout , stderr )

SCons.Platform.posix.exec_subprocess ( l, env )

SCons.Platform.posix.generate ( env ) → None

SCons.Platform.posix.piped_env_spawn ( sh , escape , cmd , args , env , stdout , stderr )

SCons.Platform package

136 SCons.Platform.posix.subprocess_spawn ( sh , escape , cmd , args , env )

# SCons.Platform.sunos module

Platform-specific initialization for Sun systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

SCons.Platform.sunos.generate ( env ) → None

# SCons.Platform.virtualenv module

Platform support for a Python virtualenv.

This is support code, not a loadable Platform module.

SCons.Platform.virtualenv.ImportVirtualenv ( env ) → None

Add virtualenv information to env .

SCons.Platform.virtualenv.IsInVirtualenv ( path: str ) → bool

Check whether path is under the virtualenv’s directory.

Returns False if not using a virtualenv.

SCons.Platform.virtualenv.Virtualenv () → str

Return whether operating in a virtualenv.

Returns the path to the virtualenv home if scons is executing within a virtualenv, else and empty string.

SCons.Platform.virtualenv._enable_virtualenv_default ()

SCons.Platform.virtualenv._ignore_virtualenv_default ()

SCons.Platform.virtualenv._inject_venv_path ( env , path_list= None) → None

Insert virtualenv-related paths from os.environe to env .

SCons.Platform.virtualenv._inject_venv_variables ( env ) → None

Copy any set virtualenv variables from os.environ to env .

SCons.Platform.virtualenv._is_path_in ( path: str , base: str ) → bool

Check if path is located under the base directory.

SCons.Platform.virtualenv._running_in_virtualenv () → bool

Check whether scons is running in a virtualenv.

SCons.Platform.virtualenv.select_paths_in_venv ( path_list: str | list[str] ) → list [str ]

Filter path_list , returning values under the virtualenv.

# SCons.Platform.win32 module

Platform-specific initialization for Win32 systems.

There normally shouldn’t be any need to import this module directly. It will usually be imported through the generic SCons.Platform.Platform() selection method.

class SCons.Platform.win32.ArchDefinition ( arch , synonyms= [])

Bases: object

Determine which windows CPU were running on. A class for defining architecture-specific settings and logic.

SCons.Platform.win32.escape ( x)

SCons.Platform.win32.exec_spawn ( l, env )

SCons.Platform.win32.generate ( env )

SCons.Platform.win32.get_architecture ( arch= None)

Returns the definition for the specified architecture string.

If no string is specified, the system default is returned (as defined by the registry PROCESSOR_ARCHITECTURE value, PROCESSOR_ARCHITEW6432 environment variable, PROCESSOR_ARCHITECTURE environment variable, or the platform machine).

SCons.Platform.win32.get_program_files_dir ()

Get the location of the program files directory

SCons.Platform.win32.get_system_root ()

SCons.Platform.win32.piped_spawn ( sh , escape , cmd , args , env , stdout , stderr )

SCons.Platform.win32.spawn ( sh , escape , cmd , args , env )

SCons.Platform package

137 SCons.Platform.win32.spawnve ( mode , file , args , env )

# SCons.Scanner package

# Module contents

The Scanner package for the SCons software construction utility.

SCons.Scanner.Base

alias of ScannerBase

class SCons.Scanner.Classic ( name , suffixes , path_variable , regex , *args , **kwargs )

Bases: Current

A Scanner subclass to contain the common logic for classic CPP-style include scanning, but which can be customized to use different regular expressions to find the includes.

Note that in order for this to work “out of the box” (without overriding the find_include() and sort_key1() methods), the regular expression passed to the constructor must return the name of the include file in group 0.

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

static find_include ( include , source_dir , path )

find_include_names ( node )

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

scan ( node , path= ())

select ( node )

static sort_key ( include )

class SCons.Scanner.ClassicCPP ( name , suffixes , path_variable , regex , *args , **kwargs )

Bases: Classic

A Classic Scanner subclass which takes into account the type of bracketing used to include the file, and uses classic CPP rules for searching for the files based on the bracketing.

Note that in order for this to work, the regular expression passed to the constructor must return the leading bracket in group 0, and the contained filename in group 1.

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

static find_include ( include , source_dir , path )

SCons.Scanner package

138 find_include_names ( node )

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

scan ( node , path= ())

select ( node )

static sort_key ( include )

class SCons.Scanner.Current ( *args , **kwargs )

Bases: ScannerBase

A class for scanning files that are source files (have no builder) or are derived files and are current (which implies that they exist, either locally or in a repository).

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

select ( node )

class SCons.Scanner.FindPathDirs ( variable )

Bases: object

Class to bind a specific E{_}PATH variable name to a function that will return all of the E{_}path directories.

SCons.Scanner.Scanner ( function , *args , **kwargs )

Factory function to create a Scanner Object.

Creates the appropriate Scanner based on the type of “function”.

TODO: Deprecate this some day. We’ve moved the functionality inside the ScannerBase class and really don’t need this factory function any more. It was, however, used by some of our Tool modules, so the call probably ended up in various people’s custom modules patterned on SCons code.

class SCons.Scanner.ScannerBase ( function , name: str = 'NONE' , argument=<class 'SCons.Scanner._Null'> , skeys=<class 'SCons.Scanner._Null'> , path_function=None ,

node_class=<class 'SCons.Node.FS.Base'> , node_factory=None , scan_check=None ,

recursive=None )

Bases: object

Base class for dependency scanners.

Implements straightforward, single-pass scanning of a single file.

A Scanner is usually set up with a scanner function (and optionally a path function), but can also be a kind of dispatcher which passes control to other Scanners.

A scanner function takes three arguments: a Node to scan for dependecies, the construction environment to use, and an optional tuple of paths (as generated by the optional path function). It must return a list containing the Nodes for all the direct dependencies of the file.

The optional path function is called to return paths that can be searched for implicit dependency files. It takes five arguments: a construction environment, a Node for the directory containing the SConscript file that defined the primary target, a list of target nodes, a list of source nodes, and the optional argument for this instance.

Examples:

s = Scanner(my_scanner_function) s = Scanner(function=my_scanner_function) s = Scanner(function=my_scanner_function, argument='foo')

SCons.Scanner package

139 Parameters: • function – either a scanner function taking two or three arguments and returning a list of File Nodes; or a mapping of keys to other Scanner objects.

• name – an optional name for identifying this scanner object (defaults to “NONE”).

• argument – an optional argument that will be passed to both function and path_function .

• skeys – an optional list argument that can be used to determine if this scanner can be used for a given Node. In the case of File nodes, for example, the skeys would be file suffixes.

• path_function – an optional function which returns a tuple of the directories that can be searched for implicit dependency files. May also return a callable which is called with no args and returns the tuple (supporting Bindable class).

• node_class – optional class of Nodes which this scan will return. If not specified, defaults to SCons.Node.FS.Base. If node_class is None , then this scanner will not enforce any Node conversion and will return the raw results from function .

• node_factory – optional factory function to be called to translate the raw results returned by function into the expected node_class objects.

• scan_check – optional function to be called to first check whether this node really needs to be scanned.

• recursive – optional specifier of whether this scanner should be invoked recursively on all of the implicit dependencies it returns (for example #include lines in C source files, which may refer to header files which should themselves be scanned). May be a callable, which will be called to filter the list of nodes found to select a subset for recursive scanning (the canonical example being only recursively scanning subdirectories within a directory). The default is to not do recursive scanning.

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

select ( node )

class SCons.Scanner.Selector ( mapping , *args , **kwargs )

Bases: ScannerBase

A class for selecting a more specific scanner based on the scanner_key() (suffix) for a specific Node.

TODO: This functionality has been moved into the inner workings of the ScannerBase class, and this class will be deprecated at some point. (It was never exposed directly as part of the public interface, although it is used by the Scanner() factory function that was used by various Tool modules and therefore was likely a template for custom modules that may be out there.)

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

SCons.Scanner package

140 Add a skey to the list of skeys

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

select ( node )

class SCons.Scanner._Null

Bases: object

SCons.Scanner._null

alias of _Null

# Submodules

# SCons.Scanner.C module

Dependency scanner for C/C++ code.

Two scanners are defined here: the default CScanner, and the optional CConditionalScanner, which must be explicitly selected by calling add_scanner() for each affected suffix.

SCons.Scanner.C.CConditionalScanner ()

Return an advanced conditional Scanner instance for scanning source files

Interprets C/C++ Preprocessor conditional syntax (#ifdef, #if, defined, #else, #elif, etc.).

SCons.Scanner.C.CScanner ()

Return a prototype Scanner instance for scanning source files that use the C pre-processor

class SCons.Scanner.C.SConsCPPConditionalScanner ( *args , **kwargs )

Bases: PreProcessor

SCons-specific subclass of the cpp.py module’s processing.

We subclass this so that: 1) we can deal with files represented by Nodes, not strings; 2) we can keep track of the files that are missing.

__call__ ( file )

Pre-processes a file.

This is the main public entry point.

_do_if_else_condition ( condition ) → None

Common logic for evaluating the conditions on #if, #ifdef and #ifndef lines.

_match_tuples ( tuples )

_parse_tuples ( contents )

_process_tuples ( tuples , file= None)

all_include ( t) → None

do_define ( t) → None

Default handling of a #define line.

do_elif ( t) → None

Default handling of a #elif line.

do_else ( t) → None

Default handling of a #else line.

do_endif ( t) → None

Default handling of a #endif line.

do_if ( t) → None

Default handling of a #if line.

do_ifdef ( t) → None

Default handling of a #ifdef line.

do_ifndef ( t) → None

Default handling of a #ifndef line.

do_import ( t) → None

Default handling of a #import line.

do_include ( t) → None

Default handling of a #include line.

do_include_next ( t) → None

Default handling of a #include line.

do_nothing ( t) → None

SCons.Scanner package

141 Null method for when we explicitly want the action for a specific preprocessor directive to do nothing.

do_undef ( t) → None

Default handling of a #undef line.

eval_constant_expression ( s)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

Returns None if the eval() result is not an integer.

eval_expression ( t)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

finalize_result ( fname )

find_include_file ( t)

Finds the #include file for a given preprocessor tuple.

initialize_result ( fname ) → None

process_contents ( contents )

Pre-processes a file contents.

Is used by tests

process_file ( file )

Pre-processes a file.

This is the main internal entry point.

read_file ( file ) → str

resolve_include ( t)

Resolve a tuple-ized #include line.

This handles recursive expansion of values without “” or <> surrounding the name until an initial “ or < is found, to handle #include FILE where FILE is a #define somewhere else.

restore () → None

Pops the previous dispatch table off the stack and makes it the current one.

save () → None

Pushes the current dispatch table on the stack and re-initializes the current dispatch table to the default.

scons_current_file ( t) → None

start_handling_includes ( t= None) → None

Causes the PreProcessor object to start processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates True, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated False.

stop_handling_includes ( t= None) → None

Causes the PreProcessor object to stop processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates False, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated True.

tupleize ( contents )

Turns the contents of a file into a list of easily-processed tuples describing the CPP lines in the file.

The first element of each tuple is the line’s preprocessor directive (#if, #include, #define, etc., minus the initial ‘#’). The remaining elements are specific to the type of directive, as pulled apart by the regular expression.

class SCons.Scanner.C.SConsCPPConditionalScannerWrapper ( name , variable )

Bases: object

The SCons wrapper around a cpp.py scanner.

This is the actual glue between the calling conventions of generic SCons scanners, and the (subclass of) cpp.py class that knows how to look for #include lines with reasonably real C-preprocessor-like evaluation of #if/#ifdef/#else/#elif lines.

recurse_nodes ( nodes )

select ( node )

class SCons.Scanner.C.SConsCPPScanner ( *args , **kwargs )

Bases: PreProcessor

SCons-specific subclass of the cpp.py module’s processing.

SCons.Scanner package

142 We subclass this so that: 1) we can deal with files represented by Nodes, not strings; 2) we can keep track of the files that are missing.

__call__ ( file )

Pre-processes a file.

This is the main public entry point.

_do_if_else_condition ( condition ) → None

Common logic for evaluating the conditions on #if, #ifdef and #ifndef lines.

_match_tuples ( tuples )

_parse_tuples ( contents )

_process_tuples ( tuples , file= None)

all_include ( t) → None

do_define ( t) → None

Default handling of a #define line.

do_elif ( t) → None

Default handling of a #elif line.

do_else ( t) → None

Default handling of a #else line.

do_endif ( t) → None

Default handling of a #endif line.

do_if ( t) → None

Default handling of a #if line.

do_ifdef ( t) → None

Default handling of a #ifdef line.

do_ifndef ( t) → None

Default handling of a #ifndef line.

do_import ( t) → None

Default handling of a #import line.

do_include ( t) → None

Default handling of a #include line.

do_include_next ( t) → None

Default handling of a #include line.

do_nothing ( t) → None

Null method for when we explicitly want the action for a specific preprocessor directive to do nothing.

do_undef ( t) → None

Default handling of a #undef line.

eval_constant_expression ( s)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

Returns None if the eval() result is not an integer.

eval_expression ( t)

Evaluates a C preprocessor expression.

This is done by converting it to a Python equivalent and eval()ing it in the C preprocessor namespace we use to track #define values.

finalize_result ( fname )

find_include_file ( t)

Finds the #include file for a given preprocessor tuple.

initialize_result ( fname ) → None

process_contents ( contents )

Pre-processes a file contents.

Is used by tests

process_file ( file )

Pre-processes a file.

This is the main internal entry point.

read_file ( file ) → str

resolve_include ( t)

SCons.Scanner package

143 Resolve a tuple-ized #include line.

This handles recursive expansion of values without “” or <> surrounding the name until an initial “ or < is found, to handle #include FILE where FILE is a #define somewhere else.

restore () → None

Pops the previous dispatch table off the stack and makes it the current one.

save () → None

Pushes the current dispatch table on the stack and re-initializes the current dispatch table to the default.

scons_current_file ( t) → None

start_handling_includes ( t= None) → None

Causes the PreProcessor object to start processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates True, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated False.

stop_handling_includes ( t= None) → None

Causes the PreProcessor object to stop processing #import, #include and #include_next lines.

This method will be called when a #if, #ifdef, #ifndef or #elif evaluates False, or when we reach the #else in a #if, #ifdef, #ifndef or #elif block where a condition already evaluated True.

tupleize ( contents )

Turns the contents of a file into a list of easily-processed tuples describing the CPP lines in the file.

The first element of each tuple is the line’s preprocessor directive (#if, #include, #define, etc., minus the initial ‘#’). The remaining elements are specific to the type of directive, as pulled apart by the regular expression.

class SCons.Scanner.C.SConsCPPScannerWrapper ( name , variable )

Bases: object

The SCons wrapper around a cpp.py scanner.

This is the actual glue between the calling conventions of generic SCons scanners, and the (subclass of) cpp.py class that knows how to look for #include lines with reasonably real C-preprocessor-like evaluation of #if/#ifdef/#else/#elif lines.

recurse_nodes ( nodes )

select ( node )

SCons.Scanner.C.dictify_CPPDEFINES ( env , replace: bool = False) → dict

Return CPPDEFINES converted to a dict for preprocessor emulation.

The concept is similar to processDefines(): turn the values stored in an internal form in env['CPPDEFINES'] into one needed for a specific context - in this case the cpp-like work the C/C++ scanner will do. We can’t reuse

processDefines output as that’s a list of strings for the command line. We also can’t pass the CPPDEFINES

variable directly to the dict constructor, as SCons allows it to be stored in several different ways - it’s only after

Append and relatives has been called we know for sure it will be a deque of tuples.

If requested (replace is true), simulate some of the macro replacement that would take place if an actual preprocessor ran, to avoid some conditional inclusions comeing out wrong. A bit of an edge case, but does happen (GH #4623). See 6.10.5 in the C standard and 15.6 in the C++ standard).

Parameters: replace – if true, simulate macro replacement

Changed in version 4.9.0: Simple macro replacement added, and replace arg to enable it.

# SCons.Scanner.D module

Scanner for the Digital Mars “D” programming language.

Coded by Andy Friesen, 17 Nov 2003

class SCons.Scanner.D.D

Bases: Classic

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

SCons.Scanner package

144 static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

static find_include ( include , source_dir , path )

find_include_names ( node )

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

scan ( node , path= ())

select ( node )

static sort_key ( include )

SCons.Scanner.D.DScanner ()

Return a prototype Scanner instance for scanning D source files

# SCons.Scanner.Dir module

SCons.Scanner.Dir.DirEntryScanner ( **kwargs )

Return a prototype Scanner instance for “scanning” directory Nodes for their in-memory entries

SCons.Scanner.Dir.DirScanner ( **kwargs )

Return a prototype Scanner instance for scanning directories for on-disk files

SCons.Scanner.Dir.do_not_scan ( k)

SCons.Scanner.Dir.only_dirs ( nodes )

SCons.Scanner.Dir.scan_in_memory ( node , env , path= ())

“Scans” a Node.FS.Dir for its in-memory entries.

SCons.Scanner.Dir.scan_on_disk ( node , env , path= ())

Scans a directory for on-disk files and directories therein.

Looking up the entries will add these to the in-memory Node tree representation of the file system, so all we have to do is just that and then call the in-memory scanning function.

# SCons.Scanner.Fortran module

Dependency scanner for Fortran code.

class SCons.Scanner.Fortran.F90Scanner ( name , suffixes , path_variable , use_regex , incl_regex ,

def_regex , *args , **kwargs )

Bases: Classic

A Classic Scanner subclass for Fortran source files which takes into account both USE and INCLUDE statements. This scanner will work for both F77 and F90 (and beyond) compilers.

Currently, this scanner assumes that the include files do not contain USE statements. To enable the ability to deal with USE statements in include files, add logic right after the module names are found to loop over each include file, search for and locate each USE statement, and append each module name to the list of dependencies. Caching the search results in a common dictionary somewhere so that the same include file is not searched multiple times would be a smart thing to do.

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

SCons.Scanner package

145 static find_include ( include , source_dir , path )

find_include_names ( node )

get_skeys ( env= None)

path ( env , dir= None, target= None, source= None)

scan ( node , env , path= ())

select ( node )

static sort_key ( include )

SCons.Scanner.Fortran.FortranScan ( path_variable: str = 'FORTRANPATH')

Return a prototype Scanner instance for scanning source files for Fortran USE & INCLUDE statements

# SCons.Scanner.IDL module

Dependency scanner for IDL (Interface Definition Language) files.

SCons.Scanner.IDL.IDLScan ()

Return a prototype Scanner instance for scanning IDL source files

# SCons.Scanner.Java module

SCons.Scanner.Java.JavaScanner ()

Scanner for .java files.

Added in version 4.4.

SCons.Scanner.Java._collect_classes ( classlist , dirname , files ) → None

SCons.Scanner.Java._subst_paths ( env , paths ) → list

Return a list of substituted path elements.

If paths is a string, it is split on the search-path separator. Otherwise, substitution is done on string-valued list elements but they are not split.

Note helps support behavior like pulling in the external CLASSPATH and setting it directly into JAVACLASSPATH ,however splitting on os.pathsep makes the interpretation system-specific (this is warned about in the manpage entry for JAVACLASSPATH ).

SCons.Scanner.Java.scan ( node , env , libpath= ()) → list

Scan for files both on JAVACLASSPATH and JAVAPROCESSORPATH.

JAVACLASSPATH/JAVAPROCESSORPATH path can contain:

• Explicit paths to JAR/Zip files

• Wildcards (*)

• Directories which contain classes in an unnamed package

• Parent directories of the root package for classes in a named package

Class path entries that are neither directories nor archives (.zip or JAR files) nor the asterisk (*) wildcard character are ignored.

# SCons.Scanner.LaTeX module

Dependency scanner for LaTeX code.

class SCons.Scanner.LaTeX.FindENVPathDirs ( variable )

Bases: object

A class to bind a specific E{_}PATH variable name to a function that will return all of the E{_}path directories.

class SCons.Scanner.LaTeX.LaTeX ( name , suffixes , graphics_extensions , *args , **kwargs )

Bases: ScannerBase

Class for scanning LaTeX files for included files.

Unlike most scanners, which use regular expressions that just return the included file name, this returns a tuple consisting of the keyword for the inclusion (“include”, “includegraphics”, “input”, or “bibliography”), and then the file name itself. Based on a quick look at LaTeX documentation, it seems that we should append .tex suffix for the “include” keywords, append .tex if there is no extension for the “input” keyword, and need to add .bib for the “bibliography” keyword that does not accept extensions by itself.

SCons.Scanner package

146 Finally, if there is no extension for an “includegraphics” keyword latex will append .ps or .eps to find the file, while pdftex may use .pdf, .jpg, .tif, .mps, or .png.

The actual subset and search order may be altered by DeclareGraphicsExtensions command. This complication is ignored. The default order corresponds to experimentation with teTeX:

$ latex --version pdfeTeX 3.141592-1.21a-2.2 (Web2C 7.5.4) kpathsea version 3.5.4

The order is:

[‘.eps’, ‘.ps’] for latex [‘.png’, ‘.pdf’, ‘.jpg’, ‘.tif’].

Another difference is that the search path is determined by the type of the file being searched: env[‘TEXINPUTS’] for “input” and “include” keywords env[‘TEXINPUTS’] for “includegraphics” keyword env[‘TEXINPUTS’] for “lstinputlisting” keyword env[‘BIBINPUTS’] for “bibliography” keyword env[‘BSTINPUTS’] for “bibliographystyle” keyword env[‘INDEXSTYLE’] for “makeindex” keyword, no scanning support needed just allows user to set it if needed.

FIXME: also look for the class or style in document[class|style]{} FIXME: also look for the argument of bibliographystyle{}

__call__ ( node , env , path= ()) → list

Scans a single object.

Parameters: • node – the node that will be passed to the scanner function

• env – the environment that will be passed to the scanner function.

• path – tuple of paths from the path_function

Returns: A list of direct dependency nodes for the specified node.

_latex_names ( include_type , filename )

static _recurse_all_nodes ( nodes )

static _recurse_no_nodes ( nodes )

add_scanner ( skey , scanner ) → None

add_skey ( skey ) → None

Add a skey to the list of skeys

canonical_text ( text )

Standardize an input TeX-file contents.

Currently:

• removes comments, unwrapping comment-wrapped lines.

env_variables = ['TEXINPUTS', 'BIBINPUTS', 'BSTINPUTS', 'INDEXSTYLE']

find_include ( include , source_dir , path )

get_skeys ( env= None)

keyword_paths = {'addbibresource': 'BIBINPUTS', 'addglobalbib': 'BIBINPUTS', 'addsectionbib': 'BIBINPUTS', 'bibliography': 'BIBINPUTS', 'bibliographystyle': 'BSTINPUTS', 'include': 'TEXINPUTS', 'includegraphics': 'TEXINPUTS', 'input': 'TEXINPUTS', 'lstinputlisting': 'TEXINPUTS', 'makeindex': 'INDEXSTYLE', 'usecolortheme': 'TEXINPUTS', 'usefonttheme': 'TEXINPUTS', 'useinnertheme': 'TEXINPUTS', 'useoutertheme': 'TEXINPUTS', 'usepackage': 'TEXINPUTS', 'usetheme': 'TEXINPUTS'}

path ( env , dir= None, target= None, source= None)

scan ( node , subdir: str = '.')

scan_recurse ( node , path= ())

do a recursive scan of the top level target file This lets us search for included files based on the directory of the main file just as latex does

select ( node )

static sort_key ( include )

two_arg_commands = ['import', 'subimport', 'includefrom', 'subincludefrom', 'inputfrom', 'subinputfrom']

SCons.Scanner.LaTeX.LaTeXScanner ()

Return a prototype Scanner instance for scanning LaTeX source files when built with latex.

SCons.Scanner package

147 SCons.Scanner.LaTeX.PDFLaTeXScanner ()

Return a prototype Scanner instance for scanning LaTeX source files when built with pdflatex.

class SCons.Scanner.LaTeX._Null

Bases: object

SCons.Scanner.LaTeX._null

alias of _Null

SCons.Scanner.LaTeX.modify_env_var ( env , var , abspath )

# SCons.Scanner.Prog module

Dependency scanner for program files.

SCons.Scanner.Prog.ProgramScanner ( **kwargs )

Return a prototype Scanner instance for scanning executable files for static-lib dependencies

SCons.Scanner.Prog._subst_libs ( env , libs )

Substitute environment variables and split into list.

SCons.Scanner.Prog.scan ( node , env , libpath= ())

Scans program files for static-library dependencies.

It will search the LIBPATH environment variable for libraries specified in the LIBS variable, returning any files it finds as dependencies.

# SCons.Scanner.RC module

Dependency scanner for RC (Interface Definition Language) files.

SCons.Scanner.RC.RCScan ()

Return a prototype Scanner instance for scanning RC source files

SCons.Scanner.RC.no_tlb ( nodes )

Filter out .tlb files as they are binary and shouldn’t be scanned.

# SCons.Scanner.SWIG module

Dependency scanner for SWIG code.

SCons.Scanner.SWIG.SWIGScanner ()

# SCons.Script package

# Module contents

The main() function used by the scons script.

Architecturally, this is the scons script, and will likely only be called from the external “scons” wrapper. Consequently, anything here should not be, or be considered, part of the build engine. If it’s something that we expect other software to want to use, it should go in some other module. If it’s specific to the “scons” script invocation, it goes here.

SCons.Script.HelpFunction ( text , append: bool = False, local_only: bool = False) → None

The implementaion of the the Help method.

See Help().

Changed in version 4.6.0: The keep_local parameter was added.

Changed in version 4.9.0: The keep_local parameter was renamed local_only to match manpage

class SCons.Script.TargetList ( initlist= None)

Bases: UserList

_abc_impl = <_abc._abc_data object>

_add_Default ( list ) → None

_clear () → None

_do_nothing ( *args , **kw ) → None

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

SCons.Script package

148 count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

SCons.Script.Variables ( files= None, args= {})

SCons.Script._Add_Arguments ( alist: list[str] ) → None

Add value(s) to ARGLIST and ARGUMENTS .

SCons.Script._Add_Targets ( tlist: list[str] ) → None

Add value(s) to COMMAND_LINE_TARGETS and BUILD_TARGETS .

SCons.Script._Get_Default_Targets ( d, fs )

SCons.Script._Remove_Argument ( aarg: str ) → None

Remove aarg from ARGLIST and ARGUMENTS .

Used to remove a variables-style argument that is no longer valid. This can happpen because the command line is processed once early, before we see any SCons.Script.Main.AddOption() calls, so we could not recognize it belongs to an option and is not a standalone variable=value argument.

Added in version 4.10.0.

SCons.Script._Remove_Target ( targ: str ) → None

Remove targ from BUILD_TARGETS and COMMAND_LINE_TARGETS .

Used to remove a target that is no longer valid. This can happpen because the command line is processed once early, before we see any SCons.Script.Main.AddOption() calls, so we could not recognize it belongs to an option and is not a standalone target argument.

Since we are “correcting an error”, we also have to fix up the internal _build_plus_default list.

Added in version 4.10.0.

SCons.Script._Set_Default_Targets ( env , tlist ) → None

SCons.Script._Set_Default_Targets_Has_Been_Called ( d, fs )

SCons.Script._Set_Default_Targets_Has_Not_Been_Called ( d, fs )

SCons.Script.set_missing_sconscript_error ( flag: bool = True) → bool

Set behavior on missing file in SConscript() call.

Returns: previous value

# Submodules

# SCons.Script.Interactive module

SCons interactive mode.

class SCons.Script.Interactive.SConsInteractiveCmd ( **kw )

Bases: Cmd

build [TARGETS] Build the specified TARGETS and their dependencies. ‘b’ is a synonym. clean [TARGETS] Clean (remove) the specified TARGETS and their dependencies. ‘c’ is a synonym. exit Exit SCons interactive mode. help [COMMAND] Prints help for the specified COMMAND. ‘h’ and ‘?’ are synonyms. shell [COMMANDLINE] Execute COMMANDLINE in a subshell. ‘sh’ and ‘!’ are synonyms. version Prints SCons version information.

_do_one_help ( arg ) → None

_doc_to_help ( obj )

_strip_initial_spaces ( s)

SCons.Script package

149 cmdloop ( intro= None)

Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument.

columnize ( list , displaywidth= 80)

Display a list of strings as a compact set of columns.

Each column is only as wide as necessary. Columns are separated by two spaces (one was not legible enough).

complete ( text , state )

Return the next possible completion for ‘text’.

If a command has not been entered, then complete against command list. Otherwise try to call complete_<command> to get list of completions.

complete_help ( *args )

completedefault ( *ignored )

Method called to complete an input line when no command-specific complete_*() method is available.

By default, it returns an empty list.

completenames ( text , *ignored )

default ( argv ) → None

Called on an input line when the command prefix is not recognized.

If this method is not overridden, it prints an error message and returns.

do_EOF ( argv ) → None

do_build ( argv ) → None

build [TARGETS] Build the specified TARGETS and their dependencies. ‘b’ is a synonym.

do_clean ( argv )

clean [TARGETS] Clean (remove) the specified TARGETS and their dependencies. ‘c’ is a synonym.

do_exit ( argv ) → None

exit Exit SCons interactive mode.

do_help ( argv ) → None

help [COMMAND] Prints help for the specified COMMAND. ‘h’ and ‘?’ are synonyms.

do_shell ( argv ) → None

shell [COMMANDLINE] Execute COMMANDLINE in a subshell. ‘sh’ and ‘!’ are synonyms.

do_version ( argv ) → None

version Prints SCons version information.

doc_header = 'Documented commands (type help <topic>):'

doc_leader = ''

emptyline ()

Called when an empty line is entered in response to the prompt.

If this method is not overridden, it repeats the last nonempty command entered.

get_names ()

identchars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

intro = None

lastcmd = ''

misc_header = 'Miscellaneous help topics:'

nohelp = '*** No help on %s'

onecmd ( line )

Interpret the argument as though it had been typed in response to the prompt.

This may be overridden, but should not normally need to be; see the precmd() and postcmd() methods for useful execution hooks. The return value is a flag indicating whether interpretation of commands by the interpreter should stop.

parseline ( line )

Parse the line into a command name and a string containing the arguments. Returns a tuple containing (command, args, line). ‘command’ and ‘args’ may be None if the line couldn’t be parsed.

postcmd ( stop , line )

Hook method executed just after a command dispatch is finished.

postloop ()

Hook method executed once when the cmdloop() method is about to return.

precmd ( line )

SCons.Script package

150 Hook method executed just before the command line is interpreted, but after the input prompt is generated and issued.

preloop ()

Hook method executed once when the cmdloop() method is called.

print_topics ( header , cmds , cmdlen , maxcol )

prompt = '(Cmd) '

ruler = '='

synonyms = {'b': 'build', 'c': 'clean', 'h': 'help', 'scons': 'build', 'sh': 'shell'}

undoc_header = 'Undocumented commands:'

use_rawinput = 1

SCons.Script.Interactive.interact ( fs , parser , options , targets , target_top ) → None

# SCons.Script.Main module

The main() function used by the scons script.

Architecturally, this is the scons script, and will likely only be called from the external “scons” wrapper. Consequently, anything here should not be, or be considered, part of the build engine. If it’s something that we expect other software to want to use, it should go in some other module. If it’s specific to the “scons” script invocation, it goes here.

SCons.Script.Main.AddOption ( *args , **kw ) → SConsOption

Add a local option to the option parser - Public API.

If the SCons-specific settable kwarg is true (default False ), the option will allow calling SetOption().

Changed in version 4.8.0: The settable parameter added to allow including the new option in the table of options eligible to use SetOption().

class SCons.Script.Main.BuildTask ( tm , targets , top , node )

Bases: OutOfDateTask

An SCons build task.

LOGGER = None

_abc_impl = <_abc._abc_data object>

_exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

_no_exception_to_raise () → None

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

do_failed ( status: int = 2) → None

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute () → None

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

executed ()

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call

SCons.Script package

151 “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed () → None

Default action when a task fails: stop the build.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

get_target ()

Fetch the target being built or updated by this task.

make_ready () → None

Make a task ready for execution

make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

needs_execute () → bool

Returns True (indicating this Task should be executed) if this Task’s target state indicates it needs executing, which has already been determined by an earlier up-to-date check.

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare ()

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

trace_message ( node , description: str = 'node') → None

class SCons.Script.Main.CleanTask ( tm , targets , top , node )

Bases: AlwaysTask

An SCons clean task.

LOGGER = None

_abc_impl = <_abc._abc_data object>

_clean_targets ( remove: bool = True) → None

SCons.Script package

152 _exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

_get_files_to_clean ()

_no_exception_to_raise () → None

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute () → None

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

executed () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed () → None

Default action when a task fails: stop the build.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fs_delete ( path , pathstr , remove: bool = True)

get_target ()

Fetch the target being built or updated by this task.

make_ready () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

SCons.Script package

153 make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

needs_execute () → bool

Always returns True (indicating this Task should always be executed).

Subclasses that need this behavior (as opposed to the default of only executing Nodes that are out of date w.r.t. their dependencies) can use this as follows:

class MyTaskSubclass(SCons.Taskmaster.Task):

needs_execute = SCons.Taskmaster.AlwaysTask.needs_execute

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare () → None

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

remove () → None

show () → None

trace_message ( node , description: str = 'node') → None

SCons.Script.Main.DebugOptions ( json: str | None = None) → None

Specify options to SCons debug logic - Public API.

Currently only json is supported, which changes the JSON file written to if the --debug=json command-line option is specified to the value supplied.

Added in version 4.6.0.

class SCons.Script.Main.FakeOptionParser

Bases: object

A do-nothing option parser, used for the initial OptionsParser value.

During normal SCons operation, the OptionsParser is created right away by the main() function. Certain test scripts however, can introspect on different Tool modules, the initialization of which can try to add a new, local option to an otherwise uninitialized OptionsParser object. This allows that introspection to happen without blowing up.

class FakeOptionValues

Bases: object

add_local_option ( *args , **kw ) → SConsOption

values = <SCons.Script.Main.FakeOptionParser.FakeOptionValues object>

SCons.Script.Main.GetBuildFailures ()

SCons.Script.Main.GetOption ( name: str )

Get the value from an option - Public API.

SCons.Script.Main.PrintHelp ( file= None, local_only: bool = False) → None

SCons.Script.Main.Progress ( *args , **kw ) → None

Show progress during building - Public API.

class SCons.Script.Main.Progressor ( obj , interval: int = 1, file= None, overwrite: bool = False)

Bases: object

count = 0

erase_previous () → None

prev = ''

replace_string ( node ) → None

spinner ( node ) → None

string ( node ) → None

target_string = '$TARGET'

SCons.Script package

154 write ( s) → None

class SCons.Script.Main.QuestionTask ( tm , targets , top , node )

Bases: AlwaysTask

An SCons task for the -q (question) option.

LOGGER = None

_abc_impl = <_abc._abc_data object>

_exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

_no_exception_to_raise () → None

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute () → None

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

executed () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed () → None

Default action when a task fails: stop the build.

SCons.Script package

155 Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

get_target ()

Fetch the target being built or updated by this task.

make_ready ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

needs_execute () → bool

Always returns True (indicating this Task should always be executed).

Subclasses that need this behavior (as opposed to the default of only executing Nodes that are out of date w.r.t. their dependencies) can use this as follows:

class MyTaskSubclass(SCons.Taskmaster.Task):

needs_execute = SCons.Taskmaster.AlwaysTask.needs_execute

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare () → None

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

trace_message ( node , description: str = 'node') → None

exception SCons.Script.Main.SConsPrintHelpException

Bases: Exception

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

SCons.Script.Main.SetOption ( name: str , value )

Set the value of an option - Public API.

class SCons.Script.Main.TreePrinter ( derived: bool = False, prune: bool = False, status: bool =

False, sLineDraw: bool = False)

Bases: object

display ( t) → None

get_all_children ( node )

get_derived_children ( node )

SCons.Script.Main.ValidateOptions ( throw_exception: bool = False) → None

Validate options passed to SCons on the command line.

Checks that all options given on the command line are known to this instance of SCons. Call after all of the cli options have been set up through AddOption() calls. For example, if you added an option --xyz and you call SCons with

--xyy you can cause SCons to issue an error message and exit by calling this function.

Parameters: throw_exception – if an invalid option is present on the command line, raises an exception if this optional parameter evaluates true; if false (the default), issue a message and exit with error status.

SCons.Script package

156 Raises: SConsBadOptionError – If throw_exception is true and there are invalid options on the command line.

Added in version 4.5.0.

SCons.Script.Main._SConstruct_exists ( dirname: str , repositories: list[str] , filelist: list[str] )

→ str | None

Check that an SConstruct file exists in a directory.

Parameters: • dirname – the directory to search. If empty, look in cwd.

• repositories – a list of repositories to search in addition to the project directory tree.

• filelist – names of SConstruct file(s) to search for. If empty list, use the built-in list of names.

Returns: The path to the located SConstruct file, or None .

SCons.Script.Main._build_targets ( fs , options , targets , target_top )

SCons.Script.Main._create_path ( plist )

SCons.Script.Main._exec_main ( parser , values ) → None

SCons.Script.Main._load_all_site_scons_dirs ( topdir , verbose: bool = False) → None

Load all of the predefined site_scons dir. Order is significant; we load them in order from most generic (machine-wide) to most specific (topdir). The verbose argument is only for testing.

SCons.Script.Main._load_site_scons_dir ( topdir , site_dir_name= None)

Load the site directory under topdir.

If a site dir name is supplied use it, else use default “site_scons” Prepend site dir to sys.path. If a “site_tools” subdir exists, prepend to toolpath. Import “site_init.py” from site dir if it exists.

SCons.Script.Main._main ( parser )

SCons.Script.Main._scons_internal_error () → None

Handle all errors but user errors. Print out a message telling the user what to do in this case and print a normal trace.

SCons.Script.Main._scons_internal_warning ( e) → None

Slightly different from _scons_user_warning in that we use the current call stack rather than sys.exc_info() to get our stack trace. This is used by the warnings framework to print warnings.

SCons.Script.Main._scons_syntax_error ( e) → None

Handle syntax errors. Print out a message and show where the error occurred.

SCons.Script.Main._scons_user_error ( e) → None

Handle user errors. Print out a message and a description of the error, along with the line number and routine where it occured. The file and line number will be the deepest stack frame that is not part of SCons itself.

SCons.Script.Main._scons_user_warning ( e) → None

Handle user warnings. Print out a message and a description of the warning, along with the line number and routine where it occured. The file and line number will be the deepest stack frame that is not part of SCons itself.

SCons.Script.Main._set_debug_values ( options ) → None

SCons.Script.Main.find_deepest_user_frame ( tb )

Find the deepest stack frame that is not part of SCons.

Input is a “pre-processed” stack trace in the form returned by traceback.extract_tb() or traceback.extract_stack()

SCons.Script.Main.main () → None

SCons.Script.Main.path_string ( label , module ) → str

SCons.Script.Main.python_version_deprecated ( version= (3, 11, 14, 'final', 0))

SCons.Script.Main.python_version_string ()

SCons.Script.Main.python_version_unsupported ( version= (3, 11, 14, 'final', 0))

SCons.Script.Main.revert_io () → None

SCons.Script.Main.test_load_all_site_scons_dirs ( d) → None

SCons.Script.Main.version_string ( label , module )

# SCons.Script.SConsOptions module

SCons.Script.SConsOptions.Parser ( version )

Returns a parser object initialized with the standard SCons options.

Add options in the order we want them to show up in the -H help text, basically alphabetical. For readability, Each add_option() call should have a consistent format:

SCons.Script package

157 op.add_option( "-L", "--long-option-name", nargs=1, type="string", dest="long_option_name", default='foo', action="callback", callback=opt_long_option, help="help text goes here", metavar="VAR" )

Even though the optparse module constructs reasonable default destination names from the long option names, we’re going to be explicit about each one for easier readability and so this code will at least show up when grepping the source for option attribute names, or otherwise browsing the source code.

exception SCons.Script.SConsOptions.SConsBadOptionError ( opt_str: str , parser: SConsOptionParser | None = None)

Bases: BadOptionError

Raised if an invalid option value is encountered on the command line.

Variables: • opt_str – The unrecognized command-line option.

• parser – The active argument parser.

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

class SCons.Script.SConsOptions.SConsIndentedHelpFormatter ( indent_increment= 2,

max_help_position= 24, width= None, short_first= 1)

Bases: IndentedHelpFormatter

NO_DEFAULT_VALUE = 'none'

_format_text ( text )

Format a paragraph of free-form text for inclusion in the help output at the current indentation level.

dedent ()

expand_default ( option )

format_description ( description )

format_epilog ( epilog )

format_heading ( heading )

Translate heading to “SCons Options”

Heading of “Options” changed to “SCons Options.” Unfortunately, we have to do this here, because those titles are hard-coded in the optparse calls.

format_option ( option )

SCons-specific option formatter.

A copy of the optparse.IndentedHelpFormatter.format_option() method. Overridden so we can modify text wrapping to our liking:

• add our own regular expression that doesn’t break on hyphens (so things like --no-print-directory

don’t get broken).

• wrap the list of options themselves when it’s too long (the wrapper.fill(opts) call below).

• set the subsequent_indent when wrapping the help_text.

The help for each option consists of two parts:

• the opt strings and metavars e.g. ( -x , or -fFILENAME, --file=FILENAME )

• the user-supplied help string e.g. ( turn on expert mode , read data from FILENAME )

If possible, we write both of these on the same line:

SCons.Script package

158 -x turn on expert mode

If the opt string list is too long, we put the help string on a second line, indented to the same column it would start in if it fit on the first line:

-fFILENAME, --file=FILENAME read data from FILENAME

Help strings are wrapped for terminal width and do not preserve any hand-made formatting that may have been used in the AddOption call, so don’t attempt prettying up a list of choices (for example).

format_option_strings ( option )

Return a comma-separated list of option strings & metavariables.

format_usage ( usage ) → str

Format the usage message for SCons.

indent ()

set_long_opt_delimiter ( delim )

set_parser ( parser )

set_short_opt_delimiter ( delim )

store_local_option_strings ( parser , group )

Local-only version of store_option_strings.

We need to replicate this so the formatter will be set up properly if we didn’t go through the “normal” .

Added in version 4.6.0.

store_option_strings ( parser )

class SCons.Script.SConsOptions.SConsOption ( *opts , **attrs )

Bases: Option

SCons added option.

Changes CHECK_METHODS and CONST_ACTIONS settings from optparse.Option base class to tune for our usage.

New function _check_nargs_optional() implements the nargs=? syntax from argparse, and is added to the

CHECK_METHODS list. Overridden convert_value() supports this usage.

Changed in version 4.9.0: The settable attribute is added to ATTRS , allowing it to be set in the option. A parameter to mark the option settable was added in 4.8.0, but was not initially made part of the option object itself.

ACTIONS = ('store', 'store_const', 'store_true', 'store_false', 'append', 'append_const', 'count', 'callback', 'help', 'version')

ALWAYS_TYPED_ACTIONS = ('store', 'append')

ATTRS = ['action', 'type', 'dest', 'default', 'nargs', 'const', 'choices', 'callback', 'callback_args', 'callback_kwargs', 'help', 'metavar', 'settable']

CHECK_METHODS = [<function Option._check_action>, <function Option._check_type>, <function Option._check_choice>, <function Option._check_dest>, <function Option._check_const>, <function Option._check_nargs>, <function Option._check_callback>, <function SConsOption._check_nargs_optional>]

CONST_ACTIONS = ('store_const', 'append_const', 'store', 'append', 'callback')

STORE_ACTIONS = ('store', 'store_const', 'store_true', 'store_false', 'append', 'append_const', 'count')

TYPED_ACTIONS = ('store', 'append', 'callback')

TYPES = ('string', 'int', 'long', 'float', 'complex', 'choice')

TYPE_CHECKER = {'choice': <function check_choice>, 'complex': <function check_builtin>, 'float': <function check_builtin>, 'int': <function check_builtin>, 'long': <function check_builtin>}

_check_action ()

_check_callback ()

_check_choice ()

_check_const ()

_check_dest ()

_check_nargs ()

_check_nargs_optional () → None

SCons added: deal with optional option-arguments.

SCons.Script package

159 _check_opt_strings ( opts )

_check_type ()

_set_attrs ( attrs )

_set_opt_strings ( opts )

check_value ( opt , value )

convert_value ( opt: str , value )

SCons override: recognize nargs=”?”.

get_opt_string ()

process ( opt , value , values , parser )

Process a value.

Direct copy of optparse version including the comments - we don’t change anything so this could just be dropped.

take_action ( action , dest , opt , value , values , parser )

takes_value ()

class SCons.Script.SConsOptions.SConsOptionGroup ( parser , title , description= None)

Bases: OptionGroup

A subclass for SCons-specific option groups.

The only difference between this and the base class is that we print the group’s help text flush left, underneath their own title but lined up with the normal “SCons Options”.

_check_conflict ( option )

_create_option_list ()

_create_option_mappings ()

_share_option_mappings ( parser )

add_option ( Option )

add_option ( opt_str , ... , kwarg=val , ... ) → None

add_options ( option_list )

destroy ()

see OptionParser.destroy().

format_description ( formatter )

format_help ( formatter ) → str

SCons-specific formatting of an option group’s help text.

The title is dedented so it’s flush with the “SCons Options” title we print at the top.

format_option_help ( formatter )

get_description ()

get_option ( opt_str )

has_option ( opt_str )

remove_option ( opt_str )

set_conflict_handler ( handler )

set_description ( description )

set_title ( title )

class SCons.Script.SConsOptions.SConsOptionParser ( usage=None , option_list=None ,

option_class=<class 'optparse.Option'> , version=None , conflict_handler='error' ,

description=None , formatter=None , add_help_option=True , prog=None , epilog=None )

Bases: OptionParser

_add_help_option ()

_add_version_option ()

_check_conflict ( option )

_create_option_list ()

_create_option_mappings ()

_get_all_options ()

_get_args ( args )

_init_parsing_state ()

_match_long_opt ( opt: string ) → string

Determine which long option string ‘opt’ matches, ie. which one it is an unambiguous abbreviation for. Raises BadOptionError if ‘opt’ doesn’t unambiguously match any long option string.

_populate_option_list ( option_list , add_help= True)

_process_args ( largs , rargs , values )

SCons.Script package

160 _process_args(largs : [string],

rargs : [string], values : Values)

Process command-line arguments and populate ‘values’, consuming options and arguments from ‘rargs’. If ‘allow_interspersed_args’ is false, stop at the first non-option argument. If true, accumulate any interspersed non-option arguments in ‘largs’.

_process_long_opt ( rargs , values ) → None

SCons-specific processing of long options.

This is copied directly from the normal Optparse _process_long_opt() method, except that, if configured to do so, we catch the exception thrown when an unknown option is encountered and just stick it back on the “leftover” arguments for later (re-)processing. This is because we may see the option definition later, while processing SConscript files.

_process_short_opts ( rargs , values ) → None

SCons-specific processing of short options.

This is copied directly from the normal Optparse _process_short_opts() method, except that, if configured to do so, we catch the exception thrown when an unknown option is encountered and just stick it back on the “leftover” arguments for later (re-)processing. This is because we may see the option definition later, while processing SConscript files.

_share_option_mappings ( parser )

add_local_option ( *args , **kw ) → SConsOption

Add a local option to the parser.

This is the implementation of AddOption(), to add a project-defined command-line option. Local options are added to a separate option group, which is created if necessary.

The keyword argument settable is recognized specially (and removed from kw ). If true, the option is marked as modifiable; by default “local” (project-added) options are not eligible for SetOption() calls.

Changed in version NEXT_VERSION: If the option’s settable attribute is true, it is added to the SConsValues.settable list. settable handling was added in 4.8.0, but was not made an option attribute at the time.

add_option ( Option )

add_option ( opt_str , ... , kwarg=val , ... ) → None

add_option_group ( *args , **kwargs )

add_options ( option_list )

check_values ( values: Values , args: [string] )

-> (values : Values, args : [string])

Check that the supplied option values and leftover arguments are valid. Returns the option values and leftover arguments (possibly adjusted, possibly completely new – whatever you like). Default implementation just returns the passed-in values; subclasses may override as desired.

destroy ()

Declare that you are done with this OptionParser. This cleans up reference cycles so the OptionParser (and all objects referenced by it) can be garbage-collected promptly. After calling destroy(), the OptionParser is unusable.

disable_interspersed_args ()

Set parsing to stop on the first non-option. Use this if you have a command processor which runs another command that has options of its own and you want to make sure these options don’t get confused.

enable_interspersed_args ()

Set parsing to not stop on the first non-option, allowing interspersing switches with command arguments. This is the default behavior. See also disable_interspersed_args() and the class documentation description of the attribute allow_interspersed_args.

error ( msg: str ) → None

SCons-specific handling of option errors.

exit ( status= 0, msg= None)

expand_prog_name ( s)

format_description ( formatter )

format_epilog ( formatter )

format_help ( formatter= None)

format_local_option_help ( formatter= None, file= None)

Return the help for the project-level (“local”) SCons options.

Added in version 4.6.0.

format_option_help ( formatter= None)

SCons.Script package

161 get_default_values ()

get_description ()

get_option ( opt_str )

get_option_group ( opt_str )

get_prog_name ()

get_usage ()

get_version ()

has_option ( opt_str )

parse_args ( args= None, values= None)

parse_args(args : [string] = sys.argv[1:],

values : Values = None)

-> (values : Values, args : [string])

Parse the command-line options found in ‘args’ (default: sys.argv[1:]). Any errors result in a call to ‘error()’, which by default prints the usage message to stderr and calls sys.exit() with an error message. On success returns a pair (values, args) where ‘values’ is a Values instance (with all your option values) and ‘args’ is the list of arguments left over after parsing options.

preserve_unknown_options = False

print_help ( file: file = stdout)

Print an extended help message, listing all options and any help text provided with them, to ‘file’ (default stdout).

print_local_option_help ( file= None)

Print help for just local SCons options.

Writes to file (default stdout).

Added in version 4.6.0.

print_usage ( file: file = stdout)

Print the usage message for the current program (self.usage) to ‘file’ (default stdout). Any occurrence of the string “%prog” in self.usage is replaced with the name of the current program (basename of sys.argv[0]). Does nothing if self.usage is empty or not defined.

print_version ( file: file = stdout)

Print the version message for this program (self.version) to ‘file’ (default stdout). As with print_usage(), any occurrence of “%prog” in self.version is replaced by the current program’s name. Does nothing if self.version is empty or undefined.

raise_exception_on_error = False

remove_option ( opt_str )

reparse_local_options () → None

Re-parse the leftover command-line options.

Leftover options are stored in self.largs , so that any value overridden on the command line is immediately available if the user turns around and does a GetOption() right away.

We mimic the processing of the single args in the original OptionParser _process_args(), but here we allow exact matches for long-opts only (no partial argument names!). Otherwise there could be problems in add_local_option() below. When called from there, we try to reparse the command-line arguments that haven’t been processed so far (self.largs ), but are possibly not added to the options list yet.

So, when we only have a value for --myargument so far, a command-line argument of --myarg=test would set it, per the behaviour of _match_long_opt(), which allows for partial matches of the option name, as long as the common prefix appears to be unique. This would lead to further confusion, because we might want to add another option --myarg later on (see issue #2929).

set_conflict_handler ( handler )

set_default ( dest , value )

set_defaults ( **kwargs )

set_description ( description )

set_process_default_values ( process )

set_usage ( usage )

standard_option_list = []

class SCons.Script.SConsOptions.SConsValues ( defaults )

Bases: Values

Holder class for uniform access to SCons options.

SCons.Script package

162 A SCons option value can originate three different ways:

1. set on the command line.

2. set in an SConscript file via SetOption().

3. the default setting (from the the op.add_option() calls in the Parser() function.

The command line always overrides a value set in a SConscript file, which in turn always overrides default settings. Because we want to support user-specified options in the SConscript file itself, though, we may not know about all of the options when the command line is first parsed, so we can’t make all the necessary precedence decisions at the time the option is configured.

The solution implemented in this class is to keep these different sets of settings separate (command line, SConscript file, and default) and to override the __getattr__() method to check them in turn. This allows the rest of the code to just fetch values as attributes of an instance of this class, without having to worry about where they came from (the scheme is similar to a ChainMap ).

Note that not all command line options are settable from SConscript files, and the ones that are must be explicitly added to the settable list in this class, and optionally validated and coerced in the set_option() method.

__getattr__ ( attr )

Fetch an options value, respecting priority rules.

This is a little tricky: since we’re answering questions about outselves, we have avoid lookups that would send us into into infinite recursion, thus the __dict__ stuff.

_update ( dict , mode )

_update_careful ( dict )

Update the option values from an arbitrary dictionary, but only use keys from dict that already have acorresponding attribute in self. Any keys in dict without a corresponding attribute are silently ignored.

_update_loose ( dict )

Update the option values from an arbitrary dictionary, using all keys from the dictionary regardless of whether they have a corresponding attribute in self or not.

ensure_value ( attr , value )

read_file ( filename , mode= 'careful')

read_module ( modname , mode= 'careful')

set_option ( name: str , value ) → None

Set an option value from a SetOption() call.

Validation steps for settable options (those defined in SCons itself) are in-line here. Duplicates the logic for the matching command-line options in Parse() - these need to be kept in sync. Cannot provide validation for options added via AddOption() since we don’t know about those ahead of time - it is up to the developer to figure that out.

Raises: UserError – the option is not settable.

settable = ['clean', 'diskcheck', 'duplicate', 'experimental', 'hash_chunksize', 'hash_format', 'help', 'implicit_cache', 'implicit_deps_changed', 'implicit_deps_unchanged', 'max_drift', 'md5_chunksize', 'no_exec', 'no_progress', 'num_jobs', 'random', 'silent', 'stack_size', 'warn']

SCons.Script.SConsOptions.diskcheck_convert ( value )

# SCons.Script.SConscript module

This module defines the Python API provided to SConscript files.

SCons.Script.SConscript.BuildDefaultGlobals ()

Create a dictionary containing all the default globals for SConstruct and SConscript files.

SCons.Script.SConscript.Configure ( *args , **kw )

class SCons.Script.SConscript.DefaultEnvironmentCall ( method_name , subst: int = 0)

Bases: object

A class that implements “global function” calls of Environment methods by fetching the specified method from the DefaultEnvironment’s class. Note that this uses an intermediate proxy class instead of calling the DefaultEnvironment method directly so that the proxy can override the subst() method and thereby prevent expansion of construction variables (since from the user’s point of view this was called as a global function, with no associated construction environment).

class SCons.Script.SConscript.Frame ( fs , exports , sconscript )

Bases: object

SCons.Script package

163 A frame on the SConstruct/SConscript call stack

SCons.Script.SConscript.Return ( *vars , **kw )

class SCons.Script.SConscript.SConsEnvironment ( platform= None, tools= None, toolpath= None,

variables= None, parse_flags= None, **kw )

Bases: Base

An Environment subclass that contains all of the methods that are particular to the wrapper SCons interface and which aren’t (or shouldn’t be) part of the build engine itself.

Note that not all of the methods of this class have corresponding global functions, there are some private methods.

Action ( *args , **kw )

AddMethod ( function , name= None) → None

Adds the specified function as a method of this construction environment with the specified name. If the name is omitted, the default name is the name of the function itself.

AddPostAction ( files , action )

AddPreAction ( files , action )

Alias ( target , source= [], action= None, **kw )

AlwaysBuild ( *targets )

Append ( **kw ) → None

Append values to construction variables in an Environment.

The variable is created if it is not already present.

AppendENVPath ( name , newpath , envname: str = 'ENV', sep= ':', delete_existing: bool = False) →

None

Append path elements to the path name in the envname dictionary for this environment. Will only add any particular path once, and will normpath and normcase all paths to help assure this. This can also handle the case where the env variable is a list instead of a string.

If delete_existing is False, a newpath element already in the path will not be moved to the end (it will be left where it is).

AppendUnique ( delete_existing: bool = False, **kw ) → None

Append values uniquely to existing construction variables.

Similar to Append(), but the result may not contain duplicates of any values passed for each given key (construction variable), so an existing list may need to be pruned first, however it may still contain other duplicates.

If delete_existing is true, removes existing values first, so values move to the end; otherwise (the default) values are skipped if already present.

Builder ( **kw )

CacheDir ( path , custom_class= None) → None

Clean ( targets , files ) → None

Mark additional files for cleaning.

files will be removed if any of targets are selected for cleaning - that is, the combination of target selection and -c clean mode.

Parameters: • targets (files or nodes ) – targets to associate files with.

• files (files or nodes ) – items to remove if targets are selected.

Clone ( tools= [], toolpath= None, variables= None, parse_flags= None, **kw )

Return a copy of a construction Environment.

The copy is like a Python “deep copy”: independent copies are made recursively of each object, except that a reference is copied when an object is not deep-copyable (like a function). There are no references to any mutable objects in the original environment.

Unrecognized keyword arguments are taken as construction variable assignments.

Parameters: • tools – list of tools to initialize.

• toolpath – list of paths to search for tools.

• variables – a Variables object to use to populate construction variables from command-line variables.

• parse_flags – option strings to parse into construction variables.

Added in version 4.8.0: The optional variables parameter was added.

SCons.Script package

164 Command ( target , source , action , **kw )

Set up a one-off build command.

Builds target from source using action , which may be be any type that the Builder factory will accept for an action. Generates an anonymous builder and calls it, to add the details to the build graph. The builder is not named, added to BUILDERS , or otherwise saved.

Recognizes the Builder() keywords source_scanner , target_scanner , source_factory and

target_factory . All other arguments from kw are passed on to the builder when it is called.

Configure ( *args , **kw )

Decider ( function )

Default ( *targets ) → None

Depends ( target , dependency )

Explicity specify that target depends on dependency .

Detect ( progs )

Return the first available program from one or more possibilities.

Parameters: progs (str or list ) – one or more command names to check for

Dictionary ( *args: str , as_dict: bool = False)

Return construction variables from an environment.

Parameters: • args (optional ) – construction variable names to select. If omitted, all variables are selected and returned as a dict.

• as_dict – if true, and args is supplied, return the variables and their values in a dict. If false (the default), return a single value as a scalar, or multiple values in a list.

Returns: A dictionary of construction variables, or a single value or list of values.

Raises: KeyError – if any of args is not in the construction environment.

Changed in version 4.9.0: Added the as_dict keyword arg to specify always returning a dict.

Dir ( name , *args , **kw )

Dump ( *key: str , format: str = 'pretty') → str

Return string of serialized construction variables.

Produces a “pretty” output of a dictionary of selected construction variables, or all of them. The display format is selectable. The result is intended for human consumption (e.g, to print), mainly when debugging. Objects that cannot directly be represented get a placeholder like <function foo at 0x123456> (pretty-print) or

<<non-serializable: function>> (JSON).

Parameters: • key – variables to format together with their values. If omitted, format the whole dict of variables,

• format – specify the format to serialize to. "pretty" generates a pretty-printed string,

"json" a JSON-formatted string.

Raises: ValueError – format is not a recognized serialization format.

Changed in version 4.9.0: key is no longer limited to a single construction variable name. If key is supplied, a formatted dictionary is generated like the no-arg case - previously a single key displayed just the value.

static EnsurePythonVersion ( major , minor ) → None

Exit abnormally if the Python version is not late enough.

static EnsureSConsVersion ( major: int , minor: int , revision: int = 0) → None

Exit abnormally if the SCons version is not late enough.

Entry ( name , *args , **kw )

Environment ( **kw )

Execute ( action , *args , **kw )

Directly execute an action through an Environment

static Exit ( value: int = 0) → None

Export ( *vars , **kw ) → None

File ( name , *args , **kw )

FindFile ( file , dirs )

FindInstalledFiles ()

SCons.Script package

165 returns the list of all targets of the Install and InstallAs Builder.

FindIxes ( paths: Sequence[str] , prefix: str , suffix: str ) → str | None

Search paths for a path that has prefix and suffix .

Returns on first match.

Parameters: • paths – the list of paths or nodes.

• prefix – construction variable for the prefix.

• suffix – construction variable for the suffix.

Returns: The matched path or None

FindSourceFiles ( node: str = '.') → list

Return a list of all source files.

Flatten ( sequence )

GetBuildPath ( files )

static GetLaunchDir ()

GetOption ( name )

static GetSConsVersion () → tuple [int , int , int ]

Return the current SCons version.

Added in version 4.8.0.

Glob ( pattern , ondisk: bool = True, source: bool = False, strings: bool = False, exclude= None)

Help ( text , append: bool = False, local_only: bool = False) → None

Update the help text.

The previous help text has text appended to it, except on the first call. On first call, the values of append and

local_only are considered to determine what is appended to.

Parameters: • text – string to add to the help text.

• append – on first call, if true, keep the existing help text (default False).

• local_only – on first call, if true and append is also true, keep only the help text from AddOption calls.

Changed in version 4.6.0: The keep_local parameter was added.

Changed in version 4.9.0: The keep_local parameter was renamed local_only to match manpage

Ignore ( target , dependency )

Ignore a dependency.

Import ( *vars )

Literal ( string )

Local ( *targets )

MergeFlags ( args , unique: bool = True) → None

Merge flags into construction variables.

Merges the flags from args into this construction environent. If args is not a dict, it is first converted to one with flags distributed into appropriate construction variables. See ParseFlags().

As a side effect, if unique is true, a new object is created for each modified construction variable by the loop at the end. This is silently expected by the Override() parse_flags functionality, which does not want to share the list (or whatever) with the environment being overridden.

Parameters: • args – flags to merge

• unique – merge flags rather than appending (default: True). When merging, path variables are retained from the front, other construction variables from the end.

NoCache ( *targets )

Tag target(s) so that it will not be cached.

NoClean ( *targets ) → list

Tag targets to not be removed in clean mode.

Override ( overrides )

Create an override environment from the current environment.

SCons.Script package

166 Produces a modified environment where the current variables are overridden by any same-named variables from the overrides dict.

An override is much more efficient than doing Clone() or creating a new Environment because it doesn’t copy the construction environment dictionary, it just wraps the underlying construction environment, and doesn’t even create a wrapper object if there are no overrides.

Using this method is preferred over directly instantiating an OverrideEnvirionment because extra checks are performed, substitution takes place, and there is special handling for a parse_flags keyword argument.

This method is not currently exposed as part of the public API, but is invoked internally when things like builder calls have keyword arguments, which are then passed as overrides here. Some tools also call this explicitly.

Returns: A proxy environment of type OverrideEnvironment. or the current environment if overrides is empty.

ParseConfig ( command , function= None, unique: bool = True)

Parse the result of running a command to update construction vars.

Use function to parse the output of running command in order to modify the current environment.

Parameters: • command – a string or a list of strings representing a command and its arguments.

• function – called to process the result of command , which will be passed as args . If

function is omitted or None , MergeFlags() is used. Takes 3 args

(env, args, unique)

• unique – whether no duplicate values are allowed (default true)

ParseDepends ( filename , must_exist= None, only_one: bool = False)

Parse a mkdep-style file for explicit dependencies. This is completely abusable, and should be unnecessary in the “normal” case of proper SCons configuration, but it may help make the transition from a Make hierarchy easier for some people to swallow. It can also be genuinely useful when using a tool that can write a .d file, but for which writing a scanner would be too complicated.

ParseFlags ( *flags ) → dict

Return a dict of parsed flags.

Parse flags and return a dict with the flags distributed into the appropriate construction variable names. The flags are treated as a typical set of command-line flags for a GNU-style toolchain, such as might have been generated by one of the {foo}-config scripts, and used to populate the entries based on knowledge embedded in this method -the choices are not expected to be portable to other toolchains.

If one of the flags strings begins with a bang (exclamation mark), it is assumed to be a command and the rest of the string is executed; the result of that evaluation is then added to the dict.

Platform ( platform )

Precious ( *targets )

Mark targets as precious: do not delete before building.

Prepend ( **kw ) → None

Prepend values to construction variables in an Environment.

The variable is created if it is not already present.

PrependENVPath ( name , newpath , envname: str = 'ENV', sep= ':', delete_existing: bool = True) →

None

Prepend path elements to the path name in the envname dictionary for this environment. Will only add any particular path once, and will normpath and normcase all paths to help assure this. This can also handle the case where the env variable is a list instead of a string.

If delete_existing is False, a newpath component already in the path will not be moved to the front (it will be left where it is).

PrependUnique ( delete_existing: bool = False, **kw ) → None

Prepend values uniquely to existing construction variables.

Similar to Prepend(), but the result may not contain duplicates of any values passed for each given key (construction variable), so an existing list may need to be pruned first, however it may still contain other duplicates.

If delete_existing is true, removes existing values first, so values move to the front; otherwise (the default) values are skipped if already present.

Pseudo ( *targets )

Mark targets as pseudo: must not exist.

SCons.Script package

167 PyPackageDir ( modulename )

RemoveMethod ( function ) → None

Removes the specified function’s MethodWrapper from the added_methods list, so we don’t re-bind it when making a clone.

Replace ( **kw ) → None

Replace existing construction variables in an Environment with new construction variables and/or values.

ReplaceIxes ( path , old_prefix , old_suffix , new_prefix , new_suffix )

Replace old_prefix with new_prefix and old_suffix with new_suffix.

env - Environment used to interpolate variables. path - the path that will be modified. old_prefix - construction variable for the old prefix. old_suffix - construction variable for the old suffix. new_prefix - construction variable for the new prefix. new_suffix - construction variable for the new suffix.

Repository ( *dirs , **kw ) → None

Specify Repository directories to search.

Requires ( target , prerequisite )

Specify that prerequisite must be built before target .

Creates an order-only relationship, not a full dependency. prerequisite must exist before target can be built, but a change to prerequisite does not trigger a rebuild of target .

SConscript ( *ls , **kw )

Execute SCons configuration files.

Parameters: *ls (str or list ) – configuration file(s) to execute.

Keyword Arguments: • dirs (list ) – execute SConscript in each listed directory.

• name (str ) – execute script ‘name’ (used only with ‘dirs’).

• exports (list or dict ) – locally export variables the called script(s) can import.

• variant_dir (str ) – mirror sources needed for the build in a variant directory to allow building in it.

• duplicate (bool ) – physically duplicate sources instead of just adjusting paths of derived files (used only with ‘variant_dir’) (default is True).

• must_exist (bool ) – fail if a requested script is missing (default is False, default is deprecated).

Returns: list of variables returned by the called script

Raises: UserError – a script is not found and such exceptions are enabled.

static SConscriptChdir ( flag: bool ) → None

SConsignFile ( name= '.sconsign', dbm_module= None) → None

Scanner ( *args , **kw )

SetDefault ( **kw ) → None

SetOption ( name , value ) → None

SideEffect ( side_effect , target )

Tell scons that side_effects are built as side effects of building targets.

Split ( arg )

This function converts a string or list into a list of strings or Nodes. This makes things easier for users by allowing files to be specified as a white-space separated list to be split.

The input rules are:

• A single string containing names separated by spaces. These will be split apart at the spaces.

• A single Node instance

• A list containing either strings or Node instances. Any strings in the list are not split at spaces.

In all cases, the function returns a list of Nodes and strings.

Tool ( tool: str | Callable , toolpath: Collection[str] | None = None, **kwargs ) → Callable

Find and run tool module tool .

SCons.Script package

168 tool is generally a string, but can also be a callable object, in which case it is just called, without any of the setup. The skipped setup includes storing kwargs into the created Tool instance, which is extracted and used when the instance is called, so in the skip case, the called object will not get the kwargs .

Changed in version 4.2: returns the tool object rather than None .

Value ( value , built_value= None, name= None)

Return a Value (Python expression) node.

Changed in version 4.0: the name parameter was added.

VariantDir ( variant_dir , src_dir , duplicate: int = 1) → None

WhereIs ( prog , path= None, pathext= None, reject= None)

Find prog in the path.

__eq__ ( other )

Compare two environments.

This is used by checks in Builder to determine if duplicate targets have environments that would cause the same result. The more reliable way (respecting the admonition to avoid poking at _dict directly) would be to use

Dictionary so this is sure to work even if one or both are are instances of OverrideEnvironment. However an actual SubstitutionEnvironment doesn’t have a Dictionary method That causes problems for unit tests written to excercise SubsitutionEnvironment directly, although nobody else seems to ever instantiate one. We count on OverrideEnvironment to fake the _dict to make things work.

__getattr__ ( name )

Handle missing attribute in an environment.

Assume this is a builder that’s not instantiated, becasue that has been a common failure mode. Could also be a typo. Emit a message about this to try to help. We can’t get too clever, other parts of SCons depend on seeing the AttributeError that triggers this call, so all we do is produce our own message.

Added in version 4.10.0.

_canonicalize ( path )

Allow Dirs and strings beginning with # for top-relative.

Note this uses the current env’s fs (in self).

_changed_build ( dependency , target , prev_ni , repo_node= None) → bool

_changed_content ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_match ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_newer ( dependency , target , prev_ni , repo_node= None) → bool

_changed_timestamp_then_content ( dependency , target , prev_ni , repo_node= None) → bool

_find_toolpath_dir ( tp )

_get_SConscript_filenames ( ls , kw )

Convert the parameters passed to SConscript() calls into a list of files and export variables. If the parameters are invalid, throws SCons.Errors.UserError. Returns a tuple (l, e) where l is a list of SConscript filenames and e is a list of exports.

static _get_major_minor_revision ( version_string: str ) → tuple [int , int , int ]

Split a version string into major, minor and (optionally) revision parts.

This is complicated by the fact that a version string can be something like 3.2b1.

_gsm ()

_init_special () → None

Initial the dispatch tables for special handling of special construction variables.

_update ( other ) → None

Private method to update an environment’s consvar dict directly.

Bypasses the normal checks that occur when users try to set items.

_update_onlynew ( other ) → None

Private method to add new items to an environment’s consvar dict.

Only adds items from other whose keys do not already appear in the existing dict; values from other are not used for replacement. Bypasses the normal checks that occur when users try to set items.

arg2nodes ( args , node_factory=<class 'SCons.Environment._Null'> , lookup_list=<class 'SCons.Environment._Null'> , **kw )

Converts args to a list of nodes.

SCons.Script package

169 Parameters: • just (args - filename strings or nodes to convert; nodes are ) – added to the list without further processing.

• not (node_factory - optional factory to create the nodes; if ) – specified, will use this environment’s fs.File method.

• to (lookup_list - optional list of lookup functions to call ) – attempt to find the file referenced by each args .

• add. (kw - keyword arguments that represent additional nodes to )

backtick ( command ) → str

Emulate command substitution.

Provides behavior conceptually like POSIX Shell notation for running a command in backquotes (backticks) by running command and returning the resulting output string.

This is not really a public API any longer, it is provided for the use of ParseFlags() (which supports it using a syntax of !command) and ParseConfig().

Raises: OSError – if the external command returned non-zero exit status.

get ( key , default= None)

Emulates the get() method of dictionaries.

get_CacheDir ()

get_builder ( name )

Fetch the builder with the specified name from the environment.

get_factory ( factory , default: str = 'File')

Return a factory function for creating Nodes for this construction environment.

get_scanner ( skey )

Find the appropriate scanner given a key (usually a file suffix).

gvars ()

items ()

Emulates the items() method of dictionaries.

keys ()

Emulates the keys() method of dictionaries.

lvars ()

scanner_map_delete ( kw= None) → None

Delete the cached scanner map (if we need to).

setdefault ( key , default= None)

Emulates the setdefault() method of dictionaries.

subst ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None =

None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

subst_kw ( kw , raw: int = 0, target= None, source= None)

subst_list ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Calls through to SCons.Subst.scons_subst_list().

See the documentation for that function.

subst_path ( path , target= None, source= None)

Substitute a path list.

Turns EntryProxies into Nodes, leaving Nodes (and other objects) as-is.

subst_target_source ( string , raw: int = 0, target= None, source= None, conv= None, executor: Executor | None = None, overrides: dict | None = None)

Recursively interpolates construction variables from the Environment into the specified string, returning the expanded result. Construction variables are specified by a $ prefix in the string and begin with an initial underscore or alphabetic character followed by any number of underscores or alphanumeric characters. The construction variable names may be surrounded by curly braces to separate the name from trailing characters.

SCons.Script package

170 validate_CacheDir_class ( custom_class= None)

Validate the passed custom CacheDir class, or if no args are passed, validate the custom CacheDir class from the environment.

values ()

Emulates the values() method of dictionaries.

exception SCons.Script.SConscript.SConscriptReturn

Bases: Exception

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

SCons.Script.SConscript.SConscript_exception ( file=<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'> ) → None

Print an exception stack trace just for the SConscript file(s). This will show users who have Python errors where the problem is, without cluttering the output with all of the internal calls leading up to where we exec the SConscript.

SCons.Script.SConscript._SConscript ( fs , *files , **kw )

SCons.Script.SConscript.annotate ( node )

Annotate a node with the stack frame describing the SConscript file and line number that created it.

SCons.Script.SConscript.compute_exports ( exports )

Compute a dictionary of exports given one of the parameters to the Export() function or the exports argument to SConscript().

SCons.Script.SConscript.get_DefaultEnvironmentProxy ()

SCons.Script.SConscript.get_calling_namespaces ()

Return the locals and globals for the function that called into this module in the current call stack.

SCons.Script.SConscript.handle_missing_SConscript ( f: str , must_exist: bool = True) → None

Take appropriate action on missing file in SConscript() call.

Print a warning or raise an exception on missing file, unless missing is explicitly allowed by the must_exist parameter or by a global flag.

Parameters: • f – path to missing configuration file

• must_exist – if true (the default), fail. If false do nothing, allowing a build to declare it’s okay to be missing.

Raises: UserError – if must_exist is true or if global SCons.Script._no_missing_sconscript is true.

# SCons.Taskmaster package

# Module contents

Generic Taskmaster module for the SCons build engine.

This module contains the primary interface(s) between a wrapping user interface and the SCons build engine. There are two key classes here:

Taskmaster

This is the main engine for walking the dependency graph and calling things to decide what does or doesn’t need to be built.

Task

This is the base class for allowing a wrapping interface to decide what does or doesn’t actually need to be done. The intention is for a wrapping interface to subclass this as appropriate for different types of behavior it may need. The canonical example is the SCons native Python interface, which has Task subclasses that handle its specific behavior, like printing “‘foo’ is up to date” when a top-level target doesn’t need to be built, and handling the -c option by removing targets as its “build” action. There is also a separate subclass for suppressing this output when the -q option is used.

SCons.Taskmaster package

171 The Taskmaster instantiates a Task object for each (set of) target(s) that it decides need to be evaluated and/or built.

class SCons.Taskmaster.AlwaysTask ( tm , targets , top , node )

Bases: Task

LOGGER = None

_abc_impl = <_abc._abc_data object>

_exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

_no_exception_to_raise () → None

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute ()

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

executed () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed () → None

Default action when a task fails: stop the build.

SCons.Taskmaster package

172 Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

get_target ()

Fetch the target being built or updated by this task.

make_ready ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

needs_execute () → bool

Always returns True (indicating this Task should always be executed).

Subclasses that need this behavior (as opposed to the default of only executing Nodes that are out of date w.r.t. their dependencies) can use this as follows:

class MyTaskSubclass(SCons.Taskmaster.Task):

needs_execute = SCons.Taskmaster.AlwaysTask.needs_execute

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare () → None

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

trace_message ( node , description: str = 'node') → None

class SCons.Taskmaster.OutOfDateTask ( tm , targets , top , node )

Bases: Task

LOGGER = None

_abc_impl = <_abc._abc_data object>

_exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

_no_exception_to_raise () → None

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute ()

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

SCons.Taskmaster package

173 executed () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed () → None

Default action when a task fails: stop the build.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

get_target ()

Fetch the target being built or updated by this task.

make_ready ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

needs_execute ()

Returns True (indicating this Task should be executed) if this Task’s target state indicates it needs executing, which has already been determined by an earlier up-to-date check.

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare () → None

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

trace_message ( node , description: str = 'node') → None

SCons.Taskmaster package

174 class SCons.Taskmaster.Stats

Bases: object

A simple class for holding statistics about the disposition of a Node by the Taskmaster. If we’re collecting statistics, each Node processed by the Taskmaster gets one of these attached, in which case the Taskmaster records its decision each time it processes the Node. (Ideally, that’s just once per Node.)

class SCons.Taskmaster.Task ( tm , targets , top , node )

Bases: ABC

SCons build engine abstract task class.

This controls the interaction of the actual building of node and the rest of the engine.

This is expected to handle all of the normally-customizable aspects of controlling a build, so any given application

should be able to do what it wants by sub-classing this class and overriding methods as appropriate. If an application needs to customize something by sub-classing Taskmaster (or some other build engine class), we should first try to migrate that functionality into this class.

Note that it’s generally a good idea for sub-classes to call these methods explicitly to update state, etc., rather than roll their own interaction with Taskmaster from scratch.

LOGGER = None

_abc_impl = <_abc._abc_data object>

_exception_raise ()

Raises a pending exception that was recorded while getting a Task ready for execution.

_no_exception_to_raise () → None

display ( message ) → None

Hook to allow the calling interface to display a message.

This hook gets called as part of preparing a task for execution (that is, a Node to be built). As part of figuring out what Node should be built next, the actual target list may be altered, along with a message describing the alteration. The calling interface can subclass Task and provide a concrete implementation of this method to see those messages.

exc_clear () → None

Clears any recorded exception.

This also changes the “exception_raise” attribute to point to the appropriate do-nothing method.

exc_info ()

Returns info about a recorded exception.

exception_set ( exception= None) → None

Records an exception to be raised at the appropriate time.

This also changes the “exception_raise” attribute to point to the method that will, in fact

execute ()

Called to execute the task.

This method is called from multiple threads in a parallel build, so only do thread safe stuff here. Do thread unsafe stuff in prepare(), executed() or failed().

executed () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_with_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance wants to call the Node’s callback methods.

This may have been a do-nothing operation (to preserve build order), so we must check the node’s state before deciding whether it was “built”, in which case we call the appropriate Node method. In any event, we always call “visited()”, which will handle any post-visit actions that must take place regardless of whether or not the target was an actual built target or a source Node.

executed_without_callbacks () → None

Called when the task has been successfully executed and the Taskmaster instance doesn’t want to call the Node’s callback methods.

fail_continue () → None

SCons.Taskmaster package

175 Explicit continue-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

fail_stop () → None

Explicit stop-the-build failure.

This sets failure status on the target nodes and all of their dependent parent nodes.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

failed () → None

Default action when a task fails: stop the build.

Note: Although this function is normally invoked on nodes in the executing state, it might also be invoked on up-to-date nodes when using Configure().

get_target ()

Fetch the target being built or updated by this task.

make_ready ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

make_ready_all () → None

Marks all targets in a task ready for execution.

This is used when the interface needs every target Node to be visited–the canonical example being the “scons -c” option.

make_ready_current ()

Marks all targets in a task ready for execution if any target is not current.

This is the default behavior for building only what’s necessary.

abstractmethod needs_execute ()

postprocess () → None

Post-processes a task after it’s been executed.

This examines all the targets just built (or not, we don’t care if the build was successful, or even if there was no build because everything was up-to-date) to see if they have any waiting parent Nodes, or Nodes waiting on a common side effect, that can be put back on the candidates list.

prepare () → None

Called just before the task is executed.

This is mainly intended to give the target Nodes a chance to unlink underlying files and make all necessary directories before the Action is actually called to build the targets.

trace_message ( node , description: str = 'node') → None

class SCons.Taskmaster.Taskmaster ( targets= [], tasker= None, order= None, trace= None)

Bases: object

The Taskmaster for walking the dependency DAG.

_find_next_ready_node ()

Finds the next node that is ready to be built.

This is the main guts of the DAG walk. We loop through the list of candidates, looking for something that has no un-built children (i.e., that is a leaf Node or has dependencies that are all leaf Nodes or up-to-date). Candidate Nodes are re-scanned (both the target Node itself and its sources, which are always scanned in the context of a given target) to discover implicit dependencies. A Node that must wait for some children to be built will be put back on the candidates list after the children have finished building. A Node that has been put back on the candidates list in this way may have itself (or its sources) re-scanned, in order to handle generated header files (e.g.) and the implicit dependencies therein.

Note that this method does not do any signature calculation or up-to-date check itself. All of that is handled by the Task class. This is purely concerned with the dependency graph walk.

_validate_pending_children () → None

Validate the content of the pending_children set. Assert if an internal error is found.

This function is used strictly for debugging the taskmaster by checking that no invariants are violated. It is not used in normal operation.

The pending_children set is used to detect cycles in the dependency graph. We call a “pending child” a child that is found in the “pending” state when checking the dependencies of its parent node.

SCons.Taskmaster package

176 A pending child can occur when the Taskmaster completes a loop through a cycle. For example, let’s imagine a graph made of three nodes (A, B and C) making a cycle. The evaluation starts at node A. The Taskmaster first considers whether node A’s child B is up-to-date. Then, recursively, node B needs to check whether node C is up-to-date. This leaves us with a dependency graph looking like:

Next candidate ^ || |+-------------------------------------+

Now, when the Taskmaster examines the Node C’s child Node A, it finds that Node A is in the “pending” state. Therefore, Node A is a pending child of node C.

Pending children indicate that the Taskmaster has potentially loop back through a cycle. We say potentially because it could also occur when a DAG is evaluated in parallel. For example, consider the following graph:

Node A (Pending) --> Node B(Pending) --> Node C (Pending) --> ... | ^| |+----------> Node D (NoState) --------+ /Next candidate /

The Taskmaster first evaluates the nodes A, B, and C and starts building some children of node C. Assuming, that the maximum parallel level has not been reached, the Taskmaster will examine Node D. It will find that Node C is a pending child of Node D.

In summary, evaluating a graph with a cycle will always involve a pending child at one point. A pending child might indicate either a cycle or a diamond-shaped DAG. Only a fraction of the nodes ends-up being a “pending child” of another node. This keeps the pending_children set small in practice.

We can differentiate between the two cases if we wait until the end of the build. At this point, all the pending children nodes due to a diamond-shaped DAG will have been properly built (or will have failed to build). But, the pending children involved in a cycle will still be in the pending state.

The taskmaster removes nodes from the pending_children set as soon as a pending_children node moves out of the pending state. This also helps to keep the pending_children set small.

cleanup ()

Check for dependency cycles.

configure_trace ( trace= None) → None

This handles the command line option –taskmastertrace= It can be: - : output to stdout <filename> : output to a file False/None : Do not trace

find_next_candidate ()

Returns the next candidate Node for (potential) evaluation.

The candidate list (really a stack) initially consists of all of the top-level (command line) targets provided when the Taskmaster was initialized. While we walk the DAG, visiting Nodes, all the children that haven’t finished processing get pushed on to the candidate list. Each child can then be popped and examined in turn for whether their children are all up-to-date, in which case a Task will be created for their actual evaluation and potential building.

Here is where we also allow candidate Nodes to alter the list of Nodes that should be examined. This is used, for example, when invoking SCons in a source directory. A source directory Node can return its corresponding build directory Node, essentially saying, “Hey, you really need to build this thing over here instead.”

next_task ()

Returns the next task to be executed.

This simply asks for the next Node to be evaluated, and then wraps it in the specific Task subclass with which we were initialized.

no_next_candidate ()

Stops Taskmaster processing by not returning a next candidate.

Note that we have to clean-up the Taskmaster candidate list because the cycle detection depends on the fact all nodes have been processed somehow.

SCons.Taskmaster package

177 stop () → None

Stops the current build completely.

tm_trace_node ( node ) → str

will_not_build ( nodes , node_func=<function Taskmaster.<lambda>> ) → None

Perform clean-up about nodes that will never be built. Invokes a user defined function on all of these nodes (including all of their parents).

SCons.Taskmaster.dump_stats () → None

SCons.Taskmaster.find_cycle ( stack , visited )

# Submodules

# SCons.Taskmaster.Job module

Serial and Parallel classes to execute build tasks.

The Jobs class provides a higher level interface to start, stop, and wait on jobs.

class SCons.Taskmaster.Job.InterruptState

Bases: object

set () → None

class SCons.Taskmaster.Job.Jobs ( num , taskmaster )

Bases: object

An instance of this class initializes N jobs, and provides methods for starting, stopping, and waiting on all N jobs.

_reset_sig_handler () → None

Restore the signal handlers to their previous state (before the call to _setup_sig_handler().

_setup_sig_handler () → None

Setup an interrupt handler so that SCons can shutdown cleanly in various conditions:

a. SIGINT: Keyboard interrupt

b. SIGTERM: kill or system shutdown

c. SIGHUP: Controlling shell exiting

We handle all of these cases by stopping the taskmaster. It turns out that it’s very difficult to stop the build process by throwing asynchronously an exception such as KeyboardInterrupt. For example, the python Condition variables (threading.Condition) and queues do not seem to be asynchronous-exception-safe. It would require adding a whole bunch of try/finally block and except KeyboardInterrupt all over the place.

Note also that we have to be careful to handle the case when SCons forks before executing another process. In that case, we want the child to exit immediately.

run ( postfunc=<function Jobs.<lambda>> ) → None

Run the jobs.

postfunc() will be invoked after the jobs has run. It will be invoked even if the jobs are interrupted by a keyboard interrupt (well, in fact by a signal such as either SIGINT, SIGTERM or SIGHUP). The execution of postfunc() is protected against keyboard interrupts and is guaranteed to run to completion.

were_interrupted ()

Returns whether the jobs were interrupted by a signal.

class SCons.Taskmaster.Job.LegacyParallel ( taskmaster , num , stack_size )

Bases: object

This class is used to execute tasks in parallel, and is somewhat less efficient than Serial, but is appropriate for parallel builds.

This class is thread safe.

start ()

Start the job. This will begin pulling tasks from the taskmaster and executing them, and return when there are no more tasks. If a task fails to execute (i.e. execute() raises an exception), then the job will stop.

class SCons.Taskmaster.Job.NewParallel ( taskmaster , num , stack_size )

Bases: object

class FakeCondition ( lock )

Bases: object

notify ()

SCons.Taskmaster package

178 notify_all ()

wait ()

class FakeLock

Bases: object

lock ()

unlock ()

class State ( value )

Bases: Enum

COMPLETED = 3

READY = 0

SEARCHING = 1

STALLED = 2

classmethod __contains__ ( member )

Return True if member is a member of this enum raises TypeError if member is not an enum member

note: in 3.12 TypeError will no longer be raised, and True will also be returned if member is the value of a member in this enum

classmethod __getitem__ ( name )

Return the member matching name .

classmethod __iter__ ()

Return members in definition order.

classmethod __len__ ()

Return the number of members (no aliases)

class Worker ( owner )

Bases: Thread

_bootstrap ()

_bootstrap_inner ()

_delete ()

Remove current thread from the dict of currently running threads.

_initialized = False

_reset_internal_locks ( is_alive )

_set_ident ()

_set_native_id ()

_set_tstate_lock ()

Set a lock object which will be released by the interpreter when the underlying thread state (see pystate.h) gets deleted.

_stop ()

_wait_for_tstate_lock ( block= True, timeout= -1)

property daemon

A boolean value indicating whether this thread is a daemon thread.

This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.

The entire Python program exits when only daemon threads are left.

getName ()

Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.

property ident

Thread identifier of this thread or None if it has not been started.

This is a nonzero integer. See the get_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited.

isDaemon ()

Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.

is_alive ()

Return whether the thread is alive.

SCons.Taskmaster package

179 This method returns True just before the run() method starts until just after the run() method terminates. See also the module function enumerate().

join ( timeout= None)

Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is called terminates – either normally or through an unhandled exception or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof). As join() always returns None, you must call is_alive() after join() to decide whether a timeout happened – if the thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock. It is also an error to join() a thread before it has been started and attempts to do so raises the same exception.

property name

A string used for identification purposes only.

It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.

property native_id

Native integral thread ID of this thread, or None if it has not been started.

This is a non-negative integer. See the get_native_id() function. This represents the Thread ID as reported by the kernel.

run () → None

Method representing the thread’s activity.

You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

setDaemon ( daemonic )

Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.

setName ( name )

Set the name string for this thread.

This method is deprecated, use the name attribute instead.

start ()

Start the thread’s activity.

It must be called at most once per thread object. It arranges for the object’s run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the same thread object.

_adjust_stack_size ()

_maybe_start_worker () → None

_restore_stack_size ( prev_size ) → None

_setup_logging ()

_start_worker () → None

_work ()

start () → None

trace_message ( message ) → None

class SCons.Taskmaster.Job.Serial ( taskmaster )

Bases: object

This class is used to execute tasks in series, and is more efficient than Parallel, but is only appropriate for non-parallel builds. Only one instance of this class should be in existence at a time.

This class is not thread safe.

start ()

Start the job. This will begin pulling tasks from the taskmaster and executing them, and return when there are no more tasks. If a task fails to execute (i.e. execute() raises an exception), then the job will stop.

class SCons.Taskmaster.Job.ThreadPool ( num , stack_size , interrupted )

Bases: object

This class is responsible for spawning and managing worker threads.

cleanup () → None

SCons.Taskmaster package

180 Shuts down the thread pool, giving each worker thread a chance to shut down gracefully.

get ()

Remove and return a result tuple from the results queue.

preparation_failed ( task ) → None

put ( task ) → None

Put task into request queue.

class SCons.Taskmaster.Job.Worker ( requestQueue , resultsQueue , interrupted )

Bases: Thread

A worker thread waits on a task to be posted to its request queue, dequeues the task, executes it, and posts a tuple including the task and a boolean indicating whether the task executed successfully.

_bootstrap ()

_bootstrap_inner ()

_delete ()

Remove current thread from the dict of currently running threads.

_initialized = False

_reset_internal_locks ( is_alive )

_set_ident ()

_set_native_id ()

_set_tstate_lock ()

Set a lock object which will be released by the interpreter when the underlying thread state (see pystate.h) gets deleted.

_stop ()

_wait_for_tstate_lock ( block= True, timeout= -1)

property daemon

A boolean value indicating whether this thread is a daemon thread.

This must be set before start() is called, otherwise RuntimeError is raised. Its initial value is inherited from the creating thread; the main thread is not a daemon thread and therefore all threads created in the main thread default to daemon = False.

The entire Python program exits when only daemon threads are left.

getName ()

Return a string used for identification purposes only.

This method is deprecated, use the name attribute instead.

property ident

Thread identifier of this thread or None if it has not been started.

This is a nonzero integer. See the get_ident() function. Thread identifiers may be recycled when a thread exits and another thread is created. The identifier is available even after the thread has exited.

isDaemon ()

Return whether this thread is a daemon.

This method is deprecated, use the daemon attribute instead.

is_alive ()

Return whether the thread is alive.

This method returns True just before the run() method starts until just after the run() method terminates. See also the module function enumerate().

join ( timeout= None)

Wait until the thread terminates.

This blocks the calling thread until the thread whose join() method is called terminates – either normally or through an unhandled exception or until the optional timeout occurs.

When the timeout argument is present and not None, it should be a floating point number specifying a timeout for the operation in seconds (or fractions thereof). As join() always returns None, you must call is_alive() after join() to decide whether a timeout happened – if the thread is still alive, the join() call timed out.

When the timeout argument is not present or None, the operation will block until the thread terminates.

A thread can be join()ed many times.

join() raises a RuntimeError if an attempt is made to join the current thread as that would cause a deadlock. It is also an error to join() a thread before it has been started and attempts to do so raises the same exception.

property name

A string used for identification purposes only.

SCons.Taskmaster package

181 It has no semantics. Multiple threads may be given the same name. The initial name is set by the constructor.

property native_id

Native integral thread ID of this thread, or None if it has not been started.

This is a non-negative integer. See the get_native_id() function. This represents the Thread ID as reported by the kernel.

run ()

Method representing the thread’s activity.

You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with sequential and keyword arguments taken from the args and kwargs arguments, respectively.

setDaemon ( daemonic )

Set whether this thread is a daemon.

This method is deprecated, use the .daemon property instead.

setName ( name )

Set the name string for this thread.

This method is deprecated, use the name attribute instead.

start ()

Start the thread’s activity.

It must be called at most once per thread object. It arranges for the object’s run() method to be invoked in a separate thread of control.

This method will raise a RuntimeError if called more than once on the same thread object.

# SCons.Tool package

# Module contents

SCons tool selection.

Looks for modules that define a callable object that can modify a construction environment as appropriate for a given tool (or tool chain).

Note that because this subsystem just selects a callable that can modify a construction environment, it’s possible for people to define their own “tool specification” in an arbitrary callable function. No one needs to use or tie in to this subsystem in order to roll their own tool specifications.

SCons.Tool.CreateJarBuilder ( env )

The Jar builder expects a list of class files which it can package into a jar file.

The jar tool provides an interface for passing other types of java files such as .java, directories or swig interfaces and will build them to class files in which it can package into the jar.

SCons.Tool.CreateJavaClassDirBuilder ( env )

SCons.Tool.CreateJavaClassFileBuilder ( env )

SCons.Tool.CreateJavaFileBuilder ( env )

SCons.Tool.CreateJavaHBuilder ( env )

SCons.Tool.FindAllTools ( tools , env )

SCons.Tool.FindTool ( tools , env )

SCons.Tool.Initializers ( env ) → None

class SCons.Tool.Tool ( name , toolpath= None, **kwargs )

Bases: object

_tool_module ()

Try to load a tool module.

This will hunt in the toolpath for both a Python file (toolname.py) and a Python module (toolname directory), then try the regular import machinery, then fallback to try a zipfile.

class SCons.Tool.ToolInitializer ( env , tools , names )

Bases: object

A class for delayed initialization of Tools modules.

Instances of this class associate a list of Tool modules with a list of Builder method names that will be added by those Tool modules. As part of instantiating this object for a particular construction environment, we also add the

SCons.Tool package

182 appropriate ToolInitializerMethod objects for the various Builder methods that we want to use to delay Tool searches until necessary.

apply_tools ( env ) → None

Searches the list of associated Tool modules for one that exists, and applies that to the construction environment.

remove_methods ( env ) → None

Removes the methods that were added by the tool initialization so we no longer copy and re-bind them when the construction environment gets cloned.

class SCons.Tool.ToolInitializerMethod ( name , initializer )

Bases: object

This is added to a construction environment in place of a method(s) normally called for a Builder (env.Object, env.StaticObject, etc.). When called, it has its associated ToolInitializer object search the specified list of tools and apply the first one that exists to the construction environment. It then calls whatever builder was (presumably) added to the construction environment in place of this particular instance.

__call__ ( env , *args , **kw )

get_builder ( env )

Returns the appropriate real Builder for this method name after having the associated ToolInitializer object apply the appropriate Tool module.

SCons.Tool.createCFileBuilders ( env )

This is a utility function that creates the CFile/CXXFile Builders in an Environment if they are not there already.

If they are there already, we return the existing ones.

This is a separate function because soooo many Tools use this functionality.

The return is a 2-tuple of (CFile, CXXFile)

SCons.Tool.createLoadableModuleBuilder ( env , loadable_module_suffix: str = '$_LDMODULESUFFIX')

This is a utility function that creates the LoadableModule Builder in an Environment if it is not there already.

If it is already there, we return the existing one.

Parameters: loadable_module_suffix – The suffix specified for the loadable module builder

SCons.Tool.createObjBuilders ( env )

This is a utility function that creates the StaticObject and SharedObject Builders in an Environment if they are not there already.

If they are there already, we return the existing ones.

This is a separate function because soooo many Tools use this functionality.

The return is a 2-tuple of (StaticObject, SharedObject)

SCons.Tool.createProgBuilder ( env )

This is a utility function that creates the Program Builder in an Environment if it is not there already.

If it is already there, we return the existing one.

SCons.Tool.createSharedLibBuilder ( env , shlib_suffix: str = '$_SHLIBSUFFIX')

This is a utility function that creates the SharedLibrary Builder in an Environment if it is not there already.

If it is already there, we return the existing one.

Parameters: shlib_suffix – The suffix specified for the shared library builder

SCons.Tool.createStaticLibBuilder ( env )

This is a utility function that creates the StaticLibrary Builder in an Environment if it is not there already.

If it is already there, we return the existing one.

SCons.Tool.find_program_path ( env , key_program , default_paths= None, add_path: bool = False) → str |

None

Find the location of a tool using various means.

Mainly for windows where tools aren’t all installed in /usr/bin, etc.

Parameters: • env – Current Construction Environment.

• key_program – Tool to locate.

• default_paths – List of additional paths this tool might be found in.

• add_path – If true, add path found if it was from default_paths .

SCons.Tool.tool_list ( platform , env )

SCons.Tool package

183 SCons.Util package

# Module contents

SCons utility functions

This package contains routines for use by other parts of SCons. Candidates for inclusion here are routines that do not need other parts of SCons (other than Util), and have a reasonable chance of being useful in multiple places, rather then being topical only to one module/package.

class SCons.Util.CLVar ( initlist= None)

Bases: UserList

A container for command-line construction variables.

Forces the use of a list of strings intended as command-line arguments. Like collections.UserList, but the argument passed to the initializter will be processed by the Split() function, which includes special handling for string types: they will be split into a list of words, not coereced directly to a list. The same happens if a string is added to a CLVar, which allows doing the right thing with both Append()/Prepend() methods, as well as with pure Python addition, regardless of whether adding a list or a string to a construction variable.

Side effect: spaces will be stripped from individual string arguments. If you need spaces preserved, pass strings containing spaces inside a list argument.

>>> u = UserList("--some --opts and args") >>> print(len(u), repr(u)) 22 ['-', '-', 's', 'o', 'm', 'e', ' ', '-', '-', 'o', 'p', 't', 's', ' ', 'a', 'n', 'd', ' >>> c = CLVar("--some --opts and args") >>> print(len(c), repr(c)) 4 ['--some', '--opts', 'and', 'args'] >>> c += " strips spaces ">>> print(len(c), repr(c)) 6 ['--some', '--opts', 'and', 'args', 'strips', 'spaces'] >>> c += [" does not split or strip "] 7 ['--some', '--opts', 'and', 'args', 'strips', 'spaces', ' does not split or strip ']

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

class SCons.Util.Delegate ( attribute )

Bases: object

A Python Descriptor class that delegates attribute fetches to an underlying wrapped subject of a Proxy. Typical use:

SCons.Util package

184 class Foo(Proxy): __str__ = Delegate('__str__')

class SCons.Util.DispatchingFormatter ( formatters , default_formatter )

Bases: Formatter

Logging formatter which dispatches to various formatters.

converter ()

localtime([seconds]) -> (tm_year,tm_mon,tm_mday,tm_hour,tm_min,

tm_sec,tm_wday,tm_yday,tm_isdst)

Convert seconds since the Epoch to a time tuple expressing local time. When ‘seconds’ is not passed in, convert the current time instead.

default_msec_format = '%s,%03d'

default_time_format = '%Y-%m-%d %H:%M:%S'

format ( record )

Format the specified record as text.

The record’s attribute dictionary is used as the operand to a string formatting operation which yields the returned string. Before formatting the dictionary, a couple of preparatory steps are carried out. The message attribute of the record is computed using LogRecord.getMessage(). If the formatting string uses the time (as determined by a call to usesTime(), formatTime() is called to format the event time. If there is exception information, it is formatted using formatException() and appended to the message.

formatException ( ei )

Format and return the specified exception information as a string.

This default implementation just uses traceback.print_exception()

formatMessage ( record )

formatStack ( stack_info )

This method is provided as an extension point for specialized formatting of stack information.

The input data is a string as returned from a call to traceback.print_stack(), but with the last trailing newline removed.

The base implementation just returns the value passed in.

formatTime ( record , datefmt= None)

Return the creation time of the specified LogRecord as formatted text.

This method should be called from format() by a formatter which wants to make use of a formatted time. This method can be overridden in formatters to provide for any specific requirement, but the basic behaviour is as follows: if datefmt (a string) is specified, it is used with time.strftime() to format the creation time of the record. Otherwise, an ISO8601-like (or RFC 3339-like) format is used. The resulting string is returned. This function uses a user-configurable function to convert the creation time to a tuple. By default, time.localtime() is used; to change this for a particular formatter instance, set the ‘converter’ attribute to a function with the same signature as time.localtime() or time.gmtime(). To change it for all formatters, for example if you want all logging times to be shown in GMT, set the ‘converter’ attribute in the Formatter class.

usesTime ()

Check if the format uses the creation time of the record.

class SCons.Util.DisplayEngine

Bases: object

A callable class used to display SCons messages.

print_it = True

set_mode ( mode ) → None

SCons.Util.IDX ( n) → bool

Generate in index into strings from the tree legends.

These are always a choice between two, so bool works fine.

class SCons.Util.LogicalLines ( fileobj )

Bases: object

Wrapper class for the logical_lines() function.

Allows us to read all “logical” lines at once from a given file object.

readlines ()

class SCons.Util.NodeList ( initlist= None)

SCons.Util package

185 Bases: UserList

A list of Nodes with special attribute retrieval.

Unlike an ordinary list, access to a member’s attribute returns a NodeList containing the same attribute for each member. Although this can hold any object, it is intended for use when processing Nodes, where fetching an attribute of each member is very commone, for example getting the content signature of each node. The term “attribute” here includes the string representation.

>>> someList = NodeList([' foo ', ' bar ']) >>> someList.strip() ['foo', 'bar']

__getattr__ ( name ) → NodeList

Returns a NodeList of name from each member.

__getitem__ ( index )

Returns one item, forces a NodeList if index is a slice.

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

class SCons.Util.Proxy ( subject )

Bases: object

A simple generic Proxy class, forwarding all calls to subject.

This means you can take an object, let’s call it ‘obj_a` , and wrap it in this Proxy class, with a statement like this:

proxy_obj = Proxy(obj_a)

Then, if in the future, you do something like this:

x = proxy_obj.var1

since the Proxy class does not have a var1 attribute (but presumably obj_a does), the request actually is equivalent to saying:

x = obj_a.var1

Inherit from this class to create a Proxy.

With Python 3.5+ this does not work transparently for Proxy subclasses that use special dunder method names, because those names are now bound to the class, not the individual instances. You now need to know in advance

SCons.Util package

186 which special method names you want to pass on to the underlying Proxy object, and specifically delegate their calls like this:

class Foo(Proxy): __str__ = Delegate('__str__')

__getattr__ ( name )

Retrieve an attribute from the wrapped object.

Raises: AttributeError – if attribute name doesn’t exist.

get ()

Retrieve the entire wrapped object

SCons.Util.RegError

alias of _NoError

SCons.Util.RegGetValue ( root , key )

SCons.Util.RegOpenKeyEx ( root , key )

class SCons.Util.Selector

Bases: dict

A callable dict for file suffix lookup.

Often used to associate actions or emitters with file types.

Depends on insertion order being preserved so that get_suffix() calls always return the first suffix added.

clear () → None. Remove all items from D.

copy () → a shallow copy of D

classmethod fromkeys ( iterable , value= None, /)

Create a new dictionary with keys from iterable and values set to value.

get ( key , default= None, /)

Return the value for key if key is in the dictionary, else default.

items () → a set-like object providing a view on D's items

keys () → a set-like object providing a view on D's keys

pop ( k[, d]) → v, remove specified key and return the corresponding value.

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem ()

Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault ( key , default= None, /)

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update ([, E], **F ) → None. Update D from dict/iterable E and F.

If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

values () → an object providing a view on D's values

SCons.Util.Split ( arg ) → list

Returns a list of file names or other objects.

If arg is a string, it will be split on whitespace within the string. If arg is already a list, the list will be returned untouched. If arg is any other type of object, it will be returned in a single-item list.

>>> print(Split(" this is a string ")) ['this', 'is', 'a', 'string'] >>> print(Split(["stringlist", " preserving ", " spaces "])) ['stringlist', ' preserving ', ' spaces ']

class SCons.Util.Unbuffered ( file )

Bases: object

A proxy that wraps a file object, flushing after every write.

Delegates everything else to the wrapped object.

SCons.Util package

187 write ( arg ) → None

writelines ( arg ) → None

class SCons.Util.UniqueList ( initlist= None)

Bases: UserList

A list which maintains uniqueness.

Uniquing is lazy: rather than being enforced on list changes, it is fixed up on access by those methods which need to act on a unique list to be correct. That means things like membership tests don’t have to eat the uniquing time.

__make_unique () → None

_abc_impl = <_abc._abc_data object>

append ( item ) → None

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other ) → None

S.extend(iterable) – extend sequence by appending elements from the iterable

index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item ) → None

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse () → None

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

SCons.Util.WhereIs ( file , path= None, pathext= None, reject= None) → str | None

Return the path to an executable that matches file .

Searches the given path for file , considering any filename extensions in pathext (on the Windows platform only), and returns the full path to the matching command of the first match, or None if there are no matches. Will not select any path name or names in the optional reject list.

If path is None (the default), os.environ[PATH] is used. On Windows, If pathext is None (the default), os.environ[PATHEXT] is used.

The construction environment method of the same name wraps a call to this function by filling in path from the execution environment if it is None (and for pathext on Windows, if necessary), so if called from there, this function will not backfill from os.environ.

# Note

Finding things in os.environ may answer the question “does file exist on the system”, but not the question “can SCons use that executable”, unless the path element that yields the match is also in the the Execution Environment (e.g. env['ENV']['PATH'] ). Since this utility function has no environment reference, it cannot make that determination.

exception SCons.Util._NoError

Bases: Exception

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

SCons.Util._is_process_alive ( pid: int ) → bool

SCons.Util package

188 SCons.Util._semi_deepcopy_list ( obj ) → list

SCons.Util._semi_deepcopy_tuple ( obj ) → tuple

SCons.Util._wait_for_process_to_die_non_psutil ( pid: int , timeout: float = 60.0) → None

SCons.Util.adjustixes ( fname , pre , suf , ensure_suffix: bool = False) → str

Adjust filename prefixes and suffixes as needed.

Add prefix to fname if specified. Add suffix to fname if specified and if ensure_suffix is True

SCons.Util.case_sensitive_suffixes ( s1: str , s2: str ) → bool

Returns whether platform distinguishes case in file suffixes.

SCons.Util.cmp ( a, b) → bool

A cmp function because one is no longer available in Python3.

SCons.Util.containsAll ( s, pat ) → bool

Check whether string s contains ALL of the items in pat .

SCons.Util.containsAny ( s, pat ) → bool

Check whether string s contains ANY of the items in pat .

SCons.Util.containsOnly ( s, pat ) → bool

Check whether string s contains ONLY items in pat .

SCons.Util.dictify ( keys , values , result= None) → dict

SCons.Util.do_flatten ( sequence , result , isinstance=<built-in function isinstance> ,

StringTypes=(<class 'str'> , <class 'collections.UserString'>) , SequenceTypes=(<class 'list'> , <class 'tuple'> , <class 'collections.deque'> , <class 'collections.UserList'> ,

<class 'collections.abc.KeysView'> , <class 'collections.abc.ValuesView'> , <class 'collections.abc.ItemsView'>) ) → None

SCons.Util.flatten ( obj , isinstance=<built-in function isinstance> , StringTypes=(<class 'str'> ,

<class 'collections.UserString'>) , SequenceTypes=(<class 'list'> , <class 'tuple'> , <class 'collections.deque'> , <class 'collections.UserList'> , <class 'collections.abc.KeysView'> ,

<class 'collections.abc.ValuesView'> , <class 'collections.abc.ItemsView'>) ,

do_flatten=<function do_flatten> ) → list

Flatten a sequence to a non-nested list.

Converts either a single scalar or a nested sequence to a non-nested list. Note that flatten() considers strings to be scalars instead of sequences like pure Python would.

SCons.Util.flatten_sequence ( sequence , isinstance=<built-in function isinstance> ,

StringTypes=(<class 'str'> , <class 'collections.UserString'>) , SequenceTypes=(<class 'list'> , <class 'tuple'> , <class 'collections.deque'> , <class 'collections.UserList'> ,

<class 'collections.abc.KeysView'> , <class 'collections.abc.ValuesView'> , <class 'collections.abc.ItemsView'>) , do_flatten=<function do_flatten> ) → list

Flatten a sequence to a non-nested list.

Same as flatten(), but it does not handle the single scalar case. This is slightly more efficient when one knows that the sequence to flatten can not be a scalar.

SCons.Util.get_native_path ( path: str ) → str

Transform an absolute path into a native path for the system.

In Cygwin, this converts from a Cygwin path to a Windows path, without regard to whether path refers to an existing file system object. For other platforms, path is unchanged.

SCons.Util.logical_lines ( physical_lines , joiner=<built-in method join of str object> )

SCons.Util.make_path_relative ( path ) → str

Converts an absolute path name to a relative pathname.

SCons.Util.print_time ()

Hack to return a value from Main if can’t import Main.

SCons.Util.print_tree ( root , child_func , prune: bool = False, showtags: int = 0, margin: list[bool] = [False], visited: dict | None = None, lastChild: bool = False, singleLineDraw: bool = False)

→ None

Print a tree of nodes.

This is like func: render_tree , except it prints lines directly instead of creating a string representation in memory, so that huge trees can be handled.

SCons.Util package

189 Parameters: • root – the root node of the tree

• child_func – the function called to get the children of a node

• prune – don’t visit the same node twice

• showtags – print status information to the left of each node line The default is false (value 0). A value of 2 will also print a legend for the margin tags.

• margin – the format of the left margin to use for children of root . Each entry represents a column, where a true value will display a vertical bar and a false one a blank.

• visited – a dictionary of visited nodes in the current branch if prune is false, or in the whole tree if prune is true.

• lastChild – this is the last leaf of a branch

• singleLineDraw – use line-drawing characters rather than ASCII.

SCons.Util.render_tree ( root , child_func , prune: bool = False, margin: list[bool] = [False], visited: dict | None = None) → str

Render a tree of nodes into an ASCII tree view.

Parameters: • root – the root node of the tree

• child_func – the function called to get the children of a node

• prune – don’t visit the same node twice

• margin – the format of the left margin to use for children of root . Each entry represents a column where a true value will display a vertical bar and a false one a blank.

• visited – a dictionary of visited nodes in the current branch if prune is false, or in the whole tree if prune is true.

SCons.Util.rightmost_separator ( path , sep )

SCons.Util.sanitize_shell_env ( execution_env: dict ) → dict

Sanitize all values in execution_env

The execution environment (typically comes from env['ENV'] ) is propagated to the shell, and may need to be cleaned first.

Parameters: • execution_env – The shell environment variables to be propagated

• shell. (to the spawned )

Returns: sanitized dictionary of env variables (similar to what you’d get from os.environ)

SCons.Util.semi_deepcopy ( obj )

SCons.Util.semi_deepcopy_dict ( obj , exclude= None) → dict

SCons.Util.silent_intern ( __string: Any ) → str

Intern a string without failing.

Perform sys.intern on the passed argument and return the result. If the input is ineligible for interning the original argument is returned and no exception is thrown.

SCons.Util.splitext ( path ) → tuple

Split path into a (root, ext) pair.

Same as os.path.splitext but faster.

SCons.Util.unique ( seq )

Return a list of the elements in seq without duplicates, ignoring order.

For best speed, all sequence elements should be hashable. Then unique() will usually work in linear time.

If not possible, the sequence elements should enjoy a total ordering, and if list(s).sort() doesn’t raise

TypeError it is assumed that they do enjoy a total ordering. Then unique() will usually work in O(N*log2(N)) time.

If that’s not possible either, the sequence elements must support equality-testing. Then unique() will usually work in quadratic time.

SCons.Util package

190 >>> mylist = unique([1, 2, 3, 1, 2, 3]) >>> print(sorted(mylist)) [1, 2, 3] >>> mylist = unique("abcabc") >>> print(sorted(mylist)) ['a', 'b', 'c'] >>> mylist = unique(([1, 2], [2, 3], [1, 2])) >>> print(sorted(mylist)) [[1, 2], [2, 3]]

SCons.Util.uniquer_hashables ( seq )

SCons.Util.updrive ( path ) → str

Make the drive letter (if any) upper case.

This is useful because Windows is inconsistent on the case of the drive letter, which can cause inconsistencies when calculating command signatures.

SCons.Util.wait_for_process_to_die ( pid: int ) → None

Wait for the specified process to die.

TODO: Add timeout which raises exception

# Submodules

# SCons.Util.envs module

SCons environment utility functions.

Routines for working with environments and construction variables that don’t need the specifics of the Environment class.

SCons.Util.envs.AddMethod ( obj , function: Callable , name: str | None = None) → None

Add a method to an object.

Adds function to obj if obj is a class object. Adds function as a bound method if obj is an instance object. If obj looks like an environment instance, use MethodWrapper to add it. If name is supplied it is used as the name of function .

Although this works for any class object, the intent as a public API is to be used on Environment, to be able to add a method to all construction environments; it is preferred to use env.AddMethod to add to an individual environment.

>>> class A: ... ...

>>> a = A()

>>> def f(self, x, y): ... self.z = x + y

>>> AddMethod(A, f, "add") >>> a.add(2, 4) >>> print(a.z) 6>>> a.data = ['a', 'b', 'c', 'd', 'e', 'f'] >>> AddMethod(a, lambda self, i: self.data[i], "listIndex") >>> print(a.listIndex(3)) d

SCons.Util.envs.AddPathIfNotExists ( env_dict , key , path , sep: str = ':') → None

Add a path element to a construction variable.

SCons.Util package

191 key is looked up in env_dict , and path is added to it if it is not already present. env_dict[key] is assumed to be in the format of a PATH variable: a list of paths separated by sep tokens.

>>> env = {'PATH': '/bin:/usr/bin:/usr/local/bin'} >>> AddPathIfNotExists(env, 'PATH', '/opt/bin') >>> print(env['PATH']) /opt/bin:/bin:/usr/bin:/usr/local/bin

SCons.Util.envs.AppendPath ( oldpath , newpath , sep= ':', delete_existing: bool = True, canonicalize: Callable | None = None) → list | str

Append newpath path elements to oldpath .

Will only add any particular path once (leaving the last one it encounters and ignoring the rest, to preserve path order), and will os.path.normpath and os.path.normcase all paths for comparisons to help assure this. oldpath may be a list instead of a string, in which case a list is returned.

Example:

>>> p = AppendPath("/foo/bar:/foo", "/biz/boom:/foo") >>> print(p) /foo/bar:/biz/boom:/foo

If delete_existing is False , then adding a path that exists will not move it to the end; it will stay where it is in the list.

>>> p = AppendPath("/foo/bar:/foo", "/biz/boom:/foo", delete_existing=False) >>> print(p) /foo/bar:/foo:/biz/boom

If canonicalize is not None , it is applied to each element of newpath before use.

class SCons.Util.envs.MethodWrapper ( obj: Any , method: Callable , name: str | None = None)

Bases: object

A generic Wrapper class that associates a method with an object.

As part of creating this MethodWrapper object an attribute with the specified name (by default, the name of the supplied method) is added to the underlying object. When that new “method” is called, our __call__() method adds the object as the first argument, simulating the Python behavior of supplying “self” on method calls.

We hang on to the name by which the method was added to the underlying base class so that we can provide a method to “clone” ourselves onto a new underlying object being copied (without which we wouldn’t need to save that info).

clone ( new_object )

Returns an object that re-binds the underlying “method” to the specified new object.

SCons.Util.envs.PrependPath ( oldpath , newpath , sep= ':', delete_existing: bool = True, canonicalize: Callable | None = None) → list | str

Prepend newpath path elements to oldpath .

Will only add any particular path once (leaving the first one it encounters and ignoring the rest, to preserve path order), and will os.path.normpath and os.path.normcase all paths for comparisons to help assure this. oldpath may be a list instead of a string, in which case a list is returned.

Example:

>>> p = PrependPath("/foo/bar:/foo", "/biz/boom:/foo") >>> print(p) /biz/boom:/foo:/foo/bar

If delete_existing is False , then adding a path that exists will not move it to the beginning; it will stay where it is in the list.

SCons.Util package

192 >>> p = PrependPath("/foo/bar:/foo", "/biz/boom:/foo", delete_existing=False) >>> print(p) /biz/boom:/foo/bar:/foo

If canonicalize is not None , it is applied to each element of newpath before use.

SCons.Util.envs.is_valid_construction_var ( varstr: str ) → bool

Return True if varstr is a legitimate name of a construction variable.

# SCons.Util.filelock module

SCons file locking functions.

Simple-minded filesystem-based locking. Provides a context manager which acquires a lock (or at least, permission) on entry and releases it on exit.

Usage:

from SCons.Util.filelock import FileLock with FileLock("myfile.txt", writer=True) as lock: print(f"Lock on {lock.file} acquired.") # work with the file as it is now locked

class SCons.Util.filelock.FileLock ( file: str , timeout: int | None = None, delay: float | None =

0.05, writer: bool = False)

Bases: object

Lock a file using a lockfile.

Basic locking for when multiple processes may hit an externally shared resource that cannot depend on locking within a single SCons process. SCons does not have a lot of those, but caches come to mind.

Cross-platform safe, does not use any OS-specific features. Provides context manager support, or can be called with acquire_lock() and release_lock().

Lock can be a write lock, which is held until released, or a read lock, which releases immediately upon aquisition - we want to not read a file which somebody else may be writing, but not create the writers starvation problem of the classic readers/writers lock.

TODO: Should default timeout be None (non-blocking), or 0 (block forever),

or some arbitrary number?

Parameters: • file – name of file to lock. Only used to build the lockfile name.

• timeout – optional time (sec) to give up trying. If None , quit now if we failed to get the lock (non-blocking). If 0, block forever (well, a long time).

• delay – optional delay between tries [default 0.05s]

• writer – if True, obtain the lock for safe writing. If False (default), just wait till the lock is available, give it back right away.

Raises: SConsLockFailure – if the operation “timed out”, including the non-blocking mode.

__enter__ () → FileLock

Context manager entry: acquire lock if not holding.

__exit__ ( exc_type , exc_value , exc_tb ) → None

Context manager exit: release lock if holding.

__repr__ () → str

Nicer display if someone repr’s the lock class.

acquire_lock () → None

Acquire the lock, if possible.

If the lock is in use, check again every delay seconds. Continue until lock acquired or timeout expires.

SCons.Util package

193 release_lock () → None

Release the lock by deleting the lockfile.

exception SCons.Util.filelock.SConsLockFailure

Bases: Exception

Lock failure exception.

add_note ()

Exception.add_note(note) – add a note to the exception

args

with_traceback ()

Exception.with_traceback(tb) – set self.__traceback__ to tb and return self.

# SCons.Util.hashes module

SCons hash utility routines.

Routines for working with content and signature hashes.

SCons.Util.hashes.MD5collect ( signatures )

Deprecated. Use hash_collect() instead.

SCons.Util.hashes.MD5filesignature ( fname , chunksize: int = 65536)

Deprecated. Use hash_file_signature() instead.

SCons.Util.hashes.MD5signature ( s)

Deprecated. Use hash_signature() instead.

SCons.Util.hashes._attempt_get_hash_function ( hash_name , hashlib_used=<module 'hashlib' from '/opt /local/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/hashlib.py'> ,

sys_used=<module 'sys' (built-in)> )

Wrapper used to try to initialize a hash function given.

If successful, returns the name of the hash function back to the user.

Otherwise returns None.

SCons.Util.hashes._attempt_init_of_python_3_9_hash_object ( hash_function_object , sys_used=<module 'sys' (built-in)> )

Initialize hash function with non-security indicator.

In Python 3.9 and onwards, hashlib constructors accept a keyword argument usedforsecurity , which, if set to False ,lets us continue to use algorithms that have been deprecated either by FIPS or by Python itself, as the MD5 algorithm SCons prefers is not being used for security purposes as much as a short, 32 char hash that is resistant to accidental collisions.

In prior versions of python, hashlib returns a native function wrapper, which errors out when it’s queried for the optional parameter, so this function wraps that call.

It can still throw a ValueError if the initialization fails due to FIPS compliance issues, but that is assumed to be the responsibility of the caller.

SCons.Util.hashes._get_hash_object ( hash_format , hashlib_used=<module 'hashlib' from '/opt/local /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/hashlib.py'> ,

sys_used=<module 'sys' (built-in)> )

Allocates a hash object using the requested hash format.

Parameters: hash_format – Hash format to use.

Returns: hashlib object.

SCons.Util.hashes._set_allowed_viable_default_hashes ( hashlib_used , sys_used=<module 'sys' (built-in)> ) → None

Check if the default hash algorithms can be called.

This util class is sometimes called prior to setting the user-selected hash algorithm, meaning that on FIPS-compliant systems the library would default-initialize MD5 and throw an exception in set_hash_format. A common case is using the SConf options, which can run prior to main, and thus ignore the options.hash_format variable.

This function checks the DEFAULT_HASH_FORMATS and sets the ALLOWED_HASH_FORMATS to only the ones that can be called. In Python >= 3.9 this will always default to MD5 as in Python 3.9 there is an optional attribute “usedforsecurity” set for the method.

Throws if no allowed hash formats are detected.

SCons.Util.hashes._show_md5_warning ( function_name ) → None

SCons.Util package

194 Shows a deprecation warning for various MD5 functions.

SCons.Util.hashes.get_current_hash_algorithm_used ()

Returns the current hash algorithm name used.

Where the python version >= 3.9, this is expected to return md5. If python’s version is <= 3.8, this returns md5 on non-FIPS-mode platforms, and sha1 or sha256 on FIPS-mode Linux platforms.

This function is primarily useful for testing, where one expects a value to be one of N distinct hashes, and therefore the test needs to know which hash to select.

SCons.Util.hashes.get_hash_format ()

Retrieves the hash format or None if not overridden.

A return value of None does not guarantee that MD5 is being used; instead, it means that the default precedence order documented in SCons.Util.set_hash_format() is respected.

SCons.Util.hashes.hash_collect ( signatures , hash_format= None)

Collects a list of signatures into an aggregate signature.

Parameters: • signatures – a list of signatures

• hash_format – Specify to override default hash format

Returns: the aggregate signature

SCons.Util.hashes.hash_file_signature ( fname: str , chunksize: int = 65536, hash_format= None) → str

Generate the md5 signature of a file

Parameters: • fname – file to hash

• chunksize – chunk size to read

• hash_format – Specify to override default hash format

Returns: String of Hex digits representing the signature

SCons.Util.hashes.hash_signature ( s, hash_format= None)

Generate hash signature of a string

Parameters: • s – either string or bytes. Normally should be bytes

• hash_format – Specify to override default hash format

Returns: String of hex digits representing the signature

SCons.Util.hashes.set_hash_format ( hash_format , hashlib_used=<module 'hashlib' from '/opt/local/ Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/hashlib.py'> ,

sys_used=<module 'sys' (built-in)> )

Sets the default hash format used by SCons.

If hash_format is None or an empty string, the default is determined by this function.

Currently the default behavior is to use the first available format of the following options: MD5, SHA1, SHA256.

# SCons.Util.sctypes module

Various SCons utility functions

Routines which check types and do type conversions.

class SCons.Util.sctypes.Null ( *args , **kwargs )

Bases: object

Null objects always and reliably ‘do nothing’.

class SCons.Util.sctypes.NullSeq ( *args , **kwargs )

Bases: Null

A Null object that can also be iterated over.

SCons.Util.sctypes.get_env_bool ( env , name: str , default: bool = False) → bool

Convert a construction variable to bool.

If the value of name in dict-like object env is ‘true’, ‘yes’, ‘y’, ‘on’ (case insensitive) or anything convertible to int that yields non-zero, return True ; if ‘false’, ‘no’, ‘n’, ‘off’ (case insensitive) or a number that converts to integer zero return

False . Otherwise, or if name is not found, return the value of default .

SCons.Util package

195 Parameters: • env – construction environment, or any dict-like object.

• name – name of the variable.

• default – value to return if name not in env or cannot be converted (default: False).

SCons.Util.sctypes.get_environment_var ( varstr ) → str | None

Return undecorated construction variable string.

Determine if varstr looks like a reference to a single environment variable, like "$FOO" or "${FOO}" . If so, return that variable with no decorations, like "FOO" . If not, return None .

SCons.Util.sctypes.get_os_env_bool ( name: str , default: bool = False) → bool

Convert an external environment variable to boolean.

Like get_env_bool(), but uses os.environ as the lookup dict.

SCons.Util.sctypes.is_Dict ( obj , isinstance=<built-in function isinstance> , DictTypes=(<class 'dict'> , <class 'collections.UserDict'>) ) → TypeGuard [dict | UserDict ]

Check if object is a dict.

SCons.Util.sctypes.is_List ( obj , isinstance=<built-in function isinstance> , ListTypes=(<class 'list'> , <class 'collections.UserList'> , <class 'collections.deque'>) ) → TypeGuard [list |

UserList | deque ]

Check if object is a list.

SCons.Util.sctypes.is_Scalar ( obj , isinstance=<built-in function isinstance> , StringTypes=(<class 'str'> , <class 'collections.UserString'>) , Iterable=<class 'collections.abc.Iterable'> ) →

bool

Check if object is a scalar: not a container or iterable.

SCons.Util.sctypes.is_Sequence ( obj , isinstance=<built-in function isinstance> ,

SequenceTypes=(<class 'list'> , <class 'tuple'> , <class 'collections.deque'> , <class 'collections.UserList'> , <class 'collections.abc.KeysView'> , <class 'collections.abc.ValuesView'> , <class 'collections.abc.ItemsView'>) ) → TypeGuard [list | tuple

| deque | UserList | KeysView | ValuesView | ItemsView ]

Check if object is a sequence.

SCons.Util.sctypes.is_String ( obj , isinstance=<built-in function isinstance> , StringTypes=(<class 'str'> , <class 'collections.UserString'>) ) → TypeGuard [str | UserString ]

Check if object is a string.

SCons.Util.sctypes.is_Tuple ( obj , isinstance=<built-in function isinstance> , tuple=<class 'tuple'> ) → TypeGuard [tuple ]

Check if object is a tuple.

SCons.Util.sctypes.to_String ( obj , isinstance=<built-in function isinstance> , str=<class 'str'> ,

UserString=<class 'collections.UserString'> , BaseStringTypes=<class 'str'> ) → str

Return a string version of obj.

Use this for data likely to be well-behaved. Use to_Text() for unknown file data that needs to be decoded.

SCons.Util.sctypes.to_String_for_signature ( obj , to_String_for_subst=<function to_String_for_subst> ,

AttributeError=<class 'AttributeError'> ) → str

Return a string version of obj for signature usage.

Like to_String_for_subst() but has special handling for scons objects that have a for_signature() method, and for dicts.

SCons.Util.sctypes.to_String_for_subst ( obj , isinstance=<built-in function isinstance> , str=<class 'str'> , BaseStringTypes=<class 'str'> , SequenceTypes=(<class 'list'> , <class 'tuple'> ,

<class 'collections.deque'> , <class 'collections.UserList'> , <class 'collections.abc.KeysView'> , <class 'collections.abc.ValuesView'> , <class 'collections.abc.ItemsView'>) , UserString=<class 'collections.UserString'> ) → str

Return a string version of obj for subst usage.

SCons.Util.sctypes.to_Text ( data: bytes ) → str

Return bytes data converted to text.

Useful for whole-file reads where the data needs some interpretation, particularly for Scanners. Attempts to figure out what the encoding of the text is based upon the BOM bytes, and then decodes the contents so that it’s a valid python string.

SCons.Util.sctypes.to_bytes ( s) → bytes

SCons.Util package

196 Convert object to bytes.

SCons.Util.sctypes.to_str ( s) → str

Convert object to string.

# SCons.Util.stats module

SCons statistics routines.

This package provides a way to gather various statistics during an SCons run and dump that info in several formats

Additionally, it probably makes sense to do stderr/stdout output of those statistics here as well

There are basically two types of stats:

1. Timer (start/stop/time) for specific event. These events can be hierarchical. So you can record the children events of some parent. Think program compile could contain the total Program builder time, which could include linking, and stripping the executable

2. Counter. Counting the number of events and/or objects created. This would likely only be reported at the end of a given SCons run, though it might be useful to query during a run.

class SCons.Util.stats.CountStats

Bases: Stats

_abc_impl = <_abc._abc_data object>

do_append ( label )

do_nothing ( *args , **kw )

do_print ()

enable ( outfp )

class SCons.Util.stats.MemStats

Bases: Stats

_abc_impl = <_abc._abc_data object>

do_append ( label )

do_nothing ( *args , **kw )

do_print ()

enable ( outfp )

class SCons.Util.stats.Stats

Bases: ABC

_abc_impl = <_abc._abc_data object>

do_append ( label )

do_nothing ( *args , **kw )

do_print ()

enable ( outfp )

class SCons.Util.stats.TimeStats

Bases: Stats

_abc_impl = <_abc._abc_data object>

add_command ( command , start_time , finish_time )

do_append ( label )

do_nothing ( *args , **kw )

do_print ()

enable ( outfp )

total_times ( build_time , sconscript_time , scons_exec_time , command_exec_time )

SCons.Util.stats.add_stat_type ( name , stat_object )

Add a statistic type to the global collection

SCons.Util.stats.write_scons_stats_file ()

Actually write the JSON file with debug information. Depending which of : count, time, action-timestamps,memory their information will be written.

SCons.Util package

197 SCons.Variables package

# Module contents

Adds user-friendly customizable variables to an SCons build.

SCons.Variables.BoolVariable ( key , help: str , default ) → tuple [str , str , str , Callable , Callable ]

Return a tuple describing a boolean SCons Variable.

The input parameters describe a boolean variable, using a string value as described by TRUE_STRINGS and FALSE_STRINGS. Returns a tuple including the correct converter and validator. The help text will have (yes|no)

automatically appended to show the valid values. The result is usable as input to Add().

SCons.Variables.EnumVariable ( key , help: str , default: str , allowed_values: list[str] , map: dict | None = None, ignorecase: int = 0) → tuple [str , str , str , Callable , Callable ]

Return a tuple describing an enumaration SCons Variable.

An Enum Variable is an abstraction that allows choosing one value from a provided list of possibilities (allowed_values ). The value of ignorecase defines the behavior of the validator and converter: if 0, the validator/converter are case-sensitive; if 1, the validator/converter are case-insensitive; if 2, the validator/converter are case-insensitive and the converted value will always be lower-case.

Parameters: • key – the name of the variable.

• default – default value, passed directly through to the return tuple.

• help – descriptive part of the help text, will have the allowed values automatically appended.

• allowed_values – the values for the choice.

• map – optional dictionary which may be used for converting the input value into canonical values (e.g. for aliases).

• ignorecase – defines the behavior of the validator and converter.

Returns: A tuple including an appropriate converter and validator. The result is usable as input to Add(). and AddVariables().

SCons.Variables.ListVariable ( key , help: str , default: str | list[str] , names: list[str] , map: dict | None = None, validator: Callable | None = None) → tuple [str , str , str , Callable , Callable ]

Return a tuple describing a list variable.

A List Variable is an abstraction that allows choosing one or more values from a provided list of possibilities ( names ). The special terms “all” and “none” are also provided to help make the selection.

Parameters: • key – the name of the list variable.

• help – the basic help message. Will have text appended indicating the allowed values (not including any extra names from map ).

• default – the default value(s) for the list variable. Can be given as string (use commas to -separated multiple values), or as a list of strings. “all” or “none” are allowed as default . A must-specify list variable can be simulated by giving a value that is not part of names ,which will cause validation to fail if the variable is not supplied in the input sources.

• names – the values to choose from. Must be a list of strings.

• map – optional dictionary to map alternative names to the ones in names , providing a form of alias. The converter will perform the replacement. Names from map are not stored, and will not appear in the help message.

• validator – optional callback to validate supplied values. The default validator is used if not specified.

Returns: A tuple including the correct converter and validator. The result is usable as input to Add().

Changed in version 4.8.0: The validation step was split from the converter to allow for custom validators. The

validator keyword argument was added.

SCons.Variables package

198 SCons.Variables.PackageVariable ( key: str , help: str , default , searchfunc: Callable | None = None)

→ tuple [str , str , str , Callable , Callable ]

Return a tuple describing a package list SCons Variable.

The input parameters describe a ‘package list’ variable. Returns a tuple with the correct converter and validator appended. The result is usable as input to Add().

A ‘package list’ variable may be specified as a truthy string from ENABLE_STRINGS, a falsy string from DISABLE_STRINGS, or as a pathname string. This information is appended to help using only one string each for truthy/falsy.

class SCons.Variables.Variable ( key: str , aliases: list[str] , help: str , default: Any , validator: Callable | None , converter: Callable | None , do_subst: bool )

Bases: object

A Build Variable.

aliases : list [str ]

converter : Callable | None

default : Any

do_subst : bool

help : str

key : str

validator : Callable | None

class SCons.Variables.Variables ( files: str | Sequence[str | None] = None, args: dict | None =

None, is_global: bool = False)

Bases: object

A container for Build Variables.

Includes a method to populate the variables with values into a construction envirionment, and methods to render the help text.

Note that the pubic API for creating a Variables object is SCons.Script.Variables(), a kind of factory function, which defaults to supplying the contents of ARGUMENTS as the args parameter if it was not otherwise given. That is the behavior documented in the manpage for Variables - and different from the default if you instantiate this directly.

Parameters: • files – string or list of strings naming variable config scripts (default None )

• args – dictionary to override values set from files . (default None )

• is_global – if true, return a global singleton Variables object instead of a fresh instance. Currently inoperable (default False )

Changed in version 4.8.0: The default for is_global changed to False (the previous default True had no effect due to an implementation error).

Deprecated since version 4.8.0: is_global is deprecated.

Added in version 4.9.0: The defaulted attribute now lists those variables which were filled in from default values.

Add ( key: str | Sequence , *args , **kwargs ) → None

Add a Build Variable.

Parameters: • key – the name of the variable, or a 5-tuple (or other sequence). If key is a tuple, and there are no additional arguments except the help , default , validator and converter

keyword arguments, key is unpacked into the variable name plus the help , default ,

validator and converter arguments; if there are additional arguments, the first elements of key is taken as the variable name, and the remainder as aliases.

• args – optional positional arguments, corresponding to the help , default , validator and

converter keyword args.

• kwargs – arbitrary keyword arguments used by the variable itself.

SCons.Variables package

199 Keyword Arguments: • help – help text for the variable (default: empty string)

• default – default value for variable (default: None )

• validator – function called to validate the value (default: None )

• converter – function to be called to convert the variable’s value before putting it in the environment. (default: None )

• subst – perform substitution on the value before the converter and validator functions (if any) are called (default: True )

Added in version 4.8.0: The subst keyword argument is now specially recognized.

AddVariables ( *optlist ) → None

Add Build Variables.

Each optlist element is a sequence of arguments to be passed on to the underlying method for adding variables.

Example:

opt = Variables() opt.AddVariables( ('debug', '', 0), ('CC', 'The C compiler'), ('VALIDATE', 'An option for testing validation', 'notset', validator, None), )

FormatVariableHelpText ( env , key: str , help: str , default , actual , aliases: list[str | None] =

None) → str

Format the help text for a single variable.

The caller is responsible for obtaining all the values, although now the Variable class is more publicly exposed, this method could easily do most of that work - however that would change the existing published API.

GenerateHelpText ( env , sort: bool | Callable = False) → str

Generate the help text for the Variables object.

Parameters: • env – an environment that is used to get the current values of the variables.

• sort – Either a comparison function used for sorting (must take two arguments and return -1 , 0 or 1) or a boolean to indicate if it should be sorted.

Save ( filename , env ) → None

Save the variables to a script.

Saves all the variables which have non-default settings to the given file as Python expressions. This script can then be used to load the variables for a subsequent run. This can be used to create a build variable “cache” or capture different configurations for selection.

Parameters: • filename – Name of the file to save into

• env – the environment to get the option values from

UnknownVariables () → dict

Return dict of unknown variables.

Identifies variables that were not recognized in this object.

Update ( env , args: dict | None = None) → None

Update an environment with the Build Variables.

This is where the work of adding variables to the environment happens, The input sources saved at init time are scanned for variables to add, though if args is passed, then it is used instead of the saved one. If any variable description set up a callback for a validator and/or converter, those are called. Variables from the input sources which do not match a variable description in this object are ignored for purposes of adding to env , but are saved in the unknown dict attribute. Variables which are set in env from the default in a variable description and not from the input sources are saved in the defaulted list attribute.

SCons.Variables package

200 Parameters: • env – the environment to update.

• args – a dictionary of keys and values to update in env . If omitted, uses the saved args

__str__ () → str

Provide a way to “print” a Variables object.

_do_add ( key: str | Sequence[str] , help: str = '', default= None, validator: Callable | None = None, converter: Callable | None = None, **kwargs ) → None

Create a Variable and add it to the list.

This is the internal implementation for Add() and AddVariables(). Not part of the public API.

Added in version 4.8.0: subst keyword argument is now recognized.

aliasfmt = '\n%s: %s\n default: %s\n actual: %s\n aliases: %s\n'

fmt = '\n%s: %s\n default: %s\n actual: %s\n'

keys () → list

Return the variable names.

# Submodules

# SCons.Variables.BoolVariable module

Variable type for true/false Variables.

Usage example:

opts = Variables() opts.Add(BoolVariable('embedded', 'build for an embedded system', False)) env = Environment(variables=opts) if env['embedded']: ...

SCons.Variables.BoolVariable.BoolVariable ( key , help: str , default ) → tuple [str , str , str , Callable ,

Callable ]

Return a tuple describing a boolean SCons Variable.

The input parameters describe a boolean variable, using a string value as described by TRUE_STRINGS and FALSE_STRINGS. Returns a tuple including the correct converter and validator. The help text will have (yes|no)

automatically appended to show the valid values. The result is usable as input to Add().

SCons.Variables.BoolVariable._text2bool ( val: str | bool ) → bool

Convert boolean-like string to boolean.

If val looks like it expresses a bool-like value, based on the TRUE_STRINGS and FALSE_STRINGS tuples, return the appropriate value.

This is usable as a converter function for SCons Variables.

Raises: ValueError – if val cannot be converted to boolean.

SCons.Variables.BoolVariable._validator ( key: str , val , env ) → None

Validate that the value of key in env is a boolean.

Parameter val is not used in the check.

Usable as a validator function for SCons Variables.

Raises: • KeyError – if key is not set in env

• UserError – if the value of key is not True or False .

# SCons.Variables.EnumVariable module

Variable type for enumeration Variables.

Enumeration variables allow selection of one from a specified set of values.

Usage example:

SCons.Variables package

201 opts = Variables() opts.Add( EnumVariable( 'debug', help='debug output and symbols', default='no', allowed_values=('yes', 'no', 'full'), map={}, ignorecase=2, ))env = Environment(variables=opts) if env['debug'] == 'full': ...

SCons.Variables.EnumVariable.EnumVariable ( key , help: str , default: str , allowed_values: list[str] ,

map: dict | None = None, ignorecase: int = 0) → tuple [str , str , str , Callable , Callable ]

Return a tuple describing an enumaration SCons Variable.

An Enum Variable is an abstraction that allows choosing one value from a provided list of possibilities (allowed_values ). The value of ignorecase defines the behavior of the validator and converter: if 0, the validator/converter are case-sensitive; if 1, the validator/converter are case-insensitive; if 2, the validator/converter are case-insensitive and the converted value will always be lower-case.

Parameters: • key – the name of the variable.

• default – default value, passed directly through to the return tuple.

• help – descriptive part of the help text, will have the allowed values automatically appended.

• allowed_values – the values for the choice.

• map – optional dictionary which may be used for converting the input value into canonical values (e.g. for aliases).

• ignorecase – defines the behavior of the validator and converter.

Returns: A tuple including an appropriate converter and validator. The result is usable as input to Add(). and AddVariables().

SCons.Variables.EnumVariable._validator ( key , val , env , vals ) → None

Validate that val is in vals.

Usable as the base for EnumVariable validators.

# SCons.Variables.ListVariable module

Variable type for List Variables.

A list variable allows selecting one or more from a supplied set of allowable values, as well as from an optional mapping of alternate names (such as aliases and abbreviations) and the special names “all” and “none”. Specified values are converted during processing into values only from the allowable values set.

Usage example:

list_of_libs = Split('x11 gl qt ical') opts = Variables() opts.Add( ListVariable( 'shared',

SCons.Variables package

202 help='libraries to build as shared libraries', default='all', elems=list_of_libs, ))env = Environment(variables=opts) for lib in list_of_libs: if lib in env['shared']: env.SharedObject(...) else: env.Object(...)

SCons.Variables.ListVariable.ListVariable ( key , help: str , default: str | list[str] , names: list[str] ,

map: dict | None = None, validator: Callable | None = None) → tuple [str , str , str , Callable ,

Callable ]

Return a tuple describing a list variable.

A List Variable is an abstraction that allows choosing one or more values from a provided list of possibilities ( names ). The special terms “all” and “none” are also provided to help make the selection.

Parameters: • key – the name of the list variable.

• help – the basic help message. Will have text appended indicating the allowed values (not including any extra names from map ).

• default – the default value(s) for the list variable. Can be given as string (use commas to -separated multiple values), or as a list of strings. “all” or “none” are allowed as default . A must-specify list variable can be simulated by giving a value that is not part of names ,which will cause validation to fail if the variable is not supplied in the input sources.

• names – the values to choose from. Must be a list of strings.

• map – optional dictionary to map alternative names to the ones in names , providing a form of alias. The converter will perform the replacement. Names from map are not stored, and will not appear in the help message.

• validator – optional callback to validate supplied values. The default validator is used if not specified.

Returns: A tuple including the correct converter and validator. The result is usable as input to Add().

Changed in version 4.8.0: The validation step was split from the converter to allow for custom validators. The

validator keyword argument was added.

class SCons.Variables.ListVariable._ListVariable ( initlist: list | None = None, allowedElems: list | None = None)

Bases: UserList

Internal class holding the data for a List Variable.

This is normally not directly instantiated, rather the ListVariable converter callback “converts” string input (or the default value if none) into an instance and stores it.

Parameters: • initlist – the list of actual values given.

• allowedElems – the list of allowable values.

_abc_impl = <_abc._abc_data object>

append ( item )

S.append(value) – append value to the end of the sequence

clear () → None -- remove all items from S

copy ()

count ( value ) → integer -- return number of occurrences of value

extend ( other )

S.extend(iterable) – extend sequence by appending elements from the iterable

SCons.Variables package

203 index ( value [, start [, stop ]]) → integer -- return first index of value.

Raises ValueError if the value is not present.

Supporting start and stop arguments is optional, but recommended.

insert ( i, item )

S.insert(index, value) – insert value before index

pop ([, index ]) → item -- remove and return item at index (default last).

Raise IndexError if list is empty or index is out of range.

prepare_to_store ()

remove ( item )

S.remove(value) – remove first occurrence of value. Raise ValueError if the value is not present.

reverse ()

S.reverse() – reverse IN PLACE

sort ( *args , **kwds )

SCons.Variables.ListVariable._converter ( val , allowedElems , mapdict ) →_ListVariable

Callback to convert list variables into a suitable form.

The arguments allowedElems and mapdict are non-standard for a Variables converter: the lambda in the ListVariable() function arranges for us to be called correctly.

Incoming values “all” and “none” are recognized and converted into their expanded form.

SCons.Variables.ListVariable._validator ( key , val , env ) → None

Callback to validate supplied value(s) for a ListVariable.

Validation means “is val in the allowed list”? val has been subject to substitution before the validator is called. The converter created a _ListVariable container which is stored in env after it runs; this includes the allowable elements list. Substitution makes a string made out of the values (only), so we need to fish the allowed elements list out of the environment to complete the validation.

Note that since 18b45e456, whether subst has been called is conditional on the value of the subst argument to Add(), so we have to account for possible different types of val .

Raises: UserError – if validation failed.

Added in version 4.8.0: _validator split off from_converter() with an additional check for whether val has been substituted before the call.

# SCons.Variables.PackageVariable module

Variable type for package Variables.

To be used whenever a ‘package’ may be enabled/disabled and the package path may be specified.

Given these options

x11=no (disables X11 support) x11=yes (will search for the package installation dir) x11=/usr/local/X11 (will check this path for existence)

Can be used as a replacement for autoconf’s --with-xxx=yyy

opts = Variables() opts.Add( PackageVariable( key='x11', help='use X11 installed here (yes = search some places)', default='yes' ))env = Environment(variables=opts) if env['x11'] is True: dir = ... # search X11 in some standard places ...

SCons.Variables package

204 env['x11'] = dir if env['x11']: ... # build with x11 ...

SCons.Variables.PackageVariable.PackageVariable ( key: str , help: str , default , searchfunc: Callable | None = None) → tuple [str , str , str , Callable , Callable ]

Return a tuple describing a package list SCons Variable.

The input parameters describe a ‘package list’ variable. Returns a tuple with the correct converter and validator appended. The result is usable as input to Add().

A ‘package list’ variable may be specified as a truthy string from ENABLE_STRINGS, a falsy string from DISABLE_STRINGS, or as a pathname string. This information is appended to help using only one string each for truthy/falsy.

SCons.Variables.PackageVariable._converter ( val: str | bool , default: str ) → str | bool

Convert a package variable.

Returns val if it looks like a path string, and False if it is a disabling string. If val is an enabling string, returns default

unless default is an enabling or disabling string, in which case ignore default and return True .

SCons.Variables.PackageVariable._validator ( key: str , val , env , searchfunc ) → None

Validate package variable for valid path.

Checks that if a path is given as the value, that pathname actually exists.

# SCons.Variables.PathVariable module

Variable type for path Variables.

To be used whenever a user-specified path override setting should be allowed.

Arguments to PathVariable are:

• key - name of this variable on the command line (e.g. “prefix”)

• help - help string for variable

• default - default value for this variable

• validator - [optional] validator for variable value. Predefined are:

• PathAccept - accepts any path setting; no validation

• PathIsDir - path must be an existing directory

• PathIsDirCreate - path must be a dir; will create

• PathIsFile - path must be a file

• PathExists - path must exist (any type) [default] The validator is a function that is called and which should return True or False to indicate if the path is valid. The arguments to the validator function are: ( key , val , env ). key is the name of the variable, val is the path specified for the variable, and env is the environment to which the Variables have been added.

Usage example:

opts = Variables() opts.Add( PathVariable( 'qtdir', help='where the root of Qt is installed', default=qtdir, validator=PathIsDir, ))

SCons.Variables package

205 opts.Add( PathVariable( 'qt_includes', help='where the Qt includes are installed', default='$qtdir/includes', validator=PathIsDirCreate, ))opts.Add( PathVariable( 'qt_libraries', help='where the Qt library is installed', default='$qtdir/lib', ))

class SCons.Variables.PathVariable._PathVariableClass

Bases: object

Class implementing path variables.

This class exists mainly to expose the validators without code having to import the names: they will appear as methods of PathVariable , a statically created instance of this class, which is placed in the SConscript namespace.

Instances are callable to produce a suitable variable tuple.

static PathAccept ( key: str , val , env ) → None

Validate path with no checking.

static PathExists ( key: str , val , env ) → None

Validate path exists.

static PathIsDir ( key: str , val , env ) → None

Validate path is a directory.

static PathIsDirCreate ( key: str , val , env ) → None

Validate path is a directory, creating if needed.

static PathIsFile ( key: str , val , env ) → None

Validate path is a file.

__call__ ( key: str , help: str , default , validator: Callable | None = None) → tuple [str , str , str ,

Callable , None ]

Return a tuple describing a path list SCons Variable.

The input parameters describe a ‘path list’ variable. Returns a tuple with the correct converter and validator appended. The result is usable for input to Add().

The default parameter specifies the default path to use if the user does not specify an override with this variable.

validator is a validator, see this file for examples

# Indices and Tables

• genindex

• modindex

• search

Indices and Tables

206 Index

_

__call__() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.FunctionEvaluator method) (SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method) (SCons.Scanner.Classic method) (SCons.Scanner.ClassicCPP method) (SCons.Scanner.Current method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method) (SCons.Scanner.ScannerBase method) (SCons.Tool.ToolInitializerMethod method) (SCons.Variables.PathVariable._PathVariableClass method)

__clearRepositoryCache() (SCons.Node.FS.Dir method)

__contains__() (SCons.Environment.OverrideEnvironment method)

(SCons.Taskmaster.Job.NewParallel.State class method)

__delitem__() (SCons.Environment.OverrideEnvironment method)

__dmap_cache (SCons.Node.FS.File attribute)

__dmap_sig_cache (SCons.Node.FS.File attribute)

__enter__() (SCons.Util.filelock.FileLock method)

__eq__() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

__exit__() (SCons.Util.filelock.FileLock method)

__get_abspath() (SCons.Node.FS.EntryProxy method)

__get_base_path() (SCons.Node.FS.EntryProxy method)

__get_dir() (SCons.Node.FS.EntryProxy method)

__get_file() (SCons.Node.FS.EntryProxy method)

__get_filebase() (SCons.Node.FS.EntryProxy method)

__get_posix_path() (SCons.Node.FS.EntryProxy method)

__get_relpath() (SCons.Node.FS.EntryProxy method)

__get_rsrcdir() (SCons.Node.FS.EntryProxy method)

__get_rsrcnode() (SCons.Node.FS.EntryProxy method)

__get_srcdir() (SCons.Node.FS.EntryProxy method)

__get_srcnode() (SCons.Node.FS.EntryProxy method)

__get_suffix() (SCons.Node.FS.EntryProxy method)

__get_windows_path() (SCons.Node.FS.EntryProxy method)

__getattr__() (SCons.Builder.CompositeBuilder method)

(SCons.Environment.Base method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Script.SConsOptions.SConsValues method) (SCons.Util.NodeList method) (SCons.Util.Proxy method)

__getitem__() (SCons.Environment.OverrideEnvironment method)

(SCons.Taskmaster.Job.NewParallel.State class method) (SCons.Util.NodeList method)

__getstate__() (SCons.Node.Alias.AliasBuildInfo method)

(SCons.Node.Alias.AliasNodeInfo method) (SCons.Node.BuildInfoBase method) (SCons.Node.FS.DirBuildInfo method) (SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileBuildInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.NodeInfoBase method) (SCons.Node.Python.ValueBuildInfo method) (SCons.Node.Python.ValueNodeInfo method) (SCons.SConf.SConfBuildInfo method)

__iter__() (SCons.Taskmaster.Job.NewParallel.State class method) __len__() (SCons.Taskmaster.Job.NewParallel.State class method)

__lib_either_version_flag() (in module SCons.Defaults)

__libversionflags() (in module SCons.Defaults)

__lt__() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

__make_unique() (SCons.Util.UniqueList method)

__repr__() (SCons.Util.filelock.FileLock method)

__resetDuplicate() (SCons.Node.FS.Dir method)

__setstate__() (SCons.Node.Alias.AliasBuildInfo method)

(SCons.Node.Alias.AliasNodeInfo method) (SCons.Node.BuildInfoBase method) (SCons.Node.FS.DirBuildInfo method) (SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileBuildInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.NodeInfoBase method) (SCons.Node.Python.ValueBuildInfo method) (SCons.Node.Python.ValueNodeInfo method) (SCons.SConf.SConfBuildInfo method)

__str__() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Variables.Variables method)

_abc_impl (SCons.Action._ActionAction attribute)

(SCons.Action.ActionBase attribute) (SCons.Action.CommandAction attribute) (SCons.Action.CommandGeneratorAction attribute) (SCons.Action.FunctionAction attribute) (SCons.Action.LazyAction attribute) (SCons.Action.ListAction attribute) (SCons.Builder.ListEmitter attribute) (SCons.Builder.OverrideWarner attribute) (SCons.Environment.BuilderDict attribute)

(SCons.Executor.TSList attribute)

(SCons.Node.Alias.AliasNameSpace attribute) (SCons.Node.NodeList attribute) (SCons.SConf.SConfBuildTask attribute) (SCons.Script.Main.BuildTask attribute) (SCons.Script.Main.CleanTask attribute) (SCons.Script.Main.QuestionTask attribute) (SCons.Script.TargetList attribute) (SCons.Subst.CmdStringHolder attribute) (SCons.Subst.ListSubber attribute) (SCons.Subst.Targets_or_Sources attribute) (SCons.Taskmaster.AlwaysTask attribute) (SCons.Taskmaster.OutOfDateTask attribute) (SCons.Taskmaster.Task attribute) (SCons.Util.CLVar attribute) (SCons.Util.NodeList attribute) (SCons.Util.stats.CountStats attribute) (SCons.Util.stats.MemStats attribute) (SCons.Util.stats.Stats attribute) (SCons.Util.stats.TimeStats attribute) (SCons.Util.UniqueList attribute) (SCons.Variables.ListVariable._ListVariable attribute)

_abspath (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_ActionAction (class in SCons.Action)

_actionAppend() (in module SCons.Action)

_Add_Arguments() (in module SCons.Script)

_add_child() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

_add_config() (SCons.CacheDir.CacheDir method) _add_cppdefines() (in module SCons.Environment)

_add_Default() (SCons.Script.TargetList method)

_add_help_option() (SCons.Script.SConsOptions.SConsOptionParser method)

_add_strings_to_dependency_map() (SCons.Node.FS.File method)

_Add_Targets() (in module SCons.Script)

_add_version_option() (SCons.Script.SConsOptions.SConsOptionParser method)

_adjust_stack_size() (SCons.Taskmaster.Job.NewParallel method)

_adjustixes() (SCons.Builder.BuilderBase method)

_attempt_get_hash_function() (in module SCons.Util.hashes)

_attempt_init_of_python_3_9_hash_object() (in module SCons.Util.hashes)

_bootstrap() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_bootstrap_inner() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_build_dependency_map() (SCons.Node.FS.File method)

_build_targets() (in module SCons.Script.Main)

_CacheDir (SCons.Executor.NullEnvironment attribute)

_CacheDir_path (SCons.Executor.NullEnvironment attribute)

_callable_contents() (in module SCons.Action)

_canonicalize() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_changed_build() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_changed_content() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_changed_timestamp_match() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_changed_timestamp_newer() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_changed_timestamp_then_content() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_check_action() (SCons.Script.SConsOptions.SConsOption method)

_check_callback() (SCons.Script.SConsOptions.SConsOption method)

_check_choice() (SCons.Script.SConsOptions.SConsOption method)

_check_conflict() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

_check_const() (SCons.Script.SConsOptions.SConsOption method)

_check_dest() (SCons.Script.SConsOptions.SConsOption method)

_check_empty_program() (in module SCons.Conftest)

_check_nargs() (SCons.Script.SConsOptions.SConsOption method)

_check_nargs_optional() (SCons.Script.SConsOptions.SConsOption method)

_check_opt_strings() (SCons.Script.SConsOptions.SConsOption method)

_check_type() (SCons.Script.SConsOptions.SConsOption method)

_check_writable() (SCons.dblite._Dblite method)

_children_get() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

_children_reset() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

_classEntry (in module SCons.Node.FS)

_clean_targets() (SCons.Script.Main.CleanTask method)

_clear() (SCons.Script.TargetList method)

_code_contents() (in module SCons.Action)

_collect_classes() (in module SCons.Scanner.Java)

_concat() (in module SCons.Defaults)

_concat_ixes() (in module SCons.Defaults)

_converter() (in module SCons.Variables.ListVariable)

(in module SCons.Variables.PackageVariable)

_copy_func() (in module SCons.Node.FS)

_create() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

_create_nodelist() (SCons.Subst.NLWrapper method)

_create_nodes() (SCons.Builder.BuilderBase method)

_create_option_list() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

_create_option_mappings() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

_create_path() (in module SCons.Script.Main)

_createConfigH() (in module SCons.SConf)

_createDir() (SCons.Node.FS.File method)

(SCons.SConf.SConfBase method)

_createSource() (in module SCons.SConf)

_Dblite (class in SCons.dblite)

_defines() (in module SCons.Defaults)

_del_SCANNERS() (in module SCons.Environment)

_delete() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_delete_duplicates() (in module SCons.Environment)

_do_add() (SCons.Variables.Variables method)

_do_create_action() (in module SCons.Action)

_do_create_keywords() (in module SCons.Action)

_do_create_list_action() (in module SCons.Action)

_do_execute (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

_do_if_else_condition() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

_do_nothing() (SCons.Script.TargetList method)

_do_one_help() (SCons.Script.Interactive.SConsInteractiveCmd method)

_doc_to_help() (SCons.Script.Interactive.SConsInteractiveCmd method)

_dump_one_caller() (in module SCons.Debug)

_enable_virtualenv_default() (in module SCons.Platform.virtualenv)

_exception_raise() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

_exec_main() (in module SCons.Script.Main)

_execute() (SCons.Builder.BuilderBase method)

_execute_str (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

_exercise() (in module SCons.dblite)

_fetch_DefaultEnvironment() (in module SCons.Defaults)

_find_file_key() (SCons.Node.FS.FileFinder method)_find_next_ready_node() (SCons.Taskmaster.Taskmaster method)

_find_toolpath_dir() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_format_text() (SCons.Script.SConsOptions.SConsInden tedHelpFormatter method)

_func_exists (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_func_get_contents (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_func_is_derived (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_func_rexists (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_func_sconsign (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_func_target_from_source (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_function_contents() (in module SCons.Action)

_gen_nodelist() (SCons.Subst.NLWrapper method)

_generate() (SCons.Action.CommandGeneratorAction method)

(SCons.Action.LazyAction method)

_generate_cache() (SCons.Action.LazyAction method)

_get_all_options() (SCons.Script.SConsOptions.SConsOptionParser method)

_get_args() (SCons.Script.SConsOptions.SConsOptionParser method)

_get_changed_sources() (SCons.Executor.Executor method)

_get_changed_targets() (SCons.Executor.Executor method)

_get_changes() (SCons.Executor.Executor method)

_Get_Default_Targets() (in module SCons.Script)

_get_files_to_clean() (SCons.Script.Main.CleanTask method)

_get_found_includes_key() (SCons.Node.FS.File method)

_get_hash_object() (in module SCons.Util.hashes)

_get_implicit_deps_heavyweight() (SCons.Action.CommandAction method)

(SCons.Action.LazyAction method)

_get_implicit_deps_lightweight() (SCons.Action.CommandAction method)

(SCons.Action.LazyAction method) _get_major_minor_revision() (SCons.Script.SConscript.SConsEnvironment static method)

_get_previous_signatures() (SCons.Node.FS.File method)

_get_scanner() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

_get_SConscript_filenames() (SCons.Script.SConscript.SConsEnvironment method)

_get_sdict() (SCons.Builder.BuilderBase method)

_get_source() (SCons.Executor.Executor method)

_get_sources() (SCons.Executor.Executor method)

_get_src_builders_key() (SCons.Builder.BuilderBase method)

_get_str() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

_get_target() (SCons.Executor.Executor method)

_get_targets() (SCons.Executor.Executor method)

_get_unchanged_sources() (SCons.Executor.Executor method)

_get_unchanged_targets() (SCons.Executor.Executor method)

_get_unignored_sources_key() (SCons.Executor.Executor method)

_glob1() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

_gsm() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_hardlink_func() (in module SCons.Node.FS)

_Have() (in module SCons.Conftest)

_ignore_virtualenv_default() (in module SCons.Platform.virtualenv)

_init_parsing_state() (SCons.Script.SConsOptions.SConsOptionParser method)

_init_special() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_initialized (SCons.Taskmaster.Job.NewParallel.Worker attribute)

(SCons.Taskmaster.Job.Worker attribute)

_inject_venv_path() (in module SCons.Platform.virtualenv)

_inject_venv_variables() (in module SCons.Platform.virtualenv)

_instance (SCons.Subst.NullNodeList attribute)

_is_path_in() (in module SCons.Platform.virtualenv)

_is_process_alive() (in module SCons.Util)

_labspath (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_lang2suffix() (in module SCons.Conftest)

_latex_names() (SCons.Scanner.LaTeX.LaTeX method)

_ListVariable (class in SCons.Variables.ListVariable)

_load_all_site_scons_dirs() (in module SCons.Script.Main)

_load_site_scons_dir() (in module SCons.Script.Main)

_local (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_LogFailed() (in module SCons.Conftest)

_lookup() (SCons.Node.FS.FS method)

_lookup_abs() (SCons.Node.FS.RootDir method) _lookupDict (SCons.Node.FS.RootDir attribute)

_main() (in module SCons.Script.Main)

_match_long_opt() (SCons.Script.SConsOptions.SConsOptionParser method)

_match_tuples() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

_maybe_start_worker() (SCons.Taskmaster.Job.NewParallel method)

_memo (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute) (SCons.Node.Alias.Alias attribute) (SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_mkdir_atomic() (SCons.CacheDir.CacheDir method)

_morph() (SCons.Executor.Null method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

_my_normcase() (in module SCons.Node.FS)

_no_exception_to_raise() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

_node_errors() (in module SCons.Builder)

_NoError

_null (class in SCons.Action)

_Null (class in SCons.Builder)

(class in SCons.Environment) (class in SCons.Node.FS) (class in SCons.Scanner) (class in SCons.Scanner.LaTeX)

_null (in module SCons.Builder)

(in module SCons.Environment) (in module SCons.Scanner) (in module SCons.Scanner.LaTeX)

_object_contents() (in module SCons.Action)

_object_instance_content() (in module SCons.Action)

_open() (SCons.dblite._Dblite static method)

_os_chmod() (SCons.dblite._Dblite static method)

_os_chown() (SCons.dblite._Dblite static method)

_os_replace() (SCons.dblite._Dblite static method)

_parse_tuples() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

_path (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_path_elements (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_PathList (class in SCons.PathList)

_PathVariableClass (class in SCons.Variables.PathVariable)

_pickle_dump() (SCons.dblite._Dblite static method)

_pickle_protocol (SCons.dblite._Dblite attribute)

_populate_option_list() (SCons.Script.SConsOptions.SConsOptionParser method)

_print_cmd_str() (SCons.Platform.TempFileMunge method)_process_args() (SCons.Script.SConsOptions.SConsOptionParser method)

_process_long_opt() (SCons.Script.SConsOptions.SConsOptionParser method)

_process_short_opts() (SCons.Script.SConsOptions.SConsOptionParser method)

_process_tuples() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

_proxy (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_readconfig() (SCons.CacheDir.CacheDir method)

_recurse_all_nodes() (SCons.Scanner.Classic static method)

(SCons.Scanner.ClassicCPP static method) (SCons.Scanner.Current static method) (SCons.Scanner.D.D static method) (SCons.Scanner.Fortran.F90Scanner static method) (SCons.Scanner.LaTeX.LaTeX static method) (SCons.Scanner.ScannerBase static method) (SCons.Scanner.Selector static method)

_recurse_no_nodes() (SCons.Scanner.Classic static method)

(SCons.Scanner.ClassicCPP static method) (SCons.Scanner.Current static method) (SCons.Scanner.D.D static method) (SCons.Scanner.Fortran.F90Scanner static method) (SCons.Scanner.LaTeX.LaTeX static method) (SCons.Scanner.ScannerBase static method) (SCons.Scanner.Selector static method)

_rel_path_key() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

_Remove_Argument() (in module SCons.Script)

_remove_list() (in module SCons.Subst)

_Remove_Target() (in module SCons.Script)

_reset_internal_locks() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_reset_sig_handler() (SCons.Taskmaster.Job.Jobs method)

_resolve_shell_env() (in module SCons.Action)

_restore_stack_size() (SCons.Taskmaster.Job.NewParallel method)

_return_nodelist() (SCons.Subst.NLWrapper method)

_Rfindalldirs_key() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

_rm_list() (in module SCons.Subst)

_rmv_existing() (SCons.Node.FS.File method)

_run_exitfuncs() (in module SCons.exitfuncs)

_running_in_virtualenv() (in module SCons.Platform.virtualenv)

_save_str() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

_scons_internal_error() (in module SCons.Script.Main)

_scons_internal_warning() (in module SCons.Script.Main)

_scons_syntax_error() (in module SCons.Script.Main)

_scons_user_error() (in module SCons.Script.Main)

_scons_user_warning() (in module SCons.Script.Main)

_SConscript() (in module SCons.Script.SConscript)

_sconsign (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_SConstruct_exists() (in module SCons.Script.Main)

_semi_deepcopy_list() (in module SCons.Util)

_semi_deepcopy_tuple() (in module SCons.Util)_set_allowed_viable_default_hashes() (in module SCons.Util.hashes)

_set_attrs() (SCons.Script.SConsOptions.SConsOption method)

_set_BUILDERS() (in module SCons.Environment)

_set_conftest_node() (in module SCons.SConf)

_set_debug_values() (in module SCons.Script.Main)

_Set_Default_Targets() (in module SCons.Script)

_Set_Default_Targets_Has_Been_Called() (in module SCons.Script)

_Set_Default_Targets_Has_Not_Been_Called() (in module SCons.Script)

_set_future_reserved() (in module SCons.Environment)

_set_ident() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_set_native_id() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_set_opt_strings() (SCons.Script.SConsOptions.SConsOption method)

_set_reserved() (in module SCons.Environment)

_set_SCANNERS() (in module SCons.Environment)

_set_tstate_lock() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_setup_logging() (SCons.Taskmaster.Job.NewParallel method)

_setup_sig_handler() (SCons.Taskmaster.Job.Jobs method)

_share_option_mappings() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

_show_md5_warning() (in module SCons.Util.hashes)

_shutdown() (SCons.SConf.SConfBase method)

_shutil_copyfile() (SCons.dblite._Dblite static method)

_softlink_func() (in module SCons.Node.FS)

_specific_sources (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute)

(SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_srcdir_find_file_key() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

_start_worker() (SCons.Taskmaster.Job.NewParallel method)

_startup() (SCons.SConf.SConfBase method)

_stop() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_string_from_cmd_list() (in module SCons.Action)

_stringConfigH() (in module SCons.SConf)

_stringSource() (in module SCons.SConf)

_strip_initial_spaces() (SCons.Script.Interactive.SConsInteractiveCmd method)

_stripixes() (in module SCons.Defaults)

_subproc() (in module SCons.Action)

_subst_libs() (in module SCons.Scanner.Prog)

_subst_paths() (in module SCons.Scanner.Java)

_subst_src_suffixes_key() (SCons.Builder.BuilderBase method)

_tags (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

_text2bool() (in module SCons.Variables.BoolVariable)

_time_time() (SCons.dblite._Dblite static method)

_tool_module() (SCons.Tool.Tool method)

_tpath (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

_update() (SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Script.SConsOptions.SConsValues method)

_update_careful() (SCons.Script.SConsOptions.SConsValues method)

_update_loose() (SCons.Script.SConsOptions.SConsValues method)

_update_onlynew() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

_validate_pending_children() (SCons.Taskmaster.Taskmaster method)

_validator() (in module SCons.Variables.BoolVariable)

(in module SCons.Variables.EnumVariable) (in module SCons.Variables.ListVariable) (in module SCons.Variables.PackageVariable)

_wait_for_process_to_die_non_psutil() (in module SCons.Util)

_wait_for_tstate_lock() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

_work() (SCons.Taskmaster.Job.NewParallel method)

_YesNoResult() (in module SCons.Conftest)

A

abspath (SCons.Node.FS.RootDir attribute)

acquire_lock() (SCons.Util.filelock.FileLock method)

Action() (in module SCons.Action)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

action_list (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

ActionBase (class in SCons.Action)

ActionCaller (class in SCons.Action)

ActionFactory (class in SCons.Action)

ACTIONS (SCons.Script.SConsOptions.SConsOption attribute)

Add() (SCons.Variables.Variables method)

add_action() (SCons.Builder.CompositeBuilder method)

(SCons.Builder.DictCmdGenerator method)

add_batch() (SCons.Executor.Executor method)

add_command() (SCons.Util.stats.TimeStats method)

add_dependency() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_emitter() (SCons.Builder.BuilderBase method)

add_ignore() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_local_option() (SCons.Script.Main.FakeOptionParser method)

(SCons.Script.SConsOptions.SConsOptionParser method)

add_new_word() (SCons.Subst.ListSubber method)

add_note() (SCons.Node.FS.EntryProxyAttributeError method)

(SCons.Node.FS.FileBuildInfoFileToCsigMappingEr ror method) (SCons.SConf.ConfigureCacheError method) (SCons.SConf.ConfigureDryRunError method) (SCons.SConf.SConfError method) (SCons.SConf.SConfWarning method) (SCons.Script.Main.SConsPrintHelpException method) (SCons.Script.SConscript.SConscriptReturn method) (SCons.Script.SConsOptions.SConsBadOptionError method) (SCons.Util._NoError method) (SCons.Util.filelock.SConsLockFailure method) add_option() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

add_option_group() (SCons.Script.SConsOptions.SConsOptionParser method)

add_options() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

add_post_action() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

add_pre_action() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

add_prerequisite() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_scanner() (SCons.Scanner.Classic method)

(SCons.Scanner.ClassicCPP method) (SCons.Scanner.Current method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method) (SCons.Scanner.ScannerBase method) (SCons.Scanner.Selector method)

add_skey() (SCons.Scanner.Classic method)

(SCons.Scanner.ClassicCPP method) (SCons.Scanner.Current method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method) (SCons.Scanner.ScannerBase method) (SCons.Scanner.Selector method)

add_source() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_sources() (SCons.Executor.Executor method)

add_src_builder() (SCons.Builder.BuilderBase method)

add_stat_type() (in module SCons.Util.stats)

add_to_current_word() (SCons.Subst.ListSubber method)

add_to_implicit() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_to_waiting_parents() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_to_waiting_s_e() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

add_wkid() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

AddBatchExecutor() (in module SCons.Executor)

addEntity() (bin.SConsDoc.DoctypeDeclaration method)

AddMethod() (in module SCons.Util.envs)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

AddOption() (in module SCons.Script.Main)

AddPathIfNotExists() (in module SCons.Util.envs)

AddPostAction() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

AddPreAction() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

addRepository() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

AddTest() (SCons.SConf.SConfBase method)

AddTests() (SCons.SConf.SConfBase method)

AddVariables() (SCons.Variables.Variables method)

adjust_suffix() (SCons.Builder.BuilderBase method)

adjustixes() (in module SCons.Util)

Alias (class in SCons.Node.Alias)

Alias() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Script.SConscript.SConsEnvironment method)

Alias.Attrs (class in SCons.Node.Alias)

alias_builder() (in module SCons.Environment)

AliasBuildInfo (class in SCons.Node.Alias)

aliases (SCons.Variables.Variable attribute)

aliasfmt (SCons.Variables.Variables attribute)

AliasNameSpace (class in SCons.Node.Alias)

AliasNodeInfo (class in SCons.Node.Alias)

all_children() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

all_include() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

alter_targets() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

always_build (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

ALWAYS_TYPED_ACTIONS (SCons.Script.SConsOptions.SConsOption attribute)

AlwaysBuild() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

AlwaysTask (class in SCons.Taskmaster)

Annotate() (in module SCons.Node) annotate() (in module SCons.Script.SConscript)

append() (bin.SConsDoc.Arguments method)

(SCons.Builder.ListEmitter method)

Append() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method)

append() (SCons.Executor.TSList method)

(SCons.Node.NodeList method)

Append() (SCons.Script.SConscript.SConsEnvironment method)

append() (SCons.Script.TargetList method)

(SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

appendCvLink() (bin.SConsDoc.TreeFactory static method)

AppendENVPath() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

AppendLIBS() (SCons.SConf.CheckContext method)

appendNode() (bin.SConsDoc.TreeFactory static method)

AppendPath() (in module SCons.Util.envs)

AppendUnique() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

apply_tools() (in module SCons.Environment)

(SCons.Tool.ToolInitializer method)

ArchDefinition (class in SCons.Platform.win32)

arg2nodes() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

args (SCons.Node.FS.EntryProxyAttributeError attribute)

(SCons.Node.FS.FileBuildInfoFileToCsigMappingEr ror attribute) (SCons.SConf.ConfigureCacheError attribute) (SCons.SConf.ConfigureDryRunError attribute) (SCons.SConf.SConfError attribute) (SCons.SConf.SConfWarning attribute) (SCons.Script.Main.SConsPrintHelpException attribute) (SCons.Script.SConscript.SConscriptReturn attribute) (SCons.Script.SConsOptions.SConsBadOptionError attribute) (SCons.Util._NoError attribute) (SCons.Util.filelock.SConsLockFailure attribute)

Arguments (class in bin.SConsDoc)

attributes (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

ATTRS (SCons.Script.SConsOptions.SConsOption attribute)

B

backtick() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

bact (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

bactsig (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

Base (class in SCons.Environment)

(class in SCons.Node.FS) (class in SCons.SConsign) (in module SCons.Scanner)

Base.Attrs (class in SCons.Node.FS)

Batch (class in SCons.Executor)

batch_key() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

batches (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

bdepends (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

bdependsigs (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

bimplicit (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

bimplicitsigs (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute)

(SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

bin.SConsDoc

module

bin.SConsExamples

module

binfo (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute) (SCons.SConsign.SConsignEntry attribute)

BoolVariable() (in module SCons.Variables)

(in module SCons.Variables.BoolVariable)

bsources (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

bsourcesigs (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.SConf.SConfBuildInfo attribute)

build() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

BuildDefaultGlobals() (in module SCons.Script.SConscript) Builder (class in bin.SConsDoc)

builder (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Builder() (in module SCons.Builder)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

builder_kw (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

builder_set() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

BuilderBase (class in SCons.Builder)

BuilderDict (class in SCons.Environment)

BuildError

BuilderWrapper (class in SCons.Environment)

BuildInfo (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

BuildInfoBase (class in SCons.Node)

BuildNodes() (SCons.SConf.SConfBase method)

BuildProg() (SCons.SConf.CheckContext method)

BuildTask (class in SCons.Script.Main)

built() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

C

CacheCleanupErrorWarning

cached (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

CacheDebug() (SCons.CacheDir.CacheDir method)

CacheDir (class in SCons.CacheDir)

CacheDir() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

cachedir_csig (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

cachepath() (SCons.CacheDir.CacheDir method)

CachePushFunc() (in module SCons.CacheDir)

CacheRetrieveFunc() (in module SCons.CacheDir)

CacheRetrieveString() (in module SCons.CacheDir)

cachesig (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

CacheVersionWarning

CacheWriteErrorWarning CallableSelector (class in SCons.Builder)

caller_stack() (in module SCons.Debug)

caller_trace() (in module SCons.Debug)

canonical_text() (SCons.Scanner.LaTeX.LaTeX method)

capitalize() (SCons.Subst.CmdStringHolder method)

case_sensitive_suffixes() (in module SCons.Util)

casefold() (SCons.Subst.CmdStringHolder method)

CConditionalScanner() (in module SCons.Scanner.C)

center() (SCons.Subst.CmdStringHolder method)

changed() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

changed_content() (SCons.Node.FS.File method)

changed_since_last_build (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

changed_since_last_build_alias() (in module SCons.Node)

changed_since_last_build_entry() (in module SCons.Node)

changed_since_last_build_node() (in module SCons.Node)

changed_since_last_build_python() (in module SCons.Node)

changed_since_last_build_state_changed() (in module SCons.Node)

changed_state() (SCons.Node.FS.File method)

changed_timestamp_match() (SCons.Node.FS.File method)

changed_timestamp_newer() (SCons.Node.FS.File method)

changed_timestamp_then_content() (SCons.Node.FS.File method)

chdir() (SCons.Node.FS.FS method)

check_attributes() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

CHECK_METHODS (SCons.Script.SConsOptions.SConsOption attribute)

check_value() (SCons.Script.SConsOptions.SConsOption method)

check_values() (SCons.Script.SConsOptions.SConsOptionParser method)

CheckBuilder() (in module SCons.Conftest)

CheckCC() (in module SCons.Conftest)

(in module SCons.SConf)

CheckCHeader() (in module SCons.SConf)

CheckContext (class in SCons.SConf)

CheckCXX() (in module SCons.Conftest)

(in module SCons.SConf)

CheckCXXHeader() (in module SCons.SConf)

CheckDeclaration() (in module SCons.Conftest)

(in module SCons.SConf)

CheckFunc() (in module SCons.Conftest)

(in module SCons.SConf)

CheckHeader() (in module SCons.Conftest)

(in module SCons.SConf)

CheckLib() (in module SCons.Conftest)

(in module SCons.SConf)

CheckLibWithHeader() (in module SCons.SConf)

CheckMember() (in module SCons.Conftest)

(in module SCons.SConf)

CheckProg() (in module SCons.Conftest)

(in module SCons.SConf)

CheckSHCC() (in module SCons.Conftest)

(in module SCons.SConf) CheckSHCXX() (in module SCons.Conftest)

(in module SCons.SConf)

CheckType() (in module SCons.Conftest)

(in module SCons.SConf)

CheckTypeSize() (in module SCons.Conftest)

(in module SCons.SConf)

children() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

children_are_up_to_date() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

chmod() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

chmod_func() (in module SCons.Defaults)

chmod_strfunc() (in module SCons.Defaults)

Classic (class in SCons.Scanner)

ClassicCPP (class in SCons.Scanner)

classname() (in module SCons.Node)

Clean() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

CleanTask (class in SCons.Script.Main)

cleanup() (SCons.Executor.Executor method)

(SCons.Executor.Null method) (SCons.Taskmaster.Job.ThreadPool method) (SCons.Taskmaster.Taskmaster method)

Cleanup_CPP_Expressions() (in module SCons.cpp)

clear() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.ListEmitter method) (SCons.Builder.OverrideWarner method) (SCons.Environment.BuilderDict method) (SCons.Executor.TSList method) (SCons.Node.Alias.Alias method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.NodeList method) (SCons.Node.Python.Value method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.Selector method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

clear_memoized_values() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

Clone() (SCons.Environment.Base method)

clone() (SCons.Environment.BuilderWrapper method)

Clone() (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

clone() (SCons.Util.envs.MethodWrapper method)

close() (SCons.dblite._Dblite method)

close_strip() (SCons.Subst.ListSubber method)

CLVar (class in SCons.Util)

cmdloop() (SCons.Script.Interactive.SConsInteractiveCmd method)

CmdStringHolder (class in SCons.Subst)

cmp() (in module SCons.Util)

cmp_name() (bin.SConsDoc.Builder method)

(bin.SConsDoc.ConstructionVariable method) (bin.SConsDoc.Function method) (bin.SConsDoc.Item method) (bin.SConsDoc.Tool method)

collect_node_states() (SCons.SConf.SConfBuildTask method)

collectSConsExampleNames() (in module bin.SConsExamples)

columnize() (SCons.Script.Interactive.SConsInteractiveCmd method)

Command() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

command_edit() (in module bin.SConsExamples)

command_ls() (in module bin.SConsExamples)

command_scons() (in module bin.SConsExamples)

command_sleep() (in module bin.SConsExamples)

command_touch() (in module bin.SConsExamples)

CommandAction (class in SCons.Action)

CommandGeneratorAction (class in SCons.Action)

CompileProg() (SCons.SConf.CheckContext method)

CompileSharedObject() (SCons.SConf.CheckContext method)

complete() (SCons.Script.Interactive.SConsInteractiveCmd method)

complete_help() (SCons.Script.Interactive.SConsInteractiveCmd method)

COMPLETED (SCons.Taskmaster.Job.NewParallel.State attribute)

completedefault() (SCons.Script.Interactive.SConsInteractiveCmd method)

completenames() (SCons.Script.Interactive.SConsInteractiveCmd method)

CompositeBuilder (class in SCons.Builder)

compute_exports() (in module SCons.Script.SConscript)

Configure() (in module SCons.Script.SConscript)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

configure_trace() (SCons.Taskmaster.Taskmaster method)

ConfigureCacheError

ConfigureDryRunError

CONST_ACTIONS (SCons.Script.SConsOptions.SConsOption attribute)

ConstructionVariable (class in bin.SConsDoc)

containsAll() (in module SCons.Util)

containsAny() (in module SCons.Util)

containsOnly() (in module SCons.Util)

contentsig (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

convert() (SCons.Node.Alias.Alias method)

(SCons.Node.Alias.AliasNodeInfo method) (SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.NodeInfoBase method) (SCons.Node.Python.ValueNodeInfo method)

convert_copy_attrs (SCons.Node.FS.File attribute)

convert_from_sconsign() (SCons.Node.FS.FileBuildInfo method)

(SCons.SConf.SConfBuildInfo method) (SCons.SConsign.SConsignEntry method)

convert_old_entry() (SCons.Node.FS.File method)

convert_sig_attrs (SCons.Node.FS.File attribute)

convert_to_BuildError() (in module SCons.Errors)

convert_to_sconsign() (SCons.Node.FS.FileBuildInfo method)

(SCons.SConf.SConfBuildInfo method) (SCons.SConsign.SConsignEntry method) convert_value() (SCons.Script.SConsOptions.SConsOption method)

convertElementTree() (bin.SConsDoc.TreeFactory static method)

converter (SCons.Variables.Variable attribute)

converter() (SCons.Util.DispatchingFormatter method)

copy() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.ListEmitter method) (SCons.Builder.OverrideWarner method) (SCons.Environment.BuilderDict method) (SCons.Executor.TSList method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.Selector method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

copy2() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

copy_from_cache() (SCons.CacheDir.CacheDir class method)

copy_func() (in module SCons.Defaults)

copy_non_reserved_keywords() (in module SCons.Environment)

copy_strfunc() (in module SCons.Defaults)

copy_to_cache() (SCons.CacheDir.CacheDir class method)

copyNode() (bin.SConsDoc.TreeFactory static method)

corrupt_dblite_warning() (in module SCons.SConsign)

CorruptSConsignWarning

count (SCons.Script.Main.Progressor attribute)

count() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Memoize.CountDict method) (SCons.Memoize.CountValue method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.CmdStringHolder method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

CountDict (class in SCons.Memoize)

CountDictCall() (in module SCons.Memoize)

Counter (class in SCons.Memoize)

countLoggedInstances() (in module SCons.Debug)

CountMethodCall() (in module SCons.Memoize)

CountStats (class in SCons.Util.stats)

CountValue (class in SCons.Memoize)

CPP_to_Python() (in module SCons.cpp)

CPP_to_Python_Ops_Sub() (in module SCons.cpp)

create_scons_output() (in module bin.SConsExamples)

createAllExampleOutputs() (in module bin.SConsExamples)

createCFileBuilders() (in module SCons.Tool)

CreateConfigHBuilder() (in module SCons.SConf)

createDoctype() (bin.SConsDoc.DoctypeDeclaration method)

createIncludesFromHeaders() (in module SCons.SConf)

CreateJarBuilder() (in module SCons.Tool)

CreateJavaClassDirBuilder() (in module SCons.Tool)

CreateJavaClassFileBuilder() (in module SCons.Tool)

CreateJavaFileBuilder() (in module SCons.Tool)

CreateJavaHBuilder() (in module SCons.Tool)

createLoadableModuleBuilder() (in module SCons.Tool)

createObjBuilders() (in module SCons.Tool)

createProgBuilder() (in module SCons.Tool)

createSharedLibBuilder() (in module SCons.Tool)

createStaticLibBuilder() (in module SCons.Tool) CScanner() (in module SCons.Scanner.C)

csig (SCons.Node.Alias.AliasNodeInfo attribute)

(SCons.Node.FS.FileNodeInfo attribute) (SCons.Node.Python.ValueNodeInfo attribute)

Current (class in SCons.Scanner)

current_sconsign_filename() (in module SCons.SConsign)

current_version_id (SCons.Node.Alias.AliasBuildInfo attribute)

(SCons.Node.Alias.AliasNodeInfo attribute) (SCons.Node.BuildInfoBase attribute) (SCons.Node.FS.DirBuildInfo attribute) (SCons.Node.FS.DirNodeInfo attribute) (SCons.Node.FS.FileBuildInfo attribute) (SCons.Node.FS.FileNodeInfo attribute) (SCons.Node.NodeInfoBase attribute) (SCons.Node.Python.ValueBuildInfo attribute) (SCons.Node.Python.ValueNodeInfo attribute) (SCons.SConf.SConfBuildInfo attribute) (SCons.SConsign.SConsignEntry attribute)

cwd (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

D

D (class in SCons.Scanner.D)

daemon (SCons.Taskmaster.Job.NewParallel.Worker property)

(SCons.Taskmaster.Job.Worker property)

DB (class in SCons.SConsign)

DebugOptions() (in module SCons.Script.Main)

decide_source() (in module SCons.Node)

decide_target() (in module SCons.Node)

Decider() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method)

(SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.Script.SConscript.SConsEnvironment method)

decorateWithHeader() (bin.SConsDoc.TreeFactory static method)

dedent() (SCons.Script.SConsOptions.SConsIndentedH elpFormatter method)

default (SCons.Variables.Variable attribute)

default() (SCons.Script.Interactive.SConsInteractiveCmd method)

Default() (SCons.Script.SConscript.SConsEnvironment method)

default_copy_from_cache() (in module SCons.Environment)

default_copy_to_cache() (in module SCons.Environment)

default_decide_source() (in module SCons.Environment)

default_decide_target() (in module SCons.Environment)

default_exitstatfunc() (in module SCons.Action)

default_msec_format (SCons.Util.DispatchingFormatter attribute)

default_time_format (SCons.Util.DispatchingFormatter attribute)

DefaultEnvironment() (in module SCons.Defaults)

DefaultEnvironmentCall (class in SCons.Script.SConscript)

DefaultToolList() (in module SCons.Platform)

Define() (SCons.SConf.SConfBase method)

del_binfo() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

Delegate (class in SCons.Util)

delete_func() (in module SCons.Defaults)

delete_strfunc() (in module SCons.Defaults) dependency_map (SCons.Node.FS.FileBuildInfo attribute)

(SCons.SConf.SConfBuildInfo attribute)

DependencyWarning

depends (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Depends() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

depends_set (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

DeprecatedDebugOptionsWarning

DeprecatedOptionsWarning

DeprecatedWarning

destroy() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

Detect() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

DevelopmentVersionWarning

DictCmdGenerator (class in SCons.Builder)

DictEmitter (class in SCons.Builder)

dictify() (in module SCons.Util)

dictify_CPPDEFINES() (in module SCons.Scanner.C)

Dictionary() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

dictSpecialAttrs (SCons.Node.FS.EntryProxy attribute)

Dir (class in SCons.Node.FS)

(class in SCons.SConsign)

dir (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

Dir() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.FS.Dir method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.RootDir method) (SCons.Script.SConscript.SConsEnvironment method)

Dir.Attrs (class in SCons.Node.FS)

dir_on_disk() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

DirBuildInfo (class in SCons.Node.FS)

DirEntryScanner() (in module SCons.Scanner.Dir)

DirFile (class in SCons.SConsign)

dirname (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

DirNodeInfo (class in SCons.Node.FS)

Dirs() (SCons.Node.FS.File method)

DirScanner() (in module SCons.Scanner.Dir)

disable_interspersed_args() (SCons.Script.SConsOptions.SConsOptionParser method)

disambiguate() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

diskcheck_convert() (in module SCons.Script.SConsOptions)

diskcheck_match() (SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

diskcheck_types() (in module SCons.Node.FS)

DiskChecker (class in SCons.Node.FS)

DispatchingFormatter (class in SCons.Util)

display() (SCons.Memoize.CountDict method)

(SCons.Memoize.Counter method) (SCons.Memoize.CountValue method)

Display() (SCons.SConf.CheckContext method)

display() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Script.Main.TreePrinter method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

display_cached_string() (SCons.SConf.SConfBuildTask method)

DisplayEngine (class in SCons.Util)

do_append() (SCons.Util.stats.CountStats method)

(SCons.Util.stats.MemStats method) (SCons.Util.stats.Stats method) (SCons.Util.stats.TimeStats method)

do_build() (SCons.Script.Interactive.SConsInteractiveCmd method)

do_clean() (SCons.Script.Interactive.SConsInteractiveCmd method)

do_define() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_diskcheck_match() (in module SCons.Node.FS)

do_duplicate() (SCons.Node.FS.Dir method)

(SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

do_elif() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_else() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_endif() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_EOF() (SCons.Script.Interactive.SConsInteractiveCmd method)

do_exit() (SCons.Script.Interactive.SConsInteractiveCmd method)

do_failed() (SCons.Script.Main.BuildTask method)

do_flatten() (in module SCons.Util)

do_help() (SCons.Script.Interactive.SConsInteractiveCmd method)

do_if() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_ifdef() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_ifndef() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method) do_import() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_include() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_include_next() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_not_scan() (in module SCons.Scanner.Dir)

do_not_set_entry() (SCons.SConsign.Base method)

(SCons.SConsign.DB method) (SCons.SConsign.Dir method) (SCons.SConsign.DirFile method)

do_not_store_info() (SCons.SConsign.Base method)

(SCons.SConsign.DB method) (SCons.SConsign.Dir method) (SCons.SConsign.DirFile method)

do_nothing() (in module SCons.Node)

(SCons.cpp.DumbPreProcessor method) (SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method) (SCons.Util.stats.CountStats method) (SCons.Util.stats.MemStats method) (SCons.Util.stats.Stats method) (SCons.Util.stats.TimeStats method)

do_nothing_node() (in module SCons.Node)

do_print() (SCons.Util.stats.CountStats method)

(SCons.Util.stats.MemStats method) (SCons.Util.stats.Stats method) (SCons.Util.stats.TimeStats method)

do_shell() (SCons.Script.Interactive.SConsInteractiveCmd method)

do_subst (SCons.Variables.Variable attribute)

do_undef() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

do_version() (SCons.Script.Interactive.SConsInteractiveCmd method)

doc_header (SCons.Script.Interactive.SConsInteractiveCmd attribute)

doc_leader (SCons.Script.Interactive.SConsInteractiveCmd attribute)

DoctypeDeclaration (class in bin.SConsDoc)

DoctypeEntity (class in bin.SConsDoc)

DScanner() (in module SCons.Scanner.D)

DumbPreProcessor (class in SCons.cpp)

Dump() (in module SCons.Memoize)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

dump_caller_counts() (in module SCons.Debug)

dump_stats() (in module SCons.Taskmaster)

dumpLoggedInstances() (in module SCons.Debug)

duplicate (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

DuplicateEnvironmentWarning

E

EmitterProxy (class in SCons.Builder)

emptyline() (SCons.Script.Interactive.SConsInteractiveCmd method)

enable() (SCons.Node.FS.DiskChecker method)

(SCons.Util.stats.CountStats method) (SCons.Util.stats.MemStats method)

(SCons.Util.stats.Stats method) (SCons.Util.stats.TimeStats method)

enable_interspersed_args() (SCons.Script.SConsOptions.SConsOptionParser method)

EnableMemoization() (in module SCons.Memoize)

enableWarningClass() (in module SCons.Warnings)

encode() (SCons.Subst.CmdStringHolder method)

endswith() (SCons.Subst.CmdStringHolder method)

ensure_value() (SCons.Script.SConsOptions.SConsValues method)

ensureExampleOutputsExist() (in module bin.SConsExamples)

EnsurePythonVersion() (SCons.Script.SConscript.SConsEnvironment static method)

EnsureSConsVersion() (SCons.Script.SConscript.SConsEnvironment static method)

entries (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

Entry (class in SCons.Node.FS)

Entry() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.FS.Dir method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.RootDir method) (SCons.Script.SConscript.SConsEnvironment method)

Entry.Attrs (class in SCons.Node.FS)

entry_abspath() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

entry_exists_on_disk() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

entry_labspath() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

entry_path() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

entry_tpath() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

EntryProxy (class in SCons.Node.FS)

EntryProxyAttributeError

EnumVariable() (in module SCons.Variables)

(in module SCons.Variables.EnumVariable)

env (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute) (SCons.Node.Alias.Alias attribute) (SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

env_set() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

env_variables (SCons.Scanner.LaTeX.LaTeX attribute)

Environment() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

erase_previous() (SCons.Script.Main.Progressor method)

error() (bin.SConsDoc.Libxml2ValidityHandler method)

(SCons.Script.SConsOptions.SConsOptionParser method)

escape() (in module SCons.Platform.posix)

(in module SCons.Platform.win32) (SCons.Subst.CmdStringHolder method) (SCons.Subst.Literal method) (SCons.Subst.SpecialAttrWrapper method)

escape_list() (in module SCons.Subst)

eval_constant_expression() (SCons.cpp.DumbPreProcessor method) (SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

eval_expression() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

ExampleCommand (class in bin.SConsExamples)

ExampleFile (class in bin.SConsExamples)

ExampleFolder (class in bin.SConsExamples)

ExampleInfo (class in bin.SConsExamples)

exampleNamesAreUnique() (in module bin.SConsExamples)

ExampleOutput (class in bin.SConsExamples)

exc_clear() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

exc_info() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

exception_set() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

exec_popen3() (in module SCons.Platform.posix)

exec_spawn() (in module SCons.Platform.win32)

exec_subprocess() (in module SCons.Platform.posix)

execute() (SCons.Action.CommandAction method)

(SCons.Action.FunctionAction method) (SCons.Action.LazyAction method)

Execute() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method)

execute() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method)

Execute() (SCons.Script.SConscript.SConsEnvironment method)

execute() (SCons.Taskmaster.AlwaysTask method)

(SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

execute_action_list() (in module SCons.Executor)

execute_actions_str() (in module SCons.Executor)

execute_nothing() (in module SCons.Executor)

execute_null_str() (in module SCons.Executor)

ExecuteCommand() (in module bin.SConsExamples)

executed() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

executed_with_callbacks() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

executed_without_callbacks() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

Executor (class in SCons.Executor)

executor (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

executor_cleanup() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

exists() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

exists_always() (in module SCons.Node)

exists_base() (in module SCons.Node)

exists_entry() (in module SCons.Node)

exists_file() (in module SCons.Node)

exists_none() (in module SCons.Node)

Exit() (SCons.Script.SConscript.SConsEnvironment static method)

exit() (SCons.Script.SConsOptions.SConsOptionParser method)

expand() (SCons.Subst.ListSubber method)

(SCons.Subst.StringSubber method)

expand_default() (SCons.Script.SConsOptions.SConsIn dentedHelpFormatter method)

expand_prog_name() (SCons.Script.SConsOptions.SConsOptionParser method)

expanded() (SCons.Subst.ListSubber method)

expandtabs() (SCons.Subst.CmdStringHolder method)

explain() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

ExplicitExit

Export() (SCons.Script.SConscript.SConsEnvironment method)

extend() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

F

F90Scanner (class in SCons.Scanner.Fortran)

fail_continue() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

fail_stop() (SCons.SConf.SConfBuildTask method) (SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

failed() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

FakeOptionParser (class in SCons.Script.Main)

FakeOptionParser.FakeOptionValues (class in SCons.Script.Main)

fetchLoggedInstances() (in module SCons.Debug)

field_list (SCons.Node.Alias.AliasNodeInfo attribute)

(SCons.Node.FS.FileNodeInfo attribute) (SCons.Node.Python.ValueNodeInfo attribute)

File (class in SCons.Node.FS)

File() (in module SCons.SConsign)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Node.FS.Dir method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.RootDir method) (SCons.Script.SConscript.SConsEnvironment method)

File.Attrs (class in SCons.Node.FS)

file_on_disk() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

FileBuildInfo (class in SCons.Node.FS)

FileBuildInfoFileToCsigMappingError

filedir_lookup() (SCons.Node.FS.FileFinder method)

FileFinder (class in SCons.Node.FS)

FileLock (class in SCons.Util.filelock)

FileNodeInfo (class in SCons.Node.FS)

finalize_result() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

find() (SCons.Subst.CmdStringHolder method)

find_cycle() (in module SCons.Taskmaster)

find_deepest_user_frame() (in module SCons.Script.Main)

find_file() (in module SCons.Node.FS)

(SCons.Node.FS.FileFinder method)

find_include() (SCons.Scanner.Classic static method)

(SCons.Scanner.ClassicCPP static method) (SCons.Scanner.D.D static method) (SCons.Scanner.Fortran.F90Scanner static method) (SCons.Scanner.LaTeX.LaTeX method)

find_include_file() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

find_include_names() (SCons.Scanner.Classic method)

(SCons.Scanner.ClassicCPP method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method)

find_next_candidate() (SCons.Taskmaster.Taskmaster method)

find_program_path() (in module SCons.Tool)

find_repo_file() (SCons.Node.FS.File method)

find_src_builder() (SCons.Node.FS.File method)

findAll() (bin.SConsDoc.TreeFactory static method)

findAllChildrenOf() (bin.SConsDoc.TreeFactory static method)

FindAllTools() (in module SCons.Tool)

FindENVPathDirs (class in SCons.Scanner.LaTeX)

FindFile() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

FindInstalledFiles() (SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

FindIxes() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

FindPathDirs (class in SCons.Scanner)

FindSourceFiles() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

FindTool() (in module SCons.Tool)

Finish() (SCons.SConf.SConfBase method)

flatten() (in module SCons.Util)

Flatten() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

flatten_sequence() (in module SCons.Util)

flush() (SCons.SConf.Streamer method)

fmt (SCons.Variables.Variables attribute)

for_signature() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.Subst.Literal method) (SCons.Subst.SpecialAttrWrapper method)

ForDirectory (in module SCons.SConsign)

format() (SCons.Node.Alias.AliasNodeInfo method)

(SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileBuildInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.NodeInfoBase method) (SCons.Node.Python.ValueNodeInfo method) (SCons.SConf.SConfBuildInfo method)

(SCons.Subst.CmdStringHolder method) (SCons.Util.DispatchingFormatter method)

format_description() (SCons.Script.SConsOptions.SCon sIndentedHelpFormatter method)

(SCons.Script.SConsOptions.SConsOptionGroup method) (SCons.Script.SConsOptions.SConsOptionParser method)

format_epilog() (SCons.Script.SConsOptions.SConsInde ntedHelpFormatter method)

(SCons.Script.SConsOptions.SConsOptionParser method)

format_heading() (SCons.Script.SConsOptions.SConsIn dentedHelpFormatter method)

format_help() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

format_local_option_help() (SCons.Script.SConsOptions.SConsOptionParser method)

format_map() (SCons.Subst.CmdStringHolder method)

format_option() (SCons.Script.SConsOptions.SConsInde ntedHelpFormatter method)

format_option_help() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

format_option_strings() (SCons.Script.SConsOptions.SC onsIndentedHelpFormatter method)

format_usage() (SCons.Script.SConsOptions.SConsInde ntedHelpFormatter method)

formatException() (SCons.Util.DispatchingFormatter method)

formatMessage() (SCons.Util.DispatchingFormatter method)

formatStack() (SCons.Util.DispatchingFormatter method)

formatTime() (SCons.Util.DispatchingFormatter method)

FormatVariableHelpText() (SCons.Variables.Variables method)

FortranCxxMixWarning

FortranScan() (in module SCons.Scanner.Fortran)

Frame (class in SCons.Script.SConscript) fromkeys() (SCons.Builder.CallableSelector class method)

(SCons.Builder.DictCmdGenerator class method) (SCons.Builder.DictEmitter class method) (SCons.Builder.OverrideWarner class method) (SCons.Environment.BuilderDict class method) (SCons.Node.Alias.AliasNameSpace class method) (SCons.Util.Selector class method)

FS (class in SCons.Node.FS)

fs (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.DirNodeInfo attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.FileNodeInfo attribute) (SCons.Node.FS.RootDir attribute)

fs_delete() (SCons.Script.Main.CleanTask method)

func_shorten() (in module SCons.Debug)

Function (class in bin.SConsDoc)

function_name() (SCons.Action.FunctionAction method)

FunctionAction (class in SCons.Action)

FunctionEvaluator (class in SCons.cpp)

FutureDeprecatedWarning

FutureReservedVariableWarning

G

generate() (in module SCons.Platform.aix)

(in module SCons.Platform.cygwin) (in module SCons.Platform.darwin) (in module SCons.Platform.hpux) (in module SCons.Platform.irix) (in module SCons.Platform.os2) (in module SCons.Platform.posix) (in module SCons.Platform.sunos) (in module SCons.Platform.win32)

GenerateHelpText() (SCons.Variables.Variables method)

genstring() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method)

(SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

get() (SCons.Builder.CallableSelector method)

(SCons.Builder.CompositeBuilder method) (SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.OverrideWarner method) (SCons.Environment.Base method) (SCons.Environment.BuilderDict method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Node.FS.EntryProxy method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Taskmaster.Job.ThreadPool method) (SCons.Util.Proxy method) (SCons.Util.Selector method)

get_abspath() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_action_list() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_action_side_effects() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_action_targets() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_all_children() (SCons.Executor.Executor method)

(SCons.Executor.Null method) (SCons.Script.Main.TreePrinter method) get_all_prerequisites() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_all_rdirs() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

get_all_sources() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_all_targets() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_architecture() (in module SCons.Platform.win32)

get_binfo() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_build_env() (SCons.Executor.Executor method)

(SCons.Executor.Null method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_build_scanner_path() (SCons.Executor.Executor method)

(SCons.Executor.Null method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_builder() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Tool.ToolInitializerMethod method)

get_CacheDir() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Executor.NullEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

get_cachedir_bsig() (SCons.Node.FS.File method)

get_cachedir_csig() (SCons.CacheDir.CacheDir method)

(SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_calling_namespaces() (in module SCons.Script.SConscript)

get_children() (in module SCons.Node)

get_content_hash() (SCons.Node.FS.File method)

get_contents() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.ActionCaller method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method) (SCons.Executor.Executor method) (SCons.Executor.Null method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_contents_dir() (in module SCons.Node)

get_contents_entry() (in module SCons.Node)

get_contents_file() (in module SCons.Node)

get_contents_none() (in module SCons.Node)

get_contents_sig() (SCons.Node.FS.File method)

get_csig() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_current_hash_algorithm_used() (in module SCons.Util.hashes)

Get_DataBase() (in module SCons.SConsign)

get_default_ENV() (in module SCons.Action)

get_default_fs() (in module SCons.Node.FS)

get_default_values() (SCons.Script.SConsOptions.SConsOptionParser method)

get_DefaultEnvironmentProxy() (in module SCons.Script.SConscript)

get_derived_children() (SCons.Script.Main.TreePrinter method)

get_description() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

get_dir() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method)

(SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_entry() (SCons.SConsign.Base method)

(SCons.SConsign.DB method) (SCons.SConsign.Dir method) (SCons.SConsign.DirFile method)

get_env() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_env_bool() (in module SCons.Util.sctypes)

get_env_scanner() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_environment_var() (in module SCons.Util.sctypes)

get_executor() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_factory() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

get_found_includes() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_hash_format() (in module SCons.Util.hashes)

get_implicit_deps() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method) (SCons.Executor.Executor method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_internal_path() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_kw() (SCons.Executor.Executor method)

get_labspath() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_lvars() (SCons.Executor.Executor method)

get_max_drift() (SCons.Node.FS.FS method)

get_max_drift_csig() (SCons.Node.FS.File method)

get_MkdirBuilder() (in module SCons.Node.FS)

get_name() (SCons.Builder.BuilderBase method)

get_names() (SCons.Script.Interactive.SConsInteractiveCmd method)

get_native_path() (in module SCons.Util)

get_next() (SCons.Node.Walker method)

get_ninfo() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_NullEnvironment() (in module SCons.Executor)

get_opt_string() (SCons.Script.SConsOptions.SConsOption method)

get_option() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

get_option_group() (SCons.Script.SConsOptions.SConsOptionParser method)

get_os_env_bool() (in module SCons.Util.sctypes)

get_parent_class() (SCons.Action.LazyAction method)

get_path() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_path_elements() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_paths_str() (in module SCons.Defaults)

get_prefix() (SCons.Builder.BuilderBase method)

get_presig() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

get_prog_name() (SCons.Script.SConsOptions.SConsOptionParser method)

get_program_files_dir() (in module SCons.Platform.win32)

get_relpath() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_root() (SCons.Node.FS.FS method)

get_scanner() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

get_size() (SCons.Node.FS.File method)

get_skeys() (SCons.Scanner.Classic method)

(SCons.Scanner.ClassicCPP method) (SCons.Scanner.Current method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method) (SCons.Scanner.ScannerBase method) (SCons.Scanner.Selector method)

get_source_scanner() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_sources() (SCons.Executor.Executor method)

get_src_builders() (SCons.Builder.BuilderBase method)

get_src_suffix() (SCons.Builder.BuilderBase method)

get_state() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_stored_implicit() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_stored_info() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_string() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_subst_proxy() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_suffix() (SCons.Builder.BuilderBase method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_system_root() (in module SCons.Platform.win32)

get_target() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

get_target_scanner() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

get_targets() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

get_text_contents() (SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Python.Value method)

get_timestamp() (SCons.Executor.Executor method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.File method)

(SCons.Node.FS.RootDir method)

get_tpath() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

get_unignored_sources() (SCons.Executor.Executor method)

(SCons.Executor.Null method)

get_usage() (SCons.Script.SConsOptions.SConsOptionParser method)

get_varlist() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

get_version() (SCons.Script.SConsOptions.SConsOptionParser method)

get_xlc() (in module SCons.Platform.aix)

getAttribute() (bin.SConsDoc.TreeFactory static method)

GetBatchExecutor() (in module SCons.Executor)

GetBuildFailures() (in module SCons.Script.Main)

GetBuildPath() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

getcwd() (SCons.Node.FS.FS method)

getEntityString() (bin.SConsDoc.DoctypeEntity method)

getFileContents() (bin.SConsExamples.ExampleInfo method)

GetLaunchDir() (SCons.Script.SConscript.SConsEnvironment static method)

getmtime() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

getName() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

GetOption() (in module SCons.Script.Main)

(SCons.Script.SConscript.SConsEnvironment method)

getRepositories() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

GetSConsVersion() (SCons.Script.SConscript.SConsEnvironment static method)

getsize() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

GetTag() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

getTail() (bin.SConsDoc.TreeFactory static method)

getText() (bin.SConsDoc.TreeFactory static method)

getvalue() (SCons.SConf.Streamer method)

Glob() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method)

glob() (SCons.Node.FS.Dir method)

Glob() (SCons.Node.FS.FS method)

glob() (SCons.Node.FS.RootDir method)

Glob() (SCons.Script.SConscript.SConsEnvironment method)

gvars() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method)

(SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

H

handle_missing_SConscript() (in module SCons.Script.SConscript)

has_builder() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

has_explicit_builder() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

has_glob_magic() (in module SCons.Node.FS)

has_option() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

has_src_builder() (SCons.Node.FS.File method)

hasAttribute() (bin.SConsDoc.TreeFactory static method)

hash_chunksize (SCons.Node.FS.File attribute)

hash_collect() (in module SCons.Util.hashes)

hash_file_signature() (in module SCons.Util.hashes)

hash_signature() (in module SCons.Util.hashes)

help (SCons.Variables.Variable attribute)

Help() (SCons.Script.SConscript.SConsEnvironment method)

HelpFunction() (in module SCons.Script)

hit_ratio (SCons.CacheDir.CacheDir property) I

ident (SCons.Taskmaster.Job.NewParallel.Worker property)

(SCons.Taskmaster.Job.Worker property)

identchars (SCons.Script.Interactive.SConsInteractiveCmd attribute)

IDLScan() (in module SCons.Scanner.IDL)

IDX() (in module SCons.Util)

ignore (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Ignore() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

ignore_cycle() (in module SCons.Node)

ignore_diskcheck_match() (in module SCons.Node.FS)

ignore_set (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

implicit (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

implicit_set (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Import() (SCons.Script.SConscript.SConsEnvironment method)

importfile() (in module bin.SConsDoc)

ImportVirtualenv() (in module SCons.Platform.virtualenv)

includes (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

indent() (SCons.Script.SConsOptions.SConsIndentedHe lpFormatter method)

index() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.CmdStringHolder method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

initialize_do_splitdrive() (in module SCons.Node.FS)

initialize_result() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

Initializers() (in module SCons.Tool) insert() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

interact() (in module SCons.Script.Interactive)

InternalError

InterruptState (class in SCons.Taskmaster.Job)

intro (SCons.Script.Interactive.SConsInteractiveCmd attribute)

invalidate_node_memos() (in module SCons.Node.FS)

is_a_Builder() (in module SCons.Builder)

is_alive() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

is_conftest() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

is_derived() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

is_derived_node() (in module SCons.Node)

is_derived_none() (in module SCons.Node)

is_Dict() (in module SCons.Util.sctypes)

is_done() (SCons.Node.Walker method)

is_enabled() (SCons.CacheDir.CacheDir method)

is_explicit (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

is_List() (in module SCons.Util.sctypes)

is_literal() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.Subst.CmdStringHolder method) (SCons.Subst.Literal method) (SCons.Subst.SpecialAttrWrapper method)

is_readonly() (SCons.CacheDir.CacheDir method)

is_Scalar() (in module SCons.Util.sctypes)

is_sconscript() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

is_Sequence() (in module SCons.Util.sctypes)

is_String() (in module SCons.Util.sctypes)

is_Tuple() (in module SCons.Util.sctypes)

is_under() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Python.Value method)

is_up_to_date() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

is_valid_construction_var() (in module SCons.Util.envs)

isalnum() (SCons.Subst.CmdStringHolder method)

isalpha() (SCons.Subst.CmdStringHolder method)

isascii() (SCons.Subst.CmdStringHolder method)

isDaemon() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

isdecimal() (SCons.Subst.CmdStringHolder method)

isdigit() (SCons.Subst.CmdStringHolder method)

isdir() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

isfile() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

isFileRef() (bin.SConsExamples.ExampleFile method)

isidentifier() (SCons.Subst.CmdStringHolder method)

IsInVirtualenv() (in module SCons.Platform.virtualenv)

islink() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

islower() (SCons.Subst.CmdStringHolder method)

isnumeric() (SCons.Subst.CmdStringHolder method)

isprintable() (SCons.Subst.CmdStringHolder method)

isSConsXml() (in module bin.SConsDoc)

isspace() (SCons.Subst.CmdStringHolder method)

istitle() (SCons.Subst.CmdStringHolder method)

isupper() (SCons.Subst.CmdStringHolder method)

Item (class in bin.SConsDoc)

items() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.OverrideWarner method) (SCons.dblite._Dblite method) (SCons.Environment.Base method) (SCons.Environment.BuilderDict method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Util.Selector method)

J

JavaScanner() (in module SCons.Scanner.Java)

Jobs (class in SCons.Taskmaster.Job)

join() (SCons.Subst.CmdStringHolder method)

(SCons.Taskmaster.Job.NewParallel.Worker method) (SCons.Taskmaster.Job.Worker method)

K

key (SCons.Variables.Variable attribute)

key() (SCons.Memoize.CountDict method)

(SCons.Memoize.Counter method) (SCons.Memoize.CountValue method) keys() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.OverrideWarner method) (SCons.dblite._Dblite method) (SCons.Environment.Base method) (SCons.Environment.BuilderDict method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Util.Selector method) (SCons.Variables.Variables method)

keyword_paths (SCons.Scanner.LaTeX.LaTeX attribute)

L

lastcmd (SCons.Script.Interactive.SConsInteractiveCmd attribute)

LaTeX (class in SCons.Scanner.LaTeX)

LaTeXScanner() (in module SCons.Scanner.LaTeX)

LazyAction (class in SCons.Action)

LegacyParallel (class in SCons.Taskmaster.Job)

Libxml2ValidityHandler (class in bin.SConsDoc)

link() (SCons.Node.FS.Dir method)

(SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

linked (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

LinkFunc() (in module SCons.Node.FS)

LinkWarning

ListAction (class in SCons.Action)

listdir() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

ListEmitter (class in SCons.Builder)

listLoggedInstances() (in module SCons.Debug)

ListSubber (class in SCons.Subst)

ListVariable() (in module SCons.Variables)

(in module SCons.Variables.ListVariable)

Literal (class in SCons.Subst)

Literal() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

literal() (SCons.Subst.ListSubber method)

ljust() (SCons.Subst.CmdStringHolder method)

Local() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

LocalFS (class in SCons.Node.FS)

LocalString() (in module SCons.Node.FS)

lock() (SCons.Taskmaster.Job.NewParallel.FakeLock method)

Log() (SCons.SConf.CheckContext method)

LOGGER (SCons.SConf.SConfBuildTask attribute)

(SCons.Script.Main.BuildTask attribute) (SCons.Script.Main.CleanTask attribute) (SCons.Script.Main.QuestionTask attribute) (SCons.Taskmaster.AlwaysTask attribute) (SCons.Taskmaster.OutOfDateTask attribute) (SCons.Taskmaster.Task attribute)

logical_lines() (in module SCons.Util)

LogicalLines (class in SCons.Util)

logInstanceCreation() (in module SCons.Debug)

lookup() (SCons.Node.Alias.AliasNameSpace method)

lower() (SCons.Subst.CmdStringHolder method)

lstat() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

lstrip() (SCons.Subst.CmdStringHolder method)

lvars (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

lvars() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

M

main() (in module SCons.Script.Main)

make_path_relative() (in module SCons.Util)

make_ready() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.SConf.SConfBuildTask method) (SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

make_ready_all() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

make_ready_current() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method)

(SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

makedirs() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

maketrans() (SCons.Subst.CmdStringHolder method)

MandatoryDeprecatedWarning

match_splitext() (in module SCons.Builder)

MD5collect() (in module SCons.Util.hashes)

MD5filesignature() (in module SCons.Util.hashes)

MD5signature() (in module SCons.Util.hashes)

memory() (in module SCons.Debug)

MemStats (class in SCons.Util.stats)

merge() (SCons.Node.Alias.AliasBuildInfo method)

(SCons.Node.Alias.AliasNodeInfo method) (SCons.Node.BuildInfoBase method) (SCons.Node.FS.DirBuildInfo method) (SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileBuildInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.NodeInfoBase method) (SCons.Node.Python.ValueBuildInfo method) (SCons.Node.Python.ValueNodeInfo method) (SCons.SConf.SConfBuildInfo method) (SCons.SConsign.Base method) (SCons.SConsign.DB method) (SCons.SConsign.Dir method) (SCons.SConsign.DirFile method)

MergeFlags() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

Message() (SCons.SConf.CheckContext method)

MethodWrapper (class in SCons.Util.envs)

misc_header (SCons.Script.Interactive.SConsInteractiveCmd attribute) MisleadingKeywordsWarning

misses (SCons.CacheDir.CacheDir property)

missing() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

MissingSConscriptWarning

mkdir() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

mkdir_func() (in module SCons.Defaults)

MkdirFunc() (in module SCons.Node.FS)

modify_env_var() (in module SCons.Scanner.LaTeX)

module

bin.SConsDoc bin.SConsExamples SCons SCons.Action SCons.Builder SCons.CacheDir SCons.compat SCons.Conftest SCons.cpp SCons.dblite SCons.Debug SCons.Defaults SCons.Environment SCons.Errors SCons.Executor SCons.exitfuncs SCons.Memoize SCons.Node SCons.Node.Alias SCons.Node.FS SCons.Node.Python SCons.PathList

SCons.Platform SCons.Platform.aix SCons.Platform.cygwin SCons.Platform.darwin SCons.Platform.hpux SCons.Platform.irix SCons.Platform.mingw SCons.Platform.os2 SCons.Platform.posix SCons.Platform.sunos SCons.Platform.virtualenv SCons.Platform.win32 SCons.Scanner SCons.Scanner.C SCons.Scanner.D SCons.Scanner.Dir SCons.Scanner.Fortran SCons.Scanner.IDL SCons.Scanner.Java SCons.Scanner.LaTeX SCons.Scanner.Prog SCons.Scanner.RC SCons.Scanner.SWIG SCons.SConf SCons.SConsign SCons.Script SCons.Script.Interactive SCons.Script.Main SCons.Script.SConscript SCons.Script.SConsOptions SCons.Subst SCons.Taskmaster SCons.Taskmaster.Job SCons.Tool SCons.Util SCons.Util.envs SCons.Util.filelock SCons.Util.hashes SCons.Util.sctypes SCons.Util.stats SCons.Variables SCons.Variables.BoolVariable SCons.Variables.EnumVariable SCons.Variables.ListVariable SCons.Variables.PackageVariable SCons.Variables.PathVariable SCons.Warnings

move_func() (in module SCons.Defaults)

mro() (SCons.compat.NoSlotsPyPy method)

MSVCError

multiple_side_effect_has_builder() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

must_be_same() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

N

name (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.EntryProxyAttributeError attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Taskmaster.Job.NewParallel.Worker property) (SCons.Taskmaster.Job.Worker property)

native_id (SCons.Taskmaster.Job.NewParallel.Worker property)

(SCons.Taskmaster.Job.Worker property)

NeedConfigHBuilder() (in module SCons.SConf)

needs_execute() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

needs_normpath_match() (in module SCons.Node.FS)

new_binfo() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

new_ninfo() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

newEtreeNode() (bin.SConsDoc.TreeFactory static method)

newNode() (bin.SConsDoc.TreeFactory static method)

NewParallel (class in SCons.Taskmaster.Job)

NewParallel.FakeCondition (class in SCons.Taskmaster.Job)

NewParallel.FakeLock (class in SCons.Taskmaster.Job)

NewParallel.State (class in SCons.Taskmaster.Job)

NewParallel.Worker (class in SCons.Taskmaster.Job)

newSubNode() (bin.SConsDoc.TreeFactory static method)

newXmlTree() (bin.SConsDoc.TreeFactory method)

next_line() (SCons.Subst.ListSubber method)

next_task() (SCons.Taskmaster.Taskmaster method)

next_word() (SCons.Subst.ListSubber method) ninfo (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute) (SCons.SConsign.SConsignEntry attribute)

NLWrapper (class in SCons.Subst)

no_batch_key() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

NO_DEFAULT_VALUE (SCons.Script.SConsOptions.S ConsIndentedHelpFormatter attribute)

no_next_candidate() (SCons.Taskmaster.Taskmaster method)

no_tlb() (in module SCons.Scanner.RC)

nocache (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

NoCache() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

noclean (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

(SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

NoClean() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

Node (class in SCons.Node)

Node.Attrs (class in SCons.Node)

node_conv() (in module SCons.PathList)

NodeInfo (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

NodeInfoBase (class in SCons.Node)

NodeList (class in SCons.Node)

(class in SCons.Util)

nohelp (SCons.Script.Interactive.SConsInteractiveCmd attribute)

non_sconf_nodes (SCons.SConf.SConfBuildTask attribute)

NoObjectCountWarning

NoParallelSupportWarning

NoSlotsPyPy (class in SCons.compat)

NoSubstitutionProxy() (in module SCons.Environment)

notify() (SCons.Taskmaster.Job.NewParallel.FakeCondition method)

notify_all() (SCons.Taskmaster.Job.NewParallel.FakeCondition method)

Null (class in SCons.Executor)

(class in SCons.Util.sctypes)

NullCmdGenerator (class in SCons.Defaults)

NullEnvironment (class in SCons.Executor)

nullify() (SCons.Executor.Executor method)

NullNodeList (class in SCons.Subst)

NullSeq (class in SCons.Util.sctypes) O

obj (SCons.Node.FS.EntryProxyAttributeError attribute)

on_disk_entries (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

onecmd() (SCons.Script.Interactive.SConsInteractiveCmd method)

only_dirs() (in module SCons.Scanner.Dir)

open() (in module SCons.dblite)

(SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method)

open_strip() (SCons.Subst.ListSubber method)

opener() (SCons.dblite._Dblite method)

OutOfDateTask (class in SCons.Taskmaster)

Override() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

OverrideEnvironment (class in SCons.Environment)

overridelist (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

OverrideWarner (class in SCons.Builder)

P

PackageVariable() (in module SCons.Variables)

(in module SCons.Variables.PackageVariable)

parse_args() (SCons.Script.SConsOptions.SConsOptionParser method)

ParseConfig() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

parseContent() (bin.SConsDoc.SConsDocHandler method)

(bin.SConsDoc.SConsDocTree method)

ParseDepends() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method)

(SCons.Script.SConscript.SConsEnvironment method)

parseDomtree() (bin.SConsDoc.SConsDocHandler method)

ParseFlags() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

parseInstance() (bin.SConsDoc.SConsDocHandler method)

parseItems() (bin.SConsDoc.SConsDocHandler method)

parseline() (SCons.Script.Interactive.SConsInteractiveCmd method)

Parser() (in module SCons.Script.SConsOptions)

parseUsesSets() (bin.SConsDoc.SConsDocHandler method)

parseXmlFile() (bin.SConsDoc.SConsDocHandler method)

(bin.SConsDoc.SConsDocTree method)

partition() (SCons.Subst.CmdStringHolder method)

path (SCons.Node.FS.RootDir attribute)

path() (SCons.Scanner.Classic method)

(SCons.Scanner.ClassicCPP method) (SCons.Scanner.Current method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method) (SCons.Scanner.ScannerBase method) (SCons.Scanner.Selector method)

path_string() (in module SCons.Script.Main)

PathAccept() (SCons.Variables.PathVariable._PathVariableClass static method)

PathExists() (SCons.Variables.PathVariable._PathVariableClass static method)

PathIsDir() (SCons.Variables.PathVariable._PathVariableClass static method)

PathIsDirCreate() (SCons.Variables.PathVariable._PathVariableClass static method)

PathIsFile() (SCons.Variables.PathVariable._PathVariableClass static method) PathList() (in module SCons.PathList)

PDFLaTeXScanner() (in module SCons.Scanner.LaTeX)

piped_env_spawn() (in module SCons.Platform.posix)

piped_spawn() (in module SCons.Platform.win32)

Platform() (in module SCons.Platform)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

platform_default() (in module SCons.Platform)

platform_module() (in module SCons.Platform)

PlatformSpec (class in SCons.Platform)

pop() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.ListEmitter method) (SCons.Builder.OverrideWarner method) (SCons.Environment.BuilderDict method) (SCons.Executor.TSList method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.Selector method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

popitem() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.OverrideWarner method) (SCons.Environment.BuilderDict method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Util.Selector method)

post_actions (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

postcmd() (SCons.Script.Interactive.SConsInteractiveCmd method)

postloop() (SCons.Script.Interactive.SConsInteractiveCmd method)

postprocess() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.SConf.SConfBuildTask method) (SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

pre_actions (SCons.Executor.Executor attribute)

(SCons.Executor.Null attribute)

precious (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Precious() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

precmd() (SCons.Script.Interactive.SConsInteractiveCmd method)

preloop() (SCons.Script.Interactive.SConsInteractiveCmd method)

preparation_failed() (SCons.Taskmaster.Job.ThreadPool method)

prepare() (SCons.Executor.Executor method)

(SCons.Executor.Null method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.SConf.SConfBuildTask method) (SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

prepare_dependencies() (SCons.Node.FS.FileBuildInfo method)

(SCons.SConf.SConfBuildInfo method)

prepare_to_store() (SCons.Variables.ListVariable._ListVariable method)

Prepend() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

PrependENVPath() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

PrependLIBS() (SCons.SConf.CheckContext method)

PrependPath() (in module SCons.Util.envs)

PrependUnique() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

PreProcessor (class in SCons.cpp)

prerequisites (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute)

(SCons.Node.FS.RootDir attribute)

(SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

preserve_unknown_options (SCons.Script.SConsOptions.SConsOptionParser attribute)

presub_lines() (SCons.Action._ActionAction method)

(SCons.Action.ActionBase method) (SCons.Action.CommandAction method) (SCons.Action.CommandGeneratorAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method) (SCons.Action.ListAction method)

prettyPrintFile() (bin.SConsDoc.TreeFactory static method)

prev (SCons.Script.Main.Progressor attribute)

print_cmd_line() (SCons.Action._ActionAction method)

(SCons.Action.CommandAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method)

print_help() (SCons.Script.SConsOptions.SConsOptionParser method)

print_it (SCons.Util.DisplayEngine attribute)

print_local_option_help() (SCons.Script.SConsOptions.SConsOptionParser method)

print_time() (in module SCons.Util)

print_topics() (SCons.Script.Interactive.SConsInteractiveCmd method)

print_tree() (in module SCons.Util)

print_usage() (SCons.Script.SConsOptions.SConsOptionParser method)

print_version() (SCons.Script.SConsOptions.SConsOptionParser method)

PrintHelp() (in module SCons.Script.Main)

process() (SCons.Action.CommandAction method)

(SCons.Action.LazyAction method) (SCons.Script.SConsOptions.SConsOption method)

process_contents() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

process_file() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

process_warn_strings() (in module SCons.Warnings)

processDefines() (in module SCons.Defaults)

ProgramScanner() (in module SCons.Scanner.Prog)

Progress() (in module SCons.Script.Main)

Progressor (class in SCons.Script.Main)

prompt (SCons.Script.Interactive.SConsInteractiveCmd attribute)

Proxy (class in SCons.Util)

pseudo (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Pseudo() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

pspawn_wrapper() (SCons.SConf.SConfBase method)

push() (SCons.CacheDir.CacheDir method)

push_if_forced() (SCons.CacheDir.CacheDir method)

push_to_cache() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

put() (SCons.Taskmaster.Job.ThreadPool method)

PyPackageDir() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.FS.FS method) (SCons.Script.SConscript.SConsEnvironment method)

python_version_deprecated() (in module SCons.Script.Main)

python_version_string() (in module SCons.Script.Main)

python_version_unsupported() (in module SCons.Script.Main)

PythonVersionWarning

Q

QuestionTask (class in SCons.Script.Main)

quote_spaces() (in module SCons.Subst)

R

raise_exception() (in module SCons.Subst)

raise_exception_on_error (SCons.Script.SConsOptions.SConsOptionParser attribute)

RCScan() (in module SCons.Scanner.RC)

rdir() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

RDirs() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

read() (SCons.Node.Python.Value method)

read_file() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method) (SCons.Script.SConsOptions.SConsValues method)

read_module() (SCons.Script.SConsOptions.SConsValues method)

readAllExampleInfos() (in module bin.SConsExamples)

readExampleInfos() (in module bin.SConsExamples)

readlines() (SCons.Util.LogicalLines method)

readlink() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method) READY (SCons.Taskmaster.Job.NewParallel.State attribute)

really_build() (SCons.Node.Alias.Alias method)

recurse_nodes() (SCons.Scanner.C.SConsCPPConditio nalScannerWrapper method)

(SCons.Scanner.C.SConsCPPScannerWrapper method)

ref_count (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

RegError (in module SCons.Util)

RegGetValue() (in module SCons.Util)

register() (in module SCons.exitfuncs)

RegOpenKeyEx() (in module SCons.Util)

rel_path() (SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

release_lock() (SCons.Util.filelock.FileLock method)

release_target_info() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

released_target_info (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

remove() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.NodeList method) (SCons.Node.Python.Value method) (SCons.Script.Main.CleanTask method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

remove_entities() (in module bin.SConsDoc)

remove_methods() (SCons.Tool.ToolInitializer method)

remove_option() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

RemoveMethod() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

removeprefix() (SCons.Subst.CmdStringHolder method)

removesuffix() (SCons.Subst.CmdStringHolder method)

rename() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

rename_module() (in module SCons.compat)

render_include_tree() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

render_tree() (in module SCons.Util)

rentry() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

rentry_exists_on_disk() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

reparse_local_options() (SCons.Script.SConsOptions.SConsOptionParser method)

Replace() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

replace() (SCons.Subst.CmdStringHolder method)

replace_string() (SCons.Script.Main.Progressor method)

ReplaceIxes() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

repositories (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

Repository() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.FS.FS method) (SCons.Script.SConscript.SConsEnvironment method)

Requires() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

ReservedVariableWarning

Reset() (in module SCons.SConsign)

reset_executor() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method)

(SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

resolve_include() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

restore() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

result (SCons.SConf.SConfBuildInfo attribute)

Result() (SCons.SConf.CheckContext method)

retrieve() (SCons.CacheDir.CacheDir method)

retrieve_from_cache() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

Return() (in module SCons.Script.SConscript)

reverse() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Node.NodeList method) (SCons.Script.TargetList method) (SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

revert_io() (in module SCons.Script.Main)

rexists() (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

rexists_base() (in module SCons.Node)

rexists_node() (in module SCons.Node)

rexists_none() (in module SCons.Node)

rfile() (in module SCons.Action)

(in module SCons.Executor) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

rfind() (SCons.Subst.CmdStringHolder method)

Rfindalldirs() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

rightmost_separator() (in module SCons.Util)

rindex() (SCons.Subst.CmdStringHolder method)

rjust() (SCons.Subst.CmdStringHolder method)

root (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

RootDir (class in SCons.Node.FS)

RootDir.Attrs (class in SCons.Node.FS)

rpartition() (SCons.Subst.CmdStringHolder method)

rsplit() (SCons.Subst.CmdStringHolder method)

rstr() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

rstrip() (SCons.Subst.CmdStringHolder method)

ruler (SCons.Script.Interactive.SConsInteractiveCmd attribute)

run() (SCons.Taskmaster.Job.Jobs method)

(SCons.Taskmaster.Job.NewParallel.Worker method) (SCons.Taskmaster.Job.Worker method)

RunProg() (SCons.SConf.CheckContext method)

S

sanitize_shell_env() (in module SCons.Util)

save() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

Save() (SCons.Variables.Variables method)

save_strings() (in module SCons.Node.FS)

sbuilder (SCons.Node.FS.Base attribute)

(SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

scan() (in module SCons.Scanner.Java)

(in module SCons.Scanner.Prog) (SCons.Executor.Executor method) (SCons.Node.Alias.Alias method) (SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method) (SCons.Scanner.Classic method) (SCons.Scanner.ClassicCPP method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method)

scan_in_memory() (in module SCons.Scanner.Dir)

scan_on_disk() (in module SCons.Scanner.Dir) scan_recurse() (SCons.Scanner.LaTeX.LaTeX method)

scan_sources() (SCons.Executor.Executor method)

scan_targets() (SCons.Executor.Executor method)

scandir() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

Scanner() (in module SCons.Scanner)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

scanner_key() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

scanner_map_delete() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

scanner_paths (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

ScannerBase (class in SCons.Scanner)

SConf() (in module SCons.SConf)

SConfBase (class in SCons.SConf)

SConfBase.TestWrapper (class in SCons.SConf)

SConfBuildInfo (class in SCons.SConf)

SConfBuildTask (class in SCons.SConf)

SConfError

SConfWarning

SCons

module

SCons (SCons.Executor.NullEnvironment attribute)

SCons.Action

module

SCons.Builder

module

SCons.CacheDir

module

SCons.compat

module

SCons.Conftest

module

SCons.cpp

module

SCons.dblite

module

SCons.Debug

module

SCons.Defaults

module

SCons.Environment

module

SCons.Errors

module

SCons.Executor

module

SCons.exitfuncs

module

SCons.Memoize

module

SCons.Node

module

SCons.Node.Alias

module

SCons.Node.FS

module

SCons.Node.Python

module

SCons.PathList

module

SCons.Platform

module

SCons.Platform.aix

module

SCons.Platform.cygwin

module

SCons.Platform.darwin

module

SCons.Platform.hpux

module SCons.Platform.irix

module

SCons.Platform.mingw

module

SCons.Platform.os2

module

SCons.Platform.posix

module

SCons.Platform.sunos

module

SCons.Platform.virtualenv

module

SCons.Platform.win32

module

SCons.Scanner

module

SCons.Scanner.C

module

SCons.Scanner.D

module

SCons.Scanner.Dir

module

SCons.Scanner.Fortran

module

SCons.Scanner.IDL

module

SCons.Scanner.Java

module

SCons.Scanner.LaTeX

module

SCons.Scanner.Prog

module

SCons.Scanner.RC

module

SCons.Scanner.SWIG

module

SCons.SConf

module

SCons.SConsign

module

SCons.Script

module

SCons.Script.Interactive

module

SCons.Script.Main

module

SCons.Script.SConscript

module

SCons.Script.SConsOptions

module

SCons.Subst

module

SCons.Taskmaster

module

SCons.Taskmaster.Job

module

SCons.Tool

module

SCons.Util

module

SCons.Util.envs

module

SCons.Util.filelock

module

SCons.Util.hashes

module

SCons.Util.sctypes

module

SCons.Util.stats

module

SCons.Variables

module

SCons.Variables.BoolVariable

module

SCons.Variables.EnumVariable

module

SCons.Variables.ListVariable

module

SCons.Variables.PackageVariable

module

SCons.Variables.PathVariable

module

SCons.Warnings

module

scons_current_file() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method) scons_subproc_run() (in module SCons.Action)

scons_subst() (in module SCons.Subst)

scons_subst_list() (in module SCons.Subst)

scons_subst_once() (in module SCons.Subst)

SConsBadOptionError

SConsCPPConditionalScanner (class in SCons.Scanner.C)

SConsCPPConditionalScannerWrapper (class in SCons.Scanner.C)

SConsCPPScanner (class in SCons.Scanner.C)

SConsCPPScannerWrapper (class in SCons.Scanner.C)

SConscript() (SCons.Script.SConscript.SConsEnvironment method)

SConscript_exception() (in module SCons.Script.SConscript)

SConscriptChdir() (SCons.Script.SConscript.SConsEnvironment static method)

SConscriptReturn

SConsDocHandler (class in bin.SConsDoc)

SConsDocTree (class in bin.SConsDoc)

SConsEnvironment (class in SCons.Script.SConscript)

SConsEnvironmentError

sconsign() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.RootDir method)

sconsign_dir() (in module SCons.Node.FS)

sconsign_none() (in module SCons.Node.FS)

SConsignEntry (class in SCons.SConsign)

SConsignFile() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

SConsIndentedHelpFormatter (class in SCons.Script.SConsOptions)

SConsInteractiveCmd (class in SCons.Script.Interactive)

SConsLockFailure

SConsOption (class in SCons.Script.SConsOptions)

SConsOptionGroup (class in SCons.Script.SConsOptions)

SConsOptionParser (class in SCons.Script.SConsOptions)

SConsPrintHelpException

SConsValues (class in SCons.Script.SConsOptions)

SConsWarning

SConsWarningOnByDefault (in module SCons.Warnings)

searched (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

SEARCHING (SCons.Taskmaster.Job.NewParallel.State attribute)

select() (SCons.Scanner.C.SConsCPPConditionalScann erWrapper method)

(SCons.Scanner.C.SConsCPPScannerWrapper method) (SCons.Scanner.Classic method) (SCons.Scanner.ClassicCPP method) (SCons.Scanner.Current method) (SCons.Scanner.D.D method) (SCons.Scanner.Fortran.F90Scanner method) (SCons.Scanner.LaTeX.LaTeX method) (SCons.Scanner.ScannerBase method) (SCons.Scanner.Selector method)

select_paths_in_venv() (in module SCons.Platform.virtualenv)

select_scanner() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

Selector (class in SCons.Scanner)

(class in SCons.Util)

semi_deepcopy() (in module SCons.Util)

semi_deepcopy_dict() (in module SCons.Util)

Serial (class in SCons.Taskmaster.Job)

set() (SCons.Taskmaster.Job.InterruptState method)

set_action_list() (SCons.Executor.Executor method)

(SCons.Executor.Null method) set_always_build() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_build_result() (SCons.SConf.SConfBuildInfo method)

set_conflict_handler() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

set_default() (SCons.Script.SConsOptions.SConsOptionParser method)

set_defaults() (SCons.Script.SConsOptions.SConsOptionParser method)

set_description() (SCons.Script.SConsOptions.SConsOptionGroup method)

(SCons.Script.SConsOptions.SConsOptionParser method)

set_diskcheck() (in module SCons.Node.FS)

set_duplicate() (in module SCons.Node.FS)

set_entry() (SCons.SConsign.Base method)

(SCons.SConsign.DB method) (SCons.SConsign.Dir method) (SCons.SConsign.DirFile method)

set_executor() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_explicit() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method)

(SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_hash_format() (in module SCons.Util.hashes)

set_local() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

set_long_opt_delimiter() (SCons.Script.SConsOptions.S ConsIndentedHelpFormatter method)

set_max_drift() (SCons.Node.FS.FS method)

set_missing_sconscript_error() (in module SCons.Script)

set_mode() (SCons.Util.DisplayEngine method)

set_nocache() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_noclean() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_option() (SCons.Script.SConsOptions.SConsValues method)

set_parser() (SCons.Script.SConsOptions.SConsIndente dHelpFormatter method)

set_precious() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_process_default_values() (SCons.Script.SConsOptions.SConsOptionParser method)

set_pseudo() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_SConstruct_dir() (SCons.Node.FS.FS method)

set_short_opt_delimiter() (SCons.Script.SConsOptions.S ConsIndentedHelpFormatter method)

set_specific_source() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_src_builder() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

set_src_suffix() (SCons.Builder.BuilderBase method)

set_state() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

set_suffix() (SCons.Builder.BuilderBase method)

set_title() (SCons.Script.SConsOptions.SConsOptionGroup method)

set_usage() (SCons.Script.SConsOptions.SConsOptionParser method)

SetAllowableExceptions() (in module SCons.Subst)

setAttribute() (bin.SConsDoc.TreeFactory static method)

SetBuildType() (in module SCons.SConf)

SetCacheMode() (in module SCons.SConf)

setDaemon() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

setdefault() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.OverrideWarner method)

SetDefault() (SCons.Environment.Base method)

setdefault() (SCons.Environment.Base method)

(SCons.Environment.BuilderDict method)

SetDefault() (SCons.Environment.OverrideEnvironment method)

setdefault() (SCons.Environment.OverrideEnvironment method)

(SCons.Environment.SubstitutionEnvironment method) (SCons.Node.Alias.AliasNameSpace method)

SetDefault() (SCons.Script.SConscript.SConsEnvironment method)

setdefault() (SCons.Script.SConscript.SConsEnvironment method)

(SCons.Util.Selector method)

SetLIBS() (SCons.SConf.CheckContext method)

setName() (SCons.Taskmaster.Job.NewParallel.Worker method)

(SCons.Taskmaster.Job.Worker method)

SetOption() (in module SCons.Script.Main)

(SCons.Script.SConscript.SConsEnvironment method)

SetProgressDisplay() (in module SCons.SConf)

settable (SCons.Script.SConsOptions.SConsValues attribute) setTail() (bin.SConsDoc.TreeFactory static method)

setText() (bin.SConsDoc.TreeFactory static method)

shared (SCons.Node.Alias.Alias.Attrs attribute)

(SCons.Node.FS.Base.Attrs attribute) (SCons.Node.FS.Dir.Attrs attribute) (SCons.Node.FS.Entry.Attrs attribute) (SCons.Node.FS.File.Attrs attribute) (SCons.Node.FS.RootDir.Attrs attribute) (SCons.Node.Node.Attrs attribute) (SCons.Node.Python.Value.Attrs attribute)

SharedFlagChecker() (in module SCons.Defaults)

SharedObjectEmitter() (in module SCons.Defaults)

show() (SCons.Script.Main.CleanTask method)

side_effect (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

side_effects (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

SideEffect() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

silent_intern() (in module SCons.Util)

size (SCons.Node.FS.FileNodeInfo attribute)

sort() (SCons.Builder.ListEmitter method)

(SCons.Executor.TSList method) (SCons.Node.NodeList method) (SCons.Script.TargetList method)

(SCons.Subst.ListSubber method) (SCons.Subst.Targets_or_Sources method) (SCons.Util.CLVar method) (SCons.Util.NodeList method) (SCons.Util.UniqueList method) (SCons.Variables.ListVariable._ListVariable method)

sort_key() (SCons.Scanner.Classic static method)

(SCons.Scanner.ClassicCPP static method) (SCons.Scanner.D.D static method) (SCons.Scanner.Fortran.F90Scanner static method) (SCons.Scanner.LaTeX.LaTeX static method)

sources (SCons.Executor.Batch attribute)

(SCons.Node.Alias.Alias attribute) (SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

sources_set (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

spawn() (in module SCons.Platform.win32)

spawnve() (in module SCons.Platform.win32)

SpecialAttrWrapper (class in SCons.Subst)

spinner() (SCons.Script.Main.Progressor method)

Split() (in module SCons.Util)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

split() (SCons.Subst.CmdStringHolder method)

splitext() (in module SCons.Util) (SCons.Builder.BuilderBase method)

splitlines() (SCons.Subst.CmdStringHolder method)

src_builder() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

src_builder_sources() (SCons.Builder.BuilderBase method)

src_suffixes() (SCons.Builder.BuilderBase method)

(SCons.Builder.DictCmdGenerator method)

srcdir (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

srcdir_duplicate() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

srcdir_find_file() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

srcdir_list() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

srcnode() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

StackSizeWarning

STALLED (SCons.Taskmaster.Job.NewParallel.State attribute)

standard_option_list (SCons.Script.SConsOptions.SConsOptionParser attribute)

start() (SCons.Taskmaster.Job.LegacyParallel method)

(SCons.Taskmaster.Job.NewParallel method) (SCons.Taskmaster.Job.NewParallel.Worker method) (SCons.Taskmaster.Job.Serial method) (SCons.Taskmaster.Job.Worker method)

start_handling_includes() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method)

(SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

startswith() (SCons.Subst.CmdStringHolder method)

stat() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.FS method) (SCons.Node.FS.LocalFS method) (SCons.Node.FS.RootDir method)

state (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

StaticObjectEmitter() (in module SCons.Defaults)

Stats (class in SCons.Taskmaster)

(class in SCons.Util.stats)

stop() (SCons.Taskmaster.Taskmaster method)

stop_handling_includes() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

StopError

STORE_ACTIONS (SCons.Script.SConsOptions.SConsOption attribute)

store_info (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute) store_info() (SCons.SConsign.Base method)

(SCons.SConsign.DB method) (SCons.SConsign.Dir method) (SCons.SConsign.DirFile method)

store_info_file() (in module SCons.Node)

store_info_pass() (in module SCons.Node)

store_local_option_strings() (SCons.Script.SConsOption s.SConsIndentedHelpFormatter method)

store_option_strings() (SCons.Script.SConsOptions.SCo nsIndentedHelpFormatter method)

str_for_display() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Python.Value method)

str_to_node() (SCons.Node.Alias.AliasNodeInfo method)

(SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.Python.ValueNodeInfo method)

Streamer (class in SCons.SConf)

strfunction() (SCons.Action.ActionCaller method)

(SCons.Action.CommandAction method) (SCons.Action.FunctionAction method) (SCons.Action.LazyAction method)

string (SCons.SConf.SConfBuildInfo attribute)

string() (SCons.Script.Main.Progressor method)

string_to_classes() (in module SCons.Debug)

StringSubber (class in SCons.Subst)

strip() (SCons.Subst.CmdStringHolder method)

subprocess_spawn() (in module SCons.Platform.posix)

subst() (SCons.Action.ActionCaller method)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

subst_args() (SCons.Action.ActionCaller method)

subst_dict() (in module SCons.Subst)

subst_kw() (SCons.Action.ActionCaller method)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

subst_list() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

subst_path() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.PathList._PathList method) (SCons.Script.SConscript.SConsEnvironment method)

subst_src_suffixes() (SCons.Builder.BuilderBase method)

subst_target_source() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

substitute() (SCons.Subst.ListSubber method)

(SCons.Subst.StringSubber method)

SubstitutionEnvironment (class in SCons.Environment)

suppressWarningClass() (in module SCons.Warnings)

swapcase() (SCons.Subst.CmdStringHolder method)

SWIGScanner() (in module SCons.Scanner.SWIG)

symlink() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

sync() (SCons.dblite._Dblite method)

synonyms (SCons.Script.Interactive.SConsInteractiveCmd attribute) T

Tag() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

take_action() (SCons.Script.SConsOptions.SConsOption method)

takes_value() (SCons.Script.SConsOptions.SConsOption method)

target_from_source() (SCons.Node.FS.Base method)

(SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method)

target_from_source_base() (in module SCons.Node)

target_from_source_none() (in module SCons.Node)

Target_or_Source (class in SCons.Subst)

target_peers (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

target_string (SCons.Script.Main.Progressor attribute)

TargetList (class in SCons.Script)

TargetNotBuiltWarning

targets (SCons.Executor.Batch attribute)

Targets_or_Sources (class in SCons.Subst)

Task (class in SCons.Taskmaster)

Taskmaster (class in SCons.Taskmaster)

TempFileMunge (class in SCons.Platform)

test_load_all_site_scons_dirs() (in module SCons.Script.Main)

this_word() (SCons.Subst.ListSubber method)

ThreadPool (class in SCons.Taskmaster.Job)

timestamp (SCons.Node.FS.FileNodeInfo attribute)

TimeStats (class in SCons.Util.stats)

title() (SCons.Subst.CmdStringHolder method)

tm_trace_node() (SCons.Taskmaster.Taskmaster method)

to_bytes() (in module SCons.Util.sctypes)

to_str() (in module SCons.Util.sctypes)

to_String() (in module SCons.Util.sctypes)

to_String_for_signature() (in module SCons.Util.sctypes)

to_String_for_subst() (in module SCons.Util.sctypes)

to_Text() (in module SCons.Util.sctypes)

Tool (class in bin.SConsDoc)

(class in SCons.Tool)

Tool() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

tool_list() (in module SCons.Tool)

ToolInitializer (class in SCons.Tool)

ToolInitializerMethod (class in SCons.Tool)

ToolQtDeprecatedWarning

total_times() (SCons.Util.stats.TimeStats method)

touch_func() (in module SCons.Defaults)

Trace() (in module SCons.Debug)

trace_message() (SCons.SConf.SConfBuildTask method)

(SCons.Script.Main.BuildTask method) (SCons.Script.Main.CleanTask method) (SCons.Script.Main.QuestionTask method) (SCons.Taskmaster.AlwaysTask method) (SCons.Taskmaster.Job.NewParallel method) (SCons.Taskmaster.OutOfDateTask method) (SCons.Taskmaster.Task method)

translate() (SCons.Subst.CmdStringHolder method)

TreeFactory (class in bin.SConsDoc)

TreePrinter (class in SCons.Script.Main)

TryAction() (SCons.SConf.CheckContext method)

(SCons.SConf.SConfBase method)

TryBuild() (SCons.SConf.CheckContext method) (SCons.SConf.SConfBase method)

TryCompile() (SCons.SConf.CheckContext method)

(SCons.SConf.SConfBase method)

TryLink() (SCons.SConf.CheckContext method)

(SCons.SConf.SConfBase method)

TryRun() (SCons.SConf.CheckContext method)

(SCons.SConf.SConfBase method)

TSList (class in SCons.Executor)

TSObject (class in SCons.Executor)

tupleize() (SCons.cpp.DumbPreProcessor method)

(SCons.cpp.PreProcessor method) (SCons.Scanner.C.SConsCPPConditionalScanner method) (SCons.Scanner.C.SConsCPPScanner method)

two_arg_commands (SCons.Scanner.LaTeX.LaTeX attribute)

TYPE_CHECKER (SCons.Script.SConsOptions.SConsOption attribute)

TYPED_ACTIONS (SCons.Script.SConsOptions.SConsOption attribute)

TYPES (SCons.Script.SConsOptions.SConsOption attribute)

U

Unbuffered (class in SCons.Util)

undoc_header (SCons.Script.Interactive.SConsInteractiveCmd attribute)

unique() (in module SCons.Util)

UniqueList (class in SCons.Util)

uniquer_hashables() (in module SCons.Util)

UnknownVariables() (SCons.Variables.Variables method)

unlink() (SCons.Node.FS.FS method)

(SCons.Node.FS.LocalFS method)

UnlinkFunc() (in module SCons.Node.FS)

unlock() (SCons.Taskmaster.Job.NewParallel.FakeLock method)

up() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

update() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method)

(SCons.Builder.DictEmitter method)

(SCons.Builder.OverrideWarner method) (SCons.Environment.BuilderDict method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Node.Alias.AliasNodeInfo method) (SCons.Node.FS.DirNodeInfo method) (SCons.Node.FS.FileNodeInfo method) (SCons.Node.NodeInfoBase method) (SCons.Node.Python.ValueNodeInfo method) (SCons.Util.Selector method)

Update() (SCons.Variables.Variables method)

updrive() (in module SCons.Util)

upper() (SCons.Subst.CmdStringHolder method)

use_rawinput (SCons.Script.Interactive.SConsInteractiveCmd attribute)

UserError

usesTime() (SCons.Util.DispatchingFormatter method)

V

validate_all_xml() (in module bin.SConsDoc)

validate_CacheDir_class() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

ValidateOptions() (in module SCons.Script.Main)

validateXml() (bin.SConsDoc.TreeFactory static method)

validator (SCons.Variables.Variable attribute)

Value (class in SCons.Node.Python)

Value() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

Value.Attrs (class in SCons.Node.Python)

ValueBuildInfo (class in SCons.Node.Python)

ValueNodeInfo (class in SCons.Node.Python)

values (SCons.Script.Main.FakeOptionParser attribute)

values() (SCons.Builder.CallableSelector method)

(SCons.Builder.DictCmdGenerator method) (SCons.Builder.DictEmitter method) (SCons.Builder.OverrideWarner method) (SCons.dblite._Dblite method) (SCons.Environment.Base method) (SCons.Environment.BuilderDict method) (SCons.Environment.OverrideEnvironment method) (SCons.Environment.SubstitutionEnvironment method) (SCons.Node.Alias.AliasNameSpace method) (SCons.Script.SConscript.SConsEnvironment method) (SCons.Util.Selector method)

ValueWithMemo() (in module SCons.Node.Python)

Variable (class in SCons.Variables)

Variable_Method_Caller (class in SCons.Defaults)

Variables (class in SCons.Variables)

Variables() (in module SCons.Script)

variant_dir_target_climb() (SCons.Node.FS.FS method)

variant_dirs (SCons.Node.FS.Dir attribute)

(SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute)

VariantDir() (SCons.Environment.Base method)

(SCons.Environment.OverrideEnvironment method) (SCons.Node.FS.FS method) (SCons.Script.SConscript.SConsEnvironment method)

version_string() (in module SCons.Script.Main)

Virtualenv() (in module SCons.Platform.virtualenv)

visited() (SCons.Node.Alias.Alias method)

(SCons.Node.FS.Base method) (SCons.Node.FS.Dir method) (SCons.Node.FS.Entry method) (SCons.Node.FS.File method) (SCons.Node.FS.RootDir method) (SCons.Node.Node method) (SCons.Node.Python.Value method)

VisualCMissingWarning

VisualStudioMissingWarning

VisualVersionMismatch

W

wait() (SCons.Taskmaster.Job.NewParallel.FakeCondition method)

wait_for_process_to_die() (in module SCons.Util)

waiting_parents (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

waiting_s_e (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

walk() (SCons.Node.FS.Dir method)

(SCons.Node.FS.RootDir method)

Walker (class in SCons.Node)

warn() (in module SCons.Warnings)

(SCons.Builder.OverrideWarner method)

warning() (bin.SConsDoc.Libxml2ValidityHandler method)

warningAsException() (in module SCons.Warnings)

WarningOnByDefault

were_interrupted() (SCons.Taskmaster.Job.Jobs method)

WhereIs() (in module SCons.Util)

(SCons.Environment.Base method) (SCons.Environment.OverrideEnvironment method) (SCons.Script.SConscript.SConsEnvironment method)

will_not_build() (SCons.Taskmaster.Taskmaster method)

with_traceback() (SCons.Node.FS.EntryProxyAttributeError method) (SCons.Node.FS.FileBuildInfoFileToCsigMappingEr ror method) (SCons.SConf.ConfigureCacheError method) (SCons.SConf.ConfigureDryRunError method) (SCons.SConf.SConfError method) (SCons.SConf.SConfWarning method) (SCons.Script.Main.SConsPrintHelpException method) (SCons.Script.SConscript.SConscriptReturn method) (SCons.Script.SConsOptions.SConsBadOptionError method) (SCons.Util._NoError method) (SCons.Util.filelock.SConsLockFailure method)

wkids (SCons.Node.Alias.Alias attribute)

(SCons.Node.FS.Base attribute) (SCons.Node.FS.Dir attribute) (SCons.Node.FS.Entry attribute) (SCons.Node.FS.File attribute) (SCons.Node.FS.RootDir attribute) (SCons.Node.Node attribute) (SCons.Node.Python.Value attribute)

Worker (class in SCons.Taskmaster.Job)

write() (in module SCons.SConsign)

(SCons.Node.Python.Value method) (SCons.SConf.Streamer method) (SCons.SConsign.DB method) (SCons.SConsign.DirFile method) (SCons.Script.Main.Progressor method) (SCons.Util.Unbuffered method)

write_scons_stats_file() (in module SCons.Util.stats)

writeGenTree() (bin.SConsDoc.TreeFactory static method)

writelines() (SCons.SConf.Streamer method)

(SCons.Util.Unbuffered method)

writeTree() (bin.SConsDoc.TreeFactory static method)

X

xmlschema (bin.SConsDoc.TreeFactory attribute)

Z

zfill() (SCons.Subst.CmdStringHolder method) Python Module Index

b

bin

bin.SConsDoc

bin.SConsExamples

s

SCons

SCons.Action

SCons.Builder

SCons.CacheDir

SCons.compat

SCons.Conftest

SCons.cpp

SCons.dblite

SCons.Debug

SCons.Defaults

SCons.Environment

SCons.Errors

SCons.Executor

SCons.exitfuncs

SCons.Memoize

SCons.Node

SCons.Node.Alias

SCons.Node.FS

SCons.Node.Python

SCons.PathList

SCons.Platform

SCons.Platform.aix

SCons.Platform.cygwin

SCons.Platform.darwin

SCons.Platform.hpux

SCons.Platform.irix

SCons.Platform.mingw

SCons.Platform.os2

SCons.Platform.posix

SCons.Platform.sunos

SCons.Platform.virtualenv

SCons.Platform.win32

SCons.Scanner

SCons.Scanner.C

SCons.Scanner.D

SCons.Scanner.Dir

SCons.Scanner.Fortran

SCons.Scanner.IDL

SCons.Scanner.Java

SCons.Scanner.LaTeX

SCons.Scanner.Prog

SCons.Scanner.RC

SCons.Scanner.SWIG

SCons.SConf

SCons.SConsign

SCons.Script

SCons.Script.Interactive

SCons.Script.Main

SCons.Script.SConscript

SCons.Script.SConsOptions

SCons.Subst

SCons.Taskmaster

SCons.Taskmaster.Job

SCons.Tool

SCons.Util

SCons.Util.envs

SCons.Util.filelock

SCons.Util.hashes

SCons.Util.sctypes

SCons.Util.stats

SCons.Variables

SCons.Variables.BoolVariable

SCons.Variables.EnumVariable

SCons.Variables.ListVariable

SCons.Variables.PackageVariable

SCons.Variables.PathVariable

SCons.Warnings
