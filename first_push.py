import traceback


def main():
    print('Hello World')


if __name__ == '__main__':
    try:
        main()
    except:
        print(traceback.format_exc())
