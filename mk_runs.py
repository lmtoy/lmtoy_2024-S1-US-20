#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-20"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["G29.96_01_of_04"] =     [ 132924,]
on["G29.96_01_of_04_SB0"] = [ 132241, 132242,]

on["G30.76_01_of_04"] =  [ 120665, 120666,]
on["G30.76_02_of_04"] =  [ 120796, 120797,]
on["G30.76_03_of_04"] =  [ 120952, 120953,]
on["G30.76_04_of_04"] =  [ 120957, 120958,]


on["G45.47_01_of_04"] =  [ 113512, 113513,]
on["G45.47_02_of_04"] =  [-117355, 119626, 119627,]
on["G45.47_03_of_04"] =  [ 119631, 120329, 120330,]
on["G45.47_04_of_04"] =  [ 120268, 120522, 120523,]


on["G45-mos"] = on["G45.47_01_of_04"]  + on["G45.47_02_of_04"]  + on["G45.47_03_of_04"] + on["G45.47_04_of_04"]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}

pars1["G29.96_01_of_04"]     = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G29.96_01_of_04_SB0"] = "extent=500 b_order=1 dv=60 dw=60"

pars1["G30.76_01_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G30.76_02_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"

pars1["G45.47_01_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45.47_02_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45.47_03_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45.47_04_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-15"
pars1["G45-mos"]         = "skip=1"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}

pars2["G29.96_01_of_04"]     = "bank=0 pix_list=-13"
pars2["G29.96_01_of_04_SB0"] = ""

pars2["G30.76_01_of_04"] = "bank=0 pix_list=-13"
pars2["G30.76_02_of_04"] = "bank=0 pix_list=-13"

pars2["G45.47_01_of_04"] = "bank=0 pix_list=-13"
pars2["G45.47_02_of_04"] = "bank=0 pix_list=-13"
pars2["G45.47_03_of_04"] = "bank=0 pix_list=-13"
pars2["G45.47_04_of_04"] = "bank=0 pix_list=-13"

pars3 = {}

pars3["G29.96_01_of_04"] = "bank=1 pix_list=-13,15"

pars3["G30.76_01_of_04"] = "bank=0 pix_list=-13,15"
pars3["G30.76_02_of_04"] = "bank=0 pix_list=-13,15"

pars3["G45.47_01_of_04"] = "bank=1 pix_list=-13,14,15"
pars3["G45.47_02_of_04"] = "bank=1 pix_list=-13,14,15"
pars3["G45.47_03_of_04"] = "bank=1 pix_list=-13,14,15"
pars3["G45.47_04_of_04"] = "bank=1 pix_list=-13,14,15"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
