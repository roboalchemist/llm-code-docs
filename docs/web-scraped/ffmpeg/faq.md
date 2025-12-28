# Source: https://ffmpeg.org/faq.html

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

# [](#) FFmpeg FAQ

[] []

## Table of Contents 

-   [1 General Questions](#General-Questions)
    -   [1.1 Why doesn't FFmpeg support feature \[xyz\]?](#Why-doesn_0027t-FFmpeg-support-feature-_005bxyz_005d_003f)
    -   [1.2 FFmpeg does not support codec XXX. Can you include a Windows DLL loader to support it?](#FFmpeg-does-not-support-codec-XXX_002e-Can-you-include-a-Windows-DLL-loader-to-support-it_003f)
    -   [1.3 I cannot read this file although this format seems to be supported by ffmpeg.](#I-cannot-read-this-file-although-this-format-seems-to-be-supported-by-ffmpeg_002e)
    -   [1.4 Which codecs are supported by Windows?](#Which-codecs-are-supported-by-Windows_003f)
-   [2 Compilation](#Compilation)
    -   [2.1 `error: can't find a register in class 'GENERAL_REGS' while reloading 'asm'`](#error_003a-can_0027t-find-a-register-in-class-_0027GENERAL_005fREGS_0027-while-reloading-_0027asm_0027)
    -   [2.2 I have installed this library with my distro's package manager. Why does `configure` not see it?](#I-have-installed-this-library-with-my-distro_0027s-package-manager_002e-Why-does-configure-not-see-it_003f)
    -   [2.3 How do I make `pkg-config` find my libraries?](#How-do-I-make-pkg_002dconfig-find-my-libraries_003f)
    -   [2.4 How do I use `pkg-config` when cross-compiling?](#How-do-I-use-pkg_002dconfig-when-cross_002dcompiling_003f)
-   [3 Usage](#Usage)
    -   [3.1 ffmpeg does not work; what is wrong?](#ffmpeg-does-not-work_003b-what-is-wrong_003f)
    -   [3.2 How do I encode single pictures into movies?](#How-do-I-encode-single-pictures-into-movies_003f)
    -   [3.3 How do I encode movie to single pictures?](#How-do-I-encode-movie-to-single-pictures_003f)
    -   [3.4 Why do I see a slight quality degradation with multithreaded MPEG\* encoding?](#Why-do-I-see-a-slight-quality-degradation-with-multithreaded-MPEG_002a-encoding_003f)
    -   [3.5 How can I read from the standard input or write to the standard output?](#How-can-I-read-from-the-standard-input-or-write-to-the-standard-output_003f)
    -   [3.6 -f jpeg doesn't work.](#g_t_002df-jpeg-doesn_0027t-work_002e)
    -   [3.7 Why can I not change the frame rate?](#Why-can-I-not-change-the-frame-rate_003f)
    -   [3.8 How do I encode Xvid or DivX video with ffmpeg?](#How-do-I-encode-Xvid-or-DivX-video-with-ffmpeg_003f)
    -   [3.9 Which are good parameters for encoding high quality MPEG-4?](#Which-are-good-parameters-for-encoding-high-quality-MPEG_002d4_003f)
    -   [3.10 Which are good parameters for encoding high quality MPEG-1/MPEG-2?](#Which-are-good-parameters-for-encoding-high-quality-MPEG_002d1_002fMPEG_002d2_003f)
    -   [3.11 Interlaced video looks very bad when encoded with ffmpeg, what is wrong?](#Interlaced-video-looks-very-bad-when-encoded-with-ffmpeg_002c-what-is-wrong_003f)
    -   [3.12 How can I read DirectShow files?](#How-can-I-read-DirectShow-files_003f)
    -   [3.13 How can I join video files?](#How-can-I-join-video-files_003f)
    -   [3.14 How can I concatenate video files?](#How-can-I-concatenate-video-files_003f)
        -   [3.14.1 Concatenating using the concat *filter*](#Concatenating-using-the-concat-filter)
        -   [3.14.2 Concatenating using the concat *demuxer*](#Concatenating-using-the-concat-demuxer)
        -   [3.14.3 Concatenating using the concat *protocol* (file level)](#Concatenating-using-the-concat-protocol-_0028file-level_0029)
        -   [3.14.4 Concatenating using raw audio and video](#Concatenating-using-raw-audio-and-video)
    -   [3.15 Using `-f lavfi`, audio becomes mono for no apparent reason.](#Using-_002df-lavfi_002c-audio-becomes-mono-for-no-apparent-reason_002e)
    -   [3.16 Why does FFmpeg not see the subtitles in my VOB file?](#Why-does-FFmpeg-not-see-the-subtitles-in-my-VOB-file_003f)
    -   [3.17 Why was the `ffmpeg` `-sameq` option removed? What to use instead?](#Why-was-the-ffmpeg-_002dsameq-option-removed_003f-What-to-use-instead_003f)
    -   [3.18 I have a stretched video, why does scaling not fix it?](#I-have-a-stretched-video_002c-why-does-scaling-not-fix-it_003f)
    -   [3.19 How do I run ffmpeg as a background task?](#How-do-I-run-ffmpeg-as-a-background-task_003f)
    -   [3.20 How do I prevent ffmpeg from suspending with a message like *suspended (tty output)*?](#How-do-I-prevent-ffmpeg-from-suspending-with-a-message-like-suspended-_0028tty-output_0029_003f)
-   [4 Development](#Development)
    -   [4.1 Are there examples illustrating how to use the FFmpeg libraries, particularly libavcodec and libavformat?](#Are-there-examples-illustrating-how-to-use-the-FFmpeg-libraries_002c-particularly-libavcodec-and-libavformat_003f)
    -   [4.2 Can you support my C compiler XXX?](#Can-you-support-my-C-compiler-XXX_003f)
    -   [4.3 Is Microsoft Visual C++ supported?](#Is-Microsoft-Visual-C_002b_002b-supported_003f)
    -   [4.4 Can you add automake, libtool or autoconf support?](#Can-you-add-automake_002c-libtool-or-autoconf-support_003f)
    -   [4.5 Why not rewrite FFmpeg in object-oriented C++?](#Why-not-rewrite-FFmpeg-in-object_002doriented-C_002b_002b_003f)
    -   [4.6 Why are the ffmpeg programs devoid of debugging symbols?](#Why-are-the-ffmpeg-programs-devoid-of-debugging-symbols_003f)
    -   [4.7 I do not like the LGPL, can I contribute code under the GPL instead?](#I-do-not-like-the-LGPL_002c-can-I-contribute-code-under-the-GPL-instead_003f)
    -   [4.8 I'm using FFmpeg from within my C application but the linker complains about missing symbols from the libraries themselves.](#I_0027m-using-FFmpeg-from-within-my-C-application-but-the-linker-complains-about-missing-symbols-from-the-libraries-themselves_002e)
    -   [4.9 I'm using FFmpeg from within my C++ application but the linker complains about missing symbols which seem to be available.](#I_0027m-using-FFmpeg-from-within-my-C_002b_002b-application-but-the-linker-complains-about-missing-symbols-which-seem-to-be-available_002e)
    -   [4.10 I'm using libavutil from within my C++ application but the compiler complains about 'UINT64_C' was not declared in this scope](#I_0027m-using-libavutil-from-within-my-C_002b_002b-application-but-the-compiler-complains-about-_0027UINT64_005fC_0027-was-not-declared-in-this-scope)
    -   [4.11 I have a file in memory / a API different from \*open/\*read/ libc how do I use it with libavformat?](#I-have-a-file-in-memory-_002f-a-API-different-from-_002aopen_002f_002aread_002f-libc-how-do-I-use-it-with-libavformat_003f)
    -   [4.12 Where is the documentation about ffv1, msmpeg4, asv1, 4xm?](#Where-is-the-documentation-about-ffv1_002c-msmpeg4_002c-asv1_002c-4xm_003f)
    -   [4.13 How do I feed H.263-RTP (and other codecs in RTP) to libavcodec?](#How-do-I-feed-H_002e263_002dRTP-_0028and-other-codecs-in-RTP_0029-to-libavcodec_003f)
    -   [4.14 AVStream.r_frame_rate is wrong, it is much larger than the frame rate.](#AVStream_002er_005fframe_005frate-is-wrong_002c-it-is-much-larger-than-the-frame-rate_002e)
    -   [4.15 Why is `make fate` not running all tests?](#Why-is-make-fate-not-running-all-tests_003f)
    -   [4.16 Why is `make fate` not finding the samples?](#Why-is-make-fate-not-finding-the-samples_003f)

[]

## [1 General Questions](#toc-General-Questions) 

[]

### [1.1 Why doesn't FFmpeg support feature \[xyz\]?](#toc-Why-doesn_0027t-FFmpeg-support-feature-_005bxyz_005d_003f) 

Because no one has taken on that task yet. FFmpeg development is driven by the tasks that are important to the individual developers. If there is a feature that is important to you, the best way to get it implemented is to undertake the task yourself or sponsor a developer.

[]

### [1.2 FFmpeg does not support codec XXX. Can you include a Windows DLL loader to support it?](#toc-FFmpeg-does-not-support-codec-XXX_002e-Can-you-include-a-Windows-DLL-loader-to-support-it_003f) 

No. Windows DLLs are not portable, bloated and often slow. Moreover FFmpeg strives to support all codecs natively. A DLL loader is not conducive to that goal.

[]

### [1.3 I cannot read this file although this format seems to be supported by ffmpeg.](#toc-I-cannot-read-this-file-although-this-format-seems-to-be-supported-by-ffmpeg_002e) 

Even if ffmpeg can read the container format, it may not support all its codecs. Please consult the supported codec list in the ffmpeg documentation.

[]

### [1.4 Which codecs are supported by Windows?](#toc-Which-codecs-are-supported-by-Windows_003f) 

Windows does not support standard formats like MPEG very well, unless you install some additional codecs.

The following list of video codecs should work on most Windows systems:

`msmpeg4v2`

:   .avi/.asf

`msmpeg4`

:   .asf only

`wmv1`

:   .asf only

`wmv2`

:   .asf only

`mpeg4`

:   Only if you have some MPEG-4 codec like ffdshow or Xvid installed.

`mpeg1video`

:   .mpg only

Note, ASF files often have .wmv or .wma extensions in Windows. It should also be mentioned that Microsoft claims a patent on the ASF format, and may sue or threaten users who create ASF files with non-Microsoft software. It is strongly advised to avoid ASF where possible.

The following list of audio codecs should work on most Windows systems:

`adpcm_ima_wav`\
`adpcm_ms`\
`pcm_s16le`

:   always

`libmp3lame`

:   If some MP3 codec like LAME is installed.

[]

## [2 Compilation](#toc-Compilation) 

[]

### [2.1 `error: can't find a register in class 'GENERAL_REGS' while reloading 'asm'`](#toc-error_003a-can_0027t-find-a-register-in-class-_0027GENERAL_005fREGS_0027-while-reloading-_0027asm_0027) 

This is a bug in gcc. Do not report it to us. Instead, please report it to the gcc developers. Note that we will not add workarounds for gcc bugs.

Also note that (some of) the gcc developers believe this is not a bug or not a bug they should fix: <https://gcc.gnu.org/bugzilla/show_bug.cgi?id=11203>. Then again, some of them do not know the difference between an undecidable problem and an NP-hard problem\...

[]

### [2.2 I have installed this library with my distro's package manager. Why does `configure` not see it?](#toc-I-have-installed-this-library-with-my-distro_0027s-package-manager_002e-Why-does-configure-not-see-it_003f) 

Distributions usually split libraries in several packages. The main package contains the files necessary to run programs using the library. The development package contains the files necessary to build programs using the library. Sometimes, docs and/or data are in a separate package too.

To build FFmpeg, you need to install the development package. It is usually called `libfoo-dev` or `libfoo-devel`. You can remove it after the build is finished, but be sure to keep the main package.

[]

### [2.3 How do I make `pkg-config` find my libraries?](#toc-How-do-I-make-pkg_002dconfig-find-my-libraries_003f) 

Somewhere along with your libraries, there is a `.pc` file (or several) in a `pkgconfig` directory. You need to set environment variables to point `pkg-config` to these files.

If you need to *add* directories to `pkg-config`'s search list (typical use case: library installed separately), add it to `$PKG_CONFIG_PATH`:

``` example
export PKG_CONFIG_PATH=/opt/x264/lib/pkgconfig:/opt/opus/lib/pkgconfig
```

If you need to *replace* `pkg-config`'s search list (typical use case: cross-compiling), set it in `$PKG_CONFIG_LIBDIR`:

``` example
export PKG_CONFIG_LIBDIR=/home/me/cross/usr/lib/pkgconfig:/home/me/cross/usr/local/lib/pkgconfig
```

If you need to know the library's internal dependencies (typical use: static linking), add the `--static` option to `pkg-config`:

``` example
./configure --pkg-config-flags=--static
```

[]

### [2.4 How do I use `pkg-config` when cross-compiling?](#toc-How-do-I-use-pkg_002dconfig-when-cross_002dcompiling_003f) 

The best way is to install `pkg-config` in your cross-compilation environment. It will automatically use the cross-compilation libraries.

You can also use `pkg-config` from the host environment by specifying explicitly `--pkg-config=pkg-config` to `configure`. In that case, you must point `pkg-config` to the correct directories using the `PKG_CONFIG_LIBDIR`, as explained in the previous entry.

As an intermediate solution, you can place in your cross-compilation environment a script that calls the host `pkg-config` with `PKG_CONFIG_LIBDIR` set. That script can look like that:

``` example
#!/bin/sh
PKG_CONFIG_LIBDIR=/path/to/cross/lib/pkgconfig
export PKG_CONFIG_LIBDIR
exec /usr/bin/pkg-config "$@"
```

[]

## [3 Usage](#toc-Usage) 

[]

### [3.1 ffmpeg does not work; what is wrong?](#toc-ffmpeg-does-not-work_003b-what-is-wrong_003f) 

Try a `make distclean` in the ffmpeg source directory before the build. If this does not help see (<https://ffmpeg.org/bugreports.html>).

[]

### [3.2 How do I encode single pictures into movies?](#toc-How-do-I-encode-single-pictures-into-movies_003f) 

First, rename your pictures to follow a numerical sequence. For example, img1.jpg, img2.jpg, img3.jpg,\... Then you may run:

``` example
ffmpeg -f image2 -i img%d.jpg /tmp/a.mpg
```

Notice that '`%d`' is replaced by the image number.

`img%03d.jpg` means the sequence `img001.jpg`, `img002.jpg`, etc.

Use the `-start_number` option to declare a starting number for the sequence. This is useful if your sequence does not start with `img001.jpg` but is still in a numerical order. The following example will start with `img100.jpg`:

``` example
ffmpeg -f image2 -start_number 100 -i img%d.jpg /tmp/a.mpg
```

If you have large number of pictures to rename, you can use the following command to ease the burden. The command, using the bourne shell syntax, symbolically links all files in the current directory that match `*jpg` to the `/tmp` directory in the sequence of `img001.jpg`, `img002.jpg` and so on.

``` example
x=1; for i in *jpg; do counter=$(printf %03d $x); ln -s "$i" /tmp/img"$counter".jpg; x=$(($x+1)); done
```

If you want to sequence them by oldest modified first, substitute `$(ls -r -t *jpg)` in place of `*jpg`.

Then run:

``` example
ffmpeg -f image2 -i /tmp/img%03d.jpg /tmp/a.mpg
```

The same logic is used for any image format that ffmpeg reads.

You can also use `cat` to pipe images to ffmpeg:

``` example
cat *.jpg | ffmpeg -f image2pipe -c:v mjpeg -i - output.mpg
```

[]

### [3.3 How do I encode movie to single pictures?](#toc-How-do-I-encode-movie-to-single-pictures_003f) 

Use:

``` example
ffmpeg -i movie.mpg movie%d.jpg
```

The `movie.mpg` used as input will be converted to `movie1.jpg`, `movie2.jpg`, etc\...

Instead of relying on file format self-recognition, you may also use

`-c:v ppm`

`-c:v png`

`-c:v mjpeg`

to force the encoding.

Applying that to the previous example:

``` example
ffmpeg -i movie.mpg -f image2 -c:v mjpeg menu%d.jpg
```

Beware that there is no \"jpeg\" codec. Use \"mjpeg\" instead.

[]

### [3.4 Why do I see a slight quality degradation with multithreaded MPEG\* encoding?](#toc-Why-do-I-see-a-slight-quality-degradation-with-multithreaded-MPEG_002a-encoding_003f) 

For multithreaded MPEG\* encoding, the encoded slices must be independent, otherwise thread n would practically have to wait for n-1 to finish, so it's quite logical that there is a small reduction of quality. This is not a bug.

[]

### [3.5 How can I read from the standard input or write to the standard output?](#toc-How-can-I-read-from-the-standard-input-or-write-to-the-standard-output_003f) 

Use `-` as file name.

[]

### [3.6 -f jpeg doesn't work.](#toc-_002df-jpeg-doesn_0027t-work_002e) 

Try '-f image2 test%d.jpg'.

[]

### [3.7 Why can I not change the frame rate?](#toc-Why-can-I-not-change-the-frame-rate_003f) 

Some codecs, like MPEG-1/2, only allow a small number of fixed frame rates. Choose a different codec with the -c:v command line option.

[]

### [3.8 How do I encode Xvid or DivX video with ffmpeg?](#toc-How-do-I-encode-Xvid-or-DivX-video-with-ffmpeg_003f) 

Both Xvid and DivX (version 4+) are implementations of the ISO MPEG-4 standard (note that there are many other coding formats that use this same standard). Thus, use '-c:v mpeg4' to encode in these formats. The default fourcc stored in an MPEG-4-coded file will be 'FMP4'. If you want a different fourcc, use the '-vtag' option. E.g., '-vtag xvid' will force the fourcc 'xvid' to be stored as the video fourcc rather than the default.

[]

### [3.9 Which are good parameters for encoding high quality MPEG-4?](#toc-Which-are-good-parameters-for-encoding-high-quality-MPEG_002d4_003f) 

'-mbd rd -flags +mv4+aic -trellis 2 -cmp 2 -subcmp 2 -g 300 -pass 1/2', things to try: '-bf 2', '-mpv_flags qp_rd', '-mpv_flags mv0', '-mpv_flags skip_rd'.

[]

### [3.10 Which are good parameters for encoding high quality MPEG-1/MPEG-2?](#toc-Which-are-good-parameters-for-encoding-high-quality-MPEG_002d1_002fMPEG_002d2_003f) 

'-mbd rd -trellis 2 -cmp 2 -subcmp 2 -g 100 -pass 1/2' but beware the '-g 100' might cause problems with some decoders. Things to try: '-bf 2', '-mpv_flags qp_rd', '-mpv_flags mv0', '-mpv_flags skip_rd'.

[]

### [3.11 Interlaced video looks very bad when encoded with ffmpeg, what is wrong?](#toc-Interlaced-video-looks-very-bad-when-encoded-with-ffmpeg_002c-what-is-wrong_003f) 

You should use '-flags +ilme+ildct' and maybe '-flags +alt' for interlaced material, and try '-top 0/1' if the result looks really messed-up.

[]

### [3.12 How can I read DirectShow files?](#toc-How-can-I-read-DirectShow-files_003f) 

If you have built FFmpeg with `./configure --enable-avisynth` (only possible on MinGW/Cygwin platforms), then you may use any file that DirectShow can read as input.

Just create an \"input.avs\" text file with this single line \...

``` example
DirectShowSource("C:\path to your file\yourfile.asf")
```

\... and then feed that text file to ffmpeg:

``` example
ffmpeg -i input.avs
```

For ANY other help on AviSynth, please visit the [AviSynth homepage](http://www.avisynth.org/).

[]

### [3.13 How can I join video files?](#toc-How-can-I-join-video-files_003f) 

To \"join\" video files is quite ambiguous. The following list explains the different kinds of \"joining\" and points out how those are addressed in FFmpeg. To join video files may mean:

-   To put them one after the other: this is called to *concatenate* them (in short: concat) and is addressed [in this very faq](#How-can-I-concatenate-video-files).
-   To put them together in the same file, to let the user choose between the different versions (example: different audio languages): this is called to *multiplex* them together (in short: mux), and is done by simply invoking ffmpeg with several `-i` options.
-   For audio, to put all channels together in a single stream (example: two mono streams into one stereo stream): this is sometimes called to *merge* them, and can be done using the [`amerge`](ffmpeg-filters.html#amerge) filter.
-   For audio, to play one on top of the other: this is called to *mix* them, and can be done by first merging them into a single stream and then using the [`pan`](ffmpeg-filters.html#pan) filter to mix the channels at will.
-   For video, to display both together, side by side or one on top of a part of the other; it can be done using the [`overlay`](ffmpeg-filters.html#overlay) video filter.

[][]

### [3.14 How can I concatenate video files?](#toc-How-can-I-concatenate-video-files_003f) 

There are several solutions, depending on the exact circumstances.

[]

#### [3.14.1 Concatenating using the concat *filter*](#toc-Concatenating-using-the-concat-filter) 

FFmpeg has a [`concat`](ffmpeg-filters.html#concat) filter designed specifically for that, with examples in the documentation. This operation is recommended if you need to re-encode.

[]

#### [3.14.2 Concatenating using the concat *demuxer*](#toc-Concatenating-using-the-concat-demuxer) 

FFmpeg has a [`concat`](ffmpeg-formats.html#concat) demuxer which you can use when you want to avoid a re-encode and your format doesn't support file level concatenation.

[]

#### [3.14.3 Concatenating using the concat *protocol* (file level)](#toc-Concatenating-using-the-concat-protocol-_0028file-level_0029) 

FFmpeg has a [`concat`](ffmpeg-protocols.html#concat) protocol designed specifically for that, with examples in the documentation.

A few multimedia containers (MPEG-1, MPEG-2 PS, DV) allow one to concatenate video by merely concatenating the files containing them.

Hence you may concatenate your multimedia files by first transcoding them to these privileged formats, then using the humble `cat` command (or the equally humble `copy` under Windows), and finally transcoding back to your format of choice.

``` example
ffmpeg -i input1.avi -qscale:v 1 intermediate1.mpg
ffmpeg -i input2.avi -qscale:v 1 intermediate2.mpg
cat intermediate1.mpg intermediate2.mpg > intermediate_all.mpg
ffmpeg -i intermediate_all.mpg -qscale:v 2 output.avi
```

Additionally, you can use the `concat` protocol instead of `cat` or `copy` which will avoid creation of a potentially huge intermediate file.

``` example
ffmpeg -i input1.avi -qscale:v 1 intermediate1.mpg
ffmpeg -i input2.avi -qscale:v 1 intermediate2.mpg
ffmpeg -i concat:"intermediate1.mpg|intermediate2.mpg" -c copy intermediate_all.mpg
ffmpeg -i intermediate_all.mpg -qscale:v 2 output.avi
```

Note that you may need to escape the character \"\|\" which is special for many shells.

Another option is usage of named pipes, should your platform support it:

``` example
mkfifo intermediate1.mpg
mkfifo intermediate2.mpg
ffmpeg -i input1.avi -qscale:v 1 -y intermediate1.mpg < /dev/null &
ffmpeg -i input2.avi -qscale:v 1 -y intermediate2.mpg < /dev/null &
cat intermediate1.mpg intermediate2.mpg |\
ffmpeg -f mpeg -i - -c:v mpeg4 -c:a libmp3lame output.avi
```

[]

#### [3.14.4 Concatenating using raw audio and video](#toc-Concatenating-using-raw-audio-and-video) 

Similarly, the yuv4mpegpipe format, and the raw video, raw audio codecs also allow concatenation, and the transcoding step is almost lossless. When using multiple yuv4mpegpipe(s), the first line needs to be discarded from all but the first stream. This can be accomplished by piping through `tail` as seen below. Note that when piping through `tail` you must use command grouping, ``, to background properly.

For example, let's say we want to concatenate two FLV files into an output.flv file:

``` example
mkfifo temp1.a
mkfifo temp1.v
mkfifo temp2.a
mkfifo temp2.v
mkfifo all.a
mkfifo all.v
ffmpeg -i input1.flv -vn -f u16le -c:a pcm_s16le -ac 2 -ar 44100 - > temp1.a < /dev/null &
ffmpeg -i input2.flv -vn -f u16le -c:a pcm_s16le -ac 2 -ar 44100 - > temp2.a < /dev/null &
ffmpeg -i input1.flv -an -f yuv4mpegpipe - > temp1.v < /dev/null &
 &
cat temp1.a temp2.a > all.a &
cat temp1.v temp2.v > all.v &
ffmpeg -f u16le -c:a pcm_s16le -ac 2 -ar 44100 -i all.a \
       -f yuv4mpegpipe -i all.v \
       -y output.flv
rm temp[12].[av] all.[av]
```

[]

### [3.15 Using `-f lavfi`, audio becomes mono for no apparent reason.](#toc-Using-_002df-lavfi_002c-audio-becomes-mono-for-no-apparent-reason_002e) 

Use `-dumpgraph -` to find out exactly where the channel layout is lost.

Most likely, it is through `auto-inserted aresample`. Try to understand why the converting filter was needed at that place.

Just before the output is a likely place, as `-f lavfi` currently only support packed S16.

Then insert the correct `aformat` explicitly in the filtergraph, specifying the exact format.

``` example
aformat=sample_fmts=s16:channel_layouts=stereo
```

[]

### [3.16 Why does FFmpeg not see the subtitles in my VOB file?](#toc-Why-does-FFmpeg-not-see-the-subtitles-in-my-VOB-file_003f) 

VOB and a few other formats do not have a global header that describes everything present in the file. Instead, applications are supposed to scan the file to see what it contains. Since VOB files are frequently large, only the beginning is scanned. If the subtitles happen only later in the file, they will not be initially detected.

Some applications, including the `ffmpeg` command-line tool, can only work with streams that were detected during the initial scan; streams that are detected later are ignored.

The size of the initial scan is controlled by two options: `probesize` (default \~5 Mo) and `analyzeduration` (default 5,000,000 Âµs = 5 s). For the subtitle stream to be detected, both values must be large enough.

[]

### [3.17 Why was the `ffmpeg` `-sameq` option removed? What to use instead?](#toc-Why-was-the-ffmpeg-_002dsameq-option-removed_003f-What-to-use-instead_003f) 

The `-sameq` option meant \"same quantizer\", and made sense only in a very limited set of cases. Unfortunately, a lot of people mistook it for \"same quality\" and used it in places where it did not make sense: it had roughly the expected visible effect, but achieved it in a very inefficient way.

Each encoder has its own set of options to set the quality-vs-size balance, use the options for the encoder you are using to set the quality level to a point acceptable for your tastes. The most common options to do that are `-qscale` and `-qmax`, but you should peruse the documentation of the encoder you chose.

[]

### [3.18 I have a stretched video, why does scaling not fix it?](#toc-I-have-a-stretched-video_002c-why-does-scaling-not-fix-it_003f) 

A lot of video codecs and formats can store the *aspect ratio* of the video: this is the ratio between the width and the height of either the full image (DAR, display aspect ratio) or individual pixels (SAR, sample aspect ratio). For example, EGA screens at resolution 640Ã---350 had 4:3 DAR and 35:48 SAR.

Most still image processing work with square pixels, i.e. 1:1 SAR, but a lot of video standards, especially from the analogic-numeric transition era, use non-square pixels.

Most processing filters in FFmpeg handle the aspect ratio to avoid stretching the image: cropping adjusts the DAR to keep the SAR constant, scaling adjusts the SAR to keep the DAR constant.

If you want to stretch, or â€œunstretchâ€?, the image, you need to override the information with the [`setdar or setsar filters`](ffmpeg-filters.html#setdar_002c-setsar).

Do not forget to examine carefully the original video to check whether the stretching comes from the image or from the aspect ratio information.

For example, to fix a badly encoded EGA capture, use the following commands, either the first one to upscale to square pixels or the second one to set the correct aspect ratio or the third one to avoid transcoding (may not work depending on the format / codec / player / phase of the moon):

``` example
ffmpeg -i ega_screen.nut -vf scale=640:480,setsar=1 ega_screen_scaled.nut
ffmpeg -i ega_screen.nut -vf setdar=4/3 ega_screen_anamorphic.nut
ffmpeg -i ega_screen.nut -aspect 4/3 -c copy ega_screen_overridden.nut
```

[][]

### [3.19 How do I run ffmpeg as a background task?](#toc-How-do-I-run-ffmpeg-as-a-background-task_003f) 

ffmpeg normally checks the console input, for entries like \"q\" to stop and \"?\" to give help, while performing operations. ffmpeg does not have a way of detecting when it is running as a background task. When it checks the console input, that can cause the process running ffmpeg in the background to suspend.

To prevent those input checks, allowing ffmpeg to run as a background task, use the [`-nostdin` option](ffmpeg.html#stdin-option) in the ffmpeg invocation. This is effective whether you run ffmpeg in a shell or invoke ffmpeg in its own process via an operating system API.

As an alternative, when you are running ffmpeg in a shell, you can redirect standard input to `/dev/null` (on Linux and macOS) or `NUL` (on Windows). You can do this redirect either on the ffmpeg invocation, or from a shell script which calls ffmpeg.

For example:

``` example
ffmpeg -nostdin -i INPUT OUTPUT
```

or (on Linux, macOS, and other UNIX-like shells):

``` example
ffmpeg -i INPUT OUTPUT </dev/null
```

or (on Windows):

``` example
ffmpeg -i INPUT OUTPUT <NUL
```

[]

### [3.20 How do I prevent ffmpeg from suspending with a message like *suspended (tty output)*?](#toc-How-do-I-prevent-ffmpeg-from-suspending-with-a-message-like-suspended-_0028tty-output_0029_003f) 

If you run ffmpeg in the background, you may find that its process suspends. There may be a message like *suspended (tty output)*. The question is how to prevent the process from being suspended.

For example:

``` example
% ffmpeg -i INPUT OUTPUT &> ~/tmp/log.txt &
[1] 93352
%
[1]  + suspended (tty output)  ffmpeg -i INPUT OUTPUT &>
```

The message \"tty output\" notwithstanding, the problem here is that ffmpeg normally checks the console input when it runs. The operating system detects this, and suspends the process until you can bring it to the foreground and attend to it.

The solution is to use the right techniques to tell ffmpeg not to consult console input. You can use the [`-nostdin` option](ffmpeg.html#stdin-option), or redirect standard input with `< /dev/null`. See FAQ [*How do I run ffmpeg as a background task?*](#background-task) for details.

[]

## [4 Development](#toc-Development) 

[]

### [4.1 Are there examples illustrating how to use the FFmpeg libraries, particularly libavcodec and libavformat?](#toc-Are-there-examples-illustrating-how-to-use-the-FFmpeg-libraries_002c-particularly-libavcodec-and-libavformat_003f) 

Yes. Check the `doc/examples` directory in the source repository, also available online at: <https://github.com/FFmpeg/FFmpeg/tree/master/doc/examples>.

Examples are also installed by default, usually in `$PREFIX/share/ffmpeg/examples`.

Also you may read the Developers Guide of the FFmpeg documentation. Alternatively, examine the source code for one of the many open source projects that already incorporate FFmpeg at ([projects.html](projects.html)).

[]

### [4.2 Can you support my C compiler XXX?](#toc-Can-you-support-my-C-compiler-XXX_003f) 

It depends. If your compiler is C99-compliant, then patches to support it are likely to be welcome if they do not pollute the source code with `#ifdef`s related to the compiler.

[]

### [4.3 Is Microsoft Visual C++ supported?](#toc-Is-Microsoft-Visual-C_002b_002b-supported_003f) 

Yes. Please see the [Microsoft Visual C++](platform.html) section in the FFmpeg documentation.

[]

### [4.4 Can you add automake, libtool or autoconf support?](#toc-Can-you-add-automake_002c-libtool-or-autoconf-support_003f) 

No. These tools are too bloated and they complicate the build.

[]

### [4.5 Why not rewrite FFmpeg in object-oriented C++?](#toc-Why-not-rewrite-FFmpeg-in-object_002doriented-C_002b_002b_003f) 

FFmpeg is already organized in a highly modular manner and does not need to be rewritten in a formal object language. Further, many of the developers favor straight C; it works for them. For more arguments on this matter, read [\"Programming Religion\"](https://web.archive.org/web/20111004021423/http://kernel.org/pub/linux/docs/lkml/#s15).

[]

### [4.6 Why are the ffmpeg programs devoid of debugging symbols?](#toc-Why-are-the-ffmpeg-programs-devoid-of-debugging-symbols_003f) 

The build process creates `ffmpeg_g`, `ffplay_g`, etc. which contain full debug information. Those binaries are stripped to create `ffmpeg`, `ffplay`, etc. If you need the debug information, use the \*\_g versions.

[]

### [4.7 I do not like the LGPL, can I contribute code under the GPL instead?](#toc-I-do-not-like-the-LGPL_002c-can-I-contribute-code-under-the-GPL-instead_003f) 

Yes, as long as the code is optional and can easily and cleanly be placed under #if CONFIG_GPL without breaking anything. So, for example, a new codec or filter would be OK under GPL while a bug fix to LGPL code would not.

[]

### [4.8 I'm using FFmpeg from within my C application but the linker complains about missing symbols from the libraries themselves.](#toc-I_0027m-using-FFmpeg-from-within-my-C-application-but-the-linker-complains-about-missing-symbols-from-the-libraries-themselves_002e) 

FFmpeg builds static libraries by default. In static libraries, dependencies are not handled. That has two consequences. First, you must specify the libraries in dependency order: `-lavdevice` must come before `-lavformat`, `-lavutil` must come after everything else, etc. Second, external libraries that are used in FFmpeg have to be specified too.

An easy way to get the full list of required libraries in dependency order is to use `pkg-config`.

``` example
c99 -o program program.c $(pkg-config --cflags --libs libavformat libavcodec)
```

See `doc/example/Makefile` and `doc/example/pc-uninstalled` for more details.

[]

### [4.9 I'm using FFmpeg from within my C++ application but the linker complains about missing symbols which seem to be available.](#toc-I_0027m-using-FFmpeg-from-within-my-C_002b_002b-application-but-the-linker-complains-about-missing-symbols-which-seem-to-be-available_002e) 

FFmpeg is a pure C project, so to use the libraries within your C++ application you need to explicitly state that you are using a C library. You can do this by encompassing your FFmpeg includes using `extern "C"`.

See <http://www.parashift.com/c++-faq-lite/mixing-c-and-cpp.html#faq-32.3>

[]

### [4.10 I'm using libavutil from within my C++ application but the compiler complains about 'UINT64_C' was not declared in this scope](#toc-I_0027m-using-libavutil-from-within-my-C_002b_002b-application-but-the-compiler-complains-about-_0027UINT64_005fC_0027-was-not-declared-in-this-scope) 

FFmpeg is a pure C project using C99 math features, in order to enable C++ to use them you have to append -D\_\_STDC_CONSTANT_MACROS to your CXXFLAGS

[]

### [4.11 I have a file in memory / a API different from \*open/\*read/ libc how do I use it with libavformat?](#toc-I-have-a-file-in-memory-_002f-a-API-different-from-_002aopen_002f_002aread_002f-libc-how-do-I-use-it-with-libavformat_003f) 

You have to create a custom AVIOContext using `avio_alloc_context`, see `libavformat/aviobuf.c` in FFmpeg and `libmpdemux/demux_lavf.c` in MPlayer or MPlayer2 sources.

[]

### [4.12 Where is the documentation about ffv1, msmpeg4, asv1, 4xm?](#toc-Where-is-the-documentation-about-ffv1_002c-msmpeg4_002c-asv1_002c-4xm_003f) 

see <https://www.ffmpeg.org/~michael/>

[]

### [4.13 How do I feed H.263-RTP (and other codecs in RTP) to libavcodec?](#toc-How-do-I-feed-H_002e263_002dRTP-_0028and-other-codecs-in-RTP_0029-to-libavcodec_003f) 

Even if peculiar since it is network oriented, RTP is a container like any other. You have to *demux* RTP before feeding the payload to libavcodec. In this specific case please look at RFC 4629 to see how it should be done.

[]

### [4.14 AVStream.r_frame_rate is wrong, it is much larger than the frame rate.](#toc-AVStream_002er_005fframe_005frate-is-wrong_002c-it-is-much-larger-than-the-frame-rate_002e) 

`r_frame_rate` is NOT the average frame rate, it is the smallest frame rate that can accurately represent all timestamps. So no, it is not wrong if it is larger than the average! For example, if you have mixed 25 and 30 fps content, then `r_frame_rate` will be 150 (it is the least common multiple). If you are looking for the average frame rate, see `AVStream.avg_frame_rate`.

[]

### [4.15 Why is `make fate` not running all tests?](#toc-Why-is-make-fate-not-running-all-tests_003f) 

Make sure you have the fate-suite samples and the `SAMPLES` Make variable or `FATE_SAMPLES` environment variable or the `--samples` `configure` option is set to the right path.

[]

### [4.16 Why is `make fate` not finding the samples?](#toc-Why-is-make-fate-not-finding-the-samples_003f) 

Do you happen to have a `~` character in the samples path to indicate a home directory? The value is used in ways where the shell cannot expand it, causing FATE to not find files. Just replace `~` by the full path.

This document was generated on *December 27, 2025* using [*makeinfo*](http://www.gnu.org/software/texinfo/).

[Hosting provided by [telepoint.bg](https://telepoint.bg)]