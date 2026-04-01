(function () {
  var root = document.documentElement;
  var body = document.body;
  var themeKey = 'km-iii-iv-theme';

  function applyTheme(theme) {
    body.classList.toggle('light', theme === 'light');
  }

  function syncTheme() {
    var saved = localStorage.getItem(themeKey);
    if (saved === 'light' || saved === 'dark') {
      applyTheme(saved);
      return;
    }
    applyTheme(window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  }

  function initModeToggle() {
    syncTheme();
    document.querySelectorAll('[data-mode-toggle]').forEach(function (button) {
      button.addEventListener('click', function () {
        var nextTheme = body.classList.contains('light') ? 'dark' : 'light';
        applyTheme(nextTheme);
        localStorage.setItem(themeKey, nextTheme);
      });
    });
  }

  function initClock() {
    function tick() {
      var now = new Date();
      var time = now.toLocaleTimeString('en-ZA', {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit'
      });
      document.querySelectorAll('[data-status-clock]').forEach(function (node) {
        node.textContent = time + ' SAST';
      });
    }
    tick();
    window.setInterval(tick, 1000);
  }

  function initReveal() {
    var nodes = document.querySelectorAll('.reveal');
    if (!nodes.length || !('IntersectionObserver' in window)) {
      nodes.forEach(function (node) { node.classList.add('visible'); });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry, index) {
        if (entry.isIntersecting) {
          window.setTimeout(function () {
            entry.target.classList.add('visible');
          }, index * 90);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    nodes.forEach(function (node) {
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

    function setFilter(target) {
      filterButtons.forEach(function (button) {
        button.classList.toggle('active', button.dataset.filter === target);
      });

      cards.forEach(function (card) {
        var filters = (card.dataset.filters || '').split(/\s+/).filter(Boolean);
        var visible = target === 'all' || filters.indexOf(target) >= 0;
        card.classList.toggle('is-hidden', !visible);
      });

      sections.forEach(function (section) {
        var hasVisible = section.querySelector('[data-filterable]:not(.is-hidden)');
        section.classList.toggle('is-hidden', !hasVisible);
      });
    }

    filterButtons.forEach(function (button) {
      button.addEventListener('click', function () {
        setFilter(button.dataset.filter || 'all');
      });
    });
  }

  initModeToggle();
  initClock();
  initReveal();
  initTypewriter();
  initProjectFilters();
})();
