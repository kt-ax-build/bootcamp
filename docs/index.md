---
hide:
  - navigation
  - toc
hide_comments: true
title: AI Agentic Bootcamp
---

<div class="hero-section">
  <div class="hero-animation">
    <div class="floating-icon">🚀</div>
    <div class="floating-icon">🤖</div>
    <div class="floating-icon">⚡</div>
    <div class="floating-icon">💻</div>
  </div>
  
  <div class="hero-content">
    <div class="hero-badge">
      <span class="badge-glow">✨ Next Generation Development</span>
    </div>
    
    <h1 class="hero-title">
      <span class="title-line">
        <span class="highlight-ai">AI</span>
        <span class="highlight-agentic">Agentic</span>
      </span>
      <span class="title-line">
        <span class="highlight-bootcamp">Bootcamp</span>
      </span>
    </h1>
    
    <div class="hero-features">
      <div class="feature-list">
        <div class="feature-item">
          <span class="feature-icon">🎯</span>
          <span class="feature-text">Agile 방법론 통합</span>
        </div>
        <div class="feature-item">
          <span class="feature-icon">⚡</span>
          <span class="feature-text">Agile 기반 AI 활용</span>
        </div>
        <div class="feature-item">
          <span class="feature-icon">🏆</span>
          <span class="feature-text">다양한 Hands-on</span>
        </div>
      </div>
    </div>
  </div>
</div>

<style>
/* Hide default title */
.md-content h1:first-child {
  display: none;
}

/* md-main 영역에 정확히 맞춤 */
.md-main {
  margin: 0;
  padding: 0;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  min-height: 80vh;
}

.md-main__inner {
  margin: 0;
  padding: 0;
  max-width: none;
}

.md-content {
  margin: 0;
  padding: 0;
  max-width: none;
}

.md-content__inner {
  margin: 0;
  padding: 0;
  max-width: none;
}

/* Hero Section */
.hero-section {
  position: relative;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  color: white;
  padding: 4rem 2rem;
  text-align: center;
  margin: 0;
  width: 100%;
  overflow: hidden;
  min-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hero-animation {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.floating-icon {
  position: absolute;
  font-size: 2rem;
  opacity: 0.3;
  animation: float 2s ease-in-out infinite;
}

.floating-icon:nth-child(1) {
  top: 10%;
  left: 10%;
  animation-delay: 0s;
}

.floating-icon:nth-child(2) {
  top: 20%;
  right: 15%;
  animation-delay: 0.5s;
}

.floating-icon:nth-child(3) {
  bottom: 30%;
  left: 20%;
  animation-delay: 1s;
}

.floating-icon:nth-child(4) {
  bottom: 15%;
  right: 10%;
  animation-delay: 2s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
  padding: 0 1rem;
}

.hero-badge {
  display: inline-block;
  margin-bottom: 2rem;
}

.badge-glow {
  background: rgba(255, 255, 255, 0.2);
  padding: 1rem 2.5rem;
  border-radius: 3rem;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  font-weight: 600;
  font-size: 1.1rem;
  animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
  from { box-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
  to { box-shadow: 0 0 30px rgba(255, 255, 255, 0.8); }
}

.hero-title {
  font-size: 5.5rem;
  font-weight: 900;
  margin: 2rem 0;
  line-height: 1.1;
}

.title-line {
  display: block;
  margin: 0.5rem 0;
}

.highlight-ai {
  color: #FFE066;
  text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
  animation: pulse 2s ease-in-out infinite;
}

.highlight-agentic {
  color: #4ECDC4;
  text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
  animation: pulse 2s ease-in-out infinite 0.5s;
}

.highlight-bootcamp {
  color: #FF6B9D;
  text-shadow: 3px 3px 6px rgba(0,0,0,0.4);
  animation: pulse 2s ease-in-out infinite 1s;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.hero-subtitle {
  font-size: 2rem;
  margin: 2rem 0;
  opacity: 0.9;
  font-weight: 300;
}

.hero-features {
  margin-top: 3rem;
}

.feature-list {
  display: flex;
  justify-content: space-between;
  gap: 4rem;
  flex-wrap: wrap;
  max-width: 1000px;
  margin: 0 auto;
  padding: 0 2rem;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
  text-align: center;
}

.feature-icon {
  font-size: 3.5rem;
  margin-bottom: 1rem;
}

.feature-text {
  font-size: 1.3rem;
  font-weight: 400;
  opacity: 0.9;
  white-space: nowrap;
}

/* Responsive Design */
@media (max-width: 1200px) {
  .feature-list {
    max-width: 800px;
    gap: 3rem;
  }
}

@media (max-width: 768px) {
  .hero-section {
    padding: 3rem 1rem;
    margin: 0;
    width: 100%;
    min-height: 65vh;
  }
  
  .hero-content {
    padding: 0 0.5rem;
  }
  
  .hero-title {
    font-size: 3rem;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
  }
  
  .feature-list {
    gap: 2rem;
    padding: 0 1rem;
    max-width: 100%;
    justify-content: center;
  }
  
  .feature-icon {
    font-size: 2rem;
  }
  
  .feature-text {
    font-size: 0.9rem;
  }
}

@media (max-width: 480px) {
  .hero-section {
    padding: 2rem 1rem;
    margin: 0;
    width: 100%;
    min-height: 55vh;
  }
  
  .hero-content {
    padding: 0 0.5rem;
  }
  
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1rem;
    margin: 1.5rem 0;
  }
  
  .hero-features {
    margin-top: 2rem;
  }
  
  .feature-list {
    gap: 1.5rem;
    padding: 0 0.5rem;
    justify-content: center;
  }
  
  .feature-icon {
    font-size: 1.8rem;
  }
  
  .feature-text {
    font-size: 0.85rem;
  }
}
</style>
