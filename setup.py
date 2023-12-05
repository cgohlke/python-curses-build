import os
import sys

from setuptools import Extension, setup

libraries = ['pdcurses', 'user32', 'advapi32', 'gdi32', 'comdlg32', 'shell32']

define_macros = [
    ('PDC_WIDE', None),
    ('HAVE_NCURSESW', None),
    ('HAVE_TERM_H', None),
    ('HAVE_CURSES_IS_TERM_RESIZED', None),
    ('HAVE_CURSES_RESIZE_TERM', None),
    ('HAVE_CURSES_TYPEAHEAD', None),
    ('HAVE_CURSES_HAS_KEY', None),
    ('HAVE_CURSES_FILTER', None),
    ('HAVE_CURSES_WCHGAT', None),
    ('HAVE_CURSES_USE_ENV', None),
    ('HAVE_CURSES_IMMEDOK', None),
    ('HAVE_CURSES_SYNCOK', None),
    # ('HAVE_CURSES_IS_PAD', None),
    ('WINDOW_HAS_FLAGS', None),
    ('NCURSES_MOUSE_VERSION', 2),
    ('_ISPAD', 0x10),
    ('is_term_resized', 'is_termresized'),
]

include_dirs = [os.path.dirname(__file__)]
library_dirs = ['wincon']

srcdir = 'py%i%i//' % sys.version_info[:2]

setup(
    name='python-curses',
    version='2.2.2',
    description='Support for the standard curses module on Windows',
    url='https://github.com/python/cpython/issues/47138',
    license='PSF2',
    ext_modules=[
        Extension(
            '_curses',
            sources=['terminfo.c', srcdir + '_cursesmodule.c'],
            define_macros=define_macros,
            libraries=libraries,
            library_dirs=library_dirs,
            include_dirs=include_dirs,
        ),
        Extension(
            '_curses_panel',
            sources=['terminfo.c', srcdir + '_curses_panel.c'],
            define_macros=define_macros,
            libraries=libraries,
            library_dirs=library_dirs,
            include_dirs=include_dirs,
        ),
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
        'Environment :: Win32 (MS Windows)',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: C',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
