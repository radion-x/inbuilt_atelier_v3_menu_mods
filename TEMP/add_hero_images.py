#!/usr/bin/env python3
"""
Add high-quality hero background images to all inner pages.
Uses Unsplash images with dark gradient overlays for text readability.
"""

import os
import re

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public')

# Curated Unsplash images for each page theme
# Format: path -> (unsplash_photo_id, focus_position)
HERO_IMAGES = {
    # About
    'about/index.html': (
        'photo-1600585154340-be6161a56a0c',  # Luxury modern house
        'center 40%'
    ),
    # Contact
    'contact/index.html': (
        'photo-1600210492486-724fe5c67fb0',  # Modern luxury interior
        'center center'
    ),
    # Services Overview
    'service/index.html': (
        'photo-1616486338812-3dadae4b4ace',  # Modern minimalist interior
        'center 35%'
    ),
    # Built-In Wardrobes
    'service/ai-assistants/index.html': (
        'photo-1558618666-fcd25c85f82e',  # Walk-in wardrobe luxury
        'center center'
    ),
    # Walk-In Wardrobes
    'service/website-development/index.html': (
        'photo-1616594039964-ae9021a400a0',  # Modern wardrobe system
        'center 45%'
    ),
    # Joinery & Cabinetry
    'service/seo-local-seo/index.html': (
        'photo-1600585154526-d187d34e371d',  # Kitchen joinery
        'center center'
    ),
    # Vanities
    'service/social-growth/index.html': (
        'photo-1600566752355-35792bedcfea',  # Luxury bathroom
        'center center'
    ),
    # Home Office
    'service/crm-sales-funnel/index.html': (
        'photo-1518455027359-f3f8164ba6bd',  # Elegant home office
        'center 40%'
    ),
    # TV Units & Media
    'service/growth-strategy-analytics/index.html': (
        'photo-1600607687939-ce8a6c25118c',  # Luxury living room
        'center center'
    ),
    # Spaces Overview
    'industries/index.html': (
        'photo-1600566753190-17f0baa2a6c3',  # Modern interior design
        'center 40%'
    ),
    # New Builds
    'industries/healthcare/index.html': (
        'photo-1600047509807-ba8f99d2cdde',  # Modern new build home
        'center center'
    ),
    # Renovations
    'industries/real-estate/index.html': (
        'photo-1600573472592-401b489a3cdc',  # Renovated interior
        'center 35%'
    ),
    # Apartments
    'industries/home-services/index.html': (
        'photo-1502672260266-1c1ef2d93688',  # Apartment living space
        'center center'
    ),
    # Prestige Homes
    'industries/hospitality/index.html': (
        'photo-1600607687644-c7171b42498f',  # Prestige luxury interior
        'center 40%'
    ),
    # Family Homes
    'industries/professional-services/index.html': (
        'photo-1600566753086-00f18fb6b3ea',  # Warm family living
        'center center'
    ),
    # Builders & Developers
    'industries/ecommerce/index.html': (
        'photo-1600596542815-ffad4c1539a9',  # Modern development
        'center 35%'
    ),
    # Blog / Journal
    'blog/index.html': (
        'photo-1497366216548-37526070297c',  # Elegant desk / editorial
        'center center'
    ),
    # Case Studies / Projects
    'case-studies/index.html': (
        'photo-1600585154526-d187d34e371d',  # Interior project
        'center 40%'
    ),
    # Offers / Consultation
    'offers/index.html': (
        'photo-1600210492486-724fe5c67fb0',  # Luxury consultation space
        'center center'
    ),
    # Privacy Policy
    'privacy-policy-2/index.html': (
        'photo-1497366216548-37526070297c',  # Office / document
        'center center'
    ),
}


def make_image_url(photo_id):
    """Build Unsplash CDN URL optimised for hero backgrounds."""
    return f'https://images.unsplash.com/{photo_id}?w=1920&q=80&fit=crop&auto=format'


def update_inner_page(filepath, photo_id, position):
    """Replace the gradient overlay div in inner-page heroes with image + overlay."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    img_url = make_image_url(photo_id)

    # Pattern 1: Match the radial-gradient overlay div used in inner pages
    # These look like: <div style="position:absolute;inset:0;background:radial-gradient(...);pointer-events:none;"></div>
    old_pattern = re.compile(
        r'<div\s+style="position:absolute;inset:0;background:radial-gradient\([^"]+\);pointer-events:none;"></div>'
    )

    new_div = (
        f'<div style="position:absolute;inset:0;'
        f'background:linear-gradient(160deg,rgba(28,28,30,.82) 0%,rgba(28,28,30,.88) 100%),'
        f"url('{img_url}');"
        f'background-size:cover;background-position:{position};pointer-events:none;"></div>'
    )

    new_content, count = old_pattern.subn(new_div, content)

    if count == 0:
        # Try alternate pattern with slightly different format
        old_pattern2 = re.compile(
            r'<div\s+style="position:absolute;inset:0;background:\s*radial-gradient\([^"]+\);\s*pointer-events:none;"\s*></div>'
        )
        new_content, count = old_pattern2.subn(new_div, content)

    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  [OK] {filepath} — hero image added ({count} replacement{'s' if count > 1 else ''})")
    else:
        print(f"  [SKIP] {filepath} — no matching gradient pattern found")

    return count > 0


def main():
    print("=" * 60)
    print("Adding Hero Background Images to All Pages")
    print("=" * 60)

    success = 0
    skipped = 0

    for rel_path, (photo_id, position) in HERO_IMAGES.items():
        filepath = os.path.join(BASE, rel_path)
        if not os.path.exists(filepath):
            print(f"  [MISS] {rel_path} — file not found")
            skipped += 1
            continue

        if update_inner_page(filepath, photo_id, position):
            success += 1
        else:
            skipped += 1

    print()
    print(f"Done: {success} pages updated, {skipped} skipped")
    print("=" * 60)


if __name__ == '__main__':
    main()
