#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-20"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["G45.47_01_of_04"] =  [ 113512, 113513,]

on["G45.47_02_of_04"] =  [-117355, 119626, 119627,]

on["G45.47_03_of_04"] =  [ 119631, 120329, 120330,]

on["G45.47_04_of_04"] =  [ 120268,]


on["G45-mos"] = on["G45.47_01_of_04"]  + on["G45.47_02_of_04"]  + on["G45.47_03_of_04"] + on["G45.47_04_of_04"]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["G45.47_01_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45.47_02_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45.47_03_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45.47_04_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45-mos"]         = "skip=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["G45.47_01_of_04"] = "bank=0 pix_list=-13"
pars2["G45.47_02_of_04"] = "bank=0 pix_list=-13"
pars2["G45.47_03_of_04"] = "bank=0 pix_list=-13"
pars2["G45.47_04_of_04"] = "bank=0 pix_list=-13"

pars3 = {}
pars3["G45.47_01_of_04"] = "bank=1 pix_list=-13,14,15"
pars3["G45.47_02_of_04"] = "bank=1 pix_list=-13,14,15"
pars3["G45.47_03_of_04"] = "bank=1 pix_list=-13,14,15"
pars3["G45.47_04_of_04"] = "bank=1 pix_list=-13,14,15"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
