#!/usr/bin/env python3
import sys

def main():
    """The main entry point of the standalone program."""
    print("Hello, World!")
    
    # Example of accessing command-line arguments
    if len(sys.argv) > 1:
        print(f"Arguments passed: {sys.argv[1:]}")

if __name__ == "__main__":
    main()

