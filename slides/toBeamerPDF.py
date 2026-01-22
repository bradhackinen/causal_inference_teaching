import os
import glob
from pathlib import Path
import re
import subprocess
from argparse import ArgumentParser
import time


pandoc_args = ['--slide-level=2','-V','theme:metropolis']

path = Path(os.path.dirname(os.path.realpath(__file__)))


def compile_slides(overwrite=False,verbose=True):

    md_files = glob.iglob(f'{path}/**/**.md',recursive=True)

    for md_file in md_files:
        temp_file = md_file + '.temp.md'
        out_file = re.sub(r'\.md$','.pdf',md_file)

        if os.path.isfile(path/out_file):
            out_modified_time = os.path.getmtime(path/out_file)
            md_modified_time = os.path.getmtime(path/md_file)
            if md_modified_time < out_modified_time:

                if not overwrite:
                    if verbose: print(f'Already compiled {md_file}')
                    continue

        print(f'Compiling {md_file}')

        with open(path/md_file,'r') as f:
            md = f.read()

        # Replace line breaks
        md = md.replace('<br>',r'\  ')

        # Replace small
        md = md.replace('<small>',r' \tiny ')
        md = md.replace('</small>',r' \normalsize ')

        # Check for replacements
        any_replacement = False
        for m in re.finditer(r'.*\<\!\-\-beamer\:(.*)\-\-\>.*',md):
            if verbose: print(f'\tReplacing "{m.group(0)}"\n\t\t--> "{m.group(1)}"')
            any_replacement = True

        if any_replacement:
            # Replace lines tagged with "beamer:" html comment
            md = re.sub(r'.*\<\!\-\-beamer\:(.*)\-\-\>.*',r'\1',md)

            # write temp file with modified contents
            with open(path/temp_file, 'w') as f:
                f.write(md)

            in_file = temp_file

        else:
            in_file = md_file

        subprocess.run(['pandoc','-t','beamer',path/in_file]+pandoc_args+['-o',path/out_file])

        if os.path.isfile(path/temp_file):
            os.remove(path/temp_file)



parser = ArgumentParser()
parser.add_argument('--overwrite',action='store_true')
parser.add_argument('--watch',action='store_true')
parser.add_argument('--verbose',action='store_true')

args = parser.parse_args()

if args.watch:
    print(f'Watching {path} for changes')
   
    while True:
        compile_slides(args.overwrite,args.verbose)
        time.sleep(1)

else:
    print(f'Compiling all .md files in {path}')
    compile_slides(args.overwrite,args.verbose)