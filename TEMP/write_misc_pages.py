#!/usr/bin/env python3
"""Write Blog, Case Studies, Offers, and Privacy pages for Inbuilt Atelier."""
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ─── Shared NAV & FOOTER ────────────────────────────────────────────────────
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
    <li class="nav-item-dropdown"><a href="/industries/">Spaces &#9662;</a>
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

HEAD_TPL = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://inbuiltatelier.com.au{canonical}">
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
    </style>
</head>
<body>"""

# ─── Blog ────────────────────────────────────────────────────────────────────
blog = HEAD_TPL.format(
    title="Journal | Joinery Ideas &amp; Design Inspiration | Inbuilt Atelier",
    desc="Joinery ideas, wardrobe design inspiration, and material guides from the Inbuilt Atelier studio in Double Bay, Sydney.",
    canonical="/blog/"
) + f"""
{NAV}
<section style="position:relative;min-height:45vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 45%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;max-width:720px;">
    <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
      <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Our Journal
    </div>
    <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
      Ideas &amp;<br><em style="font-style:italic;color:var(--color-copper);">Inspiration</em>
    </h1>
    <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);">Design ideas, material guides, and stories from our projects &mdash; published when we have something worth saying.</p>
  </div>
</section>
<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container" style="max-width:900px;margin:0 auto;">
    <div style="text-align:center;padding:5rem 2rem;border:1px solid var(--border-light);background:#fff;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Coming Soon<span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:2.25rem;color:var(--color-primary);margin-bottom:1rem;">We Are Working on It</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);max-width:500px;margin:0 auto 2rem;">Our Journal will feature material guides, project stories, and design ideas from the studio. In the meantime, get in touch if you have a project in mind.</p>
      <a href="/contact/" class="btn btn-primary">Start a Conversation</a>
    </div>
  </div>
</section>
<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:600px;margin:0 auto;">
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,4vw,3rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.5rem;">Have a Project in Mind?</h2>
    <a href="/contact/" class="btn btn-primary" style="margin-right:1rem;">Book a Consultation</a>
    <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:rgba(245,242,237,.65);text-decoration:none;padding:.85rem 1.5rem;border:1px solid rgba(245,242,237,.2);">Call 0417 431 124</a>
  </div>
</section>
{FOOTER_CHAT}"""

# ─── Case Studies ─────────────────────────────────────────────────────────────
case_studies = HEAD_TPL.format(
    title="Projects | Bespoke Joinery Portfolio | Inbuilt Atelier",
    desc="Selected projects from the Inbuilt Atelier studio — built-in wardrobes, walk-in robes, joinery, and cabinetry for homes across Sydney.",
    canonical="/case-studies/"
) + f"""
{NAV}
<section style="position:relative;min-height:45vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 45%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;max-width:720px;">
    <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
      <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Selected Work
    </div>
    <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
      Our<br><em style="font-style:italic;color:var(--color-copper);">Projects</em>
    </h1>
    <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);">A selection of wardrobes, joinery, and custom cabinetry installed for homes across Sydney.</p>
  </div>
</section>
<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container" style="max-width:900px;margin:0 auto;">
    <div style="text-align:center;padding:5rem 2rem;border:1px solid var(--border-light);background:#fff;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Portfolio Coming Soon<span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:2.25rem;color:var(--color-primary);margin-bottom:1rem;">Photography in Progress</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);max-width:560px;margin:0 auto 2rem;">We are currently commissioning professional photography of our recent installations. Project case studies will be published here shortly. Call us to discuss any specific projects or styles you are interested in.</p>
      <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
        <a href="/contact/" class="btn btn-primary">Discuss Your Project</a>
        <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:var(--color-accent);text-decoration:none;padding:.85rem 1.5rem;border:1px solid var(--color-accent);">Call 0417 431 124</a>
      </div>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.5rem;margin-top:3rem;">
      <div style="padding:2rem;background:#fff;border:1px solid var(--border-light);border-top:2px solid var(--color-accent);">
        <p style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--color-accent);margin-bottom:.75rem;">Project Type</p>
        <h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;color:var(--color-primary);margin-bottom:.5rem;">Walk-In Robe, Mosman</h3>
        <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">American oak veneer island dressing bench, integrated LED lighting, and full-height mirror wall with concealed pivot door. Photography pending.</p>
      </div>
      <div style="padding:2rem;background:#fff;border:1px solid var(--border-light);border-top:2px solid var(--color-accent);">
        <p style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--color-accent);margin-bottom:.75rem;">Project Type</p>
        <h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;color:var(--color-primary);margin-bottom:.5rem;">Full Home Joinery, Vaucluse</h3>
        <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">Seven-room joinery commission including master walk-in robe, four built-in wardrobes, library wall, and dual vanities. Photography pending.</p>
      </div>
      <div style="padding:2rem;background:#fff;border:1px solid var(--border-light);border-top:2px solid var(--color-accent);">
        <p style="font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.15em;text-transform:uppercase;color:var(--color-accent);margin-bottom:.75rem;">Project Type</p>
        <h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;color:var(--color-primary);margin-bottom:.5rem;">New Build Package, Double Bay</h3>
        <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">Coordinated with builder and interior designer on a new build: wardrobes, kitchen overhead cabinetry, laundry, and home office. Photography pending.</p>
      </div>
    </div>
  </div>
