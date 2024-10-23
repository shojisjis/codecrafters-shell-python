import sys


def main():
    # Main loop
    while True:
        # Print the prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # 사용자 입력 대기
        cmd = input()
        parsed_cmd = parse_command(cmd)
        if parsed_cmd['command'] == 'exit':
            sys.exit(int(parsed_cmd['args']))
        elif parsed_cmd['command'] == 'echo':
            print(parsed_cmd['args'])
        else:
            print(f"{parsed_cmd['command']}: command not found")

def parse_command(cmd):
    parts = cmd.split(maxsplit=1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ''
    return {'command': command, 'args': args}


if __name__ == "__main__":
    main()
