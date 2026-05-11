#!/bin/bash

# Check if mamba exists, otherwise fallback to conda
PM="mamba"
if ! command -v mamba &> /dev/null; then
    PM="conda"
fi

echo "Using package manager: $PM"

# Create the environment (if it doesn't exist)
$PM create -n BigWig python=3.10 -y

# Install packages using the 'run' command or '-n' flag
$PM install -n BigWig -c conda-forge -c bioconda \
    ucsc-wigtobigwig \
    pygenometracks -y
