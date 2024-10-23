import sys


# 유효한 명령어 목록 추가
VALID_COMMANDS = ['exit', 'echo', 'type']

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
        elif parsed_cmd['command'] == 'type':
            check_command(parsed_cmd['args'])
        else:
            print(f"{parsed_cmd['command']}: command not found")

def parse_command(cmd):
    parts = cmd.split(maxsplit=1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else '0' if command == 'exit' else ''
    return {'command': command, 'args': args}

# 'type' 명령어를 처리하는 함수 추가
def check_command(cmd):
    if cmd in VALID_COMMANDS:
        print(f"{cmd} is a shell builtin")
    else:
        print(f"{cmd}: not found")

if __name__ == "__main__":
    main()
