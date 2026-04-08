#!/usr/bin/env python3
import re
import os

icons = {
    'whatsapp': '#25D366',
    'telegram': '#26A5E4',
    'vk': '#4C75A3'
}

for name, color in icons.items():
    infile = f'icons/{name}.svg'
    outfile = f'icons/color/{name}.svg'
    with open(infile, 'r', encoding='utf-8') as f:
        content = f.read()
    # Добавляем fill в тег path, если его нет
    # Простой способ: заменить <path на <path fill="color"
    # Но может быть несколько path, заменим все
    # Используем регулярное выражение
    def add_fill(match):
        tag = match.group(0)
        if 'fill=' not in tag:
            # Вставляем fill перед закрывающим >
            tag = tag.replace('<path', f'<path fill="{color}"')
        return tag
    content = re.sub(r'<path[^>]*>', add_fill, content)
    # Также добавим fill в возможные другие элементы, например, circle, rect
    with open(outfile, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {outfile}')

print('Done')