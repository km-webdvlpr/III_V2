---
layout: home
title: Product Data Analyst Portfolio
description: I'm Kabelo. I work as a Product Data Analyst, using data to support clearer product and business decisions.
status_context: JHB, ZA // AVAILABLE
body_class: page-home
---
{% assign homepage_count = 0 %}
{% for entry in site.data.project_registry %}
  {% if entry.homepage %}
    {% assign homepage_count = homepage_count | plus: 1 %}
  {% endif %}
{% endfor %}

<section class="hero">
  <div class="grid-bg"></div>
  <div class="vignette"></div>

  <div class="hero-left">
    <div class="prompt-line">
      <span class="dollar">$</span>
      <span>kabelo@{{ site.mark_name }}:~</span>
      <span class="cursor"></span>
    </div>

    <h1 class="hero-name">
      Kabelo<br>
      <span class="accent">Makua</span>
    </h1>

    <div class="version-tag">v {{ site.mark_name }} &nbsp;//&nbsp; {{ site.location_label }}</div>

    <div class="typewriter-box">
      <p data-typewriter="I'm Kabelo. I work as a Product Data Analyst, building analysis around business questions and practical decisions.||My work sits between analytics, product thinking, and decision support, helping teams see what matters and what to do next.||I'm especially aligned with EdTech, FinTech, and digital product teams, but the work travels well across industries."></p>
    </div>

    <p class="tagline">
      Based in {{ site.location_label }} &nbsp;//&nbsp; Open to work<br>
      Product Data Analyst &nbsp;//&nbsp; Product Thinking &nbsp;//&nbsp; Especially aligned with EdTech / FinTech
    </p>

    <div class="cta-row">
      <a href="{{ '/projects/' | relative_url }}" class="btn-solid">Browse Projects</a>
      <a href="{{ '/about/' | relative_url }}" class="btn-outline">About My Process</a>
    </div>
  </div>

  <div class="hero-right">
    <div class="hero-terminal reveal visible">
      <div class="hero-terminal__bar">
        <div class="hero-terminal__dot"></div>
        <div class="hero-terminal__dot"></div>
        <div class="hero-terminal__dot"></div>
        <span class="hero-terminal__title">profile.sh - bash</span>
      </div>
      <div class="hero-terminal__body">
        <div class="hero-terminal__section">// CURRENT FOCUS</div>
        <div class="hero-terminal__row"><span class="hero-terminal__arrow">&rarr;</span><span class="hero-terminal__cmd">analyst.exe --role product-data</span></div>
        <div class="hero-terminal__out hero-terminal__out--hi">Product questions. KPI logic.</div>
        <div class="hero-terminal__out">Decision support teams can use.</div>
        <hr class="hero-terminal__divider">
        <div class="hero-terminal__section">// TOOLKIT</div>
        <div class="hero-terminal__row"><span class="hero-terminal__arrow">&rarr;</span><span class="hero-terminal__cmd">skills --list</span></div>
        <div class="hero-terminal__out">SQL &middot; Python &middot; Power BI &middot; dbt</div>
        <div class="hero-terminal__out hero-terminal__out--hi">Product analytics // KPI design</div>
        <div class="hero-terminal__out">Workflow thinking // stakeholder context</div>
        <hr class="hero-terminal__divider">
        <div class="hero-terminal__section">// BEST FIT NOW</div>
        <div class="hero-terminal__row"><span class="hero-terminal__arrow">&rarr;</span><span class="hero-terminal__cmd">match --sector edtech fintech</span></div>
        <div class="hero-terminal__out">Product Data Analyst</div>
        <div class="hero-terminal__out">Product analytics // Commercial insights</div>
        <div class="hero-terminal__out hero-terminal__out--hi">EdTech // FinTech // Digital product teams</div>
        <hr class="hero-terminal__divider">
        <div class="hero-terminal__status">status: <span class="hero-terminal__out--hi">AVAILABLE</span> <span class="cursor" style="width:7px;height:12px;"></span></div>
      </div>
    </div>
  </div>
</section>

<section class="section-shell">
  <div class="section-label reveal">// BEST FIT</div>
  <h2 class="section-title reveal">Where I Fit Now</h2>
  <div class="fit-grid">
    <div class="fit-card reveal">
      <div class="fit-card-label">STRONGEST MATCH</div>
      <div class="fit-card-title">Product Data<br>Analyst</div>
      <div class="fit-card-body">Product, commercial, and customer analysis shaped around business questions, KPI logic, and usable decision support.</div>
    </div>
    <div class="fit-card reveal">
      <div class="fit-card-label">NATURAL PROGRESSION</div>
      <div class="fit-card-title">Senior Analytics<br>Strategy Lead</div>
      <div class="fit-card-body">Insights manager. Product or commercial strategy roles where analysis shapes direction.</div>
    </div>
    <div class="fit-card reveal">
      <div class="fit-card-label">BEST ENVIRONMENT</div>
      <div class="fit-card-title">Teams That Need<br>Signal into Decision</div>
      <div class="fit-card-body">Teams using product, customer, and commercial evidence to make clearer next-step decisions.</div>
    </div>
  </div>
</section>

<section class="section-shell">
  <div class="feed-section-header reveal">
    <span class="feed-section-label">// FEATURED CASE FILES</span>
    <div class="feed-section-line"></div>
    <span class="feed-section-count">{{ homepage_count }}</span>
  </div>
  <div class="featured-grid">
    {% for entry in site.data.project_registry %}
      {% if entry.homepage %}
        {% for project in site.projects %}
          {% if project.slug == entry.slug %}
          {% assign meta = entry %}
          {% include project-card.html project=project meta=meta variant='featured' %}
          {% break %}
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </div>
</section>

<section class="section-shell">
  <div class="feed-section-header reveal">
    <span class="feed-section-label">// CORE TOOLKIT</span>
    <div class="feed-section-line"></div>
    <span class="feed-section-count">ANALYST STACK</span>
  </div>
  <div class="compact-grid">
    <div class="compact-card reveal">
      <h3 class="compact-title">Technical Delivery</h3>
      <p class="compact-desc">SQL, Python, Power BI, dbt, data modelling, and analytics engineering foundations.</p>
      <div class="compact-tags">
        <span class="compact-tag">#SQL</span>
        <span class="compact-tag">#Python</span>
        <span class="compact-tag">#PowerBI</span>
      </div>
    </div>
    <div class="compact-card reveal">
      <h3 class="compact-title">Decision Support</h3>
      <p class="compact-desc">Business analysis, KPI logic, workflow framing, and practical recommendation-building.</p>
      <div class="compact-tags">
        <span class="compact-tag">#BusinessAnalysis</span>
        <span class="compact-tag">#KPIDesign</span>
        <span class="compact-tag">#ProcessThinking</span>
      </div>
    </div>
  </div>
</section>
