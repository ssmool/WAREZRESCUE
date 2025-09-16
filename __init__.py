import argparse
from pypol.media_rescue import *

TYPECODES = ['r', 'd', 'b', 'l', 'p', 's', 'w', 'v']
DESCRIPTIONS = [
    'unknown type',
    'regular file',
    'deleted file',
    'block device',
    'symbolic link',
    'named FIFO',
    'shadow file',
    'whiteout file',
    'TSK virtual file',
]
TYPEDICT = dict(zip((tt.strip('\\') for tt in TYPECODES),  DESCRIPTIONS))

parser = argparse.ArgumentParser(
    description='Recover files from a disk image using Warez_Rescue',
)
parser.add_argument(
    'image', type=str, nargs=1, help='path to disk image or mount point',
)
parser.add_argument(
    '-o', '--output', type=str, nargs='?', dest='output', default='recovered',
    help=('output extracted files to this directory [default=./recovered/]'),
)
parser.add_argument(
     '-v', '--verbose', dest='verbose', action='store_true',
    default=False, help=('print progress message'),
)

if __name__ == '__main__':
    args = parser.parse_args()
    imgpath = args.image[0]
    outpath = args.output
    recover(imgpath, outpath, verbose=args.verbose)
