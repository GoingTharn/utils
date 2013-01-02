'''
TODO: Add a set of snippets for the templating of new files and tests
'''
import argparse
import os
import subprocess
import sys

def vim_ezadd(git_url, bundle_path=None):
    '''
        Quick way to conviently clone a vim plugin living in git
    '''

    if bundle_path is None:
        if sys.platform == 'win32':
            bundle_path = os.path.join('~', 'vimfiles', 'bundle')
        else:
            bundle_path = os.path.join('~', '.vim', 'bundle')

    tgt = os.path.expanduser(bundle_path) 
    start_dir = os.getcwd()
    os.chdir(tgt)

    if sys.platform == 'win32':
        call_git_windows(git_url)
    else:
        cmd = ' '.join(['git clone', git_url]).split()
        subprocess.call(cmd)

    os.chdir(start_dir)
    
def call_git_windows(git_url):
    '''
    Used for calling git from windows, since it uses cygwin
    '''
    temp_path = os.path.expanduser('~\\vimfiles\\temp_sh.sh')
    # default git path
    path = os.path.join('C:', '\Program Files (x86)', 'Git', 'bin', 'sh.exe')
    with open(temp_path, 'wb') as tempfile:
        shell_cmd  = ' '.join(['git clone', git_url])
        tempfile.write(shell_cmd)
    cmd = ' '.join([path, '--login', '-i', temp_path])
    subprocess.call(cmd)
    os.remove(temp_path)

def vim_load_many(urls, bundle_path=None):
    '''
    load a list of urls into vim config. Useful to bootstrap new system.
    '''
    for url in urls:
        vim_ezadd( url, bundle_path)

def main(**kw):
    '''
    Usage - derp
    '''
    url = kw.get('url')
    bundle = kw.get('bundle')
    vim_ezadd(url, bundle)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser(description="File to add")
        parser.add_argument('--url',  help='Url for the git repo to clone')
        helpmsg = 'path to pathogen bundle directory' 
        parser.add_argument('--bundle',  help=helpmsg)
        args = parser.parse_args()
        main(url=args.url, bundle=args.bundle)
