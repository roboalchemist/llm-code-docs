# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es6/open-pdf-file/from-azure-active-directory.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/javascript-es5/open-pdf-file/from-azure-active-directory.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/vue/open-pdf-file/from-azure-active-directory.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/react/open-pdf-file/from-azure-active-directory.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/angular/open-pdf-file/from-azure-active-directory.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-mvc/open-pdf-file/from-azure-active-directory.md

# Source: https://docs.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-core/open-pdf-file/from-azure-active-directory.md

# Open PDF from Azure Active Directory

### Overview

The ASP.NET Core PDF Viewer component supports loading and saving PDF files with Azure Active Directory (AAD). The following steps explain how to securely load and store PDFs using AAD.

### Steps to open a PDF from Azure Active Directory

### Step 2: Create the Azure Storage account

1. **Create a Storage Account**:
   - In the Azure portal, use the search bar to search for **Storage accounts**.
   - Create a new storage account by filling in the required details (e.g., name, location, resource group, etc.).

    ![storage-account](../images/storage-account.png)

### Step 4: Upload the PDF to Azure Storage

1. **Navigate to Data Storage**:
   - In the Azure portal, go to **Data storage** > **Containers**.

2. **Upload the PDF File**:
   - Create a new container and upload the PDF document you want to access in the PDF Viewer.

    ![upload-pdf](../images/upload-pdf.png)
---

### Step 5: Server-side configuration
1. Follow the steps provided in the [link](https://help.syncfusion.com/document-processing/pdf/pdf-viewer/asp-net-core/getting-started-with-server-backed) to create a simple PDF Viewer sample.

2. Add the following code snippet in `Index.cshtml.cs`.

{% tabs %}
{% highlight c# tabtitle="~/Index.cshtml.cs" %}

using Azure.Identity;
using Azure.Storage.Blobs;

string tenantId = "YOUR_TENANT_ID";
string clientId = "YOUR_CLIENT_ID";
string clientSecret = "YOUR_CLIENT_SECRET";
string blobServiceEndpoint = "https://your-storage-account.blob.core.windows.net";
string containerName = "your-container-name";

 public async Task<IActionResult> OnGetLoadFromAAD(string fileName)
 {
     var clientSecretCredential = new ClientSecretCredential(tenantId, clientId, clientSecret);
     var blobServiceClient = new BlobServiceClient(new Uri(blobServiceEndpoint), clientSecretCredential);
     var containerClient = blobServiceClient.GetBlobContainerClient(containerName);
     var blobClient = containerClient.GetBlobClient(fileName);

     // Download the PDF file to a local stream
     using MemoryStream pdfStream = new MemoryStream();
     await blobClient.DownloadToAsync(pdfStream);
     var base64 = Convert.ToBase64String(pdfStream.ToArray());
     return Content("data:application/pdf;base64," + base64);
 }

 public async Task<IActionResult> OnPostSaveToAAD([FromBody]jsonObjects responseData)
 {
     var jsonObject = JsonConverterstring(responseData);
     PdfRenderer pdfviewer = new PdfRenderer(_cache);
     var fileName = jsonObject.ContainsKey("documentId") ? jsonObject["documentId"] : "Test.pdf";
     string documentBase = pdfviewer.GetDocumentAsBase64(jsonObject);
     string convertedBase = documentBase.Substring(documentBase.LastIndexOf(',') + 1);
     // Decode the Base64 string to a byte array
     byte[] byteArray = Convert.FromBase64String(convertedBase);
     // Create a MemoryStream from the byte array
     MemoryStream stream = new MemoryStream(byteArray);
     // Create a new BlobServiceClient using the DefaultAzureCredential
     var clientSecretCredential = new ClientSecretCredential(tenantId, clientId, clientSecret);
     var blobServiceClient = new BlobServiceClient(new Uri(blobServiceEndpoint), clientSecretCredential);
     // Get a reference to the container
     var containerClient = blobServiceClient.GetBlobContainerClient(containerName);
     // Get a reference to the blob
     var blobClient = containerClient.GetBlobClient(fileName);
     //FileStream uploadFileStream = new FileStream();
     await blobClient.UploadAsync(stream, true);
     stream.Close();
     return Content(string.Empty);
 }

{% endhighlight %}
{% endtabs %}

3. Configure server-side code:
   - Open the server-side application (e.g., ASP.NET Core) and configure the following details in the `PdfViewerController` file:
     - `tenantId` (your Azure AD tenant ID),
     - `clientId` (your registered application client ID),
     - `clientSecret` (your registered application client secret),
     - `blobServiceEndpoint` (your storage account blob service URL),
     - `containerName` (your container name in Azure Blob Storage).

4. Add the following code snippet in `Index.cshtml`.

{% tabs %}
{% highlight c# tabtitle="~/Index.cshtml" %}

@page "{handler?}"
@model IndexModel
@{
    ViewData["Title"] = "Home page";
}

<div>

    <!-- Custom buttons for Load and Save -->
    <div style="margin-top: 10px;">
        <button id="loadFromAADButton" class="e-btn" style="margin-right: 10px;">Load From AAD</button>
        <button id="saveToAADButton" class="e-btn">Save To AAD</button>
    </div>
    <ejs-pdfviewer id="pdfviewer" style="height:600px" serviceUrl="/Index" documentPath="https://cdn.syncfusion.com/content/pdf/pdf-succinctly.pdf">
    </ejs-pdfviewer>

</div>

<script type="text/javascript">
    window.onload = function () {
        var pdfViewer = document.getElementById('pdfviewer').ej2_instances[0];

        // Handle the Load From AAD button click
        document.getElementById('loadFromAADButton').addEventListener('click', function () {
            const xhr = new XMLHttpRequest();
            xhr.open('GET', `/Index/LoadFromAAD?fileName=1Page.pdf`, true);
            xhr.onreadystatechange = () => {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    const data = xhr.responseText; // Get the response (assumed to be the PDF data or URL)
                    console.log(data); // Handle the response (for debugging)

                    // Load the PDF into the viewer (assuming the response contains the PDF data or URL)
                    pdfViewer.load(data, ''); // Load the document
                }
            };
            xhr.send();
        });

        // Handle the Save To AAD button click
        document.getElementById('saveToAADButton').addEventListener('click', function () {
            // Save PDF to AAD
            // Set the server action settings to handle the "Save To AAD" action
            pdfViewer.serverActionSettings.download = "SaveToAAD"; // This triggers a custom server-side save action
            // Download the file (assuming this will be saved to AAD)
            pdfViewer.download(); // Trigger the download, which may involve saving it to AAD

        });
    }
</script>


{% endhighlight %}
{% endtabs %}

5. Run the Application
    - Build and run your Core application. The PDF Viewer will be displayed with Load from AAD and Save to AAD buttons.

6. Load PDF from AAD
    - Click the Load from AAD button.
    - The server fetches the PDF from Azure Blob Storage and loads it into the Syncfusion PDF Viewer.

7. Save PDF to AAD
    - Click the Save to AAD button.
    - The server uploads the modified PDF back to Azure Blob Storage.

[View sample in GitHub](https://github.com/SyncfusionExamples/open-save-pdf-documents-in-aad).