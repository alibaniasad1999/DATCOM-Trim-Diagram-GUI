import csv
a = []
with open('export/Trim_diag.csv') as data:
    reader = csv.reader(data)
    for i in reader:
        a.append(i)

test = '''-------------------
0 ALPHA     CD       CL       CM       CN       CA       XCP        CLA          CMA          CYB          CNB          CLB
0
     .0     .020     .164    -.0472    .164     .020    -.289    9.430E-02   -4.954E-02   -1.317E-02   -8.191E-04   -1.512E-03
    1.3     .022     .286    -.1137    .287     .015    -.396    9.441E-02   -5.115E-02                             -1.781E-03
0                                    ALPHA     Q/QINF    EPSLON  D(EPSLON)/D(ALPHA)
0
                                       .0      1.000       .672         .319
                                      1.3      1.000      1.086         .319
1                               AUTOMATED STABILITY AND CONTROL METHODS PER APRIL 1976 VERSION OF DATCOM
                                                         DYNAMIC DERIVATIVES
                                        WING-BODY-VERTICAL TAIL-HORIZONTAL TAIL CONFIGURATION
                                                          TOTAL AIRCRAFT'''
a = []