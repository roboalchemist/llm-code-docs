# Stream.io Documentation
# Source: https://getstream.io/chat/docs/file_uploads/

* [Chat Messaging](/chat/)

/

  * [Docs](/chat/docs/)

/

  * [React](/chat/docs/react/)

/

  * [Image and File Uploads](/chat/docs/react/file_uploads/)

# Image and File Uploads

Stream Chat allows you to upload images, videos, and other files to the Stream
CDN or your own CDN. Uploaded files can be used as message attachments, user
avatars, or channel images.

Streamâs UI SDKs (React, React Native, Flutter, SwiftUI, Jetpack Compose,
etc.) handle file uploads automatically through their message composer
components. The upload process, progress tracking, and attachment handling are
built into these components. Use the methods described on this page only if
you need custom upload behavior or are building a custom UI.

## Uploading Files to a Channel

Files uploaded to a channel can be attached to messages. You can either upload
a file first and then attach it to a message, or let the SDK handle the upload
when sending a message with attachments.

JavaScriptKotlinSwiftDartJavaNode.jsPythonPHPRubyC#Unity

    
    
    // Upload an image to the channel
    const response = await channel.sendImage(file);
    const imageUrl = response.file;
    
    // Send a message with the uploaded image
    await channel.sendMessage({
      text: "Check out this image",
      attachments: [
        {
          type: "image",
          asset_url: imageUrl,
          thumb_url: imageUrl,
        },
      ],
    });
    
    
    val channelClient = client.channel("messaging", "general")
    
    // Upload an image
    channelClient.sendImage(imageFile).enqueue { result ->
      if (result is Result.Success) {
        val imageUrl = result.value.file
        val attachment = Attachment(
          type = "image",
          imageUrl = imageUrl,
        )
        val message = Message(attachments = mutableListOf(attachment))
        channelClient.sendMessage(message).enqueue { /* ... */ }
      }
    }
    
    // Upload a file with progress tracking
    channelClient.sendFile(
      file,
      object : ProgressCallback {
        override fun onSuccess(url: String?) {
          // File uploaded successfully
        }
        override fun onError(error: Error) {
          // Handle error
        }
        override fun onProgress(bytesUploaded: Long, totalBytes: Long) {
          // Update progress UI
        }
      }
    ).enqueue()
    
    
    let channelId = ChannelId(type: .messaging, id: "general")
    let channelController = chatClient.channelController(for: channelId)
    
    // Option 1: Send message with local attachment (SDK handles upload)
    let imageAttachment = try AnyAttachmentPayload(
      localFileURL: localImageUrl,
      attachmentType: .image
    )
    channelController.createNewMessage(
      text: "Hello",
      attachments: [imageAttachment]
    )
    
    // Option 2: Upload first, then attach to message
    channelController.uploadAttachment(
      localFileURL: localFileUrl,
      type: .image,
      progress: { value in
        // Track upload progress (0.0 to 1.0)
      },
      completion: { result in
        switch result {
        case .success(let uploadedFile):
          let payload = ImageAttachmentPayload(
            title: nil,
            imageRemoteURL: uploadedFile.url
          )
          let attachment = AnyAttachmentPayload(payload: payload)
          channelController.createNewMessage(
            text: "Hello",
            attachments: [attachment]
          )
        case .failure(let error):
          // Handle upload error
        }
      }
    )
    
    
    // Option 1: Send message with local attachments (SDK handles upload)
    final message = Message(text: "Hello", attachments: [
      Attachment(
        type: "image",
        file: AttachmentFile(path: "imagePath/imageName.png"),
      ),
    ]);
    await channel.sendMessage(message);
    
    // Option 2: Upload first, then attach to message
    await client.sendImage(
      image,
      channelId,
      channelType,
      onSendProgress: (sent, total) {
        // Update progress UI
      },
    ).then((response) {
      final imageUrl = response.file;
      final message = Message(attachments: [
        Attachment(type: "image", imageUrl: imageUrl),
      ]);
      client.sendMessage(message, channelId, channelType);
    });
    
    
    ChannelClient channelClient = client.channel("messaging", "general");
    
    // Upload an image
    channelClient.sendImage(imageFile).enqueue(result -> {
      if (result.isSuccess()) {
        String imageUrl = result.data().getFile();
        Attachment attachment = new Attachment();
        attachment.setType("image");
        attachment.setImageUrl(imageUrl);
    
        Message message = new Message();
        message.getAttachments().add(attachment);
        channelClient.sendMessage(message).enqueue(res -> { /* ... */ });
      }
    });
    
    // Upload a file with progress tracking
    channelClient.sendFile(file, new ProgressCallback() {
      @Override
      public void onSuccess(@NotNull String url) {
        // File uploaded successfully
      }
      @Override
      public void onError(@NotNull ChatError error) {
        // Handle error
      }
      @Override
      public void onProgress(long bytesUploaded, long totalBytes) {
        // Update progress UI
      }
    }).enqueue();
    
    
    // Upload multiple images in parallel
    const promises = [
      channel.sendImage(
        fs.createReadStream("./image1.jpg"),
        "image1.jpg",
        "image/jpeg",
        { id: "user-id" },
      ),
      channel.sendImage(
        fs.createReadStream("./image2.jpg"),
        "image2.jpg",
        "image/jpeg",
        { id: "user-id" },
      ),
    ];
    
    const results = await Promise.all(promises);
    
    const attachments = results.map((response) => ({
      type: "image",
      thumb_url: response.file,
      asset_url: response.file,
    }));
    
    await channel.sendMessage({
      text: "Check out these images",
      attachments,
    });
    
    
    channel.send_image(
      "http://example.com/image.jpg",
      "image.jpg",
      {"id": "user-id"},
      "image/jpeg",
    )
    
    
    $user = ["id" => "user-id"];
    $response = $channel->sendImage("http://example.com/image.jpg", "image.jpg", $user);
    
    
    channel.send_image(
      "http://example.com/image.jpg",
      "image.jpg",
      { id: "user-id" },
      "image/jpeg"
    )
    
    
    var imageBytes = File.ReadAllBytes("image.jpg");
    await messageClient.UploadImageAsync(channel.Type, channel.Id, user, imageBytes, "image.jpg");
    
    
    var imageBytes = File.ReadAllBytes("path/to/image.jpg");
    var imageUploadResponse = await channel.UploadImageAsync(imageBytes, "image.jpg");
    var imageUrl = imageUploadResponse.FileUrl;
    
    var fileBytes = File.ReadAllBytes("path/to/document.pdf");
    var fileUploadResponse = await channel.UploadFileAsync(fileBytes, "document.pdf");
    var fileUrl = fileUploadResponse.FileUrl;

