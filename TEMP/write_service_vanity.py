#!/usr/bin/env python3
"""Write Vanities service page for Inbuilt Atelier."""
import os

COMMON = """\
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/styles.css?v=12">
    <link rel="stylesheet" href="/css/mobile.css?v=12">
    <link rel="stylesheet" href="/css/contactModal.css">
    <style>
        .nav-wordmark{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;letter-spacing:.18em;text-transform:uppercase;color:var(--color-primary);text-decoration:none;line-height:1}
        .nav-wordmark span{display:block;font-size:.5rem;letter-spacing:.35em;color:var(--color-accent);font-weight:500;font-family:'Jost',sans-serif;margin-top:3px}
        header .nav-wordmark{color:var(--color-text-inverse)}
        header .nav-wordmark span{color:var(--color-copper)}
        .feature-card{padding:2rem;border:1px solid var(--border-light);background:#fff;transition:border-color .3s,transform .3s}
        .feature-card:hover{border-color:var(--color-accent);transform:translateY(-3px)}
    </style>"""

NAV_HTML = """\
<header><nav><div class="container nav-container">
  <div class="nav-left"><a href="/" class="nav-wordmark">Inbuilt Atelier<span>Double Bay &middot; Sydney</span></a></div>
  <div class="nav-center"><ul class="nav-links">
    <li><a href="/">Home</a></li><li><a href="/about/">About</a></li>
    <li class="nav-item-dropdown"><a href="/service/" class="active">Services &#9662;</a>
      <ul class="dropdown-menu">
        <li><a href="/service/ai-assistants/">Built-In Wardrobes</a></li>
        <li><a href="/service/website-development/">Walk-In Wardrobes</a></li>
        <li><a href="/service/seo-local-seo/">Joinery &amp; Cabinetry</a></li>
        <li><a href="/service/social-growth/" class="active">Vanities</a></li>
        <li><a href="/service/crm-sales-funnel/">Home Office</a></li>
        <li><a href="/service/growth-strategy-analytics/">TV Units &amp; Media</a></li>
      </ul>
    </li>
    <li class="nav-item-dropdown"><a href="/industries/">Spaces &#9662;</a>
      <ul class="dropdown-menu">
        <li><a href="/industries/healthcare/">New Builds</a></li><li><a href="/industries/real-estate/">Renovations</a></li>
        <li><a href="/industries/home-services/">Apartments</a></li><li><a href="/industries/hospitality/">Prestige Homes</a></li>
        <li><a href="/industries/professional-services/">Family Homes</a></li><li><a href="/industries/ecommerce/">Builders &amp; Developers</a></li>
      </ul>
    </li>
    <li><a href="/contact/">Contact</a></li>
  </ul></div>
  <div class="nav-right"><div class="nav-cta"><a href="tel:+61417431124" class="btn btn-primary btn-sm">
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
    <span>0417&nbsp;431&nbsp;124</span></a></div>
    <button class="mobile-menu-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</div></nav></header>"""

FC = """\
<footer style="background:#111112;color:rgba(245,242,237,.65);padding:4rem 0 2rem;">
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:3rem;margin-bottom:3rem;border-bottom:1px solid rgba(245,242,237,.08);padding-bottom:3rem;">
      <div><span style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.5rem;letter-spacing:.18em;text-transform:uppercase;color:var(--color-text-inverse);display:block;margin-bottom:.4rem;">Inbuilt Atelier</span>
        <span style="font-family:'Jost',sans-serif;font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:var(--color-copper);font-weight:500;">Bespoke Joinery &amp; Wardrobes</span>
        <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;line-height:1.8;color:rgba(245,242,237,.45);margin-top:1.25rem;">Studio 7, 369&ndash;371 New South Head Road<br>Double Bay NSW 2029</p>
      </div>
      <div><h4 style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,242,237,.35);margin-bottom:1.25rem;">Services</h4>
        <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.6rem;">
          <li><a href="/service/ai-assistants/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Built-In Wardrobes</a></li>
          <li><a href="/service/website-development/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Walk-In Wardrobes</a></li>
          <li><a href="/service/seo-local-seo/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Joinery &amp; Cabinetry</a></li>
          <li><a href="/service/social-growth/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Vanities</a></li>
          <li><a href="/service/crm-sales-funnel/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">Home Office</a></li>
          <li><a href="/service/growth-strategy-analytics/" style="color:rgba(245,242,237,.55);text-decoration:none;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;">TV Units &amp; Media</a></li>
        </ul>
      </div>
      <div><h4 style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,242,237,.35);margin-bottom:1.25rem;">Contact</h4>
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
      <input type="text" id="chatInput" placeholder="Ask about our work..." autocomplete="off" required>
      <button type="submit" aria-label="Send message">Send</button>
    </form>
  </div>
</div>
<div id="chatNudge" class="chat-nudge-container"><div class="chat-nudge-text">Questions? Ask me!</div><svg class="chat-nudge-arrow" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"><path d="M20,20 Q60,20 70,70 L60,60 M70,70 L80,60" /></svg></div>
<link rel="stylesheet" href="/css/chat-nudge.css">
<script src="/js/formHandler.js"></script><script src="/js/aiChat.js"></script><script src="/js/main.js"></script><script src="/js/contactModal.js"></script>
<script>document.addEventListener("DOMContentLoaded",()=>{const a=new AIChat();a.init();});</script>"""

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Vanities Sydney | Bespoke Bathroom Vanities | Inbuilt Atelier</title>
    <meta name="description" content="Custom-designed bathroom vanities for Sydney homes. Stone benchtops, custom joinery, integrated basins, and premium tapware. Designed at our Double Bay studio.">
    <link rel="canonical" href="https://inbuiltatelier.com.au/service/social-growth/">
    <meta property="og:title" content="Custom Vanities Sydney | Inbuilt Atelier">
    <meta property="og:type" content="website">
{COMMON}
</head>
<body>
{NAV_HTML}
<section style="position:relative;min-height:52vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 60% 40%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;">
    <nav aria-label="breadcrumb" style="margin-bottom:2rem;"><ol class="breadcrumb">
      <li><a href="/" style="color:rgba(245,242,237,.45);">Home</a></li><li style="color:rgba(245,242,237,.45);">&middot;</li>
      <li><a href="/service/" style="color:rgba(245,242,237,.45);">Services</a></li><li style="color:rgba(245,242,237,.45);">&middot;</li>
      <li style="color:var(--color-copper);">Vanities</li>
    </ol></nav>
    <div style="max-width:720px;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;"><span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Bathroom Joinery</div>
      <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">Custom<br><em style="font-style:italic;color:var(--color-copper);">Vanities</em></h1>
      <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);max-width:600px;">A vanity is one of the most-used pieces of furniture in any home. We design and build custom vanities that are as functional as they are beautiful &mdash; fitted precisely to your space and style.</p>
    </div>
  </div>
