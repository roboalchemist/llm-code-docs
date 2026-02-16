# Swift Argument Parser - API Reference

Source: https://github.com/apple/swift-argument-parser

## Core Concepts

Swift Argument Parser provides a declarative, type-safe way to parse command-line arguments. The library is built on Swift's property wrappers and uses the following core types:

## Main Types

### ParsableCommand Protocol

The primary protocol for defining a command-line tool. Implement this protocol and decorate your struct with `@main` to create a command-line application.

```swift
@main
struct MyCommand: ParsableCommand {
    // Property declarations with wrappers
    // Implement run() method
}
```

### AsyncParsableCommand Protocol

Async version of ParsableCommand for modern async/await code patterns.

```swift
@main
struct MyAsyncCommand: AsyncParsableCommand {
    // Property declarations with wrappers
    // Implement run() async throws method
}
```

### ParsableArguments Protocol

Protocol for defining a group of related arguments that can be reused across multiple commands.

## Property Wrappers

### @Argument

Declares a positional argument (required by default).

```swift
@Argument(help: "The input file")
var inputFile: String

@Argument(help: "Output options")
var output: [String] = []
```

### @Option

Declares a named option with values (--name value).

```swift
@Option(name: .short, help: "Short flag")
var x: Int?

@Option(name: .shortAndLong, help: "Both short and long")
var count: Int = 1

@Option(name: .customLong("verbose"), help: "Custom name")
var verboseLevel: String
```

### @Flag

Declares a boolean flag (--flag sets it to true).

```swift
@Flag(help: "Enable verbose mode")
var verbose = false

@Flag(name: .shortAndLong, help: "Help flag")
var help = false
```

### @OptionGroup

Groups related options together for better organization.

```swift
@OptionGroup
var verbosity: VerbosityOptions
```

## CommandConfiguration

Configure command behavior and metadata:

```swift
struct MyCommand: ParsableCommand {
    static let configuration = CommandConfiguration(
        commandName: "my-tool",
        abstract: "A brief description",
        discussion: "Longer discussion text",
        version: "1.0.0",
        shouldDisplayRepeatableOptionsWithoutArguments: false
    )
}
```

## Subcommands

Create hierarchical command structures:

```swift
@main
struct ToolKit: ParsableCommand {
    static let configuration = CommandConfiguration(
        subcommands: [Build.self, Test.self, Deploy.self]
    )
}

struct Build: ParsableCommand {
    // Build command implementation
}
```

## Error Handling

ArgumentParser provides automatic validation and helpful error messages:

```swift
struct MyCommand: ParsableCommand {
    @Argument
    var count: Int
    
    @Argument
    var output: String
    
    mutating func validate() throws {
        // Custom validation logic
        if count < 0 {
            throw ValidationError("count must be positive")
        }
    }
}
```

## Help Generation

Automatic help text is generated from your property declarations:

```bash
$ tool --help
USAGE: tool [--count <count>] <input>

ARGUMENTS:
  <input>                 The input file.

OPTIONS:
  --count <count>         Number of iterations (default: 1)
  -h, --help              Show help for this command.
```

## Completion Support

Generate shell completions for bash, zsh, and fish:

```swift
struct MyCommand: ParsableCommand {
    @Option(completion: .list(["option1", "option2"]))
    var choice: String?
}
```

## Variable Expansion

Commands can use environment variables:

```swift
@Option
var configPath: String? = nil

@Option(envKey: "MY_TOOL_CONFIG")
var altConfigPath: String?
```

## Installation

Add to your Package.swift:

```swift
.package(url: "https://github.com/apple/swift-argument-parser", from: "1.3.0")
```

## Examples

See the Examples directory for complete working examples:

- `repeat` - Basic argument and flag usage
- `roll` - Simple command-line utility
- `math` - Nested commands and subcommands
- `count-lines` - Async/await implementation

## More Information

- [SwiftPackageIndex Documentation](https://swiftpackageindex.com/apple/swift-argument-parser/documentation/argumentparser)
- [GitHub Repository](https://github.com/apple/swift-argument-parser)
- [Swift Evolution Proposal (SE-0323)](https://github.com/apple/swift-evolution/blob/main/proposals/0323-swiftpm-command-plugins.md)
