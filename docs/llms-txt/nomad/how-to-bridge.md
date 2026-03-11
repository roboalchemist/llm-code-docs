# Source: https://docs.nomad.xyz/token-bridge/how-to-bridge.md

# How to Bridge

### Nomad vs Connext, which should I use? <a href="#nomad-vs-connext-which-should-i-use" id="nomad-vs-connext-which-should-i-use"></a>

There are two options available to send funds through [the Nomad token bridge web app](https://app.nomad.xyz), Nomad and [Connext](https://www.connext.network/). These are two distinct protocols that are complementary to one another. We have partnered with Connext to provide an optimal experience for users!

Nomad is a secure, gas-efficient cross-chain messaging protocol. The Nomad token bridge leverages Nomad message passing channels to enable users to bridge funds between networks. This takes, on average, 35-60 minutes due to Nomad's [optimistic security window](https://docs.nomad.xyz/the-nomad-protocol/security/root-of-trust/fraud/optimistic-timeout-period). There are no Nomad imposed fees, just pay gas fees on the underlying chains!

Connext provides cross-chain liquidity pools for Nomad assets, meaning users can receive funds on the destination chain much faster (less than 10 minutes) for a small fee. Connext is not available for every asset and may not be available for larger sums. We recommend using Nomad if you intend to send large transfers.

### Bridging Through Nomad[#](https://docs.nomad.xyz/bridge/nomad-gui.html#bridging-through-nomad) <a href="#bridging-through-nomad" id="bridging-through-nomad"></a>

Bridging assets using Nomad is intuitive and easy with the Nomad GUI. In this tutorial, we will walk through the steps required to bridge your assets.

Please find our production bridge GUI at [app.nomad.xyz](https://app.nomad.xyz/).

If you would like to test our bridge using testnet funds before using real funds, please visit our development GUI at [development.app.nomad.xyz](https://development.app.nomad.xyz/).

Connect to MetaMask:

![Connect Metamask](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FnCMXI7VcvEFLMaE5G56G%2Fconnect-metamask.png?alt=media\&token=1543eb9f-f3fc-4532-85f1-fd6f7cd18adb)

Select origin and destination networks:

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FGmnEP208OcuNC3zMh2kg%2Fselect-networks.png?alt=media\&token=66ce7234-83bd-4eac-8324-666ddfe63864)

(Optional) Change Destination address. This is set as your wallet address by default. Click "edit". A modal will pop up, click "change" inside the input. Then copy your address, click to paste, and save.

{% hint style="danger" %}
Sending assets to an address you do not control can result in a permanent loss of funds!
{% endhint %}

![Edit recipient address](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FpnLjNqMfxGFTRAQA0mxX%2Fchange-dest-1.png?alt=media\&token=436a5f69-817f-4f91-a812-904f8636a338) ![Save recipient address](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FLq0PsPIHqULgehvlmLug%2Fchange-dest-2.png?alt=media\&token=6c5b3006-cfc5-4cbd-9239-c023a6b0e549)

Select the asset you want to send using the asset dropdown menu and the amount you want to send using the input prompt:

![Select asset and enter amount](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FANuHfxgtiaopiWSikgmr%2Fselect-token.png?alt=media\&token=dc3cdde5-b130-4370-bab1-47d3dba12d9a)

Click `Next`:

![Input transfer data](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F5pxvFWbkvAlndbZpsy5e%2Finput-data.png?alt=media\&token=6f5d407b-cc14-4bf3-b53c-0aae2cd1d14d)

Review your transaction details and associated fees. Check if Connext liquidity is available for your transfer for a faster bridging experience! If proceeding with Connext, continue reading [here](#fast-transfers-with-connext).

![Select protocol and review](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F9kfCw7x6g76swHo6To6z%2Freview.png?alt=media\&token=1fe86254-640e-488d-94dd-08144785ed88)

Click `Bridge Tokens` and approve the transaction in Metamask:

![Approve Bridge Transaction](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FHSHHz1UqGN6cgJRSAPvw%2Fsending.png?alt=media\&token=6012e8ed-c695-4f0e-85be-8bacfd830dd0)

After approving the transaction, you will be taken to the transaction details page. Here, you will see the estimated time remaining for your transfer to complete. Please save your transaction hash for convenience. If you lose it, you can visit your wallet address on the block explorer of the origin network and find the transaction again.

{% hint style="info" %}
You must return to the Transaction Page after bridging has concluded to pay for gas and complete your transfer. Nomad may cover the processing and gas fees for some chains.
{% endhint %}

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F7x7qn3Jdr5y0O4VWfpsa%2Ftransfer-pending.png?alt=media\&token=741dcba0-ed29-42fa-a949-1b3c6499fbc5)

You can expand the time estimate tab to track your transaction status by clicking the down arrow in the blue box:

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2F1nhJHas7jkxrAU9i1kX9%2Fexpand-status.png?alt=media\&token=0aa7b52c-7df2-4e39-8e94-049870e060e8)

(Optional) If you navigated away from the GUI at any point and want to find your transfer's progress page again, visit <https://app.nomad.xyz/tx> and enter the origin network and your transfer's transaction hash.

![Search bridge transfer](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FkAEpP6suEFxczQiefzN9%2FScreen%20Shot%202022-06-30%20at%2010.25.18%20AM.png?alt=media\&token=395f519e-a9da-4c2e-8eb1-9d2c34d197e9)

Once your transfer has completed, you should see the below display and your funds will be in the account of your destination address. If your transfer is taking longer than expected, please reach out to us on [Discord](https://discord.gg/RurtmJApqm) in the #support channel:

![Finished](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FkILcCDa4Y9BXJME5DhbL%2Ftransfer-complete.png?alt=media\&token=f24915aa-08e5-4de9-98c9-6e808113667e)

### Completing a Transfer (Ethereum Destination Only)

If you are sending to Ethereum, there is one additional processing step due to the high cost of processing transactions on Ethereum. You will see the following display and should click "Complete Transfer" and complete the MetaMask transaction. After this, your funds should be at your destination on Ethereum!

![Claim on Ethereum](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FfimCFHA1tlInMXmMV6z3%2Fcomplete-transfer.png?alt=media\&token=ff4d87bc-0d13-428d-982f-ee246a960a9b)

## Fast Transfers with Connext

Fill out data for your transfer and click "Next." Select "Connext." If there is liquidity available for your transfer, it will calculate associated fees for your transaction. Note that Connext collects gas fees in the asset that is being sent.

If there is not liquidity available, you can [continue by using Nomad](#bridging-through-nomad).

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FLSqU2uCxbMFdQYILQkYo%2Fcheck-connext.png?alt=media\&token=04a226ca-1959-4015-bf52-be75667183b1)

Click `Send` and approve the transaction in MetaMask!

In a few minutes, you will see your transfer appear in a table below. Click "Claim" to submit a transaction to receive your funds on the destination chain.

Click "View" to go to your transaction in the ConnextScan block explorer. Or you can visit `https://connextscan.io/tx/<yourtransactionhash>`.

![](https://1068756784-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FJAvJLO26ISS4zqpWVWWq%2Fuploads%2FSPM2G9Y2nlBV2D8YtVGm%2Fconnext-claim.png?alt=media\&token=aafdf26d-fc9a-4d0b-b78a-f6a4f94b8f6b)