</section>
<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:600px;margin:0 auto;">
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,4vw,3rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.5rem;">Ready to Start?</h2>
    <a href="/contact/" class="btn btn-primary">Book a Consultation</a>
  </div>
</section>
{FOOTER_CHAT}"""

# ─── Offers ───────────────────────────────────────────────────────────────────
offers = HEAD_TPL.format(
    title="Free Design Consultation | Bespoke Wardrobes &amp; Joinery | Inbuilt Atelier",
    desc="Book a free, no-obligation design consultation with Inbuilt Atelier. We come to your home, measure your space, and present a joinery concept — no pressure. Double Bay, Sydney.",
    canonical="/offers/"
) + f"""
{NAV}
<section style="position:relative;min-height:55vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 45%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center;">
      <div>
        <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
          <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Complimentary
        </div>
        <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.75rem,5vw,4.5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
          Free Design<br><em style="font-style:italic;color:var(--color-copper);">Consultation</em>
        </h1>
        <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);max-width:520px;margin-bottom:2.5rem;">We come to your home, take proper measurements, understand how you live, and present a joinery concept &mdash; all before you spend a dollar.</p>
        <a href="/contact/" class="btn btn-primary" style="font-size:1rem;padding:1rem 2rem;">Book Your Free Consultation</a>
      </div>
      <div style="display:grid;grid-template-columns:1fr;gap:1.25rem;">
        <div style="display:flex;align-items:start;gap:1.25rem;padding:1.5rem;border:1px solid rgba(245,242,237,.12);">
          <div style="width:2rem;height:2rem;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-family:'Cormorant Garamond',serif;font-size:1rem;color:#fff;">1</div>
          <div>
            <h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-size:1.15rem;font-weight:400;color:var(--color-text-inverse);margin-bottom:.35rem;">We Come to You</h3>
            <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:rgba(245,242,237,.5);line-height:1.7;">We visit your home at a time that suits you, see the actual space, and take thorough measurements.</p>
          </div>
        </div>
        <div style="display:flex;align-items:start;gap:1.25rem;padding:1.5rem;border:1px solid rgba(245,242,237,.12);">
          <div style="width:2rem;height:2rem;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-family:'Cormorant Garamond',serif;font-size:1rem;color:#fff;">2</div>
          <div>
            <h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-size:1.15rem;font-weight:400;color:var(--color-text-inverse);margin-bottom:.35rem;">We Design for Your Space</h3>
            <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:rgba(245,242,237,.5);line-height:1.7;">We prepare a tailored joinery concept showing layout, materials, and interior configuration options.</p>
          </div>
        </div>
        <div style="display:flex;align-items:start;gap:1.25rem;padding:1.5rem;border:1px solid rgba(245,242,237,.12);">
          <div style="width:2rem;height:2rem;border-radius:50%;background:var(--color-accent);display:flex;align-items:center;justify-content:center;flex-shrink:0;font-family:'Cormorant Garamond',serif;font-size:1rem;color:#fff;">3</div>
          <div>
            <h3 style="font-family:'Cormorant Garamond',Georgia,serif;font-size:1.15rem;font-weight:400;color:var(--color-text-inverse);margin-bottom:.35rem;">No Pressure, No Obligation</h3>
            <p style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:rgba(245,242,237,.5);line-height:1.7;">You receive a fixed-price quote and decide in your own time. Nothing is rushed and nothing is assumed.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container" style="max-width:800px;margin:0 auto;">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">
      <div>
        <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.5rem;">
          <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>What to Expect
        </div>
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3vw,2.5rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">A Genuine Design Conversation</h2>
        <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:1.25rem;">The initial consultation typically takes 45&ndash;60 minutes. We ask about how you use the space, what is not working currently, what materials appeal to you, and what your budget range is.</p>
        <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);">We then return within a week with a design concept and a fixed-price quote. No hourly rates for the initial consultation, no commitment required.</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:1.25rem;">
        <div style="padding:1.5rem;border-left:2px solid var(--color-accent);">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:1.2rem;font-weight:400;color:var(--color-primary);margin-bottom:.4rem;">&ldquo;Marina took the time to understand how my daughters and I actually use the robes before she suggested anything. The result feels completely personal.&rdquo;</p>
          <p style="font-family:'Jost',sans-serif;font-size:.78rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--color-text-secondary);">Client, Woollahra</p>
        </div>
        <div style="padding:1.5rem;border-left:2px solid var(--color-accent);">
          <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:1.2rem;font-weight:400;color:var(--color-primary);margin-bottom:.4rem;">&ldquo;No pushy sales approach. Just a really clear brief, good ideas, and a fair price.&rdquo;</p>
          <p style="font-family:'Jost',sans-serif;font-size:.78rem;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--color-text-secondary);">Client, Cremorne</p>
        </div>
      </div>
    </div>
  </div>
