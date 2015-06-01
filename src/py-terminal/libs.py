#!/usr/bin/env python 
import urllib
import os
import tarfile
import zipfile
from cStringIO import StringIO

def name_from_url(url):
    basename = os.path.basename(url)
    if (basename.find('tar') > 0):
        return os.path.splitext(os.path.splitext(basename)[0])[0]
    return os.path.splitext(basename)[0]

def extract_file(url, dir_path='.'):
    lfile = None
    if url.endswith('.zip'):
        opener, mode = zipfile.ZipFile, 'r'
        lfile = StringIO(urllib.urlopen(url).read())
    elif url.endswith('.tar.gz') or url.endswith('.tgz'):
        opener, mode = tarfile.open, 'r:gz'
    elif url.endswith('.tar.bz2') or url.endswith('.tbz'):
        opener, mode = tarfile.open, 'r:bz2'
    else: 
        raise ValueError, "Could not extract `%s` as no appropriate extractor is found" % url
    
    cwd = os.getcwd()
    os.chdir(os.path.dirname(dir_path))

    try:
        if lfile is None:
            file = opener(fileobj=StringIO(urllib.urlopen(url).read()), mode=mode)
        else:
            file = opener(lfile, mode)
        try: file.extractall(dir_path)
        finally: file.close()
    finally:
        os.chdir(cwd)

if __name__ == '__main__':
    curr_dir = os.path.dirname(__file__)
    # get package
    get_list = [['http://www.cosc.canterbury.ac.nz/greg.ewing/python_gui/PyGUI-2.5.3.tar.gz', 'PyGUI'],
                ('http://liquidtelecom.dl.sourceforge.net/project/pywin32/pywin32/Build%20219/pywin32-219.zip', '')
                ['http://downloads.sourceforge.net/project/ctypes/ctypes/1.0.2/ctypes-1.0.2.tar.gz','']
                ]
    libs_dir = 'libs'
    for url, name in get_list:
        if name:
            contain_dir = os.path.join(curr_dir, libs_dir, name)
        else:
            contain_dir = os.path.join(curr_dir, libs_dir, name_from_url(url))
        if (os.path.exists(contain_dir)):
            print contain_dir, 'installed'
        else:
            print 'installing ...  ' , url
            extract_file(url, contain_dir)
            
            
    print 'libs install done !!'
