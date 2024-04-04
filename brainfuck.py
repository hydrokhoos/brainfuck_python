def run_brainfuck(code: str) -> str:
    cmds = ['>', '<', '+', '-', '.', '[', ']']
    code = list(filter(lambda c: c in cmds, code))
    tape = [0] * 30000
    ptr = 0
    pc = 0
    bracket_map = {}
    loop_stack = []
    output = ''

    # []のマッチング対応を作成
    for i, cmd in enumerate(code):
        if cmd == '[':
            loop_stack.append(i)
        elif cmd == ']':
            if len(loop_stack) == 0:
                raise SyntaxError("No matching '[' for ']'")
            start = loop_stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    if len(loop_stack) > 0:
        raise SyntaxError("No matching ']' for '['")

    while pc < len(code):
        cmd = code[pc]

        if cmd == '>':
            ptr += 1
        elif cmd == '<':
            ptr -= 1
        elif cmd == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif cmd == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif cmd == '.':
            output += chr(tape[ptr])
        elif cmd == '[':
            if tape[ptr] == 0:
                pc = bracket_map[pc]
        elif cmd == ']':
            if tape[ptr] != 0:
                pc = bracket_map[pc]

        pc += 1

    return output


if __name__ == '__main__':
    # Hello Worldを出力するBrainfuckプログラム
    bf_code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
    print(run_brainfuck(bf_code), end='')
