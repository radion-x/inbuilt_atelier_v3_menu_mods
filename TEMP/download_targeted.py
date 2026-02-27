#!/usr/bin/env python3
"""Download targeted Presotto images for specific use cases."""
import os, re, urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v2_sminimal/public/images/presotto"
os.makedirs(BASE, exist_ok=True)

# Targeted pages for each category we need
pages = {
    # Walk-in closets
    "https://www.presotto.com/en/wardrobes/walk-in-closets/": "walkin",
    # Night/bedroom 
    "https://www.presotto.com/en/night/": "night",
    "https://www.presotto.com/en/night/beds/": "beds",
    "https://www.presotto.com/en/night/bedside-tables/": "bedside",
    # Day/living room
    "https://www.presotto.com/en/day/": "day",
    "https://www.presotto.com/en/day/tv-units/": "tvunits",
    "https://www.presotto.com/en/day/bookcases/": "bookcases",
    "https://www.presotto.com/en/day/sideboards/": "sideboards",
    # Wardrobes - sliding doors (different from hinged we already have)
    "https://www.presotto.com/en/wardrobes/sliding-doors/": "sliding",
    # About / showroom for hero-quality shots
    "https://www.presotto.com/en/about-us/": "about",
    "https://www.presotto.com/en/flagship-store/": "flagship",
    # Homepage for hero-quality shots
    "https://www.presotto.com/en/": "homepage",
}

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

all_urls = set()

for url, prefix in pages.items():
    print(f"\n--- Scraping: {url} ({prefix}) ---")
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, context=ctx, timeout=15).read().decode("utf-8", errors="ignore")
        
        # Find all image URLs from wp-content/uploads - get full-res versions
        imgs = re.findall(r'https?://(?:www\.)?presotto\.com/wp-content/uploads/[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', html, re.IGNORECASE)
        
        # Filter for full-res (no dimension suffixes like -300x200)
        full_res = []
        for img in imgs:
            # Skip thumbnails/resized
            if re.search(r'-\d{2,4}x\d{2,4}\.', img):
                continue
            full_res.append(img)
        
        # Also get resized if no full-res found
        if not full_res:
            full_res = imgs[:10]
        
        # Deduplicate
        unique = list(dict.fromkeys(full_res))
        print(f"  Found {len(unique)} full-res images")
        
        for img_url in unique:
            all_urls.add((img_url, prefix))
            
    except Exception as e:
        print(f"  Error: {e}")

print(f"\n\nTotal unique URLs to download: {len(all_urls)}")

downloaded = 0
skipped = 0
for img_url, prefix in all_urls:
    # Create filename with prefix for easy identification
    orig_name = img_url.split("/")[-1].split("?")[0]
    filename = f"{prefix}-{orig_name}"
    filepath = os.path.join(BASE, filename)
    
    if os.path.exists(filepath):
        skipped += 1
        continue
    
    try:
        req = urllib.request.Request(img_url, headers=headers)
        data = urllib.request.urlopen(req, context=ctx, timeout=15).read()
        
        # Only save if decent size (>20KB - skip tiny icons)
        if len(data) > 20000:
            with open(filepath, "wb") as f:
                f.write(data)
            size_kb = len(data) / 1024
            print(f"  Downloaded ({size_kb:.0f}KB): {filename}")
            downloaded += 1
        else:
            print(f"  Skipped (too small {len(data)}B): {filename}")
    except Exception as e:
        print(f"  Error downloading {orig_name}: {e}")

print(f"\n✅ Done! Downloaded: {downloaded}, Skipped (existing): {skipped}")
