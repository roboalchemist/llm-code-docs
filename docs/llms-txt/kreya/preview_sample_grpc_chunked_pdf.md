# Source: https://kreya.app/docs/scripting-and-tests/samples/previews/preview_sample_grpc_chunked_pdf.md

# Preview PDF streamed via gRPC [Pro / Enterprise](/pricing.md)

This sample demonstrates how to use Kreya's scripting capabilities to handle a gRPC streamed chunked PDF response and visualize the resulting PDF file.

## Overview[​](#overview "Direct link to Overview")

The gRPC service streams a PDF file in chunks. The script processes these chunks, assembles them into a complete PDF file, and displays it in a preview window.

### gRPC Service Definition[​](#grpc-service-definition "Direct link to gRPC Service Definition")

The following `protobuf` definition describes the gRPC service and the streamed response:

```
service PreviewService {
  rpc Pdf (google.protobuf.Empty)
    returns (stream FileChunk);
}

message FileChunk {
  bytes data = 1;
}
```

### Script[​](#script "Direct link to Script")

The following operation script listens for streamed chunks, assembles them into a PDF file, and displays the file in Kreya's preview tab:

```
import { writeFile, appendFile } from 'fs/promises';

const path = './preview-pdf.pdf';

// Ensure the file is empty before starting
await writeFile(path, '');

// Append each chunk of data to the file as it is received
kreya.grpc.onResponse(async msg => await appendFile(path, msg.content.data, 'base64'));

// Once the stream is complete, display the PDF in the preview tab
kreya.grpc.onCallCompleted(async () => await kreya.preview.file(path, 'PDF Preview'));
```

### How it works[​](#how-it-works "Direct link to How it works")

1. **Stream initialization**: The gRPC service streams chunks of the PDF file as `FileChunk` messages.
2. **Chunk handling**: The `onResponse` handler processes each chunk and appends it to a local file (`preview-pdf.pdf`).
3. **File completion**: Once the stream is complete, the `onCallCompleted` handler triggers and displays the assembled PDF file in Kreya's preview tab.

### Output[​](#output "Direct link to Output")

When the script runs, the PDF file will be displayed in Kreya's preview tab, allowing you to view the streamed content.
