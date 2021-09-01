from tns import TNS


def main():
    with TNS() as tns:
        tns.run()


if __name__ == "__main__":
    main()

