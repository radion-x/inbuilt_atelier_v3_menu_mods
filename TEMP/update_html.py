#!/usr/bin/env python3
"""Bulk update all HTML files for the modern minimalist redesign.
Handles: Google Fonts, logos, inline fonts, inline colors, CSS versions, inline style blocks."""
import os, re, glob

PUBLIC = 'public'

# Find all HTML files recursively
html_files = glob.glob(os.path.join(PUBLIC, '**', '*.html'), recursive=True)
# Only process actual pages, not backups
html_files = [f for f in html_files if not f.endswith('.backup') and '.old-' not in f 
              and '.backup-' not in f and 'admin/' not in f]

print(f"Found {len(html_files)} HTML files to update:")
for f in sorted(html_files):
    print(f"  {f}")

changes = 0

for filepath in html_files:
    with open(filepath, 'r') as f:
        html = f.read()
    
    original = html
    
    # ── 1. GOOGLE FONTS LINK ─────────────────────────────────
    # Replace old Cormorant Garamond + Jost with DM Sans + Inter
    html = re.sub(
        r'<link\s+href="https://fonts\.googleapis\.com/css2\?family=Cormorant\+Garamond:[^"]*?&family=Jost:[^"]*?"[^>]*>',
        '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">',
        html
    )
    
    # ── 2. HEADER LOGO ───────────────────────────────────────
    # In nav/header context: logo_inbuilt_atelier.png → inbuilt_a.png
    # The header logo uses class="nav-logo" - replace only that instance
    html = html.replace(
        '<img src="/images/logo_inbuilt_atelier.png" alt="Inbuilt Atelier" class="nav-logo">',
        '<img src="/images/inbuilt_a.png" alt="Inbuilt Atelier" class="nav-logo">'
    )
    
    # ── 3. FOOTER LOGO ───────────────────────────────────────
    # In footer: logo_inbuilt_atelier.png → inbuilt_white.png (white on dark bg)
    html = html.replace(
        '<img src="/images/logo_inbuilt_atelier.png" alt="Inbuilt Atelier" class="ia-ft-logo">',
        '<img src="/images/inbuilt_white.png" alt="Inbuilt Atelier" class="ia-ft-logo">'
    )
    
    # Catch any remaining logo refs that weren't caught above
    # (some pages may have different class names or contexts)
    # Only replace if not already replaced
    if 'logo_inbuilt_atelier.png' in html:
        html = html.replace('logo_inbuilt_atelier.png', 'inbuilt_a.png')
    
    # ── 4. INLINE FONT-FAMILY REPLACEMENTS ───────────────────
    # Replace all inline Cormorant Garamond references
    html = html.replace("font-family:'Cormorant Garamond',Georgia,serif", "font-family:'DM Sans','Inter',sans-serif")
    html = html.replace("font-family: 'Cormorant Garamond', Georgia, serif", "font-family: 'DM Sans', 'Inter', sans-serif")
    html = html.replace('font-family:\'Cormorant Garamond\',Georgia,serif', "font-family:'DM Sans','Inter',sans-serif")
    
    # Replace all inline Jost references
    html = html.replace("font-family:'Jost',sans-serif", "font-family:'Inter',sans-serif")
    html = html.replace("font-family: 'Jost', sans-serif", "font-family: 'Inter', sans-serif")
    html = html.replace("font-family:'Jost', sans-serif", "font-family:'Inter',sans-serif")
    
    # ── 5. INLINE COLOR REPLACEMENTS ─────────────────────────
    # Update dark background overlays from warm charcoal to pure black
    html = html.replace('rgba(28,28,30,', 'rgba(17,17,17,')
    html = html.replace('rgba(28, 28, 30,', 'rgba(17, 17, 17,')
    
    # Update inverse text color (off-white) from warm to cool
    html = html.replace('rgba(245,242,237,', 'rgba(245,245,245,')
    html = html.replace('rgba(245, 242, 237,', 'rgba(245, 245, 245,')
    
    # ── 6. HEADING WEIGHT ADJUSTMENTS ────────────────────────
    # For sans-serif, 300 weight is too thin for headings. Update to 600.
    # Target h1/h2 inline styles that had font-weight:300 with the heading font
    html = re.sub(
        r"(font-family:'DM Sans','Inter',sans-serif;font-weight:)300(;font-size:clamp\([^)]+\);line-height:[^;]+;color:var\(--color-text-inverse\))",
        r'\g<1>600\2',
        html
    )
    html = re.sub(
        r"(font-family:'DM Sans','Inter',sans-serif;font-weight:)300(;font-size:clamp\([^)]+\);line-height:[^;]+;color:var\(--color-primary\))",
        r'\g<1>600\2',
        html
    )
    # Also catch h2 headings with slightly different format
    html = re.sub(
        r"(font-family:'DM Sans','Inter',sans-serif;font-weight:)300(;font-size:clamp\([^)]+\);color:var\(--color-primary\))",
        r'\g<1>600\2',
        html
    )
    html = re.sub(
        r"(font-family:'DM Sans','Inter',sans-serif;font-weight:)300(;font-size:clamp\([^)]+\);color:var\(--color-text-inverse\))",
        r'\g<1>600\2',
        html
    )
    
    # Values cards with large numbers (keep 300 → change to 500 for sans-serif)
    html = re.sub(
        r"(font-family:'DM Sans','Inter',sans-serif;font-size:(?:2\.5|2\.75|4)rem;font-weight:)300(;)",
        r'\g<1>500\2',
        html
    )
    
    # Update h3 weight from 400 to 500 for sans-serif
    html = re.sub(
        r"(font-family:'DM Sans','Inter',sans-serif;font-weight:)400(;font-size:1\.[34]\d*rem;color:var\(--color-)",
        r'\g<1>500\2',
        html
    )
    
    # ── 7. LETTER SPACING FOR SANS-SERIF ─────────────────────
    # Serif headings used positive letter-spacing (.02em, .04em).
    # Sans-serif headings look better with tighter or zero spacing.
    # Update the large h1 headings letter-spacing
    html = html.replace('letter-spacing:.02em', 'letter-spacing:-0.02em')
    html = html.replace('letter-spacing:0.02em', 'letter-spacing:-0.02em')
    html = html.replace('letter-spacing:.04em', 'letter-spacing:0em')
    
    # ── 8. CSS VERSION BUMP ──────────────────────────────────
    html = html.replace('styles.css?v=16', 'styles.css?v=17')
    html = html.replace('mobile.css?v=16', 'mobile.css?v=17')
    
    # ── 9. NAV-WORDMARK INLINE STYLE BLOCK ───────────────────
    # Each page has an inline <style> block with .nav-wordmark using old fonts
    # Update .nav-wordmark font 
    html = html.replace(
        ".nav-wordmark{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;letter-spacing:.18em;text-transform:uppercase",
        ".nav-wordmark{font-family:'DM Sans','Inter',sans-serif;font-weight:600;font-size:1.1rem;letter-spacing:.08em;text-transform:uppercase"
    )
    
    # Update ia-eyebrow font
    html = html.replace(
        ".ia-eyebrow{display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;",
        ".ia-eyebrow{display:inline-flex;align-items:center;gap:.75rem;font-family:'Inter',sans-serif;"
    )
    
    # Update ia-btn-primary font
    html = html.replace(
        ".ia-btn-primary{display:inline-flex;align-items:center;gap:.6rem;padding:.875rem 2rem;background:var(--color-accent);color:#fff;font-family:'Jost',sans-serif;",
        ".ia-btn-primary{display:inline-flex;align-items:center;gap:.6rem;padding:.875rem 2rem;background:var(--color-primary);color:#fff;font-family:'Inter',sans-serif;"
    )
    
    # Update step-num font
    html = html.replace(
        ".step-num{font-family:'Cormorant Garamond',Georgia,serif;",
        ".step-num{font-family:'DM Sans','Inter',sans-serif;"
    )
    
    # ── WRITE BACK ───────────────────────────────────────────
    if html != original:
        with open(filepath, 'w') as f:
            f.write(html)
        changes += 1
        print(f"  ✓ Updated: {filepath}")
    else:
        print(f"  - No changes: {filepath}")

print(f"\n✓ {changes}/{len(html_files)} files updated")
