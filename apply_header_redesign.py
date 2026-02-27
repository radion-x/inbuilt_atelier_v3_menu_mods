#!/usr/bin/env python3
"""
Premium header redesign — transparent-to-solid full-width bar.
Run from project root:  python3 apply_header_redesign.py
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
PUBLIC = os.path.join(BASE, "public")
ok = 0
fail = 0


def replace_in_file(filepath, old, new, label=""):
    global ok, fail
    with open(filepath, "r") as f:
        content = f.read()
    if old not in content:
        print(f"  ⚠️  NOT FOUND [{label}] in {os.path.relpath(filepath, BASE)}")
        fail += 1
        return False
    content = content.replace(old, new, 1)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  ✅  [{label}] {os.path.relpath(filepath, BASE)}")
    ok += 1
    return True


def insert_after(filepath, marker, insertion, label=""):
    global ok, fail
    with open(filepath, "r") as f:
        content = f.read()
    if marker not in content:
        print(f"  ⚠️  MARKER NOT FOUND [{label}] in {os.path.relpath(filepath, BASE)}")
        fail += 1
        return False
    content = content.replace(marker, marker + insertion, 1)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  ✅  [{label}] {os.path.relpath(filepath, BASE)}")
    ok += 1
    return True


def insert_before(filepath, marker, insertion, label=""):
    global ok, fail
    with open(filepath, "r") as f:
        content = f.read()
    if marker not in content:
        print(f"  ⚠️  MARKER NOT FOUND [{label}] in {os.path.relpath(filepath, BASE)}")
        fail += 1
        return False
    content = content.replace(marker, insertion + marker, 1)
    with open(filepath, "w") as f:
        f.write(content)
    print(f"  ✅  [{label}] {os.path.relpath(filepath, BASE)}")
    ok += 1
    return True


STYLES = os.path.join(PUBLIC, "css", "styles.css")
MOBILE = os.path.join(PUBLIC, "css", "mobile.css")
MAINJS = os.path.join(PUBLIC, "js", "main.js")

# ═══════════════════════════════════════════════
# 1. styles.css — Replace header block
# ═══════════════════════════════════════════════
print("\n── 1. Replace header CSS ──")

replace_in_file(STYLES,
"""header {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 95%;
    max-width: 1200px;
    z-index: 1000;
    height: 64px;
    display: flex;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.92);
    -webkit-backdrop-filter: blur(20px);
    backdrop-filter: blur(20px);
    border-radius: var(--radius-full);
    border: 1px solid rgba(0, 0, 0, 0.04);
    box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
    padding: 0 2rem;
    transition: all 0.3s ease;
}""",
"""header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    max-width: none;
    z-index: 1000;
    height: 72px;
    display: flex;
    align-items: center;
    background: transparent;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 0;
    box-shadow: none;
    padding: 0 3rem;
    transition: background 0.4s ease, border-color 0.4s ease, box-shadow 0.4s ease;
    transform: none;
}

/* Scrolled state: solid white bar */
header.header-solid {
    background: rgba(255, 255, 255, 0.97);
    -webkit-backdrop-filter: blur(20px);
    backdrop-filter: blur(20px);
    border-bottom-color: rgba(0, 0, 0, 0.06);
    box-shadow: 0 1px 8px rgba(0, 0, 0, 0.04);
}""",
    label="header block")


# ═══════════════════════════════════════════════
# 2. styles.css — Replace nav link styles
# ═══════════════════════════════════════════════
print("\n── 2. Replace nav link styles ──")

replace_in_file(STYLES,
""".nav-links a {
    font-weight: 500;
    color: var(--color-text-main);
    font-size: 0.9rem;
    text-decoration: none;
    padding-bottom: 5px;
    border-bottom: 2px solid transparent;
    transition: all 0.2s ease;
    letter-spacing: 0.01em;
}

.nav-links a:hover, .nav-links a.active {
    color: var(--color-primary);
    border-bottom-color: var(--color-accent);
}""",
""".nav-links a {
    font-weight: 400;
    color: rgba(255, 255, 255, 0.85);
    font-size: 0.82rem;
    text-decoration: none;
    padding-bottom: 2px;
    border-bottom: 1px solid transparent;
    transition: color 0.35s ease, border-color 0.35s ease;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}

.nav-links a:hover, .nav-links a.active {
    color: #fff;
    border-bottom-color: var(--color-copper);
}

/* Solid header: dark nav text */
.header-solid .nav-links a {
    color: var(--color-text-main);
}
.header-solid .nav-links a:hover,
.header-solid .nav-links a.active {
    color: var(--color-primary);
    border-bottom-color: var(--color-accent);
}""",
    label="nav links")


# ═══════════════════════════════════════════════
# 3. styles.css — Add logo filter rules
# ═══════════════════════════════════════════════
print("\n── 3. Add logo filter rules ──")

insert_after(STYLES,
""".nav-left,
.nav-logo {
    display: flex;
    align-items: center;
    grid-column: 1;
}""",
"""

