#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import ase.io as io


class ChimesIn():

    def __init__(self):
        pass

    @classmethod
    def aims(cls, path_position, path_force, cell, output_name: str = 'input.xyzf'):
        # read positions
        data_pos = io.read(path_pos, index=':')

        # read forces
        data_for = io.read(path_force, index=':')

        # write
        with open(output_name, 'w') as f:
            for i, (ipos, ifor) in enumerate(zip(data_pos, data_for)):
                symbols = ipos.get_chemical_symbols()
                f.write(str(len(ipos.numbers)) + '\n')
                f.write(' '.join(map(str, cell)) + '\n')
                print(ipos.positions.shape, ifor.positions.shape, symbols)
                [f.write(sym + ' ' +
                         ' '.join(map(str, pos)) + ' ' +
                         ' '.join(map(str, force)) + '\n')
                         for sym, pos, force in zip(symbols, ipos.positions, ifor.positions)]

        return cls()

    @staticmethod
    def aims2dftb(path_position, cell, output_name):
        # read positions
        data_pos = io.read(path_pos, index=':')

        for i, pos in enumerate(data_pos):
            pos.cell = cell
            io.write(output_name + str(i), pos, format='dftb')

    @classmethod
    def vasp(cls):
        return cls()

    @classmethod
    def dftbplus(cls):
        return cls()

    @classmethod
    def tbmalt(cls):
        return cls()


path_force = '/home/gz_fan/Documents/ML/chimes/chimes_lsq/work/si/si.for_0.xyz'
path_pos = '/home/gz_fan/Documents/ML/chimes/chimes_lsq/work/si/si.pos.xyz'
# ChimesIn.aims(path_pos, path_force, [5.46873, 5.46873, 5.46873], 'input.xyzf')
# ChimesIn.aims2dftb(path_pos, [5.46873, 5.46873, 5.46873], 'geo.gen')

# cell=[7.257249, 0.0, 0.0, 3.6286245, 6.284962, 0.0, 3.6286245, 2.094987332, 5.925519]
cell=[7.257249, 3.6286245, 6.284962, 3.6286245, 2.094987332, 5.925519]
path_force = '/home/gz_fan/Downloads/software/fhiaims/aims21/work/md/li6/li6.for_0.xyz'
path_pos = '/home/gz_fan/Downloads/software/fhiaims/aims21/work/md/li6/li6.pos.xyz'
ChimesIn.aims(path_pos, path_force, cell, 'input.xyzf')
