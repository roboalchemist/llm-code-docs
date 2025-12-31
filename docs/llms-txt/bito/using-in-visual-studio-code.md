# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-visual-studio-code.md

# Using in Visual Studio Code

{% embed url="<https://www.youtube.com/watch?v=RXMIkgozmwc>" %}

{% hint style="info" %}
This feature is only available for our **Team Plan**. Visit the [pricing page](https://bito.ai/pricing/) or [billing documentation](https://docs.bito.ai/help/billing-and-plans) to learn more about our paid plans.
{% endhint %}

1. Open your project’s folder using Visual Studio Code.&#x20;
2. Bito uses AI to create an [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) of your project’s codebase. It enables Bito to understand the code and provide relevant answers. There are three ways to start the indexing process:&#x20;

   * When you open a new project, a popup box will appear through which Bito asks you whether you want to enable indexing of this project or not. Click on the “Enable” button to start the indexing process. You can also skip this step by clicking the “Maybe later” button. You can always index the project later if you want.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F3ftxNdlBeDRY6xqmhejw%2Fscrnli_8_29_2023_8-18-34%20AM.png?alt=media&#x26;token=d33f6f5b-1c69-4239-902e-0f6eacb9ec8c" alt="" width="563"><figcaption></figcaption></figure>

* In the bottom-left of Bito plug-in pane, hover your mouse cursor over this icon. You can also enable indexing from here by clicking on the “Click to enable it” text.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FltGHnZG7Y3tn50FP6Ra7%2Fscrnli_8_29_2023_8-47-21%20AM.png?alt=media&#x26;token=3ad4ae10-517f-4670-bdbc-350c0db5cc9e" alt="" width="563"><figcaption></figcaption></figure>
* Another option is to open the "Manage Repos" tab by clicking the laptop icon in the top-right corner of the Bito plugin pane.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fg0XkBWFOQEVv9GHwOKzM%2Fscrnli_8_29_2023_8-22-36%20AM.png?alt=media&#x26;token=7f868a77-67b6-4c2e-84a3-d3f584220e6a" alt="" width="563"><figcaption></figcaption></figure>
* From here you can start the [**indexing process**](https://docs.bito.ai/help/bitos-ai-stack/indexing) by clicking on the “Start Indexing” button. Here, you will also see the total indexable size of the repository. Read more about [**What is Indexable Size?**](https://docs.bito.ai/feature-guides/ai-that-understands-your-code/managing-index-size#what-is-indexable-size)

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F8dC14JxM7PqVLnCOjPtD%2Fscrnli_8_29_2023_8-24-50%20AM.png?alt=media&#x26;token=70f208d7-7ea6-4d7e-b6d7-f9354516a4c8" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Bito usually takes around 12 minutes per each 10MB of code to understand your repo.
{% endhint %}

{% hint style="info" %}
Bito will still work correctly if you don’t enable indexing of your project. However, in that case, Bito will only be able to provide general answers.&#x20;
{% endhint %}

{% hint style="info" %}
If you have previously indexed some projects using Bito then they will show in the “Other projects” section.&#x20;
{% endhint %}

{% hint style="info" %}
Index building is aborted if the user logs out or if the user's subscription is canceled (downgraded from a paid plan to a free plan).
{% endhint %}

3. Let’s start the indexing process by using any of the above-mentioned methods.&#x20;
4. The status will now be updated to “Indexing in progress...” instead of “Not Indexed”. You will also see the real-time indexing progress for the current folder, based on the number of files indexed.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F7gam7HQsLQpZbezxiN1w%2Fscrnli_8_29_2023_8-26-22%20AM.png?alt=media&#x26;token=edbe2d56-7454-4f55-bf55-79b09e169b7c" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
In case you close the VS Code while the indexing is in progress then don’t worry. The indexing will be paused and will automatically continue from where it left off when you reopen VS Code. Currently, the indexing will resume 5-10 minutes after reopening the IDE.
{% endhint %}

{% hint style="info" %}
The progress indicator for the other folders is updated every 5 minutes.
{% endhint %}

5. Once the indexing is complete, the status will be updated from “Indexing in progress...” to “Indexed”, and will look like this.&#x20;

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fg4WeAttB0V8dgR67vtF0%2Fscrnli_8_29_2023_8-27-30%20AM.png?alt=media&#x26;token=82dfe9c4-2a9b-44b3-a25a-b6cc1a35a079" alt="" width="563"><figcaption></figcaption></figure>
6. Now you can ask any question regarding your codebase by adding the keyword **"my code"** to your AI requests in the Bito chatbox. Bito is ready to answer them!

{% hint style="info" %}
Example: **in my code explain the file apiUser.js**

Additional keywords for various languages are listed on the [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page. Also, here are some [**Example Questions**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/example-questions).
{% endhint %}

7. In case you ever want to delete an index then you can do that by clicking on this three dots button and then clicking the “Delete” button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FfeTslygIhN3kuY5f8zSv%2Fscrnli_8_29_2023_8-28-59%20AM.png?alt=media&#x26;token=a5e62723-b423-4a16-bb48-46674e8a442d" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Index deletion is allowed even if the index is in progress or in a paused state.
{% endhint %}

8. A warning popup box will open in the bottom of Bito’s plugin pane. You can either click on the “Delete” button to delete the project’s index from your system or click on the “Cancel” button to go back.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FV94JPEw8OV9wrLOhmyb1%2Fscrnli_8_29_2023_8-30-25%20AM.png?alt=media&#x26;token=5db7c77f-033d-43ad-8e73-30a42783d8e4" alt="" width="563"><figcaption></figcaption></figure>

## A Quick Example from a Real Project&#x20;

For the sake of this tutorial, we’ve created a simple **“Music Player using JavaScript”**.&#x20;

Here’s how it looks:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FPB7eGZdEzgd5jFpT3Vcf%2Fb40.png?alt=media&#x26;token=a2f08375-1b09-4969-a031-15b49751e631" alt=""><figcaption></figcaption></figure>

We have added a bunch of songs to this project. The song details like name, artist, image, and the music file name are stored in a file called **music-list.js**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJIiaFQosvis14KXWdTTL%2Fb44.png?alt=media&#x26;token=8738366a-c749-40d5-bdb0-e4a2457c4fb6" alt="" width="375"><figcaption></figcaption></figure>

### Question # 1&#x20;

Let’s ask Bito to **list names of all song artists used in my code**

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FhXSVLnx1pjP12JpiaSNw%2Fb43.png?alt=media&#x26;token=ef967b55-d328-4821-8c34-a0c8905df65c" alt="" width="558"><figcaption></figcaption></figure>

As you can see, Bito gave the correct answer by utilizing its understanding of our repository.&#x20;

Similarly, we can ask any coding-related question like find bugs, improve code, add new features, etc.&#x20;

### Question # 2&#x20;

Our music player is working fine, but we don’t have any option to mute/unmute the song.&#x20;

Let’s ask Bito to add this feature.&#x20;

**Here’s the question I used:**&#x20;

In my code how can i add a button to mute and unmute the song? By default, set this button to unmute. Also, use the same design as existing buttons in UI.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQArzJvfKL6Vguip5gwPD%2Fb45.png?alt=media&#x26;token=c5aa365c-1adc-4ee9-bdec-f2314b064c99" alt="" width="550"><figcaption></figcaption></figure>

After adding the code suggested by Bito, here’s how the music player looks when it starts (unmuted).

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FC0Ojp9aaKqpKljABdlp5%2Fscrnli_8_18_2023_12-03-42%20PM.png?alt=media&#x26;token=1883350d-3cde-437c-a448-43eccfeb8477" alt=""><figcaption></figcaption></figure>

And when muted:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FKiC6qO4SjSjl0mEL8EkX%2Fscrnli_8_18_2023_12-04-27%20PM.png?alt=media&#x26;token=1d57af8b-d8f4-4bcd-b037-a00afd65706a" alt=""><figcaption></figcaption></figure>
