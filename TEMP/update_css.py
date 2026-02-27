#!/usr/bin/env python3
"""Update styles.css design tokens and key component styles for the modern minimalist redesign."""
import re, shutil

CSS_PATH = 'public/css/styles.css'

# Backup
shutil.copy2(CSS_PATH, CSS_PATH + '.pre-redesign')

with open(CSS_PATH, 'r') as f:
    css = f.read()

# ── 1. ROOT VARIABLES ────────────────────────────────────────
# Color updates
replacements = {
    # Primary palette
    "--color-primary: #1C1C1E;": "--color-primary: #111111;",
    "--color-primary-light: #2E2E30;": "--color-primary-light: #1a1a1a;",
    "--color-copper: #C4A882;": "--color-copper: #B8A080;",
    "--color-bg-body: #F7F4EF;": "--color-bg-body: #FAFAFA;",
    "--color-text-main: #2C2C2E;": "--color-text-main: #1A1A1A;",
    "--color-text-secondary: #6B6B6B;": "--color-text-secondary: #727272;",
    "--color-text-inverse: #F5F2ED;": "--color-text-inverse: #F5F5F5;",
    
    # Legacy bg
    "--bg-accent: #EDE9E2;": "--bg-accent: #F0F0F0;",
    "--bg-hover: #EAE6DF;": "--bg-hover: #ECECEC;",
    "--text-tertiary: #9B9B9B;": "--text-tertiary: #999999;",
    
    # Gradient accent - simpler
    "--gradient-accent: linear-gradient(135deg, var(--color-accent) 0%, var(--color-copper) 100%);":
        "--gradient-accent: linear-gradient(135deg, var(--color-accent) 0%, var(--color-accent-hover) 100%);",
    
    # Borders - neutral grey
    "--border-light: 1px solid #E2DDD6;": "--border-light: 1px solid #E5E5E5;",
    "--border-medium: 1px solid #CEC8BE;": "--border-medium: 1px solid #D4D4D4;",
    "--border-glass: 1px solid rgba(255, 255, 255, 0.2);": "--border-glass: 1px solid rgba(0, 0, 0, 0.06);",
    
    # Shadows - softer
    "--shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.06);": "--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.04);",
    "--shadow-md: 0 4px 8px -2px rgba(0, 0, 0, 0.10);": "--shadow-md: 0 4px 12px -2px rgba(0, 0, 0, 0.06);",
    "--shadow-lg: 0 12px 24px -4px rgba(0, 0, 0, 0.13);": "--shadow-lg: 0 12px 32px -4px rgba(0, 0, 0, 0.08);",
    "--shadow-xl: 0 24px 48px -8px rgba(0, 0, 0, 0.18);": "--shadow-xl: 0 24px 48px -8px rgba(0, 0, 0, 0.10);",
    "--shadow-accent: 0 8px 24px rgba(155, 128, 96, 0.22);": "--shadow-accent: 0 8px 24px rgba(155, 128, 96, 0.12);",
    "--glass-blur: blur(12px);": "--glass-blur: blur(16px);",
    "--bg-surface-hover: #F9F7F3;": "--bg-surface-hover: #F5F5F5;",
    
    # Typography
    "--font-heading: 'Cormorant Garamond', 'Georgia', serif;": "--font-heading: 'DM Sans', 'Inter', system-ui, sans-serif;",
    "--font-body: 'Jost', 'Inter', system-ui, sans-serif;": "--font-body: 'Inter', system-ui, sans-serif;",
    
    # Radius - slightly larger
    "--radius-sm: 4px;": "--radius-sm: 6px;",
    "--radius-md: 8px;": "--radius-md: 10px;",
    "--radius-lg: 14px;": "--radius-lg: 16px;",
    "--radius-xl: 20px;": "--radius-xl: 24px;",
    
    # Remove glow/neon
    "--shadow-glow: 0 0 32px rgba(155, 128, 96, 0.18);": "--shadow-glow: 0 8px 32px rgba(0, 0, 0, 0.06);",
    "--shadow-neon: 0 0 12px rgba(155, 128, 96, 0.3), 0 0 24px rgba(155, 128, 96, 0.15);": "--shadow-neon: 0 4px 16px rgba(0, 0, 0, 0.08);",
}

for old, new in replacements.items():
    css = css.replace(old, new)

