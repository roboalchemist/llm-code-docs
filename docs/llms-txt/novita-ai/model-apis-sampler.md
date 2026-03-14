# Source: https://novita.ai/docs/guides/model-apis-sampler.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# A Brief Introduction to Sampler

Stable Diffusion Art. (n.d.). Samplers. Retrieved from [https://stable-diffusion-art.com/samplers/.](https://stable-diffusion-art.com/samplers/)

Many sampling methods are available in Novita AI, including Euler a, Heun, and DDIM. What are samplers? How do they work? What are the differences between them? Which one should you use? You will find the answers in this article.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_01.png" />
</Frame>

To produce an image, Stable Diffusion first generates a completely random image in the latent space. The noise predictor then estimates the noise of the image, which is subsequently subtracted from the image. This process is repeated multiple times, resulting in a clean image.

This denoising process is called sampling because Stable Diffusion generates a new sample image at each step. The method used in sampling is referred to as the `sampler` or `sampling method`.

Sampling is just one part of the Stable Diffusion model. Read the article "How Does Stable Diffusion Work?" if you want to understand the entire model.

Below is a sampling process in action. The sampler gradually produces cleaner and cleaner images.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_02.webp" />
</Frame>

While the framework is the same, there are many different ways to carry out this denoising process. It is often a trade-off between speed and accuracy.

### Samplers Overview

As of this writing, there are 19 samplers available in Novita AI, and this number seems to be growing over time. What are the differences?

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_03.png" />
</Frame>

You will learn about them in the later part of this article. The technical details can be overwhelming, so I will include a bird's-eye view in this section to help you get a general idea of what they are.

#### Old-School ODE Solvers

Let’s start with the easier ones. Some of the samplers on the list were invented more than a hundred years ago. They are old-school solvers for ordinary differential equations (ODE).

* Euler – The simplest possible solver.
* Heun – A more accurate but slower version of Euler.
* LMS (Linear Multi-Step Method) – Same speed as Euler but supposedly more accurate.

#### Ancestral Samplers

Do you notice that some sampler names have a single letter "a"?

* Euler a
* DPM2 a
* DPM++ 2S a
* DPM++ 2S a Karras

These are ancestral samplers. An ancestral sampler adds noise to the image at each sampling step. They are stochastic samplers because the sampling outcome contains some randomness.

Be aware that many other samplers are also stochastic, even if their names do not include an "a".

The drawback of using an ancestral sampler is that the image may not converge. Compare the images generated using Euler a and Euler below.

Euler a does not converge. (sampling steps 2–40)

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_04.webp" />
</Frame>

Euler converges. (sampling steps 2-40)

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_05.webp" />
</Frame>

Images generated with Euler a do not converge at high sampling steps, while images from Euler converge well.

For reproducibility, it is desirable to have the image converge. If you want to generate slight variations, you should use a variational seed.

#### Karras Noise Schedule

The samplers labeled "Karras" use the noise schedule recommended in the [Karras article](https://arxiv.org/abs/2206.00364). If you look closely, you will see that the noise step sizes are smaller near the end. This adjustment improves the quality of the images.

#### DDIM and PLMS

DDIM (Denoising Diffusion Implicit Model) and PLMS (Pseudo Linear Multi-Step Method) were the samplers included with the original Stable Diffusion v1. DDIM is one of the first samplers designed for diffusion models, while PLMS is a newer and faster alternative to DDIM. They are generally considered outdated and are not widely used anymore.

#### DPM and DPM++

DPM (Diffusion Probabilistic Model Solver) and DPM++ are new samplers designed for diffusion models released in 2022. They represent a family of solvers with similar architecture.

DPM and DPM2 are similar, with DPM2 being second-order (more accurate but slower).

DPM++ is an improvement over DPM.

DPM adaptive adjusts the step size adaptively. It can be slow since it doesn’t guarantee completion within the specified number of sampling steps.

#### UniPC

UniPC (Unified Predictor-Corrector) is a new sampler released in 2023. Inspired by the predictor-corrector method in ODE solvers, it can achieve high-quality image generation in 5-10 steps.

### How to Pick a Sampler

In this section, I will provide some objective comparisons to help you decide.

#### Image Convergence

In this section, I will generate the same image using different samplers with up to 40 sampling steps. The last image at the 40th step will be used as a reference for evaluating how quickly the sampling converges, with the Euler method serving as the benchmark.

> Euler, DDIM, PLMS, LMS Karras and Heun

First, let’s look at Euler, DDIM, PLMS, LMS Karras, and Heun as a group since they represent old-school ODE solvers or original diffusion solvers. DDIM converges at about the same number of steps as Euler but with more variations due to the injection of random noise during its sampling steps.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_06.png" />
</Frame>

PLMS did not perform well in this test.

LMS Karras seems to have difficulty converging and stabilizes at a higher baseline.

Heun converges faster but is twice as slow since it is a second-order method. Therefore, we should compare Heun at 30 steps with Euler at 15 steps, for example.

> Ancestral Samplers

If a stable, reproducible image is your goal, you should avoid using ancestral samplers, as they all fail to converge.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_07.png" />
</Frame>

> DPM and DPM2

DPM fast did not converge well. DPM2 and DPM2 Karras performs better than Euler but again in the expense of being two times slower.

DPM adaptive performs deceptively well because it uses its own adaptive sampling steps. It can be very slow.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_08.png" />
</Frame>

> DPM++ solvers

DPM++ SDE and DPM++ SDE Karras suffer the same shortcoming as ancestral samplers. They not only don’t converge, but the images also fluctuate significantly as the number of steps changes.

DPM++ 2M and DPM++ 2M Karras perform well. The Karras variant converges faster when the number of steps is high enough.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_09.png" />
</Frame>

> UniPC

UniPC converges a bit slower than Euler, but not too bad.

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_10.png" />
</Frame>

#### Speed

<Frame>
  <img height="404" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_11.png" />
</Frame>

Although DPM adaptive performs well in convergence, it is also the slowest.

You may have noticed the rest of the rendering times fall into two groups, with the first group taking about the same time (about 1x), and the other group taking about twice as long (about 2x). This reflects the order of the solvers. 2nd order solvers, although more accurate, need to evaluate the denoising U-Net twice. So they are 2x slower.

#### Quality

Of course, speed and convergence mean nothing if the images look crappy.

**Final images**

Let’s first look at samples of the image.

<Frame>
  <img height="1200" src="https://next-app-static.s3.ap-southeast-1.amazonaws.com/get-started/sampler_12.png" />
</Frame>

DPM++ fast failed pretty badly. Ancestral samples did not converge to the image that other samplers converged to.

Ancestral samplers tend to converge to an image of a kitten, while the deterministic ones tend to converge to a cat. There are no correct answers as long as they look good to you.

Perceptual quality
An image can still look good even if it hasn’t converged. Let’s look at how quickly each sampler can produce a high-quality image.

You will see perceptual quality measured with BRISQUE (Blind/Referenceless Image Spatial Quality Evaluator). It measures the quality of natural images.

DDIM is doing surprisingly well here, capable of producing the highest quality image within the group in as few as 8 steps.

### So… which one is the best?

Here are my recommendations:

1. If you want to use something fast, converging, new, and with decent quality, excellent choices are

* DPM++ 2M Karras with 20 – 30 steps
* UniPC with 20-30 steps.

2. If you want good quality images and don’t care about convergence, good choices are

* DPM++ SDE Karras with 10-15 steps (Note: This is a slower sampler)
* DDIM with 10-15 steps.

3. Avoid using any ancestral samplers if you prefer stable, reproducible images.

4. Euler and Heun are fine choices if you prefer something simple. Reduce the number of steps for Heun to save time.


Built with [Mintlify](https://mintlify.com).