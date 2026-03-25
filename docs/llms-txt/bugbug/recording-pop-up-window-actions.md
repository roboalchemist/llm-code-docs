# Source: https://docs.bugbug.io/recording-tests-steps/recording-pop-up-window-actions.md

# Recording pop-up window actions

## Problem statement

Currently, you can record actions on pop-up windows both during the recording process and while running tests.

This is especially helpful in scenarios where, for example, the user logs in to his or her account using authorization from an external third-party service - e.g. *Google authentication* or similar.

### How does it work?

To put it simply, BugBug forces the opening of a pop-up window in a new browser tab and changes the context for it, e.g. in the scenario of logging in with an external account *(e.g. Google auth.)*,  and after correct authorization, the browser tab is automatically closed as if it had happened with a pop-up window.<br>

{% hint style="info" %}
As an example, we used the Podio page.
{% endhint %}

#### **Regular view:**

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0VpGf83sBn9iOgW3uRBK%2FRegular_popup_window.png?alt=media&#x26;token=e09688b6-ef71-4b1c-97b0-17a0977443ee" alt=""><figcaption><p>Regular pop-up window</p></figcaption></figure>

####

#### While recording the same step/flow in BugBug:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FN3i0ZYCd8vG2dfnDtqlJ%2FRecording_popup_1.png?alt=media&#x26;token=74e0f1e7-29ca-478c-a54b-c16d5f616b57" alt=""><figcaption><p>The tab pop-up doesn't appear yet</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fd0x20l86EZgcfpbL81lP%2FRecording_popup_2.png?alt=media&#x26;token=f17a642c-3633-4e0f-b2b3-d212db9c9623" alt=""><figcaption><p>The pop-up opens in a new browser tab</p></figcaption></figure>

## Recording a test with pop-up window handling

1. Create a new test (or edit an existing one)
2. Start recording new steps&#x20;
3. Record a click action on a button/element that opens a new popup window. Instead of a new pop-up, the page will open in a new browser tab, and the context will automatically switch to that tab as the active tab
4. Perform all actions on this tab, i.e. provide login details and complete the whole flow. Based on the login flow using an external 3rd party account (e.g. Google account), the tab will be automatically closed when it is completed - just as it would be in a pop-up window, and all actions will be recorded.&#x20;
5. When you automatically switch to the currently active tab, you can continue to record actions on that tab
