from moduller import *
import configparser
import sys
import argparse

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Type \"python predict.py help\" for help")
        exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="the path to the input file")
    parser.add_argument("-s", "--seq", help="raw sequence of amino acid sequence (don't use with -p)")
    parser.add_argument("-o", "--output", help="the path to the output file")
    args = parser.parse_args()

    path = args.path
    seq = args.seq
    output = args.output
    if not output:
        output = "./"

    if path:
        config = configparser.ConfigParser()
        config.read('config.ini')
        token = config['SWISS-MODEL']['token']

        swiss_model_single_file(token, path, output)
    elif seq:
        config = configparser.ConfigParser()
        config.read('config.ini')
        token = config['SWISS-MODEL']['token']

        swiss_model(token, seq, "seq", output)