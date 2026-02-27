#!/usr/bin/env python3
"""Write Services Overview page for Inbuilt Atelier."""
import os

HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Services | Bespoke Wardrobes &amp; Joinery Sydney | Inbuilt Atelier</title>
    <meta name="description" content="Explore the full range of bespoke joinery services from Inbuilt Atelier — built-in wardrobes, walk-in wardrobes, cabinetry, vanities, home office, and TV units. Double Bay, Sydney.">
    <meta name="keywords" content="bespoke joinery sydney, custom wardrobes services, wardrobe and cabinetry double bay, inbuilt atelier services">
    <link rel="canonical" href="https://inbuiltatelier.com.au/service/">
    <meta property="og:title" content="Our Services | Inbuilt Atelier">
    <meta property="og:description" content="Bespoke wardrobes and joinery services for Sydney homes.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://inbuiltatelier.com.au/service/">
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
        .service-card{display:flex;flex-direction:column;border:1px solid var(--border-light);background:#fff;overflow:hidden;transition:border-color .3s,transform .3s;text-decoration:none;color:inherit}
        .service-card:hover{border-color:var(--color-accent);transform:translateY(-4px)}
        .service-card-num{font-family:'Cormorant Garamond',Georgia,serif;font-size:3rem;font-weight:300;color:var(--color-copper);opacity:.5;line-height:1}
        .service-card-body{padding:2rem;flex:1;display:flex;flex-direction:column}
        .service-card-body h3{font-family:'Cormorant Garamond',Georgia,serif;font-weight:400;font-size:1.5rem;color:var(--color-primary);margin-bottom:.75rem;line-height:1.15}
        .service-card-body p{font-family:'Jost',sans-serif;font-size:.9rem;font-weight:300;color:var(--color-text-secondary);line-height:1.8;flex:1}
        .service-card-link{display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.78rem;font-weight:500;letter-spacing:.1em;text-transform:uppercase;color:var(--color-accent);margin-top:1.5rem;text-decoration:none}
        .service-card-header{background:var(--color-primary);padding:1.5rem 2rem;display:flex;justify-content:space-between;align-items:flex-start}
    </style>
</head>
<body>
<header><nav><div class="container nav-container">
  <div class="nav-left"><a href="/" class="nav-wordmark">Inbuilt Atelier<span>Double Bay &middot; Sydney</span></a></div>
  <div class="nav-center"><ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/about/">About</a></li>
    <li class="nav-item-dropdown"><a href="/service/" class="active">Services &#9662;</a>
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
</div></nav></header>

<!-- Hero -->
<section style="position:relative;min-height:50vh;background:var(--color-primary);display:flex;align-items:center;padding:8rem 0 5rem;overflow:hidden;">
  <div style="position:absolute;inset:0;background:radial-gradient(ellipse at 65% 45%,rgba(155,128,96,.12) 0%,transparent 65%);pointer-events:none;"></div>
  <div class="container" style="position:relative;z-index:2;">
    <nav aria-label="breadcrumb" style="margin-bottom:2rem;">
      <ol class="breadcrumb">
        <li><a href="/" style="color:rgba(245,242,237,.45);">Home</a></li>
        <li style="color:rgba(245,242,237,.45);">&middot;</li>
        <li style="color:var(--color-copper);">Services</li>
      </ol>
    </nav>
    <div style="max-width:720px;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>What We Do
      </div>
      <h1 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(3rem,6vw,5rem);line-height:1.05;color:var(--color-text-inverse);margin-bottom:1.5rem;letter-spacing:.02em;">
        Every Service,<br><em style="font-style:italic;color:var(--color-copper);">One Studio</em>
      </h1>
      <p style="font-family:'Jost',sans-serif;font-size:1.05rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.65);max-width:620px;">
        From a single built-in wardrobe to a complete home joinery programme, Inbuilt Atelier handles every service in-house &mdash; design, manufacturing, and installation under one roof.
      </p>
    </div>
  </div>
</section>

<!-- Services Grid -->
<section style="padding:7rem 0;background:var(--color-bg-body);">
  <div class="container">
    <div style="text-align:center;max-width:600px;margin:0 auto 4.5rem;">
      <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-accent);margin-bottom:1rem;">
        <span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>Our Services<span style="display:block;width:28px;height:1px;background:var(--color-accent);"></span>
      </div>
      <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2rem,3.5vw,2.75rem);line-height:1.1;color:var(--color-primary);">Six Areas of Expertise</h2>
      <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:var(--color-text-secondary);margin-top:1rem;">Each service is approached with the same obsessive attention to material, proportion, and precision.</p>
    </div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1.5rem;">

      <!-- 01 Built-In Wardrobes -->
      <a href="/service/ai-assistants/" class="service-card">
        <div class="service-card-header">
          <span class="service-card-num">01</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="service-card-body">
          <h3>Built-In Wardrobes</h3>
          <p>Precision-fitted wardrobes designed for your exact space &mdash; sliding or hinged doors, full interior configuration, integrated lighting, and floor-to-ceiling installation.</p>
          <span class="service-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <!-- 02 Walk-In Wardrobes -->
      <a href="/service/website-development/" class="service-card">
        <div class="service-card-header">
          <span class="service-card-num">02</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="service-card-body">
          <h3>Walk-In Wardrobes</h3>
          <p>Full dressing room designs with island benches, custom shoe storage, display shelving, full-length mirrors, and integrated lighting &mdash; the room your wardrobe deserves.</p>
          <span class="service-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <!-- 03 Joinery & Cabinetry -->
      <a href="/service/seo-local-seo/" class="service-card">
        <div class="service-card-header">
          <span class="service-card-num">03</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="service-card-body">
          <h3>Joinery &amp; Cabinetry</h3>
          <p>Library walls, hallway storage, pantries, laundry cabinetry, and bespoke display work &mdash; fitted joinery that integrates seamlessly into the architecture of your home.</p>
          <span class="service-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <!-- 04 Vanities -->
      <a href="/service/social-growth/" class="service-card">
        <div class="service-card-header">
          <span class="service-card-num">04</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="service-card-body">
          <h3>Vanities</h3>
          <p>Custom bathroom vanities with stone benchtops, integrated basins, mirrored cabinetry, and premium tapware &mdash; built to the centimetre for your renovation.</p>
          <span class="service-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <!-- 05 Home Office -->
      <a href="/service/crm-sales-funnel/" class="service-card">
        <div class="service-card-header">
          <span class="service-card-num">05</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="service-card-body">
          <h3>Home Office</h3>
          <p>Built-in desks, study walls, filing storage, and dual workstation configurations &mdash; designed around how you actually work, not how a catalogue thinks you do.</p>
          <span class="service-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

      <!-- 06 TV Units & Media -->
      <a href="/service/growth-strategy-analytics/" class="service-card">
        <div class="service-card-header">
          <span class="service-card-num">06</span>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="rgba(245,242,237,.4)" stroke-width="1.5"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
        <div class="service-card-body">
          <h3>TV Units &amp; Media</h3>
          <p>Full media walls, floating TV credenzas, and entertainment joinery with hidden cable management, ventilated AV bays, and integrated fireplace surrounds.</p>
          <span class="service-card-link">Explore <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></span>
        </div>
      </a>

    </div>
  </div>
