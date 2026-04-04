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

  function applyTheme(theme) {
    body.classList.toggle('light', theme === 'light');
    forEachNode(document.querySelectorAll('[data-mode-toggle]'), function (button) {
      button.textContent = theme === 'light' ? '[ THEME: LIGHT ]' : '[ THEME: DARK ]';
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

    function setFilter(target) {
      forEachNode(filterButtons, function (button) {
        button.classList.toggle('active', button.dataset.filter === target);
      });

      forEachNode(cards, function (card) {
        var filters = (card.dataset.filters || '').split(/\s+/).filter(Boolean);
        var visible = target === 'all' || filters.indexOf(target) >= 0;
        card.classList.toggle('is-hidden', !visible);
      });

      forEachNode(sections, function (section) {
        var hasVisible = section.querySelector('[data-filterable]:not(.is-hidden)');
        section.classList.toggle('is-hidden', !hasVisible);
      });
    }

    forEachNode(filterButtons, function (button) {
      button.addEventListener('click', function () {
        setFilter(button.dataset.filter || 'all');
      });
    });
  }

  runSafely('reveal init', initReveal);
  runSafely('theme init', initModeToggle);
  runSafely('clock init', initClock);
  runSafely('typewriter init', initTypewriter);
  runSafely('project filters init', initProjectFilters);
})();
