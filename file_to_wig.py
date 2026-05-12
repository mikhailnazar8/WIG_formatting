#!/usr/bin/env python3

import argparse
import sys
import math
import itertools
import re
import logging
import subprocess
from operator import itemgetter
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger()
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="Path to Input file")
parser.add_argument("--output", required=True, help="Path to Output file")
parser.add_argument("--type", required=True, help="""

Type of file, file can be:
-fst
-pi
-tajimas_d (default window)
-window_fst
-window_pi


""")

args = parser.parse_args()

class convert_file:
    def __init__(self, args):
        self.input = args.input
        self.output = args.output
        self.type = args.type

    def write_wig(self, chromsomes):
        with open(self.output, 'w') as f:
            if self.type =="fst" or self.type == "pi":
                for chrom in chromsomes:
                   f.write(f"variableStep chrom={chrom}\n")
                   for pos, value in chromsomes[chrom]:
                       f.write(f"{pos}\t{value}\n")
            ##this function is a repeat of the above but was built to figure out how to impliment fixedStep, which is not reading into IGV
            elif self.type =="window_fst" or self.type == "window_pi" or self.type == "tajimas_d":
                for chrom in chromsomes:
                    f.write(f"variableStep chrom={chrom}\n")
                    for pos, value in chromsomes[chrom]:
                        f.write(f"{pos}\t{value}\n")
            else:
                print("Failure at write step. This file type is not supported yet.")

    def convert_fst_to_wig(self):
        log.info(f"Converting FST to WIG for {self.input}\n")
        chromsomes=defaultdict(list)
        with open(self.input, 'r') as f:
            next(f)
            for line in f:
                line=line.strip().split()
                chrom=line[0]
                pos=int(line[1])
                fst= float(line[2])
                if fst <0 or math.isnan(fst): fst=0
                chromsomes[chrom].append((pos, fst))
        self.write_wig(chromsomes)

    def convert_pi_to_wig(self):
        log.info(f"Converting Pi to WIG for {self.input}\n")
        chromsomes=defaultdict(list)
        with open(self.input, 'r') as f:
            next(f)
            for line in f:
                line=line.strip().split()
                chrom=line[0]
                pos=int(line[1])
                pi= float(line[2])
                if pi <0 or math.isnan(pi): pi=0
                chromsomes[chrom].append((pos, pi))
        self.write_wig(chromsomes)

    def convert_win_fst_to_wig(self):
        log.info(f"Converting Windowed FST to WIG for {self.input}\n")
        chromsomes=defaultdict(list)
        with open(self.input, 'r') as f:
            next(f)
            for line in f:
                line=line.strip().split()
                chrom=line[0]
                start=int(line[1])
                fst= float(line[4])
                if fst <0 or math.isnan(fst): fst=0
                chromsomes[chrom].append((start,fst))
        self.write_wig(chromsomes)

    def convert_windowed_pi_to_wig(self):
        log.info(f"Converting Windowed Pi to WIG for {self.input}\n")
        chromsomes=defaultdict(list)
        with open(self.input,'r') as f:
            next(f)
            for line in f:
                line=line.strip().split()
                chrom=line[0]
                start=int(line[1])
                pi= float(line[4])
                if pi <0 or math.isnan(pi): pi=0
                chromsomes[chrom].append((start,pi))
        self.write_wig(chromsomes)

    def convert_tajimas_d_to_wig(self):
        log.info(f"Converting Tajimas D to WIG for {self.input}\n")
        chromsomes=defaultdict(list)
        with open(self.input,'r') as f:
            next(f)
            for line in f:
                line=line.strip().split()
                if int(line[2])<0: continue
                chrom=line[0]
                start=int(line[1])
                tajimas_d=float(line[3])
                if math.isnan(tajimas_d): tajimas_d=0
                if start <= 0: start =1
                chromsomes[chrom].append((start,tajimas_d))
        self.write_wig(chromsomes)
        

    def run(self):
        if self.type == "fst":
            self.convert_fst_to_wig()
        elif self.type == "pi":
            self.convert_pi_to_wig()
        elif self.type == "window_fst":
            self.convert_win_fst_to_wig()
        elif self.type == "window_pi":
            self.convert_windowed_pi_to_wig()
        elif self.type == "tajimas_d":
            self.convert_tajimas_d_to_wig()
        else:
            log.error(f"File type '{self.type}' is not supported yet.")

if __name__ == "__main__":
    converter = convert_file(args)
    converter.run()