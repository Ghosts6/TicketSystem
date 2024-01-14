#!/bin/bash

echo "Stopping project..."
kill $(lsof -t -i:8000)
