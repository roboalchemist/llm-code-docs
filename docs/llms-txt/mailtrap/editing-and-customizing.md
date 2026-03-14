# Source: https://docs.mailtrap.io/email-api-smtp/email-templates/editing-and-customizing.md

# Editing and Customizing

### Details

Each template must have a name, subject, category, and assigned domain. The subject also supports variables.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-940dfd68b21c2a101059dfadfcb7857e371653bd%2Ftemplate-details-view.png?alt=media" alt="Template Details page showing domain, name, subject, and category fields in a bordered section" width="563"><figcaption><p>Template details section</p></figcaption></figure></div>

### Drag & Drop Editor

The drag-and-drop editor allows you to design templates without any coding.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-d113e67ef60ce61aa373995bd7d775b5750784f0%2Ftemplate-drag-drop-interface.png?alt=media" alt="Drag and Drop Editor interface showing template preview in center with blocks and content options on right sidebar" width="563"><figcaption><p>Drag and Drop Editor</p></figcaption></figure></div>

### Code Editor

Code Editor allows you to edit the HTML or Text content, depending on the emails you want to send.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-a13a7256fbeafc8cc946b9b71c1115bb07b93ba7%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

The editor supports Find and Replace options, and you can use Cmd+F or Win+F as a hotkey to reveal a quick search bar.

If your template has an error, Handlebars cannot render it. You'll see an error message in the Preview tab, and the RAW code with an error will be highlighted in the Editor.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-403e2b462026d23199f72e547fbb1576c88ac32b%2Fimage.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

You can't save a template with errors, either. Remember that we don't validate HTML.

### **Uploading an image**

{% stepper %}
{% step %}
Click Upload image in the upper right corner of the Code Editor.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-1c636a6f212f1eb0016484ce6996e33e23f26483%2Ftemplate-upload-image-button.png?alt=media" alt="Code Editor with Upload image button highlighted in upper right corner" width="375"><figcaption><p>Upload image button in Code Editor</p></figcaption></figure></div>
{% endstep %}

{% step %}
Hit the Upload New button in the following menu and choose an image from your local drive (Supported formats are JPG, PNG, and GIF, and the maximum file size is 2 MB).

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-af66650da784a3ba3a9591ad8626cd93605e92bd%2Ftemplate-images-library.png?alt=media" alt="Images library page showing Upload New button highlighted in top right" width="563"><figcaption><p>Images library with Upload New button</p></figcaption></figure></div>
{% endstep %}

{% step %}
Once the image is uploaded, you will receive a confirmation notification. If the file format is unsupported or the image is too big, you will receive the corresponding error message.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-3c240eac8ce9ee4922028a23cf32b616a4143cdb%2Ftemplate-image-upload-success.png?alt=media" alt="Success notification showing Image successfully uploaded message in green banner" width="563"><figcaption><p>Image upload success notification</p></figcaption></figure></div>
{% endstep %}

{% step %}
Click the Copy URL button to copy the image URL to your clipboard, then click Template to return to the editing menu.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-8c33d18b581f860bb20fc7f11d661cd63c758472%2Ftemplate-copy-url-button.png?alt=media" alt="Images library showing uploaded images with Copy URL button highlighted" width="563"><figcaption><p>Copy URL button for uploaded images</p></figcaption></figure></div>
{% endstep %}

{% step %}
Proceed to add the image to the template body under the `<img>` tag. You can preview it in the template as soon as the asset is added.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-2226ade6f36bc2deb1d039dffcc6394e93093a54%2Ftemplate-image-in-code.png?alt=media" alt="HTML code showing image URL inserted in img src attribute with highlighted code" width="375"><figcaption><p>Image URL added to template HTML</p></figcaption></figure></div>
{% endstep %}
{% endstepper %}

### **Test Data**

Code Editor automatically parses your template and shows all the variables found. The Test Data tab helps you preview the object variables.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-58f9d403a4f9289176f7a2b14d0712c9b5a802f1%2Ftemplate-test-data-variables.png?alt=media" alt="Test Data tab showing template variables with test values and preview" width="563"><figcaption><p>Test Data tab with template variables</p></figcaption></figure></div>

By default, as a value, we put a variable name and add the "Test\_" prefix.

### Send test

If you're using email templates in production, you can send a test email to the account owner's email address to run basic tests. Simply press the Send Test button.

<div align="left" data-with-frame="true"><figure><img src="https://1476453098-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS3xyr7ba7aGO19rc8dSK%2Fuploads%2Fgit-blob-e656b0110b9272cc878ad6e33ac0a35c9c24a4ea%2Ftemplate-send-test-button.png?alt=media" alt="Template editor showing Send Test button highlighted in top right" width="563"><figcaption><p>Send Test button</p></figcaption></figure></div>

Important Notes:

* Your domain should be verified to send a test.
* Each test email is billed over your quota.

### Next steps

* [Handlebars Guide](https://docs.mailtrap.io/email-api-smtp/email-templates/handlebars) - Learn how to use Handlebars syntax to add dynamic content
* [Integration](https://docs.mailtrap.io/email-api-smtp/email-templates/integration) - Integrate templates with Email API/SMTP
* [Debugging](https://docs.mailtrap.io/email-api-smtp/email-templates/debugging) - Test templates with Email Sandbox
