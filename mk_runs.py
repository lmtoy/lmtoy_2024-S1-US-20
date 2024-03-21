#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-US-20"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["G45.47_01_of_04"] =  [ 113512, 113513,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["G45.47_01_of_04"] = "extent=500 b_order=1 dv=60 dw=60 pix_list=-13,14,15"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2["G45.47_01_of_04"] = "pix_list=-13"

pars3 = {}
pars3["G45.47_01_of_04"] = ""

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
