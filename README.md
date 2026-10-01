# Web Security Lab

A beginner-friendly cybersecurity project focused on web security analysis and HTTP security headers.

## Project Overview

This project contains a Python-based security header checker that analyzes a website's HTTP response headers and reports whether common security headers are present or missing.

## Security Headers Checked

- Content-Security-Policy
- Strict-Transport-Security
- X-Content-Type-Options
- X-Frame-Options
- Referrer-Policy
- Permissions-Policy

## Features

- Accepts a website URL from the command line
- Automatically adds HTTPS when needed
- Checks common HTTP security headers
- Displays missing security controls
- Calculates a basic security header score
- Handles HTTP and connection errors

## Usage

Run the script using Python:

```bash
python security_headers_checker.py https://example.com
```

## Example Output

Scanning: https://example.com

HTTP Status: 200
------------------------------------------------------------
[-] Content-Security-Policy
    Missing: Helps protect against XSS and content injection attacks.

[-] Strict-Transport-Security
    Missing: Forces browsers to use HTTPS connections.

[-] X-Content-Type-Options
    Missing: Prevents MIME type sniffing.

[-] X-Frame-Options
    Missing: Helps prevent clickjacking attacks.

[-] Referrer-Policy
    Missing: Controls how much referrer information is shared.

[-] Permissions-Policy
    Missing: Controls access to browser features and APIs.

------------------------------------------------------------
Security Header Summary
Present: 0
Missing: 6
Basic Header Score: 0%

## Skills Practiced

- Python
- HTTP/HTTPS
- Web Security
- Security Headers
- Basic Vulnerability Analysis
- Error Handling

## Disclaimer

This project is intended for educational and defensive security purposes only.

Only test systems that you own or have permission to assess.

## Author

Enana Khalil  
Networks & Cybersecurity Student