/* Logo: white on transparent header, dark on solid */
.nav-logo {
    transition: filter 0.35s ease;
    filter: brightness(0) invert(1);
}
.header-solid .nav-logo {
    filter: none;
}""",
    label="logo filter")


# ═══════════════════════════════════════════════
# 4. styles.css — Replace CTA button
# ═══════════════════════════════════════════════
print("\n── 4. Replace CTA button ──")

replace_in_file(STYLES,
""".nav-cta .btn {
    padding: 0.45rem 0.9rem;
    font-size: 0.95rem;
    font-weight: 700;
    background-color: var(--color-primary);
    color: white;
    border-radius: 10px;
    transition: all 0.18s ease;
    min-width: 0; /* allow content width */
}

.nav-cta .btn:hover {
    background-color: #3b4d40;
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}""",
""".nav-cta .btn {
    padding: 0.5rem 1.25rem;
    font-size: 0.78rem;
    font-weight: 400;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    background: transparent;
    color: rgba(255, 255, 255, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 0;
    transition: color 0.35s ease, border-color 0.35s ease, background 0.35s ease;
    min-width: 0;
}

.nav-cta .btn:hover {
    color: #fff;
    border-color: rgba(255, 255, 255, 0.6);
    background: rgba(255, 255, 255, 0.06);
    transform: none;
    box-shadow: none;
}

/* Solid header: dark CTA */
.header-solid .nav-cta .btn {
    color: var(--color-text-main);
    border-color: rgba(0, 0, 0, 0.2);
}
.header-solid .nav-cta .btn:hover {
    color: var(--color-primary);
    border-color: var(--color-accent);
    background: rgba(155, 128, 96, 0.04);
}""",
    label="CTA button")


# ═══════════════════════════════════════════════
# 5. styles.css — Dropdown always dark text
# ═══════════════════════════════════════════════
print("\n── 5. Add dropdown dark text override ──")

insert_after(STYLES,
""".dropdown-menu a:hover {
    color: var(--color-primary);
    background: rgba(0, 0, 0, 0.03);
    padding-left: 1.5rem;
    border-bottom: none;
}""",
"""

/* Dropdown always uses dark text regardless of header state */
.dropdown-menu a {
    color: var(--color-text-secondary) !important;
    text-transform: none !important;
    letter-spacing: 0.01em !important;
    font-weight: 400 !important;
}
.dropdown-menu a:hover {
    color: var(--color-primary) !important;
}""",
    label="dropdown override")


# ═══════════════════════════════════════════════
# 6. styles.css — Hamburger colour + nav-phone colour
# ═══════════════════════════════════════════════
print("\n── 6. Add hamburger + nav-phone colour rules ──")

insert_before(STYLES,
"""/* 8. HERO SECTIONS */""",
"""/* Hamburger colour matches header state */
.mobile-menu-toggle span {
    background: rgba(255, 255, 255, 0.85);
    transition: background 0.35s ease;
}
.header-solid .mobile-menu-toggle span {
    background: var(--color-text-main);
}

/* Nav phone: white on transparent, dark on solid */
.nav-phone {
    color: rgba(255, 255, 255, 0.85);
}
.header-solid .nav-phone {
    color: var(--color-text-main);
}
.header-solid .nav-phone:hover {
    color: var(--color-primary);
}

""",
    label="hamburger + phone colour")


# ═══════════════════════════════════════════════
# 7. main.js — Add scroll detection at top
# ═══════════════════════════════════════════════
print("\n── 7. Add scroll detection to main.js ──")

insert_before(MAINJS,
"""/**
 * Main JavaScript file
 * Handles general website functionality
 */""",
"""/* ── Transparent → Solid header on scroll ── */
(function() {
    const header = document.querySelector('header');
    if (!header) return;
    const SCROLL_THRESHOLD = 80;
    const onScroll = () => {
        if (window.scrollY > SCROLL_THRESHOLD) {
            header.classList.add('header-solid');
        } else {
            header.classList.remove('header-solid');
        }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll(); // set initial state
})();

""",
    label="scroll detection")


# ═══════════════════════════════════════════════
# 8. mobile.css — Replace mobile header block
# ═══════════════════════════════════════════════
print("\n── 8. Replace mobile header block ──")

replace_in_file(MOBILE,
"""    /* Fixed clean header on mobile */
    header {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        max-width: none !important;
        transform: none !important;
        background: #ffffff !important;
        -webkit-backdrop-filter: none !important;
        backdrop-filter: none !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
        border-bottom: 1px solid rgba(0, 0, 0, 0.04) !important;
        padding: 0.75rem 0 !important;
        border-radius: 0 !important;
        z-index: 1000 !important;
    }""",
"""    /* Fixed clean header on mobile — transparent by default */
    header {
        position: fixed !important;
        top: 0 !important;
        left: 0 !important;
        right: 0 !important;
        width: 100% !important;
        max-width: none !important;
        transform: none !important;
        background: transparent !important;
        -webkit-backdrop-filter: none !important;
        backdrop-filter: none !important;
        box-shadow: none !important;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
        padding: 0.75rem 0 !important;
        border-radius: 0 !important;
        z-index: 1000 !important;
    }

    /* Mobile: solid header on scroll */
    header.header-solid {
        background: rgba(255, 255, 255, 0.97) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        backdrop-filter: blur(16px) !important;
        border-bottom-color: rgba(0, 0, 0, 0.06) !important;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.04) !important;
    }

    /* Mobile: logo white on transparent, dark on solid */
    .nav-logo {
        filter: brightness(0) invert(1) !important;
    }
    header.header-solid .nav-logo {
        filter: none !important;
    }""",
    label="mobile header")


# ═══════════════════════════════════════════════
# 9. mobile.css — Replace mobile hamburger colour
# ═══════════════════════════════════════════════
print("\n── 9. Replace mobile hamburger colour ──")

replace_in_file(MOBILE,
"""    .mobile-menu-toggle span {
        display: block;
        width: 22px;
        height: 2px;
        background: #1a1a2e;
        border-radius: 2px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        transform-origin: center;
    }""",
"""    .mobile-menu-toggle span {
        display: block;
        width: 22px;
        height: 2px;
        background: rgba(255, 255, 255, 0.85);
        border-radius: 2px;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        transform-origin: center;
    }

    /* Solid header: dark hamburger */
    header.header-solid .mobile-menu-toggle span {
        background: #1a1a2e;
    }""",
    label="mobile hamburger")


# ═══════════════════════════════════════════════
# 10. HTML files — Remove inline nav-wordmark header overrides
# ═══════════════════════════════════════════════
print("\n── 10. Clean inline header overrides from HTML ──")

HTML_FILES = [
    "index.html",
    "about/index.html",
    "blog/index.html",
    "case-studies/index.html",
    "contact/index.html",
    "industries/index.html",
    "industries/ecommerce/index.html",
    "industries/healthcare/index.html",
    "industries/home-services/index.html",
    "industries/hospitality/index.html",
    "industries/professional-services/index.html",
    "industries/real-estate/index.html",
    "offers/index.html",
    "privacy-policy-2/index.html",
    "service/index.html",
    "service/ai-assistants/index.html",
    "service/crm-sales-funnel/index.html",
    "service/growth-strategy-analytics/index.html",
    "service/seo-local-seo/index.html",
    "service/social-growth/index.html",
    "service/website-development/index.html",
]

# Two patterns: minified (most pages) and expanded (index.html)
PATTERNS_TO_REMOVE = [
    # Minified form
    r'\n\s*header \.nav-wordmark\{color:var\(--color-text-inverse\)\}',
    r'\n\s*header \.nav-wordmark span\{color:var\(--color-copper\)\}',
    # Expanded form (homepage)
    r'\n\s*header \.nav-wordmark \{ color: var\(--color-text-inverse\); \}',
    r'\n\s*header \.nav-wordmark span \{ color: var\(--color-copper\); \}',
]

cleaned = 0
for rel_path in HTML_FILES:
    filepath = os.path.join(PUBLIC, rel_path)
    if not os.path.exists(filepath):
        print(f"  ⚠️  File not found: {rel_path}")
        fail += 1
        continue
    with open(filepath, "r") as f:
        content = f.read()
    original = content
    for pat in PATTERNS_TO_REMOVE:
        content = re.sub(pat, "", content)
    if content != original:
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  ✅  Cleaned {rel_path}")
        cleaned += 1
    else:
        print(f"  ── No matching lines in {rel_path}")

ok += cleaned


# ═══════════════════════════════════════════════
# 11. CSS version bump: v17/v18 → v=20
# ═══════════════════════════════════════════════
print("\n── 11. Bump CSS & mobile version strings ──")

bumped = 0
for rel_path in HTML_FILES:
    filepath = os.path.join(PUBLIC, rel_path)
    if not os.path.exists(filepath):
        continue
    with open(filepath, "r") as f:
        content = f.read()
    original = content
    # Bump styles.css version
    content = re.sub(r'styles\.css\?v=\d+', 'styles.css?v=20', content)
    # Bump mobile.css version
    content = re.sub(r'mobile\.css\?v=\d+', 'mobile.css?v=20', content)
    if content != original:
        with open(filepath, "w") as f:
            f.write(content)
        bumped += 1

print(f"  ✅  Bumped {bumped} files to v=20")
ok += bumped


# ═══════════════════════════════════════════════
print(f"\n{'='*50}")
print(f"Done! ✅ {ok} successful  ⚠️ {fail} failed")
if fail:
    print("Review warnings above — some patterns may need manual adjustment.")
    sys.exit(1)
else:
    print("All edits applied. Refresh browser to see the premium header.")
