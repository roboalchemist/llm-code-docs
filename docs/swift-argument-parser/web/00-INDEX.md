# Swift Argument Parser Documentation

**Project:** Apple's Swift Argument Parser
**Repository:** https://github.com/apple/swift-argument-parser
**Latest Version:** 1.3.0+
**Minimum Swift Version:** 5.7

## Overview

Swift Argument Parser is Apple's official library for building type-safe, declarative command-line tools in Swift. It provides a modern, property-wrapper-based API for parsing command-line arguments with automatic help text generation and validation.

## Key Features

- **Type-Safe**: Full type safety with Swift's type system
- **Declarative**: Property wrapper-based declaration of arguments and options
- **Auto-Generated Help**: Automatic help text from your property declarations
- **Validation**: Built-in and custom validation support
- **Subcommands**: Hierarchical command structures
- **Completions**: Shell completion generation (bash, zsh, fish)
- **Modern Async/Await Support**: AsyncParsableCommand for async code
- **Environment Variables**: Support for environment variable expansion
- **Customizable**: Rich configuration options for commands and arguments

## What's Included

1. **01-README.md** - Getting started guide with basic usage examples
2. **02-CHANGELOG.md** - Complete version history and feature updates
3. **03-CONTRIBUTING.md** - Contributing guidelines
4. **04-EXAMPLES.md** - Four complete working examples (repeat, roll, math, count-lines)
5. **05-PACKAGE-MANIFEST.md** - Swift package manifest and configuration
6. **06-API-REFERENCE.md** - Comprehensive API reference guide

## Quick Start

```swift
import ArgumentParser

@main
struct Repeat: ParsableCommand {
    @Flag(help: "Include a counter with each repetition.")
    var includeCounter = false

    @Option(name: .shortAndLong, help: "How many times to repeat 'phrase'.")
    var count: Int? = nil

    @Argument(help: "The phrase to repeat.")
    var phrase: String

    mutating func run() throws {
        let repeatCount = count ?? 2

        for i in 1...repeatCount {
            if includeCounter {
                print("\(i): \(phrase)")
            } else {
                print(phrase)
            }
        }
    }
}
```

## Core Components

- **ParsableCommand**: Protocol for creating command-line commands
- **AsyncParsableCommand**: Async version with async/await support
- **@Argument**: Property wrapper for positional arguments
- **@Option**: Property wrapper for named options (--name value)
- **@Flag**: Property wrapper for boolean flags (--flag)
- **@OptionGroup**: Group related options together
- **CommandConfiguration**: Configure command metadata and behavior

## Use Cases

- Building command-line tools in Swift
- Creating shell utilities
- Implementing CLI applications for macOS
- Developing cross-platform command-line tools
- Creating Xcode plugins and build tools

## Links

- [GitHub Repository](https://github.com/apple/swift-argument-parser)
- [SwiftPackageIndex Docs](https://swiftpackageindex.com/apple/swift-argument-parser/documentation/argumentparser)
- [Swift Package Index Getting Started](https://swiftpackageindex.com/apple/swift-argument-parser/documentation/argumentparser/gettingstarted)
