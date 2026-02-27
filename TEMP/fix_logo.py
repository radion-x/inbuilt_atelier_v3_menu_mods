#!/usr/bin/env python3
"""Fix header logo (remove text, make bigger) and footer logo (remove invert filter)."""
import re, os

BASE = "/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v1/public"

pages = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith('.html') and not any(x in f for x in ['backup', '.old-']):
            pages.append(os.path.join(root, f))
pages.sort()

count = 0
for filepath in pages:
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    original = content
    short = filepath.replace(BASE + '/', '')

    # ── HEADER: Remove <span>Double Bay · Sydney</span> ──
    # Multi-line pattern (homepage)
    content = re.sub(
        r'(<img src="/images/logo_inbuilt_atelier\.png"[^>]*class="nav-logo"[^>]*>)\s*\n\s*<span>Double Bay.*?</span>\s*\n',
        r'\1\n',
        content
    )
    # Single-line pattern (other pages)
    content = re.sub(
        r'(<img src="/images/logo_inbuilt_atelier\.png"[^>]*class="nav-logo"[^>]*>)<span>Double Bay.*?</span>',
        r'\1',
        content
    )

    # ── HEADER CSS: Make logo bigger (36px → 52px), remove gap/flex since no text ──
    # Multi-line (homepage)
    content = re.sub(
        r'\.nav-logo \{ height: 36px; width: auto; display: block; \}',
        '.nav-logo { height: 52px; width: auto; display: block; }',
        content
    )
    # Single-line (other pages)  
    content = re.sub(
        r'\.nav-logo\s*\{\s*height:\s*36px;\s*width:\s*auto;\s*display:\s*block;\s*\}',
        '.nav-logo { height: 52px; width: auto; display: block; }',
        content
    )

    # ── FOOTER: Remove the brightness/invert filter, show actual logo ──
    content = re.sub(
        r'filter:brightness\(0\) invert\(1\) brightness\(\.92\);',
        '',
        content
    )

    # ── FOOTER: Increase logo size from 64px to 80px ──
    content = content.replace(
        'class="footer-logo" style="height:64px;',
        'class="footer-logo" style="height:80px;'
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(content)
        count += 1
        print(f"  ✓ {short}")
    else:
        print(f"  – {short} (no change)")

print(f"\nDone: {count} pages updated")
