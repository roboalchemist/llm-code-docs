# Source: https://symfony.com/doc/8.0/components/expression_language.html

Title: The ExpressionLanguage Component (Symfony Docs)

URL Source: https://symfony.com/doc/8.0/components/expression_language.html

Markdown Content:
[Edit this page](https://github.com/symfony/symfony-docs/edit/8.0/components/expression_language.rst)

> The ExpressionLanguage component provides an engine that can compile and evaluate expressions. An expression is a one-liner that returns a value (mostly, but not limited to, Booleans).

[Installation](https://symfony.com/doc/8.0/components/expression_language.html#installation "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

Note

If you install this component outside of a Symfony application, you must require the `vendor/autoload.php` file in your code to enable the class autoloading mechanism provided by Composer. Read [this article](https://symfony.com/doc/current/components/using_components.html) for more details.

[How can the Expression Language Help Me?](https://symfony.com/doc/8.0/components/expression_language.html#how-can-the-expression-language-help-me "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The purpose of the component is to allow users to use expressions inside configuration for more complex logic. For example, the Symfony Framework uses expressions in security, for validation rules and in route matching.

Besides using the component in the framework itself, the ExpressionLanguage component is a perfect candidate for the foundation of a _business rule engine_. The idea is to let the webmaster of a website configure things in a dynamic way without using PHP and without introducing security problems:

Expressions can be seen as a very restricted PHP sandbox and are less vulnerable to external injections because you must explicitly declare which variables are available in an expression (but you should still sanitize any data given by end users and passed to expressions).

[Usage](https://symfony.com/doc/8.0/components/expression_language.html#usage "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------

The ExpressionLanguage component can compile and evaluate expressions. Expressions are one-liners that often return a Boolean, which can be used by the code executing the expression in an `if` statement. A simple example of an expression is `1 + 2`. You can also use more complicated expressions, such as `someArray[3].someMethod('bar')`.

The component provides 2 ways to work with expressions:

* **evaluation**: the expression is evaluated without being compiled to PHP;
* **compile**: the expression is compiled to PHP, so it can be cached and evaluated.

The main class of the component is [ExpressionLanguage](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php "Symfony\Component\ExpressionLanguage\ExpressionLanguage"):

### [Parsing and Linting Expressions](https://symfony.com/doc/8.0/components/expression_language.html#parsing-and-linting-expressions "Permalink to this headline")

The ExpressionLanguage component provides a way to parse and lint expressions. The [parse()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20parse "Symfony\Component\ExpressionLanguage\ExpressionLanguage::parse()") method returns a [ParsedExpression](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ParsedExpression.php "Symfony\Component\ExpressionLanguage\ParsedExpression") instance that can be used to inspect and manipulate the expression. The [lint()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20lint "Symfony\Component\ExpressionLanguage\ExpressionLanguage::lint()"), on the other hand, throws a [SyntaxError](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/SyntaxError.php "Symfony\Component\ExpressionLanguage\SyntaxError") if the expression is not valid:

The behavior of these methods can be configured with some flags defined in the [Parser](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/Parser.php "Symfony\Component\ExpressionLanguage\Parser") class:

* `IGNORE_UNKNOWN_VARIABLES`: don't throw an exception if a variable is not defined in the expression;
* `IGNORE_UNKNOWN_FUNCTIONS`: don't throw an exception if a function is not defined in the expression.

This is how you can use these flags:

[Caching](https://symfony.com/doc/8.0/components/expression_language.html#caching "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

The ExpressionLanguage component provides a [compile()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20compile "Symfony\Component\ExpressionLanguage\ExpressionLanguage::compile()") method to be able to cache the expressions in plain PHP. But internally, the component also caches the parsed expressions, so duplicated expressions can be compiled/evaluated quicker.

#### [The Workflow](https://symfony.com/doc/8.0/components/expression_language.html#the-workflow "Permalink to this headline")

Both [evaluate()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20evaluate "Symfony\Component\ExpressionLanguage\ExpressionLanguage::evaluate()") and `compile()` need to do some things before each can provide the return values. For `evaluate()`, this overhead is even bigger.

Both methods need to tokenize and parse the expression. This is done by the [parse()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20parse "Symfony\Component\ExpressionLanguage\ExpressionLanguage::parse()") method. It returns a [ParsedExpression](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ParsedExpression.php "Symfony\Component\ExpressionLanguage\ParsedExpression"). Now, the `compile()` method just returns the string conversion of this object. The `evaluate()` method needs to loop through the "nodes" (pieces of an expression saved in the `ParsedExpression`) and evaluate them dynamically.

To save time, the `ExpressionLanguage` caches the `ParsedExpression` so it can skip the tokenization and parsing steps with duplicate expressions. The caching is done by a PSR-6 [CacheItemPoolInterface](https://github.com/php-fig/cache/blob/master/src/CacheItemPoolInterface.php) instance (by default, it uses an [ArrayAdapter](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/Cache/Adapter/ArrayAdapter.php "Symfony\Component\Cache\Adapter\ArrayAdapter")). You can customize this by creating a custom cache pool or using one of the available ones and injecting this using the constructor:

See also

See the [The Cache Component](https://symfony.com/doc/current/components/cache.html) documentation for more information about available cache adapters.

#### [Using Parsed and Serialized Expressions](https://symfony.com/doc/8.0/components/expression_language.html#using-parsed-and-serialized-expressions "Permalink to this headline")

Both `evaluate()` and `compile()` can handle `ParsedExpression` and `SerializedParsedExpression`:

[AST Dumping and Editing](https://symfony.com/doc/8.0/components/expression_language.html#ast-dumping-and-editing "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------

It's difficult to manipulate or inspect the expressions created with the ExpressionLanguage component, because the expressions are plain strings. A better approach is to turn those expressions into an AST. In computer science, [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (_Abstract Syntax Tree_) is _"a tree representation of the structure of source code written in a programming language"_. In Symfony, an ExpressionLanguage AST is a set of nodes that contain PHP classes representing the given expression.

#### [Dumping the AST](https://symfony.com/doc/8.0/components/expression_language.html#dumping-the-ast "Permalink to this headline")

Call the [getNodes()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20getNodes "Symfony\Component\ExpressionLanguage\ExpressionLanguage::getNodes()") method after parsing any expression to get its AST:

#### [Manipulating the AST](https://symfony.com/doc/8.0/components/expression_language.html#manipulating-the-ast "Permalink to this headline")

The nodes of the AST can also be dumped into a PHP array of nodes to allow manipulating them. Call the [toArray()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20toArray "Symfony\Component\ExpressionLanguage\ExpressionLanguage::toArray()") method to turn the AST into an array:

[Extending the ExpressionLanguage](https://symfony.com/doc/8.0/components/expression_language.html#extending-the-expressionlanguage "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The ExpressionLanguage can be extended by adding custom functions. For instance, in the Symfony Framework, the security has custom functions to check the user's role.

#### [Registering Functions](https://symfony.com/doc/8.0/components/expression_language.html#registering-functions "Permalink to this headline")

Functions are registered on each specific `ExpressionLanguage` instance. That means the functions can be used in any expression executed by that instance.

To register a function, use [register()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20register "Symfony\Component\ExpressionLanguage\ExpressionLanguage::register()"). This method has 3 arguments:

* **name** - The name of the function in an expression;
* **compiler** - A function executed when compiling an expression using the function;
* **evaluator** - A function executed when the expression is evaluated.

Example:

In addition to the custom function arguments, the **evaluator** is passed an `arguments` variable as its first argument, which is equal to the second argument of `evaluate()` (e.g. the "values" when evaluating an expression).

#### [Using Expression Providers](https://symfony.com/doc/8.0/components/expression_language.html#using-expression-providers "Permalink to this headline")

When you use the `ExpressionLanguage` class in your library, you often want to add custom functions. To do so, you can create a new expression provider by creating a class that implements [ExpressionFunctionProviderInterface](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionFunctionProviderInterface.php "Symfony\Component\ExpressionLanguage\ExpressionFunctionProviderInterface").

This interface requires one method: [getFunctions()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionFunctionProviderInterface.php#:~:text=function%20getFunctions "Symfony\Component\ExpressionLanguage\ExpressionFunctionProviderInterface::getFunctions()"), which returns an array of expression functions (instances of [ExpressionFunction](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionFunction.php "Symfony\Component\ExpressionLanguage\ExpressionFunction")) to register:

Tip

To create an expression function from a PHP function with the [fromPhp()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionFunction.php#:~:text=function%20fromPhp "Symfony\Component\ExpressionLanguage\ExpressionFunction::fromPhp()") static method:

Namespaced functions are supported, but they require a second argument to define the name of the expression:

You can register providers using [registerProvider()](https://github.com/symfony/symfony/blob/8.0/src/Symfony/Component/ExpressionLanguage/ExpressionLanguage.php#:~:text=function%20registerProvider "Symfony\Component\ExpressionLanguage\ExpressionLanguage::registerProvider()") or by using the second argument of the constructor:

Tip

It is recommended to create your own `ExpressionLanguage` class in your library. Now you can add the extension by overriding the constructor:

This work, including the code samples, is licensed under a [Creative Commons BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) license.
