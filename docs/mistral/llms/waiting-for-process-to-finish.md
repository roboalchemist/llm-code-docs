# Waiting for process to finish

while status.processing_status == "Running":
    status = client.beta.libraries.documents.status(library_id=new_library.id, document_id=uploaded_doc.id)
    time.sleep(1)
print(status)
```

 </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
// Check status document
const docStatus = await client.beta.libraries.documents.status({
    libraryId: newLibrary.id,
    documentId: uploadedDoc.id
});
console.log(docStatus);

// Waiting for process to finish
while (docStatus.processingStatus === "Running") {
    await new Promise(resolve => setTimeout(resolve, 1000)); // Wait for 1 second
    const updatedStatus = await client.beta.libraries.documents.status({
        libraryId: newLibrary.id,
        documentId: uploadedDoc.id
    });
    console.log(updatedStatus);
    Object.assign(docStatus, updatedStatus); // Update the status object
}
console.log(docStatus);

```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/libraries/<library_id>/documents/<document_id>/status" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>
</Tabs>

<details>
    <summary><b>Contents</b></summary>

**Running Status**
```json
{
  "document_id": "424fdcb8-3c11-478c-a651-9637be8b4fc4",
  "processing_status": "Running"
}
```

**Finished Status**
```json
{
  "document_id": "2445a837-8f4e-475f-8183-fe4e99fed2d9",
  "processing_status": "Completed"
}
```

</details>

#### Get Document
<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python