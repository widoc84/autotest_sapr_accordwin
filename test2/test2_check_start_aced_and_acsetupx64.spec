# -*- mode: python -*-

block_cipher = None


a = Analysis(['test2_check_start_aced_and_acsetupx64.py'],
             pathex=['C:\\Users\\tester\\source\\repos\\autotest_sapr_accordwin\\test2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='test2_check_start_aced_and_acsetupx64',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
