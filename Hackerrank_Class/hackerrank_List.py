if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        inp = input().split()
        cmd = inp[0]
        if cmd == "insert":
            list.insert(inp[1],inp[2])
        elif cmd == "print":
            print(list)
        elif cmd == "remove":
            list.remove(inp[1])
        elif cmd == "append":
            list.append(inp[1])
        elif cmd == "sort":
            list.sort()
        elif cmd =="pop":
            list.pop()
        elif cmd == "reverse":
            list.reverse()