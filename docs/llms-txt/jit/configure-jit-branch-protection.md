# Source: https://docs.jit.io/docs/configure-jit-branch-protection.md

# Configuring Branch Protection to work with Jit

How to troubleshoot Branch Protection

## Overview

Branch Protection in GitHub is a valuable best practice to ensure code quality and security.

However, specific branch protection settings can sometimes conflict with Jit’s functionality in the centralized configuration repository. Follow this guide to configure branch protection without disrupting Jit’s operations.

## Solution

To maintain branch protection while ensuring Jit operates without issues, add `Jit CI` to the `Bypass list` in GitHub’s Branch Protection settings.

This adjustment allows `Jit CI` to function smoothly at both the repository and organization levels, without compromising branch protection.

## Screenshots

Refer to the screenshots below for detailed steps on configuring the Bypass settings at the repository and organization levels.

### Repository

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e82cea4f42fbe70f6c48e563d4af66673b2894d40718378f5f0e281f1f95bc0e-BP-Bypass-repository.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

### Organization

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/167e3cf2de9c240c3f90103c3a37389f93850d019535411dcd2106fda8ece74e-BP-Bypass-organization.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]