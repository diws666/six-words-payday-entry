import os

LINE = 'First payday arrived. I bought silence.'  # verified: 39 chars, 6 words, no trailing newline

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
path = os.path.join(output_dir, 'entry.txt')

os.makedirs(output_dir, exist_ok=True)
with open(path, 'w', encoding='utf-8') as f:
    f.write(LINE)