## Uploading Standalone Files

Files not tied to a specific channel can be used for user avatars, channel
images, or other application needs.

KotlinSwiftDart

    
    
    val client = ChatClient.instance()
    
    // Upload an image
    val uploadResult = client.uploadImage(
      file = imageFile,
      progressCallback = progressCallback,
    ).await()
    
    when (uploadResult) {
      is Result.Success -> {
        val imageUrl = uploadResult.value.file
        // Use the URL (e.g., update user avatar)
        client.updateUser(user.copy(image = imageUrl)).await()
      }
      is Result.Failure -> {
        // Handle error
      }
    }
    
    
    let chatClient = ChatClient.shared
    
    chatClient.uploadAttachment(
      localUrl: imageLocalFileUrl,
      progress: { progressValue in
        // Track upload progress (0.0 to 1.0)
      },
      completion: { result in
        switch result {
        case .success(let uploadedFile):
          // Use the URL (e.g., update user avatar)
          chatClient.currentUserController().updateUserData(
            imageURL: uploadedFile.url
          )
        case .failure(let error):
          // Handle upload error
        }
      }
    )
    
    
    final client = StreamChatClient("api-key");
    
    // Upload an image
    final image = AttachmentFile(path: "imagePath/image.png");
    final response = await client.uploadImage(
      image,
      onUploadProgress: (count, total) {
        // Update progress UI
      },
    );
    
    final imageUrl = response.file;
    // Use the URL (e.g., update user avatar)
    final user = User(id: "user-id", image: imageUrl);
    await client.updateUser(user);

