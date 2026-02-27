import os, re

base = '/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v2_sminimal/public'

files = []
for root, dirs, fnames in os.walk(base):
    for fn in fnames:
        if fn.endswith('.html') and 'backup' not in fn and 'old' not in fn:
            files.append(os.path.join(root, fn))

count_footer = 0
count_video = 0

for f in files:
    with open(f, 'r') as fh:
        content = fh.read()
    
    original = content
    
    # 1. Remove the wordmark span (keep logo img)
    content = re.sub(r'\s*<span class="ia-ft-wordmark">.*?</span>', '', content)
    
    # 2. Remove the tagline span
    content = re.sub(r'\s*<span class="ia-ft-tagline">.*?</span>', '', content)
    
    if content != original:
        count_footer += 1
    
    # 3. Update video URL (only homepage)
    old_video = 'https://radions-website.s3.ap-southeast-2.amazonaws.com/timelapse-of-sunrise-in-sydney-2025-12-17-20-38-30-utc.mov'
    new_video = 'https://radions-website.s3.ap-southeast-2.amazonaws.com/presotto_hero.mp4'
    if old_video in content:
        content = content.replace(old_video, new_video)
        count_video += 1
    
    if content != original:
        with open(f, 'w') as fh:
            fh.write(content)

print(f'Footer updated: {count_footer} pages')
print(f'Video updated: {count_video} pages')
