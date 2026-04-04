# Source: https://docs.intelligems.io/developer-resources/javascript-api/campaigns-object/campaigns.sethistorystatus-params.md

# campaigns.setHistoryStatus(params)

{% hint style="success" %}
Use this to customize how you include or exclude visitors from Intelligems campaigns
{% endhint %}

This function expects **two** parameters:

1. campaignId: full uuid for the campaign you want to modify
2. status: one of "E" (exclude) "I" (include) or "U" (unassigned) *most use cases will only utilize exclude or include*

Call it like `window.igData.campaigns.setHistoryStatus("ef2c64e6-aac3-47c6-98b2-1854f641afd1", "U")`

This function has no return value if successful. However, you'll see console warnings if you pass an invalid campaignId or status

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-6c81fd9db730c2e10666e555119d9aea183e60c7%2FScreenshot%202023-11-30%20at%2012.03.31%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-ada2d9b5d52f8603090d632079c5f139d71a4d8a%2FScreenshot%202023-11-30%20at%2012.04.11%20PM.png?alt=media" alt=""><figcaption></figcaption></figure>
