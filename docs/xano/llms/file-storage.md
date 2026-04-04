# Source: https://docs.xano.com/xanoscript/function-reference/file-storage.md

# Source: https://docs.xano.com/the-function-stack/functions/file-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# File Storage

### Read more about how file management works in Xano

<Card icon="download" href="/file-storage/file-storage-in-xano">
  File Storage in Xano
</Card>

## The Content Upload Flow

When working with files in Xano, they can exist in a few different states.

* **File Resource**
  * The file resource can be thought of as a reference to your raw file data. It is a base64 encoded string that represents the file during execution, enabling you to pass the data through variables and functions that handle content management with ease.
* **Raw File Data**
  * When necessary, you do also have the ability to turn your file resource into raw file data, and manipulate it inside of the function stack when appropriate, such as a CSV file.
* **Metadata**
  * While the metadata is not a representation of the file data itself, the metadata is necessary when the file needs to be referenced inside of a database table. The tables do not store the files themselves, but hold onto the metadata, so that when the record is retrieved, you can also retrieve the file data, or deliver a link to the file.

Files in Xano always start with a **file resource**. Here's what a typical flow looks like. In this example, we'll be adding a file to our database table.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a569ea93-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=7278afce26042eaf7bacba9867c46013" width="2203" height="1275" data-path="images/a569ea93-image.jpeg" />
</Frame>

1. Files in a function stack always start with a \*\*file resource. \*\*The file resource can come via a **file resource input**, or by using a **Create File Resource** function in the function stack itself (such as if the file comes from an external API request).
2. After we have our file resource (in this case, our File Resource input), we need to generate **metadata** for that file in preparation to store it in our database table.
3. Finally, once we have our **metadata**, we can write it to our database table, adding the metadata to the appropriate field in the record.

This is the simplest and most typical scenario when working with files in Xano. Following this flow will allow you to ingest files through your API and store them in your database. You can then read the metadata from the table and use the URL from there to deliver those files back to your front-end.

## Input, Field Types, and Functions

### The File Resource Input

Your content upload function stacks should always start with a **file resource input**, if your users are uploading files through your application. You can then utilize the file resource input in future functions, such as \*\*metadata generation, \*\*to store the file in your database or return a URL to the file.

### Field Types

Xano supports several different field types in the database related to content upload.

* **Image** - For storing images
* **Video** - For storing video
* **Audio** - For storing audio
* **Attachment** - For storing anything else

### Functions

The Content Upload Functions are:

* **Create Image Metadata** - Creates image metadata from a file resource so that it can be formatted properly to be stored in Xano.

* **Create Video Metadata** - Creates video metadata from a file resource so that it can be formatted properly to be stored in Xano.

* **Create Audio Metadata** - Creates auto metadata from a file resource so that it can be formatted properly to be stored in Xano

* **Create Attachment Metadata** - Creates attachment metadata from a file resource so that it can be formatted properly to be stored in Xano.

* **Create File Resource** - This functions is able to create a file resource in the function stack from a variable. Typically, you will use a file resource as an input. However, there are certain use cases, for example, where you may hit an external API which is providing you with a raw image or file. In this event, you will want to first use this function to create a file resource then use one of the create metadata functions.

* **Delete File Resource** - This function will permanently delete a file stored in your Xano file storage. You'll usually pair this with a database operation like Get Record / Query All Records, or you can delete a file created earlier in your function stack as long as one of the Metadata functions have been executed, as the Delete File Resource function requires you to specify the path to the file. **Files are not recoverable. Proceed with caution**.

* **Zip: Create File Resource** - Creates a new, empty zip file that you can add files to in your function stack

* **Zip: Add File Resource** - Used to add additional files into an existing zip file

* **Zip: Remove File Resource** - Used to remove files from an existing zip file

* **Zip: Extract Zip File Resource** - Used to extract a zip file and generate separate file resources for each file extracted

* **Zip: View Contents** - Show details about the files contained inside of a zip file

## Serving File Downloads

There are a couple of different ways you can serve downloads of files, depending on your use case.

