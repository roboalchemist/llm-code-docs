# Source: https://trigger.dev/docs/apikeys.md

# API keys

> How to authenticate with Trigger.dev so you can trigger tasks.

### Authentication and your secret keys

When you [trigger a task](/triggering) from your backend code, you need to set the `TRIGGER_SECRET_KEY` environment variable.

Each environment has its own secret key. You can find the value on the API keys page in the Trigger.dev dashboard:

<img src="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=89dd26bf57f345bad4508ee5eec70c8c" alt="How to find your secret key" data-og-width="1600" width="1600" data-og-height="900" height="900" data-path="images/api-keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?w=280&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=988f98dd098b108ca51d8c0aeb829344 280w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?w=560&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=14431ee3376a9a6b845744b0b3acce60 560w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?w=840&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=9059b9369eb793b9df4cceee1f985286 840w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?w=1100&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ccd1e2a8512f491128a53cd4ebe8823f 1100w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?w=1650&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=ab656ff2f4b95e32558aacaa485c86ea 1650w, https://mintcdn.com/trigger/uys6iMwf9B_ojh8r/images/api-keys.png?w=2500&fit=max&auto=format&n=uys6iMwf9B_ojh8r&q=85&s=3bb0b87a8e1a3033a8ff1ba3590f5786 2500w" />

<Note>
  For preview branches, you need to also set the `TRIGGER_PREVIEW_BRANCH` environment variable as
  well. You can find the value on the API keys page when you're on the preview branch.
</Note>

### Automatically Configuring the SDK

To automatically configure the SDK with your secret key, you can set the `TRIGGER_SECRET_KEY` environment variable. The SDK will automatically use this value when calling API methods (like `trigger`).

```bash .env theme={null}
TRIGGER_SECRET_KEY="tr_dev_…"
TRIGGER_PREVIEW_BRANCH="my-branch" # Only needed for preview branches
```

You can do the same if you are self-hosting and need to change the default URL by using `TRIGGER_API_URL`.

```bash .env theme={null}
TRIGGER_API_URL="https://trigger.example.com"
TRIGGER_PREVIEW_BRANCH="my-branch" # Only needed for preview branches
```

The default URL is `https://api.trigger.dev`.

### Manually Configuring the SDK

If you prefer to manually configure the SDK, you can call the `configure` method:

```ts  theme={null}
import { configure } from "@trigger.dev/sdk";
import { myTask } from "./trigger/myTasks";

configure({
  secretKey: "tr_dev_1234", // WARNING: Never actually hardcode your secret key like this
  previewBranch: "my-branch", // Only needed for preview branches
  baseURL: "https://mytrigger.example.com", // Optional
});

async function triggerTask() {
  await myTask.trigger({ userId: "1234" }); // This will use the secret key and base URL you configured
}
```