# ── 2. TYPOGRAPHY ────────────────────────────────────────────
# Update heading font weights for modern sans-serif
css = css.replace(
    """h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    color: var(--color-primary);
    font-weight: 400;
    line-height: 1.1;
    letter-spacing: 0.01em;
    margin-bottom: 0.75rem;
}""",
    """h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    color: var(--color-primary);
    font-weight: 600;
    line-height: 1.1;
    letter-spacing: -0.02em;
    margin-bottom: 0.75rem;
}""")

css = css.replace(
    """h1 {
    font-size: clamp(2.75rem, 6vw, 5rem);
    margin-bottom: 1.25rem;
    font-weight: 300;
    letter-spacing: 0.02em;
}""",
    """h1 {
    font-size: clamp(2.75rem, 6vw, 5rem);
    margin-bottom: 1.25rem;
    font-weight: 600;
    letter-spacing: -0.03em;
}""")

css = css.replace(
    """h2 {
    font-size: clamp(2.25rem, 4.5vw, 3.75rem);
    font-weight: 400;
}""",
    """h2 {
    font-size: clamp(2.25rem, 4.5vw, 3.75rem);
    font-weight: 600;
    letter-spacing: -0.02em;
}""")

# ── 3. BUTTONS ───────────────────────────────────────────────
# Primary button - pill shape, solid color, no gradient shine
css = css.replace(
    """.btn-primary {
    background: var(--gradient-accent);
    color: white;
    box-shadow: var(--shadow-accent);
    border: none;
}""",
    """.btn-primary {
    background: var(--color-primary);
    color: white;
    box-shadow: none;
    border: none;
    border-radius: var(--radius-full);
}""")

# Remove btn-primary shine pseudo-element
css = css.replace(
    """.btn-primary::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
    transition: left 0.6s var(--ease-smooth);
}""",
    """.btn-primary::before {
    display: none;
}""")

css = css.replace(
    """.btn-primary:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 32px rgba(200, 85, 61, 0.35);
}""",
    """.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
    background: var(--color-primary-light);
}""")

# Secondary button - outlined pill
css = css.replace(
    """.btn-secondary {
    background: white;
    border: 2px solid var(--color-primary);
    color: var(--color-primary);
    font-weight: 600;
}""",
    """.btn-secondary {
    background: transparent;
    border: 2px solid var(--color-primary);
    color: var(--color-primary);
    font-weight: 500;
    border-radius: var(--radius-full);
}""")

# Fix duplicate .btn-secondary:hover - remove the second one that overrides with accent color
css = css.replace(
    """.btn-secondary:hover {
    background: var(--color-primary);
    color: white;
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.btn-secondary:hover {
    background: var(--bg-surface);
    border-color: var(--accent-indigo);
    color: var(--accent-indigo);
    transform: translateY(-2px);
}""",
    """.btn-secondary:hover {
    background: var(--color-primary);
    color: white;
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}""")

# Base btn - pill shape
css = css.replace(
    """.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 1.1rem 2.25rem;
    border-radius: var(--radius-md);
    font-weight: 600;
    font-size: 1rem;
    font-family: var(--font-body);
    text-decoration: none;
    transition: all 0.3s var(--ease-smooth);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    border: none;
    letter-spacing: 0.01em;
}""",
    """.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 0.875rem 2rem;
    border-radius: var(--radius-full);
    font-weight: 500;
    font-size: 0.9rem;
    font-family: var(--font-body);
    text-decoration: none;
    transition: all 0.3s var(--ease-smooth);
    position: relative;
    overflow: hidden;
    cursor: pointer;
    border: none;
    letter-spacing: 0.02em;
    text-transform: uppercase;
}""")

