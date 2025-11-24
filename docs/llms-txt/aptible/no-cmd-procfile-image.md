# Source: https://www.aptible.com/docs/how-to-guides/troubleshooting/common-errors-issues/no-cmd-procfile-image.md

# No CMD or Procfile in Image

### Cause

Aptible relies on your [Image's](/core-concepts/apps/deploying-apps/image/overview) `CMD` or the presence of a [Procfile](/how-to-guides/app-guides/define-services) in order to define [Services](/core-concepts/apps/deploying-apps/services) for your [App](/core-concepts/apps/overview).

If your App has neither, the deploy cannot succeed.

### Resolution

Add a `CMD` directive to your image, or add a Procfile in your repository.
