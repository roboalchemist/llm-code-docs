# Source: https://www.mux.com/docs/integrations/cosmic.md

# Integrate with Cosmic
With the Mux Video integration for Cosmic JS, you can upload videos directly to Mux from your Cosmic JS Dashboard.
## 1. Install the Mux Extension

Log in to your Cosmic JS account and navigate to Your Bucket > Settings > Extensions. Click the Extensions tab and find the Mux Videos Extension. Hit Install.

<Image src="/docs/images/cosmic-install.png" width={1304} height={828} />

## 2. Enter Mux credentials

After installing, you will be redirected to the Extension settings page. Under Query Parameters, you will need to provide the Mux API credentials on your Mux account (mux\_access\_token, mux\_secret).

<Image src="/docs/images/cosmic-credentials.png" width={1304} height={828} />

If you need to generate a new Access Token, go to the Access Token settings of your Mux account dashboard.

<Image src="/docs/images/settings-api-access-tokens.png" width={500} height={500} />

The access token should have **Read** and **Write** permissions for Mux Video.

<Image src="/docs/images/new-access-token.png" width={760} height={376} alt="Mux Video access token permissions" sm />

Go back to the Cosmic Extensions setting page, enter your Mux credentials, and save your Extension.

## 3. Upload video

After installing the Extension and setting your Mux account keys, click the Mux Videos Extension link in the left-hand nav. Next, upload your videos.

<Image src="/docs/images/cosmic-upload.gif" width={1273} height={781} />

The Extension saves the uploaded video data to the Mux Videos Object Type. Now you can add your Mux Videos to any Object using an Object metafield. Then you can fetch Mux data into your application by using the `mux_playback_url` property located in the Object metadata.

<Image src="/docs/images/cosmic-edit.gif" width={1272} height={827} />

## 4. Playback

To retrieve your video for playback, check out the [Cosmic docs](https://www.cosmicjs.com/articles/mux-videos-extension-overview-jqpvec5d) to see how to add the Mux playback URL to your HTML Video player.

<GuideCard title="Set up playback" description="Set up your iOS application, Android application or web application to start playing your Mux assets" links={[{ title: 'Read the guide', href: '/docs/guides/play-your-videos' }]} />

<GuideCard title="Preview your video" description="Now that you have Mux assets, build rich experiences into your application by extracting images from your videos" links={[{ title: 'Read the guide', href: '/docs/guides/get-images-from-a-video' }]} />

<GuideCard title="Integrate Mux Data" description="Add the Mux Data SDK to your player and start collecting playback performance metrics." links={[{ title: 'Read the guide', href: '/docs/guides/track-your-video-performance' }]} />
