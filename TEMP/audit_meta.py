import re, os

files = [
  'public/index.html',
  'public/about/index.html',
  'public/contact/index.html',
  'public/blog/index.html',
  'public/case-studies/index.html',
  'public/offers/index.html',
  'public/privacy-policy-2/index.html',
  'public/service/index.html',
  'public/service/ai-assistants/index.html',
  'public/service/website-development/index.html',
  'public/service/seo-local-seo/index.html',
  'public/service/social-growth/index.html',
  'public/service/crm-sales-funnel/index.html',
  'public/service/growth-strategy-analytics/index.html',
  'public/industries/index.html',
  'public/industries/healthcare/index.html',
  'public/industries/real-estate/index.html',
  'public/industries/home-services/index.html',
  'public/industries/hospitality/index.html',
  'public/industries/professional-services/index.html',
  'public/industries/ecommerce/index.html',
]

def extract(html, pattern):
    m = re.search(pattern, html, re.IGNORECASE | re.DOTALL)
    return m.group(1).strip() if m else '(none)'

for f in files:
    if not os.path.exists(f):
        print(f'===== {f} =====')
        print('FILE NOT FOUND')
        print()
        continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
        html = fh.read()
    
    title = extract(html, r'<title>(.*?)</title>')
    
    meta_desc = extract(html, r'<meta\s+name="description"\s+content="([^"]*)"')
    if meta_desc == '(none)':
        meta_desc = extract(html, r'content="([^"]*)"[^>]*name="description"')
    
    canonical = extract(html, r'<link\s+rel="canonical"\s+href="([^"]*)"')
    if canonical == '(none)':
        canonical = extract(html, r'href="([^"]*)"[^>]*rel="canonical"')
    
    og_title = extract(html, r'<meta\s+property="og:title"\s+content="([^"]*)"')
    if og_title == '(none)':
        og_title = extract(html, r'content="([^"]*)"[^>]*property="og:title"')
    
    og_desc = extract(html, r'<meta\s+property="og:description"\s+content="([^"]*)"')
    if og_desc == '(none)':
        og_desc = extract(html, r'content="([^"]*)"[^>]*property="og:description"')
    
    og_url = extract(html, r'<meta\s+property="og:url"\s+content="([^"]*)"')
    if og_url == '(none)':
        og_url = extract(html, r'content="([^"]*)"[^>]*property="og:url"')
    
    # Get h1/h2 headings
    headings = re.findall(r'<h[12][^>]*>(.*?)</h[12]>', html, re.IGNORECASE | re.DOTALL)
    headings_clean = [re.sub(r'<[^>]+>', '', h).strip()[:120] for h in headings[:6]]
    
    print(f'===== {f} =====')
    print(f'  TITLE: {title}')
    print(f'  META DESC: {meta_desc}')
    print(f'  CANONICAL: {canonical}')
    print(f'  OG:TITLE: {og_title}')
    print(f'  OG:DESC: {og_desc}')
    print(f'  OG:URL: {og_url}')
    print(f'  HEADINGS: {headings_clean}')
    print()
