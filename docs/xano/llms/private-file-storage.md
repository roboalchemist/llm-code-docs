# Source: https://docs.xano.com/file-storage/private-file-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Private File Storage

Private file storage is included with our **Pro plan**.

All files stored as private files are only accessible through on-demand time sensitive URL generation. This means that all files in your Private Storage are inaccessible until you generate a new URL in your function stack.

To work with private file storage, there are two key components to understand: **private file database fields** and the **Private File: Sign URL function.**

#### Private File Database Field

To store files in your private files library and have them accessible from your function stacks, you'll need to use a database field that is enabled for private file storage. You can enable this for any of the current file field types. Keep in mind that the file access is defined per field, which means that you can not store both public and private files in the same field.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/55eae540-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=a1ee25f4cdac05e08a92de347389f572" width="494" height="745" data-path="images/55eae540-image.jpeg" />
</Frame>

When private files are enabled for a file storage field, a lock icon is displayed in the field name. You will also notice that private files do not display previews from the database view; this is by design, as the files are not accessible until a new URL is generated.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/RVHCrB1RJjFkWEmQ/images/10afa07a-image.jpeg?fit=max&auto=format&n=RVHCrB1RJjFkWEmQ&q=85&s=6493e5bf39f29c8e8ddce19baa15bdfb" width="726" height="249" data-path="images/10afa07a-image.jpeg" />
</Frame>

#### Private File: Sign URL function

To generate a signed URL that enables a private file to be accessible, you first need to retrieve the path of the file, which is stored in the database record. In this example, we have queried our files table and this is the expected return for a private image. The main difference here is that on public files, a URL is returned. For private files, no URL is provided.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b29b0a0f-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=1b0ed044c61aa31cec23250d3b7c5806" width="592" height="577" data-path="images/b29b0a0f-image.jpeg" />
</Frame>

We can then leverage the **Private File: Sign URL** function to generate a publicly accessible link to the file. Provide the path as offered from the database record, a TTL (how long in seconds the link should be valid for), and finally a return variable to contain the output of the function

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/42f028b4-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=307e611d54e937a44c79b32dd4c91cc8" width="1190" height="961" data-path="images/42f028b4-image.jpeg" />
</Frame>

When we run this function, we are returned our new signed URL.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0816120d-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=e780400b0052ecbf67041f7d1cea83de" width="588" height="414" data-path="images/0816120d-image.jpeg" />
</Frame>


Built with [Mintlify](https://mintlify.com).