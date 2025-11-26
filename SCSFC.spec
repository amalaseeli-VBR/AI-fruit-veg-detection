# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['D:\\AI_FRUIT_CODE_DETECTION\\fruit_detection.py'],
    pathex=[],
    binaries=[('C:\\Program Files\\Python313\\DLLs\\libffi-8.dll', '.')],
    datas=[('D:\\AI_FRUIT_CODE_DETECTION\\db_cred.yaml', '.'), ('D:\\AI_FRUIT_CODE_DETECTION\\models', 'models')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='SCSFC',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='SCSFC',
)
