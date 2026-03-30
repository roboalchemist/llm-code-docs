# Source: https://docs.tabnine.com/main/getting-started/tabnine-chat/consume.md

# Reviewing suggestions

## How to review the Tabnine Chat suggestions

Once you get an answer from Tabnine Chat, review it. If you aren't satisfied with the answer, refine your original request with an alternative or a more specific prompt **in the current or new session**.

If you're happy with the response, you can add it to your code in one of the following ways.

### Manual Copy and Paste

Copy the answer (or part of it) and paste it into the relevant location in your code:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-53d8af6982ff3841c092ec3c1e349856c7dd86cd%2Fmanual%20copy%20paste%20(1).gif?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Copy Function

Click **Copy,** then paste the answer into the relevant location in your code:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-649b8ff0bbb9c863d50b3e015f3c877d4179ed92%2Fcopy_raw%20(1).gif?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Insert Action

Click **Insert** to copy and insert the code into the open file with one click.

The code is pasted at the cursor location or inside the selected block:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a4664f72e3517d37291fec501aa6b7bb78473110%2FInsert%20(1).gif?alt=media" alt="" width="563"><figcaption></figcaption></figure>

### Show Diff

If the Chat answer is close enough to the current open file, a **Show diff** option appears. Click **Show diff** to see the specific change offered by Tabnine.

To paste the changes into the file, click **Insert**.

{% hint style="info" %}
Diff insert is available in VS Code, JetBrains and Visual Studio 2022
{% endhint %}

In VS Code, you'll need to **Accept** each change inline:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2f3262817a89754459a4711e314dc5ed95b753ab%2Fshow%20diff_latest%20(1).gif?alt=media" alt="" width="563"><figcaption><p>Show diff, Insert, and Accept in VS Code</p></figcaption></figure>

### Apply

Within Chat, you will have the option to apply suggestions directly to the relevant code snippet in your target file.

After generating a response, the Apply button will appear in the upper right-hand corner of the code snippet. Simply click and the code will be inserted.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d67f1741b1feb78a1fce73173ff81d0d7f2819a8%2FLonger%20scripts%20include%20an%20Apply%20button%20in%20the%20top-right%20corner.gif?alt=media" alt=""><figcaption></figcaption></figure>

You should receive confirmation of changes with a screen that lists the files where code changes were applied, similar to this:

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b5197cf47dc3cf33d5a0d16c5d3bddb96950c428%2Fimage.png?alt=media" alt=""><figcaption><p>Changes applied successfully using the 'Apply' button in Tabnine</p></figcaption></figure>

#### References

If the context for local code awareness is enabled, by default the Tabnine Chat tries to answer the user questions with context from the local workspace. When returning the answer to the user, Tabnine Chat is explicit about the context used to answer the question by including a list of references:

<figure><img src="https://lh7-us.googleusercontent.com/ZVxhJ2hiw7zDcHHHeUmxRgn3xYHQq63tMN8tlH6EZ4WnQ4MuVw5JO8gN04chVw_Ft8uByddl7i-ubYP4PWdPfqDOpGo24y6bpQGOo0TgWhA7Gf3ANRZARVH19bTWbdbSl-z6zPmeVyj77QuDYd_yQVM" alt="" width="563"><figcaption></figcaption></figure>

You can click each reference and get to the full code that was induced in the chat context. \\
