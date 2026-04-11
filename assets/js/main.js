(function () {
  var root = document.documentElement;
  var body = document.body;
  var themeKey = 'km-iii-iv-theme';

  function forEachNode(nodes, callback) {
    Array.prototype.forEach.call(nodes || [], callback);
  }

  function runSafely(label, fn) {
    try {
      fn();
    } catch (error) {
      if (window.console && typeof window.console.warn === 'function') {
        window.console.warn(label + ' failed', error);
      }
    }
  }

  function readStorage(key) {
    try {
      return window.localStorage.getItem(key);
    } catch (error) {
      return null;
    }
  }

  function writeStorage(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (error) {
      // Ignore storage failures so they do not block page rendering.
    }
  }

  function getAllowedFilters() {
    return ['all', 'commercial', 'consumer', 'product', 'operations', 'culture'];
  }

  function normalizeFilter(value) {
    var filter = (value || '').toString().toLowerCase();
    return getAllowedFilters().indexOf(filter) >= 0 ? filter : 'all';
  }

  function buildFilterHref(baseHref, filter) {
    if (!baseHref) return '#';

    try {
      var url = new window.URL(baseHref, window.location.origin);
      if (normalizeFilter(filter) === 'all') {
        url.searchParams.delete('filter');
      } else {
        url.searchParams.set('filter', normalizeFilter(filter));
      }
      return url.pathname + url.search + url.hash;
    } catch (error) {
      return baseHref;
    }
  }

  function updateProjectLinks(filter) {
    forEachNode(document.querySelectorAll('[data-project-link]'), function (link) {
      var baseHref = link.getAttribute('data-base-href') || link.getAttribute('href');
      if (!baseHref) return;
      link.setAttribute('href', buildFilterHref(baseHref, filter));
    });
  }

  function updateIndexLinks(filter) {
    forEachNode(document.querySelectorAll('[data-project-index-link]'), function (link) {
      var baseHref = link.getAttribute('href');
      if (!baseHref) return;
      link.setAttribute('href', buildFilterHref(baseHref, filter));
    });
  }

  function applyTheme(theme) {
    body.classList.toggle('light', theme === 'light');
    forEachNode(document.querySelectorAll('[data-mode-toggle]'), function (button) {
      button.textContent = theme === 'light' ? '[ THEME: LIGHT ]' : '[ THEME: GREEN ]';
    });
  }

  function syncTheme() {
    var saved = readStorage(themeKey);
    if (saved === 'light' || saved === 'dark') {
      applyTheme(saved);
      return;
    }

    var prefersLight =
      typeof window.matchMedia === 'function' &&
      window.matchMedia('(prefers-color-scheme: light)').matches;
    applyTheme(prefersLight ? 'light' : 'dark');
  }

  function initModeToggle() {
    syncTheme();

    forEachNode(document.querySelectorAll('[data-mode-toggle]'), function (button) {
      button.addEventListener('click', function () {
        var nextTheme = body.classList.contains('light') ? 'dark' : 'light';
        applyTheme(nextTheme);
        writeStorage(themeKey, nextTheme);
      });
    });
  }

  function initClock() {
    function formatTime(now) {
      try {
        return now.toLocaleTimeString('en-ZA', {
          hour: '2-digit',
          minute: '2-digit',
          second: '2-digit'
        });
      } catch (error) {
        return now.toTimeString().slice(0, 8);
      }
    }

    function tick() {
      var time = formatTime(new Date());
      forEachNode(document.querySelectorAll('[data-status-clock]'), function (node) {
        node.textContent = time + ' SAST';
      });
    }

    tick();
    window.setInterval(tick, 1000);
  }

  function initReveal() {
    var nodes = document.querySelectorAll('.reveal');
    if (!nodes.length || !('IntersectionObserver' in window)) {
      forEachNode(nodes, function (node) {
        node.classList.add('visible');
      });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      forEachNode(entries, function (entry, index) {
        if (entry.isIntersecting) {
          window.setTimeout(function () {
            entry.target.classList.add('visible');
          }, index * 90);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    forEachNode(nodes, function (node) {
      observer.observe(node);
    });
  }

  function initTypewriter() {
    var node = document.querySelector('[data-typewriter]');
    if (!node) return;

    var lines = (node.dataset.typewriter || '')
      .split('||')
      .map(function (line) { return line.trim(); })
      .filter(Boolean);

    if (!lines.length) return;

    var lineIndex = 0;
    var charIndex = 0;
    var deleting = false;

    function step() {
      var line = lines[lineIndex];
      if (!deleting) {
        charIndex += 1;
        node.textContent = line.slice(0, charIndex);
        if (charIndex === line.length) {
          deleting = true;
          window.setTimeout(step, 2800);
          return;
        }
      } else {
        charIndex -= 1;
        node.textContent = line.slice(0, charIndex);
        if (charIndex === 0) {
          deleting = false;
          lineIndex = (lineIndex + 1) % lines.length;
        }
      }
      window.setTimeout(step, deleting ? 26 : 48);
    }

    window.setTimeout(step, 1200);
  }

  function initProjectFilters() {
    var filterButtons = document.querySelectorAll('[data-filter]');
    if (!filterButtons.length) return;

    var cards = document.querySelectorAll('[data-filterable]');
    var sections = document.querySelectorAll('[data-filter-section]');
    var visibleCountNode = document.querySelector('[data-project-visible-count]');

    function setFilter(target, options) {
      var normalizedTarget = normalizeFilter(target);
      var visibleCount = 0;

      forEachNode(filterButtons, function (button) {
        button.classList.toggle('active', button.dataset.filter === normalizedTarget);
      });

      forEachNode(cards, function (card) {
        var filters = (card.dataset.filters || '').split(/\s+/).filter(Boolean);
        var visible = normalizedTarget === 'all' || filters.indexOf(normalizedTarget) >= 0;
        card.classList.toggle('is-hidden', !visible);
        if (visible) visibleCount += 1;
      });

      forEachNode(sections, function (section) {
        var hasVisible = section.querySelector('[data-filterable]:not(.is-hidden)');
        section.classList.toggle('is-hidden', !hasVisible);
      });

      if (visibleCountNode) {
        visibleCountNode.textContent = String(visibleCount);
      }

      updateProjectLinks(normalizedTarget);

      if (options && options.skipHistory) return;

      try {
        var currentUrl = new window.URL(window.location.href);
        if (normalizedTarget === 'all') {
          currentUrl.searchParams.delete('filter');
        } else {
          currentUrl.searchParams.set('filter', normalizedTarget);
        }
        window.history.replaceState({}, '', currentUrl.pathname + currentUrl.search + currentUrl.hash);
      } catch (error) {
        // Ignore history update failures.
      }
    }

    forEachNode(filterButtons, function (button) {
      button.addEventListener('click', function () {
        setFilter(button.dataset.filter || 'all');
      });
    });

    var initialFilter = 'all';
    try {
      initialFilter = normalizeFilter(new window.URL(window.location.href).searchParams.get('filter'));
    } catch (error) {
      initialFilter = 'all';
    }

    setFilter(initialFilter, { skipHistory: true });
  }

  function initProjectNavigator() {
    var rootNode = document.querySelector('[data-project-nav]');
    if (!rootNode) return;

    var currentSlug = rootNode.getAttribute('data-current-slug');
    if (!currentSlug) return;

    var items = [];
    forEachNode(rootNode.querySelectorAll('[data-project-nav-item]'), function (node) {
      items.push({
        slug: node.getAttribute('data-slug'),
        title: node.getAttribute('data-title') || '',
        url: node.getAttribute('data-url') || '',
        log: node.getAttribute('data-log') || '',
        filters: (node.getAttribute('data-filters') || '').split(/\s+/).filter(Boolean)
      });
    });

    if (!items.length) return;

    var filter = 'all';
    try {
      filter = normalizeFilter(new window.URL(window.location.href).searchParams.get('filter'));
    } catch (error) {
      filter = 'all';
    }

    var filteredItems = filter === 'all'
      ? items.slice()
      : items.filter(function (item) {
          return item.filters.indexOf(filter) >= 0;
        });

    var currentIndex = filteredItems.findIndex(function (item) {
      return item.slug === currentSlug;
    });

    if (currentIndex < 0) {
      filter = 'all';
      filteredItems = items.slice();
      currentIndex = filteredItems.findIndex(function (item) {
        return item.slug === currentSlug;
      });
    }

    if (currentIndex < 0) return;

    updateIndexLinks(filter);

    var filterLabelNode = rootNode.querySelector('[data-project-nav-label]');
    if (filterLabelNode) {
      filterLabelNode.textContent = filter === 'all'
        ? 'All projects'
        : filter + ' filter';
    }

    function updateNavLink(selector, item, fallbackTitle) {
      var link = rootNode.querySelector(selector);
      if (!link) return;

      var logNode = link.querySelector('[data-project-nav-prev-log], [data-project-nav-next-log]');
      var titleNode = link.querySelector('[data-project-nav-prev-title], [data-project-nav-next-title]');

      if (!item) {
        link.classList.add('is-disabled');
        link.setAttribute('href', buildFilterHref(rootNode.getAttribute('data-projects-url') || '/projects/', filter));
        if (logNode) logNode.textContent = '';
        if (titleNode) titleNode.textContent = fallbackTitle;
        return;
      }

      link.classList.remove('is-disabled');
      link.setAttribute('href', buildFilterHref(item.url, filter));
      if (logNode) logNode.textContent = item.log ? 'LOG-' + item.log : '';
      if (titleNode) titleNode.textContent = item.title;
    }

    updateNavLink('[data-project-nav-prev]', filteredItems[currentIndex - 1], 'Start of filtered set');
    updateNavLink('[data-project-nav-next]', filteredItems[currentIndex + 1], 'End of filtered set');

    var progressRoot = rootNode.querySelector('[data-project-nav-progress]');
    if (!progressRoot) return;

    var progressInner = document.createElement('div');
    progressInner.className = 'project-nav-progress__inner';

    var pips = document.createElement('div');
    pips.className = 'project-nav-pips';

    filteredItems.forEach(function (item, index) {
      var pip = document.createElement('span');
      pip.className = 'project-nav-pip' + (index === currentIndex ? ' is-active' : '');
      pips.appendChild(pip);
    });

    var label = document.createElement('span');
    label.className = 'project-nav-progress__label';
    label.textContent = String(currentIndex + 1).padStart(2, '0') + ' / ' + String(filteredItems.length).padStart(2, '0');

    progressInner.appendChild(pips);
    progressInner.appendChild(label);
    progressRoot.innerHTML = '';
    progressRoot.appendChild(progressInner);
  }

  runSafely('reveal init', initReveal);
  runSafely('theme init', initModeToggle);
  runSafely('clock init', initClock);
  runSafely('typewriter init', initTypewriter);
  runSafely('project filters init', initProjectFilters);
  runSafely('project navigator init', initProjectNavigator);
})();
