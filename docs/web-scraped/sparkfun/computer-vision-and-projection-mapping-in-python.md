# Source: https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Computer Vision and Projection Mapping in Python

# Computer Vision and Projection Mapping in Python

[≡ Pages](#)

Contributors: [ Member #914806]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft862&name=Computer+Vision+and+Projection+Mapping+in+Python "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft862 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Computer+Vision+and+Projection+Mapping+in+Python&url=http%3A%2F%2Fsfe.io%2Ft862&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft862&t=Computer+Vision+and+Projection+Mapping+in+Python "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft862&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F6%2F2%2F2019-01-30_02-11-11-0700.jpg&description=Computer+Vision+and+Projection+Mapping+in+Python "Pin It")

## Introduction

Let\'s face it - [Python](https://www.sparkfun.com/python) is pretty awesome, and what better way to make use of that awesomeness than to incorporate it into your projects? Here we\'re looking at some of the methods and libraries involved with projecting images using computer vision and Python. Since I'm finishing this tutorial around the holidays, it seems appropriate to create a Santa hat projector! Hopefully once you\'ve completed the tutorial, you\'ll be able to substitute in whatever item you want for your own uses. To establish an acceptance criteria, I'll consider this project finished when someone can walk in front of the projector and have the computer track them, projecting a Santa hat on their head.

[![Cameron and his Santa Hat](https://cdn.sparkfun.com/r/600-600/assets/learn_tutorials/8/6/2/IMG_1196.jpg)](https://cdn.sparkfun.com/assets/learn_tutorials/8/6/2/IMG_1196.jpg)

### Required Materials

To follow along with this tutorial, you will need the following materials. You may not need everything, depending on what you already have. Add it to your cart, read through the guide, and adjust the cart as necessary.

In addition you\'ll need:

- projector

### Suggested Reading

[](https://learn.sparkfun.com/tutorials/raspberry-pi-3-starter-kit-hookup-guide)

### Raspberry Pi 3 Starter Kit Hookup Guide 

Guide for getting going with the Raspberry Pi 3 Model B and Raspberry Pi 3 Model B+ starter kit.

[](https://learn.sparkfun.com/tutorials/python-programming-tutorial-getting-started-with-the-raspberry-pi)

### Python Programming Tutorial: Getting Started with the Raspberry Pi 

This guide will show you how to write programs on your Raspberry Pi using Python to control hardware.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft862&name=Computer+Vision+and+Projection+Mapping+in+Python "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft862 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Computer+Vision+and+Projection+Mapping+in+Python&url=http%3A%2F%2Fsfe.io%2Ft862&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft862&t=Computer+Vision+and+Projection+Mapping+in+Python "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft862&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F8%2F6%2F2%2F2019-01-30_02-11-11-0700.jpg&description=Computer+Vision+and+Projection+Mapping+in+Python "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/all) [Next Page →\
[Set Up a Raspberry Pi]](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/set-up-a-raspberry-pi)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/introduction) [Set Up a Raspberry Pi](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/set-up-a-raspberry-pi) [Install the Project Dependencies](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/install-the-project-dependencies) [Calibrate the Camera](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/calibrate-the-camera) [Find the Project-able Area](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/find-the-project-able-area) [Correct for Off Axis Viewing](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/correct-for-off-axis-viewing) [Identify and Track Faces](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/identify-and-track-faces) [Map Between What the Camera Sees and What the Projector Projects](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/map-between-what-the-camera-sees-and-what-the-projector-projects) [Put a Hat On It](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/put-a-hat-on-it) [Resources and Going Further](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/resources-and-going-further)

[Comments [0]](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/discuss) [Single Page](https://learn.sparkfun.com/tutorials/computer-vision-and-projection-mapping-in-python/all) [Print]

- **Tags**
- - [Projects](https://learn.sparkfun.com/tutorials/tags/projects)
  - [Python](https://learn.sparkfun.com/tutorials/tags/python)
  - [Raspberry Pi](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)
  - [Single Board Computer](https://learn.sparkfun.com/tutorials/tags/single-board-computer)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]