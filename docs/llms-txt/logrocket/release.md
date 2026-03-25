# Source: https://docs.logrocket.com/reference/release.md

# Add a Release

Specify a release version for your project

#### `release` - String

##### optional (default - `null`)

The release value can be a Git hash, version string, or any unique identifier for your application.

This release hash will appear in every LogRocket recording, making it easier to determine the code that was running at the time of recording.

```javascript
LogRocket.init(YOUR_APP_ID, {
   release: '0.1.0',
});
```