# -*- mode: python -*-

block_cipher = None


a = Analysis(['test5_check_correct_file_on_distrx64.py'],
             pathex=['C:\\Users\\tester\\source\\repos\\autotest_sapr_accordwin\\test05'],
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
          name='test5_check_correct_file_on_distrx64',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
