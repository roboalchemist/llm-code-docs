# Source: https://ngrok.com/docs/using-ngrok-with/docker/desktop.md

> ## Documentation Index
> Fetch the complete documentation index at: https://ngrok.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Using ngrok Docker Desktop

> Learn how to use ngrok with Docker Desktop.

export const YouTubeEmbed = ({className, title, videoId, ...props}) => {
  return <div className={`relative aspect-video mb-3 ${className}`} {...props}>
      <iframe src={`https://www.youtube.com/embed/${videoId}`} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen className="absolute inset-0 w-full h-full" title={title} />
    </div>;
};

The ngrok Docker Desktop Extension allows you to use ngrok's API Gateway cloud service to forward traffic from internet-accessible endpoint URLs to your local Docker containers.

The extension provides tools to:

* Create and manage endpoints
* Apply Traffic Policy
* Configure custom URLs and endpoint binding type
* Enable endpoint pooling for load balancing scenarios

<YouTubeEmbed videoId="v5SlQXRouPs" title="ngrok's Docker Extension" />

## Installation

Click [here](https://open.docker.com/extensions/marketplace?extensionId=ngrok/ngrok-docker-extension) to add the ngrok extension to Docker Desktop.

## Quick start

1. After installing the extension, you will be prompted to add your [ngrok authtoken](https://dashboard.ngrok.com/get-started/your-authtoken).
2. Start an endpoint by clicking `+` icon on the container you want to put online.
3. Optionally specify a custom URL and [Traffic Policy](/traffic-policy/).

You now have an endpoint URL for your container that you can share.


Built with [Mintlify](https://mintlify.com).