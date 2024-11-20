import argparse


from .Compressor import Compressor

class MiniMe:

    def __init__(self, *paths, to=None):
        """
        Used to init the compressor. Pass ``paths`` and ``to`` if the class is used in another file.
        :param paths: Paths file/directory to compress (ABSOLUTE PATH IS REQUIRED !)
        :param to: Destination path. Default : the first directory path given. If is a file, the destination is the directory file.
        """
        self.args: argparse.Namespace
        self.paths = paths
        self.to = to
        self.path_compressed_file: str = ''

    def _in_shell(self)->None:
        """
        Execute if the file is executed in a shell
        **ONLY EXECUTABLE**
        :return: None
        """

        parser = argparse.ArgumentParser(
            usage='Compress all files into a small file.',
            description='File compressor for windows')

        parser.add_argument("paths", action="extend", nargs='+', type=str,
                            help="Give all paths (directory of file) to compress")
        parser.add_argument("--to", "--t", action='store', type=str, default='',
                            help="Give the destination path. Default : the first directory path given. If is a file, the destination is the directory file.")

        self.args = parser.parse_args(["D:\PycharmProjects\Compresseur_fichiers\\test.txt"])
        print(self.args)

        self.path_compressed_file = Compressor().start_compressor(*self.args.paths, destination=self.args.to)

