# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['dipy_5_6NoPaths.py'],
             pathex=['/Users/Seansmac/Desktop/Dev/NetflixSerendipidity'],
             binaries=[],
             datas=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='dipy_5_6NoPaths',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='dipyIcon.icns')
app = BUNDLE(exe,
             name='dipy_5_6NoPaths.app',
             icon='dipyIcon.icns',
             bundle_identifier=None)
