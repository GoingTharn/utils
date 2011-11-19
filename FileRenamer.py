import os.path
import logging as log

def name_changer(path, prefix):
    max_inc = get_max_inc(path, prefix)
    for filename in os.listdir(path):
        wn = filename.split('.')
        if wn != prefix and wn[1] == 'JPG':
            max_inc += 1             
            new_file = '{1}{0}.jpg'.format(max_inc, prefix)
            filename = os.path.join(path, filename)
            new_file = os.path.join(path, new_file)
            log.info("Found {0}, renaming to {1}".format(filename, new_file))
            os.rename(filename, new_file )
        
def get_max_inc(mypath, prefix):
    max_inc = 0
    for filename in os.listdir(mypath):
        wn = filename.split('.')
        if wn[0].startswith(prefix):
            this_inc = int(wn[0][6:])
            if this_inc > max_inc:
                max_inc = this_inc
    return max_inc

if __name__=="__main__":
    path = os.path.join('E:', "Public", "Pictures", "Pictures", "Lottie")
    prefix = "lottie"
    name_changer(path, prefix)
