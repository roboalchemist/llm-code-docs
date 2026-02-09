# Source: https://docs.augmentcode.com/troubleshooting/feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Feedback

> We love feedback, and want to hear from you. We want to make the best AI-powered code assistant so you can get more done.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

Feedback helps us improve, and we encourage you to share your feedback on every aspect of using Augment—from suggestion and chat response quality, to user experience nusances, and even how we can improve getting your feedback.

### Reporting a bug

To report a bug, please [contact support](https://support.augmentcode.com/). Include as much detail to reproduce the problem as possible; screenshots and videos are very helpful.

### Feedback on completions

We are always balancing the needs for speed and accuracy. We want to know when you get a poor suggestion, hallucination, or a completion that actually doesn't work. The History panel has a log of all of your completions; we encourage you to use it to send us feedback on the completions you've received.

<Note>
  Providing feedback directly in your IDE through the History panel is currently
  only available in Visual Studio Code.
</Note>

<Steps>
  <Step title="Open the History panel">
    Open the History panel by pressing <Keyboard shortcut="Cmd/Ctrl Shift P" />
    and then searching for `Augment: Show History` in the command menu.
  </Step>

  <Step title="Find the completion you want to report">
    Recent completions are listed in reverse chronological order. Locate the
    completion you want to report and add complete the feedback form.
  </Step>

  <Step title="Submit your feedback">
    After completing the form, click either the red button for bad completions
    or the green button for good completions.
  </Step>
</Steps>

### Feedback on chat

After each Chat interaction, you have the opportunity to provide feedback on the quality of the response. At the bottom of the response click either the thumbs up <Icon icon="thumbs-up" iconType="light" /> or thumbs down <Icon icon="thumbs-down" iconType="light" /> icon. Add additional information in the feedback field, and click `Send Feedback`.
