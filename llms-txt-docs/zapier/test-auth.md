# Source: https://docs.zapier.com/platform/build/test-auth.md

# Test authentication

> Testing a user's authentication is crucially important, as it is later used to test subsequent trigger and action steps when built.

## Prerequisites

* Completed authentication configuration with your app's authentication scheme
* Set of valid user credentials for your app - recommended to use a new account specifically for testing so you don't clutter your core app account with testing data.

## Steps

1. In the final *Test your Authentication* step, enter user credentials
2. Select *Test Authentication* to make the test API call you configured
3. Successful authentication shows a green check and a *Request Successful* message at the top of the dialog.

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=a52fda38121be30f371421ffe834466f" data-og-width="1239" width="1239" data-og-height="539" height="539" data-path="images/60ebf09a1442345cc5d86b44440eb11c.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?w=280&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=ddf5264f31d4746b8febb155400edac1 280w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?w=560&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=d7f5a33cf68a5ca222617dcee853af8c 560w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?w=840&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=64edaeb283691e6fc0587e95c5ba23eb 840w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?w=1100&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=788f5d4739d72a240e3125b19990bfae 1100w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?w=1650&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=9e43d9f9cde248aaa40e2dcf982d2026 1650w, https://mintcdn.com/zapier-82f0e938/MptVjeuYuatFg3LM/images/60ebf09a1442345cc5d86b44440eb11c.webp?w=2500&fit=max&auto=format&n=MptVjeuYuatFg3LM&q=85&s=c4be7e7009ee3df04095feb21c3cca5c 2500w" />
</Frame>

4. The *Response* tab shows the JSON data response from your API, with each field and its data listed.

5. The *Bundle* tab shows the data Zapier stores about your authentication. Values returned by the test API call are stored in the `inputData` [bundle](/platform/build/bundle#inputdata) and can be accessed by `{{bundle.inputData.field}}` where `field` is the field key from the API response, for use in the [connection label](/platform/build/connection-label) or trigger and action requests. However, responses from the test API call are not stored for subsequent requests in the case of OAuth v2 and session authentication unless you use [computed fields](/platform/build/computed-test-field).

6. The *HTTP* tab shows the full request details for each API call Zapier made during the test.

7. The *Console* tab shows any additional data your API calls logged in Zapier if you use custom code for any part of your authentication.

8. Check each tab to ensure the expected data came through - it is possible to have an unsuccessful API call come through as successful if your API returns a message without an HTTP error code. Check the Response to make sure it includes the data expected from this API call, and if anything is incorrect, check the HTTP tab to help diagnose where things went wrong.

   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=60ddc617e6a3492a97070c411992152d" data-og-width="1239" width="1239" data-og-height="784" height="784" data-path="images/dacbdf7561aa6d2a78e599f12b80a325.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?w=280&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=8fc8a46a67ed257b4f5e4ceb9d99e47f 280w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?w=560&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=5c32729a9886d591c17624dbd0083c7f 560w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?w=840&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=502834fcf9af8c5912f10f57a6f38b43 840w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?w=1100&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=e6ba564eda78583e422205b6dd66c7fd 1100w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?w=1650&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=895511ffdf1bc7c854f65d57059cfe65 1650w, https://mintcdn.com/zapier-82f0e938/2ebL4bG5uJP5JVc0/images/dacbdf7561aa6d2a78e599f12b80a325.webp?w=2500&fit=max&auto=format&n=2ebL4bG5uJP5JVc0&q=85&s=eae28d4d7b7a8cf6d4a78aaf795419c6 2500w" />
   </Frame>

9. Clean up and remove older testing accounts from your core Zapier account. Open your [Zapier *Connected Accounts*](https://zapier.com/app/connections) page, and find your app's name (you may need to use the search box or `CMD`+`F` (Mac) or `Ctrl`+`F` (PC)). Click the app name. Once on the app's connections page, identify the connection to remove and click the three dots, then *Delete*, and confirm the deletion. Repeat for each subsequent testing account you added to clean up your authentication list.

   Then refresh your integration page in the Platform UI, and you'll only see the authentications that were not deleted.

   <Frame>
     <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=851d89dbac45d0ae610ddaf438ea71c7" data-og-width="1246" width="1246" data-og-height="562" height="562" data-path="images/943cd7b0ee2ada32492c834157a2eccb.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9617cebb41b80e095eba3d06ad339a62 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=287be3e83303ece19f56c3d4d9530b7a 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=1e50509411fb10da4478fe8c346eff5f 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f1f5ff0012d24d2801f7e71f47cce656 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=0832f7b311c5485c4240bc966067a4f2 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/943cd7b0ee2ada32492c834157a2eccb.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=cd3a3e133e668ba4eb5aeafcfec4b12c 2500w" />
   </Frame>

<Frame>
  <img src="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f52b4c4122537436aecbbdd48dd78bdf" data-og-width="1056" width="1056" data-og-height="468" height="468" data-path="images/b31f5c7f712c1a585e727b729248615a.webp" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?w=280&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=f89fd402bfb8cece2c752b58de20b940 280w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?w=560&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=9ba2bea7b41c15a054d58745ba3eaab8 560w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?w=840&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c78cd4414b39b624a79907185daf0c01 840w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?w=1100&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=c1df7576e1c5ffb8749de744798b4a99 1100w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?w=1650&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=695051fdf4044485de1408a0c3e6ef32 1650w, https://mintcdn.com/zapier-82f0e938/ziHY4Q2Lym35bUQM/images/b31f5c7f712c1a585e727b729248615a.webp?w=2500&fit=max&auto=format&n=ziHY4Q2Lym35bUQM&q=85&s=21ad1d5064b260f1938d01e7e5dc46d8 2500w" />
</Frame>

10. A caveat of testing in the Platform UI is that tokens are not saved in the Zapier database, so if you are testing the access/refresh token mechanism, make sure to test in a Zap in your account to avoid connections expiring or being marked as invalid.

***

*Need help? [Tell us about your problem](https://developer.zapier.com/contact) and we'll connect you with the right resource or contact support.*
