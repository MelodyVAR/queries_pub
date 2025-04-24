def print_heart():
    # 定义爱心的大小
    size = 6
    
    # 打印爱心的上半部分
    for x in range(size):
        for y in range(size+1):
            if (x == 0 and y % 3 != 0) or (x == 1 and y % 3 == 0) or (x - y == 2) or (x + y == 8):
                print('❤️', end=' ')
            else:
                print('  ', end=' ')
        print()
    
    # 打印爱心的下半部分
    for x in range(size-1):
        for y in range(size-x):
            print('❤️', end=' ')
        print()

if __name__ == '__main__':
    print('\033[91m')  # 设置红色文字
    print_heart()
    print('\033[0m')   # 重置颜色