# Source: https://docs.intelligems.io/integrations/google-analytics-4-integration/integrating-with-ga4-using-google-tag-manager.md

# Integrating with GA4 using Google Tag Manager

Depending on your GA4 setup, you may need to route the Intelligems `experience_impression` event from the Data Layer to GA4 using Google Tag Manager. This step-by-step guide will help you set up the Tag in Google Tag Manager to do this.

1. **Add an Intelligems setting so that the GA4 event is added to the Data Layer**. In your theme code, above the Intelligems script in the \<head> of the theme, add:\\

   ```html
   <script>
     window.igSettings = {
       useDataLayer: true
     }
   </script>
   ```
2. In Google Tag Manager (GTM), first create the Variable. Select "Variables" then "New":

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-1d3afbcfd2f7e310c22b06495fb823bda38e9778%2FGTM1.png?alt=media" alt=""><figcaption></figcaption></figure>
3. Click on "Variable Configuration":

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-dce12cae4e6b5f53982e86fbb3039fe956cfd943%2FGTM2.png?alt=media" alt=""><figcaption></figcaption></figure>
4. Choose "Data Layer Variable":\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-42e9aab49862a364e574946fb6e8dc95d8a1c794%2FGTM3.png?alt=media" alt=""><figcaption></figcaption></figure>
5. Enter `exp_variant_string` for Data Layer Variable Name, title the variable `exp_variant_string`, and click Save:\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2ef56d7f22bdc03cb74970a8e453eaffb22c728a%2FGTM-var-1.png?alt=media" alt=""><figcaption></figcaption></figure>
6. Now create the tag. Click "Tags" then click "New":\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9658eab0d5af07ab4dac4d09b9d7326f3cae8d1b%2FGTM5.png?alt=media" alt=""><figcaption></figcaption></figure>
7. Click Tag Configuration:

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f2405ceecc8e7529a08789f2c99bfbc561c88254%2FGTM6.png?alt=media" alt=""><figcaption></figcaption></figure>
8. Choose Google Analytics:\\

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b2050de70c00af22dd761182db92033d4d2379d9%2FGTM7.png?alt=media" alt=""><figcaption></figcaption></figure>
9. Choose Google Analytics: GA4 Event

   <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-eb7318e4b98df71389bc51c3956584cf5034754a%2FGTM8.png?alt=media" alt=""><figcaption></figcaption></figure>
10. Enter your GA4 Measurement ID, enter `experience_impression` as the Event Name, enter `exp_variant_string` as the Event Parameter, and choose `exp_variant_string` as the Event Value by clicking on the variable picker icon (choosing the Variable we created in step 5):\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-33394ad68f1e2f6cbb9157eb1a79ee0a999360ae%2FGTM-var-2.png?alt=media" alt=""><figcaption></figcaption></figure>
11. Click Triggering:\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bfde97b301592ffc9dc2280ce84f8469abfc2b62%2FGTM10.png?alt=media" alt=""><figcaption></figcaption></figure>
12. Click Trigger Configuration:

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-10f4cf7f718ff6a00da9020f732e96f17d2b7081%2FGTM12.png?alt=media" alt=""><figcaption></figcaption></figure>
13. Choose Custom Event:\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-bd1e38737a3b58668772ae1efcd981ca651f1703%2FGTM13.png?alt=media" alt=""><figcaption></figcaption></figure>
14. Enter `experience_impression` for Event Name, title the trigger `experience_impression` , and click Save:\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-e043fcd0f1159d22bbfac3a8c5f6b3030d0caa2e%2FGTM14.png?alt=media" alt=""><figcaption></figcaption></figure>
15. Click Submit:\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2a05ecefc3d5e93d4c7f2a58ee2683bd9efa0dcb%2FGTM16.png?alt=media" alt=""><figcaption></figcaption></figure>
16. Click Publish:\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-f94b5b44a7da775855ea69910443ead07c9055a9%2FGTM17.png?alt=media" alt=""><figcaption></figcaption></figure>
17. Give the version a name and click Continue:\\

    <figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-9fd228a8c2011e0a2b051046d6ee5ab4628ea0e0%2FGTM18.png?alt=media" alt=""><figcaption></figcaption></figure>
