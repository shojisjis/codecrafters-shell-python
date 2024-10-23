import sys


def main():
    # Main loop
    while True:
        # Print the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()
        print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
