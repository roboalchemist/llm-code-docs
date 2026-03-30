# Source: https://docs.acceldata.io/documentation/knowledge-base.md

# Knowledge Base

## Overview

The Knowledge Base is your organization’s central document repository. ADM uses it for retrieval-augmented generation (RAG) to produce accurate, contextual answers grounded in your policies, procedures, and technical docs.

**Purpose**

- Centralize organization-specific knowledge.
- Enrich AI responses with verified context.
- Share domain knowledge and maintain a single source of truth.

**How it works**

1. **Upload** documents.
2. **Index** content (text extraction and structuring).
3. **Embed** content into vectors for fast similarity search.
4. **Retrieve** relevant sections at question time.
5. **Answer** with sources and citations.

When you ask a question, ADM automatically searches the Knowledge Base, pulls the most relevant passages, and cites them in the response.

## Uploading Documents

**Navigate**

- **Main menu:** _Knowledge Base_.
- **Command:** type **/knowledge-base** in any conversation.

**Upload**

1. Click **Upload Document** (or drag and drop files).
2. (Optional) Add metadata:
    - **Title**, **Description**, **Tags**, **Access Level**.

3. Click **Upload** and wait for indexing to complete.

**Supported formats**

- **Fully supported:** PDF, DOC/DOCX, TXT, MD, XLS/XLSX
 (Spreadsheets index static values; formulas are not executed.)
- **Partially supported:** PPTX (text only), JSON (experimental), XML (experimental)
- **Not supported:** Images, audio, video, archives, executables

**Limits**

- Max file size: **25 MB**
- PDF: **≤ 500 pages**
- Word: **≤ 200 pages**

## Document Indexing

**What indexing does**

- Extracts text and structure.
- Splits content into meaningful chunks.
- Generates semantic embeddings.
- Stores vectors for fast similarity search.

**Status indicators**

- **Indexing** ⟳: Processing
- **Indexed** ✓: Ready to use
- **Failed** ✗: Needs attention

**Re-indexing**

- Occurs automatically when you upload a new version.
- Trigger manually with **Re-index** if results look off or after system updates.

## Using Knowledge in Conversations

**Automatic context**

- ADM analyzes your question, retrieves relevant passages (typically 3–5), synthesizes an answer, and shows **citations**.

**Citations include**

- Document name, and page numbers when available.
- Click a citation to open the source and verify the context.

**See sources**

- Expand **Sources** at the end of a response to view all referenced documents.

## Managing Your Knowledge Base

**View**

- The document table shows **Name**, **Upload Date**, **Size**, **Status**, **Tags**.
 Sort and filter as needed.

**Search**

- Search by **Name**, **Tags**, **Content**, and **Upload Date**.
 Combine criteria to narrow results; save frequent searches.

**Edit metadata**

1. Open a document **&gt;** **Edit**.
2. Update **Title**, **Description**, **Tags**, **Access**.
3. **Save Changes**. (No re-index required for metadata edits.)

**Delete**

1. Select document(s) **&gt;** **Delete** **&gt;** confirm **Delete Permanently**.
> Warning This action cannot be undone. Download a copy first if needed.

**Organize with tags**

- Use clear, consistent tags (e.g., `policy`, `technical-doc`, `onboarding`, `engineering`, `project-alpha`).
- Establish a simple tag taxonomy for teams to follow.

**Best practices**

- Keep documents current; review quarterly.
- Remove superseded content.
- Use descriptive filenames (e.g., `Dept_DocType_Version_Date`).
- Monitor which docs are cited often to spot gaps.

## Technical Architecture (Brief)

- **RAG pipeline:** vector store + semantic retrieval + grounded generation.
- **Vector database:** FAISS for fast similarity search.
- **Embeddings:** transformer models create semantic vectors.
- **Chunking:** sentence/token strategies preserve context within optimal chunk sizes.
- **Retrieval:** top matches (cosine similarity) provided as context to the model for faithful answers.

Quality controls include checks for relevancy, contextual precision, faithfulness, and hallucination/toxicity safeguards.

## Integration with External Knowledge Sources

ADM supports external sources via **Model Context Protocol (MCP)**:

- **Confluence:** query live pages without manual upload.
- **Jira:** reference tickets and project artifacts.
- Future options: Google Drive, SharePoint, and more.

> Note MCP integrations require administrator configuration.

## Troubleshooting

**Document not appearing**

- Verify format and size limits; refresh the page.
- Wait for **Indexing** to finish.
- Known: PPTX may not list correctly in some cases; contact support if persistent.

**Incorrect/incomplete answers**

- Confirm the source document contains the correct content.
- **Re-index** the document.
- Check for conflicting versions or duplicates.

**Indexing failed**

- Open the file locally to confirm it isn’t corrupted.
- Re-upload in a supported format and within limits.

**Slow indexing**

- Large/complex docs take longer.
- Break very large documents into smaller files if needed.

## Security and Privacy

### Access Control

The Knowledge Base respects your organization's security requirements:

- **Document-Level Permissions**: Set access levels during upload to control who can view and query each document. Options typically include Public (all users), Department-specific, and Private (uploader only).
- **Role-Based Access**: Your ADM administrator can configure role-based access control (RBAC) to automatically apply permissions based on user roles.
- **Audit Logging**: All document uploads, accesses, and deletions are logged for security and compliance purposes.

### Data Protection

Your documents are protected through multiple security layers:

- **Encryption at Rest**: All documents are encrypted in storage using industry-standard encryption protocols.
- **Encryption in Transit**: Data transfers between your browser and ADM servers use TLS encryption.
- **Data Isolation**: In multi-tenant environments, your documents are isolated from other organizations' data.
- **Retention Policies**: Configure automatic deletion of documents after a specified period to comply with data retention requirements.

### Compliance

The Knowledge Base supports various compliance frameworks:

- GDPR compliance for European data
- SOC 2 Type II certification
- ISO 27001 information security standards
- HIPAA compliance for healthcare documents (when configured)