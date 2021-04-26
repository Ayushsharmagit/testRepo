import traceback


def tempFunc():
    pass


def main():
    print('Seecond File')


if __name__ == '__main__':
    try:
        main()
    except:
        print(traceback.format_exc())
