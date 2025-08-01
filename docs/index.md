---
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
    
    <p class="hero-subtitle">
      차세대 개발자를 위한 개발 가이드
    </p>
    
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

/* Hero Section */
.hero-section {
  position: relative;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
  color: white;
  padding: 4rem 2rem;
  text-align: center;
  margin: -1.5rem -1.5rem 0 -1.5rem;
  overflow: hidden;
  min-height: 60vh;
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
  animation: float 6s ease-in-out infinite;
}

.floating-icon:nth-child(1) {
  top: 10%;
  left: 10%;
  animation-delay: 0s;
}

.floating-icon:nth-child(2) {
  top: 20%;
  right: 15%;
  animation-delay: 1.5s;
}

.floating-icon:nth-child(3) {
  bottom: 30%;
  left: 20%;
  animation-delay: 3s;
}

.floating-icon:nth-child(4) {
  bottom: 15%;
  right: 10%;
  animation-delay: 4.5s;
}

@keyframes float {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-20px) rotate(180deg); }
}

.hero-content {
  position: relative;
  z-index: 2;
  max-width: 900px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-block;
  margin-bottom: 2rem;
}

.badge-glow {
  background: rgba(255, 255, 255, 0.2);
  padding: 0.8rem 2rem;
  border-radius: 3rem;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  font-weight: 600;
  animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
  from { box-shadow: 0 0 20px rgba(255, 255, 255, 0.5); }
  to { box-shadow: 0 0 30px rgba(255, 255, 255, 0.8); }
}

.hero-title {
  font-size: 4.5rem;
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
  font-size: 1.5rem;
  margin: 2rem 0;
  opacity: 0.9;
  font-weight: 300;
}

.hero-features {
  margin-top: 3rem;
}

.feature-list {
  display: flex;
  justify-content: center;
  gap: 3rem;
  flex-wrap: wrap;
}

.feature-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.8rem;
  text-align: center;
}

.feature-icon {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.feature-text {
  font-size: 1rem;
  font-weight: 400;
  opacity: 0.9;
  white-space: nowrap;
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero-section {
    padding: 3rem 1rem;
    min-height: 50vh;
  }
  
  .hero-title {
    font-size: 3rem;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
  }
  
  .feature-list {
    gap: 2rem;
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
    min-height: 45vh;
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
  }
  
  .feature-icon {
    font-size: 1.8rem;
  }
  
  .feature-text {
    font-size: 0.85rem;
  }
}
</style>
