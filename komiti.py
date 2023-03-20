#!/usr/bin/env fontforge -lang=py -script
# -*- coding: utf-8 -*-

import fontforge
from datetime import date

# Titilium Web のあるディレクトリのパス
titillium_path = "./titilliumweb"

# Roboto のあるディレクトリのパス
roboto_path = "./roboto"

# M+ のあるディレクトリのパス
mplus_path = "./mplus"

# komiti を生成するディレクトリのパス
# 同じディレクトリに一時ファイルも生成される
komiti_path = "./komiti"

# フォントリスト
# Open Sans ファイル名, Roboto ファイル名, M+ ファイル名, komiti ウェイト
font_list = [
    ("TitilliumWeb-Light.ttf", "Roboto-Light.ttf", "mplus-1p-light.ttf", "Light"),
    ("TitilliumWeb-Regular.ttf", "Roboto-Regular.ttf", "mplus-1p-regular.ttf", "Regular"),
    ("TitilliumWeb-SemiBold.ttf", "Roboto-Medium.ttf", "mplus-1p-medium.ttf", "Medium"),
    ("TitilliumWeb-Bold.ttf", "Roboto-Bold.ttf", "mplus-1p-bold.ttf", "Bold"),
    ("TitilliumWeb-Black.ttf", "Roboto-Black.ttf", "mplus-1p-heavy.ttf", "Black"),
]

def main():
    # 縦書き対応
    fontforge.setPrefs('CoverageFormatsAllowed', 1)

    # バージョンを今日の日付から生成する
    today = date.today()
    version = "komiti-{0}".format(today.strftime("%Y%m%d"))

    for (ti, rb, mp, weight) in font_list:
        ti_path = "{0}/{1}".format(titillium_path, ti)
        rb_path = "{0}/{1}".format(roboto_path, rb)
        mp_path = "{0}/{1}".format(mplus_path, mp)
        ko_path = "{0}/komiti-{1}.ttf".format(komiti_path, weight)
        generate_komiti(ti_path, rb_path, mp_path, ko_path, weight, version)

def komiti_sfnt_names(weight, version):
    return (
        ('English (US)', 'Copyright',
         '''\
         komiti: Copyright (c) 2023- Hikali.
         komiti is fork of Koruri.
         Koruri: Copyright (c) 2013- lindwurm.

         titillium Web: 2009-2011 by Accademia di Belle Arti di Urbino and students of MA course of Visual design.
         Roboto: Copyright (c) 2012- Google.
         M+ OUTLINE FONTS: Copyright (C) 2002- M+ FONTS PROJECT.'''),
        ("English (US)", "License",
         "This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL",
        ),
        ("English (US)", "License URL", "http://scripts.sil.org/OFL"),
        ('English (US)', 'Family', 'komiti {0}'.format(weight)),
        ('English (US)', 'SubFamily', weight),
        ('English (US)', 'Fullname', 'komiti-{0}'.format(weight)),
        ('English (US)', 'Version', version),
        ('English (US)', 'PostScriptName', 'komiti-{0}'.format(weight)),
        ('English (US)', 'Vendor URL', 'https://komiti.github.io'),
        ('English (US)', 'Preferred Family', 'komiti'),
        ('English (US)', 'Preferred Styles', weight),
        ('Japanese', 'Preferred Family', 'komiti'),
        ('Japanese', 'Preferred Styles', weight),
    )

def komiti_gasp():
    return (
        (8, ('antialias',)),
        (13, ('antialias', 'symmetric-smoothing')),
        (65535, ('antialias', 'symmetric-smoothing')),
    )

def generate_komiti(ti_path, rb_path, mp_path, ko_path, weight, version):
    # M+ を開く
    try:
        font = fontforge.open(mp_path)
    except OSError as e:
        print("OSError:", e, "\nM+ 1p を mplus/ に展開しましたか?")
        exit(1)

    # EMの大きさを1024に設定する 
    font.em = 1024

    # Titillium Web を開く
    print(ti_path)
    tifont = fontforge.open(ti_path)

    # Titillium Web に含まれるグリフを削除する
    font.selection.none()
    tifont.selection.all()
    for glyph in tifont.selection.byGlyphs:
        if glyph.glyphname in font:
            font.selection.select(("more",), glyph.glyphname)
    font.clear()

    # Titillium Web をマージする
    font.mergeFonts(ti_path)

    # Fancy Colon を Roboto からコピーする
    rbfont = fontforge.open(rb_path)
    
    # Fancy Colon をコピー
    rbfont.selection.select(0xee01)
    rbfont.copy()
    font.selection.select(0xee01)
    font.paste()

    # Fancy Colon を U+A789 にコピー
    font.selection.select(0xee01)
    font.copy()
    font.selection.select(0xa789)
    font.paste()

    # フォント情報の設定
    font.sfnt_names = komiti_sfnt_names(weight, version)
    font.os2_vendor = "4741"

    # Grid Fittingの設定
    font.gasp = komiti_gasp()

    # TTF の生成
    font.generate(ko_path, '', ('short-post', 'opentype', 'PfEd-lookups'))

if __name__ == '__main__':
    main()
