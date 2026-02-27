#!/usr/bin/env python3
"""Download wardrobe images from correct Presotto URLs."""
import os, re, urllib.request, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

BASE = "/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v2_sminimal/public/images/presotto"
os.makedirs(BASE, exist_ok=True)

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

# Correct URLs from the sitemap
pages = [
    "https://www.presotto.com/en/product-category/wardrobes/",
    "https://www.presotto.com/en/product-category/wardrobes/hinged-door/",
    "https://www.presotto.com/en/product-category/wardrobes/sliding-door/",
    "https://www.presotto.com/en/product-category/wardrobes/coplanar-door/",
    "https://www.presotto.com/en/product-category/walk-in-closet/",
    "https://www.presotto.com/en/products/custom-wardrobes/",
    "https://www.presotto.com/en/product-category/night-space/",
    "https://www.presotto.com/en/product-category/living-space/day-program/",
    "https://www.presotto.com/en/products/i-modulart-1/",
    "https://www.presotto.com/en/craftsmanship/",
    "https://www.presotto.com/en/look-mood/",
]

all_urls = set()

for url in pages:
    print(f"Scraping: {url}")
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, context=ctx, timeout=20).read().decode("utf-8", errors="ignore")
        
        # Find ALL image URLs (src, data-src, srcset, CSS backgrounds)
        patterns = [
            r'(?:src|data-src|data-lazy-src)=["\']?(https?://(?:www\.)?presotto\.com/wp-content/uploads/[^\s"\'<>]+\.(?:jpg|jpeg|png|webp))',
            r'url\(["\']?(https?://(?:www\.)?presotto\.com/wp-content/uploads/[^\s"\'<>)]+\.(?:jpg|jpeg|png|webp))',
            r'srcset="([^"]*presotto\.com/wp-content/uploads/[^"]*)"',
        ]
        
        imgs = []
        for pat in patterns[:2]:
            imgs.extend(re.findall(pat, html, re.IGNORECASE))
        
        # For srcset, extract individual URLs
        srcsets = re.findall(patterns[2], html, re.IGNORECASE)
        for srcset in srcsets:
            urls_in_srcset = re.findall(r'(https?://(?:www\.)?presotto\.com/wp-content/uploads/[^\s,]+)', srcset)
            imgs.extend(urls_in_srcset)
        
        # Clean up and get full-res
        for img in imgs:
            full = re.sub(r'-\d{2,4}x\d{2,4}(\.\w+)$', r'\1', img)
            all_urls.add(full)
        
        print(f"  Found {len(imgs)} images ({len(set(imgs))} unique)")
    except Exception as e:
        print(f"  Error: {e}")

print(f"\nTotal unique full-res URLs: {len(all_urls)}")

downloaded = 0
skipped_existing = 0
skipped_small = 0

for img_url in sorted(all_urls):
    orig_name = img_url.split("/")[-1].split("?")[0]
    filename = f"wd-{orig_name}"
    filepath = os.path.join(BASE, filename)
    
    if os.path.exists(filepath):
        skipped_existing += 1
        continue
    
    try:
        req = urllib.request.Request(img_url, headers=headers)
        data = urllib.request.urlopen(req, context=ctx, timeout=20).read()
        
        if len(data) > 40000:  # 40KB minimum for lifestyle photos
            with open(filepath, "wb") as f:
                f.write(data)
            size_kb = len(data) / 1024
            print(f"  Downloaded ({size_kb:.0f}KB): {filename}")
            downloaded += 1
        else:
            skipped_small += 1
    except Exception as e:
        pass  # Silent fail to keep output clean

print(f"\n✅ Downloaded: {downloaded}, Existing: {skipped_existing}, Too small: {skipped_small}")
