# Source: https://firebase.google.com/docs/ai-logic/solutions/cloud-storage.md.txt

|---|
| *Only available when using the Vertex AI Gemini API as your API provider.* |

<br />

When calling the Vertex AI Gemini API from your app using a
Firebase AI Logic SDK, you can prompt a Gemini model to generate text
based on a multimodal input, like images, PDFs, video, and audio.

For the non-text parts of the input (like media files), you can optionally use
[Cloud Storage for Firebase](https://firebase.google.com/docs/storage) to include files in the request. At a
high-level, here's what you need to know about this feature:

- You can use Cloud Storage for Firebase with any multimodal request (like both
  text generation and chat) if you're using the Vertex AI Gemini API.
  The [examples](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#include-file-info-in-request) in this guide show a basic
  text-and-image input.

- You specify the file's MIME type and its Cloud Storage for Firebase URL
  (which always begin with `gs://`) in the request input. These values are
  metadata automatically assigned to any file uploaded to a Cloud Storage
  bucket.

- You need to use a supported [file type and URL](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#supported-files-and-urls).

> [!IMPORTANT]
> **Important:** **For Firebase AI Logic SDKs, the maximum request size is
> 20 MB** . You get an HTTP 413 error if a request is too large.   
>
> If a file's size will make the total request size *exceed 20 MB* , then you'll need to [provide the file using a URL](https://firebase.google.com/docs/ai-logic/input-file-requirements#provide-file-using-url) (for example, by using a Cloud Storage for Firebase URL, as described on this page). However, if a file is small, you can often pass it directly as inline data (note though, that a file provided as inline data is encoded to base64 in transit, which increases the size of the request).

<br />

This solution guide describes how to set up Cloud Storage for Firebase, upload a
file to a Cloud Storage for Firebase bucket from your app, and then include the
file's MIME type and Cloud Storage for Firebase URL in your multimodal request to
the Gemini API.

**Do you want to see the code examples? Or have you already set up
Cloud Storage for Firebase and you're ready to start using it with your
multimodal requests?**

[Jump to the code examples](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#include-file-info-in-request)

## Why use Cloud Storage for Firebase with your app?

[Cloud Storage for Firebase](https://firebase.google.com/docs/storage) uses the same fast, secure, and
scalable infrastructure as Google Cloud Storage to store blobs and files,
and its *client SDKs* are specifically built for mobile and web apps.

For Firebase AI Logic SDKs, the maximum request size is 20 MB.
You get an HTTP 413 error if a request is too large. **If a file's size will
make the total request size exceed 20 MB, then use a
Cloud Storage for Firebase URL to include the file in your multimodal request.**
However, if a file is small, you can often pass it directly as inline data
(note though, that a file provided as inline data is encoded to base64 in
transit, which increases the size of the request).

**Here are some additional benefits of using Cloud Storage for Firebase:**

- You can have end users upload images directly from your app into a
  Cloud Storage for Firebase bucket, and then you can include those images in
  your multimodal prompts just by specifying the file's MIME type and
  Cloud Storage for Firebase URL (which is an identifier for the file).

- You can save your end users time and bandwidth if they need to provide images,
  especially if they have poor or flaky network quality.

  - If a file upload or download gets interrupted, the Cloud Storage for Firebase SDKs automatically restart the operation right where it left off.
  - The same uploaded file can be used multiple times without the end user having to upload the same file each time its needed in your app (like in a new multimodal request).
- You can restrict end user access to files stored in
  Cloud Storage for Firebase by using [Firebase Security Rules](https://firebase.google.com/docs/storage/security),
  which allow only an authorized user to upload, download, or delete files.

- You can access the files in your bucket from Firebase or from Google Cloud,
  giving you the flexibility to do server-side processing such as image
  filtering or video transcoding using the Google Cloud Storage APIs.

## What types of files and URLs are supported?

Here are the requirements for files and URLs when you want to use
Cloud Storage for Firebase URLs with the Firebase AI Logic SDKs:

- The file must meet the
  [requirements of input files for multimodal requests](https://firebase.google.com/docs/ai-logic/input-file-requirements).
  This includes requirements like MIME type and file size.

- The file must be stored in a [Cloud Storage for Firebase](https://firebase.google.com/docs/storage) bucket
  (which means the bucket is accessible to Firebase services, like Firebase Security Rules).
  If you can view your bucket in the
  [Firebase console](https://console.firebase.google.com/project/_/storage/),
  then it's a Cloud Storage for Firebase bucket.

- The Cloud Storage for Firebase bucket must be in the same Firebase project in
  which you registered your app.

- The file's Cloud Storage for Firebase URL must begin with `gs://`, which is the
  way that all Google Cloud Storage URLs are constructed.

- The file's URL cannot be a "browser" URL (for example, the URL of an image
  that you find on the internet).

Also, the [Firebase Security Rules](https://firebase.google.com/docs/storage/security) for your bucket must allow
appropriate access to the file. For example:

- If you have [public rules](https://firebase.google.com/docs/storage/security/rules-conditions#public),
  then *any* user or client can access the file.

- If you have [robust rules](https://firebase.google.com/docs/rules/basics#content-owner_only_access)
  *(strongly recommended)*, then Firebase will check that the signed in user or
  client has sufficient access to the file before allowing the call to go
  through with the provided URL.

> [!CAUTION]
> **Caution:** **Public rules should only be used to get started and during early
> prototyping** (unless the files are actually meant to be wholly publicly accessible files).

## Use Cloud Storage for Firebase URLs with Firebase AI Logic


|---|
| *Only available when using the Vertex AI Gemini API as your API provider.* |

<br />

### **Step 1** : Set up Cloud Storage for Firebase

You can find detailed instructions for setting up Cloud Storage for Firebase in
its getting started guide:
[iOS+](https://firebase.google.com/docs/storage/ios/start) \|
[Android](https://firebase.google.com/docs/storage/android/start) \|
[Web](https://firebase.google.com/docs/storage/web/start) \|
[Flutter](https://firebase.google.com/docs/storage/flutter/start) \|
[Unity](https://firebase.google.com/docs/storage/unity/start)

Here are the high-level tasks that you'll need to do:

1. Create or import a Cloud Storage for Firebase bucket in your Firebase
   project.

2. Apply [Firebase Security Rules](https://firebase.google.com/docs/storage/security) to this bucket. Security Rules
   help you secure your files by restricting access to authorized end users.

   > [!IMPORTANT]
   > **Important:** To get started or during early prototyping, you can consider setting these Security Rules for [public access](https://firebase.google.com/docs/storage/security/rules-conditions#public), but we *strongly recommend* that you **apply more robust Firebase Security Rules once you
   > start seriously developing your app and *especially* before going to
   > production**.

3. Add the client library for Cloud Storage for Firebase to your app.

   Note that you can skip this task, but you must then *always*
   [explicitly include the MIME type and URL values in your requests](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#include-file-info-explicitly).

### **Step 2**: Upload a file to a bucket

In the Cloud Storage documentation, you can learn all the different
ways to upload files to a bucket. For example, you can upload local files from
the end-user's device, such as photos and videos from the camera.
Learn more:
[iOS+](https://firebase.google.com/docs/storage/ios/upload-files) \|
[Android](https://firebase.google.com/docs/storage/android/upload-files) \|
[Web](https://firebase.google.com/docs/storage/web/upload-files) \|
[Flutter](https://firebase.google.com/docs/storage/flutter/upload-files) \|
[Unity](https://firebase.google.com/docs/storage/unity/upload-files)

When you upload a file to a bucket, Cloud Storage automatically applies
the following two pieces of information to the file. You'll need to include
these values in the request (as shown in the next step of this guide).

- **MIME type** : This is the media type of the file (for example, `image/png`).
  We'll automatically try to detect the MIME type during upload and apply that
  metadata to the object in the bucket. However, you can optionally specify the
  MIME type during upload.

- **Cloud Storage for Firebase URL** : This is a unique identifier for the file.
  The URL must start with `gs://`.

### **Step 3**: Include the file's MIME type and URL in a multimodal request

Once you have a file stored in a bucket, you can include its MIME type and URL
in a request. Note that these examples show a non-streaming `generateContent`
request, but you can also use URLs with streaming and chat.

> [!IMPORTANT]
> **Important:** Make sure to review which [types of files and URLs](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#supported-files-and-urls) are supported by Firebase AI Logic SDKs.

To include the file in the request, you can use either of the following options:

- **Option 1:** [Include the MIME type and URL using a Storage reference](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#include-file-info-with-reference)

- **Option 2:** [Include the MIME type and URL explicitly](https://firebase.google.com/docs/ai-logic/solutions/cloud-storage#include-file-info-explicitly)

#### Option 1: Include the MIME type and URL using a Storage reference

|---|
| *Before trying this example, make sure that you've completed the [getting started guide for the Firebase AI Logic SDKs](https://firebase.google.com/docs/ai-logic/get-started).* |

Use this option if you've just uploaded the file to the bucket, and you want to
immediately include the file (via a Storage reference) in the request. The call
requires both the MIME type and the Cloud Storage for Firebase URL.

### Swift

    // Upload an image file using Cloud Storage for Firebase.
    let storageRef = Storage.storage().reference(withPath: "images/image.jpg")
    guard let imageURL = Bundle.main.url(forResource: "image", withExtension: "jpg") else {
      fatalError("File 'image.jpg' not found in main bundle.")
    }
    let metadata = try await storageRef.putFileAsync(from: imageURL)

    // Get the MIME type and Cloud Storage for Firebase URL.
    guard let mimeType = metadata.contentType else {
      fatalError("The MIME type of the uploaded image is nil.")
    }
    // Construct a URL in the required format.
    let storageURL = "gs://\(storageRef.bucket)/\(storageRef.fullPath)"

    let prompt = "What's in this picture?"
    // Construct the imagePart with the MIME type and the URL.
    let imagePart = FileDataPart(uri: storageURL, mimeType: mimeType)

    // To generate text output, call generateContent with the prompt and the imagePart.
    let result = try await model.generateContent(prompt, imagePart)
    if let text = result.text {
      print(text)
    }

### Kotlin

^*For Kotlin, the methods in this SDK are suspend functions and need to be called
from a [Coroutine scope](https://developer.android.com/kotlin/coroutines).*^

    // Upload an image file using Cloud Storage for Firebase.
    val storageRef = Firebase.storage.reference.child("images/image.jpg")
    val fileUri = Uri.fromFile(File("image.jpg"))
    try {
        val taskSnapshot = storageRef.putFile(fileUri).await()
        // Get the MIME type and Cloud Storage for Firebase file path.
        val mimeType = taskSnapshot.metadata?.contentType
        val bucket = taskSnapshot.metadata?.bucket
        val filePath = taskSnapshot.metadata?.path

        if (mimeType != null && bucket != null) {
            // Construct a URL in the required format.
            val storageUrl = "gs://$bucket/$filePath"
            // Construct a prompt that includes text, the MIME type, and the URL.
            val prompt = content {
                fileData(mimeType = mimeType, uri = storageUrl)
                text("What's in this picture?")
            }
            // To generate text output, call generateContent with the prompt.
            val response = model.generateContent(prompt)
            println(response.text)
        }
    } catch (e: StorageException) {
        // An error occurred while uploading the file.
    } catch (e: GoogleGenerativeAIException) {
        // An error occurred while generating text.
    }

### Java

^*For Java, the methods in this SDK return a
[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture).*^

    // Upload an image file using Cloud Storage for Firebase.
    StorageReference storage = FirebaseStorage.getInstance().getReference("images/image.jpg");
    Uri fileUri = Uri.fromFile(new File("images/image.jpg"));

    storage.putFile(fileUri).addOnSuccessListener(taskSnapshot -> {
        // Get the MIME type and Cloud Storage for Firebase file path.
        String mimeType = taskSnapshot.getMetadata().getContentType();
        String bucket = taskSnapshot.getMetadata().getBucket();
        String filePath = taskSnapshot.getMetadata().getPath();

        if (mimeType != null && bucket != null) {
            // Construct a URL in the required format.
            String storageUrl = "gs://" + bucket + "/" + filePath;
            // Create a prompt that includes text, the MIME type, and the URL.
            Content prompt = new Content.Builder()
                    .addFileData(storageUrl, mimeType)
                    .addText("What's in this picture?")
                    .build();

            // To generate text output, call generateContent with the prompt.
            GenerativeModelFutures modelFutures = GenerativeModelFutures.from(model);
            ListenableFuture<GenerateContentResponse> response = modelFutures.generateContent(prompt);
            Futures.addCallback(response, new FutureCallback<>() {
                @Override
                public void onSuccess(GenerateContentResponse result) {
                    String resultText = result.getText();
                    System.out.println(resultText);
                }

                @Override
                public void onFailure(@NonNull Throwable t) {
                    t.printStackTrace();
                }
            }, executor);
        }
    }).addOnFailureListener(e -> {
        // An error occurred while uploading the file.
        e.printStackTrace();
    });

### Web

    // Upload an image file using Cloud Storage for Firebase.
    const storageRef = ref(storage, "image.jpg");
    const uploadResult = await uploadBytes(storageRef, file);

    // Get the MIME type and Cloud Storage for Firebase URL.
    // toString() is the simplest way to construct the Cloud Storage for Firebase URL
    // in the required format.
    const mimeType = uploadResult.metadata.contentType;
    const storageUrl = uploadResult.ref.toString();

    // Construct the imagePart with the MIME type and the URL.
    const imagePart = { fileData: { mimeType, fileUri: storageUrl }};

    // To generate text output, call generateContent with the prompt and imagePart.
    const result = await model.generateContent([prompt, imagePart]);
    console.log(result.response.text());

### Dart

    // Upload an image file using Cloud Storage for Firebase.
    final storageRef = FirebaseStorage.instance.ref();
    final imageRef = storageRef.child("images/image.jpg");
    await imageRef.putData(data);

    // Get the MIME type and Cloud Storage for Firebase file path.
    final metadata = await imageRef.getMetadata();
    final mimeType = metadata.contentType;
    final bucket = imageRef.bucket;
    final fullPath = imageRef.fullPath;

    final prompt = TextPart("What's in the picture?");
    // Construct a URL in the required format.
    final storageUrl = 'gs://$bucket/$fullPath';
    // Construct the filePart with the MIME type and the URL.
    final filePart = FileData(mimeType, storageUrl);
    // To generate text output, call generateContent with the text and the filePart.
    final response = await model.generateContent([
      Content.multi([prompt, filePart])
    ]);
    print(response.text);

### Unity

    var storageRef = FirebaseStorage.DefaultInstance.GetReference("images/image.jpg");
    var metadata = await storageRef.PutFileAsync(filePathToJpg);

    // Get the MIME type and Cloud Storage for Firebase URL.
    var mimeType = metadata.ContentType;
    // Construct a URL in the required format.
    var storageURL = new Uri($"gs://{storageRef.Bucket}/{storageRef.Path}");

    var prompt = ModelContent.Text("What's in this picture?");
    // Construct a FileData that explicitly includes the MIME type and
    // Cloud Storage for Firebase URL values.
    var fileData = ModelContent.FileData(mimeType, storageURL);

    // To generate text output, call GenerateContentAsync with the prompt and fileData.
    var response = await model.GenerateContentAsync(new [] { prompt, fileData });
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");

#### Option 2: Include the MIME type and URL explicitly

|---|
| *Before trying this example, make sure that you've completed the [getting started guide for the Firebase AI Logic SDKs](https://firebase.google.com/docs/ai-logic/get-started).* |

Use this option if you know the values for the MIME type and
Cloud Storage for Firebase URL, and you want to include them explicitly in the
multimodal request. The call requires both the MIME type and the URL.

### Swift

    let prompt = "What's in this picture?"
    // Construct an imagePart that explicitly includes the MIME type and
    // Cloud Storage for Firebase URL values.
    let imagePart = FileDataPart(uri: "gs://bucket-name/path/image.jpg", mimeType: "image/jpeg")

    // To generate text output, call generateContent with the prompt and imagePart.
    let result = try await model.generateContent(prompt, imagePart)
    if let text = result.text {
      print(text)
    }

### Kotlin

^*For Kotlin, the methods in this SDK are suspend functions and need to be called
from a [Coroutine scope](https://developer.android.com/kotlin/coroutines).*^

    // Construct a prompt that explicitly includes the MIME type and Cloud Storage for Firebase URL values.
    val prompt = content {
        fileData(mimeType = "image/jpeg", uri = "gs://bucket-name/path/image.jpg")
        text("What's in this picture?")
    }
    // To generate text output, call generateContent with the prompt.
    val response = model.generateContent(prompt)
    println(response.text)

### Java

^*For Java, the methods in this SDK return a
[`ListenableFuture`](https://developer.android.com/guide/background/asynchronous/listenablefuture).*^

    // Construct a prompt that explicitly includes the MIME type and Cloud Storage for Firebase URL values.
    Content prompt = new Content.Builder()
            .addFilePart("gs://bucket-name/path/image.jpg", "image/jpeg")
            .addText("What's in this picture?")
            .build();

    // To generate text output, call generateContent with the prompt
    GenerativeModelFutures modelFutures = GenerativeModelFutures.from(model);
    ListenableFuture<GenerateContentResponse> response = modelFutures.generateContent(prompt);
    Futures.addCallback(response, new FutureCallback<>() {
        @Override
        public void onSuccess(GenerateContentResponse result) {
            String resultText = result.getText();
            System.out.println(resultText);
        }

        @Override
        public void onFailure(@NonNull Throwable t) {
            t.printStackTrace();
        }
    }, executor);

### Web

    const prompt = "What's in this picture?";
    // Construct an imagePart that explicitly includes the MIME type and Cloud Storage for Firebase URL values.
    const imagePart = { fileData: { mimeType: "image/jpeg", fileUri: "gs://bucket-name/path/image.jpg" }};

    // To generate text output, call generateContent with the prompt and imagePart.
    const result = await model.generateContent([prompt, imagePart]);
    console.log(result.response.text());

### Dart

    final prompt = TextPart("What's in the picture?");
    // Construct a filePart that explicitly includes the MIME type and Cloud Storage for Firebase URL values.
    final filePart = FileData('image/jpeg', 'gs://bucket-name/path/image.jpg'),
    // To generate text output, call generateContent with the prompt and filePart.
    final response = await model.generateContent([
      Content.multi([prompt, filePart])
    ]);
    print(response.text);

### Unity

    var prompt = ModelContent.Text("What's in this picture?");
    // Construct a FileData that explicitly includes the MIME type and
    // Cloud Storage for Firebase URL values.
    var fileData = ModelContent.FileData(
      mimeType: "image/jpeg",
      uri: new Uri("gs://bucket-name/path/image.jpg")
    );

    // To generate text output, call GenerateContentAsync with the prompt and fileData.
    var response = await model.GenerateContentAsync(new [] { prompt, fileData });
    UnityEngine.Debug.Log(response.Text ?? "No text in response.");