</section>

<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center;">
      <div>
        <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.25rem;"><span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Designed for Real Life</div>
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.25rem,4vw,3.25rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">Vanities Built to Your Bathroom, Your Vision</h2>
        <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.25rem;">Whether you are renovating an ensuite or completely rebuilding a main bathroom, a custom vanity from Inbuilt Atelier replaces generic flat-pack cabinetry with something designed specifically for your space.</p>
        <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:2rem;">We work with your architect, builder, or interior designer &mdash; or directly with you &mdash; to produce detailed drawings and a fixed-price proposal before any manufacturing begins.</p>
        <a href="/contact/" class="btn btn-primary">Book a Consultation</a>
      </div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--border-light);">
        <div class="feature-card"><div style="width:36px;height:1px;background:var(--color-accent);margin-bottom:1.25rem;"></div><h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.2rem;color:var(--color-primary);margin-bottom:.6rem;">Stone Benchtops</h3><p style="font-family:'Jost',sans-serif;font-size:.85rem;font-weight:300;color:var(--color-text-secondary);line-height:1.75;">Honed marble, travertine, Calacatta or engineered stone &mdash; with waterfall ends, integrated basins, or separate undermounts.</p></div>
        <div class="feature-card"><div style="width:36px;height:1px;background:var(--color-accent);margin-bottom:1.25rem;"></div><h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.2rem;color:var(--color-primary);margin-bottom:.6rem;">Custom Carcass</h3><p style="font-family:'Jost',sans-serif;font-size:.85rem;font-weight:300;color:var(--color-text-secondary);line-height:1.75;">Floating or floor-standing, any width and depth. Drawers, doors, or open shelf configurations to suit your storage needs.</p></div>
        <div class="feature-card"><div style="width:36px;height:1px;background:var(--color-accent);margin-bottom:1.25rem;"></div><h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.2rem;color:var(--color-primary);margin-bottom:.6rem;">Mirror &amp; Shaving Cabinets</h3><p style="font-family:'Jost',sans-serif;font-size:.85rem;font-weight:300;color:var(--color-text-secondary);line-height:1.75;">Bespoke mirror frames, backlit panels, and built-in shaving cabinets designed to align perfectly with your vanity.</p></div>
        <div class="feature-card"><div style="width:36px;height:1px;background:var(--color-accent);margin-bottom:1.25rem;"></div><h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.2rem;color:var(--color-primary);margin-bottom:.6rem;">Premium Hardware</h3><p style="font-family:'Jost',sans-serif;font-size:.85rem;font-weight:300;color:var(--color-text-secondary);line-height:1.75;">Brushed brass, matte black, or chrome tapware and pulls. We source from leading European hardware suppliers.</p></div>
      </div>
    </div>
  </div>
</section>

<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:680px;margin:0 auto;">
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.25rem,4vw,3.25rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.5rem;">Design Your Custom Vanity</h2>
    <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.55);margin-bottom:2.5rem;">Bring your bathroom dimensions and we will show you what is possible &mdash; with sample materials and a full 3D render before you commit.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-primary">Book a Consultation</a>
      <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:rgba(245,242,237,.65);text-decoration:none;padding:.85rem 1.5rem;border:1px solid rgba(245,242,237,.2);">Call 0417 431 124</a>
    </div>
  </div>
</section>
{FC}
</body>
</html>
"""

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target = os.path.join(base, 'public', 'service', 'social-growth', 'index.html')
with open(target, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f"Written: {os.path.getsize(target)} bytes → {target}")
