#!/usr/bin/env python3
"""Write Spaces pages for Inbuilt Atelier — all 6 spaces + overview."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = """\
<header><nav><div class="container nav-container">
  <div class="nav-left"><a href="/" class="nav-wordmark">Inbuilt Atelier<span>Double Bay &middot; Sydney</span></a></div>
  <div class="nav-center"><ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li class="nav-item-dropdown"><a href="/service/">Services &#9662;</a>
      <ul class="dropdown-menu">
        <li><a href="/service/ai-assistants/">Built-In Wardrobes</a></li>
        <li><a href="/service/website-development/">Walk-In Wardrobes</a></li>
        <li><a href="/service/seo-local-seo/">Joinery &amp; Cabinetry</a></li>
        <li><a href="/service/social-growth/">Vanities</a></li>
        <li><a href="/service/crm-sales-funnel/">Home Office</a></li>
        <li><a href="/service/growth-strategy-analytics/">TV Units &amp; Media</a></li>
      </ul>
    </li>
    <li class="nav-item-dropdown"><a href="/industries/" class="active">Spaces &#9662;</a>
      <ul class="dropdown-menu">
        <li><a href="/industries/healthcare/">New Builds</a></li>
        <li><a href="/industries/real-estate/">Renovations</a></li>
        <li><a href="/industries/home-services/">Apartments</a></li>
        <li><a href="/industries/hospitality/">Prestige Homes</a></li>
        <li><a href="/industries/professional-services/">Family Homes</a></li>
        <li><a href="/industries/ecommerce/">Builders &amp; Developers</a></li>
      </ul>
    </li>
    <li><a href="/contact/">Contact</a></li>
  </ul></div>
  <div class="nav-right">
    <div class="nav-cta"><a href="tel:+61417431124" class="btn btn-primary btn-sm">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      <span>0417&nbsp;431&nbsp;124</span>
    </a></div>
    <button class="mobile-menu-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</div></nav></header>"""

FOOTER_CHAT = """\
<footer style="background:#111112;color:rgba(245,242,237,.65);padding:4rem 0 2rem;">
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:3rem;margin-bottom:3rem;border-bottom:1px solid rgba(245,242,237,.08);padding-bottom:3rem;">
      <div>
        <span style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.5rem;letter-spacing:.18em;text-transform:uppercase;color:var(--color-text-inverse);display:block;margin-bottom:.4rem;">Inbuilt Atelier</span>
        <span style="font-family:'Jost',sans-serif;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:var(--color-copper);font-weight:500;">Bespoke Joinery &amp; Wardrobes</span>
        <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;line-height:1.8;color:rgba(245,242,237,.45);margin-top:1.25rem;">Studio 7, 369&ndash;371 New South Head Road<br>Double Bay NSW 2029</p>
      </div>
      <div>
        <h4 style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,242,237,.35);margin-bottom:1.25rem;">Services</h4>
        <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem;">
          <li><a href="/service/ai-assistants/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Built-In Wardrobes</a></li>
          <li><a href="/service/website-development/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Walk-In Wardrobes</a></li>
          <li><a href="/service/seo-local-seo/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Joinery &amp; Cabinetry</a></li>
          <li><a href="/service/social-growth/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Vanities</a></li>
          <li><a href="/service/crm-sales-funnel/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Home Office</a></li>
          <li><a href="/service/growth-strategy-analytics/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">TV Units &amp; Media</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,242,237,.35);margin-bottom:1.25rem;">Contact</h4>
        <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.75rem;">
          <li><a href="tel:+61417431124" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">0417 431 124</a></li>
          <li><a href="mailto:marina@inbuiltatelier.com.au" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">marina@inbuiltatelier.com.au</a></li>
        </ul>
      </div>
    </div>
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem;">
      <p style="font-family:'Jost',sans-serif;font-size:.8rem;font-weight:300;color:rgba(245,242,237,.28);margin:0;">&copy; 2026 Inbuilt Atelier. All rights reserved.</p>
      <a href="/privacy-policy-2/" style="font-family:'Jost',sans-serif;font-size:.8rem;font-weight:300;color:rgba(245,242,237,.28);text-decoration:none;">Privacy Policy</a>
    </div>
  </div>
</footer>
<div id="aiChatWidget" class="ai-chat-widget">
  <button id="chatToggle" class="chat-toggle" aria-label="Open chat"><span class="chat-icon"></span></button>
  <div id="chatWindow" class="chat-window hidden">
    <div class="chat-header"><h3>Chat with Inbuilt Atelier</h3>
      <div class="chat-header-actions">
        <button id="chatEmail" class="chat-email" aria-label="Save chat transcript" title="Save chat transcript"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg></button>
        <button id="chatReset" class="chat-reset" aria-label="Reset chat"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path></svg></button>
        <button id="chatClose" class="chat-close" aria-label="Close chat">&times;</button>
      </div>
    </div>
    <div id="chatMessages" class="chat-messages"></div>
    <form id="chatForm" class="chat-form">
      <input type="text" id="chatInput" placeholder="Ask about our services..." autocomplete="off" required>
      <button type="submit" aria-label="Send message">Send</button>
    </form>
  </div>
</div>
<div id="chatNudge" class="chat-nudge-container"><div class="chat-nudge-text">Questions? Ask me!</div><svg class="chat-nudge-arrow" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"><path d="M20,20 Q60,20 70,70 L60,60 M70,70 L80,60" /></svg></div>
<link rel="stylesheet" href="/css/chat-nudge.css">
<script src="/js/formHandler.js"></script>
<script src="/js/aiChat.js"></script>
<script src="/js/main.js"></script>
<script src="/js/contactModal.js"></script>
<script>document.addEventListener("DOMContentLoaded",()=>{const a=new AIChat();a.init();});</script>
</body>
</html>"""

