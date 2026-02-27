#!/usr/bin/env python3
"""Download HIGH-QUALITY wardrobe and walk-in images from specific Presotto product pages."""
import os, re, urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v2_sminimal/public/images/presotto"
os.makedirs(BASE, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

# Specific product pages with high-quality lifestyle images
pages = [
    # Hinged door wardrobes - individual product pages
    "https://www.presotto.com/en/wardrobes/hinged-doors/liscia/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/newone/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/naos/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/alibi/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/glass/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/tau/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/astipalea/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/sketch-2024/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/beverly/",
    # Sliding door wardrobes
    "https://www.presotto.com/en/wardrobes/sliding-doors/step/",
    "https://www.presotto.com/en/wardrobes/sliding-doors/step-3/",
    "https://www.presotto.com/en/wardrobes/sliding-doors/loft/",
    # Walk-in / interior systems
    "https://www.presotto.com/en/wardrobes/walk-in-closets/interno/",
    "https://www.presotto.com/en/wardrobes/walk-in-closets/rimadesio/",
    # Wardrobes overview 
    "https://www.presotto.com/en/wardrobes/",
    "https://www.presotto.com/en/wardrobes/hinged-doors/",
    "https://www.presotto.com/en/wardrobes/sliding-doors/",
    "https://www.presotto.com/en/wardrobes/walk-in-closets/",
    # Night (bedroom) - contextual lifestyle shots
    "https://www.presotto.com/en/night/beds/vela/",
    "https://www.presotto.com/en/night/beds/dado/",
    "https://www.presotto.com/en/night/beds/clio/",
    # Day program - living room images
    "https://www.presotto.com/en/day/tv-units/i-modulart/",
    "https://www.presotto.com/en/day/tv-units/pari-dispari/",
    "https://www.presotto.com/en/day/sideboards/match/",
]

all_urls = set()

for url in pages:
    print(f"Scraping: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, context=ctx, timeout=20).read().decode("utf-8", errors="ignore")
        
        # Find all image URLs - both src and data-src
        imgs = re.findall(r'(?:src|data-src)=["\']?(https?://(?:www\.)?presotto\.com/wp-content/uploads/[^\s"\'<>]+\.(?:jpg|jpeg|png|webp))', html, re.IGNORECASE)
        
        # Also find CSS background images
        bg_imgs = re.findall(r'url\(["\']?(https?://(?:www\.)?presotto\.com/wp-content/uploads/[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp))', html, re.IGNORECASE)
        imgs.extend(bg_imgs)
        
        # Get full-res versions (remove dimension suffixes)
        for img in imgs:
            # Try to get full resolution by removing -WxH suffix
            full = re.sub(r'-\d{2,4}x\d{2,4}(\.\w+)$', r'\1', img)
            all_urls.add(full)
        
        print(f"  Found {len(imgs)} images")
    except Exception as e:
        print(f"  Error: {e}")

print(f"\nTotal unique URLs: {len(all_urls)}")

downloaded = 0
skipped = 0
for img_url in sorted(all_urls):
    orig_name = img_url.split("/")[-1].split("?")[0]
    # Prefix with 'wd-' for wardrobe-specific
    filename = f"wd-{orig_name}"
    filepath = os.path.join(BASE, filename)
    
    if os.path.exists(filepath):
        skipped += 1
        continue
    
    try:
        req = urllib.request.Request(img_url, headers=headers)
        data = urllib.request.urlopen(req, context=ctx, timeout=20).read()
        
        # Only save if decent size (>30KB)
        if len(data) > 30000:
            with open(filepath, "wb") as f:
                f.write(data)
            size_kb = len(data) / 1024
            print(f"  Downloaded ({size_kb:.0f}KB): {filename}")
            downloaded += 1
    except Exception as e:
        print(f"  Error: {orig_name}: {e}")

print(f"\n✅ Done! Downloaded: {downloaded}, Skipped: {skipped}")
print(f"Total files in directory:")
os.system(f'find "{BASE}" -type f -name "wd-*" | wc -l')
