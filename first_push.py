import traceback


def main():
    print('Hello World')
    print("Ayush")


if __name__ == '__main__':
    try:
        main()
    except:
        print(traceback.format_exc())
