import argparse
import os
import subprocess
import sys

def vim_ezadd(gitUrl, bundlePath=None):
    if bundlePath is None:
        if sys.platform == 'win32':
            bundlePath = os.path.join('~', 'vimfiles', 'bundle')
        else:
            bundlePath = os.path.join('~', '.vim', 'bundle')

    tgt = os.path.expanduser(bundlePath) 
    start_dir = os.getcwd()
    os.chdir(tgt)
    cmd = ' '.join(['git clone', gitUrl]).split()
    subprocess.call(cmd)
    os.chdir(start_dir)
    
def vim_load_many(urlList, bundlePath=None):
    for url in urlList:
        vim_ezadd( url, bundlePath)

def main(**kw):
    url = kw.get('url')
    bundle = kw.get('bundle')
    vim_ezadd(url, bundle)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="File to add")
    parser.add_argument('--url',  help='Url for the git repo to clone')
    parser.add_argument('--bundle',  help='path to pathogen bundle directory')
    args = parser.parse_args()

    main(url=args.url, bundle=args.bundle)
