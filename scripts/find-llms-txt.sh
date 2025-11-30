#!/bin/bash
# find-llms-txt.sh - Probe a domain for llms.txt files
# Usage: ./find-llms-txt.sh example.com
#
# Checks common subdomain + path combinations to find llms.txt files

DOMAIN="${1:?Usage: $0 domain.com}"
DOMAIN="${DOMAIN#https://}"
DOMAIN="${DOMAIN#http://}"
DOMAIN="${DOMAIN%%/*}"

SUBDOMAINS=("" "www." "docs." "developers." "developer." "api." "dev.")
PATHS=("/llms.txt" "/llms-full.txt" "/docs/llms.txt" "/docs/llms-full.txt" "/.well-known/llms.txt")

echo "Checking llms.txt locations for: $DOMAIN"
echo "---"

found=0
for sub in "${SUBDOMAINS[@]}"; do
  for path in "${PATHS[@]}"; do
    url="https://${sub}${DOMAIN}${path}"
    status=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 3 -m 5 -L "$url")
    if [[ "$status" == "200" ]]; then
      echo "✓ FOUND: $url"
      ((found++))
    fi
  done
done

echo "---"
if [[ $found -eq 0 ]]; then
  echo "No llms.txt found for $DOMAIN"
  exit 1
else
  echo "Found $found llms.txt location(s)"
  exit 0
fi
