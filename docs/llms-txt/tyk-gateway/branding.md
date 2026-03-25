# Source: https://tyk.io/docs/portal/customization/branding.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customize Branding in Developer Portal

> How to customize branding in developer portal

In this section we will explain how to apply your branding (styling - CSS) on the portal elements with your own colors and logo within minutes.

**Prerequisites**

* A Tyk Self-Managed [installation](/tyk-self-managed/install)
* A login for the portal admin app
* Access to your Tyk portal file system

## Changing Portal Logo

1. Access the file directory for the Developer portal
2. The default logo is located in `/themes/default/assets/images/` and is called `dev-portal-logo.svg`.
3. Replace the default image with your own, keeping the same file name and in `.svg` format, ensuring that `xmlns="http://www.w3.org/2000/svg"` is included within your `<svg>` tag.

   <Note>
     If you want to use different naming, path reference or extension, the code is `<img src="/assets/images/dev-portal-logo.svg">` and is found on line 6 from the `/themes/default/partials/footer.tmpl` template.
   </Note>

## Changing Brand Colors

Let’s now explain how to manage borders and change the colors of buttons, texts and backgrounds. The file we’ll be looking at is `/themes/default/assets/stylesheets/main.css` which contains some CSS variables that are used throughout the app. Let’s take a closer look.
You can apply some changes in the portal based on your preferences. For example, you can change the navigation background color, the text color and the different button theme colors. Furthermore, you can change table border color and radius.

If you want to change the navigation background color you need to edit the variable called `--tdp-nav-bg-color` Similarly other variables as you can see where/how each one is used:

<Note>
  `tdp` stands for Tyk Developer Portal
</Note>

### Background Colors

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/background-colors.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=03400b92c1471b71fec4e0686308987c" alt="Background Colour settings Tyk Enterprise Portal" width="512" height="116" data-path="img/dashboard/portal-management/enterprise-portal/background-colors.png" />

* `--tdp-nav-bg-color` navigation background color
* `--tdp-body-bg-color` App background color

### Text Colors

<img src="https://mintcdn.com/tyk/B97_xetnHOB2KQMe/img/dashboard/portal-management/enterprise-portal/text-colors.png?fit=max&auto=format&n=B97_xetnHOB2KQMe&q=85&s=220c8d1ddb5e03d8de3a3f6262605a9f" alt="Text Colour settings Tyk Enterprise Portal" width="508" height="148" data-path="img/dashboard/portal-management/enterprise-portal/text-colors.png" />

* `--tdp-text-color` default text color
* `--tdp-link-color` links (anchor tags)
* `--tdp-nav-link-color` navigation links

### Borders

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/borders.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=0285051b88ce33d6385fd0d943648e4f" alt="Border Colour settings Tyk Enterprise Portal" width="780" height="258" data-path="img/dashboard/portal-management/enterprise-portal/borders.png" />

* `--tdp-card-border-radius` Card component
* `--tdp-border-color-on-error` input color if there’s an error
* `--tdp-table-border-color` table
* `--tdp-border-radius` radius
* `--tdp-primary-border form` elements (such as `<input>` and `<select>`) if active
* `--tdp-form-element-border` form elements (such as `<input>` and `<select>`)

### Buttons

Buttons have four different concepts and each one of them has two or more variables:

<img src="https://mintcdn.com/tyk/RUEpCcfQ3zk4RxhB/img/dashboard/portal-management/enterprise-portal/buttons.png?fit=max&auto=format&n=RUEpCcfQ3zk4RxhB&q=85&s=bdf45bc3052deb2d3023e9286495036c" alt="Button Colour settings Tyk Enterprise Portal" width="876" height="400" data-path="img/dashboard/portal-management/enterprise-portal/buttons.png" />

**Primary**

* `--tdp-primary-btn-color` background color
* `--tdp-primary-btn-border` border color

**Secondary**

* `--tdp-secondary-btn-color` background color
* `--tdp-secondary-btn-border` border color

**Danger**

* `--tdp-danger-btn-color` background color
* `--tdp-danger-btn-border` border color
* `--tdp-danger-outline-btn-border` border color of the outline variation

**Warning**

* `--tdp-warning-btn-color` background color
* `--tdp-warning-btn-border` border color
* `--tdp-warning-outline-btn-border`  border color of the outline variation

Built with [Mintlify](https://mintlify.com).
