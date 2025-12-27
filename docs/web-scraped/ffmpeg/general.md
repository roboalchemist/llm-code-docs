# Source: https://ffmpeg.org/general.html

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

# [](#) General Documentation

[] []

## Table of Contents 

-   [1 External libraries](#External-libraries)
    -   [1.1 Alliance for Open Media (AOM)](#Alliance-for-Open-Media-_0028AOM_0029)
    -   [1.2 AMD AMF/VCE](#AMD-AMF_002fVCE)
    -   [1.3 AviSynth](#AviSynth)
    -   [1.4 Chromaprint](#Chromaprint)
    -   [1.5 codec2](#codec2)
    -   [1.6 dav1d](#dav1d)
    -   [1.7 davs2](#davs2)
    -   [1.8 uavs3d](#uavs3d)
    -   [1.9 Game Music Emu](#Game-Music-Emu)
    -   [1.10 Intel QuickSync Video](#Intel-QuickSync-Video)
    -   [1.11 Kvazaar](#Kvazaar)
    -   [1.12 LAME](#LAME)
    -   [1.13 LCEVCdec](#LCEVCdec)
    -   [1.14 libilbc](#libilbc)
    -   [1.15 libjxl](#libjxl)
    -   [1.16 libvpx](#libvpx)
    -   [1.17 ModPlug](#ModPlug)
    -   [1.18 OpenCORE, VisualOn, and Fraunhofer libraries](#OpenCORE_002c-VisualOn_002c-and-Fraunhofer-libraries)
        -   [1.18.1 OpenCORE AMR](#OpenCORE-AMR)
        -   [1.18.2 VisualOn AMR-WB encoder library](#VisualOn-AMR_002dWB-encoder-library)
        -   [1.18.3 Fraunhofer AAC library](#Fraunhofer-AAC-library)
        -   [1.18.4 Fraunhofer MPEG-H 3D Audio decoder library](#Fraunhofer-MPEG_002dH-3D-Audio-decoder-library)
        -   [1.18.5 LC3 library](#LC3-library)
    -   [1.19 OpenH264](#OpenH264)
    -   [1.20 OpenJPEG](#OpenJPEG)
    -   [1.21 rav1e](#rav1e)
    -   [1.22 SVT-AV1](#SVT_002dAV1)
    -   [1.23 SVT-JPEG-XS](#SVT_002dJPEG_002dXS)
    -   [1.24 TwoLAME](#TwoLAME)
    -   [1.25 VapourSynth](#VapourSynth)
    -   [1.26 x264](#x264)
    -   [1.27 x265](#x265)
    -   [1.28 xavs](#xavs)
    -   [1.29 xavs2](#xavs2)
    -   [1.30 eXtra-fast Essential Video Encoder (XEVE)](#eXtra_002dfast-Essential-Video-Encoder-_0028XEVE_0029)
    -   [1.31 eXtra-fast Essential Video Decoder (XEVD)](#eXtra_002dfast-Essential-Video-Decoder-_0028XEVD_0029)
    -   [1.32 ZVBI](#ZVBI)
-   [2 Supported File Formats, Codecs or Features](#Supported-File-Formats_002c-Codecs-or-Features)
    -   [2.1 File Formats](#File-Formats)
    -   [2.2 Image Formats](#Image-Formats)
    -   [2.3 Video Codecs](#Video-Codecs)
    -   [2.4 Audio Codecs](#Audio-Codecs)
    -   [2.5 Subtitle Formats](#Subtitle-Formats)
    -   [2.6 Network Protocols](#Network-Protocols)
    -   [2.7 Input/Output Devices](#Input_002fOutput-Devices)
    -   [2.8 Timecode](#Timecode)

[]

## [1 External libraries](#toc-External-libraries) 

FFmpeg can be hooked up with a number of external libraries to add support for more formats. None of them are used by default, their use has to be explicitly requested by passing the appropriate flags to `./configure`.

[]

### [1.1 Alliance for Open Media (AOM)](#toc-Alliance-for-Open-Media-_0028AOM_0029) 

FFmpeg can make use of the AOM library for AV1 decoding and encoding.

Go to <http://aomedia.org/> and follow the instructions for installing the library. Then pass `--enable-libaom` to configure to enable it.

[]

### [1.2 AMD AMF/VCE](#toc-AMD-AMF_002fVCE) 

FFmpeg can use the AMD Advanced Media Framework library for accelerated H.264 and HEVC(only windows) encoding on hardware with Video Coding Engine (VCE).

To enable support you must obtain the AMF framework header files(version 1.4.9+) from <https://github.com/GPUOpen-LibrariesAndSDKs/AMF.git>.

Create an `AMF/` directory in the system include path. Copy the contents of `AMF/amf/public/include/` into that directory. Then configure FFmpeg with `--enable-amf`.

Initialization of amf encoder occurs in this order: 1) trying to initialize through dx11(only windows) 2) trying to initialize through dx9(only windows) 3) trying to initialize through vulkan

To use h.264(AMD VCE) encoder on linux amdgru-pro version 19.20+ and amf-amdgpu-pro package(amdgru-pro contains, but does not install automatically) are required.

This driver can be installed using amdgpu-pro-install script in official amd driver archive.

[]

### [1.3 AviSynth](#toc-AviSynth) 

FFmpeg can read AviSynth scripts as input. To enable support, pass `--enable-avisynth` to configure after installing the headers provided by [AviSynth+](https://github.com/AviSynth/AviSynthPlus). AviSynth+ can be configured to install only the headers by either passing `-DHEADERS_ONLY:bool=on` to the normal CMake-based build system, or by using the supplied `GNUmakefile`.

For Windows, supported AviSynth variants are [AviSynth 2.6 RC1 or higher](http://avisynth.nl) for 32-bit builds and [AviSynth+ r1718 or higher](http://avisynth.nl/index.php/AviSynth+) for 32-bit and 64-bit builds.

For Linux, macOS, and BSD, the only supported AviSynth variant is [AviSynth+](https://github.com/AviSynth/AviSynthPlus), starting with version 3.5.

In 2016, AviSynth+ added support for building with GCC. However, due to the eccentricities of Windows' calling conventions, 32-bit GCC builds of AviSynth+ are not compatible with typical 32-bit builds of FFmpeg.

By default, FFmpeg assumes compatibility with 32-bit MSVC builds of AviSynth+ since that is the most widely-used and entrenched build configuration. Users can override this and enable support for 32-bit GCC builds of AviSynth+ by passing `-DAVSC_WIN32_GCC32` to `--extra-cflags` when configuring FFmpeg.

64-bit builds of FFmpeg are not affected, and can use either MSVC or GCC builds of AviSynth+ without any special flags.

AviSynth(+) is loaded dynamically. Distributors can build FFmpeg with `--enable-avisynth`, and the binaries will work regardless of the end user having AviSynth installed. If/when an end user would like to use AviSynth scripts, then they can install AviSynth(+) and FFmpeg will be able to find and use it to open scripts.

[]

### [1.4 Chromaprint](#toc-Chromaprint) 

FFmpeg can make use of the Chromaprint library for generating audio fingerprints. Pass `--enable-chromaprint` to configure to enable it. See <https://acoustid.org/chromaprint>.

[]

### [1.5 codec2](#toc-codec2) 

FFmpeg can make use of the codec2 library for codec2 decoding and encoding. There is currently no native decoder, so libcodec2 must be used for decoding.

Go to <http://freedv.org/>, download \"Codec 2 source archive\". Build and install using CMake. Debian users can install the libcodec2-dev package instead. Once libcodec2 is installed you can pass `--enable-libcodec2` to configure to enable it.

The easiest way to use codec2 is with .c2 files, since they contain the mode information required for decoding. To encode such a file, use a .c2 file extension and give the libcodec2 encoder the -mode option: `ffmpeg -i input.wav -mode 700C output.c2`. Playback is as simple as `ffplay output.c2`. For a list of supported modes, run `ffmpeg -h encoder=libcodec2`. Raw codec2 files are also supported. To make sense of them the mode in use needs to be specified as a format option: `ffmpeg -f codec2raw -mode 1300 -i input.raw output.wav`.

[]

### [1.6 dav1d](#toc-dav1d) 

FFmpeg can make use of the dav1d library for AV1 video decoding.

Go to <https://code.videolan.org/videolan/dav1d> and follow the instructions for installing the library. Then pass `--enable-libdav1d` to configure to enable it.

[]

### [1.7 davs2](#toc-davs2) 

FFmpeg can make use of the davs2 library for AVS2-P2/IEEE1857.4 video decoding.

Go to <https://github.com/pkuvcl/davs2> and follow the instructions for installing the library. Then pass `--enable-libdavs2` to configure to enable it.

libdavs2 is under the GNU Public License Version 2 or later (see <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html> for details), you must upgrade FFmpeg's license to GPL in order to use it.

[]

### [1.8 uavs3d](#toc-uavs3d) 

FFmpeg can make use of the uavs3d library for AVS3-P2/IEEE1857.10 video decoding.

Go to <https://github.com/uavs3/uavs3d> and follow the instructions for installing the library. Then pass `--enable-libuavs3d` to configure to enable it.

[]

### [1.9 Game Music Emu](#toc-Game-Music-Emu) 

FFmpeg can make use of the Game Music Emu library to read audio from supported video game music file formats. Pass `--enable-libgme` to configure to enable it. See <https://bitbucket.org/mpyne/game-music-emu/overview>.

[]

### [1.10 Intel QuickSync Video](#toc-Intel-QuickSync-Video) 

FFmpeg can use Intel QuickSync Video (QSV) for accelerated decoding and encoding of multiple codecs. To use QSV, FFmpeg must be linked against the `libmfx` dispatcher, which loads the actual decoding libraries.

The dispatcher is open source and can be downloaded from <https://github.com/lu-zero/mfx_dispatch.git>. FFmpeg needs to be configured with the `--enable-libmfx` option and `pkg-config` needs to be able to locate the dispatcher's `.pc` files.

[]

### [1.11 Kvazaar](#toc-Kvazaar) 

FFmpeg can make use of the Kvazaar library for HEVC encoding.

Go to <https://github.com/ultravideo/kvazaar> and follow the instructions for installing the library. Then pass `--enable-libkvazaar` to configure to enable it.

[]

### [1.12 LAME](#toc-LAME) 

FFmpeg can make use of the LAME library for MP3 encoding.

Go to <http://lame.sourceforge.net/> and follow the instructions for installing the library. Then pass `--enable-libmp3lame` to configure to enable it.

[]

### [1.13 LCEVCdec](#toc-LCEVCdec) 

FFmpeg can make use of the liblcevc_dec library for LCEVC enhancement layer decoding on supported bitstreams.

Go to <https://github.com/v-novaltd/LCEVCdec> and follow the instructions for installing the library. Then pass `--enable-liblcevc-dec` to configure to enable it.

LCEVCdec is under the BSD-3-Clause-Clear License.

[]

### [1.14 libilbc](#toc-libilbc) 

iLBC is a narrowband speech codec that has been made freely available by Google as part of the WebRTC project. libilbc is a packaging friendly copy of the iLBC codec. FFmpeg can make use of the libilbc library for iLBC decoding and encoding.

Go to <https://github.com/TimothyGu/libilbc> and follow the instructions for installing the library. Then pass `--enable-libilbc` to configure to enable it.

[]

### [1.15 libjxl](#toc-libjxl) 

JPEG XL is an image format intended to fully replace legacy JPEG for an extended period of life. See <https://jpegxl.info/> for more information, and see <https://github.com/libjxl/libjxl> for the library source. You can pass `--enable-libjxl` to configure in order enable the libjxl wrapper.

[]

### [1.16 libvpx](#toc-libvpx) 

FFmpeg can make use of the libvpx library for VP8/VP9 decoding and encoding.

Go to <http://www.webmproject.org/> and follow the instructions for installing the library. Then pass `--enable-libvpx` to configure to enable it.

[]

### [1.17 ModPlug](#toc-ModPlug) 

FFmpeg can make use of this library, originating in Modplug-XMMS, to read from MOD-like music files. See <https://github.com/Konstanty/libmodplug>. Pass `--enable-libmodplug` to configure to enable it.

[]

### [1.18 OpenCORE, VisualOn, and Fraunhofer libraries](#toc-OpenCORE_002c-VisualOn_002c-and-Fraunhofer-libraries) 

Spun off Google Android sources, OpenCore, VisualOn and Fraunhofer libraries provide encoders for a number of audio codecs.

OpenCORE and VisualOn libraries are under the Apache License 2.0 (see <http://www.apache.org/licenses/LICENSE-2.0> for details), which is incompatible to the LGPL version 2.1 and GPL version 2. You have to upgrade FFmpeg's license to LGPL version 3 (or if you have enabled GPL components, GPL version 3) by passing `--enable-version3` to configure in order to use it.

The license of the Fraunhofer AAC library is incompatible with the GPL. Therefore, for GPL builds, you have to pass `--enable-nonfree` to configure in order to use it. To the best of our knowledge, it is compatible with the LGPL.

[]

#### [1.18.1 OpenCORE AMR](#toc-OpenCORE-AMR) 

FFmpeg can make use of the OpenCORE libraries for AMR-NB decoding/encoding and AMR-WB decoding.

Go to <http://sourceforge.net/projects/opencore-amr/> and follow the instructions for installing the libraries. Then pass `--enable-libopencore-amrnb` and/or `--enable-libopencore-amrwb` to configure to enable them.

[]

#### [1.18.2 VisualOn AMR-WB encoder library](#toc-VisualOn-AMR_002dWB-encoder-library) 

FFmpeg can make use of the VisualOn AMR-WBenc library for AMR-WB encoding.

Go to <http://sourceforge.net/projects/opencore-amr/> and follow the instructions for installing the library. Then pass `--enable-libvo-amrwbenc` to configure to enable it.

[]

#### [1.18.3 Fraunhofer AAC library](#toc-Fraunhofer-AAC-library) 

FFmpeg can make use of the Fraunhofer AAC library for AAC decoding & encoding.

Go to <http://sourceforge.net/projects/opencore-amr/> and follow the instructions for installing the library. Then pass `--enable-libfdk-aac` to configure to enable it.

[]

#### [1.18.4 Fraunhofer MPEG-H 3D Audio decoder library](#toc-Fraunhofer-MPEG_002dH-3D-Audio-decoder-library) 

FFmpeg can make use of the Fraunhofer MPEG-H decoder library for MPEG-H 3DA decoding.

Go to <https://github.com/Fraunhofer-IIS/mpeghdec> and follow the instructions for installing the library. Then pass `--enable-libmpeghdec --enable-nonfree` to configure to enable it.

[]

#### [1.18.5 LC3 library](#toc-LC3-library) 

FFmpeg can make use of the Google LC3 library for LC3 decoding & encoding.

Go to <https://github.com/google/liblc3/> and follow the instructions for installing the library. Then pass `--enable-liblc3` to configure to enable it.

[]

### [1.19 OpenH264](#toc-OpenH264) 

FFmpeg can make use of the OpenH264 library for H.264 decoding and encoding.

Go to <http://www.openh264.org/> and follow the instructions for installing the library. Then pass `--enable-libopenh264` to configure to enable it.

For decoding, this library is much more limited than the built-in decoder in libavcodec; currently, this library lacks support for decoding B-frames and some other main/high profile features. (It currently only supports constrained baseline profile and CABAC.) Using it is mostly useful for testing and for taking advantage of Cisco's patent portfolio license (<http://www.openh264.org/BINARY_LICENSE.txt>).

[]

### [1.20 OpenJPEG](#toc-OpenJPEG) 

FFmpeg can use the OpenJPEG libraries for decoding/encoding J2K videos. Go to <http://www.openjpeg.org/> to get the libraries and follow the installation instructions. To enable using OpenJPEG in FFmpeg, pass `--enable-libopenjpeg` to `./configure`.

[]

### [1.21 rav1e](#toc-rav1e) 

FFmpeg can make use of rav1e (Rust AV1 Encoder) via its C bindings to encode videos. Go to <https://github.com/xiph/rav1e/> and follow the instructions to build the C library. To enable using rav1e in FFmpeg, pass `--enable-librav1e` to `./configure`.

[]

### [1.22 SVT-AV1](#toc-SVT_002dAV1) 

FFmpeg can make use of the Scalable Video Technology for AV1 library for AV1 encoding.

Go to <https://gitlab.com/AOMediaCodec/SVT-AV1/> and follow the instructions for installing the library. Then pass `--enable-libsvtav1` to configure to enable it.

[]

### [1.23 SVT-JPEG-XS](#toc-SVT_002dJPEG_002dXS) 

FFmpeg can make use of the Scalable Video Technology for JPEG-XS library for JPEG-XS decoding and encoding.

Go to <https://github.com/OpenVisualCloud/SVT-JPEG-XS> and follow the instructions for installing the library. Then pass `--enable-libsvtjpegxs` to configure to enable it.

[]

### [1.24 TwoLAME](#toc-TwoLAME) 

FFmpeg can make use of the TwoLAME library for MP2 encoding.

Go to <http://www.twolame.org/> and follow the instructions for installing the library. Then pass `--enable-libtwolame` to configure to enable it.

[]

### [1.25 VapourSynth](#toc-VapourSynth) 

FFmpeg can read VapourSynth scripts as input. To enable support, pass `--enable-vapoursynth` to configure. Vapoursynth is detected via `pkg-config`. Versions 42 or greater supported. See <http://www.vapoursynth.com/>.

Due to security concerns, Vapoursynth scripts will not be autodetected so the input format has to be forced. For ff\* CLI tools, add `-f vapoursynth` before the input `-i yourscript.vpy`.

[]

### [1.26 x264](#toc-x264) 

FFmpeg can make use of the x264 library for H.264 encoding.

Go to <http://www.videolan.org/developers/x264.html> and follow the instructions for installing the library. Then pass `--enable-libx264` to configure to enable it.

x264 is under the GNU Public License Version 2 or later (see <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html> for details), you must upgrade FFmpeg's license to GPL in order to use it.

[]

### [1.27 x265](#toc-x265) 

FFmpeg can make use of the x265 library for HEVC encoding.

Go to <http://x265.org/developers.html> and follow the instructions for installing the library. Then pass `--enable-libx265` to configure to enable it.

x265 is under the GNU Public License Version 2 or later (see <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html> for details), you must upgrade FFmpeg's license to GPL in order to use it.

[]

### [1.28 xavs](#toc-xavs) 

FFmpeg can make use of the xavs library for AVS encoding.

Go to <http://xavs.sf.net/> and follow the instructions for installing the library. Then pass `--enable-libxavs` to configure to enable it.

[]

### [1.29 xavs2](#toc-xavs2) 

FFmpeg can make use of the xavs2 library for AVS2-P2/IEEE1857.4 video encoding.

Go to <https://github.com/pkuvcl/xavs2> and follow the instructions for installing the library. Then pass `--enable-libxavs2` to configure to enable it.

libxavs2 is under the GNU Public License Version 2 or later (see <http://www.gnu.org/licenses/old-licenses/gpl-2.0.html> for details), you must upgrade FFmpeg's license to GPL in order to use it.

[]

### [1.30 eXtra-fast Essential Video Encoder (XEVE)](#toc-eXtra_002dfast-Essential-Video-Encoder-_0028XEVE_0029) 

FFmpeg can make use of the XEVE library for EVC video encoding.

Go to <https://github.com/mpeg5/xeve> and follow the instructions for installing the XEVE library. Then pass `--enable-libxeve` to configure to enable it.

[]

### [1.31 eXtra-fast Essential Video Decoder (XEVD)](#toc-eXtra_002dfast-Essential-Video-Decoder-_0028XEVD_0029) 

FFmpeg can make use of the XEVD library for EVC video decoding.

Go to <https://github.com/mpeg5/xevd> and follow the instructions for installing the XEVD library. Then pass `--enable-libxevd` to configure to enable it.

[]

### [1.32 ZVBI](#toc-ZVBI) 

ZVBI is a VBI decoding library which can be used by FFmpeg to decode DVB teletext pages and DVB teletext subtitles.

Go to <http://sourceforge.net/projects/zapping/> and follow the instructions for installing the library. Then pass `--enable-libzvbi` to configure to enable it.

[]

## [2 Supported File Formats, Codecs or Features](#toc-Supported-File-Formats_002c-Codecs-or-Features) 

You can use the `-formats` and `-codecs` options to have an exhaustive list.

[]

### [2.1 File Formats](#toc-File-Formats) 

FFmpeg supports the following file formats through the `libavformat` library:

  ---------------------------------------------- ---------- ---------- -------------------------------------------------------------------------------------------------------------------------------------
  Name                                           Encoding   Decoding   Comments
  3dostr                                                    X          
  4xm                                                       X          4X Technologies format, used in some games.
  8088flex TMV                                              X          
  AAX                                                       X          Audible Enhanced Audio format, used in audiobooks.
  AA                                                        X          Audible Format 2, 3, and 4, used in audiobooks.
  ACT Voice                                                 X          contains G.729 audio
  Adobe Filmstrip                                X          X          
  Audio IFF (AIFF)                               X          X          
  American Laser Games MM                                   X          Multimedia format used in games like Mad Dog McCree.
  3GPP AMR                                       X          X          
  Amazing Studio Packed Animation File                      X          Multimedia format used in game Heart Of Darkness.
  Apple HTTP Live Streaming                                 X          
  Artworx Data Format                                       X          
  Interplay ACM                                             X          Audio only format used in some Interplay games.
  ADP                                                       X          Audio format used on the Nintendo Gamecube.
  AFC                                                       X          Audio format used on the Nintendo Gamecube.
  ADS/SS2                                                   X          Audio format used on the PS2.
  APNG                                           X          X          
  ASF                                            X          X          Advanced / Active Streaming Format.
  AST                                            X          X          Audio format used on the Nintendo Wii.
  AVI                                            X          X          
  AviSynth                                                  X          
  AVR                                                       X          Audio format used on Mac.
  AVS                                                       X          Multimedia format used by the Creature Shock game.
  Beam Software SIFF                                        X          Audio and video format used in some games by Beam Software.
  Bethesda Softworks VID                                    X          Used in some games from Bethesda Softworks.
  Binary text                                               X          
  Bink                                                      X          Multimedia format used by many games.
  Bink Audio                                                X          Audio only multimedia format used by some games.
  Bitmap Brothers JV                                        X          Used in Z and Z95 games.
  BRP                                                       X          Argonaut Games format.
  Brute Force & Ignorance                                   X          Used in the game Flash Traffic: City of Angels.
  BFSTM                                                     X          Audio format used on the Nintendo WiiU (based on BRSTM).
  BRSTM                                                     X          Audio format used on the Nintendo Wii.
  BW64                                                      X          Broadcast Wave 64bit.
  BWF                                            X          X          
  codec2 (raw)                                   X          X          Must be given -mode format option to decode correctly.
  codec2 (.c2 files)                             X          X          Contains header with version and mode info, simplifying playback.
  CRI ADX                                        X          X          Audio-only format used in console video games.
  CRI AIX                                                   X          
  CRI HCA                                                   X          Audio-only format used in console video games.
  Discworld II BMV                                          X          
  Interplay C93                                             X          Used in the game Cyberia from Interplay.
  Delphine Software International CIN                       X          Multimedia format used by Delphine Software games.
  Digital Speech Standard (DSS)                             X          
  CD+G                                                      X          Video format used by CD+G karaoke disks
  Phantom Cine                                              X          
  Commodore CDXL                                            X          Amiga CD video format
  Core Audio Format                              X          X          Apple Core Audio Format
  CRC testing format                             X                     
  Creative Voice                                 X          X          Created for the Sound Blaster Pro.
  CRYO APC                                                  X          Audio format used in some games by CRYO Interactive Entertainment.
  D-Cinema audio                                 X          X          
  Deluxe Paint Animation                                    X          
  DCSTR                                                     X          
  DFA                                                       X          This format is used in Chronomaster game
  DirectDraw Surface                                        X          
  DSD Stream File (DSF)                                     X          
  DV video                                       X          X          
  DXA                                                       X          This format is used in the non-Windows version of the Feeble Files game and different game cutscenes repacked for use with ScummVM.
  Electronic Arts cdata                                     X          
  Electronic Arts Multimedia                                X          Used in various EA games; files have extensions like WVE and UV2.
  Ensoniq Paris Audio File                                  X          
  FFM (FFserver live feed)                       X          X          
  Flash (SWF)                                    X          X          
  Flash 9 (AVM2)                                 X          X          Only embedded audio is decoded.
  FLI/FLC/FLX animation                                     X          .fli/.flc files
  Flash Video (FLV)                              X          X          Macromedia Flash video files
  framecrc testing format                        X                     
  FunCom ISS                                                X          Audio format used in various games from FunCom like The Longest Journey.
  G.723.1                                        X          X          
  G.726                                                     X          Both left- and right-justified.
  G.729 BIT                                      X          X          
  G.729 raw                                                 X          
  GENH                                                      X          Audio format for various games.
  GIF Animation                                  X          X          
  GXF                                            X          X          General eXchange Format SMPTE 360M, used by Thomson Grass Valley playout servers.
  HNM                                                       X          Only version 4 supported, used in some games from Cryo Interactive
  iCEDraw File                                              X          
  ICO                                            X          X          Microsoft Windows ICO
  id Quake II CIN video                                     X          
  id RoQ                                         X          X          Used in Quake III, Jedi Knight 2 and other computer games.
  IEC61937 encapsulation                         X          X          
  IFF                                                       X          Interchange File Format
  IFV                                                       X          A format used by some old CCTV DVRs.
  iLBC                                           X          X          
  Interplay MVE                                             X          Format used in various Interplay computer games.
  Iterated Systems ClearVideo                               X          I-frames only
  IV8                                                       X          A format generated by IndigoVision 8000 video server.
  IVF (On2)                                      X          X          A format used by libvpx
  Internet Video Recording                                  X          
  IRCAM                                          X          X          
  LAF                                                       X          Limitless Audio Format
  LATM                                           X          X          
  LMLM4                                                     X          Used by Linux Media Labs MPEG-4 PCI boards
  LOAS                                                      X          contains LATM multiplexed AAC audio
  LRC                                            X          X          
  LVF                                                       X          
  LXF                                                       X          VR native stream format, used by Leitch/Harris' video servers.
  Magic Lantern Video (MLV)                                 X          
  Matroska                                       X          X          
  Matroska audio                                 X                     
  FFmpeg metadata                                X          X          Metadata in text format.
  MAXIS XA                                                  X          Used in Sim City 3000; file extension .xa.
  MCA                                                       X          Used in some games from Capcom; file extension .mca.
  MD Studio                                                 X          
  Metal Gear Solid: The Twin Snakes                         X          
  Megalux Frame                                             X          Used by Megalux Ultimate Paint
  MobiClip MODS                                             X          
  MobiClip MOFLEX                                           X          
  Mobotix .mxg                                              X          
  Monkey's Audio                                            X          
  Motion Pixels MVI                                         X          
  MOV/QuickTime/MP4                              X          X          3GP, 3GP2, PSP, iPod variants supported
  MP2                                            X          X          
  MP3                                            X          X          
  MPEG-1 System                                  X          X          muxed audio and video, VCD format supported
  MPEG-PS (program stream)                       X          X          also known as `VOB` file, SVCD and DVD format supported
  MPEG-TS (transport stream)                     X          X          also known as DVB Transport Stream
  MPEG-4                                         X          X          MPEG-4 is a variant of QuickTime.
  MSF                                                       X          Audio format used on the PS3.
  Mirillis FIC video                                        X          No cursor rendering.
  MIDI Sample Dump Standard                                 X          
  MIME multipart JPEG                            X                     
  MSN TCP webcam                                            X          Used by MSN Messenger webcam streams.
  MTV                                                       X          
  Musepack                                                  X          
  Musepack SV8                                              X          
  Material eXchange Format (MXF)                 X          X          SMPTE 377M, used by D-Cinema, broadcast industry.
  Material eXchange Format (MXF), D-10 Mapping   X          X          SMPTE 386M, D-10/IMX Mapping.
  NC camera feed                                            X          NC (AVIP NC4600) camera streams
  NIST SPeech HEader REsources                              X          
  Computerized Speech Lab NSP                               X          
  NTT TwinVQ (VQF)                                          X          Nippon Telegraph and Telephone Corporation TwinVQ.
  Nullsoft Streaming Video                                  X          
  NuppelVideo                                               X          
  NUT                                            X          X          NUT Open Container Format
  Ogg                                            X          X          
  Playstation Portable PMP                                  X          
  Portable Voice Format                                     X          
  RK Audio (RKA)                                            X          
  TechnoTrend PVA                                           X          Used by TechnoTrend DVB PCI boards.
  QCP                                                       X          
  raw ADTS (AAC)                                 X          X          
  raw AC-3                                       X          X          
  raw AMR-NB                                                X          
  raw AMR-WB                                                X          
  raw APAC                                                  X          
  raw APV                                        X          X          
  raw aptX                                       X          X          
  raw aptX HD                                    X          X          
  raw Bonk                                                  X          
  raw Chinese AVS video                          X          X          
  raw DFPWM                                      X          X          
  raw Dirac                                      X          X          
  raw DNxHD                                      X          X          
  raw DTS                                        X          X          
  raw DTS-HD                                                X          
  raw E-AC-3                                     X          X          
  raw EVC                                        X          X          
  raw FLAC                                       X          X          
  raw G.728                                                 X          
  raw GSM                                                   X          
  raw H.261                                      X          X          
  raw H.263                                      X          X          
  raw H.264                                      X          X          
  raw HEVC                                       X          X          
  raw Ingenient MJPEG                                       X          
  raw MJPEG                                      X          X          
  raw MLP                                                   X          
  raw MPEG                                                  X          
  raw MPEG-1                                                X          
  raw MPEG-2                                                X          
  raw MPEG-4                                     X          X          
  raw NULL                                       X                     
  raw video                                      X          X          
  raw id RoQ                                     X                     
  raw OBU                                        X          X          
  raw OSQ                                                   X          
  raw SBC                                        X          X          
  raw Shorten                                               X          
  raw TAK                                                   X          
  raw TrueHD                                     X          X          
  raw VC-1                                       X          X          
  raw PCM A-law                                  X          X          
  raw PCM mu-law                                 X          X          
  raw PCM Archimedes VIDC                        X          X          
  raw PCM signed 8 bit                           X          X          
  raw PCM signed 16 bit big-endian               X          X          
  raw PCM signed 16 bit little-endian            X          X          
  raw PCM signed 24 bit big-endian               X          X          
  raw PCM signed 24 bit little-endian            X          X          
  raw PCM signed 32 bit big-endian               X          X          
  raw PCM signed 32 bit little-endian            X          X          
  raw PCM signed 64 bit big-endian               X          X          
  raw PCM signed 64 bit little-endian            X          X          
  raw PCM unsigned 8 bit                         X          X          
  raw PCM unsigned 16 bit big-endian             X          X          
  raw PCM unsigned 16 bit little-endian          X          X          
  raw PCM unsigned 24 bit big-endian             X          X          
  raw PCM unsigned 24 bit little-endian          X          X          
  raw PCM unsigned 32 bit big-endian             X          X          
  raw PCM unsigned 32 bit little-endian          X          X          
  raw PCM 16.8 floating point little-endian                 X          
  raw PCM 24.0 floating point little-endian                 X          
  raw PCM floating-point 32 bit big-endian       X          X          
  raw PCM floating-point 32 bit little-endian    X          X          
  raw PCM floating-point 64 bit big-endian       X          X          
  raw PCM floating-point 64 bit little-endian    X          X          
  RDT                                                       X          
  REDCODE R3D                                               X          File format used by RED Digital cameras, contains JPEG 2000 frames and PCM audio.
  RealMedia                                      X          X          
  Redirector                                                X          
  RedSpark                                                  X          
  Renderware TeXture Dictionary                             X          
  Resolume DXV                                   X          X          Encoding is only supported for the DXT1 (Normal Quality, No Alpha) texture format.
  RF64                                                      X          
  RL2                                                       X          Audio and video format used in some games by Entertainment Software Partners.
  RPL/ARMovie                                               X          
  Lego Mindstorms RSO                            X          X          
  RSD                                                       X          
  RTMP                                           X          X          Output is performed by publishing stream to RTMP server
  RTP                                            X          X          
  RTSP                                           X          X          
  Sample Dump eXchange                                      X          
  SAP                                            X          X          
  SBG                                                       X          
  SDNS                                                      X          
  SDP                                                       X          
  SER                                                       X          
  Digital Pictures SGA                                      X          
  Sega FILM/CPK                                  X          X          Used in many Sega Saturn console games.
  Silicon Graphics Movie                                    X          
  Sierra SOL                                                X          .sol files used in Sierra Online games.
  Sierra VMD                                                X          Used in Sierra CD-ROM games.
  Smacker                                                   X          Multimedia format used by many games.
  SMJPEG                                         X          X          Used in certain Loki game ports.
  SMPTE 337M encapsulation                                  X          
  Smush                                                     X          Multimedia format used in some LucasArts games.
  Sony OpenMG (OMA)                              X          X          Audio format used in Sony Sonic Stage and Sony Vegas.
  Sony PlayStation STR                                      X          
  Sony Wave64 (W64)                              X          X          
  SoX native format                              X          X          
  SUN AU format                                  X          X          
  SUP raw PGS subtitles                          X          X          
  SVAG                                                      X          Audio format used in Konami PS2 games.
  TDSC                                                      X          
  Text files                                                X          
  THP                                                       X          Used on the Nintendo GameCube.
  Tiertex Limited SEQ                                       X          Tiertex .seq files used in the DOS CD-ROM version of the game Flashback.
  True Audio                                     X          X          
  VAG                                                       X          Audio format used in many Sony PS2 games.
  VC-1 test bitstream                            X          X          
  Vidvox Hap                                     X          X          
  Vivo                                                      X          
  VPK                                                       X          Audio format used in Sony PS games.
  Marble WADY                                               X          
  WAV                                            X          X          
  Waveform Archiver                                         X          
  WavPack                                        X          X          
  WebM                                           X          X          
  Windows Televison (WTV)                        X          X          
  Wing Commander III movie                                  X          Multimedia format used in Origin's Wing Commander III computer game.
  Westwood Studios audio                         X          X          Multimedia format used in Westwood Studios games.
  Westwood Studios VQA                                      X          Multimedia format used in Westwood Studios games.
  Wideband Single-bit Data (WSD)                            X          
  WVE                                                       X          
  Konami XMD                                                X          
  XMV                                                       X          Microsoft video container used in Xbox games.
  XVAG                                                      X          Audio format used on the PS3.
  xWMA                                                      X          Microsoft audio container used by XAudio 2.
  eXtended BINary text (XBIN)                               X          
  YUV4MPEG pipe                                  X          X          
  Psygnosis YOP                                             X          
  ---------------------------------------------- ---------- ---------- -------------------------------------------------------------------------------------------------------------------------------------

`X` means that the feature in that column (encoding / decoding) is supported.

[]

### [2.2 Image Formats](#toc-Image-Formats) 

FFmpeg can read and write images for each frame of a video sequence. The following image formats are supported:

  ------------------ ---------- ---------- ------------------------------------------------------------------------
  Name               Encoding   Decoding   Comments
  .Y.U.V             X          X          one raw file per component
  Alias PIX          X          X          Alias/Wavefront PIX image format
  animated GIF       X          X          
  APNG               X          X          Animated Portable Network Graphics
  BMP                X          X          Microsoft BMP image
  BRender PIX                   X          Argonaut BRender 3D engine image format.
  CRI                           X          Cintel RAW
  DPX                X          X          Digital Picture Exchange
  EXR                           X          OpenEXR
  FITS               X          X          Flexible Image Transport System
  HDR                X          X          Radiance HDR RGBE Image format
  IMG                           X          GEM Raster image
  JPEG               X          X          Progressive JPEG is not supported.
  JPEG 2000          X          X          
  JPEG-LS            X          X          
  JPEG-XS            E          E          Supported through external library libsvtjpegxs
  LJPEG              X                     Lossless JPEG
  Media 100                     X          
  MSP                           X          Microsoft Paint image
  PAM                X          X          PAM is a PNM extension with alpha support.
  PBM                X          X          Portable BitMap image
  PCD                           X          PhotoCD
  PCX                X          X          PC Paintbrush
  PFM                X          X          Portable FloatMap image
  PGM                X          X          Portable GrayMap image
  PGMYUV             X          X          PGM with U and V components in YUV 4:2:0
  PGX                           X          PGX file decoder
  PHM                X          X          Portable HalfFloatMap image
  PIC                           X          Pictor/PC Paint
  PNG                X          X          Portable Network Graphics image
  PPM                X          X          Portable PixelMap image
  PSD                           X          Photoshop
  PTX                           X          V.Flash PTX format
  QOI                X          X          Quite OK Image format
  SGI                X          X          SGI RGB image format
  Sun Rasterfile     X          X          Sun RAS image format
  TIFF               X          X          YUV, JPEG and some extension is not supported yet.
  Truevision Targa   X          X          Targa (.TGA) image format
  VBN                X          X          Vizrt Binary Image format
  WBMP               X          X          Wireless Application Protocol Bitmap image format
  WebP               E          X          WebP image format, encoding supported through external library libwebp
  XBM                X          X          X BitMap image format
  XFace              X          X          X-Face image format
  XPM                           X          X PixMap image format
  XWD                X          X          X Window Dump image format
  ------------------ ---------- ---------- ------------------------------------------------------------------------

`X` means that the feature in that column (encoding / decoding) is supported.

`E` means that support is provided through an external library.

[]

### [2.3 Video Codecs](#toc-Video-Codecs) 

  --------------------------------------------------------- ---------- ---------- --------------------------------------------------------------------------------
  Name                                                      Encoding   Decoding   Comments
  4X Movie                                                             X          Used in certain computer games.
  8088flex TMV                                                         X          
  A64 multicolor                                            X                     Creates video suitable to be played on a commodore 64 (multicolor mode).
  Amazing Studio PAF Video                                             X          
  American Laser Games MM                                              X          Used in games like Mad Dog McCree.
  Amuse Graphics Movie                                                 X          
  AMV Video                                                 X          X          Used in Chinese MP3 players.
  ANSI/ASCII art                                                       X          
  Apple Intermediate Codec                                             X          
  Apple MJPEG-B                                                        X          
  Apple Pixlet                                                         X          
  Apple ProRes                                              X          X          fourcc: apch,apcn,apcs,apco,ap4h,ap4x
  Apple QuickDraw                                                      X          fourcc: qdrw
  APV                                                                  X          
  Argonaut Video                                                       X          Used in some Argonaut games.
  Asus v1                                                   X          X          fourcc: ASV1
  Asus v2                                                   X          X          fourcc: ASV2
  ATI VCR1                                                             X          fourcc: VCR1
  ATI VCR2                                                             X          fourcc: VCR2
  Auravision Aura                                                      X          
  Auravision Aura 2                                                    X          
  Autodesk Animator Flic video                                         X          
  Autodesk RLE                                                         X          fourcc: AASC
  AV1                                                       E          E          Supported through external libraries libaom, libdav1d, librav1e and libsvtav1
  Avid 1:1 10-bit RGB Packer                                X          X          fourcc: AVrp
  AVS (Audio Video Standard) video                                     X          Video encoding used by the Creature Shock game.
  AVS2-P2/IEEE1857.4                                        E          E          Supported through external libraries libxavs2 and libdavs2
  AVS3-P2/IEEE1857.10                                                  E          Supported through external library libuavs3d
  AYUV                                                      X          X          Microsoft uncompressed packed 4:4:4:4
  Beam Software VB                                                     X          
  Bethesda VID video                                                   X          Used in some games from Bethesda Softworks.
  Bink Video                                                           X          
  BitJazz SheerVideo                                                   X          
  Bitmap Brothers JV video                                             X          
  y41p Brooktree uncompressed 4:1:1 12-bit                  X          X          
  Brooktree ProSumer Video                                             X          fourcc: BT20
  Brute Force & Ignorance                                              X          Used in the game Flash Traffic: City of Angels.
  C93 video                                                            X          Codec used in Cyberia game.
  CamStudio                                                            X          fourcc: CSCD
  CD+G                                                                 X          Video codec for CD+G karaoke disks
  CDXL                                                                 X          Amiga CD video codec
  Chinese AVS video                                         E          X          AVS1-P2, JiZhun profile, encoding through external library libxavs
  Delphine Software International CIN video                            X          Codec used in Delphine Software International games.
  Discworld II BMV Video                                               X          
  CineForm HD                                               X          X          
  Canopus HQ                                                           X          
  Canopus HQA                                                          X          
  Canopus HQX                                                          X          
  Canopus Lossless Codec                                               X          
  CDToons                                                              X          Codec used in various Broderbund games.
  Cinepak                                                              X          
  Cirrus Logic AccuPak                                      X          X          fourcc: CLJR
  CPiA Video Format                                                    X          
  Creative YUV (CYUV)                                                  X          
  DFA                                                                  X          Codec used in Chronomaster game.
  Dirac                                                     E          X          supported though the native vc2 (Dirac Pro) encoder
  Deluxe Paint Animation                                               X          
  DNxHD                                                     X          X          aka SMPTE VC3
  Duck TrueMotion 1.0                                                  X          fourcc: DUCK
  Duck TrueMotion 2.0                                                  X          fourcc: TM20
  Duck TrueMotion 2.0 RT                                               X          fourcc: TR20
  DV (Digital Video)                                        X          X          
  Dxtory capture format                                                X          
  Feeble Files/ScummVM DXA                                             X          Codec originally used in Feeble Files game.
  Electronic Arts CMV video                                            X          Used in NHL 95 game.
  Electronic Arts Madcow video                                         X          
  Electronic Arts TGV video                                            X          
  Electronic Arts TGQ video                                            X          
  Electronic Arts TQI video                                            X          
  Escape 124                                                           X          
  Escape 130                                                           X          
  EVC / MPEG-5 Part 1                                       E          E          encoding and decoding supported through external libraries libxeve and libxevd
  FFmpeg video codec #1                                     X          X          lossless codec (fourcc: FFV1)
  Flash Screen Video v1                                     X          X          fourcc: FSV1
  Flash Screen Video v2                                     X          X          
  Flash Video (FLV)                                         X          X          Sorenson H.263 used in Flash
  FM Screen Capture Codec                                              X          
  Forward Uncompressed                                                 X          
  Fraps                                                                X          
  Go2Meeting                                                           X          fourcc: G2M2, G2M3
  Go2Webinar                                                           X          fourcc: G2M4
  Gremlin Digital Video                                                X          
  H.261                                                     X          X          
  H.263 / H.263-1996                                        X          X          
  H.263+ / H.263-1998 / H.263 version 2                     X          X          
  H.264 / AVC / MPEG-4 AVC / MPEG-4 part 10                 E          X          encoding supported through external library libx264 and OpenH264
  HEVC                                                      X          X          encoding supported through external library libx265 and libkvazaar
  HNM version 4                                                        X          
  HuffYUV                                                   X          X          
  HuffYUV FFmpeg variant                                    X          X          
  IBM Ultimotion                                                       X          fourcc: ULTI
  id Cinematic video                                                   X          Used in Quake II.
  id RoQ video                                              X          X          Used in Quake III, Jedi Knight 2, other computer games.
  IFF ILBM                                                             X          IFF interleaved bitmap
  IFF ByteRun1                                                         X          IFF run length encoded bitmap
  Infinity IMM4                                                        X          
  Intel H.263                                                          X          
  Intel Indeo 2                                                        X          
  Intel Indeo 3                                                        X          
  Intel Indeo 4                                                        X          
  Intel Indeo 5                                                        X          
  Interplay C93                                                        X          Used in the game Cyberia from Interplay.
  Interplay MVE video                                                  X          Used in Interplay .MVE files.
  J2K                                                       X          X          
  Karl Morton's video codec                                            X          Codec used in Worms games.
  Kega Game Video (KGV1)                                               X          Kega emulator screen capture codec.
  Lagarith                                                             X          
  LCEVC / MPEG-5 LCEVC / MPEG-5 Part 2                                 E          decoding supported through external library liblcevc-dec
  LCL (LossLess Codec Library) MSZH                                    X          
  LCL (LossLess Codec Library) ZLIB                         E          E          
  LEAD MCMP                                                            X          
  LOCO                                                                 X          
  LucasArts SANM/Smush                                                 X          Used in LucasArts games / SMUSH animations.
  lossless MJPEG                                            X          X          
  MagicYUV Video                                            X          X          
  Mandsoft Screen Capture Codec                                        X          
  Microsoft ATC Screen                                                 X          Also known as Microsoft Screen 3.
  Microsoft Expression Encoder Screen                                  X          Also known as Microsoft Titanium Screen 2.
  Microsoft RLE                                             X          X          
  Microsoft Screen 1                                                   X          Also known as Windows Media Video V7 Screen.
  Microsoft Screen 2                                                   X          Also known as Windows Media Video V9 Screen.
  Microsoft Video 1                                                    X          
  Mimic                                                                X          Used in MSN Messenger Webcam streams.
  Miro VideoXL                                                         X          fourcc: VIXL
  MJPEG (Motion JPEG)                                       X          X          
  Mobotix MxPEG video                                                  X          
  Motion Pixels video                                                  X          
  MPEG-1 video                                              X          X          
  MPEG-2 video                                              X          X          
  MPEG-4 part 2                                             X          X          libxvidcore can be used alternatively for encoding.
  MPEG-4 part 2 Microsoft variant version 1                            X          
  MPEG-4 part 2 Microsoft variant version 2                 X          X          
  MPEG-4 part 2 Microsoft variant version 3                 X          X          
  Newtek SpeedHQ                                            X          X          
  Nintendo Gamecube THP video                                          X          
  NotchLC                                                              X          
  NuppelVideo/RTjpeg                                                   X          Video encoding used in NuppelVideo files.
  On2 VP3                                                              X          still experimental
  On2 VP4                                                              X          fourcc: VP40
  On2 VP5                                                              X          fourcc: VP50
  On2 VP6                                                              X          fourcc: VP60,VP61,VP62
  On2 VP7                                                              X          fourcc: VP70,VP71
  VP8                                                       E          X          fourcc: VP80, encoding supported through external library libvpx
  VP9                                                       E          X          encoding supported through external library libvpx
  Pinnacle TARGA CineWave YUV16                                        X          fourcc: Y216
  Q-team QPEG                                                          X          fourccs: QPEG, Q1.0, Q1.1
  QuickTime 8BPS video                                                 X          
  QuickTime Animation (RLE) video                           X          X          fourcc: 'rle '
  QuickTime Graphics (SMC)                                  X          X          fourcc: 'smc '
  QuickTime video (RPZA)                                    X          X          fourcc: rpza
  R10K AJA Kona 10-bit RGB Codec                            X          X          
  R210 Quicktime Uncompressed RGB 10-bit                    X          X          
  Raw Video                                                 X          X          
  RealVideo 1.0                                             X          X          
  RealVideo 2.0                                             X          X          
  RealVideo 3.0                                                        X          still far from ideal
  RealVideo 4.0                                                        X          
  RealVideo 6.0                                                        X          
  Renderware TXD (TeXture Dictionary)                                  X          Texture dictionaries used by the Renderware Engine.
  RivaTuner Video                                                      X          fourcc: 'RTV1'
  RL2 video                                                            X          used in some games by Entertainment Software Partners
  ScreenPressor                                                        X          
  Screenpresso                                                         X          
  Screen Recorder Gold Codec                                           X          
  Sierra VMD video                                                     X          Used in Sierra VMD files.
  Silicon Graphics Motion Video Compressor 1 (MVC1)                    X          
  Silicon Graphics Motion Video Compressor 2 (MVC2)                    X          
  Silicon Graphics RLE 8-bit video                                     X          
  Smacker video                                                        X          Video encoding used in Smacker.
  SMPTE VC-1                                                           X          
  Snow                                                      X          X          experimental wavelet codec (fourcc: SNOW)
  Sony PlayStation MDEC (Motion DECoder)                               X          
  Sorenson Vector Quantizer 1                               X          X          fourcc: SVQ1
  Sorenson Vector Quantizer 3                                          X          fourcc: SVQ3
  Sunplus JPEG (SP5X)                                                  X          fourcc: SP5X
  TechSmith Screen Capture Codec                                       X          fourcc: TSCC
  TechSmith Screen Capture Codec 2                                     X          fourcc: TSC2
  Theora                                                    E          X          encoding supported through external library libtheora
  Tiertex Limited SEQ video                                            X          Codec used in DOS CD-ROM FlashBack game.
  Ut Video                                                  X          X          
  v210 QuickTime uncompressed 4:2:2 10-bit                  X          X          
  v308 QuickTime uncompressed 4:4:4                         X          X          
  v408 QuickTime uncompressed 4:4:4:4                       X          X          
  v410 QuickTime uncompressed 4:4:4 10-bit                  X          X          
  VBLE Lossless Codec                                                  X          
  vMix Video                                                           X          fourcc: 'VMX1'
  VMware Screen Codec / VMware Video                                   X          Codec used in videos captured by VMware.
  Westwood Studios VQA (Vector Quantized Animation) video              X          
  Windows Media Image                                                  X          
  Windows Media Video 7                                     X          X          
  Windows Media Video 8                                     X          X          
  Windows Media Video 9                                                X          not completely working
  Wing Commander III / Xan                                             X          Used in Wing Commander III .MVE files.
  Wing Commander IV / Xan                                              X          Used in Wing Commander IV.
  Winnov WNV1                                                          X          
  WMV7                                                      X          X          
  YAMAHA SMAF                                               X          X          
  Psygnosis YOP Video                                                  X          
  yuv4                                                      X          X          libquicktime uncompressed packed 4:2:0
  ZeroCodec Lossless Video                                             X          
  ZLIB                                                      X          X          part of LCL, encoder experimental
  Zip Motion Blocks Video                                   X          X          Encoder works only in PAL8.
  --------------------------------------------------------- ---------- ---------- --------------------------------------------------------------------------------

`X` means that the feature in that column (encoding / decoding) is supported.

`E` means that support is provided through an external library.

[]

### [2.4 Audio Codecs](#toc-Audio-Codecs) 

  ------------------------------------------------------------------ ---------- ---------- ---------------------------------------------------------------------------------------
  Name                                                               Encoding   Decoding   Comments
  8SVX exponential                                                              X          
  8SVX fibonacci                                                                X          
  AAC                                                                EX         X          encoding supported through internal encoder and external library libfdk-aac
  AAC+                                                               E          IX         encoding supported through external library libfdk-aac
  AC-3                                                               IX         IX         
  ACELP.KELVIN                                                                  X          
  ADPCM 4X Movie                                                                X          
  ADPCM Yamaha AICA                                                             X          
  ADPCM AmuseGraphics Movie                                                     X          
  ADPCM Argonaut Games                                               X          X          
  ADPCM CDROM XA                                                                X          
  ADPCM Creative Technology                                                     X          16 -\> 4, 8 -\> 4, 8 -\> 3, 8 -\> 2
  ADPCM Electronic Arts                                                         X          Used in various EA titles.
  ADPCM Electronic Arts Maxis CDROM XS                                          X          Used in Sim City 3000.
  ADPCM Electronic Arts R1                                                      X          
  ADPCM Electronic Arts R2                                                      X          
  ADPCM Electronic Arts R3                                                      X          
  ADPCM Electronic Arts XAS                                                     X          
  ADPCM G.722                                                        X          X          
  ADPCM G.726                                                        X          X          
  ADPCM IMA Acorn Replay                                                        X          
  ADPCM IMA AMV                                                      X          X          Used in AMV files
  ADPCM IMA Cunning Developments                                                X          
  ADPCM IMA Electronic Arts EACS                                                X          
  ADPCM IMA Electronic Arts SEAD                                                X          
  ADPCM IMA Funcom                                                              X          
  ADPCM IMA High Voltage Software ALP                                X          X          
  ADPCM IMA Mobiclip MOFLEX                                                     X          
  ADPCM IMA QuickTime                                                X          X          
  ADPCM IMA Simon & Schuster Interactive                             X          X          
  ADPCM IMA Ubisoft APM                                              X          X          
  ADPCM IMA Loki SDL MJPEG                                                      X          
  ADPCM IMA WAV                                                      X          X          
  ADPCM IMA Westwood                                                            X          
  ADPCM ISS IMA                                                                 X          Used in FunCom games.
  ADPCM IMA Dialogic                                                            X          
  ADPCM IMA Duck DK3                                                            X          Used in some Sega Saturn console games.
  ADPCM IMA Duck DK4                                                            X          Used in some Sega Saturn console games.
  ADPCM IMA Radical                                                             X          
  ADPCM IMA Xbox                                                                X          
  ADPCM Microsoft                                                    X          X          
  ADPCM MS IMA                                                       X          X          
  ADPCM Nintendo Gamecube AFC                                                   X          
  ADPCM Nintendo Gamecube DTK                                                   X          
  ADPCM Nintendo THP                                                            X          
  ADPCM Playstation                                                             X          
  ADPCM QT IMA                                                       X          X          
  ADPCM Sanyo                                                                   X          
  ADPCM SEGA CRI ADX                                                 X          X          Used in Sega Dreamcast games.
  ADPCM Shockwave Flash                                              X          X          
  ADPCM Sound Blaster Pro 2-bit                                                 X          
  ADPCM Sound Blaster Pro 2.6-bit                                               X          
  ADPCM Sound Blaster Pro 4-bit                                                 X          
  ADPCM VIMA                                                                    X          Used in LucasArts SMUSH animations.
  ADPCM Konami XMD                                                              X          
  ADPCM Westwood Studios IMA                                         X          X          Used in Westwood Studios games like Command and Conquer.
  ADPCM Yamaha                                                       X          X          
  ADPCM Zork                                                                    X          
  AMR-NB                                                             E          X          encoding supported through external library libopencore-amrnb
  AMR-WB                                                             E          X          encoding supported through external library libvo-amrwbenc
  Amazing Studio PAF Audio                                                      X          
  Apple lossless audio                                               X          X          QuickTime fourcc 'alac'
  aptX                                                               X          X          Used in Bluetooth A2DP
  aptX HD                                                            X          X          Used in Bluetooth A2DP
  ATRAC1                                                                        X          
  ATRAC3                                                                        X          
  ATRAC3+                                                                       X          
  ATRAC9                                                                        X          
  Bink Audio                                                                    X          Used in Bink and Smacker files in many games.
  Bonk audio                                                                    X          
  CELT                                                                          E          decoding supported through external library libcelt
  codec2                                                             E          E          en/decoding supported through external library libcodec2
  CRI HCA                                                                       X          
  Delphine Software International CIN audio                                     X          Codec used in Delphine Software International games.
  DFPWM                                                              X          X          
  Digital Speech Standard - Standard Play mode (DSS SP)                         X          
  Discworld II BMV Audio                                                        X          
  COOK                                                                          X          All versions except 5.1 are supported.
  DCA (DTS Coherent Acoustics)                                       X          X          supported extensions: XCh, XXCH, X96, XBR, XLL, LBR (partially)
  Dolby E                                                                       X          
  DPCM Cuberoot-Delta-Exact                                                     X          Used in few games.
  DPCM Gremlin                                                                  X          
  DPCM id RoQ                                                        X          X          Used in Quake III, Jedi Knight 2 and other computer games.
  DPCM Marble WADY                                                              X          
  DPCM Interplay                                                                X          Used in various Interplay computer games.
  DPCM Squareroot-Delta-Exact                                                   X          Used in various games.
  DPCM Sierra Online                                                            X          Used in Sierra Online game audio files.
  DPCM Sol                                                                      X          
  DPCM Xan                                                                      X          Used in Origin's Wing Commander IV AVI files.
  DPCM Xilam DERF                                                               X          
  DSD (Direct Stream Digital), least significant bit first                      X          
  DSD (Direct Stream Digital), most significant bit first                       X          
  DSD (Direct Stream Digital), least significant bit first, planar              X          
  DSD (Direct Stream Digital), most significant bit first, planar               X          
  DSP Group TrueSpeech                                                          X          
  DST (Direct Stream Transfer)                                                  X          
  DV audio                                                                      X          
  Enhanced AC-3                                                      X          X          
  EVRC (Enhanced Variable Rate Codec)                                           X          
  FLAC (Free Lossless Audio Codec)                                   X          IX         
  FTR Voice                                                                     X          
  G.723.1                                                            X          X          
  G.728                                                                         X          
  G.729                                                                         X          
  GSM                                                                E          X          encoding supported through external library libgsm
  GSM Microsoft variant                                              E          X          encoding supported through external library libgsm
  IAC (Indeo Audio Coder)                                                       X          
  iLBC (Internet Low Bitrate Codec)                                  E          EX         encoding and decoding supported through external library libilbc
  IMC (Intel Music Coder)                                                       X          
  Interplay ACM                                                                 X          
  LC3                                                                E          E          supported through external library liblc3
  MACE (Macintosh Audio Compression/Expansion) 6:1                              X          
  Marian's A-pac audio                                                          X          
  MI-SC4 (Micronas SC-4 Audio)                                                  X          
  MLP (Meridian Lossless Packing)                                    X          X          Used in DVD-Audio discs.
  Monkey's Audio                                                                X          
  MP1 (MPEG audio layer 1)                                                      IX         
  MP2 (MPEG audio layer 2)                                           IX         IX         encoding supported also through external library TwoLAME
  MP3 (MPEG audio layer 3)                                           E          IX         encoding supported through external library LAME, ADU MP3 and MP3onMP4 also supported
  MPEG-4 Audio Lossless Coding (ALS)                                            X          
  MPEG-H 3D Audio                                                               E          decoding supported through external library libmpeghdec
  MobiClip FastAudio                                                            X          
  Musepack SV7                                                                  X          
  Musepack SV8                                                                  X          
  Nellymoser Asao                                                    X          X          
  On2 AVC (Audio for Video Codec)                                               X          
  Opus                                                               E          X          encoding supported through external library libopus
  OSQ (Original Sound Quality)                                                  X          
  PCM A-law                                                          X          X          
  PCM mu-law                                                         X          X          
  PCM Archimedes VIDC                                                X          X          
  PCM signed 8-bit planar                                            X          X          
  PCM signed 16-bit big-endian planar                                X          X          
  PCM signed 16-bit little-endian planar                             X          X          
  PCM signed 24-bit little-endian planar                             X          X          
  PCM signed 32-bit little-endian planar                             X          X          
  PCM 32-bit floating point big-endian                               X          X          
  PCM 32-bit floating point little-endian                            X          X          
  PCM 64-bit floating point big-endian                               X          X          
  PCM 64-bit floating point little-endian                            X          X          
  PCM D-Cinema audio signed 24-bit                                   X          X          
  PCM signed 8-bit                                                   X          X          
  PCM signed 16-bit big-endian                                       X          X          
  PCM signed 16-bit little-endian                                    X          X          
  PCM signed 24-bit big-endian                                       X          X          
  PCM signed 24-bit little-endian                                    X          X          
  PCM signed 32-bit big-endian                                       X          X          
  PCM signed 32-bit little-endian                                    X          X          
  PCM signed 16/20/24-bit big-endian in MPEG-TS                                 X          
  PCM unsigned 8-bit                                                 X          X          
  PCM unsigned 16-bit big-endian                                     X          X          
  PCM unsigned 16-bit little-endian                                  X          X          
  PCM unsigned 24-bit big-endian                                     X          X          
  PCM unsigned 24-bit little-endian                                  X          X          
  PCM unsigned 32-bit big-endian                                     X          X          
  PCM unsigned 32-bit little-endian                                  X          X          
  PCM SGA                                                                       X          
  QCELP / PureVoice                                                             X          
  QDesign Music Codec 1                                                         X          
  QDesign Music Codec 2                                                         X          There are still some distortions.
  RealAudio 1.0 (14.4K)                                              X          X          Real 14400 bit/s codec
  RealAudio 2.0 (28.8K)                                                         X          Real 28800 bit/s codec
  RealAudio 3.0 (dnet)                                               IX         X          Real low bitrate AC-3 codec
  RealAudio Lossless                                                            X          
  RealAudio SIPR / ACELP.NET                                                    X          
  RK Audio (RKA)                                                                X          
  SBC (low-complexity subband codec)                                 X          X          Used in Bluetooth A2DP
  Shorten                                                                       X          
  Sierra VMD audio                                                              X          Used in Sierra VMD files.
  Smacker audio                                                                 X          
  SMPTE 302M AES3 audio                                              X          X          
  Sonic                                                              X          X          experimental codec
  Sonic lossless                                                     X          X          experimental codec
  Speex                                                              E          EX         supported through external library libspeex
  TAK (Tom's lossless Audio Kompressor)                                         X          
  True Audio (TTA)                                                   X          X          
  TrueHD                                                             X          X          Used in HD-DVD and Blu-Ray discs.
  TwinVQ (VQF flavor)                                                           X          
  VIMA                                                                          X          Used in LucasArts SMUSH animations.
  ViewQuest VQC                                                                 X          
  Vorbis                                                             E          X          A native but very primitive encoder exists.
  Voxware MetaSound                                                             X          
  Waveform Archiver                                                             X          
  WavPack                                                            X          X          
  Westwood Audio (SND1)                                                         X          
  Windows Media Audio 1                                              X          X          
  Windows Media Audio 2                                              X          X          
  Windows Media Audio Lossless                                                  X          
  Windows Media Audio Pro                                                       X          
  Windows Media Audio Voice                                                     X          
  Xbox Media Audio 1                                                            X          
  Xbox Media Audio 2                                                            X          
  ------------------------------------------------------------------ ---------- ---------- ---------------------------------------------------------------------------------------

`X` means that the feature in that column (encoding / decoding) is supported.

`E` means that support is provided through an external library.

`I` means that an integer-only version is available, too (ensures high performance on systems without hardware floating point support).

[]

### [2.5 Subtitle Formats](#toc-Subtitle-Formats) 

  --------------------- -------- ---------- ---------- ----------
  Name                  Muxing   Demuxing   Encoding   Decoding
  3GPP Timed Text                           X          X
  AQTitle                        X                     X
  DVB                   X        X          X          X
  DVB teletext                   X                     E
  DVD                   X        X          X          X
  JACOsub               X        X                     X
  MicroDVD              X        X                     X
  MPL2                           X                     X
  MPsub (MPlayer)                X                     X
  PGS                                                  X
  PJS (Phoenix)                  X                     X
  RealText                       X                     X
  SAMI                           X                     X
  Spruce format (STL)            X                     X
  SSA/ASS               X        X          X          X
  SubRip (SRT)          X        X          X          X
  SubViewer v1                   X                     X
  SubViewer                      X                     X
  TED Talks captions             X                     X
  TTML                  X                   X          
  VobSub (IDX+SUB)               X                     X
  VPlayer                        X                     X
  WebVTT                X        X          X          X
  XSUB                                      X          X
  --------------------- -------- ---------- ---------- ----------

`X` means that the feature is supported.

`E` means that support is provided through an external library.

[]

### [2.6 Network Protocols](#toc-Network-Protocols) 

  -------------- ---------
  Name           Support
  AMQP           E
  file           X
  FTP            X
  Gopher         X
  Gophers        X
  HLS            X
  HTTP           X
  HTTPS          X
  Icecast        X
  MMSH           X
  MMST           X
  pipe           X
  Pro-MPEG FEC   X
  RTMP           X
  RTMPE          X
  RTMPS          X
  RTMPT          X
  RTMPTE         X
  RTMPTS         X
  RTP            X
  SAMBA          E
  SCTP           X
  SFTP           E
  TCP            X
  TLS            X
  UDP            X
  ZMQ            E
  -------------- ---------

`X` means that the protocol is supported.

`E` means that support is provided through an external library.

[]

### [2.7 Input/Output Devices](#toc-Input_002fOutput-Devices) 

  ---------------------- ------- --------
  Name                   Input   Output
  ALSA                   X       X
  BKTR                   X       
  caca                           X
  DV1394                 X       
  Lavfi virtual device   X       
  Linux framebuffer      X       X
  JACK                   X       
  LIBCDIO                X       
  LIBDC1394              X       
  OpenAL                 X       
  OpenGL                         X
  OSS                    X       X
  PulseAudio             X       X
  SDL                            X
  Video4Linux2           X       X
  VfW capture            X       
  X11 grabbing           X       
  Win32 grabbing         X       
  ---------------------- ------- --------

`X` means that input/output is supported.

[]

### [2.8 Timecode](#toc-Timecode) 

  -------------- ------ -------
  Codec/format   Read   Write
  AVI            X      X
  DV             X      X
  GXF            X      X
  MOV            X      X
  MPEG1/2        X      X
  MXF            X      X
  -------------- ------ -------

This document was generated on *December 27, 2025* using [*makeinfo*](http://www.gnu.org/software/texinfo/).

[Hosting provided by [telepoint.bg](https://telepoint.bg)]