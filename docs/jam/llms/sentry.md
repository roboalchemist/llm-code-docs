# Source: https://jam.dev/docs/integrations/sentry.md

# Sentry

{% embed url="<https://youtu.be/S0gU8csDb4Q>" %}

You can connect Sentry and Jam in order to view your Sentry logs right from Jam. This gives you easy visibility of the bug from the frontend (captured with Jam) to all the other services across your infrastructure that the bug traces across (captured with Sentry).

The goal: make it much faster for engineers to find the issue causing any reported bug by pairing Jam + Sentry together.&#x20;

## How to get started and connect Jam & Sentry

1. Jam will detect if Sentry is installed on a website, and show a Sentry tab if Sentry is detected. Click on that tab to be guided through authenticating with Sentry.\
   ![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FGM27A0SjXL3q35mIBTIb%2FScreenshot%202023-07-03%20at%2011.37.52%20AM%20\(1\).png?alt=media\&token=d26f9e80-0ebd-4657-a8af-9f80e720381c)
2. You will be prompted to connect Sentry. Click on the button and go through the Sentry OAuth flow to connect Jam to Sentry.\
   ![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FifrOpWGzx4LKziAuwGXS%2FScreenshot%202023-07-03%20at%201.49.10%20PM%20\(1\).png?alt=media\&token=9a102408-72d2-4120-a322-5595c4471709)
3. If Sentry is not installed on the website, have no fear, there is another way to connect! Go to your Jam workspace settings, click on "Connected Apps", and connect to Sentry from there. \
   ![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2Fqo7l4h9PueLMstN542Xu%2FScreenshot%202023-08-02%20at%2018.40.47.png?alt=media\&token=07482cb0-d7cf-4d91-ba7b-886997cb9ca2)
4. Done! Now you can view Sentry events right from Jam.&#x20;

Now you will be able to see Sentry events from the same timestamp of the Jam right in the Jam.&#x20;

If you are on a Sentry business plan, you will be able to see events across all your Sentry projects. If you are on a lower Sentry tier, you will only be able to choose 1 project to view logs from at a time.&#x20;

You can scope the logs by timestamp, and filter by specific keywords to find relevant Sentry events. Click on any Sentry event listed in Jam to open up that log in Sentry.

## How are Sentry logs chosen to be surfaced in Jam?

Jam's goal is to show engineers relevant logs from Sentry right in Jam.&#x20;

Jam filters Sentry logs displayed in Jam by timestamp. By default, Jam will display Sentry logs from the 5 minutes before and after the Jam was created.

By default, Jam will filter the logs you see by the detected environment field sent to Sentry from the frontend. For example, if the client web application sends events to Sentry with the environment field "staging", then Sentry logs shown in the Jam will be default scoped to show "environment:staging".

![](https://1990502200-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FtAIPUIiSH7MWC0IHLJuD%2Fuploads%2FTibTVqrpJ5NjwDHedseM%2Fimage%20\(13\).png?alt=media\&token=c02847a7-7911-4d0f-a127-a1b78c17f742)

Our goal is to over time, be able to show you only the most relevant Sentry logs so that we help you quickly and easily trace bugs across your infrastructure. We'd love to hear how you've instrumented Sentry such that we can find the proper Sentry logs for any bug. Please reach out with any feedback to <hello@jam.dev>.

## Which plan includes the Sentry integration?

Integrating with Sentry is a team plan only feature in Jam. You can learn more about our pricing here: [jam.dev/pricing](https://jam.dev/pricing).
