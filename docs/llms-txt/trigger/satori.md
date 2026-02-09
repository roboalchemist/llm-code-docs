# Source: https://trigger.dev/docs/guides/examples/satori.md

> ## Documentation Index
> Fetch the complete documentation index at: https://trigger.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate OG Images using Satori

> Learn how to generate dynamic Open Graph images using Satori and Trigger.dev.

## Overview

This example demonstrates how to use Trigger.dev to generate dynamic Open Graph (OG) images using Vercel's [Satori](https://github.com/vercel/satori). The task takes a title and image URL as input and generates a beautiful OG image with text overlay.

This can be customized and extended however you like, full list of options can be found [here](https://github.com/vercel/satori).

## Task code

```tsx trigger/generateOgImage.ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";
import satori from "satori";
import sharp from "sharp";
import { join } from "path";
import fs from "fs/promises";

export const generateOgImage = schemaTask({
  id: "generate-og-image",
  schema: z.object({
    width: z.number().optional(),
    height: z.number().optional(),
    title: z.string(),
    imageUrl: z.string().url(),
  }),
  run: async (payload) => {
    // Load font
    const fontResponse = await fetch(
      "https://github.com/googlefonts/roboto/raw/main/src/hinted/Roboto-Regular.ttf"
    ).then((res) => res.arrayBuffer());

    // Fetch and convert image to base64
    const imageResponse = await fetch(payload.imageUrl);
    const imageBuffer = await imageResponse.arrayBuffer();
    const imageBase64 = `data:${
      imageResponse.headers.get("content-type") || "image/jpeg"
    };base64,${Buffer.from(imageBuffer).toString("base64")}`;

    const markup = (
      <div
        style={{
          width: payload.width ?? 1200,
          height: payload.height ?? 630,
          display: "flex",
          backgroundColor: "#121317",
          position: "relative",
          fontFamily: "Roboto",
        }}
      >
        <img
          src={imageBase64}
          width={payload.width ?? 1200}
          height={payload.height ?? 630}
          style={{
            objectFit: "cover",
          }}
        />
        <h1
          style={{
            fontSize: "60px",
            fontWeight: "bold",
            color: "#fff",
            margin: 0,
            position: "absolute",
            top: "50%",
            transform: "translateY(-50%)",
            left: "48px",
            maxWidth: "60%",
            textShadow: "0 2px 4px rgba(0,0,0,0.5)",
          }}
        >
          {payload.title}
        </h1>
      </div>
    );

    const svg = await satori(markup, {
      width: payload.width ?? 1200,
      height: payload.height ?? 630,
      fonts: [
        {
          name: "Roboto",
          data: fontResponse,
          weight: 400,
          style: "normal",
        },
      ],
    });

    const fileName = `og-${Date.now()}.jpg`;
    const tempDir = join(process.cwd(), "tmp");
    await fs.mkdir(tempDir, { recursive: true });
    const outputPath = join(tempDir, fileName);

    await sharp(Buffer.from(svg))
      .jpeg({
        quality: 90,
        mozjpeg: true,
      })
      .toFile(outputPath);

    return {
      filePath: outputPath,
      width: payload.width,
      height: payload.height,
    };
  },
});
```

## Image example

This image was generated using the above task.

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=10c7715e00714ea7ef7c27bb7ace5c0c" alt="OG Image" data-og-width="1200" width="1200" data-og-height="630" height="630" data-path="images/react-satori-og.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8cd98cbeef77cb233b870851ce7cb74f 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=6fe23d397f6b7c27ea5c4dd471315ae9 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3b5900f0b2fba062fa9b5255410404c0 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3c140d3148b7f9820fbb83576aa50635 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=4ab2adcc93d6e0fde7541cf4fd62df15 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/react-satori-og.jpg?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f588de73d95f7c3cebb82a4278de3ec5 2500w" />

## Testing your task

To test this task in the [dashboard](https://cloud.trigger.dev), you can use the following payload:

```json  theme={"theme":"css-variables"}
{
  "title": "My Awesome OG image",
  "imageUrl": "<your-image-url>",
  "width": 1200, // optional, defaults to 1200
  "height": 630 // optional, defaults to 630
}
```