## Deleting Files

Delete uploaded files to free storage space. Deleting a file from the CDN does
not remove it from message attachments that reference it.

JavaScriptKotlinSwiftDartJavaNode.jsPythonPHPRubyGoC#Unity

    
    
    // Delete from channel
    await channel.deleteFile(fileURL);
    await channel.deleteImage(imageURL);
    
    
    // Delete from channel
    channelClient.deleteFile("file-url").enqueue()
    channelClient.deleteImage("image-url").enqueue()
    
    // Delete standalone file
    client.deleteFile("file-url").enqueue()
    client.deleteImage("image-url").enqueue()
    
    
    // Delete from channel
    channelController.deleteFile(url: "remote-url")
    channelController.deleteImage(url: "remote-url")
    
    // Delete standalone file
    ChatClient.shared.deleteAttachment(remoteUrl: "remote-url") { error in
      // Handle deletion error
    }
    
    
    // Delete from channel
    await channel.deleteFile("file-url");
    await channel.deleteImage("image-url");
    
    // Delete standalone file
    await client.removeFile("file-url");
    await client.removeImage("image-url");
    
    
    // Android SDK
    ChannelClient channelClient = client.channel("messaging", "general");
    channelClient.deleteImage("image-url").enqueue();
    channelClient.deleteFile("file-url").enqueue();
    
    // Backend SDK
    Message.deleteImage(channelType, channelId, url).request();
    Message.deleteFile(channelType, channelId, url).request();
    
    
    await channel.deleteFile(fileURL);
    await channel.deleteImage(imageURL);
    
    
    channel.delete_file(url)
    channel.delete_image(url)
    
    
    $channel->deleteFile($url);
    $channel->deleteImage($url);
    
    
    channel.delete_file(url)
    channel.delete_image(url)
    
    
    channel.DeleteFile(ctx, url)
    channel.DeleteImage(ctx, url)
    
    
    await messageClient.DeleteFileAsync("<channel-type>", "<channel-id>", url);
    await messageClient.DeleteImageAsync("<channel-type>", "<channel-id>", url);
    
    
    await channel.DeleteFileOrImageAsync("file-url");

## File Requirements

### Images

Requirement| Value  
Supported formats| BMP, GIF, JPEG, PNG, WebP, HEIC, HEIC-sequence, HEIF, HEIF-
sequence, SVG+XML  
Maximum file size| 100 MB  
  
### Other Files

Requirement| Value  
Supported formats| All file types are allowed by default. Different clients
may handle certain types differently.  
Maximum file size| 100 MB  
  
You can configure a more restrictive list of allowed file types for your
application.

## Configuring Allowed File Types

