#!/usr/bin/env python3
"""Add logo to header and footer on all HTML pages."""
import re, os, glob

BASE = "/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v1/public"

# All HTML pages (exclude backups/old)
pages = []
for root, dirs, files in os.walk(BASE):
    # Skip backup/old files
    for f in files:
        if f.endswith('.html') and not any(x in f for x in ['backup', '.old-']):
            pages.append(os.path.join(root, f))

pages.sort()
print(f"Found {len(pages)} HTML pages")

header_count = 0
footer_count = 0

for filepath in pages:
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()
    
    original = content
    short = filepath.replace(BASE + '/', '')
    
    # ──────────────────────────────────────────────
    # HEADER: Add logo image inside .nav-wordmark <a>
    # ──────────────────────────────────────────────
    
    # Pattern A (homepage): multi-line
    # <a href="/" class="nav-wordmark">
    #     Inbuilt Atelier
    #     <span>Double Bay · Sydney</span>
    # </a>
    content = re.sub(
        r'(<a\s+href="/"\s+class="nav-wordmark">)\s*\n\s*Inbuilt Atelier\s*\n',
        r'\1\n                        <img src="/images/logo_inbuilt_atelier.png" alt="Inbuilt Atelier" class="nav-logo">\n',
        content
    )
    
    # Pattern B (other pages): single-line
    # <a href="/" class="nav-wordmark">Inbuilt Atelier<span>
    content = re.sub(
        r'(<a\s+href="/"\s+class="nav-wordmark">)Inbuilt Atelier(<span>)',
        r'\1<img src="/images/logo_inbuilt_atelier.png" alt="Inbuilt Atelier" class="nav-logo">\2',
        content
    )
    
    if content != original:
        header_count += 1
    
    before_footer = content
    
    # ──────────────────────────────────────────────
    # FOOTER: Add logo before the brand name text
    # ──────────────────────────────────────────────
    
    logo_footer = '<img src="/images/logo_inbuilt_atelier.png" alt="Inbuilt Atelier" class="footer-logo" style="height:64px;width:auto;margin-bottom:1rem;display:block;filter:brightness(0) invert(1) brightness(.92);">'
    
    # Pattern A (homepage): uses class ia-footer-wordmark
    # <span class="ia-footer-wordmark">Inbuilt Atelier</span>
    if 'ia-footer-wordmark' in content and 'footer-logo' not in content:
        content = re.sub(
            r'(<span class="ia-footer-wordmark">)',
            logo_footer + '\n                    \\1',
            content
        )
    
    # Pattern B (other pages): inline-styled span
    # <span style="font-family:'Cormorant Garamond'...">Inbuilt Atelier</span>
    if 'footer-logo' not in content:
        content = re.sub(
            r'(<span style="font-family:\'Cormorant Garamond\'[^"]*">Inbuilt Atelier</span>)',
            logo_footer + '\n        \\1',
            content
        )
    
    if content != before_footer:
        footer_count += 1
    
    # ──────────────────────────────────────────────
    # HEADER INLINE STYLES: Update .nav-wordmark CSS
    # to accommodate logo image
    # ──────────────────────────────────────────────
    
    # Add .nav-logo CSS if not already present and page has inline styles
    if '.nav-wordmark' in content and '.nav-logo' not in content:
        # Add after the existing nav-wordmark styles
        # Pattern: after "header .nav-wordmark span{...}" or "header .nav-wordmark span { ... }"
        nav_logo_css = """
        .nav-logo { height: 36px; width: auto; display: block; }
        .nav-wordmark { display: flex; align-items: center; gap: 0.6rem; }"""
        
        # Insert after the last header .nav-wordmark rule
        content = re.sub(
            r'(header\s*\.nav-wordmark\s*span\s*\{[^}]+\})',
            r'\1' + nav_logo_css,
            content,
            count=1
        )
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print(f"  ✓ {short}")
    else:
        print(f"  – {short} (no change)")

print(f"\nDone: {header_count} headers, {footer_count} footers updated")
