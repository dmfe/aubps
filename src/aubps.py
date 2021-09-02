from tns import TNS
from gasnn import GASNN


def main():
    # with TNS() as tns:
        # tns.run()
    with GASNN() as gasnn:
        gasnn.run()


if __name__ == "__main__":
    main()