Stream allows all file extensions by default. To restrict allowed file types:

  * **Dashboard** : Go to Chat Overview > Upload Configuration
  * **API** : Use the [App Settings](/chat/docs/react/app_setting_overview/#file-uploads/) endpoint

## Access Control and Link Expiration

Stream CDN URLs include a signature that validates access to the file. Only
channel members can access files uploaded to that channel.

Behavior| Description  
Access control| URLs are signed and only accessible by channel members  
Link expiration| URLs expire after 14 days  
Automatic refresh| Links are refreshed automatically when messages are
retrieved (e.g., when querying a channel)  
Manual refresh| Call `getMessage` to retrieve fresh URLs for expired
attachments  
  
To check when a link expires, examine the `Expires` query parameter in the URL
(Unix timestamp).

## Image Resizing

Append query parameters to Stream CDN image URLs to resize images on the fly.

Parameter| Type| Values| Description  
w| number| | Width in pixels  
h| number| | Height in pixels  
resize| string| clip, crop, scale, fill| Resizing mode  
crop| string| center, top, bottom, left, right| Crop anchor position  
  
Images can only be resized if the source image has 16,800,000 pixels or fewer.
An image of 4000x4000 pixels (16,000,000) would be accepted, but 4100x4100
(16,810,000) would fail.

Resized images count against your storage quota.

## Using Your Own CDN

All SDKs support custom CDN implementations. Implement a custom file uploader
to use your own storage solution.

JavaScriptKotlinSwiftDartJavaUnity

    
    
    messageComposer.attachmentManager.setCustomUploadFn(async (file) => {
      const result = await customCDN.upload(file);
      return { file: result.url };
    });
    
    
    val client = ChatClient.Builder("api-key", context)
      .fileUploader(MyCustomFileUploader())
      .build()
    
    
    class CustomCDN: CDNClient {
      static var maxAttachmentSize: Int64 { 20 * 1024 * 1024 }
    
      func uploadAttachment(
        _ attachment: AnyChatMessageAttachment,
        progress: ((Double) -> Void)?,
        completion: @escaping (Result<URL, Error>) -> Void
      ) {
        // Upload to your CDN
        // Call progress() to report upload progress
        // Call completion() with the result
      }
    }
    
    // Assign to ChatClientConfig
    config.customCDNClient = CustomCDN()
    
    
    final client = StreamChatClient(
      "api-key",
      attachmentFileUploader: MyCustomFileUploader(),
    );
    
    
    // Android SDK
    ChatClient client = new ChatClient.Builder("api-key", context)
        .fileUploader(new MyCustomFileUploader())
        .build();
    
    // Backend SDK
    Message.uploadFile(channelType, channelId, userId, "text/plain")
      .file(new File("path/to/file"))
      .withFileHandler(customFileHandler)
      .request();
    
    
    // Upload to your CDN and use the returned URL
    var fileUrl = await MyCustomCDN.Upload(fileBytes);
    
    await channel.SendNewMessageAsync(new StreamSendMessageRequest
    {
      Text = "Message with file attachment",
      Attachments = new List<StreamAttachmentRequest>
      {
        new StreamAttachmentRequest
        {
          AssetUrl = fileUrl,
        }
      }
    });

Did you find this page helpful?

It was helpful

It was not helpful

I have feedback

Submit

Thank you for the feedback.

An error has occurred. Please refresh the page and try again.

[PreviousMessages Overview](/chat/docs/react/send_message/)[NextThreads &
Replies](/chat/docs/react/threads/)

Â© Stream.io, Inc. All Rights Reserved.

[Chat Messaging](https://getstream.io/chat/)[Video &
Audio](https://getstream.io/video/)[Activity
Feeds](https://getstream.io/activity-
feeds/)[Moderation](https://getstream.io/moderation/)

  * Copy LLM prompt
  * [ View as markdown](https://getstream.io/chat/docs/react/file_uploads.md)
  *   * [ Open in ChatGPT](https://chatgpt.com/?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/file_uploads.md)
  * [ Open in Claude](https://claude.ai/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/file_uploads.md)
  * [ Open in Gemini](https://gemini.google.com/app?query=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/file_uploads.md)
  * [ Open in Grok](https://x.com/i/grok?text=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/file_uploads.md)
  * [ Open in Perplexity](https://www.perplexity.ai/search/new?q=I'm working with the Stream Chat React SDK and would like to ask questions about this documentation page: https://getstream.io/chat/docs/react/file_uploads.md)

On this page:

  * Uploading Files to a Channel
  * Uploading Standalone Files
  * Deleting Files
  * File Requirements

    * Images
    * Other Files

  * Configuring Allowed File Types
  * Access Control and Link Expiration
  * Image Resizing
  * Using Your Own CDN

Is this helpful?

Thank you .

An error has occurred.