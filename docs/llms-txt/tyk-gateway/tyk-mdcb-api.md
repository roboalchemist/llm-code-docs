# Source: https://tyk.io/docs/tyk-mdcb-api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://tyk.io/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Tyk MDCB API

> Tyk MDCB API documentation. This page provides details on how to use the Tyk Multi Data Center Bridge (MDCB) API for monitoring connected Data Planes and accessing diagnostic data.

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

<ButtonLeft href="https://raw.githubusercontent.com/TykTechnologies/tyk-docs/refs/heads/production/swagger/nightly/mdcb-swagger.yml" color="green" content="Download Swagger" />

This API provides operations for monitoring Data Planes connected to MDCB and accessing diagnostic data.
It includes endpoints for retrieving connected data plane details, performing health checks,
and accessing Go's built-in pprof diagnostics for advanced performance profiling.

Built with [Mintlify](https://mintlify.com).
