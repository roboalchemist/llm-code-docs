# Source: https://firebase.google.com/docs/ml/android/recognize-text.md.txt

> [!NOTE]
>
> The Firebase ML Vision SDK for recognizing text in an image is
> now deprecated
> [(See the
> outdated docs here).](https://firebase.google.com/docs/ml/android/recognize-text-deprecated)
> This page describes how, as an alternative to the deprecated SDK, you can
> call Cloud Vision APIs using Firebase Auth and Firebase Functions to allow
> only authenticated users to access the API.


In order to call a Google Cloud API from your app, you need to create an intermediate
REST API that handles authorization and protects secret values such as API keys. You then need to
write code in your mobile app to authenticate to and communicate with this intermediate service.


One way to create this REST API is by using Firebase Authentication and Functions, which gives you a managed, serverless gateway to
Google Cloud APIs that handles authentication and can be called from your mobile app with
pre-built SDKs.


This guide demonstrates how to use this technique to call the Cloud Vision API from your app.
This method will allow all authenticated users to access Cloud Vision billed services through your Cloud project, so
consider whether this auth mechanism is sufficient for your use case before proceeding.
Use of the Cloud Vision APIs is subject to the [Google Cloud Platform License
Agreement](https://cloud.google.com/terms/) and [Service
Specific Terms](https://cloud.google.com/terms/service-terms), and billed accordingly. For billing information, see the [Pricing](https://cloud.google.com/vision/pricing) page.

> [!NOTE]
> **Looking for on-device text recognition?** Try the [standalone ML Kit library](https://developers.google.com/ml-kit/vision/text-recognition).

## Before you begin

<br />

### Configure your project

1. If you haven't already, [add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. If you haven't already enabled Cloud-based APIs for your project, do so
   now:

   1. Open the [Firebase ML
      APIs page](https://console.firebase.google.com/project/_/ml/apis) in the Firebase console.
   2. If you haven't already upgraded your project to the
      [pay-as-you-go Blaze pricing plan](https://firebase.google.com/pricing), click **Upgrade** to do so. (You'll be
      prompted to upgrade only if your project isn't on the
      Blaze pricing plan.)

      Only projects on the Blaze pricing plan can use
      Cloud-based APIs.
   3. If Cloud-based APIs aren't already enabled, click **Enable Cloud-based APIs**.
3. Configure your existing Firebase API keys to disallow access to the Cloud Vision API:
   1. Open the [Credentials](https://console.cloud.google.com/apis/credentials?project=_) page of the Cloud console.
   2. For each API key in the list, open the editing view, and in the Key Restrictions section, add all of the available APIs *except* the Cloud Vision API to the list.

### Deploy the callable function

Next, deploy the Cloud Function you will use to bridge your app and the Cloud
Vision API. The `functions-samples` repository contains an example
you can use.

By default, accessing the Cloud Vision API through this function will allow
only authenticated users of your app access to the Cloud Vision API. You can
modify the function for different requirements.

To deploy the function:

1. Clone or download the [functions-samples repo](https://github.com/firebase/functions-samples) and change to the `Node-1st-gen/vision-annotate-image` directory:

       git clone https://github.com/firebase/functions-samples
       cd Node-1st-gen/vision-annotate-image

2. Install dependencies:

       cd functions
       npm install
       cd ..

3. If you don't have the Firebase CLI, [install it](https://firebase.google.com/docs/cli#setup_update_cli).
4. Initialize a Firebase project in the `vision-annotate-image` directory. When prompted, select your project in the list.

   ```
   firebase init
   ```
5. Deploy the function:

   ```
   firebase deploy --only functions:annotateImage
   ```

### Add Firebase Auth to your app

The callable function deployed above will reject any request from non-authenticated
users of your app. If you have not already done so, you will need to [add Firebase
Auth to your app.](https://firebase.google.com/docs/auth/android/start#add_to_your_app)

### Add necessary dependencies to your app


- Add the dependencies for the Cloud Functions for Firebase (client) and gson Android libraries to your **module (app-level) Gradle file** (usually `<project>/<app-module>/build.gradle.kts` or `<project>/<app-module>/build.gradle`):

  ```
  implementation("com.google.firebase:firebase-functions:22.1.0")
  implementation("com.google.code.gson:gson:2.8.6")
  ```
- Now you are ready to start recognizing text in images.

## 1. Prepare the input image

In order to call Cloud Vision, the image must be formatted as a base64-encoded string. To process an image from a saved file URI:
  1. Get the image as a `Bitmap` object:

     ### Kotlin

     ```kotlin
     var bitmap: Bitmap = MediaStore.Images.Media.getBitmap(contentResolver, uri)
     ```

     ### Java

     ```java
     Bitmap bitmap = MediaStore.Images.Media.getBitmap(getContentResolver(), uri);
     ```
  2. Optionally, scale down the image to save on bandwidth. See the [Cloud Vision recommended image sizes.](https://cloud.google.com/vision/docs/supported-files#image_sizing)

     ### Kotlin

     ```kotlin
     private fun scaleBitmapDown(bitmap: Bitmap, maxDimension: Int): Bitmap {
         val originalWidth = bitmap.width
         val originalHeight = bitmap.height
         var resizedWidth = maxDimension
         var resizedHeight = maxDimension
         if (originalHeight > originalWidth) {
             resizedHeight = maxDimension
             resizedWidth =
                 (resizedHeight * originalWidth.toFloat() / originalHeight.toFloat()).toInt()
         } else if (originalWidth > originalHeight) {
             resizedWidth = maxDimension
             resizedHeight =
                 (resizedWidth * originalHeight.toFloat() / originalWidth.toFloat()).toInt()
         } else if (originalHeight == originalWidth) {
             resizedHeight = maxDimension
             resizedWidth = maxDimension
         }
         return Bitmap.createScaledBitmap(bitmap, resizedWidth, resizedHeight, false)
     }
     ```

     ### Java

     ```java
     private Bitmap scaleBitmapDown(Bitmap bitmap, int maxDimension) {
         int originalWidth = bitmap.getWidth();
         int originalHeight = bitmap.getHeight();
         int resizedWidth = maxDimension;
         int resizedHeight = maxDimension;

         if (originalHeight > originalWidth) {
             resizedHeight = maxDimension;
             resizedWidth = (int) (resizedHeight * (float) originalWidth / (float) originalHeight);
         } else if (originalWidth > originalHeight) {
             resizedWidth = maxDimension;
             resizedHeight = (int) (resizedWidth * (float) originalHeight / (float) originalWidth);
         } else if (originalHeight == originalWidth) {
             resizedHeight = maxDimension;
             resizedWidth = maxDimension;
         }
         return Bitmap.createScaledBitmap(bitmap, resizedWidth, resizedHeight, false);
     }
     ```

     ### Kotlin

     ```kotlin
     // Scale down bitmap size
     bitmap = scaleBitmapDown(bitmap, 640)
     ```

     ### Java

     ```java
     // Scale down bitmap size
     bitmap = scaleBitmapDown(bitmap, 640);
     ```
  3. Convert the bitmap object to a base64 encoded string:

     ### Kotlin

     ```kotlin
     // Convert bitmap to base64 encoded string
     val byteArrayOutputStream = ByteArrayOutputStream()
     bitmap.compress(Bitmap.CompressFormat.JPEG, 100, byteArrayOutputStream)
     val imageBytes: ByteArray = byteArrayOutputStream.toByteArray()
     val base64encoded = Base64.encodeToString(imageBytes, Base64.NO_WRAP)
     ```

     ### Java

     ```java
     // Convert bitmap to base64 encoded string
     ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream();
     bitmap.compress(Bitmap.CompressFormat.JPEG, 100, byteArrayOutputStream);
     byte[] imageBytes = byteArrayOutputStream.toByteArray();
     String base64encoded = Base64.encodeToString(imageBytes, Base64.NO_WRAP);
     ```
The image represented by the `Bitmap` object must be upright, with no additional rotation required.

## 2. Invoke the callable function to recognize text

- To recognize text in an image, invoke the callable function, passing a [JSON Cloud Vision request](https://cloud.google.com/vision/docs/request#json_request_format).
  1. First, initialize an instance of Cloud Functions:

     ### Kotlin

         private lateinit var functions: FirebaseFunctions
         // ...
         functions = Firebase.functions

     ### Java

         private FirebaseFunctions mFunctions;
         // ...
         mFunctions = FirebaseFunctions.getInstance();

  2. Define a method for invoking the function:

     ### Kotlin

         private fun annotateImage(requestJson: String): Task<JsonElement> {
             return functions
                 .getHttpsCallable("annotateImage")
                 .call(requestJson)
                 .continueWith { task ->
                     // This continuation runs on either success or failure, but if the task
                     // has failed then result will throw an Exception which will be
                     // propagated down.
                     val result = task.result?.data
                     JsonParser.parseString(Gson().toJson(result))
                 }
         }

     ### Java

         private Task<JsonElement> annotateImage(String requestJson) {
             return mFunctions
                     .getHttpsCallable("annotateImage")
                     .call(requestJson)
                     .continueWith(new Continuation<HttpsCallableResult, JsonElement>() {
                         @Override
                         public JsonElement then(@NonNull Task<HttpsCallableResult> task) {
                             // This continuation runs on either success or failure, but if the task
                             // has failed then getResult() will throw an Exception which will be
                             // propagated down.
                             return JsonParser.parseString(new Gson().toJson(task.getResult().getData()));
                         }
                     });
         }

  3. Create the JSON request. The Cloud Vision API supports two [Types](https://cloud.google.com/vision/docs/reference/rest/v1/Feature#type)
     of text detection: `TEXT_DETECTION` and `DOCUMENT_TEXT_DETECTION`.
     See the [Cloud Vision OCR Docs](https://cloud.google.com/vision/docs/ocr#optical_character_recognition_ocr)
     for the difference between the two use cases.

     ### Kotlin

         // Create json request to cloud vision
         val request = JsonObject()
         // Add image to request
         val image = JsonObject()
         image.add("content", JsonPrimitive(base64encoded))
         request.add("image", image)
         // Add features to the request
         val feature = JsonObject()
         feature.add("type", JsonPrimitive("TEXT_DETECTION"))
         // Alternatively, for DOCUMENT_TEXT_DETECTION:
         // feature.add("type", JsonPrimitive("DOCUMENT_TEXT_DETECTION"))
         val features = JsonArray()
         features.add(feature)
         request.add("features", features)

     ### Java

         // Create json request to cloud vision
         JsonObject request = new JsonObject();
         // Add image to request
         JsonObject image = new JsonObject();
         image.add("content", new JsonPrimitive(base64encoded));
         request.add("image", image);
         //Add features to the request
         JsonObject feature = new JsonObject();
         feature.add("type", new JsonPrimitive("TEXT_DETECTION"));
         // Alternatively, for DOCUMENT_TEXT_DETECTION:
         //feature.add("type", new JsonPrimitive("DOCUMENT_TEXT_DETECTION"));
         JsonArray features = new JsonArray();
         features.add(feature);
         request.add("features", features);

     Optionally, [provide language hints](https://cloud.google.com/vision/docs/ocr#specify_the_language_optional)
     to assist with language detection (see [supported languages](https://cloud.google.com/vision/docs/languages)):

     ### Kotlin

         val imageContext = JsonObject()
         val languageHints = JsonArray()
         languageHints.add("en")
         imageContext.add("languageHints", languageHints)
         request.add("imageContext", imageContext)

     ### Java

         JsonObject imageContext = new JsonObject();
         JsonArray languageHints = new JsonArray();
         languageHints.add("en");
         imageContext.add("languageHints", languageHints);
         request.add("imageContext", imageContext);

  4. Finally, invoke the function:

     ### Kotlin

         annotateImage(request.toString())
             .addOnCompleteListener { task ->
                 if (!task.isSuccessful) {
                     // Task failed with an exception
                     // ...
                 } else {
                     // Task completed successfully
                     // ...
                 }
             }

     ### Java

         annotateImage(request.toString())
                 .addOnCompleteListener(new OnCompleteListener<JsonElement>() {
                     @Override
                     public void onComplete(@NonNull Task<JsonElement> task) {
                         if (!task.isSuccessful()) {
                             // Task failed with an exception
                             // ...
                         } else {
                             // Task completed successfully
                             // ...
                         }
                     }
                 });

## 3. Extract text from blocks of recognized text

If the text recognition operation succeeds, a JSON response of [BatchAnnotateImagesResponse](https://cloud.google.com/vision/docs/reference/rest/v1/BatchAnnotateImagesResponse) will be returned in the task's result. The text annotations can be found in the [`fullTextAnnotation`](https://cloud.google.com/vision/docs/reference/rest/v1/AnnotateImageResponse#textannotation) object.
- You can get the recognized text as a string in the `text` field. For example:

### Kotlin

    val annotation = task.result!!.asJsonArray[0].asJsonObject["fullTextAnnotation"].asJsonObject
    System.out.format("%nComplete annotation:")
    System.out.format("%n%s", annotation["text"].asString)

### Java

    JsonObject annotation = task.getResult().getAsJsonArray().get(0).getAsJsonObject().get("fullTextAnnotation").getAsJsonObject();
    System.out.format("%nComplete annotation:%n");
    System.out.format("%s%n", annotation.get("text").getAsString());

- You can also get information specific to regions of the image. For each `block`, `paragraph`, `word`, and `symbol`, you can get the text recognized in the region and the bounding coordinates of the region. For example:

### Kotlin

    for (page in annotation["pages"].asJsonArray) {
        var pageText = ""
        for (block in page.asJsonObject["blocks"].asJsonArray) {
            var blockText = ""
            for (para in block.asJsonObject["paragraphs"].asJsonArray) {
                var paraText = ""
                for (word in para.asJsonObject["words"].asJsonArray) {
                    var wordText = ""
                    for (symbol in word.asJsonObject["symbols"].asJsonArray) {
                        wordText += symbol.asJsonObject["text"].asString
                        System.out.format(
                            "Symbol text: %s (confidence: %f)%n",
                            symbol.asJsonObject["text"].asString,
                            symbol.asJsonObject["confidence"].asFloat,
                        )
                    }
                    System.out.format(
                        "Word text: %s (confidence: %f)%n%n",
                        wordText,
                        word.asJsonObject["confidence"].asFloat,
                    )
                    System.out.format("Word bounding box: %s%n", word.asJsonObject["boundingBox"])
                    paraText = String.format("%s%s ", paraText, wordText)
                }
                System.out.format("%nParagraph: %n%s%n", paraText)
                System.out.format("Paragraph bounding box: %s%n", para.asJsonObject["boundingBox"])
                System.out.format("Paragraph Confidence: %f%n", para.asJsonObject["confidence"].asFloat)
                blockText += paraText
            }
            pageText += blockText
        }
    }

### Java

    for (JsonElement page : annotation.get("pages").getAsJsonArray()) {
        StringBuilder pageText = new StringBuilder();
        for (JsonElement block : page.getAsJsonObject().get("blocks").getAsJsonArray()) {
            StringBuilder blockText = new StringBuilder();
            for (JsonElement para : block.getAsJsonObject().get("paragraphs").getAsJsonArray()) {
                StringBuilder paraText = new StringBuilder();
                for (JsonElement word : para.getAsJsonObject().get("words").getAsJsonArray()) {
                    StringBuilder wordText = new StringBuilder();
                    for (JsonElement symbol : word.getAsJsonObject().get("symbols").getAsJsonArray()) {
                        wordText.append(symbol.getAsJsonObject().get("text").getAsString());
                        System.out.format("Symbol text: %s (confidence: %f)%n", symbol.getAsJsonObject().get("text").getAsString(), symbol.getAsJsonObject().get("confidence").getAsFloat());
                    }
                    System.out.format("Word text: %s (confidence: %f)%n%n", wordText.toString(), word.getAsJsonObject().get("confidence").getAsFloat());
                    System.out.format("Word bounding box: %s%n", word.getAsJsonObject().get("boundingBox"));
                    paraText.append(wordText.toString()).append(" ");
                }
                System.out.format("%nParagraph:%n%s%n", paraText);
                System.out.format("Paragraph bounding box: %s%n", para.getAsJsonObject().get("boundingBox"));
                System.out.format("Paragraph Confidence: %f%n", para.getAsJsonObject().get("confidence").getAsFloat());
                blockText.append(paraText);
            }
            pageText.append(blockText);
        }
    }