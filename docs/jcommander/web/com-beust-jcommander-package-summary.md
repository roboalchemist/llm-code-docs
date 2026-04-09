# Package com.beust.jcommander






- 

Interface Summary 

Interface
Description



IDefaultProvider

Allows the specification of default values.



IParameterizedParser

Thin interface allows the Parameterized parsing mechanism, which reflects an object to find the 
 JCommander annotations, to be replaced at runtime for cases where the source code cannot
 be directly annotated with JCommander annotations, but may have other annotations such as 
 JSON annotations that can be used to reflect as JCommander parameters.



IParameterValidator

The class used to validate parameters.



IParameterValidator2
 


IStringConverter<T>

An interface that converts strings to any arbitrary type.



IStringConverterFactory

A factory for IStringConverter.



IStringConverterInstanceFactory

A factory to create `IStringConverter` instances.



IUsageFormatter

A formatter for help messages.



IValueValidator<T>
 


IVariableArity

Must be implemented by argument classes that contain at least one
 \@Parameter with "variableArity = true".






- 

Class Summary 

Class
Description



DefaultUsageFormatter

The default usage formatter.



FuzzyMap

Helper class to perform fuzzy key look ups: looking up case insensitive or
 abbreviated keys.



JCommander

The main class for JCommander.



JCommander.Builder
 


JCommander.ProgramName

Encapsulation of either a main application or an individual command.



ParameterDescription
 


Parameterized

Encapsulate a field or a method annotated with @Parameter or @DynamicParameter



StringKey
 


Strings
 


UnixStyleUsageFormatter

A unix-style usage formatter.



WrappedParameter

Encapsulates the operations common to @Parameter and @DynamicParameter






- 

Exception Summary 

Exception
Description



MissingCommandException

Thrown when a command was expected.



ParameterException

The main exception that JCommand will throw when something goes wrong while
 parsing parameters.






- 

Annotation Types Summary 

Annotation Type
Description



DynamicParameter
 


Parameter
 


Parameters

An annotation used to specify settings for parameter parsing.



ParametersDelegate

When applied to a field all of its child fields annotated
 with `Parameter` will be included during arguments
 parsing.



ResourceBundle
Deprecated.
use @Parameters



SubParameter