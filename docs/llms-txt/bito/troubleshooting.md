# Source: https://docs.bito.ai/help/support-and-questions/troubleshooting.md

# Troubleshooting

## #1 **Bito JetBrain Extension doesn't work in Android Studio.**

{% embed url="<https://www.loom.com/share/4c27a38758da464a93505f86e7a08f29>" %}

Bito plugin needs support for the JCEF browser, which is not included in Android Studio due to its default boot runtime setup. You can change the default Boot runtime settings in Android Studio to a version that supports the JCEF browser and get Bito running on Android Studio\
Given below are the instructions:

1. Go to Help → Find action
2. Type → “Choose Boot Java Runtime for the IDE”
3. From the dropdown “New”, select a Boot runtime that supports the JCEF browser.
4. Select "OK" and Restart.

Once done, install Bito, and you will have it up and running.

### Bito doesn’t load and show a blank page when installed in Android Canary.

In order to load Bito in Android Canary, please follow below steps:-

1. Select `Help | Find Action` from the main menu in IDE.
2. Type `Registry...`, select it.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2Fii83S4wc9YjMoCmB2AoR%2FScreenshot%202024-01-10%20at%201.21.33%E2%80%AFPM-20240110-075138.png?alt=media&#x26;token=f0780d05-4fd1-494b-ba7d-cda5ea140e30" alt=""><figcaption></figcaption></figure>
3. In the opened list, find and disable the `ide.browser.jcef.sandbox.enable` options.

   <figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2FJinioGeEri5zI3UXP38E%2FScreenshot%202024-01-10%20at%201.22.14%E2%80%AFPM-20240110-075312.png?alt=media&#x26;token=24d3640d-21e1-45aa-9986-91d1d0188685" alt=""><figcaption></figcaption></figure>
4. Restart the IDEA.

## #2 Korean/Hangul language is behaving abnormally in the JetBrains IDE

{% embed url="<https://www.loom.com/share/d609bcf28adc401fa77fc54d60340076>" %}

In the latest JetBrains IDE (version >= 2023.2), some languages, particularly Korean/Hangul, are mistakenly typed from right to left instead of the correct left to right format.

To resolve this:

1. Open your JetBrains IDE.
2. Navigate to **Help → Edit Custom VM Options** menu.
3. A file will open. Add the following code in this file:

```
-Dide.browser.jcef.osr.enabled=false
```

4. Save the file.
5. Restart the IDE.

This workaround should address the input issue. It's a persistent setting, so you won't need to repeat this process every time you start the IDE. Additionally, while the problem is noted with Korean/Hangul, if you experience similar issues with other languages, you can try the same workaround.

## #3 Full Line Code completion is disabled notification in JetBrains 2024.1 EAP

JetBrains has released a new version, 2024.1 EAP, which introduces a new feature called **"Full Line Code Completion"**. Since this release, all JetBrains plugins supporting Line/Code completion have encountered an issue where end users receive a notification to disable the plugin if they want to access built-in local inline code completion.

<figure><img src="https://2860197046-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYgNBTrPKG0DuVdAyDvSa%2Fuploads%2F6M2qy9sgENpxRkJE0g9q%2Fimage%20(5).png?alt=media&#x26;token=c31c65d7-8121-43e6-8102-580372b59d56" alt=""><figcaption></figcaption></figure>

If you have also received this notification, do not worry because it is only the new feature of JetBrains **"Full Line Code Completion"** that is disabled. However, the existing normal JB suggestions and completions are not affected by this.

The reason you should continue using Bito [**AI Code Completions**](https://docs.bito.ai/help/support-and-questions/broken-reference) is that it is powered by best-in-class Large Language Models (such as GPT-4o mini and Google PaLM 2 – 540B parameters), which provide very high-quality and accurate suggestions based on your code.

Therefore, you can simply close this notification and continue using the Bito plugin. It will work as expected.

## #4 Setup Bito extension in VS Code running through SSH or WSL

For SSH setup, please refer to [this documentation](https://docs.bito.ai/ai-code-reviews-in-ide/installation-guide/installing-on-visual-studio-code#setup-bito-extension-in-vs-code-running-through-ssh).

For WSL setup, please refer to [this documentation](https://docs.bito.ai/ai-code-reviews-in-ide/installation-guide/installing-on-visual-studio-code#setup-bito-extension-in-vs-code-running-through-wsl).