# ── 4. HEADER ────────────────────────────────────────────────
# Refine header glass effect
css = css.replace(
    """header {
    position: fixed;
    top: 20px; /* Add some space from the top */
    left: 50%;
    transform: translateX(-50%);
    width: 95%;
    max-width: 1200px; /* Max-width for larger screens */
    z-index: 1000;
    height: 70px; /* Adjust height */
    display: flex;
    align-items: center;
    background-color: rgba(255, 255, 255, 0.9); /* Glassmorphism effect */
    -webkit-backdrop-filter: blur(10px);
    backdrop-filter: blur(10px);
    border-radius: 12px; /* Rounded corners */
    border: 1px solid rgba(0, 0, 0, 0.07);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1); /* Softer shadow */
    padding: 0 1.5rem; /* Adjust padding */
    transition: all 0.3s ease;
}""",
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
}""")

# ── 5. DROPDOWN ──────────────────────────────────────────────
# Light dropdown instead of dark
css = css.replace(
    """.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%) translateY(8px);
    background: rgba(28, 28, 30, 0.96);
    -webkit-backdrop-filter: blur(24px);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(155, 128, 96, 0.15);
    border-radius: 12px;
    padding: 0.75rem 0;
    min-width: 220px;
    opacity: 0;
    visibility: hidden;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.35), 0 0 0 1px rgba(155, 128, 96, 0.08);
    display: flex;
    flex-direction: column;
    z-index: 1001;
    list-style: none;
    margin: 0;
}""",
    """.dropdown-menu {
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translateX(-50%) translateY(8px);
    background: rgba(255, 255, 255, 0.98);
    -webkit-backdrop-filter: blur(24px);
    backdrop-filter: blur(24px);
    border: 1px solid rgba(0, 0, 0, 0.06);
    border-radius: var(--radius-lg);
    padding: 0.5rem 0;
    min-width: 220px;
    opacity: 0;
    visibility: hidden;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
    display: flex;
    flex-direction: column;
    z-index: 1001;
    list-style: none;
    margin: 0;
}""")

# Dropdown links - dark text on light bg
css = css.replace(
    """.dropdown-menu a {
    display: block;
    padding: 0.6rem 1.25rem;
    color: rgba(245, 242, 237, 0.7);
    font-family: 'Jost', sans-serif;
    font-size: 0.88rem;
    font-weight: 300;
    letter-spacing: 0.02em;
    text-decoration: none;
    transition: all 0.2s ease;
    border-bottom: none;
    white-space: nowrap;
}""",
    """.dropdown-menu a {
    display: block;
    padding: 0.55rem 1.25rem;
    color: var(--color-text-secondary);
    font-family: var(--font-body);
    font-size: 0.88rem;
    font-weight: 400;
    letter-spacing: 0.01em;
    text-decoration: none;
    transition: all 0.2s ease;
    border-bottom: none;
    white-space: nowrap;
}""")

css = css.replace(
    """.dropdown-menu a:hover {
    color: var(--color-copper);
    background: rgba(155, 128, 96, 0.08);
    padding-left: 1.5rem;
    border-bottom: none;
}""",
    """.dropdown-menu a:hover {
    color: var(--color-primary);
    background: rgba(0, 0, 0, 0.03);
    padding-left: 1.5rem;
    border-bottom: none;
}""")

# ── 6. ANIMATION CLEANUP ────────────────────────────────────
# Remove orange glow pulse (legacy handyman color)
css = css.replace(
    """@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 24px rgba(200, 85, 61, 0.25); }
    50% { box-shadow: 0 0 40px rgba(200, 85, 61, 0.45); }
}""",
    """@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 24px rgba(155, 128, 96, 0.15); }
    50% { box-shadow: 0 0 32px rgba(155, 128, 96, 0.25); }
}""")

# ── 7. GLASS CARD ────────────────────────────────────────────
css = css.replace(
    """.glass-card:hover {
    background: var(--bg-surface-hover);
    border: var(--border-glass-hover);
    transform: translateY(-5px);
    box-shadow: var(--shadow-glow);""",
    """.glass-card:hover {
    background: var(--bg-surface-hover);
    border: var(--border-glass-hover);
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);""")

# ── 8. NAV LINKS ────────────────────────────────────────────
# Update nav links to use font-body variable
css = css.replace(
    """.nav-links a {
    font-weight: 500;
    color: var(--color-text-main);
    font-size: 1rem;
    text-decoration: none;
    padding-bottom: 5px;
    border-bottom: 2px solid transparent;
    transition: all 0.2s ease;
}

.nav-links a:hover, .nav-links a.active {
    color: var(--color-primary);
    border-bottom-color: var(--color-accent);
}""",
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
}""")

# ── WRITE ────────────────────────────────────────────────────
with open(CSS_PATH, 'w') as f:
    f.write(css)

print("✓ styles.css updated successfully")
print(f"  Backup saved to: {CSS_PATH}.pre-redesign")
