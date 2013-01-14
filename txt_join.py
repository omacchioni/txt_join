#!/usr/bin/python

import csv
from optparse import OptionParser

class TxtJoiner():

    def readfile(self, filename, keycol, separator):
        output = {}
        with open(filename, 'rb') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=separator, quotechar='"')
            for row in csvreader:
                key = row[int(keycol)].strip()
                output[key] = row
            return output


    def run(self, filename1, keycol1, separator1, filename2, keycol2, separator2):
        content1 = self.readfile(filename1, keycol1, separator1)
        content2 = self.readfile(filename2, keycol2, separator2)
        all_keys = content1.keys() + content2.keys()
        for key in all_keys:
            to_print = ""
            if key in content1:
                to_print += separator1.join(content1[key])+separator1
            if key in content2:
                to_print += separator2.join(content2[key])
            print to_print


if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--file1", dest="filename1",
            help="Read data from FILE1", metavar="FILE")
    parser.add_option("--file2", dest="filename2",
            help="Read data from FILE2", metavar="FILE")
    parser.add_option("--keycol1", dest="keycol1",
            help="Column # to use", type="int")
    parser.add_option("--keycol2", dest="keycol2",
            help="Column # to use", type="int")
    parser.add_option("--separator1", dest="separator1",
            help="Separator", default=";")
    parser.add_option("--separator2", dest="separator2",
            help="Separator", default=";")
    (options, args) = parser.parse_args()

    TxtJoiner = TxtJoiner()
    TxtJoiner.run(
        options.filename1, options.keycol1, options.separator1,
        options.filename2, options.keycol2, options.separator2,
    )


