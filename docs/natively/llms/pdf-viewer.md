# Source: https://docs.buildnatively.com/guides/integration/pdf-viewer.md

# PDF Viewer

### 🧋 Bubble.io Plugin

\[Action] Natively - Open PDF

* URL - the direct URL address pointing to the PDF file (e.g., `https://example.com/document.pdf`)
* Base64 - the Base64 encoded string representing the entire PDF file
* File name - custom filename for the PDF when displayed or downloaded. If not provided, a default name with timestamp will be generated: `{timestamp}.pdf`
* Download - yes/no - controls whether to show the download button in the PDF viewer

{% hint style="warning" %}
Either URL or Base64 must be provided.
{% endhint %}

#### How to use

The native PDF Viewer is triggered via a single action in your workflow: `Natively - Open PDF action`

1. URL or Base64 - Required - Specify either the URL address pointing to the PDF file or the Base64 encoded string of the file content.
2. File name - Optional - Provide a file name (e.g., `invoice_Q4.pdf`)
3. Download - Required - Specify **yes** or **no**

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FsxyiauAbU77gMukFBUwr%2Fopen_pdf_viever.png?alt=media&#x26;token=6e306363-06c5-4c99-a2f6-7dbb1247a27d" alt="" width="341"><figcaption></figcaption></figure>

<figure><img src="https://3352617162-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F90tV7pYflEQdiAr2VfWu%2Fuploads%2FhNTA4jImZageeHpTyLHv%2Fdownload_pdf.jpg?alt=media&#x26;token=b08de584-4576-4afd-ac3d-2f499d71a353" alt="" width="375"><figcaption></figcaption></figure>

### 🛠 JavaScript SDK

{% code lineNumbers="true" %}

```javascript
// Open from URL with Download Button
window.natively.openPDF({
    url: 'https://example.com/documents/guide.pdf',
    fileName: 'UserGuide.pdf',
    download: true
}, (response) => {
    console.log('PDF Viewer action:', response);
});
// Open from Base64 Data
window.natively.openPDF({
    base64: 'JVBERi0xLjMKJcTl8uXrp...', // Truncated for brevity
    fileName: 'GeneratedReport.pdf',
    download: false
}, (response) => {
    if (response.status === 'FAILED') {
        console.error(''PDF Viewer action:', response.message);
    }
});
//Response structure
{
  "status": "SUCCESS",  // or "FAILED" if an error occurred
  "message": "PDF viewed successfully"  // or error message
}
```

{% endcode %}

### Download Functionality

When the user taps the Download button within the native PDF Viewer, the following sequence occurs:

* The PDF file is saved directly to the device's default Downloads folder.
* A snackbar notification appears at the bottom of the screen to indicate the success or failure of the download process.
* The download button is replaced with a green checkmark icon to provide immediate visual confirmation that the file has been successfully saved to the device.
