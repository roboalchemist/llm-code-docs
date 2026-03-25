# Source: https://docs.qodo.ai/qodo-documentation/code-review/get-started/use-qodo-in-prs/code-review/ask-questions-with-ask.md

# Ask Questions with /ask

{% hint style="success" %}
Platforms supported: GitHub, GitLab, Bitbucket, Azure DevOps
{% endhint %}

This feature allows you to ask questions about a pull request based on its code changes. Questions are answered using the current pull request context, so they should be specific and clearly phrased.

You can invoke this feature manually by commenting on the pull request using the `/ask` command as follows:

```
/ask ...
```

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FFD0PcDPIiTU3Y7L7TRxi%2Fimage.png?alt=media&#x26;token=1ed2a7df-8a21-4c26-bbcc-9042afb58bb5" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FNMN6CxDrWVrrd2yJv8Ao%2Fimage.png?alt=media&#x26;token=9aa8340d-60c2-42a2-b2a9-62cc3b65b9d8" alt=""><figcaption></figcaption></figure>

### Asking questions on specific lines

{% hint style="success" %}
Platforms supported: GitHub, GitLab
{% endhint %}

You can run the `/ask` command on specific lines of code directly from the pull request diff view. Qodo will answer questions based on the code changes in the selected lines.

1. Click the **+** icon next to the line number to select a line.\
   To select multiple lines, click the **+** icon on the first line, then click and drag to select additional lines.
2. In the comment box, type `/ask` followed by your question.
3. Click **Add single comment**.

Each question is handled independently. The feature does not retain context from previous questions.

<figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FDSjLdC50SMUWmepNXFIQ%2Fimage.png?alt=media&#x26;token=e2a6616b-81c2-433e-806e-05a912972cea" alt=""><figcaption></figcaption></figure>

### Asking questions about images

You can ask questions about images included in pull request comments. In this case, the entire pull request code is used as context.

```
/ask "..."[Image](https://real_link_to_image)
```

Where `https://real_link_to_image` is a direct link to the image.

GitHub allows pasting images directly into comments, but pasted images do not provide a direct image URL. To obtain a direct link:

1. Post a comment containing only the image.<br>

   <figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FxMDlEbdmnkzLOHHqewe7%2Fimage.png?alt=media&#x26;token=4bdfab6b-70dd-487b-b068-4126a069f6ba" alt=""><figcaption></figcaption></figure>
2. Click the **...** menu on the top-right of the comment and select **Quote reply**.<br>

   <figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FK94We8Zu3d4tbWtx2ZxT%2Fimage.png?alt=media&#x26;token=ed19ea52-a114-4eea-96ae-dd035ab4bdea" alt=""><figcaption></figcaption></figure>
3. In the reply box, add your question below the image using the `/ask` command.<br>

   <figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FihXadk4AkStIZ1hmwfoo%2Fimage.png?alt=media&#x26;token=df10e8b1-f2d1-4135-9a3a-5dd811fbfbb6" alt=""><figcaption></figcaption></figure>

   <figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FVDIVzeTjpHsH7y4z7Nb9%2Fimage.png?alt=media&#x26;token=636d84e5-eedd-425d-ad9a-a78628269d9d" alt=""><figcaption></figcaption></figure>
4. Post the comment to receive the answer.<br>

   <figure><img src="https://3540531895-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyXEFCLH7CkXrROa2gOqv%2Fuploads%2FSdDHIKrM2z7k5zE7D0J4%2Fimage.png?alt=media&#x26;token=d3a4528e-649b-453b-b17a-6b77e3d737ee" alt=""><figcaption></figcaption></figure>
