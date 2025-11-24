# Source: https://docs.augmentcode.com/setup-augment/sign-in.md

# Sign in and out

> After you have installed the Augment extension, you will need to sign in to your account.

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About Authentication

You can sign in to Augment using one of the supported identity providers–Google or Microsoft–or sign in using your email address and a single-use code we send to you. During the process, you will be redirected to your browser to sign in to your account.

## Sign in

<Steps>
  <Step title="Sign in to Augment">
    Click the <Command text="Sign in to Augment" /> button in the Augment panel. If you do not see the Augment panel press <Keyboard shortcut="Cmd/Ctrl L" />. If you are using Visual Studio Code, you be asked to confirm going to Augment's authentication portal.
  </Step>

  <Step title="Sign in with your email">
    In your browser, you may sign in with Google, Microsoft, or by receiving a single-use code in your email.
  </Step>

  <Step title="Accept the terms and conditions">
    If this is the first time you've signed in to Augment, you will be asked to accept the terms and conditions.
  </Step>

  <Step title="Return to your IDE">
    You will be automically redirected back to your IDE and you will see the Augment icon
    change to{" "}
    <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar.
  </Step>

  <Step title="Sync your workspace">
    If this is your first time using Augment, or you are working on a new workspace, you will see the <Command text="Sync modal" /> in the Augment panel. Click the <Command text="Sync" /> button in the Augment panel to enable Augment's rich codebase awareness. See [Syncing your workspace](/setup-augment/workspace-indexing) to customize syncing behavior and learn more.
  </Step>
</Steps>

## Sign out

<Steps>
  <Step title="Show the Augment command menu">
    Press <Keyboard shortcut="Cmd/Ctrl Shift A" /> to show the Augment command menu.
  </Step>

  <Step title="Click Sign Out">Click <Command text="Sign Out" /> from the bottom of the commands menu.</Step>

  <Step title="You are now signed out of Augment">
    You will see the status bar icon change to orange and you will be signed out of Augment in all of your active workspaces.
  </Step>
</Steps>
