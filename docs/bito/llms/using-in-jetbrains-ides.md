# Source: https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/using-in-jetbrains-ides.md

# Using in JetBrains IDEs

{% hint style="info" %}
This feature is only available for our **Team Plan**. Visit the [pricing page](https://bito.ai/pricing/) or [billing documentation](https://docs.bito.ai/help/billing-and-plans) to learn more about our paid plans.
{% endhint %}

1. Open your project’s folder using a JetBrains IDE. For this guide, we are using PyCharm.&#x20;
2. Bito uses AI to create an [**index**](https://docs.bito.ai/help/bitos-ai-stack/indexing) of your project’s codebase. It enables Bito to understand the code and provide relevant answers. There are three ways to start the indexing process:&#x20;

   * When you open a new project, a popup box will appear through which Bito asks you whether you want to enable indexing of this project or not. Click on the “Enable” button to start the indexing process. You can also skip this step by clicking the “Maybe later” button. You can always index the project later if you want.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fy4ohwQiz0sw1OSyBBIMV%2Fscrnli_8_29_2023_8-45-58%20AM.png?alt=media&#x26;token=22b663b4-57cc-46e5-ade2-580917864a53" alt="" width="563"><figcaption></figcaption></figure>

* In the bottom-left of Bito plug-in pane, hover your mouse cursor over this icon. You can also enable indexing from here by clicking on the “Click to enable it” text.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FprqcLERo0qda71JHfUE5%2Fscrnli_8_29_2023_8-48-59%20AM.png?alt=media&#x26;token=5f890235-5513-4393-868a-7d40a535345c" alt="" width="563"><figcaption></figcaption></figure>
* Another option is to open the "Manage Repos" tab by clicking the laptop icon in the top-right corner of the Bito plugin pane.

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FSEWw2YdRKyTgLzHqaYEh%2Fscrnli_8_29_2023_11-18-57%20AM.png?alt=media&#x26;token=1239730f-dca8-4c7c-bad6-23b536d64b1a" alt="" width="563"><figcaption></figcaption></figure>
* From here you can start the [**indexing process**](https://docs.bito.ai/help/bitos-ai-stack/indexing) by clicking on the “Start Indexing” button given in front of your current project. Here, you will also see the total indexable size of the repository. Read more about [**What is Indexable Size?**](https://docs.bito.ai/feature-guides/ai-that-understands-your-code/managing-index-size#what-is-indexable-size)

  <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FOKUGPMR97iPKglm0lA4e%2Fscrnli_8_29_2023_11-24-10%20AM.png?alt=media&#x26;token=744020d6-fbfc-4f34-b605-eb0d251cb923" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Bito usually takes around 12 minutes per each 10MB of code to understand your repo.
{% endhint %}

{% hint style="info" %}
Bito will still work correctly if you don’t enable indexing of your project. However, in that case, Bito will only be able to provide general answers.
{% endhint %}

{% hint style="info" %}
If you have previously indexed some projects using Bito then they will show in the “Other projects” section.
{% endhint %}

{% hint style="info" %}
Index building is aborted if the user logs out or if the user's subscription is canceled (downgraded from a paid plan to a free plan).
{% endhint %}

3. Let’s start the indexing process by using any of the above-mentioned methods.&#x20;
4. The status will now be updated to “Indexing in progress...” instead of “Not Indexed”. You will also see the real-time indexing progress for the current folder, based on the number of files indexed.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fsgi0Dr5uyQjWu1aGi5kh%2Fscrnli_8_29_2023_8-53-07%20AM.png?alt=media&#x26;token=9753b843-b5be-4547-adaf-6ec7799ccb54" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
In case you close the JetBrains IDE (e.g., PyCharm) while the indexing is in progress then don’t worry. The indexing will be paused and will automatically continue from where it left off when you reopen the IDE. Currently, the indexing will resume 5-10 minutes after reopening the IDE.
{% endhint %}

{% hint style="info" %}
The progress indicator for the other folders is updated every 5 minutes.
{% endhint %}

5. Once the indexing is complete, the status will be updated from “Indexing in progress...” to “Indexed”, and will look like this.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FMk4ALxEg2KLaCnaY01dY%2Fscrnli_8_29_2023_8-57-52%20AM.png?alt=media&#x26;token=37e7c22d-d03e-4225-a355-6f02c60308d2" alt="" width="563"><figcaption></figcaption></figure>
6. Now you can ask any question regarding your codebase by adding the keyword **"my code"** to your AI requests in the Bito chatbox. Bito is ready to answer them!

{% hint style="info" %}
Example: **in my code explain the file apiUser.js**

Additional keywords for various languages are listed on the [**Available Keywords**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/available-keywords) page. Also, here are some [**Example Questions**](https://docs.bito.ai/ai-code-reviews-in-ide/ai-that-understands-your-code/example-questions).
{% endhint %}

7. In case you ever want to delete an index then you can do that by clicking on this three dots button and then clicking the “Delete” button.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FY5fdRWYIXVti75AYv1mB%2Fscrnli_8_29_2023_8-59-06%20AM.png?alt=media&#x26;token=d39c4ff1-fd47-4563-a464-e7e45f48b5a1" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="info" %}
Index deletion is allowed even if the index is in progress or in a paused state.
{% endhint %}

8. A warning popup box will open in the bottom of Bito’s plugin pane. You can either click on the “Delete” button to delete the project’s index from your system or click on the “Cancel” button to go back.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FQmcRxNbxYroopCn1epWo%2Fscrnli_8_29_2023_8-59-51%20AM.png?alt=media&#x26;token=5a2e7dbe-11c7-4d48-88b7-50310052238e" alt="" width="563"><figcaption></figcaption></figure>

## A Quick Example from a Real Project&#x20;

For the sake of this tutorial, we’ve created a clone of popular game **“Wordle”** using Python.&#x20;

Here’s how it looks:

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJmOfDBFx3uAxIYb7z0S0%2Fb53.png?alt=media&#x26;token=c1e6ce20-bfeb-44df-ac87-670c2eae0d2f" alt=""><figcaption></figcaption></figure>

We have stored the list of words in files that are inside the “word\_files” folder. A word is selected from these files randomly at the start of the game that the player has to guess.&#x20;

### Question # 1&#x20;

Let’s ask Bito to **understand my code and briefly write about what this game is all about and how to play it**&#x20;

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FBbvesJzw19rEQUeK0hDs%2Fb54.png?alt=media&#x26;token=44f3c3f5-33bf-45b4-b23f-97c41a7b3e55" alt="" width="536"><figcaption></figcaption></figure>

Bito correctly described the game by just looking at its source code.

### Question # 2&#x20;

Our game (PyWordle) is working fine, but there is no count down timer to make it a bit more challenging.&#x20;

So, let’s ask Bito to add this feature.&#x20;

**Here’s the question I used:**&#x20;

> suggest code for main.py "class PyWordle" to add a count down timer for this game in my code. I'm using "self" in functions and variable names, so suggest the code accordingly. The player will lose the game if the time runs out. Set the time limit to 2 minutes (format like 02:00). The timer will start when the game starts. Also reset the timer when the game restarts, such as when player closes the "you won / you lost" popup. Display this real-time count down timer on the right-side of where the player score is displayed. Use the similar design as the player score UI. Also tell me exactly where to add your code. Make sure all of this functionality is working.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FPCW1jspVRlq7GJ7gyF4H%2Fb55.png?alt=media&#x26;token=b2f539b3-126e-47c8-b450-63d755902047" alt="" width="537"><figcaption></figcaption></figure>

Bito suggested the code which looks good. But, it was a bit incomplete and needs some improvements. So, I further asked a series of questions to Bito (one-by-one) to fix the remaining issues.&#x20;

After adding the code suggested by Bito, here's how the PyWordle game looks now. As you can see the countdown timer is accurately added where we want it to be added.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FqawYeeYn6KAlKA9OGMYm%2Fb56.jpg?alt=media&#x26;token=5096f8d2-4b15-4615-bdaf-645b16bc0ae3" alt=""><figcaption></figcaption></figure>
