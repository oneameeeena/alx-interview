#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""
import sys
import signal


def print_stats(total_size, status_codes):
    """Print accumulated statistics"""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function to process log lines"""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    def signal_handler(sig, frame):
        """Handle keyboard interruption"""
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                if len(parts) < 7:
                    continue

                # Check format and extract status code and file size
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                # Update metrics
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += file_size

            except (ValueError, IndexError):
                continue

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        # Print final stats
        print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
