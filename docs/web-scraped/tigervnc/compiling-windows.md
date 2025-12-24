# Source: https://github.com/TigerVNC/tigervnc/wiki/Compiling-TigerVNC-for-Windows

# Using MSYS2 and Mingw-w64 to compile TigerVNC 64 bit on Windows 10 64 bit 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#using-msys2-and-mingw-w64-to-compile-tigervnc-64-bit-on-windows-10-64-bit)

Last Updated: 30 June 2020

*This wiki was initially started because at least one developer realized there was no straight forward approach to get TigerVNC compiling for Windows and test contributions to the project. Feel free to update this with new and/or better information.*

## Install MSYS2 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#install-msys2)

MSYS2 is a self proclaimed \"software distro and building platform for Windows\". Please go to their website [https://www.msys2.org/](https://www.msys2.org/), download the one click installer and run it.

## Install prerequisite packages 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#install-prerequisite-packages)

`pacman -S mingw-w64-x86_64-cmake`

`pacman -S mingw-w64-x86_64-fltk`

`pacman -S mingw-w64-x86_64-gnutls`

`pacman -S mingw-w64-x86_64-gcc`

`pacman -S mingw-w64-x86_64-make`

`pacman -S mingw-w64-x86_64-pixman`

## Clone the TigerVNC project 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#clone-the-tigervnc-project)

`git clone https://github.com/TigerVNC/tigervnc.git`

`git checkout -b build_windows 38726ce083db1a9227325bf87989513499bfa698`

## Patch TigerVNC 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#patch-tigervnc)

*Work in process to get necessary changes incorporated into the main branch. See pull request #1039 (<https://github.com/TigerVNC/tigervnc/pull/1039>) for the first changes to be incorporated. The patch here is a temporary fix.*

Patch for including dll\'s in the installer:

From: Danny Park <danny.park@outlook.com>
Date: Tue, 9 Jun 2020 13:37:30 -0400
Subject: [PATCH] Include required dll's in the installer.

---
 cmake/BuildPackages.cmake |  7 +++++++
 release/tigervnc.iss.in   | 36 ++++++++++++++++++++++++++++++++----
 2 files changed, 39 insertions(+), 4 deletions(-)

diff --git a/cmake/BuildPackages.cmake b/cmake/BuildPackages.cmake
index 1f251929..9923e12d 100644
--- a/cmake/BuildPackages.cmake
+++ b/cmake/BuildPackages.cmake
@@ -8,6 +8,9 @@
 
 if(WIN32)
 
