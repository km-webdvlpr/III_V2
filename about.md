---
layout: page
title: About
description: Structured analytics delivery with business and product context. Built over time. Still building.
status_context: ABOUT // KABELO MAKUA
body_class: page-about
page_class: page-about
---

<section class="page-header">
  <div class="breadcrumb">HOME <span>//</span> ABOUT</div>
  <h1 class="page-title">About <span style="color:var(--green-bright);">{{ site.mark_name }}</span></h1>
  <p class="page-subtitle">Structured analytics delivery with business and product context. Built over time. Still building.</p>
</section>

<section class="about-layout">
  <aside class="sidebar">
    <div class="sidebar-label">// ON THIS PAGE</div>
    <a class="sidebar-link" href="#profile">Profile</a>
    <a class="sidebar-link" href="#career">Career log</a>
    <a class="sidebar-link" href="#process">How I work</a>
    <a class="sidebar-link" href="#credentials">Credentials</a>
    <hr class="sidebar-divider">
    <a class="sidebar-link" href="{{ '/projects/' | relative_url }}">View Projects</a>
    <a class="sidebar-link" href="mailto:{{ site.contact_email }}">Email me</a>
    <hr class="sidebar-divider">
    <div class="sidebar-meta">
      LOCATION: <span class="hi">{{ site.location_label }}</span><br>
      STATUS: <span class="hi">AVAILABLE</span><br>
      FOCUS: <span class="hi">EDTECH / FINTECH</span>
    </div>
  </aside>

  <main class="about-main">
    <section class="section" id="profile">
      <div class="section-tag reveal">// init.profile</div>
      <div class="profile-block reveal">
        <div class="profile-prompt">
          <span class="dollar">$</span>
          <span>whoami</span>
        </div>
        <div class="profile-name">Kabelo Makua</div>
        <div class="profile-title">DATA ANALYST &nbsp;//&nbsp; PRODUCT THINKING &nbsp;//&nbsp; {{ site.location_label }}</div>
        <hr class="profile-divider">
        <p class="profile-text">
          I came into analytics the long way. Bond administration at <strong>Nedbank</strong>. Web development and SME consulting. A startup, <strong>SuccessorX</strong>, where I built and pivoted a WhatsApp-based estate planning product from scratch and learned how hard it is to make a grudge product actually stick.
        </p>
        <p class="profile-text">
          Along the way I finished the <strong>ALX / ExploreAI Data Science programme</strong>, started a postgraduate path in data science, and built a portfolio that reflects how I actually think: <strong>business question first, then the data</strong>.
        </p>
        <p class="profile-text">
          I am not chasing titles for the sake of it. I am looking for teams where analysis connects to real decisions in products, operations, and commercial work, especially where the data can move something practical.
        </p>
        <div class="profile-stats">
          <div class="stat-cell">
            <span class="stat-val">8+</span>
            <span class="stat-label">Years in business</span>
          </div>
          <div class="stat-cell">
            <span class="stat-val">14</span>
            <span class="stat-label">Portfolio projects</span>
          </div>
          <div class="stat-cell">
            <span class="stat-val">{{ site.location_label }}</span>
            <span class="stat-label">Based &amp; available</span>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="career">
      <div class="section-tag reveal">// career.log --full</div>
      <div class="career-log">
        <div class="log-entry reveal">
          <div class="log-timestamp">2025 → NOW</div>
          <div class="log-role">Product &amp; Insights Analyst</div>
          <div class="log-org">TEC4TH // Independent Consulting</div>
          <div class="log-desc">Analytics consulting and portfolio development across EdTech, FinTech, civic data, customer retention, and product-style case studies. Building toward a stronger product and commercial analytics path.</div>
          <span class="log-tag">#ProductAnalytics</span>
          <span class="log-tag">#EdTech</span>
          <span class="log-tag">#FinTech</span>
        </div>
        <div class="log-entry reveal">
          <div class="log-timestamp">2022 → 2025</div>
          <div class="log-role">Co-Founder / Product Lead</div>
          <div class="log-org">SuccessorX</div>
          <div class="log-desc">Built a WhatsApp-based digital estate planning product from concept to market. Led discovery, user research, market sizing, flow design, and product pivoting.</div>
          <span class="log-tag">#ProductOwnership</span>
          <span class="log-tag">#InsurTech</span>
          <span class="log-tag">#WhatsApp</span>
          <div class="log-insight">// Estate planning is a grudge purchase. People know they need it and still avoid it. That sharpened how I think about engagement, CLTV, and what really makes a product stick.</div>
        </div>
        <div class="log-entry reveal">
          <div class="log-timestamp">2019 → 2022</div>
          <div class="log-role">SME Consultant</div>
          <div class="log-org">7Legend Agency</div>
          <div class="log-desc">Business consulting and digital delivery for SMEs. Web development, strategy support, and client-facing reporting across multiple sectors.</div>
          <span class="log-tag">#SMEConsulting</span>
          <span class="log-tag">#WebDevelopment</span>
          <span class="log-tag">#BusinessAnalysis</span>
        </div>
        <div class="log-entry reveal">
          <div class="log-timestamp">2016 → 2019</div>
          <div class="log-role">Bond Administration Clerk</div>
          <div class="log-org">Nedbank</div>
          <div class="log-desc">Financial services operations in bond administration. First exposure to structured data, process control, and how large institutions move information through systems.</div>
          <span class="log-tag">#FinancialServices</span>
          <span class="log-tag">#Operations</span>
          <span class="log-tag">#DataProcessing</span>
        </div>
        <div class="log-entry reveal" style="padding-bottom:0;">
          <div class="log-timestamp">EDUCATION</div>
          <div class="log-role">BCom — Business Management</div>
          <div class="log-org">UNISA</div>
          <div class="log-desc">Foundation in business strategy, economics, and organisational management.</div>
          <span class="log-tag">#BCom</span>
          <span class="log-tag">#UNISA</span>
        </div>
      </div>
    </section>

    <section class="section" id="process">
      <div class="section-tag reveal">// process.sh --how-i-work</div>
      <div class="process-grid reveal">
        <div class="process-cell">
          <div class="process-num">01</div>
          <div class="process-title">Business Question</div>
          <div class="process-desc">I start with what the business actually needs to decide, not just what data is available. The question shapes the work.</div>
          <div class="process-cmd">define_problem --before --choosing_work</div>
        </div>
        <div class="process-cell">
          <div class="process-num">02</div>
          <div class="process-title">Discovery</div>
          <div class="process-desc">Review the data, the process, the context, and the stakeholders before forming a view.</div>
          <div class="process-cmd">scan --data --context --stakeholders</div>
        </div>
        <div class="process-cell">
          <div class="process-num">03</div>
          <div class="process-title">Metrics &amp; Workflow</div>
          <div class="process-desc">Set clear measures and map what matters operationally. KPIs should connect to decisions, not decoration.</div>
          <div class="process-cmd">kpi.define --connect_to_decisions</div>
        </div>
        <div class="process-cell">
          <div class="process-num">04</div>
          <div class="process-title">Decision Support</div>
          <div class="process-desc">Turn findings into something a team can act on: recommendation, structure, review path, or implementation direction.</div>
          <div class="process-cmd">output --actionable --not_decorative</div>
        </div>
      </div>
    </section>

    <section class="section" id="credentials">
      <div class="section-tag reveal">// credentials[]</div>
      <div class="cred-block reveal">
        <div class="cred-row">
          <div class="cred-left">
            <div class="cred-year">2026 — 13 MONTHS</div>
            <div class="cred-title">Applied Data Science — Certificate</div>
            <div class="cred-org">ALX / ExploreAI</div>
          </div>
          <a href="{{ '/assets/images/84-data-science-certificate-kabelo-makua.png' | relative_url }}" class="cred-link" target="_blank" rel="noreferrer">View Cert</a>
        </div>
        <div class="cred-row">
          <div class="cred-left">
            <div class="cred-year">2023 — 12 WEEKS</div>
            <div class="cred-title">Entrepreneurship Development Programme</div>
            <div class="cred-org">Startup School</div>
          </div>
          <a href="{{ '/assets/images/Kabelo%20Makua.pdf' | relative_url }}" class="cred-link" target="_blank" rel="noreferrer">View Cert</a>
        </div>
        <div class="cred-row">
          <div class="cred-left">
            <div class="cred-year">IN PROGRESS</div>
            <div class="cred-title">Postgraduate Data Science Path</div>
            <div class="cred-org">Continuing technical development</div>
          </div>
          <span class="cred-link" style="cursor:default;">IN PROGRESS</span>
        </div>
      </div>
    </section>

    <div class="about-cta reveal">
      <a href="{{ '/projects/' | relative_url }}" class="btn-solid">View Projects</a>
      <a href="mailto:{{ site.contact_email }}" class="btn-outline">Get in Touch</a>
    </div>
  </main>
</section>
