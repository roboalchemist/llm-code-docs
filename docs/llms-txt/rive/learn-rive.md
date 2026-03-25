# Source: https://uat.rive.app/docs/tutorials/learn-rive.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://uat.rive.app/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Learn Rive

export const YouTube = ({id, timestamp}) => {
  const videoSrc = timestamp ? `https://www.youtube.com/embed/${id}?start=${timestamp}` : `https://www.youtube.com/embed/${id}`;
  return <iframe width="100%" height="400" src={videoSrc} title="YouTube video player" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerPolicy="strict-origin-when-cross-origin" allowFullScreen />;
};

## Rive for ABSOLUTE BEGINNERS

<YouTube id="7m4dwz8SCKo" />

## Rive 101

<YouTube id="videoseries?list=PLujDTZWVDSsFGonP9kzAnvryowW098-p3" />

## Community

<CardGroup>
  <Card title="School of Motion" href="https://www.schoolofmotion.com/courses/rive-academy-volume-1">
    **Rive Academy: Volume 1**

    Rive Academy: Volume 1 is the ultimate introduction to the world of interactive animation built with Rive. You’ll learn how to design, animate, and prototype interactive motion design that you can ship anywhere. By the end of the course you’ll be ready to use Rive in production, and go further in more advanced courses.
  </Card>

  <Card title="Motion Design School" href="https://motiondesign.school/courses/rive-interactive-motion/">
    **Rive: Interactive Motion**

    Discover the web-based software revolutionizing interactive experiences. Build 2 big faux 3d spaces filled with awesome interactive setups. Learn on practise all Rive techniques and use it in full power.
  </Card>
</CardGroup>
