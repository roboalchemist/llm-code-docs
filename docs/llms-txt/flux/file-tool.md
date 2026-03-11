# Source: https://docs.flux.ai/reference/file-tool.md

# Flux File Tool

Flux includes a powerful file tool that allows you to extract specific information from datasheets and project files directly from the chat interface. This tool helps you quickly find the information you need without having to manually search through lengthy technical documents.

## Overview

The file tool enables you to:

- Search within datasheets and project files using natural language queries
- Extract specific information such as pin configurations, electrical characteristics, or mechanical dimensions
- Access information from both text content and tables within documents
- Get relevant excerpts without leaving your design workflow

![](https:\/\/uploads.developerhub.io\/prod\/86Yw\/wppf3jd3c1snsxqsqayzigoav89tozuweb3cciiey1yn5vlablfat7hyyuohx4hk.png)

## How to Use the File Tool

To search within datasheets or project files using Flux, use the `@file` tool in your query:

```none
@file What is the maximum operating temperature of the LM7805 regulator?

@file What are the pin assignments for the STM32F103 microcontroller?
```



When you use the `@file` tool, Flux will:

1. Process your query to understand what information you're looking for
2. Search through the relevant datasheet or file
3. Extract the most relevant information, including from tables if applicable
4. Present the information in a clear, readable format

## Attaching Files

To use the file tool with your own files, you need to attach them to the chat:

1. Click the paperclip icon in the chat input area
2. Select the file you want to attach (PDF, CSV, TXT, etc.)
3. Once uploaded, you can reference the file in your queries

For example, after attaching a datasheet:

```none
@file What is the recommended input voltage range in the attached datasheet?
```



## Search Technology

The file tool uses two complementary search methods to ensure you get the most relevant information:

### Vector Search

For files that have been previously processed, Flux uses vector search technology to find semantically relevant content. This allows it to understand the meaning behind your query and find information even when your query doesn't contain the exact words used in the document.

### Direct File Processing

For newly attached files or files hosted on Flux's CDN, Flux can download and process them directly, extracting both text content and table data to provide comprehensive answers to your queries.

## Example Queries

Here are some examples of how you can use the file tool:

### Finding Electrical Specifications

```none
@file What is the input voltage range for the LM317 regulator?

@file What is the maximum current rating for the IRLZ44N MOSFET?

@file What are the power dissipation capabilities of this component?
```



### Extracting Pin Information

```none
@file What are the I2C pins on the ESP32?

@file Show me the pinout diagram for the ATmega328P.

@file Which pins support PWM output on this microcontroller?
```



### Finding Mechanical Specifications

```none
@file What are the package dimensions of this component?

@file What is the recommended footprint for this part?

@file What is the mounting hole size for this connector?
```



## Tips for Effective File Searches

To get the most out of the file tool:

1. **Be specific in your queries** - Clearly state what information you're looking for and from which document.
2. **Reference specific sections** - If you know the section of the document, mention it in your query (e.g., "in the electrical characteristics section").
3. **Ask about tables directly** - If you're looking for tabular data, explicitly mention it (e.g., "show me the truth table for this logic gate").
4. **Use technical terminology** - Using the correct technical terms will help Flux find the most relevant information.

## Limitations

While the file tool is powerful, it has some limitations to be aware of:

- The tool may have difficulty with very complex tables or diagrams in PDFs
- Very large files may take longer to process
- Some file formats may not be fully supported
- The tool works best with text-based content and structured tables
- For scanned PDFs with poor OCR quality, information extraction may be limited

## Related Features

The file tool works well with other Flux capabilities:

- [Flux Documentation Search](/reference/documentation-search) - Search Flux Editor documentation for guidance
- [Flux Library Tool](https://docs.flux.ai/flux/reference/library-tool) - Search the Flux Editor component library
- [Flux Calculator Tool](https://docs.flux.ai/flux/reference/calculator-tool) - Extract and evaluate equations
- [Getting Started With Flux](https://docs.flux.ai/flux/tutorials/getting-started-copilot) - Learn the basics of using Flux