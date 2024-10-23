import sys
import os  # 이 줄을 추가합니다
import subprocess  # 이 줄을 추가합니다


# 유효한 명령어 목록 추가
VALID_COMMANDS = ['exit', 'echo', 'type']

def main():
    # PATH 환경 변수 가져오기
    path = os.environ.get('PATH', '')
    # print(f"현재 PATH 환경 변수: {path}")

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
        elif parsed_cmd['command'] == '':
            continue
        else:
            # 유효하지 않은 명령어 실행
            try:
                result = subprocess.run([parsed_cmd['command']] + parsed_cmd['args'].split(), 
                                        capture_output=True, text=True)
                print(result.stdout)
                if result.stderr:
                    print(result.stderr, file=sys.stderr)
            except FileNotFoundError:
                print(f"{parsed_cmd['command']}: command not found")

def parse_command(cmd):
    parts = cmd.split(maxsplit=1)
    if len(parts) == 0:
        return {'command': '', 'args': ''}
    command = parts[0]
    args = parts[1] if len(parts) > 1 else '0' if command == 'exit' else ''
    return {'command': command, 'args': args}

# 'type' 명령어를 처리하는 함수 추가
def check_command(cmd):
    if cmd in VALID_COMMANDS:
        print(f"{cmd} is a shell builtin")
    else:
        # PATH 환경 변수에서 명령어 찾기
        path_dirs = os.environ.get('PATH', '').split(os.pathsep)
        for dir in path_dirs:
            file_path = os.path.join(dir, cmd)
            if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
                print(f"{cmd} is {file_path}")
                return
        print(f"{cmd}: not found")

if __name__ == "__main__":
    main()
