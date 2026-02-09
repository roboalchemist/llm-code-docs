# Source: https://loops.so/docs/creating-emails/translating-emails-with-ai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://loops.so/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Translating emails

> Loops provides an automated way to translate your emails

Translation inside of Loops is a simple, single-click method of translating emails from one language to another entirely inside of the platform.

<Note>
  Enable this feature in [Settings → Sending](https://app.loops.so/settings?page=sending).
</Note>

1. Create a branch, ensuring it contains at least one email to be translated.
2. Click the **language icon** above the branch and choose the **output** language you would like to translate the branch into.
3. The branch will be duplciated in its entirety, including all emails, filters, and timers then the emails within that branch will begin translation.
4. While translating, the emails will display a `Pending` label.
5. When the translation is complete, the emails will display a `Complete` label on the node.

<img src="https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=888c59d038da019cc78f6c56eab18eb4" alt="Llm Branch Translation" data-og-width="2280" width="2280" data-og-height="1290" height="1290" data-path="images/llm-branch-translation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?w=280&fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=195b329560ccae7fbf5996074677e42b 280w, https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?w=560&fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=201cb7f3739e92165a035b7f75f6264c 560w, https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?w=840&fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=f14f20ee358b6668969b4fccafa9fa36 840w, https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?w=1100&fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=ad1f1101ee020fdd0892a72787a28d6e 1100w, https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?w=1650&fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=b5006525386e2d4571c83c9430b8f5d7 1650w, https://mintcdn.com/loops/u5qNzejTsjudHF7z/images/llm-branch-translation.png?w=2500&fit=max&auto=format&n=u5qNzejTsjudHF7z&q=85&s=13783e07ed0d8bcd3ca30b46bfb68bd1 2500w" />

### Supported elements

We translate all text nodes in an email, but we do carve out exceptions for certain types of content and use cases.

**We translate:**

* Subject
* Preview
* Headers
* Plain text
* Button text
* From name
* Link text
* Alt text on images
* Quotes
* Dynamic content fallbacks

**We do not translate**

* Link URLs
* Plain text urls
* Email addresses
* Text inside of images
* Dynamic content
  * Data variables
  * Contact properties
  * Event properties
* Brand keywords
