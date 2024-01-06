import textgrids
from glob import glob
import argparse

parser = argparse.ArgumentParser(
                    prog='TextGrid2HTK',
                    description='Converting TextGrids to HTK-format (lab or audacity txt)')
parser.add_argument('-t','--tier',nargs='?', const='phones',help='Tier name to export. Default = "phones".')
parser.add_argument('-f','--format',nargs='?', const='lab',help='Export format. Default = "lab".')
parser.add_argument('-c','--converter',help='Converter. Default is None. You can use built-in "sil_and_br" to convert silences and breaths to HTK format.')
parser.add_argument('-cl','--clean',action='store_true',help='Clean from numbers. Default is False.')
parser.add_argument('-l','--low',action='store_true',help='Lower capitalization. Default is False.')


args = parser.parse_args()
needed_tier=args.tier
converter=args.converter
frm=args.format
cln=args.clean
low=args.low
if frm!='txt':
    frm='lab'


a=glob('**/*.textgrid',recursive=True)
labs=[]
sils=['<ap>','ap','','sil','<pad>','spn','<spn>']
brs=['<sp>','sp']
if converter is not None and converter!='sil_and_br':
    with open(converter) as f:
        dd=f.readlines()
    repl={}
    for k in dd:
        k=k.split(',')
        repl[k[0]]=k[1]
for i in a:
    f=textgrids.TextGrid(i)
    l=[]
    for j in f[needed_tier]:
        if converter=='sil_and_br':
            if j.text.lower() in sils:
                j.text='pau'
            elif j.text.lower() in brs:
                j.text='br'
        elif converter is not None:
            for k in repl:
                if j.text==k:
                    j.text=repl[k]
        if cln:
            j.text = ''.join([i for i in j.text if not i.isdigit()])
        if low:
            j.text=j.text.lower()

        if frm=='lab':
            l.append(f'{int(j.xmin*10000000)} {(int(j.xmax*10000000))} {j.text}'+'\n')
        elif frm=='txt':
            l.append(f'{j.xmin:.6f}	{j.xmax:.6f}	{j.text}'+'\n')
    with open(i.split('.')[0]+f'.{frm}','w') as lab:
        for j in l:
            lab.write(j)