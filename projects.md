---
layout: projects
title: Projects
description: Selected case studies showing how I move from business questions and KPI logic into analysis, workflow thinking, and usable outputs.
status_context: PROJECTS INDEX // 14 ENTRIES
body_class: page-projects
---
{% assign projects_sorted = site.projects | sort: 'date' | reverse %}
{% assign featured_count = 0 %}
{% assign skill_build_count = 0 %}
{% assign creative_count = 0 %}
{% for project in projects_sorted %}
  {% assign meta = site.data.project_meta[project.slug] %}
  {% if meta.group == 'featured' %}{% assign featured_count = featured_count | plus: 1 %}{% endif %}
  {% if meta.group == 'skill-build' %}{% assign skill_build_count = skill_build_count | plus: 1 %}{% endif %}
  {% if meta.group == 'creative' %}{% assign creative_count = creative_count | plus: 1 %}{% endif %}
{% endfor %}

<section class="page-header">
  <div class="breadcrumb">HOME <span>//</span> PROJECTS</div>
  <h1 class="page-title">Projects</h1>
  <p class="page-desc">Selected case studies showing how I move from business questions and KPI logic into analysis, workflow thinking, and usable outputs.</p>
</section>

<section class="filter-bar">
  <span class="filter-label">FILTER //</span>
  <button class="filter-btn active" type="button" data-filter="all">All</button>
  <button class="filter-btn" type="button" data-filter="analytics">Analytics</button>
  <button class="filter-btn" type="button" data-filter="product">Product</button>
  <button class="filter-btn" type="button" data-filter="edtech">EdTech</button>
  <button class="filter-btn" type="button" data-filter="culture">Culture</button>
</section>

<section class="projects-layout">
  <aside class="sidebar">
    <div class="sidebar-label">// FEATURED</div>
    {% for slug in site.featured_priority %}
      {% for project in projects_sorted %}
        {% assign meta = site.data.project_meta[project.slug] %}
        {% if project.slug == slug and meta.group == 'featured' %}
        <a class="sidebar-link" href="{{ project.url | relative_url }}">{{ project.title }}</a>
        {% break %}
        {% endif %}
      {% endfor %}
    {% endfor %}

    <hr class="sidebar-divider">
    <div class="sidebar-label">// SKILL-BUILD</div>
    {% for project in projects_sorted %}
      {% assign meta = site.data.project_meta[project.slug] %}
      {% if meta.group == 'skill-build' %}
      <a class="sidebar-link" href="{{ project.url | relative_url }}">{{ project.title }}</a>
      {% endif %}
    {% endfor %}

    <hr class="sidebar-divider">
    <div class="sidebar-label">// CREATIVE</div>
    {% for project in projects_sorted %}
      {% assign meta = site.data.project_meta[project.slug] %}
      {% if meta.group == 'creative' %}
      <a class="sidebar-link" href="{{ project.url | relative_url }}">{{ project.title }}</a>
      {% endif %}
    {% endfor %}

    <hr class="sidebar-divider">
    <div class="sidebar-meta">
      TOTAL PROJECTS: <span class="hi">{{ projects_sorted.size }}</span><br>
      FEATURED: <span class="hi">{{ featured_count }}</span><br>
      SKILL-BUILD: <span class="hi">{{ skill_build_count }}</span><br>
      CREATIVE: <span class="hi">{{ creative_count }}</span>
    </div>
  </aside>

  <main class="project-feed">
    <section data-filter-section>
      <div class="feed-section-header reveal">
        <span class="feed-section-label">// FEATURED ANALYST CASE STUDIES</span>
        <div class="feed-section-line"></div>
        <span class="feed-section-count">{{ featured_count }}</span>
      </div>

      {% for slug in site.featured_priority %}
        {% for project in projects_sorted %}
          {% assign meta = site.data.project_meta[project.slug] %}
          {% if project.slug == slug and meta.group == 'featured' %}
            {% include project-card.html project=project meta=meta variant='featured' %}
            {% break %}
          {% endif %}
        {% endfor %}
      {% endfor %}
    </section>

    <section data-filter-section>
      <div class="feed-section-header reveal">
        <span class="feed-section-label">// SKILL-BUILDING PROJECTS</span>
        <div class="feed-section-line"></div>
        <span class="feed-section-count">{{ skill_build_count }}</span>
      </div>
      <div class="compact-grid">
        {% for project in projects_sorted %}
          {% assign meta = site.data.project_meta[project.slug] %}
          {% if meta.group == 'skill-build' %}
            {% include project-card.html project=project meta=meta variant='compact' %}
          {% endif %}
        {% endfor %}
      </div>
    </section>

    <section data-filter-section>
      <div class="feed-section-header reveal">
        <span class="feed-section-label">// CREATIVE SPACE</span>
        <div class="feed-section-line"></div>
        <span class="feed-section-count">{{ creative_count }}</span>
      </div>
      <p class="page-desc reveal" style="margin-bottom:1.2rem;max-width:none;">Storytelling and design projects outside the core analytics portfolio.</p>
      <div class="creative-grid">
        {% for project in projects_sorted %}
          {% assign meta = site.data.project_meta[project.slug] %}
          {% if meta.group == 'creative' %}
            {% include project-card.html project=project meta=meta variant='creative' %}
          {% endif %}
        {% endfor %}
      </div>
    </section>
  </main>
</section>