</section>

<!-- Why us strip -->
<section style="padding:5rem 0;background:#fff;border-top:1px solid var(--border-light);border-bottom:1px solid var(--border-light);">
  <div class="container">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:3rem;text-align:center;">
      <div>
        <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.5rem;font-weight:300;color:var(--color-accent);margin-bottom:.5rem;line-height:1;">12+</p>
        <p style="font-family:'Jost',sans-serif;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--color-text-secondary);">Years of Craft</p>
      </div>
      <div>
        <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.5rem;font-weight:300;color:var(--color-accent);margin-bottom:.5rem;line-height:1;">500+</p>
        <p style="font-family:'Jost',sans-serif;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--color-text-secondary);">Projects Completed</p>
      </div>
      <div>
        <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.5rem;font-weight:300;color:var(--color-accent);margin-bottom:.5rem;line-height:1;">100%</p>
        <p style="font-family:'Jost',sans-serif;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--color-text-secondary);">Custom Designed</p>
      </div>
      <div>
        <p style="font-family:'Cormorant Garamond',Georgia,serif;font-size:2.5rem;font-weight:300;color:var(--color-accent);margin-bottom:.5rem;line-height:1;">10yr</p>
        <p style="font-family:'Jost',sans-serif;font-size:.75rem;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:var(--color-text-secondary);">Workmanship Warranty</p>
      </div>
    </div>
  </div>
</section>

<!-- CTA -->
<section style="padding:6rem 0;background:var(--color-primary);text-align:center;">
  <div class="container" style="max-width:680px;margin:0 auto;">
    <div style="display:inline-flex;align-items:center;gap:.75rem;font-family:'Jost',sans-serif;font-size:.7rem;font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:var(--color-copper);margin-bottom:1.5rem;">
      <span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>Start Your Project<span style="display:block;width:28px;height:1px;background:var(--color-copper);"></span>
    </div>
    <h2 style="font-family:'Cormorant Garamond',Georgia,serif;font-weight:300;font-size:clamp(2.25rem,4vw,3.25rem);line-height:1.1;color:var(--color-text-inverse);margin-bottom:1.5rem;">
      Not Sure Where to Begin?
    </h2>
    <p style="font-family:'Jost',sans-serif;font-size:.97rem;font-weight:300;line-height:1.85;color:rgba(245,242,237,.55);margin-bottom:2.5rem;">
      Tell us about your home and what you are trying to achieve. We will help you identify what you need and how to approach it.
    </p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="/contact/" class="btn btn-primary">Book a Consultation</a>
      <a href="tel:+61417431124" style="display:inline-flex;align-items:center;gap:.5rem;font-family:'Jost',sans-serif;font-size:.88rem;font-weight:400;color:rgba(245,242,237,.65);text-decoration:none;padding:.85rem 1.5rem;border:1px solid rgba(245,242,237,.2);">Call 0417 431 124</a>
    </div>
  </div>
</section>

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
</html>
"""

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
target = os.path.join(base, 'public', 'service', 'index.html')
with open(target, 'w', encoding='utf-8') as f:
    f.write(HTML)
print(f"Written: {os.path.getsize(target)} bytes → {target}")
