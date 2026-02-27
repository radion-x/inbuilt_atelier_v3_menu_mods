#!/usr/bin/env python3
"""Write Contact page for Inbuilt Atelier."""

CONTACT_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Inbuilt Atelier | Book a Design Consultation, Double Bay Sydney</title>
    <meta name="description" content="Book a design consultation with Inbuilt Atelier — Double Bay's bespoke wardrobe and joinery studio. Visit our showroom at Studio 7, 369-371 New South Head Road, or call 0417 431 124.">
    <meta name="keywords" content="contact inbuilt atelier, book wardrobe consultation sydney, bespoke wardrobe quote, double bay joinery studio">
    <meta name="author" content="Inbuilt Atelier">
    <link rel="canonical" href="https://inbuiltatelier.com.au/contact/">
    <meta property="og:title" content="Contact Inbuilt Atelier | Book a Design Consultation">
    <meta property="og:description" content="Book a design consultation with Inbuilt Atelier. Visit our Double Bay showroom or call 0417 431 124.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://inbuiltatelier.com.au/contact/">
    <meta property="og:site_name" content="Inbuilt Atelier">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/css/styles.css?v=12">
    <link rel="stylesheet" href="/css/mobile.css?v=12">
    <link rel="stylesheet" href="/css/contactModal.css">
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "ContactPage",
        "name": "Contact Inbuilt Atelier",
        "url": "https://inbuiltatelier.com.au/contact/",
        "mainEntity": {
            "@type": "HomeAndConstructionBusiness",
            "name": "Inbuilt Atelier",
            "telephone": "+61417431124",
            "email": "marina@inbuiltatelier.com.au",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "Studio 7, 369-371 New South Head Road",
                "addressLocality": "Double Bay",
                "addressRegion": "NSW",
                "postalCode": "2029",
                "addressCountry": "AU"
            }
        }
    }
    </script>
    <style>
        .nav-wordmark{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.35rem;letter-spacing:.18em;text-transform:uppercase;color:var(--color-primary);text-decoration:none;line-height:1}
        .nav-wordmark span{display:block;font-size:.5rem;letter-spacing:.35em;color:var(--color-accent);font-weight:500;font-family:'Jost',sans-serif;margin-top:3px}
        header .nav-wordmark{color:var(--color-text-inverse)}
        header .nav-wordmark span{color:var(--color-copper)}
        .ia-eyebrow{display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1.25rem}
        .ia-eyebrow::before{content:'';display:block;width:28px;height:1px;background:var(--color-accent)}
        .ia-info-card{display:flex;gap:1.25rem;align-items:flex-start;padding:1.75rem;border:1px solid var(--border-light);background:#fff;transition:border-color .3s}
        .ia-info-card:hover{border-color:var(--color-accent)}
        .ia-info-icon{flex-shrink:0;width:40px;height:40px;border:1px solid var(--color-accent);display:flex;align-items:center;justify-content:center;color:var(--color-accent)}
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
    <li><a href="/contact/" class="active">Contact</a></li>
  </ul></div>
  <div class="nav-right">
    <div class="nav-cta"><a href="tel:+61417431124" class="btn btn-primary btn-sm">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
      <span>0417&nbsp;431&nbsp;124</span>
    </a></div>
    <button class="mobile-menu-toggle" aria-label="Toggle menu"><span></span><span></span><span></span></button>
  </div>
</div></nav></header>

<!-- Page Hero -->
<section style="position:relative;min-height:50vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 70% 40%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;">
    <nav aria-label="breadcrumb" style="margin-bottom:2rem;">
      <ol class="breadcrumb">
        <li><a href="/" style="color:rgba(245,242,237,.45);">Home</a></li>
        <li style="color:rgba(245,242,237,.45);">&middot;</li>
        <li style="color:var(--color-copper);">Contact</li>
      </ol>
    </nav>
    <div style="max-width:680px;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Get in Touch
      </div>
      <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
        Begin Your<br><em style="font-style:italic;color:var(--color-copper);">Project Today</em>
      </h1>
      <p style="font-family:'Jost',sans-serif;font-size:1rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);max-width:560px;">
        Every commission begins with a conversation. Tell us about your space, your vision, and your timeline &mdash; we will take it from there.
      </p>
    </div>
  </div>
</section>

<!-- Contact Layout -->
<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container">
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:start;">

      <!-- Contact Form -->
      <div>
        <div class="ia-eyebrow">Send an Enquiry</div>
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3.5vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:2rem;">
          Tell Us About Your Space
        </h2>

        <form id="contact-form" class="contact-form">
          <div class="form-group">
            <label for="name">Your Name</label>
            <input type="text" id="name" name="name" placeholder="e.g. Sophie Reynolds" required>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="email">Email Address</label>
              <input type="email" id="email" name="email" placeholder="you@example.com" required>
            </div>
            <div class="form-group">
              <label for="phone">Phone Number</label>
              <input type="tel" id="phone" name="phone" placeholder="04xx xxx xxx" required>
            </div>
          </div>
          <div class="form-group">
            <label for="service">What Are You Looking For?</label>
            <select id="service" name="service">
              <option value="">Select a category...</option>
              <option value="built-in-wardrobe">Built-In Wardrobe</option>
              <option value="walk-in-wardrobe">Walk-In Wardrobe</option>
              <option value="joinery-cabinetry">Joinery &amp; Cabinetry</option>
              <option value="vanity">Vanity</option>
              <option value="home-office">Home Office</option>
              <option value="tv-unit-media">TV Unit &amp; Media Joinery</option>
              <option value="multiple">Multiple Items / Full Home</option>
              <option value="other">Other / Not Sure Yet</option>
            </select>
          </div>
          <div class="form-group">
            <label for="message">Tell Us About Your Project</label>
            <textarea id="message" name="message" rows="5" placeholder="Brief description of your project &mdash; room size, existing finishes, timeline, and any specific requirements." required></textarea>
          </div>
          <button type="submit" class="quote-submit-btn">
            <span>Send Enquiry</span>
            <span class="btn-arrow" style="width:30px;height:30px;">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
            </span>
          </button>
        </form>
      </div>

      <!-- Contact Info -->
      <div>
        <div class="ia-eyebrow">Studio Details</div>
        <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3.5vw,2.75rem);line-height:1.1;color:var(--color-primary);margin-bottom:1.5rem;">
          Visit the Showroom
        </h2>
        <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-bottom:2.5rem;">
          We are based in Double Bay and welcome clients by appointment. Our showroom is where you will see materials, hardware, and finished examples in person &mdash; and where we hold the initial design conversation.
        </p>

        <div style="display:flex;flex-direction:column;gap:1rem;margin-bottom:2.5rem;">
          <div class="ia-info-card">
            <div class="ia-info-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
            </div>
            <div>
              <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--color-primary);margin-bottom:.35rem;">Showroom Address</p>
              <p style="font-family:'Jost',sans-serif;font-size:.95rem;font-weight:300;color:var(--color-text-secondary);margin:0;line-height:1.6;">Studio 7, 369&ndash;371 New South Head Road<br>Double Bay NSW 2029</p>
            </div>
          </div>
          <div class="ia-info-card">
            <div class="ia-info-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
            </div>
            <div>
              <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--color-primary);margin-bottom:.35rem;">Telephone</p>
              <a href="tel:+61417431124" style="font-family:'Jost',sans-serif;font-size:.95rem;font-weight:300;color:var(--color-text-secondary);text-decoration:none;">0417 431 124</a>
            </div>
          </div>
          <div class="ia-info-card">
            <div class="ia-info-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
            </div>
            <div>
              <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--color-primary);margin-bottom:.35rem;">Email</p>
              <a href="mailto:marina@inbuiltatelier.com.au" style="font-family:'Jost',sans-serif;font-size:.95rem;font-weight:300;color:var(--color-text-secondary);text-decoration:none;">marina@inbuiltatelier.com.au</a>
            </div>
          </div>
          <div class="ia-info-card">
            <div class="ia-info-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"></circle><path d="M12 8v4l3 3"></path></svg>
            </div>
            <div>
              <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--color-primary);margin-bottom:.35rem;">Opening Hours</p>
              <p style="font-family:'Jost',sans-serif;font-size:.95rem;font-weight:300;color:var(--color-text-secondary);margin:0;line-height:1.6;">Monday &ndash; Friday: 9:00 AM &ndash; 5:00 PM<br>Saturday: 10:00 AM &ndash; 2:00 PM<br>Sunday: Closed</p>
            </div>
          </div>
        </div>

        <!-- What to expect -->
        <div style="background:var(--color-bg-body);border:1px solid var(--border-light);padding:2rem;">
          <p style="font-family:'Jost',sans-serif;font-size:.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--color-primary);margin-bottom:1rem;">What to Expect</p>
          <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.75rem;margin:0;">
            <li style="display:flex;gap:.75rem;align-items:flex-start;">
              <span style="width:5px;height:5px;border-radius:50%;background:var(--color-accent);margin-top:.5rem;flex-shrink:0;"></span>
              <span style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">We respond to all enquiries within one business day</span>
            </li>
            <li style="display:flex;gap:.75rem;align-items:flex-start;">
              <span style="width:5px;height:5px;border-radius:50%;background:var(--color-accent);margin-top:.5rem;flex-shrink:0;"></span>
              <span style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">Initial consultation is at no charge and without obligation</span>
            </li>
            <li style="display:flex;gap:.75rem;align-items:flex-start;">
              <span style="width:5px;height:5px;border-radius:50%;background:var(--color-accent);margin-top:.5rem;flex-shrink:0;"></span>
              <span style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">We can visit your home for a site measure and assessment</span>
            </li>
            <li style="display:flex;gap:.75rem;align-items:flex-start;">
              <span style="width:5px;height:5px;border-radius:50%;background:var(--color-accent);margin-top:.5rem;flex-shrink:0;"></span>
              <span style="font-family:'Jost',sans-serif;font-size:.88rem;font-weight:300;color:var(--color-text-secondary);line-height:1.7;">You will receive a detailed, fixed-price proposal before any commitment</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Footer -->
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

