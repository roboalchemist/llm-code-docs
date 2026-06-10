#!/bin/bash
# Stop TEI embedding servers
sudo docker rm -f tei-gpu4 tei-gpu5 2>/dev/null
echo "TEI servers stopped."
