# Source: https://docs.intelligems.io/analytics/custom-events/scoping-to-specific-pages.md

# Scoping to specific pages

By default, custom events fire on every page of your site. If you want to track events only on specific pages, you can specify them in the event setup:

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-fb0d71dc5dc209b36bcf7fea31ab52af128f6cc8%2FScreenshot%202025-03-24%20at%2011.43.10%E2%80%AFAM.png?alt=media" alt=""><figcaption></figcaption></figure>

This URL matching operates on the page path name, which is the part of the URL after the initial slash and before any query parameters or anchor. For example, in the URL:

<https://www.mysite.com/**pages/my-page**?utm\\_source=google#anchor>

The page path that Intelligems matches against is **pages/my-page**.\\

Because the initial slash is ignored, you should generally not have an initial slash in the pattern. URL matching for page visit events work the same way.
