import textwrap

def wrap(string, max_width):
    string_re = textwrap.wrap(string,width=max_width)
    return "\n".join(string_re)

if __name__ == '__main__':
    string, max_width = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ', 4#input(), int(input())
    result = wrap(string, max_width)
    print(result)