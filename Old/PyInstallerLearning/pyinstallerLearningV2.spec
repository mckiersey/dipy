# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['pyinstallerLearningV2.py'],
             pathex=['/Users/Seansmac/Desktop/Dev/NetflixSerendipidity/PyInstallerLearning'],
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
          [],
          exclude_binaries=True,
          name='pyinstallerLearningV2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='pyinstallerLearningV2')
app = BUNDLE(coll,
             name='pyinstallerLearningV2.app',
             icon=None,
             bundle_identifier=None)
