# Source: https://docs.airbyte.com/developers/pyairbyte/reference/airbyte/airbyte-documents.md

# Module airbyte.documents

Copy Page

This module contains the `Documents` class for converting Airbyte records into documents.

Generally you will not create `Documents` objects directly. Instead, you can use one of the following methods to generate documents from records:

* `Source.get_documents()`: Get an iterable of documents from a source.
* `Dataset.to_documents()`: Get an iterable of documents from a dataset.

## Classes[​](#classes "Direct link to Classes")

`Document(**data: Any)` : A PyAirbyte document is a specific projection on top of a record.

Documents have the following structure:

* id (str): A unique string identifier for the document.
* content (str): A string representing the record when rendered as a document.
* metadata (dict\[str, Any]): Associated metadata about the document, such as the record's IDs and/or URLs.

This class is duck-typed to be compatible with LangChain project's `Document` class.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[`ValidationError`]\[pydantic\_core.ValidationError] if the input data cannot be validated to form a valid model.

`self` is explicitly positional-only to allow `self` as a field name.

### Ancestors (in MRO)[​](#ancestors-in-mro "Direct link to Ancestors (in MRO)")

* pydantic.main.BaseModel

### Class variables[​](#class-variables "Direct link to Class variables")

`content: str` :

`id: str | None` :

`last_modified: datetime.datetime | None` :

`metadata: dict[str, Any]` :

`model_config` :

### Instance variables[​](#instance-variables "Direct link to Instance variables")

`page_content: str` : Return the content of the document.

This is an alias for the `content` property, and is provided for duck-type compatibility with the LangChain project's `Document` class.
