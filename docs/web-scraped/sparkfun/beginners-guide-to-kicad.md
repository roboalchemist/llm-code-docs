# Source: https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad

- [Home](https://learn.sparkfun.com/)
- [Tutorials](https://learn.sparkfun.com/tutorials)
- Beginner\'s Guide to KiCad

# Beginner\'s Guide to KiCad

[≡ Pages](#)

Contributors: [![](https://cdn.sparkfun.com/avatar/1ff6ad39b8c242a14296a76845e116cd?d=retro&s=20&r=pg) Nate]

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft660&name=Beginner%27s+Guide+to+KiCad "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft660 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Beginner%27s+Guide+to+KiCad&url=http%3A%2F%2Fsfe.io%2Ft660&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft660&t=Beginner%27s+Guide+to+KiCad "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft660&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F6%2F0%2Fkicad_logo_pathsTutorialTile.png&description=Beginner%27s+Guide+to+KiCad "Pin It")

## Introduction

If you\'re like me and you\'ve decided to take the plunge from EAGLE PCB to KiCad it can be really jarring. EAGLE had many quirks and rough edges that I\'m sure I cursed when I first learned it back in 2005. Since then EAGLE has become a second language to me and I\'ve forgotten all the hard bits. So as you migrate to KiCad remember to take breaks and breathe (and say \'Key-CAD\' in your head). You\'ll be dreaming in KiCad in no time!

[![KiCad Logo](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/0/kicad_logo_paths1.png)](https://cdn.sparkfun.com/assets/learn_tutorials/6/6/0/kicad_logo_paths1.png)

This tutorial will walk you through a KiCad example project from schematic capture to PCB layout. We\'ll also touch on library linking, editing, and creation. We\'ll also export our PCB to gerbers so the board can be fabricated.

While this tutorial is aimed at beginners I am going to use terms such as \'schematic components\' and \'polygon pours\'. If something doesn\'t make sense that\'s ok, just take a moment to do a [quick search](http://lmgtfy.com/?q=what%27s+a+polygon+pour). If you really get stuck please use the comments section on the right. We always want to improve our tutorials to make them easier.

[[ [] Share ]](#)

Use this URL to share:\

[[Share on Tumblr]](https://www.tumblr.com/share/link?url=http%3A%2F%2Fsfe.io%2Ft660&name=Beginner%27s+Guide+to+KiCad "Share on Tumblr") [[Submit to reddi]](https://www.reddit.com/submit?url=http%3A%2F%2Fsfe.io%2Ft660 "Submit to reddit")

[[Share on Twitter]](https://twitter.com/intent/tweet?text=Beginner%27s+Guide+to+KiCad&url=http%3A%2F%2Fsfe.io%2Ft660&via=sparkfun "Share on Twitter") [[Share on Facebook]](http://www.facebook.com/sharer.php?u=http%3A%2F%2Fsfe.io%2Ft660&t=Beginner%27s+Guide+to+KiCad "Share on Facebook") [[Pin It]](https://www.pinterest.com/pin/create/button/?url=http%3A%2F%2Fsfe.io%2Ft660&media=https%3A%2F%2Fcdn.sparkfun.com%2F%2Fr%2F500-1000%2Fassets%2Flearn_tutorials%2F6%2F6%2F0%2Fkicad_logo_pathsTutorialTile.png&description=Beginner%27s+Guide+to+KiCad "Pin It")

------------------------------------------------------------------------

[View as a single page](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/all) [Next Page →\
[KiCad Project Window]](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/kicad-project-window)

← Previous Page

[**Pages**] [Introduction](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/introduction) [KiCad Project Window](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/kicad-project-window) [Setting Up Schematic Component Libraries](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/setting-up-schematic-component-libraries) [Editing a Schematic](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/editing-a-schematic) [Editing a PCB Layout](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/editing-a-pcb-layout) [Running Design Rule Check](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/running-design-rule-check) [Exporting Gerbers](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/exporting-gerbers) [Creating a Custom KiCad Footprint Library](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/creating-a-custom-kicad-footprint-library) [Creating Custom KiCad Schematic Components](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/creating-custom-kicad-schematic-components) [Resources and Going Further](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/resources-and-going-further)

[Comments [22]](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/discuss) [Single Page](https://learn.sparkfun.com/tutorials/beginners-guide-to-kicad/all) [Print]

- **Tags**
- - [Skill](https://learn.sparkfun.com/tutorials/tags/skill)

<!-- -->

- **License**
- [ [Creative Commons] ] [tutorials are [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)]