</section>
<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:640px;margin:0 auto;">
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,4vw,3rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.25rem;">Book Your Free Consultation</h2>
    <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.55);margin-bottom:2.5rem;">Available across Sydney. Monday to Friday, 9am&ndash;5pm. Saturday by arrangement.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-primary">Request Consultation</a>
      <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:rgba(245,242,237,.65);text-decoration:none;padding:.85rem 1.5rem;border:1px solid rgba(245,242,237,.2);">Call 0417 431 124</a>
    </div>
  </div>
</section>
{FOOTER_CHAT}"""

# ─── Privacy Policy ───────────────────────────────────────────────────────────
privacy = HEAD_TPL.format(
    title="Privacy Policy | Inbuilt Atelier",
    desc="Privacy policy for Inbuilt Atelier — how we collect, use, and store your personal information.",
    canonical="/privacy-policy-2/"
) + f"""
{NAV}
<section style="position:relative;min-height:30vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 4rem;overflow:hidden;">
  <div class="container" style="position:relative;z-index:2;max-width:720px;">
    <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.5rem,5vw,4rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1rem;letter-spacing:.02em;">
      Privacy<br><em style="font-style:italic;color:var(--color-copper);">Policy</em>
    </h1>
    <p style="font-family:'Jost',sans-serif;font-size:.9rem;font-weight:300;color:rgba(245,242,237,.45);">Last updated: January 2026</p>
  </div>
</section>
<section style="padding:5rem 0;background:var(--color-bg-body);">
  <div class="container" style="max-width:760px;margin:0 auto;">
    <div style="background:#fff;padding:4rem;border:1px solid var(--border-light);">
      <div style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.9;color:var(--color-text-secondary);">
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:0 0 1.25rem;">1. About This Policy</h2>
        <p style="margin-bottom:1.5rem;">Inbuilt Atelier (&ldquo;we&rdquo;, &ldquo;our&rdquo;, &ldquo;us&rdquo;) is committed to protecting your personal information in accordance with the Australian Privacy Act 1988 (Cth) and the Australian Privacy Principles. This policy explains how we collect, use, disclose, and protect your personal information.</p>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">2. Information We Collect</h2>
        <p style="margin-bottom:1rem;">We may collect the following information when you contact us, use our website, or engage our services:</p>
        <ul style="list-style:none;padding:0;margin-bottom:1.5rem;">
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Full name and contact details (phone, email, address)</li>
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Information about your property or project</li>
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Correspondence and enquiry records</li>
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Website usage data (via cookies and analytics)</li>
          <li style="padding:.5rem 0;">Chat conversation transcripts (if you request email delivery)</li>
        </ul>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">3. How We Use Your Information</h2>
        <p style="margin-bottom:1rem;">We use your personal information to:</p>
        <ul style="list-style:none;padding:0;margin-bottom:1.5rem;">
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Respond to your enquiries and provide quotations</li>
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Schedule and conduct design consultations</li>
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Manage your project from design through to installation</li>
          <li style="padding:.5rem 0;border-bottom:1px solid var(--border-light);">Send relevant information about our services (with your consent)</li>
          <li style="padding:.5rem 0;">Comply with legal and regulatory obligations</li>
        </ul>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">4. Disclosure of Information</h2>
        <p style="margin-bottom:1.5rem;">We do not sell, trade, or rent your personal information to third parties. We may share information with trusted service providers who assist in operating our website or conducting our business, subject to confidentiality agreements. We may disclose information where required by law.</p>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">5. Data Security</h2>
        <p style="margin-bottom:1.5rem;">We take reasonable steps to protect your personal information from misuse, loss, and unauthorised access. Our website uses SSL encryption. Our project management and database systems are password-protected and access-controlled.</p>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">6. Cookies</h2>
        <p style="margin-bottom:1.5rem;">Our website uses cookies to improve your experience and analyse usage patterns. You may disable cookies in your browser settings, though this may affect site functionality.</p>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">7. Access and Correction</h2>
        <p style="margin-bottom:1.5rem;">You have the right to access and correct personal information we hold about you. To make a request, please contact us at <a href="mailto:marina@inbuiltatelier.com.au" style="color:var(--color-accent);">marina@inbuiltatelier.com.au</a>.</p>
        
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.75rem;color:var(--color-primary);margin:2rem 0 1.25rem;">8. Contact</h2>
        <p>For any privacy-related enquiries, please contact:<br><br>
        <strong style="color:var(--color-primary);">Inbuilt Atelier</strong><br>
        Studio 7, 369&ndash;371 New South Head Road, Double Bay NSW 2029<br>
        <a href="mailto:marina@inbuiltatelier.com.au" style="color:var(--color-accent);">marina@inbuiltatelier.com.au</a><br>
        <a href="tel:+61417431124" style="color:var(--color-accent);">0417 431 124</a></p>
      </div>
    </div>
  </div>
</section>
{FOOTER_CHAT}"""

pages = [
    ('blog/index.html', blog),
    ('case-studies/index.html', case_studies),
    ('offers/index.html', offers),
    ('privacy-policy-2/index.html', privacy),
]

for rel_path, content in pages:
    target = os.path.join(BASE, 'public', rel_path)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Written: {os.path.getsize(target):,} bytes → public/{rel_path}")
