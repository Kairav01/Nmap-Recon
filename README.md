# Nmap Network Reconnaissance & Automation Project

A hands-on cybersecurity portfolio project demonstrating automated network discovery, port scanning, and service version enumeration using **Python** and **Nmap**.

## Overview
This repository contains a Python-based automation script (`scanner.py`) designed to execute Nmap reconnaissance scans against authorized local targets, alongside comprehensive documentation breaking down scan mechanics, port states, and output analysis.

## Key Features
* **Automated Path Detection:** Automatically locates the Nmap executable across standard Windows installation directories.
* **Stealth & Service Enumeration:** Executes TCP SYN (`-sS`) and Service Version (`-sV`) scans via Python's `subprocess` module to identify active ports and running software.
* **Comprehensive Documentation:** Includes detailed guides explaining the Python codebase, Nmap command flags, and a line-by-line breakdown of raw scan outputs.

## Repository Contents
* `scanner.py` — Python wrapper script to run Nmap reconnaissance scans.
* `scanner_explanation.txt` — Line-by-line walkthrough of the Python automation code.
* `nmap_output_explanation.txt` — Detailed breakdown of how to read and interpret Nmap scan reports.
* `nmap_comprehensive_guide.txt` — Reference guide covering Nmap scan types, port states, and ethical guidelines.

## Disclaimer
*This project was created strictly for educational purposes and authorized home-lab testing. Never run network scans against systems or networks without explicit, written permission.*