# Source: https://docs.replit.com/replitai/image-generation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Image generation

> Generate AI images directly in Replit and seamlessly integrate them into your projects with Agent's image generation capabilities.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

Create visual content for your applications using Agent's image generation <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d1edf942c27a1fdcb20453e78feb3cd9" alt="Image generation icon" data-og-width="24" width="24" data-og-height="24" height="24" data-path="images/icons/image.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=428973fe9d67c84128e4b50d912e992b 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ce9122a62c003f28aa2b5e9713355edf 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c48009152703f2031a4d0d825b5b7020 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f2c2ef1d26a9085f706f712ee62a96f6 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=817b4de821bb4b4cb37d4795c6c3725f 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f4070d67b24e8468480c2cd607cd4864 2500w" /> capabilities.

Transform your ideas into custom images, illustrations, and graphics that perfectly match your project's needs. Whether you're building a website, mobile app, or any creative project, Agent generates images that bring your vision to life.

<Frame>
  <img src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=1afcbec6348249b8ab3fa34e29906602" alt="Agent generating AI images for app development" data-og-width="870" width="870" data-og-height="482" height="482" data-path="images/image-generation/imagegen.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c286903a5d655d3c3b4bdeddd949dc17 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=a7781b82cfad8c0eaf0e0976f2298ab0 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=648ca3cd5e0de4cf4f3984ab5951b4f5 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=88efa43c5abd1cb3a63dce1b846a0acd 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=2ba67909cd4c03ce3a974143e8f6d71e 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/image-generation/imagegen.png?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=e0bc6dc8ac0c45d1c40da0ef131ea755 2500w" />
</Frame>

Image generation empowers builders to create unique visual content without needing design skills or external tools. Generate everything from icons and illustrations to backgrounds and UI elements directly within your development workflow.

## Features

Build visually compelling applications with Agent's image generation. This eliminates the need for stock photos, external design tools, or hiring designers for basic visual content. Whether you're creating a portfolio website, building a game, or designing a mobile app interface, image generation provides custom visuals tailored to your project.

Agent can perform the following image generation actions:

* **Custom image creation**: Generate images based on detailed descriptions and specifications
* **Style adaptation**: Create images in various artistic styles, from realistic to cartoon-like
* **Project integration**: Seamlessly add generated images directly to your app's codebase
* **Iterative refinement**: Modify and improve images based on your feedback

## Usage

To enable image generation and start creating custom images:

1. Open any Replit App with Agent enabled
2. Look for <img class="icon-svg" alt="Agent settings icon" src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=23a035924bb3c8c61e7ca996c76a90a1" data-og-width="16" width="16" data-og-height="16" height="16" data-path="images/icons/agent-settings.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=08dd975be952b60db564bcfedfc6f7fd 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=4c35dd49157af177d8e2ea495eb6fb51 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=5d87fc1ea8d58c3105dadceb194b4edb 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6d68bbc6b654bd433f2260669ddbf03b 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=889488d8482ad86f6bdbe4194eb648ce 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/icons/agent-settings.svg?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ce1af7526c6290400507c309b091e5f4 2500w" /> **Agent Tools** at the bottom right of the Agent pane
3. Enable <img class="icon-svg" src="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=d1edf942c27a1fdcb20453e78feb3cd9" alt="Image generation icon" data-og-width="24" width="24" data-og-height="24" height="24" data-path="images/icons/image.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=280&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=428973fe9d67c84128e4b50d912e992b 280w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=560&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=ce9122a62c003f28aa2b5e9713355edf 560w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=840&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=c48009152703f2031a4d0d825b5b7020 840w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=1100&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f2c2ef1d26a9085f706f712ee62a96f6 1100w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=1650&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=817b4de821bb4b4cb37d4795c6c3725f 1650w, https://mintcdn.com/replit/7jcTEkTXPQwUz2BL/images/icons/image.svg?w=2500&fit=max&auto=format&n=7jcTEkTXPQwUz2BL&q=85&s=f4070d67b24e8468480c2cd607cd4864 2500w" /> **Image generation**
4. Chat with Agent and ask it to generate images for your project

Agent automatically determines when to use image generation based on your requests. Describe the visual content you need, and Agent creates custom images that match your specifications.

### When Agent uses image generation

Agent triggers image generation when you request visual content for your projects:

| Use Case                | Example Prompt                                                |
| ----------------------- | ------------------------------------------------------------- |
| **App icons and logos** | "Generate a modern logo for my fitness tracking app"          |
| **Website backgrounds** | "Create a subtle gradient background for my portfolio site"   |
| **Game assets**         | "Generate pixel art sprites for my platformer game"           |
| **UI illustrations**    | "Create an illustration for my app's empty state screen"      |
| **Marketing visuals**   | "Generate a hero image for my landing page"                   |
| **Product mockups**     | "Create mockup images of my app running on different devices" |

### Best practices for image generation

Follow these guidelines to get the best results from Agent's image generation:

**Be specific and descriptive**

* Include details about style, colors, composition, and mood
* Specify dimensions or aspect ratios when relevant
* Mention the intended use (icon, background, illustration, etc.)

**Iterate and refine**

* Start with a basic description and refine based on results
* Ask Agent to modify specific aspects of generated images
* Request variations to explore different creative directions

**Consider your project's style**

* Maintain visual consistency across your app
* Specify style preferences that match your brand or design system
* Ask for images that complement your existing visual elements

### Example prompts

Try these example prompts to get started with image generation:

<AiPrompt>
  Generate a clean, modern icon for my task management app.
  The icon should be circular with a gradient background from blue to purple,
  featuring a simple checkmark symbol in white.
  Make it suitable for use as an app icon.
</AiPrompt>

<AiPrompt>
  Create a hero illustration for my coding tutorial website.
  Show a friendly cartoon character sitting at a computer with code on the screen.
  Use a warm color palette with blues and oranges.
  The style should be approachable and encouraging for beginners.
</AiPrompt>

<AiPrompt>
  Generate a set of pixel art enemies for my retro-style platformer game.
  I need a flying bat, a walking mushroom, and a jumping slime.
  Each should be 32x32 pixels with a limited color palette of 8 colors.
  Make them cute but slightly menacing.
</AiPrompt>

### Project integration

Agent seamlessly integrates generated images into your codebase:

* **Automatic file creation**: Generated images are saved directly to your project files
* **Code updates**: Agent updates your code to reference the new image files
* **Asset organization**: Images are placed in logical directories within your project structure

This streamlined workflow means you can generate and implement visual content without leaving your development environment.

<Note>
  Replit's image generation is powered by [Google's Imagen 4](https://deepmind.google/models/imagen/), a state-of-the-art text-to-image model that excels at creating high-quality, photorealistic images with fine details and improved text rendering capabilities.
</Note>

Learn more about [working with Agent](/replitai/agent) or explore other [AI tools](/category/replit-ai).
