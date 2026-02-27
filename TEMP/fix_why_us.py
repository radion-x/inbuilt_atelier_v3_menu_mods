import sys

filepath = "public/index.html"

with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "    <!-- Why Choose Us Section -->"
end_marker = "            <!-- Testimonials -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

print(f"start={start_idx} end={end_idx} len={len(content)}")

if start_idx == -1 or end_idx == -1:
    print("ERROR: markers not found")
    sys.exit(1)

new_section = """    <!-- Why Choose Us Section -->
    <section id="why-us" class="section" style="background: var(--color-primary); padding: 7rem 0; color: white;">
        <div class="container">

            <!-- Section header -->
            <div style="text-align: center; margin-bottom: 5rem;">
                <span style="display: inline-block; padding: 0.45rem 1.1rem; background: rgba(200,85,61,0.15); border-radius: 50px; font-size: 0.8rem; font-weight: 700; letter-spacing: 0.1em; margin-bottom: 1.5rem; border: 1px solid rgba(200,85,61,0.35); color: #d4714f; text-transform: uppercase;">Why Choose Us</span>
                <h2 style="color: white; margin-bottom: 1.25rem;">We're Not Like<br>The Others</h2>
                <p style="color: rgba(255,255,255,0.65); max-width: 520px; margin: 0 auto; font-size: 1.05rem; line-height: 1.75;">Brisbane homeowners have been let down enough. Here&rsquo;s why hundreds choose River City Handyman &mdash; and keep coming back.</p>
            </div>

            <!-- 3x2 feature grid -->
            <div class="why-us-grid">

                <div class="why-card">
                    <div class="why-card-accent"></div>
                    <div class="why-card-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c8553d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <circle cx="12" cy="12" r="10"></circle>
                            <polyline points="12 6 12 12 16 14"></polyline>
                        </svg>
                    </div>
                    <h3 class="why-card-title">We Show Up On Time</h3>
                    <p class="why-card-body">If we say 8am, we mean 8am. No vague windows, no half-day guessing games. We respect that your day matters &mdash; and if something truly urgent comes up, we call you before you&rsquo;ve even noticed.</p>
                </div>

                <div class="why-card">
                    <div class="why-card-accent"></div>
                    <div class="why-card-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c8553d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
                        </svg>
                    </div>
                    <h3 class="why-card-title">Straight Answers, Clear Quotes</h3>
                    <p class="why-card-body">No jargon, no vague estimates. We tell you exactly what we&rsquo;ll do and what it costs before a single tool leaves the bag. What we quote is what you pay &mdash; no surprises on the invoice.</p>
                </div>

                <div class="why-card">
                    <div class="why-card-accent"></div>
                    <div class="why-card-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c8553d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
                            <polyline points="9 22 9 12 15 12 15 22"></polyline>
                        </svg>
                    </div>
                    <h3 class="why-card-title">We Respect Your Home</h3>
                    <p class="why-card-body">Drop sheets, boot covers, and a spotless exit. We treat your home with the same care we&rsquo;d give our own &mdash; because we know you&rsquo;ll notice. Every job ends cleaner than we found it.</p>
                </div>

                <div class="why-card">
                    <div class="why-card-accent"></div>
                    <div class="why-card-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c8553d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                        </svg>
                    </div>
                    <h3 class="why-card-title">Fully Insured &amp; Compliant</h3>
                    <p class="why-card-body">We carry full Public Liability insurance so you&rsquo;re protected on every job. No cowboy contractors, no shortcuts. Just licensed, professional tradespeople you can trust in your home.</p>
                </div>

                <div class="why-card">
                    <div class="why-card-accent"></div>
                    <div class="why-card-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c8553d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path>
                            <circle cx="12" cy="7" r="4"></circle>
                        </svg>
                    </div>
                    <h3 class="why-card-title">Police Checked</h3>
                    <p class="why-card-body">Every person who enters your home has passed a thorough background check. A small detail that matters enormously &mdash; especially for homeowners, families, and property managers who value peace of mind.</p>
                </div>

                <div class="why-card">
                    <div class="why-card-accent"></div>
                    <div class="why-card-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#c8553d" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                            <rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect>
                            <line x1="8" y1="21" x2="16" y2="21"></line>
                            <line x1="12" y1="17" x2="12" y2="21"></line>
                        </svg>
                    </div>
                    <h3 class="why-card-title">One Visit, Job Done</h3>
                    <p class="why-card-body">We arrive prepared &mdash; right tools, right parts, and the experience to handle surprises. Most jobs are completed in a single visit, because your time is too valuable to spend waiting for a return trip.</p>
                </div>

            </div>
        </div>
    </section>

    <!-- Testimonials wrapper -->
    <section style="background: var(--color-primary); padding: 0 0 7rem;">
        <div class="container">

            <!-- Testimonials -->"""

new_content = content[:start_idx] + new_section + content[end_idx + len(end_marker):]

with open(filepath, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"SUCCESS. New length: {len(new_content)}, new lines: {new_content.count(chr(10))}")
