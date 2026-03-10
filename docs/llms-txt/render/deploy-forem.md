# Source: https://render.com/docs/deploy-forem.md

# Deploy Forem

[Forem](https://github.com/forem/forem) is open source software for building communities.
It is the platform that powers [dev.to](https://dev.to), and allows members to share posts, create
classified listings, send direct messages, listen to podcasts, and
[much more](https://dev.to/devteam/for-empowering-community-2k6h).

[image: Forem screenshot showing posts and listing]

You can start building your community and deploy Forem to Render with the following components:

- A Rails web service that runs the main app.
- A Sidekiq worker that handles background jobs.
- An Elasticsearch instance for in-app searching.
- A [Render Key Value](key-value) instance to cache data.
- A [Render Postgres database](postgresql) as the primary database.

## Deployment

### Prerequisites

Forem requires [SendGrid](https://sendgrid.com/) for sending transactional emails to setup the admin
account through the browser. See the [SendGrid docs](https://sendgrid.com/docs/ui/account-and-settings/api-keys/#creating-an-api-key)
for help creating an SMTP Relay API key.

### One-Click Deploy

Use the button below to deploy Forem on Render.

<deploy-to-render repo="https://github.com/render-examples/forem">
</deploy-to-render>

### Configure the environment

1. Set `APP_DOMAIN` in the `rails` environment group.

   If you're using a [custom domain](custom-domains),
   you'll need to [configure your DNS](configure-other-dns).
   Otherwise, wait for the Forem web service to be created and copy its `.onrender` domain.

2. Configure SendGrid for account email confirmation.

   Set `SENDGRID_API_KEY` to your SendGrid SMTP Relay API key in the `rails` environment group.
   Add the email you configured with SendGrid under `DEFAULT_EMAIL` in the `rails` environment group

## Setup

### Creating the admin user

You will need to configure your admin account after the initial Forem deploy.

Visit your newly created Forem and fill out the form to create the admin account.
Render generates the "New Forem Secret" and sets it as the `FOREM_OWNER_SECRET` environment variable.
You can find its value in the `rails` environment group.

Once you complete the form, confirm your email and sign in.
Forem will ask you to complete setup on the configuration page.
See the [Basic Site Configuration Guide](https://docs.forem.com/creators/configure-forem/)
for more instructions on configuring Forem.

If you encounter problems confirming your email see [Troubleshooting](#troubleshooting) for tips.

### Integrations

Forem integrates with many other services to provide more features.
Visit the Forem docs to see the [some of the services](https://docs.forem.com/technical-overview/stack/)
and the [environment variables](https://github.com/forem/forem/blob/master/.env_sample) they require to function.

We recommend integrating [Cloudinary](https://cloudinary.com/)
to serve uploaded images with a CDN. Viewing uploaded images such as profile pictures,
cover photos, and article photos requires Cloudinary or [Imgproxy](https://docs.forem.com/installation/imgproxy/). See the
[Cloudinary docs](https://cloudinary.com/documentation/how_to_integrate_cloudinary)
to set up your account and get API credentials. Update the `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`,
and `CLOUDINARY_CLOUD_NAME` environment variables in the `rails` environment group.

Forem can store uploaded images in [AWS S3](https://aws.amazon.com/s3/) or on [a Render Disk](disks).
We use Render Disks in this example as an easy to setup and inexpensive solution.
You can find more details on Render Disks in the [docs](disks#disk-limitations-and-considerations).
You can switch to using AWS S3 by configuring the `AWS_ID`, `AWS_SECRET`,
`AWS_BUCKET_NAME`, and `AWS_UPLOAD_REGION` environment variables.

### Invite Your Users

Once you're done with setup, you can invite users and start building your community!

## Troubleshooting

If you have questions or need help, feel free to get in touch on [Discord](https://discord.gg/SpCmUMxhEy) or [support@render.com](mailto:support@render.com).

### Confirming your account

If you're unable to confirm your account through the SendGrid email, you can manually edit your account through the Rails console.

1. Enter the web shell for your Rails web server in the Render Dashboard.

2. Open the Rails console:

   ```bash
   source scripts/services.env
   bin/rails c
   ```

3. Find your user and set the `confirmed_at` field

   ```ruby
   User.ids
   # You will usually be the user with id 1
   user = User.find(1)
   user.confirmed_at = Time.current
   user.save
   ```