# Source: https://cobra.dev/docs/tutorials/first-cli/

Title: My First CLI

URL Source: https://cobra.dev/docs/tutorials/first-cli/

Markdown Content:
Welcome to the “My First CLI” tutorial! In this guide, you will learn how to create a simple Command-Line Interface (CLI) application using Cobra.

Prerequisites
-------------

*   Basic knowledge of Go programming language.
*   Go installed on your system.

Steps
-----

1.   **Install Cobra**

First, initialize a new Go module for your project:

`mkdir my-cli``cd my-cli``go mod init my-cli` 
Then install the Cobra library:

`go get -u github.com/spf13/cobra@latest` 
2.   **Initialize Your Project**

Install the Cobra CLI generator:

`go install github.com/spf13/cobra-cli@latest` 
Initialize your Cobra project:

`cobra-cli init``Your Cobra application is ready at``/path/to/my-cli` 
3.   **Add Commands**

Add a new command to your CLI:

`cobra-cli add serve``serve created at /path/to/my-cli` 
4.   **Run Your CLI**

Build and test your CLI application:

`go build -o my-cli``./my-cli``A longer description that spans multiple lines and likely contains``examples and usage of using your command. For example:``Cobra is a CLI library for Go that empowers applications.``This application is a tool to generate the needed files``to quickly create a Cobra application.` 
Test the new serve command:

`./my-cli serve``serve called` 

Summary
-------

By the end of this tutorial, you will have a working CLI application built with Cobra. Stay tuned for more advanced tutorials!
