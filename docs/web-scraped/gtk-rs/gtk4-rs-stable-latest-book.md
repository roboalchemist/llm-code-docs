# Source: https://gtk-rs.org/gtk4-rs/stable/latest/book

Title: GUI development with Rust and GTK 4

URL Source: https://gtk-rs.org/gtk4-rs/stable/latest/book

Markdown Content:
Keyboard shortcuts
------------------

Press ← or → to navigate between chapters

Press S or / to search in the book

Press ? to show this help

Press Esc to hide this help

1.   [Introduction](https://gtk-rs.org/gtk4-rs/stable/latest/book/introduction.html)

    1.   [Who this book is for](https://gtk-rs.org/gtk4-rs/stable/latest/book#who-this-book-is-for)
    2.   [How to use this book](https://gtk-rs.org/gtk4-rs/stable/latest/book#how-to-use-this-book)
    3.   [Translations](https://gtk-rs.org/gtk4-rs/stable/latest/book#translations)
    4.   [License](https://gtk-rs.org/gtk4-rs/stable/latest/book#license)

2.   [**1.** Installation](https://gtk-rs.org/gtk4-rs/stable/latest/book/installation.html)
    1.   [**1.1.** Linux](https://gtk-rs.org/gtk4-rs/stable/latest/book/installation_linux.html)
    2.   [**1.2.** macOS](https://gtk-rs.org/gtk4-rs/stable/latest/book/installation_macos.html)
    3.   [**1.3.** Windows](https://gtk-rs.org/gtk4-rs/stable/latest/book/installation_windows.html)

3.   [**2.** Project Setup](https://gtk-rs.org/gtk4-rs/stable/latest/book/project_setup.html)
4.   [**3.** Hello World!](https://gtk-rs.org/gtk4-rs/stable/latest/book/hello_world.html)
5.   [**4.** Widgets](https://gtk-rs.org/gtk4-rs/stable/latest/book/widgets.html)
6.   [**5.** GObject Concepts](https://gtk-rs.org/gtk4-rs/stable/latest/book/g_object_concepts.html)
    1.   [**5.1.** Memory Management](https://gtk-rs.org/gtk4-rs/stable/latest/book/g_object_memory_management.html)
    2.   [**5.2.** Subclassing](https://gtk-rs.org/gtk4-rs/stable/latest/book/g_object_subclassing.html)
    3.   [**5.3.** Generic Values](https://gtk-rs.org/gtk4-rs/stable/latest/book/g_object_values.html)
    4.   [**5.4.** Properties](https://gtk-rs.org/gtk4-rs/stable/latest/book/g_object_properties.html)
    5.   [**5.5.** Signals](https://gtk-rs.org/gtk4-rs/stable/latest/book/g_object_signals.html)

7.   [**6.** The Main Event Loop](https://gtk-rs.org/gtk4-rs/stable/latest/book/main_event_loop.html)
8.   [**7.** Settings](https://gtk-rs.org/gtk4-rs/stable/latest/book/settings.html)
9.   [**8.** Saving Window State](https://gtk-rs.org/gtk4-rs/stable/latest/book/saving_window_state.html)
10.   [**9.** List Widgets](https://gtk-rs.org/gtk4-rs/stable/latest/book/list_widgets.html)
11.   [**10.** Composite Templates](https://gtk-rs.org/gtk4-rs/stable/latest/book/composite_templates.html)
12.   [**11.** Building a Simple To-Do App](https://gtk-rs.org/gtk4-rs/stable/latest/book/todo_1.html)
13.   [**12.** Actions](https://gtk-rs.org/gtk4-rs/stable/latest/book/actions.html)
14.   [**13.** Manipulating State of To-Do App](https://gtk-rs.org/gtk4-rs/stable/latest/book/todo_2.html)
15.   [**14.** CSS](https://gtk-rs.org/gtk4-rs/stable/latest/book/css.html)
16.   [**15.** Libadwaita](https://gtk-rs.org/gtk4-rs/stable/latest/book/libadwaita.html)
    1.   [**15.1.** Let To-Do App use Libadwaita](https://gtk-rs.org/gtk4-rs/stable/latest/book/todo_3.html)
    2.   [**15.2.** Adding Collections](https://gtk-rs.org/gtk4-rs/stable/latest/book/todo_4.html)

17.   [**16.** Building with Meson](https://gtk-rs.org/gtk4-rs/stable/latest/book/meson.html)
18.   [**17.** Internationalization](https://gtk-rs.org/gtk4-rs/stable/latest/book/i18n.html)

[GUI development with Rust and GTK 4](https://gtk-rs.org/gtk4-rs/stable/latest/book#gui-development-with-rust-and-gtk-4)
------------------------------------------------------------------------------------------------------------------------

_by Julian Hofer, with contributions from the community_

GTK 4 is the newest version of a popular cross-platform widget toolkit written in C. Thanks to GObject-Introspection, GTK’s API can be easily targeted by various programming languages. The API even describes the ownership of its parameters!

Managing ownership without giving up speed is one of Rust’s greatest strengths, which makes it an excellent choice to develop GTK apps with. With this combination you don’t have to worry about hitting bottlenecks mid-project anymore. Additionally, with Rust you will have nice things such as

*   thread safety,
*   memory safety,
*   sensible dependency management as well as
*   excellent third party libraries.

The [`gtk-rs`](https://gtk-rs.org/) project provides bindings to many GTK-related libraries which we will be using throughout this book.

[Who this book is for](https://gtk-rs.org/gtk4-rs/stable/latest/book#who-this-book-is-for)
------------------------------------------------------------------------------------------

This book assumes that you know your way around Rust code. If this is not already the case, reading [The Rust Programming Language](https://doc.rust-lang.org/stable/book/) is an enjoyable way to get you to that stage. If you have experience with another low-level language such as C or C++ you might find that reading [A half hour to learn Rust](https://fasterthanli.me/articles/a-half-hour-to-learn-rust) gives you sufficient information as well.

Luckily, this — together with the wish to develop graphical applications — is all that is necessary to benefit from this book.

[How to use this book](https://gtk-rs.org/gtk4-rs/stable/latest/book#how-to-use-this-book)
------------------------------------------------------------------------------------------

In general, this book assumes that you are reading it in sequence from front to back. However, if you are using it as a reference for a certain topic, you might find it useful to just jump into it.

There are two kinds of chapters in this book: concept chapters and project chapters. In concept chapters, you will learn about an aspect of GTK development. In project chapters, we will build small programs together, applying what you’ve learned so far.

The book strives to explain essential GTK concepts paired with practical examples. However, if a concept can be better conveyed with a less practical example, we took this path most of the time. If you are interested in contained and useful examples, we refer you to the corresponding section of `gtk4-rs`’ [repository](https://github.com/gtk-rs/gtk4-rs/tree/main/examples).

Every valid code snippet in the book is part of a listing. Like the examples, the listings be found in the [repository](https://github.com/gtk-rs/gtk4-rs/tree/main/book/listings) of `gtk4-rs`.

[Translations](https://gtk-rs.org/gtk4-rs/stable/latest/book#translations)
--------------------------------------------------------------------------

This book has been translated to Chinese by 陈竞阁 and is served under the following [website](https://mario-hero.github.io/gtk-book-zh_cn/).

[License](https://gtk-rs.org/gtk4-rs/stable/latest/book#license)
----------------------------------------------------------------

The book itself is licensed under the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/). The only exception are the code snippets which are licensed under the [MIT license](https://github.com/gtk-rs/gtk4-rs/blob/main/README.md).

[](https://gtk-rs.org/gtk4-rs/stable/latest/book/installation.html "Next chapter")

[](https://gtk-rs.org/gtk4-rs/stable/latest/book/installation.html "Next chapter")
