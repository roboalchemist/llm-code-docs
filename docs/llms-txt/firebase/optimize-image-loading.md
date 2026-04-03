# Source: https://firebase.google.com/docs/app-hosting/optimize-image-loading.md.txt

<br />

By default, built-in[Next.js image optimization](https://nextjs.org/docs/app/building-your-application/optimizing/images)is disabled onApp Hostingunless you explicitly set[`images.unoptimized`](https://nextjs.org/docs/pages/api-reference/components/image#unoptimized)to false or use a custom[Image Loader.](https://nextjs.org/docs/app/api-reference/config/next-config-js/images#example-loader-configuration)

You can configure a Next.js global image loader with the Image Processing Firebase Extension to enable on-demand optimization and delivery of images in your Next.js app onApp Hosting.

## Prerequisites

- You have a Firebase project and anApp Hostingbackend.
- Cloud Storageis enabled in your project.
- Cloud Functions for Firebaseis enabled in your project.

## Install the extension

Navigate to the[Image Processing Extension](https://extensions.dev/extensions/invertase/image-processing-api)in the Firebase Extensions Hub and select**Install in Firebase Console**. Follow the on-screen instructions.

### Configure[local image](https://nextjs.org/docs/pages/building-your-application/optimizing/images#local-images)optimization (optional)

If your application uses local images that you want to optimize using this extension, you need to configure the "Hostname" parameter during the extension installation process.

1. **During Extension Configuration:**When you reach the "Configure extension" step, locate the "Hostname" parameter.

2. **Set the Hostname:** Enter the default domain for your FirebaseApp Hostingbackend. This domain typically ends with`.hosted.app`.

Once installation is complete, the Image Processing API should be deployed as a function inCloud Functions. Navigate to the[Functions dashboard](https://console.firebase.google.com/project/_/functions)in theFirebaseconsole and copy the Image Processing API trigger URL.

## Set up a custom image loader

Create an[image loader](https://nextjs.org/docs/app/api-reference/components/image#loaderfile)that uses the deployed Image Processing API for every optimized[image component](https://nextjs.org/docs/pages/api-reference/components/image). As an optimization,[rewrite](https://nextjs.org/docs/app/api-reference/config/next-config-js/rewrites)to it so that it's served under the same FirebaseApp Hostingdomain and cached behind the same global CDN as your Next.js application.

First, add the following fields to your[`next.config.js`](https://nextjs.org/docs/app/api-reference/config/next-config-js)file:  

    // @ts-check

    /** @type {import('next').NextConfig} */
    const nextConfig = {
      images: {
        loader: "custom",
        loaderFile: "./loader.js",
      },
      async rewrites() {
        return [
          {
            source: "/_fah/image/:path*",
            destination:
              "<CLOUD_FUNCTIONS_URL>/:path*",
          },
        ];
      },
    }

    module.exports = nextConfig;

Then create a`loader.js`file in your root directory with the following contents:  

    "use client"

    export default function myImageLoader({ src, width, quality }) {
      if (process.env.NODE_ENV === "development") {
        return src;
      }

      const operations = [
        {
          operation: "input",
          type: "url",
          url: src,
        },
        { operation: "resize", width: width },
        { operation: "output", format: "webp", quality: quality || 75 },
      ];

      const encodedOperations = encodeURIComponent(JSON.stringify(operations));

      return `/_fah/image/process?operations=${encodedOperations}`;
    }

Create a commit that includes these changes and push it to your live branch. Then, wait for theApp Hostingrollout to complete.