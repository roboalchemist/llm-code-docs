# Source: https://tyk.io/docs/dashboard-admin-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk Dashboard Admin API

> Tyk Dashboard Admin API documentation. This page provides details on how to use the Tyk Dashboard Admin API for setting up and provisioning a Tyk Dashboard instance.

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

<img src="https://tyk.io/docs/img/dashboard_admin_swagger_image.png" width="963" height="250" />

<ButtonLeft href="https://raw.githubusercontent.com/TykTechnologies/tyk-docs/refs/heads/production/swagger/nightly/dashboard-admin-swagger.yml" color="green" content="Download Swagger" />

For Tyk On-Premises installations only, the Dashboard Admin API has two endpoints and is used to set up and provision a Tyk Dashboard instance without the command line.

In order to use the Dashboard Admin API, you'll need to get the `admin_secret` value from your Tyk Dashboard configurations.

The secret you set should then be sent along as a header with each Dashboard Admin API Request in order for it to be successful:

```
admin-auth: <your-secret>
```


Built with [Mintlify](https://mintlify.com).