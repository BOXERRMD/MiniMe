import argparse

class MiniMe:

    def __init__(self):
        self.args: argparse.Namespace

    def main(self):

        parser = argparse.ArgumentParser(
            usage='Compress all files into a small file.',
            description='File compressor for windows')

        parser.add_argument("path", action="extend", nargs='+', type=str,
                            help="Give all paths (directory of file) to compress")
        parser.add_argument("--to", "--t", action='store', type=str,
                            help="Give the destination path. Default : the first directory path given. If is a file, the destination is the directory file.")

        self.args = parser.parse_args()



if __name__ == '__main__':
    C = MiniMe()
    C.main()
