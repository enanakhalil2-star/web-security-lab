import sys
import urllib.request
import urllib.error


SECURITY_HEADERS = {
    "Content-Security-Policy": "Helps protect against XSS and content injection attacks.",
    "Strict-Transport-Security": "Forces browsers to use HTTPS connections.",
    "X-Content-Type-Options": "Prevents MIME type sniffing.",
    "X-Frame-Options": "Helps prevent clickjacking attacks.",
    "Referrer-Policy": "Controls how much referrer information is shared.",
    "Permissions-Policy": "Controls access to browser features and APIs.",
}


def normalize_url(url):
    if not url.startswith(("http://", "https://")):
        return "https://" + url
    return url


def check_security_headers(url):
    url = normalize_url(url)

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Web-Security-Lab/1.0"
        },
    )

    print(f"\nScanning: {url}\n")

    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers

            print(f"HTTP Status: {response.status}")
            print("-" * 60)

            present = 0
            missing = 0

            for header, description in SECURITY_HEADERS.items():
                value = headers.get(header)

                if value:
                    present += 1
                    print(f"[+] {header}")
                    print(f"    Value: {value}")
                else:
                    missing += 1
                    print(f"[-] {header}")
                    print(f"    Missing: {description}")

                print()

            print("-" * 60)
            print("Security Header Summary")
            print(f"Present: {present}")
            print(f"Missing: {missing}")

            score = int((present / len(SECURITY_HEADERS)) * 100)
            print(f"Basic Header Score: {score}%")

    except urllib.error.HTTPError as error:
        print(f"HTTP error: {error.code} {error.reason}")

    except urllib.error.URLError as error:
        print(f"Connection error: {error.reason}")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage:")
        print("python security_headers_checker.py https://example.com")
        sys.exit(1)

    check_security_headers(sys.argv[1])
