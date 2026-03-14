# Source: https://docs.flux.ai/tutorials/tutorial-embed-a-flux-project.md

# Embedding Flux Projects in Websites and Tools

In the spirit of making collaboration easier and in response to several requests, you can now embed Flux projects with an iFrame. This works in many places you might expect like websites, blogs, and even project management tools like Trello. We're hoping that this ability will unlock collaborative use cases that we haven't even thought of!

## Getting the Embed Code

To embed your Flux project, just copy the embed code from the Share menu (top-right corner).

![](https://uploads.developerhub.io/prod/86Yw/ny0e7usf7wrwobkml9wu4hjkn5ffbj3ni0njw4nagbjoh9xoo271vbs28x778zk3.png)

That code snippet will look like this:

```html
<iframe
      height="450"
      width="800"
      allowfullscreen
      src="https://www.flux.ai/jharwinbarrozo/3v3-regulator?embed=1"
    />
```



## Embedding Examples

### Schematic Example

<iframe height="450" width="100% !important" max-width="100%" allowfullscreen src="https://www.flux.ai/jharwinbarrozo/3v3-regulator-with-led?editor=schematic&embed=1" />

### PCB Example

If you want to have the PCB editor as the default view, you need to go to the PCB editor view and then copy the embed code from the Share menu. It will look like this:

```html
<iframe 
        height="450" 
        width="800" 
        allowfullscreen src="https://www.flux.ai/jharwinbarrozo/3v3-regulator?editor=pcb_2d&embed=1" />
```



<iframe height="450" width="100% !important" max-width="100%" allowfullscreen src="https://www.flux.ai/jharwinbarrozo/example-simulation-of-astable-multivibrator-circuit?editor=pcb_3d&embed=1" />

### Using iFramely

Flux is also compatible with iFramely for apps that use this integration. iFramely makes it easier to control parameters like height and width of the embed without editing any code. Here's an example of [how to embed Flux document with iFramely](https://iframely.com/embed/https%3A%2F%2Fwww.flux.ai%2Fnatarius%2Fexample-blinking-led-demo%3Ftest%3D53723562).

## Customization Options

When embedding your Flux projects, you can customize several aspects:

- **Dimensions**: Adjust the height and width parameters to fit your website or tool
- **Default View**: Choose between schematic view, 2D PCB view, or 3D PCB view
- **Visibility**: Control what aspects of the project are visible to viewers

## What's Next

Now that you understand how to embed Flux projects, you might want to explore:

- [Collaboration Deep Dive](https://docs.flux.ai/flux/tutorials/tutorial-collaboration-deep-dive) - Learn more about collaboration features
- [Version Control](https://docs.flux.ai/flux/tutorials/version-control---deep-dive) - Understand how to track changes to your embedded projects
- [Reusing Projects](https://docs.flux.ai/flux/tutorials/reusing-community-projects) - Discover how to leverage existing projects
- [PCB Design Review](https://docs.flux.ai/flux/tutorials/pcb-design-review) - Learn how to review designs with your team

Have feedback or an idea of how to improve embedding Flux documents? [Post your feedback and ideas here](https://feedback.flux.ai/featurerequests)!