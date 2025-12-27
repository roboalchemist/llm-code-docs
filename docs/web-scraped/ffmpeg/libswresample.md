# Source: https://ffmpeg.org/libswresample.html

-   [![FFmpeg](img/ffmpeg3d_white_20.png) FFmpeg](.)
-   [About](about.html)
-   [News](index.html#news)
-   [Download](download.html)
-   [Documentation](documentation.html)
-   [Community](community.html)
    -   [Code of Conduct](community.html#CodeOfConduct)
    -   [Mailing Lists](contact.html#MailingLists)
    -   [IRC](contact.html#IRCChannels)
    -   [Forums](contact.html#Forums)
    -   [Bug Reports](bugreports.html)
    -   [Wiki](https://trac.ffmpeg.org)
    -   [Conferences](https://trac.ffmpeg.org/wiki/Conferences)
-   [Developers](developer.html)
    -   [Source Code](download.html#get-sources)
    -   [Contribute](developer.html#Introduction)
    -   [FATE](http://fate.ffmpeg.org)
    -   [Code Coverage](http://coverage.ffmpeg.org)
    -   [Funding through SPI](spi.html)
-   [More](#)
    -   [Donate[]](donations.html)
    -   [Hire Developers](consulting.html)
    -   [Contact](contact.html)
    -   [Security](security.html)
    -   [Legal](legal.html)

# [](#) Libswresample Documentation

[] []

## Table of Contents 

-   [1 Description](#Description)
-   [2 See Also](#See-Also)
-   [3 Authors](#Authors)

[]

## [1 Description](#toc-Description) 

The libswresample library performs highly optimized audio resampling, rematrixing and sample format conversion operations.

Specifically, this library performs the following conversions:

-   *Resampling*: is the process of changing the audio rate, for example from a high sample rate of 44100Hz to 8000Hz. Audio conversion from high to low sample rate is a lossy process. Several resampling options and algorithms are available.
-   *Format conversion*: is the process of converting the type of samples, for example from 16-bit signed samples to unsigned 8-bit or float samples. It also handles packing conversion, when passing from packed layout (all samples belonging to distinct channels interleaved in the same buffer), to planar layout (all samples belonging to the same channel stored in a dedicated buffer or \"plane\").
-   *Rematrixing*: is the process of changing the channel layout, for example from stereo to mono. When the input channels cannot be mapped to the output streams, the process is lossy, since it involves different gain factors and mixing.

Various other audio conversions (e.g. stretching and padding) are enabled through dedicated options.

[]

## [2 See Also](#toc-See-Also) 

[ffmpeg](ffmpeg.html), [ffplay](ffplay.html), [ffprobe](ffprobe.html), [ffmpeg-resampler](ffmpeg-resampler.html), [libavutil](libavutil.html)

[]

## [3 Authors](#toc-Authors) 

The FFmpeg developers.

For details about the authorship, see the Git history of the project (https://git.ffmpeg.org/ffmpeg), e.g. by typing the command `git log` in the FFmpeg source directory, or browsing the online repository at <https://git.ffmpeg.org/ffmpeg>.

Maintainers for the specific components are listed in the file `MAINTAINERS` in the source code tree.

This document was generated on *December 27, 2025* using [*makeinfo*](http://www.gnu.org/software/texinfo/).

[Hosting provided by [telepoint.bg](https://telepoint.bg)]