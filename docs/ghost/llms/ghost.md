# Source: https://docs.ghost.org/migration/ghost.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ghost.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Migrating from Ghost To Ghost

> Migrate from a self-hosted instance to Ghost(Pro) with this guide

<Note>
  If you're a Ghost(Pro) customer, our team may be able to help you migrate your content and subscribers. Learn more about our [Concierge service](https://ghost.org/concierge/).
</Note>

This guide will walk you through the process of migrating from a self-hosted Ghost instance on your own server to Ghost(Pro).

## Prerequisites

If your self-hosted site is running an older major version of Ghost, you may need to update. Check the latest [version of Ghost on GitHub](https://github.com/TryGhost/Ghost/releases), and follow this [upgrade guide](/update/).

## Back up your data

The first step towards moving from your own self-hosted Ghost instance to Ghost(Pro) is to retrieve all of your data from your server to your local machine. It’s best to do this first, to ensure you have a backup in place.

<Note>
  The commands in this guide assume you followed our [Ubuntu guide](/install/ubuntu/) to set up your own instance. If you used another method, you’ll need to adapt the paths in the commands to suit.
</Note>

### Exporting content

Log into Ghost Admin for your self-hosted in production and navigate to the **Import/Export** view, and click **Export**, then click the **Content & settings** button to download your content. This will be `.json` file, with a name like `my-site.ghost.2020-09-30-14-15-49.json`.

<Frame>
  <img src="https://mintcdn.com/ghost/aOtHGZ0BjEyodlHE/images/ghost-migration-tools-export-options.png?fit=max&auto=format&n=aOtHGZ0BjEyodlHE&q=85&s=dd3c8808a49396b5893e8967dd2ed895" width="1364" height="556" data-path="images/ghost-migration-tools-export-options.png" />
</Frame>

### Routes and redirects

From the **Labs** page, click **Download current redirects** to get your redirects file. This will be called `redirects.yaml` (or `redirects.json` depending on your Ghost version). If you’re using custom routes, click **Download current routes.yaml** to get your `routes.yaml` file.

<Frame>
  <img src="https://mintcdn.com/ghost/aOtHGZ0BjEyodlHE/images/ghost-migration-routes-redirects.png?fit=max&auto=format&n=aOtHGZ0BjEyodlHE&q=85&s=7f8475de1e27803c981f8a0223a6fc87" width="1384" height="1194" data-path="images/ghost-migration-routes-redirects.png" />
</Frame>

### Themes

Navigate to the **Themes** view, then go to **Installed** and click the **...** option, next to the Active label, to download your current theme. This will be a `.zip` file. Optionally, if you have other themes that you’d like to save, download them and back them up.

<Frame>
  <img src="https://mintcdn.com/ghost/aOtHGZ0BjEyodlHE/images/ghost-download-active-theme.png?fit=max&auto=format&n=aOtHGZ0BjEyodlHE&q=85&s=8a1d6eb156069ac4eabc9254444263ba" width="1270" height="472" data-path="images/ghost-download-active-theme.png" />
</Frame>

### Images

To download your images, you’ll need shell access to your server. If you’re unable to gain shell access to your current web host, you may need to contact their support team and ask for a zip of your images directory.

Once you’re logged in to your server, `cd` to the `content` directory:

```bash  theme={"dark"}
cd /var/www/ghost/content
```

And then `zip` the `images` directory with all its contents:

```bash  theme={"dark"}
zip -r images.zip images/*
```

Ensure your `images` folder only contains images. Any other file types may cause import errors.

Now we need to get that zip file from your server onto your local machine:

```bash  theme={"dark"}
scp user@123.456.789.123:/var/www/ghost/content/images.zip ~/Desktop/images.zip
```

The folder structure should look like this, with `images` being the only top-level folder once unzipped:

<Frame>
  <img src="https://mintcdn.com/ghost/KePyCzI5-bxtjueF/images/a28febce-images-in-finder_huf248f9006ca4711e6e56a11852458172_99427_1260x0_resize_q100_h2_box.webp?fit=max&auto=format&n=KePyCzI5-bxtjueF&q=85&s=089e9370f7047f700d885005f13cbf73" width="1260" height="766" data-path="images/a28febce-images-in-finder_huf248f9006ca4711e6e56a11852458172_99427_1260x0_resize_q100_h2_box.webp" />
</Frame>

## Uploading to Ghost(Pro)

Once you’ve retrieved all of these exports, you can upload them to Ghost(Pro) in the same order.

### Content

Log into your new Ghost(Pro) site, and head to the **Import/Export** view. Next, click on to the **Universal Import** button, select your content `.json` file and click **Import**.

<Frame>
  <img src="https://mintcdn.com/ghost/aOtHGZ0BjEyodlHE/images/ghost-migration-universal-import.png?fit=max&auto=format&n=aOtHGZ0BjEyodlHE&q=85&s=ef4f6a97b19e740d1f11649e510b3d8c" width="1026" height="650" data-path="images/ghost-migration-universal-import.png" />
</Frame>

### Routes and Redirects

Navigate to the **Labs** view, click **Upload redirects JSON**, then select your `redirects.json` file to upload it. Then click **Upload routes YAML**, select your `routes.yaml` file to upload that.

### Themes

Head over to the **Themes** view, and click **Upload a theme**, select your theme `.zip` file, and activate it.

<Frame>
  <img src="https://mintcdn.com/ghost/aOtHGZ0BjEyodlHE/images/ghost-theme-upload-activate.png?fit=max&auto=format&n=aOtHGZ0BjEyodlHE&q=85&s=f3a60e316a3b035be90ff68079fba425" width="1122" height="478" data-path="images/ghost-theme-upload-activate.png" />
</Frame>

### Images

The final step is to upload your images. The best way to approach this depends on how big your `images.zip` file is. A large file will take longer to upload and process.

If your file is less than 500mb, you can upload this zip in the same way you uploaded your content JSON file. If the file is larger, it’s recommended to split it into multiple smaller files, whilst retaining the folder structure.

If you have a large image directory or encounter any errors, contact support so we can help upload your images.

***

## Summary

Congratulations on moving to Ghost(Pro). All that’s left to do is check over your content to ensure everything works as expected.

By hosting your site with us, you directly fund future product development of Ghost itself and allow us to make the product better for everyone 💘


Built with [Mintlify](https://mintlify.com).