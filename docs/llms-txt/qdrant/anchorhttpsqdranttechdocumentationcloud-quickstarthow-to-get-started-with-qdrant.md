# [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#how-to-get-started-with-qdrant-cloud) How to Get Started With Qdrant Cloud

How to Get Started With Qdrant Cloud - YouTube

[Photo image of Qdrant - Vector Database & Search Engine](https://www.youtube.com/channel/UC6ftm8PwH1RU_LM1jwG0LQA?embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

Qdrant - Vector Database & Search Engine

8.12K subscribers

[How to Get Started With Qdrant Cloud](https://www.youtube.com/watch?v=3hrQP3hh69Y)

Qdrant - Vector Database & Search Engine

Search

Watch later

Share

Copy link

Info

Shopping

Tap to unmute

If playback doesn't begin shortly, try restarting your device.

More videos

## More videos

You're signed out

Videos you watch may be added to the TV's watch history and influence TV recommendations. To avoid this, cancel and sign in to YouTube on your computer.

CancelConfirm

Share

Include playlist

An error occurred while retrieving sharing information. Please try again later.

[Why am I seeing this?](https://support.google.com/youtube/answer/9004474?hl=en)

[Watch on](https://www.youtube.com/watch?v=3hrQP3hh69Y&embeds_referring_euri=https%3A%2F%2Fqdrant.tech%2F)

0:00

0:00 / 1:53
•Live

•

[Watch on YouTube](https://www.youtube.com/watch?v=3hrQP3hh69Y "Watch on YouTube")

You can try vector search on Qdrant Cloud in three steps.

Instructions are below, but the video is faster:

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#setup-a-qdrant-cloud-cluster) Setup a Qdrant Cloud Cluster

1. Register for a [Cloud account](https://cloud.qdrant.io/signup) with your email, Google or Github credentials.
2. Go to **Clusters** and follow the onboarding instructions under **Create First Cluster**.

![create a cluster](https://qdrant.tech/docs/gettingstarted/gui-quickstart/create-cluster.png)

3. When you create it, you will receive an API key. You will need to copy it and store it somewhere self. It will not be displayed again. If you loose it, you can always create a new one on the **Cluster Detail Page** later.

![get api key](https://qdrant.tech/docs/gettingstarted/gui-quickstart/api-key.png)

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#access-the-cluster-ui) Access the Cluster UI

1. Click on **Cluster UI** on the **Cluster Detail Page** to access the cluster UI dashboard.
2. Paste your new API key here. You can revoke and create new API keys in the **API Keys** tab on your **Cluster Detail Page**.
3. The key will grant you access to your Qdrant instance. Now you can see the cluster Dashboard.

![access the dashboard](https://qdrant.tech/docs/gettingstarted/gui-quickstart/access-dashboard.png)

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#authenticate-via-sdks) Authenticate via SDKs

Now that you have your cluster and key, you can use our official SDKs to access Qdrant Cloud from within your application.

bashpythontypescriptrustjavacsharpgo

```bash
curl \
  -X GET https://xyz-example.eu-central.aws.cloud.qdrant.io:6333 \
  --header 'api-key: <your-api-key>'