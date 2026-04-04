# Source: https://jam.dev/docs/record-a-jam/instant-replay/performance.md

# Performance

Instant Replay works by taking periodic HTML snapshots of the DOM (Document Object Model). These snapshots are then stored in your browser's local storage until you create a Jam, at which point they can be used to generate a video demonstrating the bug in question.

While the Instant Replay feature is incredibly useful, if used on heavier websites, could eat up browser memory storing the HTML snapshots and have a noticeable impact on browser performance. That's why we've spent a lot of time putting safeguards in place so that it has no impact on your browser performance.

Jam automatically disables Instant Replay on particularly heavy websites, such as those with numerous animations or those that re-render large volumes of data at high frequencies (e.g., crypto price websites or spreadsheet applications). This precautionary measure prevents potential performance degradation caused by frequent DOM snapshotting.

## How to override Jam's auto-disabling of Instant Replay on your website

As described above, Jam automatically disables the Instant Replay feature on particularly heavy websites as a precautionary measure to ensure no impact on browser performance.

However, users have the option to override this disabling on any website. For example, if you are using a powerful device with robust processing capabilities, you may not experience any performance issues and may wish to enable Instant Replay for capturing bugs on heavy websites.

To override Jam's cautious disabling of Instant Replay, simply adjust the settings within the Jam extension. If you later decide to revert this decision, you can remove the website from the override list in the extension settings.

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2F5XtZA2WmBjDzvnLeojKp%2Fenable-ir.gif?alt=media\&token=7c71805e-2083-4941-b7ed-dbcb4ea316c9)
