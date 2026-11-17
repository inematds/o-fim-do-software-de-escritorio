#!/usr/bin/env python3
"""Insere a ilustração de cada tópico logo após o h2 da seção, no guia PT, EN e ES. Idempotente."""
import json, re, html
from pathlib import Path
from PIL import Image

R = Path(__file__).resolve().parents[1]
dados = json.loads((R / 'scripts/imagens.json').read_text())
paginas = {'pt': (R / 'guia/index.html', 'assets/topicos/'),
           'en': (R / 'guia/en/index.html', '../assets/topicos/'),
           'es': (R / 'guia/es/index.html', '../assets/topicos/')}

for lang, (arq, pref) in paginas.items():
    s = arq.read_text()
    n = 0
    for sid, leg in dados['legendas'].items():
        jpg = R / 'guia/assets/topicos' / f'{sid}.jpg'
        if not jpg.exists() or f'data-topico="{sid}"' in s:
            continue
        w, h = Image.open(jpg).size
        txt = html.escape(leg[lang])
        fig = (f'<figure class="wide topico" data-topico="{sid}"><img src="{pref}{sid}.jpg" width="{w}" height="{h}" '
               f'alt="{txt}" loading="lazy" decoding="async"><figcaption>{txt}</figcaption></figure>')
        pat = re.compile(rf'(<section id="{sid}"><div class="wrap"><h2>.*?</h2>)', re.S)
        s, k = pat.subn(lambda m: m.group(1) + fig, s, count=1)
        n += k
    if '.topico{' not in s:
        s = s.replace('</style>', '.topico{margin:8px 0 24px}.topico img{max-height:520px;object-fit:cover}</style>', 1)
    arq.write_text(s)
    print(lang, 'inseridas', n)
