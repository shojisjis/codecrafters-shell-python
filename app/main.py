import sys


def main():
    # Main loop
    while True:
        # Print the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # 사용자 입력 대기
        cmd = input()
        if cmd.startswith("exit"):
            exit_code = (cmd + " ").split(" ", 1)[1]
            sys.exit(int(exit_code.strip()))
        else:
            print(f"{cmd}: command not found")


if __name__ == "__main__":
    main()
