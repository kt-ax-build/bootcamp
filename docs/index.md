---
hide_comments: true
title: AI Agentic Bootcamp
---

<script>
  // This script only runs in MkDocs, not on GitHub
  var hideGitHubVersion = function() {
    document.querySelectorAll('.github-only').forEach(el => el.style.display = 'none');
  };

  // Handle both initial load and subsequent navigation
  document.addEventListener('DOMContentLoaded', hideGitHubVersion);
  document$.subscribe(hideGitHubVersion);
</script>

<style>
.md-content h1 {
  display: none;
}
/* .md-header__topic {
  display: none;
} */
</style>

{% include-markdown "./README.md" %}
