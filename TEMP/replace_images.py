#!/usr/bin/env python3
"""Replace ALL Unsplash image URLs with local Presotto images across the entire site."""
import re, os, glob

BASE = "/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v2_sminimal"

# Mapping: Unsplash photo ID → local Presotto image path (relative to /images/presotto/)
# Each Unsplash URL looks like: https://images.unsplash.com/photo-XXXXX?w=...&q=...
PHOTO_MAP = {
    # Used in: offers hero, contact hero, about/index.html img src
    "photo-1600210492486-724fe5c67fb0": "about-azienda-showroom-presotto.jpg",
    
    # Used in: index.html video poster, service/ai-assistants hero  
    "photo-1558618666-fcd25c85f82e": "flagship-showroom-milano-presotto-foto-14.jpg",
    
    # Used in: index.html about section img, service/index.html hero bg
    "photo-1616486338812-3dadae4b4ace": "armadi-anta-battente-liscia-a-scaled.jpg",
    
    # Used in: styles.css parallax, about/index.html hero bg
    "photo-1600585154340-be6161a56a0c": "flagship-showroom-milano-presotto-foto-15.jpg",
    
    # Used in: privacy-policy hero, blog hero
    "photo-1497366216548-37526070297c": "about-produzione-presotto-carosello-1.jpg",
    
    # Used in: industries/hospitality hero
    "photo-1600607687644-c7171b42498f": "flagship-showroom-ny-presotto-foto-4.jpg",
    
    # Used in: industries/index.html hero
    "photo-1600566753190-17f0baa2a6c3": "homepage-pari-dispari-8-generale-b-scaled.jpg",
    
    # Used in: industries/ecommerce hero
    "photo-1600596542815-ffad4c1539a9": "flagship-showroom-thiene-presotto-foto-9.jpg",
    
    # Used in: industries/home-services hero
    "photo-1502672260266-1c1ef2d93688": "about-produzione-presotto-carosello-6.jpg",
    
    # Used in: industries/healthcare hero
    "photo-1600047509807-ba8f99d2cdde": "flagship-showroom-milano-presotto-foto-12.jpg",
    
    # Used in: industries/real-estate hero
    "photo-1600573472592-401b489a3cdc": "flagship-showroom-ny-presotto-foto-8.jpg",
    
    # Used in: industries/professional-services hero
    "photo-1600566753086-00f18fb6b3ea": "about-produzione-presotto-carosello-3.jpg",
    
    # Used in: case-studies hero, service/seo-local-seo hero
    "photo-1600585154526-d187d34e371d": "about-produzione-presotto-carosello-2.jpg",
    
    # Used in: service/index.html img - Built-in wardrobe card
    "photo-1558997519-83ea9252edf8": "armadi-anta-battente-liscia-intro-1.jpg",
    
    # Used in: service/index.html img - Walk-in wardrobe card
    "photo-1616046229478-9901c5536a45": "armadi-anta-battente-glass-anteprima-1.jpg",
    
    # Used in: service/index.html img - Joinery card
    "photo-1600607687920-4e2a09cf159d": "about-azienda-artigianalita-presotto-1-scaled.jpg",
    
    # Used in: service/index.html img - Vanity card
    "photo-1552321554-5fefe8c9ef14": "baltimora-l-balt25.jpg",
    
    # Used in: service/index.html img - Home office card
    "photo-1593062096033-9a26b09da705": "homepage-i-modul-art-1-intro.jpg",
    
    # Used in: service/index.html img - TV media wall card
    "photo-1615529182904-14819c35db37": "homepage-i-modul-art-4-generale-a-scaled.jpg",
    
    # Used in: service/social-growth hero
    "photo-1600566752355-35792bedcfea": "flagship-showroom-thiene-presotto-foto-6.jpg",
    
    # Used in: service/crm-sales-funnel hero
    "photo-1518455027359-f3f8164ba6bd": "flagship-showroom-milano-presotto-foto-4.jpg",
    
    # Used in: service/growth-strategy-analytics hero
    "photo-1600607687939-ce8a6c25118c": "about-produzione-presotto-carosello-9.jpg",
    
    # Used in: service/website-development hero
    "photo-1616594039964-ae9021a400a0": "flagship-showroom-milano-presotto-foto-2.jpg",
}

# Verify all target images exist
print("=== Verifying all target images exist ===")
all_ok = True
for photo_id, local_file in PHOTO_MAP.items():
    full_path = os.path.join(BASE, "public", "images", "presotto", local_file)
    if not os.path.exists(full_path):
        print(f"  ❌ MISSING: {local_file} (for {photo_id})")
        all_ok = False
    else:
        size_kb = os.path.getsize(full_path) / 1024
        print(f"  ✅ {local_file} ({size_kb:.0f}KB)")

if not all_ok:
    print("\n⚠️  Some images are missing! Fix before proceeding.")
    exit(1)

print(f"\n✅ All {len(PHOTO_MAP)} target images verified.\n")

# Find all HTML and CSS files (exclude backups)
html_files = []
for pattern in ["public/**/*.html", "public/css/*.css"]:
    html_files.extend(glob.glob(os.path.join(BASE, pattern), recursive=True))

# Filter out backup files
html_files = [f for f in html_files if not any(x in f for x in ['.backup', '.old-', '.bak'])]

print(f"=== Processing {len(html_files)} files ===\n")

total_replacements = 0

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    file_replacements = 0
    rel_path = os.path.relpath(filepath, BASE)
    
    for photo_id, local_file in PHOTO_MAP.items():
        # Match the full Unsplash URL including any query params
        # Pattern: https://images.unsplash.com/photo-XXXX followed by optional ?params
        pattern = re.escape(f"https://images.unsplash.com/{photo_id}") + r'[^"\');\s]*'
        
        # Determine the correct relative path based on file depth
        # Files in public/ root → /images/presotto/file.jpg
        # Files in public/about/ → /images/presotto/file.jpg
        # All use absolute paths from root
        replacement = f"/images/presotto/{local_file}"
        
        matches = re.findall(pattern, content)
        if matches:
            content = re.sub(pattern, replacement, content)
            file_replacements += len(matches)
            for m in matches:
                print(f"  {rel_path}: {photo_id[:30]}... → {local_file}")
    
    if file_replacements > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  → {file_replacements} replacement(s) in {rel_path}\n")
        total_replacements += file_replacements

print(f"\n{'='*60}")
print(f"✅ DONE! Total replacements: {total_replacements}")
print(f"{'='*60}")

# Final verification - check for any remaining Unsplash references
print(f"\n=== Verification: checking for remaining Unsplash references ===")
remaining = 0
for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = re.findall(r'unsplash\.com', content, re.IGNORECASE)
    if matches:
        rel_path = os.path.relpath(filepath, BASE)
        print(f"  ⚠️  {rel_path}: {len(matches)} remaining Unsplash reference(s)")
        remaining += len(matches)

if remaining == 0:
    print("  ✅ ZERO Unsplash references remaining! All images replaced.")
else:
    print(f"\n  ⚠️  {remaining} Unsplash references still found!")