<Steps>
  <Step title="Provide the URL for your frontend to process.">
    When you use one of the **Create Metadata** steps to store the file in your Xano files library, it returns a **path** key which contains a path to the file.

    Returning a complete URL requires prepending this path with the URL to your Xano instance.

    If our metadata looks like this...

    ```json  theme={null}
    {
        "access":"public",
        "path":"/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf",
        "name":"form_submission_1741703680742.pdf",
        "type":"pdf",
        "size":3247192,
        "mime":"application/pdf",
        "meta":{
            "validated":false
            }
        }
    ```

    ...our full URL would look like this:

    ```
    https://my-xano-instance.xano.io/vault/T3q1DKy7/MA_gz1v6HaNQnLEf6xZqVtrOVII/1Rl7QA../form_submission_1741703680742.pdf
    ```
  </Step>

  <Step title="Serve the raw file contents for direct download.">
    If you want an API call to immediately initiate a file download, add the following headers to your function stack using the [**HTTP Header**](/the-function-stack/functions/utility-functions#http-header) function.

    1. `Content-Disposition: attachment; filename="replaceme"`
    2. `Content-Type: application/octet-stream`

    These headers will tell any browser accessing the API that we're serving a direct download. Just make sure to change "replaceme" to the actual filename you are serving.

    Add a **Get File Resource Data** function so we have the raw file data to be delivered.

    Finally, in your response, return the .`data `path from the output of **Get File Resource Data**.

    Your function stack should look something like this:

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/aa282fa3-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=041b830f0e70b1d920c6b3e8d945f853" width="1188" height="299" data-path="images/aa282fa3-image.jpeg" />
    </Frame>

    To ensure it's working as expected, when you run it in Xano, you should see a **Download** button available in the Run panel.

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/p57kHPQ04p_0aEqF/images/b656ac41-image.jpeg?fit=max&auto=format&n=p57kHPQ04p_0aEqF&q=85&s=64853e3f72bf1e5de3d55e02d3bd5a32" width="600" height="322" data-path="images/b656ac41-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Private File Storage

Private file storage is available as a premium add-on for our Launch plans, or included with **Scale** or HIPAA compliance.

All files stored as private files are only accessible through on-demand time sensitive URL generation. This means that all files in your Private Storage are inaccessible until you generate a new URL in your function stack.

To work with private file storage, there are two key components to understand: **private file database fields** and the **Private File: Sign URL function.**

### **Private File Database Field**

To store files in your private files library and have them accessible from your function stacks, you'll need to use a database field that is enabled for private file storage. You can enable this for any of the current file field types. Keep in mind that the file access is defined per field, which means that you can not store both public and private files in the same field.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/Qia2QBMIuWWrGb-s/images/1f74d1f5-image.jpeg?fit=max&auto=format&n=Qia2QBMIuWWrGb-s&q=85&s=18ef1ed61f9b0b397a098599764f0071" width="494" height="745" data-path="images/1f74d1f5-image.jpeg" />
</Frame>

When private files are enabled for a file storage field, a lock icon is displayed in the field name. You will also notice that private files do not display previews from the database view; this is by design, as the files are not accessible until a new URL is generated.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c36c2b6f-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=0172b0534949d1447d26e4d1f6144580" width="726" height="249" data-path="images/c36c2b6f-image.jpeg" />
</Frame>

### **Private File: Sign URL function**

To generate a signed URL that enables a private file to be accessible, you first need to retrieve the path of the file, which is stored in the database record. In this example, we have queried our files table and this is the expected return for a private image. The main difference here is that on public files, a URL is returned. For private files, no URL is provided.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c260b48f-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=046927391a1ee485cd398d283fd29482" width="592" height="577" data-path="images/c260b48f-image.jpeg" />
</Frame>

We can then leverage the **Private File: Sign URL** function to generate a publicly accessible link to the file. Provide the path as offered from the database record, a TTL (how long in seconds the link should be valid for), and finally a return variable to contain the output of the function

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/c86d4c75-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=212ee5e0e44b0abf8f7517908bdccd8b" width="1190" height="961" data-path="images/c86d4c75-image.jpeg" />
</Frame>

When we run this function, we are returned our new signed URL.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/c30ad1d2-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=7cb055bfa0a7f980285560b3d7b9e314" width="588" height="414" data-path="images/c30ad1d2-image.jpeg" />
</Frame>

## Zip Management

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/XORZu0GGHzY" title="Zip Files in Xano - How to Read, Process, and Create Zip Files" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

### Viewing Zip File Contents

In this example, all we want to do is upload a zip file and review its contents in our function stack.

We've added our file resource input to ingest the file, and then utilize the **Zip: View Contents** function, targeting our file resource input. We can also provide a password to this function if our zip file requires one to open.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/tjSJ_pOzk8E0WRhF/images/bfeeaee4-image.jpeg?fit=max&auto=format&n=tjSJ_pOzk8E0WRhF&q=85&s=ed366e77b3c4f8fa650eecc3be179f9a" width="2216" height="1264" data-path="images/bfeeaee4-image.jpeg" />
</Frame>

1. **Zip: View Contents** - Returns the contents of our zip file to a variable

### Extracting a Zip File

In this example, our users will be uploading a zip file. We then want to extract all of those files from the zip file in order to add those files individually to our database.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/NAqNmVIgcJlXegps/images/0856afea-image.jpeg?fit=max&auto=format&n=NAqNmVIgcJlXegps&q=85&s=a0f878b6c7135c7fec08f66b32a42709" width="2098" height="1318" data-path="images/0856afea-image.jpeg" />
</Frame>

1. **Create Attachment Metadata** - Creates metadata for the uploaded zip file so we can get the filename
2. **Zip: Extract Zip File Resource** - Extracts the zip file and returns individual file resources for each file
   <Frame>
     <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/6efcbb5d-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=9e99cb81fd9e072d364aa5d401c8d885" width="634" height="725" data-path="images/6efcbb5d-image.jpeg" />
   </Frame>
3. **Create Variable** - Creates an empty array to store our individual files metadata
4. **For Each Loop** - Loops against the array of file resources created in step 2
   1. **Conditional** - Checks for junk files generated by Mac OS and skips them. This step is optional.
      1. \*\*Create Attachment \*\*- Creates metadata for the file resource that the loop is currently iterating through
      2. **Array: Add to End** - Adds the generated metadata to our metadata array established in step 3
5. **Add Record** - Adds our metadata to the database
6. **Delete File** - Deletes the zip file. This is only necessary if you generate metadata for it as we did in step 1.

### Adding to a zip file

In this example, our users are uploading a zip file, and we want to add another file to that same zip file. We have two file resource inputs: one is for the zip file, and one is for the new file to add.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/o7zunZFYmjx8RZ8N/images/f51f93b1-image.jpeg?fit=max&auto=format&n=o7zunZFYmjx8RZ8N&q=85&s=601cbf75712b97efc92b8029846a97e0" width="2216" height="1320" data-path="images/f51f93b1-image.jpeg" />
</Frame>

1. **Zip: Add File Resource** - Adds the new file into the existing zip file
2. **Zip: View Contents** - Allows us to view the contents of the updated zip file

### Removing from a zip file

In this example, our users are uploading a zip file, as well as specifying a file to remove, and we want to remove that file from the zip file. We have two inputs: a file resource input for the zip file, and a text input for the file name to remove.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/_Sd90ZcMa6hsPScv/images/d21d5ab5-image.jpeg?fit=max&auto=format&n=_Sd90ZcMa6hsPScv&q=85&s=9585c0b58812f98c9cdd5c5f1e9f536d" width="2217" height="1317" data-path="images/d21d5ab5-image.jpeg" />
</Frame>

1. **Zip: Delete File Resource** - Removes the file matching the filename from the existing zip file
2. **Zip: View Contents** - Allows us to view the contents of the updated zip file

### Creating a zip file from scratch

<Info>
  See [Serving File Downloads](/the-function-stack/functions/file-storage#serving-file-downloads) to learn how to provide a download of a created ZIP file.
</Info>

In this example, our users are uploading multiple files, and we want to store them inside of a zip file.

**From multiple file resource inputs**

In this scenario, we have multiple file resource inputs for each incoming file.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/kBkSb_XZ48XRxJA_/images/a638f6bd-image.jpeg?fit=max&auto=format&n=kBkSb_XZ48XRxJA_&q=85&s=17fdfa682363c406fdb41fa09fa61618" width="2218" height="1319" data-path="images/a638f6bd-image.jpeg" />
</Frame>

1. **Zip: Create File Resource** - Creates our zip file that we can add to in the rest of the function stack
2. **Zip: Add File Resource** - Adds the data from file1 into our zip file
3. **Zip: Add File Resource** - Adds the data from file2 into our zip file
4. **Zip: View Contents** - Allows us to review the zip file contents after completion

**From an array of files via a single file resource input**

In this scenario, we have a single file resource input, formatted as a list. This is good if you need to dynamically determine how many files your API is ingesting.

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/7844e525-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=b0808697af213329de8693443b4d30cc" width="2220" height="1321" data-path="images/7844e525-image.jpeg" />
</Frame>

1. **Zip: Create File Resource** - Creates our zip file that we can add to in the rest of the function stack
2. **For Each Loop** - Loops against our list file resource input
   1. **Zip: Add File Resource** - Adds the file the loop is currently iterating through to our zip file established in step 1
3. **Zip: View Contents** - Allows us to review the zip file contents after completion

### A note about encryption

Xano supports creating and working with encrypted zip files. In the zip functions available, you'll notice one or both of the following fields:

<Frame>
  <img src="https://mintcdn.com/xano-997cb9ee/SGxJ0muPK3um9hNH/images/761c9881-image.jpeg?fit=max&auto=format&n=SGxJ0muPK3um9hNH&q=85&s=9cc706e2cee50fc3d9c9c393dd718580" width="660" height="217" data-path="images/761c9881-image.jpeg" />
</Frame>

The **password** field is to set the password you want applied to the zip file.

The **password\_encryption** field is available for you to set the encryption method applied to the zip file upon creation. The following encryption methods are available:

* **Standard** - This is the most compatible form of encryption (Traditional PKWARE encryption). This is required if you need to be able to extract your zip files using Windows' native zip extraction.
* **AES-128**
* **AES-256**
* **AES-512**


Built with [Mintlify](https://mintlify.com).