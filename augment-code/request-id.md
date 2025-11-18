# Source: https://docs.augmentcode.com/troubleshooting/request-id.md

# Request IDs

> Request IDs are generated with every code suggestion and chat interaction. Our team may ask you to provide the request ID when you report a bug or issue.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## Finding a Request ID for Chat

<Steps>
  <Step title="Open the Chat panel">
    Open the Chat panel by clicking the Augment icon{" "}

    <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5a70e197b4ab16c79e9612aac74015cf" className="inline h-4 p-0 m-0" data-og-width="676" width="676" data-og-height="592" height="592" data-path="images/augment-icon-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2a32c9463cef1c6647f0dd08dd827cd2 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba744eb472e888403e462429f3c10a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c8393d6a3463c6e6a99eca871d66ae67 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=573abbe9afb002028f79741b4fa4bad4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=998af121c45992d4121b3fb97ee42007 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa776a96f49e4d86cb0a0d7cef78cc67 2500w" />

    {" "}

    in the action bar on the left side of your editor.
  </Step>

  <Step title="Open the chat thread">
    If the chat reply you are interested is in a previous chat thread, find the
    chat thread by clicking the <Icon icon="chevron-right" /> at the top of the
    chat panel and clicking the relevant chat thread.
  </Step>

  <Step title="Find the request ID">
    Find the reply in question and click the <Icon icon="link-simple" /> icon
    above the reply to copy the request ID to your clipboard.
  </Step>
</Steps>

## Finding a Request ID for Completions

<Steps>
  <Step title="Open the History panel">
    Open the History panel by pressing <Keyboard shortcut="Cmd/Ctrl Shift P" />
    and then searching for `Augment: Show History` in the command menu.
  </Step>

  <Step title="Find the request ID">
    Recent requests are listed in reverse chronological order. Locate the
    request you are interested in and copy the request ID by clicking on the
    request ID, for example:
    <br /> `-- Request ID: 7f67c0dd-4c80-4167-9383-8013b18836cb`
  </Step>
</Steps>