HEAD = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://inbuiltatelier.com.au{canonical}">
    <meta property="og:title" content="{og_title}">
    <meta property="og:type" content="website">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/styles.css?v=12">
    <link rel="stylesheet" href="/css/mobile.css?v=12">
    <link rel="stylesheet" href="/css/contactModal.css">
    <style>
        .nav-wordmark{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;letter-spacing:.18em;text-transform:uppercase;color:var(--color-primary);text-decoration:none;line-height:1}}
        .nav-wordmark span{{display:block;font-size:.5rem;letter-spacing:.35em;color:var(--color-accent);font-weight:500;font-family:'Jost',sans-serif;margin-top:3px}}
        header .nav-wordmark{{color:var(--color-text-inverse)}}
        header .nav-wordmark span{{color:var(--color-copper)}}
        .feature-card{{padding:2rem;border-top:2px solid var(--color-accent)}}
        .feature-card h3{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.3rem;color:var(--color-primary);margin-bottom:.75rem}}
        .feature-card p{{font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.8}}
    </style>
</head>
<body>"""

def make_page(title, desc, canonical, og_title, eyebrow, h1_top, h1_em, intro_para,
              breadcrumb_label, bc_parent, bc_parent_href,
              col_left_html, col_right_html,
              features, # list of (h3, p)
              cta_eyebrow, cta_h2, cta_para,
              active_child_href):
    """Assemble a full spaces page."""
    # active state injection for child link
    nav_active = NAV.replace(
        f'href="{active_child_href}"',
        f'href="{active_child_href}" class="active"'
    )
    head = HEAD.format(title=title, desc=desc, canonical=canonical, og_title=og_title)
    features_html = ""
    for fh3, fp in features:
        features_html += f"""
      <div class="feature-card">
        <h3>{fh3}</h3>
        <p>{fp}</p>
      </div>"""

    return f"""{head}
{nav_active}

<section style="position:relative;min-height:55vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 45%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;">
    <nav aria-label="breadcrumb" style="margin-bottom:2rem;">
      <ol class="breadcrumb">
        <li><a href="/" style="color:rgba(245,242,237,.45);">Home</a></li>
        <li style="color:rgba(245,242,237,.45);">&middot;</li>
        <li><a href="{bc_parent_href}" style="color:rgba(245,242,237,.45);">{bc_parent}</a></li>
        <li style="color:rgba(245,242,237,.45);">&middot;</li>
        <li style="color:var(--color-copper);">{breadcrumb_label}</li>
      </ol>
    </nav>
    <div style="max-width:720px;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>{eyebrow}
      </div>
      <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
        {h1_top}<br><em style="font-style:italic;color:var(--color-copper);">{h1_em}</em>
      </h1>
      <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);max-width:620px;">{intro_para}</p>
    </div>
  </div>
</section>

<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">
      <div>{col_left_html}</div>
      <div>{col_right_html}</div>
    </div>
  </div>
</section>

<section style="padding:7rem 0;background:#fff;">
  <div class="container">
    <div style="max-width:680px;margin:0 auto 4rem;text-align:center;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>What We Deliver<span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3.5vw,2.75rem);line-height:1.1;color:var(--color-primary);">Joinery Crafted for This Space</h2>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:2rem;">
      {features_html}
    </div>
  </div>
