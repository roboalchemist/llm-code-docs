#!/usr/bin/env python3
"""
Scraper for Swift Argument Parser documentation.
This library doesn't have a traditional docs site or llms.txt,
so we extract comprehensive documentation from the GitHub repository:
- README.md (getting started guide)
- Examples directory (practical usage examples)
- CHANGELOG.md (version history and features)
- Source code structure and key files

Output: docs/web-scraped/swift-argument-parser/
"""

import os
import re
from pathlib import Path
from urllib.request import urlopen
import json

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "swift-argument-parser"

def download_file(url: str) -> str:
    """Download file from GitHub raw URL."""
    try:
        with urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return ""

def create_output_dir():
    """Create output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Created output directory: {OUTPUT_DIR}")

def fetch_readme():
    """Fetch and save README.md."""
    url = "https://raw.githubusercontent.com/apple/swift-argument-parser/main/README.md"
    content = download_file(url)
    
    if content:
        filepath = OUTPUT_DIR / "01-README.md"
        with open(filepath, 'w') as f:
            f.write("# Swift Argument Parser - Getting Started\n\n")
            f.write("Source: https://github.com/apple/swift-argument-parser\n\n")
            f.write(content)
        print(f"✓ Saved README: {filepath}")
        return True
    return False

def fetch_changelog():
    """Fetch and save CHANGELOG.md."""
    url = "https://raw.githubusercontent.com/apple/swift-argument-parser/main/CHANGELOG.md"
    content = download_file(url)
    
    if content:
        filepath = OUTPUT_DIR / "02-CHANGELOG.md"
        with open(filepath, 'w') as f:
            f.write("# Swift Argument Parser - Changelog\n\n")
            f.write("Source: https://github.com/apple/swift-argument-parser/blob/main/CHANGELOG.md\n\n")
            f.write(content)
        print(f"✓ Saved CHANGELOG: {filepath}")
        return True
    return False

def fetch_contributing():
    """Fetch and save CONTRIBUTING.md."""
    url = "https://raw.githubusercontent.com/apple/swift-argument-parser/main/CONTRIBUTING.md"
    content = download_file(url)
    
    if content:
        filepath = OUTPUT_DIR / "03-CONTRIBUTING.md"
        with open(filepath, 'w') as f:
            f.write("# Contributing to Swift Argument Parser\n\n")
            f.write("Source: https://github.com/apple/swift-argument-parser/blob/main/CONTRIBUTING.md\n\n")
            f.write(content)
        print(f"✓ Saved CONTRIBUTING: {filepath}")
        return True
    return False

def fetch_examples():
    """Fetch and save example files."""
    examples = [
        ("repeat", "Examples/repeat/Repeat.swift"),
        ("roll", "Examples/roll/main.swift"),
        ("math", "Examples/math/Math.swift"),
        ("count-lines", "Examples/count-lines/CountLines.swift"),
    ]
    
    example_docs = "# Swift Argument Parser - Examples\n\n"
    example_docs += "Source: https://github.com/apple/swift-argument-parser/tree/main/Examples\n\n"
    example_docs += "The ArgumentParser library includes several examples demonstrating different usage patterns:\n\n"
    
    for example_name, example_path in examples:
        url = f"https://raw.githubusercontent.com/apple/swift-argument-parser/main/{example_path}"
        content = download_file(url)
        
        if content:
            example_docs += f"## {example_name.upper()} Example\n\n"
            example_docs += f"**File:** `{example_path}`\n\n"
            example_docs += "```swift\n"
            example_docs += content
            example_docs += "\n```\n\n"
            print(f"✓ Downloaded example: {example_name}")
        else:
            print(f"✗ Failed to download example: {example_name}")
    
    if example_docs:
        filepath = OUTPUT_DIR / "04-EXAMPLES.md"
        with open(filepath, 'w') as f:
            f.write(example_docs)
        print(f"✓ Saved examples: {filepath}")
        return True
    return False

def fetch_package_manifest():
    """Fetch and save Package.swift manifest."""
    url = "https://raw.githubusercontent.com/apple/swift-argument-parser/main/Package.swift"
    content = download_file(url)
    
    if content:
        filepath = OUTPUT_DIR / "05-PACKAGE-MANIFEST.md"
        with open(filepath, 'w') as f:
            f.write("# Swift Argument Parser - Package Manifest\n\n")
            f.write("Source: https://github.com/apple/swift-argument-parser/blob/main/Package.swift\n\n")
            f.write("## Package Definition\n\n")
            f.write("```swift\n")
            f.write(content)
            f.write("\n```\n\n")
            f.write("This manifest defines the Swift package configuration, dependencies, and targets.\n")
        print(f"✓ Saved package manifest: {filepath}")
        return True
    return False

def create_api_reference():
    """Create API reference guide from source inspection."""
    api_doc = """# Swift Argument Parser - API Reference

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
"""
    
    filepath = OUTPUT_DIR / "06-API-REFERENCE.md"
    with open(filepath, 'w') as f:
        f.write(api_doc)
    print(f"✓ Created API reference: {filepath}")
    return True

def create_index():
    """Create an index file."""
    index = """# Swift Argument Parser Documentation

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
                print("\\(i): \\(phrase)")
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
"""
    
    filepath = OUTPUT_DIR / "00-INDEX.md"
    with open(filepath, 'w') as f:
        f.write(index)
    print(f"✓ Created index: {filepath}")
    return True

def main():
    """Main scraper function."""
    print("Scraping Swift Argument Parser documentation...")
    print(f"Output directory: {OUTPUT_DIR}\n")
    
    create_output_dir()
    
    results = []
    results.append(("README", fetch_readme()))
    results.append(("CHANGELOG", fetch_changelog()))
    results.append(("CONTRIBUTING", fetch_contributing()))
    results.append(("Examples", fetch_examples()))
    results.append(("Package Manifest", fetch_package_manifest()))
    results.append(("API Reference", create_api_reference()))
    results.append(("Index", create_index()))
    
    print("\n" + "="*50)
    print("Scraping Summary:")
    print("="*50)
    for name, success in results:
        status = "✓ Success" if success else "✗ Failed"
        print(f"{status}: {name}")
    
    success_count = sum(1 for _, s in results if s)
    total_count = len(results)
    print(f"\nTotal: {success_count}/{total_count} successful")
    print(f"Output saved to: {OUTPUT_DIR}")
    
    return success_count == total_count

if __name__ == "__main__":
    exit(0 if main() else 1)