+find_path(TEMP_PATH libunistring-2.dll)
+set(WIN_DLL_PATH \"$\" CACHE PATH \"Path where Windows DLL files are located for installer.\")
+
 if(CMAKE_SIZEOF_VOID_P MATCHES 8)
   set(INST_NAME $64-$)
   set(INST_DEFS -DWIN64)
@@ -25,6 +28,10 @@ if(BUILD_WINVNC)
   set(INST_DEPS $ winvnc4 wm_hooks vncconfig)
 endif()
 
+if(ENABLE_GNUTLS)
+  set(INST_DEFS $ -DENABLE_GNUTLS)
+endif()
+
 configure_file(release/tigervnc.iss.in release/tigervnc.iss)
 
 add_custom_target(installer
diff --git a/release/tigervnc.iss.in b/release/tigervnc.iss.in
index 58501488..67dfb36e 100644
--- a/release/tigervnc.iss.in
+++ b/release/tigervnc.iss.in
@@ -24,10 +24,38 @@ LicenseFile=@CMAKE_SOURCE_DIR@\\LICENCE.txt
 Name: \"\\config\\systemprofile\\Desktop\"
 
 [Files]
+#ifndef BUILD_STATIC
+Source: \"@WIN_DLL_PATH@/libintl-8.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libiconv-2.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/mgwfltknox-1.3.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/zlib1.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libjpeg-8.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libgcc_s_seh-1.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libstdc++-6.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libwinpthread-1.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libpixman-1-0.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+#ifdef ENABLE_GNUTLS
+Source: \"@WIN_DLL_PATH@/libffi-7.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libgmp-10.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libgnutls-30.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libhogweed-6.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libidn2-0.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libnettle-8.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libp11-kit-0.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libtasn1-6.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libunistring-2.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+#endif
+#else
+Source: \"@WIN_DLL_PATH@/libffi-7.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libp11-kit-0.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libunistring-2.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libintl-8.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@WIN_DLL_PATH@/libiconv-2.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+#endif
 #ifdef BUILD_WINVNC
-Source: \"@CMAKE_CURRENT_BINARY_DIR@\\win\\winvnc\\winvnc4.exe\"; DestDir: \"\"; Flags: ignoreversion restartreplace; 
-Source: \"@CMAKE_CURRENT_BINARY_DIR@\\win\\wm_hooks\\wm_hooks.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace; 
-Source: \"@CMAKE_CURRENT_BINARY_DIR@\\win\\vncconfig\\vncconfig.exe\"; DestDir: \"\"; Flags: ignoreversion restartreplace; 
+Source: \"@CMAKE_CURRENT_BINARY_DIR@\\win\\winvnc\\winvnc4.exe\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@CMAKE_CURRENT_BINARY_DIR@\\win\\wm_hooks\\wm_hooks.dll\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
+Source: \"@CMAKE_CURRENT_BINARY_DIR@\\win\\vncconfig\\vncconfig.exe\"; DestDir: \"\"; Flags: ignoreversion restartreplace;
 #endif
 Source: \"@CMAKE_CURRENT_BINARY_DIR@\\vncviewer\\vncviewer.exe\"; DestDir: \"\"; Flags: ignoreversion restartreplace; 
 Source: \"@CMAKE_SOURCE_DIR@\\README.rst\"; DestDir: \"\"; Flags: ignoreversion
@@ -54,7 +82,7 @@ Name: \"\\Uninstall TigerVNC\"; FileName: \"\"; WorkingDir: \"
``` notranslate
From dc51216a0ffb3b044ab24966dec5212d49e17a4e Mon Sep 17 00:00:00 2001
From: Danny Park <danny.park@outlook.com>
Date: Tue, 9 Jun 2020 13:37:30 -0400
Subject: [PATCH] Include required dll's in the installer.

---
 cmake/BuildPackages.cmake |  7 +++++++
 release/tigervnc.iss.in   | 36 ++++++++++++++++++++++++++++++++----
 2 files changed, 39 insertions(+), 4 deletions(-)

diff --git a/cmake/BuildPackages.cmake b/cmake/BuildPackages.cmake
index 1f251929..9923e12d 100644
--- a/cmake/BuildPackages.cmake
+++ b/cmake/BuildPackages.cmake
@@ -8,6 +8,9 @@
 
 if(WIN32)
 
+find_path(TEMP_PATH libunistring-2.dll)
+set(WIN_DLL_PATH "$" CACHE PATH "Path where Windows DLL files are located for installer.")
+
 if(CMAKE_SIZEOF_VOID_P MATCHES 8)
   set(INST_NAME $64-$)
   set(INST_DEFS -DWIN64)
@@ -25,6 +28,10 @@ if(BUILD_WINVNC)
   set(INST_DEPS $ winvnc4 wm_hooks vncconfig)
 endif()
 
+if(ENABLE_GNUTLS)
+  set(INST_DEFS $ -DENABLE_GNUTLS)
+endif()
+
 configure_file(release/tigervnc.iss.in release/tigervnc.iss)
 
 add_custom_target(installer
diff --git a/release/tigervnc.iss.in b/release/tigervnc.iss.in
index 58501488..67dfb36e 100644
--- a/release/tigervnc.iss.in
+++ b/release/tigervnc.iss.in
@@ -24,10 +24,38 @@ LicenseFile=@CMAKE_SOURCE_DIR@\LICENCE.txt
 Name: "\config\systemprofile\Desktop"
 
 [Files]
+#ifndef BUILD_STATIC
+Source: "@WIN_DLL_PATH@/libintl-8.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libiconv-2.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/mgwfltknox-1.3.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/zlib1.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libjpeg-8.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libgcc_s_seh-1.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libstdc++-6.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libwinpthread-1.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libpixman-1-0.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+#ifdef ENABLE_GNUTLS
+Source: "@WIN_DLL_PATH@/libffi-7.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libgmp-10.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libgnutls-30.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libhogweed-6.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libidn2-0.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libnettle-8.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libp11-kit-0.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libtasn1-6.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libunistring-2.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+#endif
+#else
+Source: "@WIN_DLL_PATH@/libffi-7.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libp11-kit-0.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libunistring-2.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libintl-8.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@WIN_DLL_PATH@/libiconv-2.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+#endif
 #ifdef BUILD_WINVNC
-Source: "@CMAKE_CURRENT_BINARY_DIR@\win\winvnc\winvnc4.exe"; DestDir: ""; Flags: ignoreversion restartreplace; 
-Source: "@CMAKE_CURRENT_BINARY_DIR@\win\wm_hooks\wm_hooks.dll"; DestDir: ""; Flags: ignoreversion restartreplace; 
-Source: "@CMAKE_CURRENT_BINARY_DIR@\win\vncconfig\vncconfig.exe"; DestDir: ""; Flags: ignoreversion restartreplace; 
+Source: "@CMAKE_CURRENT_BINARY_DIR@\win\winvnc\winvnc4.exe"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@CMAKE_CURRENT_BINARY_DIR@\win\wm_hooks\wm_hooks.dll"; DestDir: ""; Flags: ignoreversion restartreplace;
+Source: "@CMAKE_CURRENT_BINARY_DIR@\win\vncconfig\vncconfig.exe"; DestDir: ""; Flags: ignoreversion restartreplace;
 #endif
 Source: "@CMAKE_CURRENT_BINARY_DIR@\vncviewer\vncviewer.exe"; DestDir: ""; Flags: ignoreversion restartreplace; 
 Source: "@CMAKE_SOURCE_DIR@\README.rst"; DestDir: ""; Flags: ignoreversion
@@ -54,7 +82,7 @@ Name: "\Uninstall TigerVNC"; FileName: ""; WorkingDir: "

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#create-a-build-directory-in-the-tigervnc-repo)

Start MSYS2-MinGW 64 bit

`cd tigervnc`

`mkdir build`

`cd build`

## Configure the build environment and run it 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#configure-the-build-environment-and-run-it)

`cmake -G "MinGW Makefiles" ../`

`mingw32-make.exe`

## Create the Windows Installer 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#create-the-windows-installer)

Creating the installer requires the above `cmake -G "MinGW Makefiles" ../` command.

Install Inno Setup 6 from [https://jrsoftware.org/isinfo.php](https://jrsoftware.org/isinfo.php). (any time before running `mingw32-make.exe installer`).

Add the path to your MinGW 64-bit path. This only changes your path for the current terminal session. This needs to be run every time before the installer is created.

`export PATH=/c/Program\ Files\ \(x86\)/Inno\ Setup\ 6/:$PATH`

Create the installer.

`mingw32-make.exe installer`

## Note for compatibility with Windows 7 

[![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0ib2N0aWNvbiBvY3RpY29uLWxpbmsiIHZpZXdib3g9IjAgMCAxNiAxNiIgdmVyc2lvbj0iMS4xIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48cGF0aCBkPSJtNy43NzUgMy4yNzUgMS4yNS0xLjI1YTMuNSAzLjUgMCAxIDEgNC45NSA0Ljk1bC0yLjUgMi41YTMuNSAzLjUgMCAwIDEtNC45NSAwIC43NTEuNzUxIDAgMCAxIC4wMTgtMS4wNDIuNzUxLjc1MSAwIDAgMSAxLjA0Mi0uMDE4IDEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwyLjUtMi41YTIuMDAyIDIuMDAyIDAgMCAwLTIuODMtMi44M2wtMS4yNSAxLjI1YS43NTEuNzUxIDAgMCAxLTEuMDQyLS4wMTguNzUxLjc1MSAwIDAgMS0uMDE4LTEuMDQyWm0tNC42OSA5LjY0YTEuOTk4IDEuOTk4IDAgMCAwIDIuODMgMGwxLjI1LTEuMjVhLjc1MS43NTEgMCAwIDEgMS4wNDIuMDE4Ljc1MS43NTEgMCAwIDEgLjAxOCAxLjA0MmwtMS4yNSAxLjI1YTMuNSAzLjUgMCAxIDEtNC45NS00Ljk1bDIuNS0yLjVhMy41IDMuNSAwIDAgMSA0Ljk1IDAgLjc1MS43NTEgMCAwIDEtLjAxOCAxLjA0Mi43NTEuNzUxIDAgMCAxLTEuMDQyLjAxOCAxLjk5OCAxLjk5OCAwIDAgMC0yLjgzIDBsLTIuNSAyLjVhMS45OTggMS45OTggMCAwIDAgMCAyLjgzWiI+PC9wYXRoPjwvc3ZnPg==)](#note-for-compatibility-with-windows-7)

Apparently the windows kernel32.dll exports a reference to CreateProcessAsUserA in Windows 10 but not in Windows 7. The libkernel32.a for newer versions of crt-git contain that export. That causes a runtime error in Windows 7. Version 6 does not have that reference so it properly links to advapi32.dll for Windows 7.

If you want a binary that is compatible with Windows 7, download mingw-w64-x86_64-crt-git-6.0.0.5225.fb06a4bf-1-any.pkg.tar.xz from [http://repo.msys2.org/mingw/x86_64/](http://repo.msys2.org/mingw/x86_64/) and then install it with the following command:

`pacman -U mingw-w64-x86_64-crt-git-6.0.0.5225.fb06a4bf-1-any.pkg.tar.xz`

The wiki is read-only because of malware spam that GitHub refuses to provide protection agains. Contact the maintainers directly with changes you\'d like to make.