<!-- AI Chat Widget -->
<div id="aiChatWidget" class="ai-chat-widget">
  <button id="chatToggle" class="chat-toggle" aria-label="Open chat"><span class="chat-icon"></span></button>
  <div id="chatWindow" class="chat-window hidden">
    <div class="chat-header">
      <h3>Chat with Inbuilt Atelier</h3>
      <div class="chat-header-actions">
        <button id="chatEmail" class="chat-email" aria-label="Save chat transcript" title="Save chat transcript">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
        </button>
        <button id="chatReset" class="chat-reset" aria-label="Reset chat">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="1 4 1 10 7 10"></polyline><polyline points="23 20 23 14 17 14"></polyline><path d="M20.49 9A9 9 0 0 0 5.64 5.64L1 10m22 4l-4.64 4.36A9 9 0 0 1 3.51 15"></path></svg>
        </button>
        <button id="chatClose" class="chat-close" aria-label="Close chat">&times;</button>
      </div>
    </div>
    <div id="chatMessages" class="chat-messages"></div>
    <form id="chatForm" class="chat-form">
      <input type="text" id="chatInput" placeholder="Ask about our wardrobes..." autocomplete="off" required>
      <button type="submit" aria-label="Send message">Send</button>
    </form>
  </div>
</div>
<div id="chatNudge" class="chat-nudge-container">
  <div class="chat-nudge-text">Questions? Ask me!</div>
  <svg class="chat-nudge-arrow" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"><path d="M20,20 Q60,20 70,70 L60,60 M70,70 L80,60" /></svg>
</div>
<link rel="stylesheet" href="/css/chat-nudge.css">
<script src="/js/formHandler.js"></script>
<script src="/js/aiChat.js"></script>
<script src="/js/main.js"></script>
<script src="/js/contactModal.js"></script>
<script>document.addEventListener("DOMContentLoaded",()=>{const a=new AIChat();a.init();});</script>
</body>
</html>
"""

target = '/Users/radions/ZONE IMAC/Working_Feb_2026/inbuilt_atelier_v1/public/contact/index.html'
with open(target, 'w', encoding='utf-8') as fh:
    fh.write(CONTACT_HTML)

import os
print(f"Written: {os.path.getsize(target)} bytes")
