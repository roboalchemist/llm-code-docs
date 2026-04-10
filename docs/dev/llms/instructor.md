# Source: https://dev.writer.com/home/integrations/instructor.md

> ## Documentation Index
> Fetch the complete documentation index at: https://dev.writer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Structured output with Instructor

This tutorial will guide you through using Writer with [Instructor](https://useinstructor.com/), a Python library that makes it easy to get structured data like JSON from LLMs.

## Prerequisites

* Python 3.8 or higher installed
* [Poetry](https://pypi.org/project/poetry/) installed (see their [installation guide](https://python-poetry.org/docs/#installation))
* A Writer API key (follow the [Quickstart](/home/quickstart) to obtain an API key)

## Getting started

To get started with Instructor, you'll need to install the library and set up your environment.

<Steps>
  <Step title="Obtain an API key">
    First, make sure that you've signed up for a Writer AI Studio account and obtained an API key. You can follow the [Quickstart](/home/quickstart) to obtain an API key.
  </Step>

  <Step title="Install instructor">
    Once you've done so, install `instructor` with Writer support by running:

    ```bash  theme={null}
    pip install instructor[writer]
    ```
  </Step>

  <Step title="Set the `WRITER_API_KEY` environment variable">
    Make sure to set the `WRITER_API_KEY` environment variable with your Writer API key or pass it as an argument to the Writer constructor.
  </Step>
</Steps>

## Basic usage

Following is a simple example of how to use `instructor` with Writer:

```python  theme={null}
import instructor
from writerai import Writer
from pydantic import BaseModel

# Initialize Writer client
client = instructor.from_writer(Writer(api_key="your API key"))


class User(BaseModel):
    name: str
    age: int


# Extract structured data
user = client.chat.completions.create(
    model="palmyra-x5",
    messages=[{"role": "user", "content": "Extract: John is 30 years old"}],
    response_model=User,
)

print(user)
#> name='John' age=30
```

This code creates a simple data model with two fields: `name` and `age`. It then uses the `instructor.from_writer` function to create a `client` object that uses the Writer API to extract structured data from a text.

## Instructor modes

Instructor supports two modes for structured output with Writer:

* [JSON mode](#json-mode): Returns a response that strictly follows the provided JSON schema.
* [Tools mode](#tools-mode): Returns a structured response using the `tool_calls` field, where it populates the defined tool and its arguments based on the input.

Both modes use the [Writer chat completion endpoint](/api-reference/completion-api/chat-completion) to generate structured outputs. The key difference lies in how the model returns the data: either as a raw JSON object or via a structured tool call.

### JSON mode

JSON mode uses Writer's native JSON schema support. When you use this mode:

* Instructor converts your Pydantic model into a JSON schema and passes it as the `response_format` parameter
* The model generates a response that strictly follows the provided JSON schema
* Instructor then parses the JSON response and validates it against your original Pydantic model

<Tip>
  For more details on structured outputs and JSON schema usage, see our [structured output documentation](/home/structured-output).
</Tip>

### Tools mode

Tools mode uses Writer's tool calling capabilities. When you use this mode:

* Instructor converts your Pydantic model into a tool definition
* Instructor adds this tool definition to the API call using the `tools` parameter
* The model returns a structured response using the `tool_calls` field, where it populates the defined tool and its arguments based on the input
* Instructor extracts the arguments from the `tool_calls` field and validates them against the original Pydantic model

<Tip>
  For more details on tool calling, see our [tool calling documentation](/home/tool-calling).
</Tip>

### Specifying the mode

You can specify which mode to use when initializing the Instructor client:

```python  theme={null}
import instructor
from writerai import Writer

# Use JSON mode
client = instructor.from_writer(
    Writer(api_key="your API key"),
    mode=instructor.Mode.WRITER_JSON
)

# Use Tools mode
client = instructor.from_writer(
    Writer(api_key="your API key"),
    mode=instructor.Mode.WRITER_TOOLS
)

```

If you don't specify a mode, Instructor will use `WRITER_TOOLS` by default.

## Instructor vs. Writer SDK

When working with structured outputs, you can choose between two main approaches: using Instructor, a high-level framework built on top of LLM providers, or using the Writer SDK directly, which offers low-level access to the Writer LLMs. Each option comes with its own strengths and trade-offs, depending on your goals and level of control needed.

| Feature                      | Instructor                                                               | Writer SDK                                                 |
| ---------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- |
| **Retry mechanism**          | Built-in retry logic with error handling and prompt editing              | Manual implementation required                             |
| **Schema handling**          | Auto-converts a wide range of Python types into JSON Schema via Pydantic | Manual schema conversion required                          |
| **Validation & reliability** | Enhanced outcomes through Pydantic validation + retries                  | Same results possible with manual implementation           |
| **Prompt optimization**      | Built-in prompt minimization and optimization                            | Manual prompt engineering required                         |
| **Model access**             | Limited to supported models (currently V4 + Tool Calls)                  | Full access to latest models (V4, V5) and all output modes |
| **Update speed**             | Requires updates/contributions for new features                          | Immediate support for latest Palmyra features              |

For more on Instructor’s advanced retry and error handling capabilities, see the [official Instructor retrying guide](https://python.useinstructor.com/concepts/retrying/).

## Building a data repair tool with Instructor and Writer

You can also use Instructor to do advanced data extraction and repair. In this example, you'll build a Python application that extracts structured data from text, CSV, and PDF files using Instructor and Writer. This application will:

* Parse text, CSV, and PDF files
* Extract and validate structured data using Instructor and Writer
* Output the results in CSV format

The finished code for this tutorial is available in the [API tutorials](https://github.com/writer/api-tutorials/tree/main/instructor-and-writer-tutorial) GitHub repository.

### Setting up the project

<Steps>
  <Step title="Create a new project">
    First, create a new project and set up Poetry for dependency management:

    ```bash  theme={null}
    mkdir instructor-and-writer-tutorial
    cd instructor-and-writer-tutorial
    poetry init -y
    ```
  </Step>

  <Step title="Add dependencies">
    Add the required dependencies to your project:

    ```bash  theme={null}
    poetry add instructor writer-sdk python-dotenv pydantic
    ```
  </Step>

  <Step title="Set up your environment variables">
    Create a `.env` file in your project root and add your Writer API key:

    ```
    WRITER_API_KEY=your_api_key_here
    ```
  </Step>

  <Step title="Create `main.py` file and add imports">
    Create a `main.py` file and add the following imports:

    ```python  theme={null}
    import asyncio
    import csv
    import json
    import os
    from typing import Annotated, Type, Iterable, List

    import instructor
    from dotenv import load_dotenv
    from pydantic import BaseModel, AfterValidator, Field
    from writerai import Writer, AsyncWriter

    load_dotenv()
    ```

    Here's what each import is used for:

    * `asyncio`: This is used to run the application on multiple files concurrently.
    * `csv`: This is used to write the extracted data to a CSV file.
    * `json`: This is used to write the extracted data to a JSON file.
    * `os`: This is used to read the files.
    * `instructor`: The `instructor` library is used for structured output.
    * `writerai`: This is the Writer Python SDK, which is used to interact with the Writer API.
    * `typing` and `pydantic`: These modules are used to define the types for fields in the `UserExtract` class defined in the next step.
    * `dotenv`: The `dotenv` module is used to load the `.env` file that contains your Writer API key.
  </Step>

  <Step title="Setting up Writer client">
    Initialize the Writer client for both synchronous and asynchronous operations:

    ```python  theme={null}
    writer_client = Writer()
    async_writer_client = AsyncWriter()
    ```
  </Step>
</Steps>

### Defining the data model

In order for Instructor to extract structured output, you need to define a data model using Pydantic. To define the data model, create a `UserExtract` class to represent the data you want to extract:

```python  theme={null}
class UserExtract(BaseModel):
    @staticmethod
    def first_last_name_validator(v):
        if v[0] != v[0].upper() or v[1:] != v[1:].lower() or not v.isalpha():
            raise ValueError("Name must contain only letters and start with uppercase letter")
        return v

    first_name: Annotated[str, AfterValidator(first_last_name_validator)] = Field(
        ..., description="The name of the user"
    )
    last_name: Annotated[str, AfterValidator(first_last_name_validator)] = Field(
        ..., description="The surname of the user"
    )
    email: str
```

This data model defines the fields that you want to extract from the files. The `first_name` and `last_name` fields are validated to ensure they start with an uppercase letter and contain only letters. In this example, the `email` field is a simple string field, though you could also use a Pydantic field to validate the email format.

### Parsing the files

With the data model defined, you can now implement file parsing. This involves creating functions to open the files and extract the text.

<Steps>
  <Step title="Create a function to handle file processing">
    Implement the main file handler function that orchestrates the entire process:

    ```python  theme={null}
    async def handle_file(file_path: str, response_model: Type[BaseModel], output_path: str = None) -> None:
        extension = os.path.splitext(file_path)[1]
        name = os.path.splitext(os.path.basename(file_path))[0]

        file_text = await fetch_file_text(file_path, name, extension)
        repaired_entities = await repair_data(file_text, response_model)

        print(f"Number of entities extracted from {name}{extension}: {len(repaired_entities)}")
        return generate_csv(repaired_entities, response_model, output_path)
    ```

    This function handles the file processing logic, including file type validation, text extraction, data repair, and CSV generation.
  </Step>

  <Step title="Create a function to read the files">
    Next, create a function to read the files based on the given path and extension:

    ```python  theme={null}
    async def fetch_file_text(file_path: str, name: str, extension: str) -> str:
        allowed_extensions = [".txt", ".csv", ".pdf"]
        if extension not in allowed_extensions:
            raise ValueError(f"File extension {extension} is not allowed. Only {', '.join(allowed_extensions)}")

        print(f"Reading {name}{extension} content...")
        with open(file_path, 'rb') as file:
            file_contents = file.read()

        return await parse_file(file_contents, name, extension)
    ```
  </Step>

  <Step title="Extract the file content">
    Next, create a function to extract the text from the files. For text files, this function simply reads the file contents. For PDFs, the function uploads the PDF using Writer's [file upload endpoint](/api-reference/file-api/upload-files), parses the text using [PDF parsing tool](/api-reference/tool-api/pdf-parser), and then deletes the file from Writer's servers using the [file delete endpoint](/api-reference/file-api/delete-file):

    ```python  theme={null}
    async def parse_file(file_bytes_content: bytes, name: str, extension: str) -> str:
        file_text = ""

        if extension == ".pdf":
            print(f"Uploading {name}{extension} content to writer servers...")
            file = await async_writer_client.files.upload(
                content=file_bytes_content,
                content_disposition=f"attachment; filename={name + extension}",
                content_type="application/octet-stream",
            )

            print(f"Converting {name}{extension} content from PDF to text...")
            file_text = await async_writer_client.tools.parse_pdf(
                file_id=file.id,
                format="text",
            )

            print(f"Deleting {name}{extension} from writer servers...")
            await async_writer_client.files.delete(file.id)
        else:
            print(f"Converting {name}{extension} content...")
            file_text = file_bytes_content.decode("utf-8")

        return file_text
    ```
  </Step>
</Steps>

### Extracting and repairing the data

With the file content extracted, you can now implement data extraction and repair using Instructor and Writer.

<Steps>
  <Step title="Create a function to repair the data">
    Create a function to extract and repair data using Instructor:

    ```python  theme={null}
    async def repair_data(file_text: str, response_model: Type[BaseModel]) -> List[BaseModel]:
        instructor_client = instructor.from_writer(client=async_writer_client)

        if not issubclass(response_model, BaseModel):
            raise ValueError("Response model must be subclass of pydantic BaseModel")

        print("Extracting data featuring Instructor tools...")
        return await instructor_client.chat.completions.create(
            model="palmyra-x5",
            response_model=Iterable[response_model],
            max_retries=5,
            messages=[
                {"role": "user", "content": f"Extract entities from {file_text}"},
            ],
        )
    ```
  </Step>

  <Step title="Implementing CSV generation">
    Add a function to save the extracted data to CSV:

    ```python  theme={null}
    def generate_csv(entities: List[BaseModel], response_model: Type[BaseModel], output_path: str = None) -> None:
        fieldnames = list(response_model.model_json_schema()["properties"].keys())
        file_path = f"{response_model.__name__}.csv"

        if output_path:
            file_path = output_path + file_path
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            dict_writer = csv.DictWriter(file, fieldnames=fieldnames)
            dict_writer.writeheader()
            for entity in entities:
                dict_writer.writerow(json.loads(response_model(**entity.model_dump()).model_dump_json()))
    ```
  </Step>
</Steps>

### Creating the main handler

Finally, implement the main function to process multiple files concurrently:

```python  theme={null}
async def main():
    data = [
        ("example_data/ExampleFileTextFormat.txt", UserExtract, None),
        ("example_data/ExampleFilePDFFormat.pdf", UserExtract, "out/"),
    ]
    tasks = []

    for row in data:
        tasks.append(handle_file(row[0], row[1], row[2]))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
```

In this example, the input paths are hardcoded, but you could modify the application to accept input paths from the command line or a web interface, or read from a directory or database.

### Testing the application

Your data repair tool is now ready to use. To test it, follow these steps:

<Steps>
  <Step title="Create an `example_data` directory">
    Create an `example_data` directory and add some test files:

    * A text file with user information
    * A PDF file with user information

    You can use the [example data](https://github.com/writer/api-tutorials/tree/main/instructor-and-writer-tutorial/example_data) provided in the GitHub repository for this tutorial. If you provide your own, be sure to update the `main.py` file to point to the new files.
  </Step>

  <Step title="Run the application">
    Run the application:

    ```bash  theme={null}
    poetry run python main.py
    ```

    The application will process both files concurrently and generate CSV files containing the extracted user information.
  </Step>
</Steps>

## Conclusion

You've now seen basic and advanced usage of Writer with Instructor. To learn more about Instructor, check out the [Instructor documentation](https://python.useinstructor.com/). Structured output is a powerful feature that can help you build more accurate and reliable applications, especially combined with [tool calling](/home/tool-calling).
