# Get document info once processed
uploaded_doc = client.beta.libraries.documents.get(library_id=new_library.id, document_id=uploaded_doc.id)
```

 </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
// Get document info once processed
const processedDoc = await client.beta.libraries.documents.get({
    libraryId: newLibrary.id,
    documentId: uploadedDoc.id
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location "https://api.mistral.ai/v1/libraries/<library_id>/documents/<document_id>" \
     --header "Accept: application/json" \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>
</Tabs>

<details>
    <summary><b>Contents</b></summary>

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
  "processing_status": "Completed",
  "uploaded_by_id": "6340e568-a546-4c41-9dee-1fbeb80493e1",
  "uploaded_by_type": "Workspace",
  "tokens_processing_total": 17143,
  "summary": "Mistral 7B is a 7-billion-parameter language model that outperforms larger models like Llama 2 and Llama 1 in various benchmarks, including reasoning, mathematics, and code generation. It uses grouped-query attention (GQA) for faster inference and sliding window attention (SWA) to handle longer sequences efficiently. The model is released under the Apache 2.0 license and includes a fine-tuned instruction-following version, Mistral 7B - Instruct, which surpasses Llama 2 13B - Chat in performance. The document also details the model's architecture, results, and applications, including content moderation and guardrails for safe usage.",
  "last_processed_at": "2025-07-10T11:43:09.604284Z",
  "number_of_pages": 9,
  "tokens_processing_main_content": 8436,
  "tokens_processing_summary": 8707
}
```

</details>

### Extracting Text from a Document

You can extract text from any document that belongs to a library.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
extracted_text = client.beta.libraries.documents.text_content(library_id=new_library.id, document_id=uploaded_doc.id)