</section>

<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:680px;margin:0 auto;">
    <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
      <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>{cta_eyebrow}<span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>
    </div>
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.25rem,4vw,3.25rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.5rem;">{cta_h2}</h2>
    <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.55);margin-bottom:2.5rem;">{cta_para}</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-primary">Book a Consultation</a>
      <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:rgba(245,242,237,.65);text-decoration:none;padding:.85rem 1.5rem;border:1px solid rgba(245,242,237,.2);">Call 0417 431 124</a>
    </div>
  </div>
</section>
{FOOTER_CHAT}"""


# ── 1. New Builds ──────────────────────────────────────────────────────────────
new_builds = make_page(
    title="New Build Joinery Sydney | Custom Wardrobes for New Homes | Inbuilt Atelier",
    desc="Bespoke built-in wardrobes and joinery for new builds in Sydney. Coordinate with your builder or architect — Inbuilt Atelier works from plans. Double Bay NSW.",
    canonical="/industries/healthcare/",
    og_title="New Build Joinery | Inbuilt Atelier",
    eyebrow="Spaces We Work In",
    h1_top="Joinery for",
    h1_em="New Builds",
    intro_para="Working from architectural plans and builder schedules, Inbuilt Atelier integrates bespoke wardrobes and fitted joinery seamlessly into new construction &mdash; before plasterers, painters, or tilers have finished their work.",
    breadcrumb_label="New Builds",
    bc_parent="Spaces",
    bc_parent_href="/industries/",
    col_left_html="""
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>The New Build Advantage
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Fitted While the Home is Being Built</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.5rem;">Engaging Inbuilt Atelier during the construction phase means your wardrobes and joinery can be designed around the exact dimensions of the space before it is locked in. No compromise, no retrofitting, no trimming.</p>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">We liaise directly with your builder and architect, attend site visits, and work to construction milestones &mdash; so everything arrives and installs on schedule with your build.</p>""",
    col_right_html="""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">100%</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Custom to Plans</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Zero</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Ugly Filler Panels</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">On-Site</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Coordination</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">10yr</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Warranty</p>
        </div>
      </div>""",
    features=[
        ("Plan-Stage Design", "We work from architectural drawings and 3D plans to design joinery that is perfectly dimensioned before a single nail goes in."),
        ("Builder Coordination", "We liaise directly with your builder, follow their programme, and install within the construction schedule — no delays, no surprises."),
        ("Floor-to-Ceiling Precision", "New builds allow true ceiling-height joinery without the need for scribe mouldings or infill strips. Everything sits flush and intentional."),
        ("Material Selection", "Timber veneer, lacquer, laminate, or stone accents &mdash; material packages chosen to complement your interior specification document."),
        ("Complete Fitout", "One team handles all joinery across the home: wardrobes, kitchen overhead cabinetry, pantry, laundry, home office &mdash; consistent quality everywhere."),
        ("Defect Rectification", "We return at practical completion to address any minor defects and ensure everything operates perfectly in the finished home."),
    ],
    cta_eyebrow="Start at the Right Stage",
    cta_h2="Engage Us Early &mdash; It Changes Everything",
    cta_para="The earlier you bring Inbuilt Atelier into your new build, the more your joinery can be designed into the architecture rather than fitted around it. Let&rsquo;s talk at the design stage.",
    active_child_href="/industries/healthcare/"
)

# ── 2. Renovations ─────────────────────────────────────────────────────────────
renovations = make_page(
    title="Renovation Joinery Sydney | Bespoke Wardrobes for Renovations | Inbuilt Atelier",
    desc="Custom joinery and wardrobes for home renovations in Sydney. Inbuilt Atelier works with existing architecture to deliver fitted storage that feels original. Double Bay NSW.",
    canonical="/industries/real-estate/",
    og_title="Renovation Joinery | Inbuilt Atelier",
    eyebrow="Spaces We Work In",
    h1_top="Joinery for",
    h1_em="Renovations",
    intro_para="Renovations demand joinery that feels like it was always part of the home. Inbuilt Atelier works closely with your architect or interior designer to produce wardrobes, cabinetry, and fitted storage that sit seamlessly within the existing fabric of your home.",
    breadcrumb_label="Renovations",
    bc_parent="Spaces",
    bc_parent_href="/industries/",
    col_left_html="""
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>The Renovation Context
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Joinery That Belongs in the Home</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.5rem;">Existing walls are rarely square. Ceiling heights change. Floors move. Renovation joinery requires measured templating, precise scribing, and an understanding of how buildings actually behave &mdash; not just how they appear on paper.</p>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">We measure each space ourselves before manufacturing a single component. Templates are made from the actual surfaces, not the architect&rsquo;s drawings. The result is joinery that fits like furniture was made for that exact room.</p>""",
    col_right_html="""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Site</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Measured Templates</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">±1mm</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Fitting Tolerance</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Dust-Free</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Factory Finish</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Staged</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Delivery Options</p>
        </div>
      </div>""",
    features=[
        ("Scribed-to-Wall Fitting", "Every panel is scribed to the actual wall surface, not the nominal dimension — so your joinery sits flush and tight even in century-old sandstone homes."),
        ("Heritage Sensitivity", "For Federation, Art Deco, and mid-century homes, we adapt our designs to complement the existing character rather than override it."),
        ("Material Matching", "Lacquer colours, timber species, and hardware can be matched to existing joinery or finishes already installed in the home."),
        ("Staged Installation", "We can stage delivery and installation to work around other trades &mdash; plumbers, electricians, tilers &mdash; minimising disruption to your renovation programme."),
        ("Demolition & Disposal", "Existing built-ins can be removed, disposed of, and replaced in a single visit where the schedule allows."),
        ("Post-Reno Touch-Ups", "We revisit after painting and flooring are complete to make any final adjustments and ensure every door and drawer operates perfectly."),
    ],
    cta_eyebrow="Renovation Projects",
    cta_h2="Let&rsquo;s Measure Your Space",
    cta_para="Send us the plans, or invite us to site. We will assess what is possible, propose options, and provide a detailed quote before any commitment is required.",
    active_child_href="/industries/real-estate/"
)

# ── 3. Apartments ──────────────────────────────────────────────────────────────
apartments = make_page(
    title="Apartment Joinery Sydney | Custom Wardrobes for Apartments | Inbuilt Atelier",
    desc="Bespoke wardrobes and joinery for Sydney apartments. Maximise every centimetre with precision-fitted storage from Inbuilt Atelier, Double Bay NSW.",
    canonical="/industries/home-services/",
    og_title="Apartment Joinery | Inbuilt Atelier",
    eyebrow="Spaces We Work In",
    h1_top="Joinery for",
    h1_em="Apartments",
    intro_para="Apartments reward clever joinery. When every square metre is valuable, built-in wardrobes and fitted storage do far more than a freestanding piece &mdash; they use the full wall height, sit flush with the architecture, and give each room a sense of considered, deliberate space.",
    breadcrumb_label="Apartments",
    bc_parent="Spaces",
    bc_parent_href="/industries/",
    col_left_html="""
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Precision in Small Spaces
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Built-Ins That Make Small Rooms Feel Larger</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.5rem;">Floor-to-ceiling joinery creates vertical emphasis and pulls the eye upward, making a room feel taller and more resolved. We design specifically for apartment proportions &mdash; narrow corridors, awkward alcoves, odd ceiling angles &mdash; and turn each constraint into an asset.</p>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">Our team manages Owners Corporation notification where required and uses lift-safe delivery methods for high-rise installations.</p>""",
    col_right_html="""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Floor</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">to Ceiling Design</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Quiet</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Soft-Close Hardware</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">OC</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Compliant Install</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">1 Day</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Typical Install Time</p>
        </div>
      </div>""",
    features=[
        ("Alcove Wardrobes", "Awkward alcoves and recessed spaces are transformed into full wardrobes &mdash; maximising depth and height while occupying space that was otherwise wasted."),
        ("Sliding Door Systems", "Space-saving sliding doors in lacquer, glass, or timber veneer &mdash; European-made tracks with soft-close mechanisms and adjustable levelling."),
        ("Mirrored Panels", "Full-length mirror panels on wardrobe fronts expand the perceived size of bedrooms and corridors without additional cost or weight."),
        ("Quiet Close Throughout", "Blum and Häfele soft-close runners on every drawer and door &mdash; essential for courteous apartment living."),
        ("Concealed Lighting", "LED strip lighting inside robes and under cabinetry, connected to a single switch &mdash; practical, warm, and visually polished."),
        ("Minimal Footprint Install", "We work cleanly, protect floors and walls, and leave no mess. Typical apartment installation is complete in a single day."),
    ],
    cta_eyebrow="Apartment Joinery",
    cta_h2="Make the Most of Every Metre",
    cta_para="Send us your floor plan or a few photos. We will come to you, measure the space, and present design concepts that show exactly how much more your apartment can offer.",
    active_child_href="/industries/home-services/"
)

# ── 4. Prestige Homes ──────────────────────────────────────────────────────────
prestige = make_page(
    title="Prestige Home Joinery Sydney | Luxury Wardrobes &amp; Cabinetry | Inbuilt Atelier",
    desc="Bespoke joinery for prestige and luxury homes in Sydney. Inbuilt Atelier delivers walk-in wardrobes, library walls, and custom cabinetry at the highest standard. Double Bay NSW.",
    canonical="/industries/hospitality/",
    og_title="Prestige Home Joinery | Inbuilt Atelier",
    eyebrow="Spaces We Work In",
    h1_top="Joinery for",
    h1_em="Prestige Homes",
    intro_para="Prestige homes demand joinery that holds its own alongside architecture, art, and interior design of the highest calibre. Inbuilt Atelier works on homes where the detail truly matters &mdash; from material specification through to the weight and sound of a closing drawer.",
    breadcrumb_label="Prestige Homes",
    bc_parent="Spaces",
    bc_parent_href="/industries/",
    col_left_html="""
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>The Prestige Standard
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Where the Craft Becomes Visible</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.5rem;">In a prestige home, joinery is not background. It is one of the first things guests notice, and one of the last things that gets specified. We approach each commission as a design project in its own right &mdash; developing material combinations and proportions that are original and resolved.</p>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">We work without compromise on hardware, edge profiles, material substrate, and finish quality. The result is joinery that looks, feels, and ages like furniture &mdash; not cabinetry.</p>""",
    col_right_html="""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Häfele</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Premium Hardware</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Stone</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Bench Upgrades</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Bespoke</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Material Packages</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">ID</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Collaboration</p>
        </div>
      </div>""",
    features=[
        ("Timber Veneer Joinery", "Natural timber veneer in American oak, walnut, and blackbutt &mdash; book-matched panels, grain-matched doors, and cathedral patterns on request."),
        ("Island Dressing Benches", "Walk-in wardrobe island benches with stone or leather inserts, soft-close drawers, and integrated jewellery trays in velvet-lined brass or bronze finishes."),
        ("Library Walls", "Floor-to-ceiling library and display walls with integrated lighting, rolling library ladders, and secret door access panels."),
        ("Interior Designer Liaison", "We work directly with your interior designer, providing material samples, CAD drawings, and 3D renders to ensure our joinery integrates with the full scheme."),
        ("Anti-Fingerprint Finishes", "Matte lacquer, satin lacquer, and textural laminates that resist marks and age gracefully &mdash; appropriate for homes that are genuinely lived in."),
        ("White Glove Installation", "Our installation teams work in gloves, protect all finished surfaces, and leave each room spotless. We treat your home as the investment it is."),
    ],
    cta_eyebrow="Prestige Projects",
    cta_h2="Let&rsquo;s Talk About Your Home",
    cta_para="Whether you are working with an interior designer or approaching us directly, we welcome the opportunity to understand your home and present a joinery proposal that truly reflects it.",
    active_child_href="/industries/hospitality/"
)

# ── 5. Family Homes ────────────────────────────────────────────────────────────
family = make_page(
    title="Family Home Joinery Sydney | Practical Built-In Wardrobes | Inbuilt Atelier",
    desc="Custom joinery and built-in wardrobes designed for family homes in Sydney. Durable, organised, and beautifully made. Inbuilt Atelier, Double Bay NSW.",
    canonical="/industries/professional-services/",
    og_title="Family Home Joinery | Inbuilt Atelier",
    eyebrow="Spaces We Work In",
    h1_top="Joinery for",
    h1_em="Family Homes",
    intro_para="Family homes demand joinery that is both beautiful and genuinely functional. We design with real family life in mind &mdash; abundant storage, durable finishes, and clever configurations that keep every room organised without looking clinical.",
    breadcrumb_label="Family Homes",
    bc_parent="Spaces",
    bc_parent_href="/industries/",
    col_left_html="""
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Built for Life
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Storage That Actually Works for Your Family</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.5rem;">The challenge in a family home is not finding space for more stuff &mdash; it is designing storage so that every member of the family knows where things go and can access them independently. Our designs place function first and layer beauty over the top.</p>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">We design wardrobes for adults and children differently, configure home office joinery around the way parents actually work, and approach laundry and mudroom cabinetry as high-use, practical spaces first.</p>""",
    col_right_html="""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">7+</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Rooms Per Home</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Tough</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Durable Substrates</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Kid</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Safe Hardware</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">10yr</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Workmanship Warranty</p>
        </div>
      </div>""",
    features=[
        ("Children&rsquo;s Wardrobes", "Adjustable interiors that grow with your children &mdash; lower hanging for small items now, easily reconfigured for full-length hanging as they get older."),
        ("Master Bedroom Wardrobes", "Generous storage for couples: double hanging, long hanging, shoe storage, drawers, and dedicated accessories sections &mdash; everything has its place."),
        ("Mudroom & Entry Joinery", "Coat hooks, shoe storage, bag cubbies, and bench seating at the entry &mdash; the joinery that absorbs the chaos before it enters the rest of the home."),
        ("Laundry Cabinetry", "Overhead cabinets, under-sink storage, pull-out hampers, and folding bench surfaces &mdash; laundry joinery that makes the least favourite room feel resolved."),
        ("Pantry Fitout", "Full pantry fitout with adjustable shelving, pull-out drawers, spice racks, and a prep bench insert &mdash; designed around how your family actually shops and cooks."),
        ("Home Office Built-Ins", "Built-in desks, reference shelving, filing drawers, and printer cabinetry &mdash; so working from home does not mean the study looks like a home office from IKEA."),
    ],
    cta_eyebrow="Family Home Projects",
    cta_h2="Tell Us About Your Home",
    cta_para="Whether you need one wardrobe or a whole-home joinery package, the process starts with a conversation about your family, your home, and how you use it. Let&rsquo;s talk.",
    active_child_href="/industries/professional-services/"
)

# ── 6. Builders & Developers ───────────────────────────────────────────────────
builders = make_page(
    title="Joinery for Builders &amp; Developers Sydney | Volume Wardrobes | Inbuilt Atelier",
    desc="Reliable joinery supply and installation for builders and property developers in Sydney. Consistent quality across every unit. Inbuilt Atelier, Double Bay NSW.",
    canonical="/industries/ecommerce/",
    og_title="Builder &amp; Developer Joinery | Inbuilt Atelier",
    eyebrow="Spaces We Work In",
    h1_top="Joinery for Builders",
    h1_em="&amp; Developers",
    intro_para="Builders and developers need a joinery partner who can deliver on time, on specification, and consistently across every unit in a project. Inbuilt Atelier has the capacity, systems, and installation discipline to perform on projects from single residences to boutique apartment blocks.",
    breadcrumb_label="Builders &amp; Developers",
    bc_parent="Spaces",
    bc_parent_href="/industries/",
    col_left_html="""
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>The Trade Partnership
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Delivery You Can Schedule Around</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.5rem;">Trade clients are taken care of from the first call. We will review your plans, propose standard specification packages, and provide fixed pricing before the contract is awarded. Delivery is staged to your construction programme and tracked by project manager.</p>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">Our installation teams are experienced in multi-unit scheduling, can service multiple sites simultaneously, and communicate directly with your site supervisor to keep the programme on track.</p>""",
    col_right_html="""
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;">
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Fixed</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Pricing per Unit</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">Multi-</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Site Capacity</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">PM</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Single Point of Contact</p>
        </div>
        <div style="padding:1.75rem;background:#fff;border:1px solid var(--border-light);text-align:center;">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.25rem;font-weight:300;color:var(--color-accent);line-height:1;margin-bottom:.5rem;">10yr</p>
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-text-secondary);">Warranty Backed</p>
        </div>
      </div>""",
    features=[
        ("Standard Specification Packages", "Pre-engineered joinery packages priced per unit type &mdash; so you can budget accurately from DA stage and provide confidence to your purchasers."),
        ("Upgrade Options", "Offer buyers upgrade options (soft-close, mirror panels, stone benchtops, integrated lighting) &mdash; additional revenue for you, added value for the purchaser."),
        ("Staged Delivery", "We stage delivery to critical path and coordinate directly with your site supervisor. Nothing arrives before you are ready for it."),
        ("Consistent Quality Across Units", "Every unit in a block receives the same material, hardware, and installation standard. No variation, no complaints at handover."),
        ("Warranty Documentation", "Warranties are issued per unit and can be transferred to purchasers at settlement &mdash; a genuine point of difference in a competitive market."),
        ("Defect Liability Period Support", "We respond promptly to any DLP defect notifications and carry out rectification work without dispute &mdash; protecting your reputation long after handover."),
    ],
    cta_eyebrow="Trade Enquiries",
    cta_h2="Supply Agreement or One-Off?",
    cta_para="Whether you need a supplier for an ongoing development programme or a single prestige project, we offer trade pricing, dedicated project management, and the quality standard your clients expect.",
    active_child_href="/industries/ecommerce/"
)


# ── 7. Spaces Overview ─────────────────────────────────────────────────────────
overview = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spaces We Work In | Wardrobes &amp; Joinery for Every Home | Inbuilt Atelier</title>
    <meta name="description" content="Inbuilt Atelier delivers bespoke joinery for new builds, renovations, apartments, prestige homes, family homes, and builders. Sydney, Double Bay NSW.">
    <link rel="canonical" href="https://inbuiltatelier.com.au/industries/">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/styles.css?v=12">
    <link rel="stylesheet" href="/css/mobile.css?v=12">
    <link rel="stylesheet" href="/css/contactModal.css">
    <style>
        .nav-wordmark{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;letter-spacing:.18em;text-transform:uppercase;color:var(--color-primary);text-decoration:none;line-height:1}}
        .nav-wordmark span{{display:block;font-size:.5rem;letter-spacing:.35em;color:var(--color-accent);font-weight:500;font-family:'Jost',sans-serif;margin-top:3px}}
        header .nav-wordmark{{color:var(--color-text-inverse)}}
        header .nav-wordmark span{{color:var(--color-copper)}}
        .space-card{{display:flex;flex-direction:column;border:1px solid var(--border-light);background:#fff;overflow:hidden;transition:border-color .3s,transform .3s;text-decoration:none;color:inherit}}
        .space-card:hover{{border-color:var(--color-accent);transform:translateY(-4px)}}
        .space-card-header{{background:var(--color-primary);padding:1.5rem 2rem;display:flex;justify-content:space-between;align-items:flex-start}}
        .space-card-num{{font-family:'Cormorant Garamond',Georgia,serif;font-size:3rem;font-weight:300;color:var(--color-copper);opacity:.5;line-height:1}}
        .space-card-body{{padding:2rem;flex:1;display:flex;flex-direction:column}}
        .space-card-body h3{{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.5rem;color:var(--color-primary);margin-bottom:.75rem;line-height:1.15}}
        .space-card-body p{{font-family:'Jost',sans-serif;font-size:.9rem;font-weight:300;color:var(--color-text-secondary);line-height:1.8;flex:1}}
        .space-card-link{{display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.78rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-accent);margin-top:1.5rem;text-decoration:none}}
    </style>
</head>
<body>
<header><nav><div class="container nav-container">
  <div class="nav-left"><a href="/" class="nav-wordmark">Inbuilt Atelier<span>Double Bay &middot; Sydney</span></a></div>
  <div class="nav-center"><ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li class="nav-item-dropdown"><a href="/service/">Services &#9662;</a>
      <ul class="dropdown-menu">
        <li><a href="/service/ai-assistants/">Built-In Wardrobes</a></li>
        <li><a href="/service/website-development/">Walk-In Wardrobes</a></li>
        <li><a href="/service/seo-local-seo/">Joinery &amp; Cabinetry</a></li>
        <li><a href="/service/social-growth/">Vanities</a></li>
        <li><a href="/service/crm-sales-funnel/">Home Office</a></li>
        <li><a href="/service/growth-strategy-analytics/">TV Units &amp; Media</a></li>
      </ul>
    </li>
    <li class="nav-item-dropdown"><a href="/industries/" class="active">Spaces &#9662;</a>
      <ul class="dropdown-menu">
        <li><a href="/industries/healthcare/">New Builds</a></li>
        <li><a href="/industries/real-estate/">Renovations</a></li>
        <li><a href="/industries/home-services/">Apartments</a></li>
        <li><a href="/industries/hospitality/">Prestige Homes</a></li>
        <li><a href="/industries/professional-services/">Family Homes</a></li>
        <li><a href="/industries/ecommerce/">Builders &amp; Developers</a></li>
      </ul>
    </li>
    <li><a href="/contact/">Contact</a></li>
  </ul></div>
  <div class="nav-right">
    <div class="nav-cta"><a href="tel:+61417431124" class="btn btn-primary btn-sm">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      <span>0417&nbsp;431&nbsp;124</span>
    </a></div>
    <button class="mobile-menu-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</div></nav></header>

<section style="position:relative;min-height:50vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 45%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;">
    <nav aria-label="breadcrumb" style="margin-bottom:2rem;">
      <ol class="breadcrumb">
        <li><a href="/" style="color:rgba(245,242,237,.45);">Home</a></li>
        <li style="color:rgba(245,242,237,.45);">&middot;</li>
        <li style="color:var(--color-copper);">Spaces</li>
      </ol>
    </nav>
    <div style="max-width:720px;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Where We Work
      </div>
      <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
        Every Space,<br><em style="font-style:italic;color:var(--color-copper);">One Standard</em>
      </h1>
      <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);max-width:620px;">
        From a studio apartment in Potts Point to a new build in Mosman, Inbuilt Atelier brings the same design rigour and quality of craft to every project, regardless of scale.
      </p>
    </div>
  </div>
</section>

<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container">
    <div style="text-align:center;max-width:600px;margin:0 auto 4.5rem;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Our Spaces<span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3.5vw,2.75rem);line-height:1.1;color:var(--color-primary);">Six Contexts, One Approach</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-top:1rem;">Each context brings its own demands. We understand all of them.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.5rem;">

      <a href="/industries/healthcare/" class="space-card">
        <div class="space-card-header">
          <span class="space-card-num">01</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="space-card-body">
          <h3>New Builds</h3>
          <p>Joinery designed from plans and installed during construction &mdash; before plasterers and painters, so everything is precision-fitted without compromise.</p>
          <span class="space-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <a href="/industries/real-estate/" class="space-card">
        <div class="space-card-header">
          <span class="space-card-num">02</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="space-card-body">
          <h3>Renovations</h3>
          <p>Site-measured and scribed to your existing walls &mdash; joinery that belongs in a renovated home and looks like it was always part of the architecture.</p>
          <span class="space-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <a href="/industries/home-services/" class="space-card">
        <div class="space-card-header">
          <span class="space-card-num">03</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="space-card-body">
          <h3>Apartments</h3>
          <p>Floor-to-ceiling precision for spaces where every centimetre matters. Sliding systems, mirrored panels, and compact configurations for inner-city living.</p>
          <span class="space-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <a href="/industries/hospitality/" class="space-card">
        <div class="space-card-header">
          <span class="space-card-num">04</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="space-card-body">
          <h3>Prestige Homes</h3>
          <p>Timber veneer, stone, and bespoke hardware &mdash; joinery as a design element, not a utility item. For homes where craft matters as much as architecture.</p>
          <span class="space-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <a href="/industries/professional-services/" class="space-card">
        <div class="space-card-header">
          <span class="space-card-num">05</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="space-card-body">
          <h3>Family Homes</h3>
          <p>Generous, practical, and durable &mdash; storage designed around how your family actually lives, from children&rsquo;s wardrobes to mudroom joinery and laundry cabinetry.</p>
          <span class="space-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <a href="/industries/ecommerce/" class="space-card">
        <div class="space-card-header">
          <span class="space-card-num">06</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="space-card-body">
          <h3>Builders &amp; Developers</h3>
          <p>Fixed pricing, staged delivery, and consistent quality for every unit in your project. Trade partnerships backed by warranty documentation for purchasers.</p>
          <span class="space-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

    </div>
  </div>
</section>

<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:680px;margin:0 auto;">
    <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
      <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Whatever Your Context<span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>
    </div>
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.25rem,4vw,3.25rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.5rem;">Let&rsquo;s Talk About Your Project</h2>
    <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.55);margin-bottom:2.5rem;">Tell us about your home, your renovation, or your development. We will listen, ask the right questions, and tell you what is possible.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-primary">Book a Consultation</a>
      <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:rgba(245,242,237,.65);text-decoration:none;padding:.85rem 1.5rem;border:1px solid rgba(245,242,237,.2);">Call 0417 431 124</a>
    </div>
  </div>
</section>
{FOOTER_CHAT}"""

pages = [
    ('industries/healthcare/index.html', new_builds),
    ('industries/real-estate/index.html', renovations),
    ('industries/home-services/index.html', apartments),
    ('industries/hospitality/index.html', prestige),
    ('industries/professional-services/index.html', family),
    ('industries/ecommerce/index.html', builders),
    ('industries/index.html', overview),
]

for rel_path, content in pages:
    target = os.path.join(BASE, 'public', rel_path)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {os.path.getsize(target):,} bytes → public/{rel_path}")
