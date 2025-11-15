from ergtransfer import transfer
import os

sent = 'Alice is talking to her dad on a phone.'
# grm = 'erg-1214-linux-64-0.9.30.dat'
grm = 'erg-1214-osx-0.9.31.dat'

transforms = transfer(
    sent,
    grm,
    f"{os.getcwd()}/ace-0.9.31/ace",
    tenses=['past'],
    progs=['+', '-'],
    perfs=[])
print(transforms)
for trans_type in transforms:
    print(trans_type)
    for t in transforms[trans_type]:
        print(' ', t['surface'])