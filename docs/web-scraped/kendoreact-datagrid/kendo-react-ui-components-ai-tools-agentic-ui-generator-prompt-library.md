# Source: https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library

Title: React Agentic UI Generator Prompt Library - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library

Markdown Content:
New to KendoReact?[Start a free 30-day trial](https://www.telerik.com/try/kendo-react-ui)

[KendoReact Agentic UI Generator Prompt Library Premium](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#kendoreact-agentic-ui-generator-prompt-library)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Feb 26, 2026

Welcome to the KendoReact Agentic UI Generator Prompt Library.

The prompts provided here are intended and optimized for use with the KendoReact MCP Server tools, including the [Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started) and the specialized assistants. They can help you accelerate the creation and styling of modern web applications, from individual components to complete responsive pages and custom themes.

This collection of prompts is not exhaustive and the KendoReact team is constantly working on adding more prompts to the library.

> [Go straight to the prompts ⬇️](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#general-prompts)

[How to Use the Prompts](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#how-to-use-the-prompts)
-----------------------------------------------------------------------------------------------------------------------------------------------

The prompts in this library target the [Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started) using the main `#kendo_ui_generator` handle, individual assistant handles, or natural language descriptions. Make sure that you have [installed and enabled](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#quick-start) the Agentic UI Generator before attempting to run the prompts.

1.   Browse the prompt library to find a prompt that suits your needs.
2.   Copy the prompt text (including any handles like `#kendo_ui_generator` if needed) or use it as inspiration for your natural language description.
3.   (Optional) Customize the prompt as needed for your specific use case.

When modifying the prompts, make sure the changes comply with the [intended use](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#use-cases) and the [recommendations](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#best-practices) for the Agentic UI Generator.
4.   Start a new chat session and run the chosen prompt.

> Always double-check the code and solutions proposed by any AI-powered tool before applying them to your project.

[General Prompts](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#general-prompts)
---------------------------------------------------------------------------------------------------------------------------------

This section provides examples of common UI creation tasks using the Agentic UI Generator. Prefixing the prompts with the `#kendo_ui_generator` handle is optional, but including it ensures the main generator is explicitly invoked.

prompt

`I have created an empty application that now needs a login screen and an admin dashboard. Add a login form with email/password fields and validation using Kendo components. After successful login, redirect to an admin dashboard page featuring a sidebar menu and a main content area displaying key metrics and recent activity.`

prompt

`Create a new page using the existing top navigation and footer. In the middle, add 3 rows with 3 responsive columns each. The top row shows system health KPIs for CPU, memory, and error counts. The middle rows include a Log Stream panel, a Kendo Line Chart of API response times, and a Bar Chart of requests per service. The bottom row contains a Deployment History table, an Alerts panel, and a list of open tickets.`

prompt

`Create a responsive appointments dashboard in the schedule page using a 3x2 grid layout. The top row contains a kendo dropdown to filter appointments by doctor and a list of today's upcoming appointments. The middle row displays a month-view scheduler showing the filtered appointments. The bottom row shows a bar chart visualizing doctor occupancy rates and a pie chart showing appointment status distribution (completed, pending, canceled).`

prompt

`Create a product catalog page with a responsive CSS grid layout displaying product cards. Add a kendo toolbar with filtering options, and expandable detail view for each product that work seamlessly on mobile, tablet, and desktop.`

prompt

`Build a landing page similar to the automotive industry kendo ui template with a hero section, feature highlights, statistics, and a call-to-action section.`

prompt

`Add an employee directory page with a search bar and department filter at the top. Display employee details in a responsive grid layout showing names, titles, hiring dates. Include a TreeView on the left for navigating the organizational hierarchy. Add a Tooltip showing detailed employee information when a row in the Grid is hovered.`

prompt

`Create an event management interface with a Scheduler component as the main element displaying events in month, week, and day views. Add a top toolbar with view switcher, date navigation, and create event button. Include a sidebar showing upcoming events list and a small Calendar for quick date selection. Add filtering options for event types and venues.`

prompt

`Build a patient portal with a Card layout showing different sections: upcoming appointments with a ListView, current prescriptions Grid, recent lab results with expandable rows, and a messaging panel for communicating with healthcare providers. Add a top navigation with icons for appointments, records, billing, and messages. Include a notification Badge showing unread messages.`

prompt

`Build a patient portal with a Card layout showing different sections: upcoming appointments with a ListView, current prescriptions Grid, recent lab results with expandable rows, and a messaging panel for communicating with healthcare providers. Add a top navigation with icons for appointments, records, billing, and messages. Include a notification Badge showing unread messages.`

prompt

`Create an employee onboarding multi-step form with the following steps: personal info, job details, credentials, review. Step 1 shows a Form for name, email, and phone with user icon in the header. Step 2 displays department DropDownList and role selection with clipboard icon. Step 3 contains system access CheckBoxList and password setup with lock icon. Final step shows a summary Card with all entered information and a submit Button with checkmark icon.`

[Assistant-Specific Prompts](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#assistant-specific-prompts)
-------------------------------------------------------------------------------------------------------------------------------------------------------

This section provides prompt examples for directly calling individual specialized assistants for more granular control.

### [Layout Assistant](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#layout-assistant)

Use the `#kendo_layout_assistant` handle to structure your page layout and organize your UI elements:

prompt

`#kendo_layout_assistant Update the existing page layout by adding a new section in the middle of the page. In that added section, a Dashboard Card displays summary KPIs (revenue, active users, growth rate), next to a Compact Card showing a recent alert or message. Make the page responsive with proper spacing and typography.`

prompt

`#kendo_layout_assistant I have an existing carousel feature section that needs to be replaced with a responsive 3-column grid layout. Convert the carousel items into a grid that displays 3 columns on desktop, 2 columns on tablet, and 1 column on mobile with proper spacing and alignment.`

### [Component Assistant](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#component-assistant)

Use the `#kendo_component_assistant` handle for specific implementations that need the KendoReact components:

prompt

`#kendo_component_assistant Create a Grid component with paging, sorting, and filtering. Include column configuration for a product catalog with name, price, category, and actions. Ensure the Grid is properly integrated into a card layout with responsive design and consistent spacing.`

prompt

`#kendo_component_assistant Insert a new section with a Grid on the left to filter and sort product data. On the right, add a Chart and DateRangePicker to visualize product sales over time. Both components should be data-bound to the same source and reactively update based on the selected date range.`

### [Styling Assistant](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#styling-assistant)

Use the `#kendo_style_assistant` handle for custom themes and brand-specific styling:

prompt

`#kendo_style_assistant Generate custom CSS variables for a corporate blue and green color scheme with high contrast accessibility requirements.`

prompt

`#kendo_style_assistant Create a comprehensive dark mode theme with a dark background, light text, subtle border radius on cards and buttons, and increased spacing between the UI components.`

### [Icon Assistant](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#icon-assistant)

Use the `#kendo_icon_assistant` handle for finding and implementing suitable icons based on your scenario:

prompt

`#kendo_icon_assistant Add icons suitable for the Home, Settings, and User Profile buttons in my navigation bar.`

prompt

`#kendo_icon_assistant Find appropriate icons for data visualization actions like export, print, refresh, and search in a dashboard toolbar.`

### [Accessibility Assistant](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#accessibility-assistant)

Use the `#kendo_accessibility_assistant` handle to verify WCAG 2.2 Level AA compliance and implement proper accessibility features:

prompt

`#kendo_accessibility_assistant I have a Grid with a custom cell template that has multiple buttons like view report, download PDF, and send email. When I try to navigate with the keyboard, I can't get to these buttons properly. How can I make the keyboard navigation work for focusable elements inside the cell?`

prompt

`#kendo_accessibility_assistant I have a Grid that displays employee data where the first column contains employee names, followed by columns for department, salary, and hire date. How can I improve accessibility for screen reader users navigating this table?`

[See Also](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#see-also)
-------------------------------------------------------------------------------------------------------------------

*   [KendoReact MCP Server Overview](https://www.telerik.com/kendo-react-ui/components/ai-tools)
*   [KendoReact Agentic UI Generator Getting Started](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started)
*   [KendoReact Agentic UI Generator Intended Use](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#use-cases)
