# Source: https://docs.lancedb.com/tables/multimodal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lancedb.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Multimodal Data (Blobs)

> Learn how to store and query multimodal data (images, audio, video) directly in LanceDB using binary columns.

export const BlobApiIngest = "import lancedb\nimport lance\n\ndb = lancedb.connect(db_path_factory(\"blob_db\"))\n    \n# Create sample data\ndata = [\n    {\"id\": 1, \"video\": b\"fake_video_bytes_1\"},\n    {\"id\": 2, \"video\": b\"fake_video_bytes_2\"}\n]\n    \n# Create the table\ntbl = db.create_table(\"videos\", data=data, schema=schema)\n";

export const BlobApiSchema = "import pyarrow as pa\n\n# Define schema with Blob API metadata for lazy loading\nschema = pa.schema([\n    pa.field(\"id\", pa.int64()),\n    pa.field(\n        \"video\", \n        pa.large_binary(), \n        metadata={\"lance-encoding:blob\": \"true\"} # Enable Blob API\n    ),\n])\n";

export const ProcessResults = "# Convert back to PIL Image\nfor _, row in results.iterrows():\n    image_bytes = row['image_blob']\n    image = Image.open(io.BytesIO(image_bytes))\n    print(f\"Retrieved image: {row['filename']}, Size: {image.size}\")\n    # You can now use 'image' with other libraries or display it\n";

export const SearchData = "# Search for similar images\nquery_vector = np.random.rand(128).astype(np.float32)\nresults = tbl.search(query_vector).limit(1).to_pandas()\n";

export const IngestData = "tbl = db.create_table(\"images\", data=data, schema=schema, mode=\"overwrite\")\n";

export const DefineSchema = "# Define schema explictly to ensure image_blob is treated as binary\nschema = pa.schema([\n    pa.field(\"id\", pa.int32()),\n    pa.field(\"filename\", pa.string()),\n    pa.field(\"vector\", pa.list_(pa.float32(), 128)),\n    pa.field(\"image_blob\", pa.binary()), # Important: Use pa.binary() for blobs\n    pa.field(\"label\", pa.string())\n])\n";

export const CreateDummyData = "# Create some dummy images\ndef create_dummy_image(color):\n    img = Image.new('RGB', (100, 100), color=color)\n    buf = io.BytesIO()\n    img.save(buf, format='PNG')\n    return buf.getvalue()\n\n# Create dataset with metadata, vectors, and image blobs\ndata = [\n    {\n        \"id\": 1,\n        \"filename\": \"red_square.png\",\n        \"vector\": np.random.rand(128).astype(np.float32),\n        \"image_blob\": create_dummy_image('red'),\n        \"label\": \"red\"\n    },\n    {\n        \"id\": 2,\n        \"filename\": \"blue_square.png\",\n        \"vector\": np.random.rand(128).astype(np.float32),\n        \"image_blob\": create_dummy_image('blue'),\n        \"label\": \"blue\"\n    }\n]\n";

export const MultimodalImports = "import lancedb\nimport pyarrow as pa\nimport pandas as pd\nimport numpy as np\nimport io\nfrom PIL import Image\n";

LanceDB handles multimodal data—images, audio, video, and PDF files—natively by storing the raw bytes in a binary column alongside your vectors and metadata. This approach simplifies your data infrastructure by keeping the raw assets and their embeddings in the same database, eliminating the need for separate object storage for many use cases.

This guide demonstrates how to ingest, store, and retrieve image data using standard binary columns, and also introduces the **Lance Blob API** for optimized handling of larger multimodal files.

## Storing binary data

To store binary data, you need to use the `pa.binary()` data type in your Arrow schema. In Python, this corresponds to `bytes` objects if you're using LanceDB's Pydantic `LanceModel` to define the schema.

### 1. Setup and imports

First, let's import the necessary libraries. We'll use `PIL` (Pillow) for image handling and `io` for byte conversion.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {MultimodalImports}
  </CodeBlock>
</CodeGroup>

### 2. Preparing data

For this example, we'll create some dummy in-memory images. In a real application, you would read these from files or an API. The key is to convert your data (image, audio, etc.) into a raw `bytes` object.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {CreateDummyData}
  </CodeBlock>
</CodeGroup>

### 3. Defining the schema

When creating the table, it is **highly recommended** to define the schema explicitly. This ensures that your binary data is correctly interpreted as a `binary` type by Arrow/LanceDB and not as a generic string or list.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {DefineSchema}
  </CodeBlock>
</CodeGroup>

### 4. Ingesting data

Now, create the table using the data and the defined schema.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {IngestData}
  </CodeBlock>
</CodeGroup>

## Retrieving and using blobs

When you search your LanceDB table, you can retrieve the binary column just like any other metadata.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {SearchData}
  </CodeBlock>
</CodeGroup>

### Converting bytes back to objects

Once you have the `bytes` data back from the search result, you can decode it back into its original format (e.g., a PIL Image, an Audio buffer, etc.).

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {ProcessResults}
  </CodeBlock>
</CodeGroup>

## Large Blobs (Blob API)

For larger files like high-resolution images or videos, Lance provides a specialized **Blob API**. By using `pa.large_binary()` and specific metadata, you enable **lazy loading** and optimized encoding. This allows you to work with massive datasets without loading all binary data into memory upfront.

### 1. Defining a blob schema

To use the Blob API, you must mark the column with `{"lance-encoding:blob": "true"}` metadata.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {BlobApiSchema}
  </CodeBlock>
</CodeGroup>

### 2. Ingesting large blobs

You can then ingest data normally, and Lance will handle the optimized storage.

<CodeGroup>
  <CodeBlock filename="Python" language="Python" icon="python">
    {BlobApiIngest}
  </CodeBlock>
</CodeGroup>

<Card>
  For more advanced usage, including random access and file-like reading of blobs, see the
  Lance format's [blob API documentation](https://lance.org/guide/blob/).
</Card>

## Other modalities

The `pa.binary()` and `pa.large_binary()` types are universal. You can use this same pattern for other types of multimodal data:

* **Audio:** Read `.wav` or `.mp3` files as bytes.
* **Video:** Store video transitions or full clips using the Blob API.
* **PDFs/Documents:** Store the raw file content for document search.
