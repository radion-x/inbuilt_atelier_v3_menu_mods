#!/usr/bin/env python3
"""Replace footer HTML on all 21 public pages with new premium .ia-ft footer."""
import re, os, glob

BASE = os.path.join(os.path.dirname(__file__), '..', 'public')

NEW_FOOTER = '''<footer class="ia-ft">
  <div class="container">
    <div class="ia-ft-rule"></div>
    <div class="ia-ft-brand">
      <img src="/images/logo_inbuilt_atelier.png" alt="Inbuilt Atelier" class="ia-ft-logo">
      <span class="ia-ft-wordmark">Inbuilt Atelier</span>
      <span class="ia-ft-tagline">Bespoke Joinery &amp; Wardrobes &middot; Double Bay</span>
    </div>
    <nav class="ia-ft-nav">
      <a href="/service/ai-assistants/">Built-In Wardrobes</a>
      <a href="/service/website-development/">Walk-In Wardrobes</a>
      <a href="/service/seo-local-seo/">Joinery &amp; Cabinetry</a>
      <a href="/service/social-growth/">Vanities</a>
      <a href="/service/crm-sales-funnel/">Home Office</a>
      <a href="/service/growth-strategy-analytics/">TV Units &amp; Media</a>
    </nav>
    <div class="ia-ft-contact">
      <div class="ia-ft-contact-item">
        <span class="ia-ft-contact-label">Studio</span>
        <span>Studio 7, 369&ndash;371 New South Head Rd<br>Double Bay NSW 2029</span>
      </div>
      <div class="ia-ft-contact-item">
        <span class="ia-ft-contact-label">Telephone</span>
        <a href="tel:+61417431124">0417 431 124</a>
      </div>
      <div class="ia-ft-contact-item">
        <span class="ia-ft-contact-label">Email</span>
        <a href="mailto:marina@inbuiltatelier.com.au">marina@inbuiltatelier.com.au</a>
      </div>
      <div class="ia-ft-contact-item">
        <span class="ia-ft-contact-label">Hours</span>
        <span>Mon &ndash; Fri 9 am &ndash; 5 pm<br>Sat 10 am &ndash; 2 pm</span>
      </div>
    </div>
    <div class="ia-ft-bottom">
      <p>&copy; 2025 Inbuilt Atelier Pty Ltd. All rights reserved.</p>
      <a href="/privacy-policy-2/">Privacy Policy</a>
    </div>
  </div>
</footer>'''

# Pattern matches <footer ...> through </footer> (greedy across newlines)
FOOTER_RE = re.compile(r'<footer[\s][^>]*>.*?</footer>', re.DOTALL)

files = glob.glob(os.path.join(BASE, '**/index.html'), recursive=True)
# Exclude admin pages
files = [f for f in files if '/admin/' not in f]

replaced = 0
skipped = []

for fpath in sorted(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = list(FOOTER_RE.finditer(content))
    if not matches:
        skipped.append(fpath)
        continue
    
    # Replace the LAST footer match (in case there are multiple footer-like elements)
    # We want the main site footer which is always the last <footer> in the file
    last_match = matches[-1]
    new_content = content[:last_match.start()] + NEW_FOOTER + content[last_match.end():]
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    rel = os.path.relpath(fpath, BASE)
    replaced += 1
    print(f"  ✅ {rel}")

print(f"\n{'='*50}")
print(f"Replaced: {replaced} files")
if skipped:
    print(f"Skipped (no footer found): {len(skipped)}")
    for s in skipped:
        print(f"    ⚠️  {os.path.relpath(s, BASE)}")
