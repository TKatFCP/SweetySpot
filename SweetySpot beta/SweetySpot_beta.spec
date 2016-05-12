# -*- mode: python -*-
from kivy.deps import sdl2, glew
def getResource(identifier, *args, **kwargs):
    if identifier == 'pygame_icon.tiff':
        raise IOError()
    return _original_getResource(identifier, *args, **kwargs)

import pygame.pkgdata
_original_getResource = pygame.pkgdata.getResource
pygame.pkgdata.getResource = getResource
a = Analysis(['C:\\Users\\TK Win10\\Desktop\\test packen\\SweetySpot_beta.py'],
             pathex=['C:\\Users\\TK Win10\\Desktop\\test packen'],
             hiddenimports=[],
             hookspath=None,
             )
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='SweetySpot_beta.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True,
          icon='C:\\Users\\TK Win10\\Desktop\\test packen\\sspot.ico' )
coll = COLLECT(exe,Tree('C:\\Users\\TK Win10\\Desktop\\test packen'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=None,
               upx=True,
               name='SweetySpot beta')
