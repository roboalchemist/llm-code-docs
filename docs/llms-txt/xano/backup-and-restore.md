# Source: https://docs.xano.com/xano-features/instance-settings/backup-and-restore.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Backup And Restore

## How do backups work in Xano?

On all of our paid plans, Xano keeps a rolling 3-day backup of your entire instance automatically, should the need arise to restore to an earlier point.

You also have the ability to take and restore backups manually.

If you are on a free plan, please note that **no backups are available**.

## Creating a Backup

<Steps>
  <Step title="From your instance selection screen, click next to the instance you want to create a backup of.">
    [Link to instance selection screen](https://app.xano.com/instance?mode=master)

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/45cc2876-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=93827ae193c780577131f338b1ee57c7" width="22" height="21" data-path="images/45cc2876-image.jpeg" />
    </Frame>
  </Step>

  <Step title="In the panel that opens, choose Database Backup.">
    &#x9;
  </Step>

  <Step title="Click Manual Backup">
    &#x9;
  </Step>

  <Step title="Check the option to include media storage if you'd like that to be included in your backup.">
    Please note that media storage should only be backed up if absolutely necessary, as it can greatly increase the size of and duration to backup / restore the instance.
  </Step>

  <Step title="Click to start the process.">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/dyVYERTquSXdpw_-/images/a10aff24-image.jpeg?fit=max&auto=format&n=dyVYERTquSXdpw_-&q=85&s=f26a9e72793a76a4340bad25e053353b" width="115" height="27" data-path="images/a10aff24-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Restoring a Backup

<Warning>
  It is \*\*strongly advised \*\*that you first create a backup before restoring another, just in case you need to roll back.
</Warning>

<Steps>
  <Step title="From your instance selection screen, click next to the instance you want to restore a backup of.">
    [Link to instance selection screen](https://app.xano.com/instance?mode=master)

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/45cc2876-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=93827ae193c780577131f338b1ee57c7" width="22" height="21" data-path="images/45cc2876-image.jpeg" />
    </Frame>
  </Step>

  <Step title="In the panel that opens, choose Database Backup.">
    &#x9;
  </Step>

  <Step title="Click Download and Restore">
    &#x9;
  </Step>

  <Step title="Choose the backup you'd like to restore and click">
    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/rOuOq7qlTNyaIMAW/images/5a3f6103-image.jpeg?fit=max&auto=format&n=rOuOq7qlTNyaIMAW&q=85&s=4e124b61bda97e417747fa7e473b3bb4" width="83" height="44" data-path="images/5a3f6103-image.jpeg" />
    </Frame>
  </Step>
</Steps>

## Custom Backup Policy

You can define your own custom schedule for when automatic backups take place.

<Steps>
  <Step title="From your instance selection screen, click next to the instance you want to adjust backup policy for.">
    [Link to instance selection screen](https://app.xano.com/instance?mode=master)

    <Frame>
      <img src="https://mintcdn.com/xano-997cb9ee/ClU5W_-qt6GI3QWZ/images/45cc2876-image.jpeg?fit=max&auto=format&n=ClU5W_-qt6GI3QWZ&q=85&s=93827ae193c780577131f338b1ee57c7" width="22" height="21" data-path="images/45cc2876-image.jpeg" />
    </Frame>
  </Step>

  <Step title="In the panel that opens, choose Database Backup.">
    &#x9;
  </Step>

  <Step title="Click Policy">
    &#x9;
  </Step>

  <Step title="Choose the time window you'd like your backups to run in.">
    Typically, backups will happen early morning PST hours. However, you can select your own time window to more closely align with your needs from here.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).