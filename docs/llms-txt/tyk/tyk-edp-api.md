# Source: https://tyk.io/docs/product-stack/tyk-enterprise-developer-portal/api-documentation/tyk-edp-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk Developer Portal API

> Tyk Developer Portal API documentation. This page provides details on how to use the Tyk Developer Portal Management API for managing portal resources.

export const ButtonLeft = ({href, color, content}) => {
  const buttonStyle = {
    display: 'inline-block',
    padding: '5px 16px',
    fontSize: '14px',
    fontWeight: '500',
    textDecoration: 'none',
    borderRadius: '25px',
    transition: 'all 0.2s ease',
    cursor: 'pointer',
    border: '1.2px solid black'
  };
  const colorStyles = {
    green: {
      backgroundColor: '#20EDBA',
      color: 'black'
    },
    red: {
      backgroundColor: '#dc2626',
      color: 'white'
    },
    black: {
      backgroundColor: '#1f2937',
      color: 'white'
    }
  };
  const hoverStyle = {
    transform: 'translateY(-1px)',
    boxShadow: '0 4px 8px rgba(0,0,0,0.15)'
  };
  const finalStyle = {
    ...buttonStyle,
    ...colorStyles[color] || colorStyles.black
  };
  return <a href={href} style={finalStyle} onMouseEnter={e => {
    Object.assign(e.target.style, hoverStyle);
  }} onMouseLeave={e => {
    e.target.style.transform = 'translateY(0)';
    e.target.style.boxShadow = 'none';
  }}>
      {content}
    </a>;
};

<img src="https://tyk.io/docs/img/developer_portal_swagger_image.png" width="963" height="250" />

<ButtonLeft href="https://raw.githubusercontent.com/TykTechnologies/tyk-docs/refs/heads/production/swagger/nightly/enterprise-developer-portal-swagger.yaml" color="green" content="Download Swagger" />

## <a name="introduction" /> Introduction

The Tyk Developer Portal Management API offers programmatic
access to all portal resources that your instance of the portal manages.
This API repeats functionality of the user interface and enables APIs
consumers integrating their portal instances with their other IT systems
such as billings, CRMs, ITSM systems and other software.

## Authentication

This API requires an admin authorisation token that is available for admin
users of the portal in the profile page.


Built with [Mintlify](https://mintlify.com).