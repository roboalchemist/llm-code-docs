# Source: https://docs.base44.com/Building-your-app/Using-media.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Uploading and managing files

> Make your app stand out with images, documents, data files, audio, and your own branding.

Media files such as images, documents, data files, and audio help you create a rich, interactive app experience for your users. You can upload files both during the app-building process and in your live app, giving your users new ways to share and engage.

You can also add a custom logo that appears when someone adds your app to their home screen. The logo is also used as the browser favicon, so your app always looks professional and on-brand from both desktop and mobile.

***

## Uploading files to the AI chat

When building with AI chat, you can upload files such as images, documents, and data files to help generate app content, styles, and data. You can work directly from documents like PRDs, brand guides, or spreadsheets, as well as structured data files such as CSV, Excel, or JSON.

To upload a file to the AI chat, click **Upload files** and type your message to explain what you want it to do with the file. You can then chat about the file, ask questions, analyze it, or ask the AI to use it to design your data model or import data into your entities.

<img src="https://mintcdn.com/base44/iWAI9SeWmmB3Mcpa/images/2025-10-05_15-44-20.png?fit=max&auto=format&n=iWAI9SeWmmB3Mcpa&q=85&s=11b1f75bd9a8f95af145c54863c229eb" alt="Uploading a file to the AI chat in Base44" title="Uploading a file to the AI chat in Base44" className="mx-auto" style={{ width:"79%" }} width="1114" height="862" data-path="images/2025-10-05_15-44-20.png" />

<Card title="File upload limits in the chat" icon="upload">
  **Images:** PNG, JPG, JPEG, GIF

  * Max size: 40MB
  * Max dimensions: 1024×1024 pixels (larger images are resized automatically)
  * Example: Upload a screenshot of a website you like and say: “Use this header style for my homepage.”

  **Documents and text files:** PDF, TXT, HTML, DOCX, MD

  * Max size:
    * PDF: 10MB
    * TXT and HTML: 5MB
    * DOCX and MD: 5MB
  * Example: Upload a PRD or brand guide so the AI follows your product and style rules, or share a markdown file with requirements for a new app.

  **Data files:** CSV, XLS, XLSX, JSON

  * Max size:
    * CSV and JSON: 10MB
    * XLS and XLSX: 15MB
  * Example: Upload a CSV, Excel, or JSON file with your existing business data and ask the AI to analyze it, suggest entities and fields, propose a data model for your app, or prepare the data for import. To learn how to import the data into your tables, see [Managing your app data](/Building-your-app/Managing-your-app-data).

  **Videos:** Not supported.
</Card>

<Tip>
  **Tip:** You can also ask the AI to add images to your app, and it will create them using AI.
</Tip>

***

## Sharing media on your live app

Let your users upload media directly in your live app. You and your users can share, download, or interact with content to create a more engaging experience.

Just tell the AI chat what you want your users to be able to do, and the AI will set it up for you. This feature uses the built-in UploadFile integration. Files that people upload can also be processed in your backend code to, for example, read data from receipts, forms, spreadsheets, or JSON files.

<img src="https://mintcdn.com/base44/iWAI9SeWmmB3Mcpa/images/2025-10-05_16-23-13.png?fit=max&auto=format&n=iWAI9SeWmmB3Mcpa&q=85&s=37f6d6c33497cfafd46b58597f535508" alt="Adding a file upload option for people using your Base44 app" title="Adding a file upload option for people using your Base44 app" className="mx-auto" style={{ width:"40%" }} width="392" height="677" data-path="images/2025-10-05_16-23-13.png" />

<Card title="File upload limits on your live app" icon="upload">
  * **Images:** PNG, JPG, JPEG, WEBP (max size: 50MB)
  * **Documents:** PDF, TXT, HTML (max size: 50MB)
  * **Data files:** CSV, XLS, XLSX, JSON (max size: 50MB)
  * **Video:** MP4 (max size: 50MB)
  * **Audio:** MP3, WAV (max size: 50MB)
</Card>

***

## Customizing your app’s logo

Personalize your app by adding a logo. Your logo is visible to users when they add your [app to their home screen](https://docs.base44.com/Building-your-app/Mobile-experience#installing-your-app-to-the-home-screen) and also appears as the browser favicon.

**To change your logo:**

1. Go to your app’s dashboard and click **Overview**.
2. Click the **Edit** icon on the logo and either:
   * Upload your own image file
   * Click **Generate Logo** to create a new one with the AI

<img src="https://mintcdn.com/base44/iWAI9SeWmmB3Mcpa/images/2025-10-05_15-56-24.png?fit=max&auto=format&n=iWAI9SeWmmB3Mcpa&q=85&s=e78075922b5d3a6a40bac5caa5a88a1c" alt="Changing your app's logo in Base44" width="1386" height="239" data-path="images/2025-10-05_15-56-24.png" />

<Note>
  Logos generated in Base44 can only be used within your app and cannot be exported.
</Note>

<Card title="File limits for your logo" icon="file-image">
  * **Image formats:** PNG, JPG, JPEG
  * **Max size:** 5MB
  * **Max dimensions:** 1024×1024 pixels (larger images are resized automatically)

  For best results, use a clear, square image with a transparent background.
</Card>

***

## FAQs

Click a question below to learn more.

<AccordionGroup>
  <Accordion title="Why isn't my file uploading to the AI chat?">
    If your file isn't uploading to the chat, it's most likely because the file is too large or the wrong format. Review the limits above and try again.
  </Accordion>

  <Accordion title="Why am I seeing an error that my image does not match the provided media type?">
    This error can happen if you upload an image that was renamed to PNG, JPG, or JPEG without converting it properly (for example, changing the file name from `.webp` to `.png`).

    **To fix this:**

    * Try reverting your last message if you just uploaded the image.
    * Check that your file is one of the supported formats listed in the [Media guide](https://docs.base44.com/Building-your-app/Using-media) and has not simply been renamed from another file type.
    * Make sure your file does not exceed the size limits set in the Media guide.
    * Try uploading your file again using a supported format.

    If you still have trouble after these steps, [contact support](https://docs.base44.com/Community-and-support/Contacting-support) for help.
  </Accordion>

  <Accordion title="Can I change my logo at any time?">
    Yes, you can replace your logo image at any time from your dashboard inside the app editor. The new logo will appear once your changes are published.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).