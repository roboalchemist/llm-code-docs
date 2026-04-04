# Upload document
file_path = "mistral7b.pdf"
with open(file_path, "rb") as file_content:
    uploaded_doc = client.beta.libraries.documents.upload(
        library_id=new_library.id,
        file=File(fileName="mistral7b.pdf", content=file_content),
    )
```

 </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const filePath = "~/path/to/doc.pdf";
const fileContent = fs.readFileSync(filePath);
const uploadedDoc = await client.beta.libraries.documents.upload({
    libraryId: newLibrary.id,
    requestBody: {
        file: {
            fileName: "mistral7b.pdf",
            content: fileContent
        }
    }
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location --request POST "https://api.mistral.ai/v1/libraries/<library_id>/documents" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --header "Content-Type: multipart/form-data" \
     --form "file=@mistral7b.pdf;type=application/pdf"

```
  </TabItem>
</Tabs>

<details>
    <summary><b>Content</b></summary>

```json
{
  "id": "424fdcb8-3c11-478c-a651-9637be8b4fc4",
  "library_id": "0197f425-5e85-7353-b8e7-e8b974b9c613",
  "hash": "8ad11d7d6d3a9ce8a0870088ebbcdb00",
  "mime_type": "application/pdf",
  "extension": "pdf",
  "size": 3749788,
  "name": "mistral7b.pdf",
  "created_at": "2025-07-10T11:43:01.017430Z",
  "processing_status": "Running",
  "uploaded_by_id": "6340e568-a546-4c41-9dee-1fbeb80493e1",
  "uploaded_by_type": "Workspace",
  "tokens_processing_total": 0,
  "summary": null,
  "last_processed_at": null,
  "number_of_pages": null,
  "tokens_processing_main_content": null,
  "tokens_processing_summary": null
}
```
</details>

#### Status

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python