# Source: https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Everything You Should Know About HyperDisplay

# Everything You Should Know About HyperDisplay

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/92955b303c984cbfe9a72102a670afc7?d=retro&s=20&r=pg) Liquid Soulder]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft863&name=Everything+You+Should+Know+About+HyperDisplay "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft863 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Everything+You+Should+Know+About+HyperDisplay&url=http%3A%2F%2Fsfe.io%2Ft863&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft863&t=Everything+You+Should+Know+About+HyperDisplay "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft863&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F6%2F3%2FTitle2.JPG&description=Everything+You+Should+Know+About+HyperDisplay "Pin It")

## Introduction

Nobody wants to reinvent the wheel, right? Well that\'s just what it felt like we were doing every time we wrote another (slightly different) graphics library for new products like the RGB OLED Breakout and ePaper displays. Not to mention that having to use specific code for each product makes it very hard to start using a new display in a project. Our HyperDisplay library is designed to put an end to all that - making it easy to add support for and use new displays!

The goal of this tutorial is to get you up-to-speed on how to use HyperDisplay, from the basics all the way to being able to extend the library. Stick around to learn all about how to use this easy, powerful, and flexible new tool!

The subjects that we cover in various sections will progress from fundamental all the way to the most advanced use of the library. Feel free to read the parts you need and skim the rest - you can always come back for more.

### Tutorial Sections

- [What is HyperDisplay](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/what-is-hyperdisplay): This is the foundation of knowledge and a roadmap to further exploration
- [Installing HyperDisplay](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/installing-hyperdisplay): What you need to know to start using the library
- [Basic Drawing Functions](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/basic-drawing-functions): A simple reference for when you just need something working
- [Advanced Drawing Functions](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/advanced-drawing-functions): See HyperDisplay\'s full drawing capability with a complete reference for drawing functions
- [Using Windows](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/using-windows): Quickly rearrange groups of elements
- [Buffering](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/buffering): Store drawings in memory and use \'show()\' to unleash them all at once
- [Derive Custom Driver](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/derive-custom-driver): Templates for use in extending support for displays

![Mandelbrot Set Fractal Shown with HyperDisplay](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/3/Title2.JPG "Mandelbrot Set Fractal Shown with HyperDisplay")

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft863&name=Everything+You+Should+Know+About+HyperDisplay "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft863 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Everything+You+Should+Know+About+HyperDisplay&url=http%3A%2F%2Fsfe.io%2Ft863&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft863&t=Everything+You+Should+Know+About+HyperDisplay "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft863&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F6%2F3%2FTitle2.JPG&description=Everything+You+Should+Know+About+HyperDisplay "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/all) [Next Page →\
[What is HyperDisplay?]](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/what-is-hyperdisplay)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/introduction) [What is HyperDisplay?](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/what-is-hyperdisplay) [Installing HyperDisplay](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/installing-hyperdisplay) [Basic Drawing Functions](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/basic-drawing-functions) [Advanced Drawing Functions](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/advanced-drawing-functions) [Using Windows](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/using-windows) [Buffering](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/buffering) [Derive Custom Driver](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/derive-custom-driver) [Resources and Going Further](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/resources-and-going-further)

[Comments [16]](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/discuss) [Single Page](https://learn.sparkfun.com/tutorials/everything-you-should-know-about-hyperdisplay/all) [Print]

- **Tags**
- - [Arduino](https://learn.sparkfun.com/tutorials/tags/arduino)
  - [Displays](https://learn.sparkfun.com/tutorials/tags/displays)
  - [Programming](https://learn.sparkfun.com/tutorials/tags/programming)
  - [Technology](https://learn.sparkfun.com/tutorials/tags/technology)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]