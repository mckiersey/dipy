# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dipy_6_5.py'],
             pathex=['/Users/Seansmac/Desktop/Dev/NetflixSerendipidity'],
             binaries=[],
             datas=[('“netflixLogo.png', '.”')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='dipy_6_5',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='dipyIconRound.icns')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='dipy_6_5')
app = BUNDLE(coll,
             name='dipy_6_5.app',
             icon='dipyIconRound.icns',
             bundle_identifier=None)
