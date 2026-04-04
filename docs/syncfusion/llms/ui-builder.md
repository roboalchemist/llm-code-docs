# Source: https://docs.syncfusion.com/code-studio/ui-builder.md

# UI Builder

## Overview

UI Builder is a specialized tool that provides essential information for building user interfaces with Syncfusion components. When you describe what you want to create, it automatically analyzes your request and returns the technical guidance to the Code Studio for implementation.

### What UI Builder Provides

- **Component Information**: Lists of available Syncfusion components for your platform
- **Implementation Context**: Platform-specific guidelines and best practices  
- **Multi-Platform Support**: Works across 14 different development frameworks

### Key Benefits

- **Eliminates Documentation Search**: Get relevant component information instantly
- **Ensures Accuracy**: Validates component availability for your specific platform
- **Accelerates Development**: Reduces trial-and-error coding with proven patterns
- **Platform Optimization**: Delivers framework-specific implementation guidance

## Quick Start

### UI Builder Setup

By default, the UI Builder tool is enabled in Code Studio. You can verify this by following these steps: 

1. **Access Configure Tools**: Open the Configure Tools panel in Code Studio.

    <img src="./ui-builder-images/tool.png" alt="UI Builder Tool" />

2. **Verify UI Builder Tool**: Confirm that the UiBuilder tool is enabled in the tools list.

    <img src="./ui-builder-images/toolenable.png" alt="UI Builder Tool Enable" />

### Basic Usage

To build with Syncfusion, just describe your requirement in this format:

```
Create a [feature description] for [platform] using Syncfusion components with [requirements]
```

**Example:**
```
Create a customer dashboard for React using Syncfusion components with data grid, charts, and export functionality.
```
<img src="./ui-builder-images/context.png" alt="UI Builder Context" />

### Required Elements

For UI Builder to activate and provide accurate results:

1. **"Syncfusion" keyword**: This keyword activates the UI Builder tool
2. **Platform Specification**: Name your framework (React, Angular, Vue, Blazor, etc.)
3. **Functionality Description**: Explain what you want to build and key features needed

### How UI Builder Works

UI Builder operates in two modes:

#### Platform Info Mode
UI Builder retrieves a comprehensive list of available Syncfusion components for your specific platform.

#### Context Mode
UI Builder prepares detailed implementation guidance including system prompts, layout configuration, and component metadata.

<img src="./ui-builder-images/buildworks.png" alt="mode" />

### Syncfusion License Setup

After implementing features with Syncfusion components, proper licensing is required:

**Trial Users:**
- Register license key from [Syncfusion Account Portal](https://www.syncfusion.com/account/downloads)
- Required for trial installations and NuGet packages from nuget.org

**Licensed Users:**
- Licensed installer includes automatic license registration
- No additional license key registration required

**License Key Registration:**
Add the license key to your application startup code to avoid licensing popups during development and production.

## Supported Platforms

UI Builder supports 14 platforms with varying component libraries:

| Platform | Components Available | 
|----------|---------------------|
| WinForms | 121 components |
| Blazor | 102 components |
| ASP.NET Core | 99 components |
| Angular | 98 components |
| TypeScript | 98 components |
| Vue.js | 98 components |
| WPF | 97 components |
| JavaScript | 97 components |
| React | 94 components |
| MAUI | 74 components |
| WinUI | 41 components |
| Flutter | 25 components |
| PureReact | 17 components |

## Best Practices

- **Be Specific**:  Use "Create a customer form with validation" instead of "Create a form"
- **Include Features**: Mention export, search, responsive design, validation
- **Name Platform Clearly**: Use Syncfusion supported platform like "React" and "JavaScript"

## Key Limitations

- **15 component maximum** per request
- **Exact component names** required (case-sensitive)
- **Platform-specific** component availability varies

## Troubleshooting

**UI Builder Not Activating**: Include "Syncfusion" keyword and specify platform explicitly (React, Angular, etc.)

**Wrong Platform Detection**: Use exact platform names early in request like "React" or "JavaScript"

**Generic Response**: Be more specific about functionality, include business context and specific features needed

**Component Not Available**: Check Supported Platforms table or request component list for your platform

## FAQ

**Does UI Builder create complete applications?**

No, UI Builder provides implementation guidance and component information. Code Studio uses this information to build complete applications with appropriate Syncfusion components.

**Can I modify the code that Code Studio creates?**

Yes, all code created by Code Studio using UI Builder guidance can be customized and extended to match your specific requirements.

**Which AI models work best with UI Builder?**

GPT and Claude provide optimal results when Code Studio implements features using UI Builder guidance. Configure your preferred model in Code Studio settings.

**Are there limits on UI Builder requests?**

UI Builder processes up to 15 components maximum per request.

**Can UI Builder work with existing projects?**

Yes, UI Builder provides component information that Code Studio can use to add Syncfusion features to existing applications.