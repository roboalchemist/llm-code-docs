# Source: https://developers.webflow.com/designer/reference/variables-overview.mdx

***

title: Variables & Collections
slug: designer/reference/variables-overview
description: >-
Learn how to create and manage variables and collections with the Designer
API.
hidden: false
'og:title': 'Webflow Designer API: Variables & Collections'
'og:description': >-
Learn how to create and manage variables and collections with the Designer
API.
----

Variables are reusable design tokens that let you [define and manage values across your Webflow projects](https://university.webflow.com/lesson/variables?topics=layout-design). They enable you to create a single source of truth for common values like colors, spacing, and typography. When you update a variable's value, that change automatically propagates everywhere the variable is used, making it easy to maintain consistency and make global design updates.

<video autoplay loop muted>
    

  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_Variables.webm" type="video/webm" />

    Your browser doesn't support HTML video.
</video>

# Variable collections

Variable collections provide an organizational structure for managing related variables. Collections enable you to group variables logically - for example, you might create separate collections for brand colors, typography, or spacing variables.

<a href="/designer/reference/variable-collections-overview">
  <button class="button cc-primary">
    Learn more about variable collections
  </button>
</a>

# Variables

Webflow supports five different types of variables, each with their own syntax for creating and updating them. Once you've created a variable, you can use it in your project by assigning it to a style property.

<CardGroup cols={3}>
  <Card
    title="Color"
    href="/designer/reference/create-color-variable"
    iconPosition="left"
    iconSize="10"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Variable.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Variable.svg" alt="" className="light-icon" />
      </>
    }
  >
    <p>
      Define colors.
    </p>
  </Card>

  <Card
    title="Size"
    href="/designer/reference/create-size-variable"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/GlobalCDN.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/GlobalCDN.svg" alt="" className="light-icon" />
      </>
    }
  >
    <p>
      Define sizes and spacing.
    </p>
  </Card>

  <Card
    title="Font"
    href="/designer/reference/create-font-family-variable"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Typography.svg" alt="" className="dark-icon" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Typography.svg" alt="" className="light-icon" />
      </>
    }
  >
    <p>
      Define fonts.
    </p>
  </Card>

  <Card
    title="Number"
    href="/designer/reference/create-number-variable"
    iconPosition="left"
    iconSize="7"
    icon={"fa-thin fa-hashtag"
    }
  >
    <p>
      Define number.
    </p>
  </Card>

  <Card
    title="Percentage"
    href="/designer/reference/create-percentage-variable"
    iconPosition="left"
    iconSize="7"
    icon={"fa-thin fa-percent"
    }
  >
    <p>
      Define percentages.
    </p>
  </Card>
</CardGroup>

<br />

<a href="/designer/reference/variables-detail-overview">
  <button class="button cc-primary">
    Learn more about variables
  </button>
</a>
