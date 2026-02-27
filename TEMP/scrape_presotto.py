#!/usr/bin/env python3
"""Scrape Presotto images and download them locally."""
import urllib.request
import re
import os
import ssl

# Disable SSL verification for scraping
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

IMG_DIR = '/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v2_sminimal/public/images/presotto'
os.makedirs(IMG_DIR, exist_ok=True)

def fetch_page(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"  Error fetching {url}: {e}")
        return ""

def extract_full_res_images(html):
    """Extract full-res image URLs (no dimension suffix) from srcset and src."""
    # From srcset - get the largest images (no dimension variants)
    urls = set()
    # Get all srcset URLs that end with the original filename (no -NNNxNNN)
    for m in re.finditer(r'https://www\.presotto\.com/wp-content/uploads/[^\s"\'<>]+\.(?:jpg|jpeg|png|webp)', html):
        url = m.group(0)
        # Skip thumbnails with dimension suffixes like -410x273
        if not re.search(r'-\d+x\d+\.', url):
            urls.add(url)
    return urls

# Pages to scrape
pages = [
    "https://www.presotto.com/en/",
    "https://www.presotto.com/en/product-category/wardrobes/",
    "https://www.presotto.com/en/product-category/walk-in-closet/",
    "https://www.presotto.com/en/product-category/night-space/",
    "https://www.presotto.com/en/product-category/living-space/",
    "https://www.presotto.com/en/product-category/furniture/",
    "https://www.presotto.com/en/product-category/furniture/desks/",
    "https://www.presotto.com/en/product-category/living-space/day-program/",
    "https://www.presotto.com/en/product-category/night-space/storage-units/",
    "https://www.presotto.com/en/about-us/",
    "https://www.presotto.com/en/flagship-store/",
    # Specific product pages for more variety
    "https://www.presotto.com/en/products/design-plus/",
    "https://www.presotto.com/en/products/liscia-hinged-door/",
    "https://www.presotto.com/en/products/tecnopolis/",
    "https://www.presotto.com/en/products/i-modulart-1/",
    "https://www.presotto.com/en/products/dama-letto/",
    "https://www.presotto.com/en/products/siena/",
    "https://www.presotto.com/en/products/kos/",
    "https://www.presotto.com/en/products/san-marino/",
    "https://www.presotto.com/en/products/custom-wardrobes/",
    "https://www.presotto.com/en/products/beverly-hinged-door/",
]

all_images = set()
for page_url in pages:
    print(f"Scraping: {page_url}")
    html = fetch_page(page_url)
    if html:
        imgs = extract_full_res_images(html)
        # Filter out favicons, logos
        imgs = {u for u in imgs if 'favicon' not in u and 'logo' not in u and 'cropped' not in u}
        print(f"  Found {len(imgs)} full-res images")
        all_images.update(imgs)

print(f"\nTotal unique full-res images: {len(all_images)}")

# Sort and show
for img in sorted(all_images):
    print(f"  {img}")

# Now download them all
print(f"\n--- Downloading {len(all_images)} images to {IMG_DIR} ---")
downloaded = 0
for url in sorted(all_images):
    fname = url.split('/')[-1]
    fpath = os.path.join(IMG_DIR, fname)
    if os.path.exists(fpath):
        print(f"  Skipping (exists): {fname}")
        downloaded += 1
        continue
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            data = resp.read()
        with open(fpath, 'wb') as f:
            f.write(data)
        size_kb = len(data) / 1024
        print(f"  Downloaded: {fname} ({size_kb:.0f}KB)")
        downloaded += 1
    except Exception as e:
        print(f"  FAILED: {fname} - {e}")

print(f"\nDone! Downloaded {downloaded}/{len(all_images)} images to {IMG_DIR}")
