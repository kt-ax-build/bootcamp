# AI Agentic Bootcamp

AI 에이전틱 기술을 활용한 현대적 소프트웨어 개발 방법론을 학습하는 부트캠프 강의 교안입니다.

## 🚀 프로젝트 개요

이 프로젝트는 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)을 사용하여 제작된 정적 문서 사이트입니다. AI Agentic 기술과 Agile 방법론을 결합한 실무 중심의 교육 과정 자료를 포함하고 있습니다.

## 📁 디렉토리 구조

```
bootcamp/
├── docs/                              # 문서 파일들
│   ├── agile/                         # AX Build Agile 관련 문서
│   │   └── ax-build-intro.md
│   ├── agile-ai-lead/                 # Agile 기반 AI 활용 문서
│   │   ├── agile-ai-coding.md
│   │   ├── ai-lead-poc.md
│   │   ├── deliver-develop.md
│   │   ├── deliver-planning.md
│   │   └── discover-prd.md
│   ├── hands-on/                      # 실습 관련 문서
│   │   ├── dev-environment.md
│   │   ├── mcp-setup.md
│   │   └── practice-tasks.md
│   ├── introduction/                  # 교육 과정 소개
│   │   └── course-overview.md
│   ├── extra.css                      # 추가 스타일시트
│   ├── index.md                       # 메인 페이지
│   └── README.md                      # 문서 내용 (index.md에서 include)
├── .github/workflows/                 # GitHub Actions 워크플로우
│   └── ci.yml                         # 자동 배포 설정
├── mkdocs.yml                         # MkDocs 설정 파일
├── pyproject.toml                     # Python 프로젝트 설정 (uv 기반)
├── uv.lock                           # uv 잠금 파일
└── README.md                         # 프로젝트 README
```

## 🔧 환경 설정

### 1. 사전 요구사항

- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** (Python 패키지 관리자)

### 2. uv 설치

macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 3. 프로젝트 설정

```bash
# 저장소 클론
git clone <repository-url>
cd bootcamp

# 의존성 설치 (pyproject.toml 기반)
uv sync

# 가상환경 활성화 (선택사항 - uv run으로도 실행 가능)
source .venv/bin/activate  # macOS/Linux
# 또는
.venv\Scripts\activate     # Windows
```

## 🖥️ 로컬 개발

### MkDocs 개발 서버 실행

```bash
# uv를 통한 실행 (권장)
uv run mkdocs serve

# 또는 가상환경 활성화 후
mkdocs serve
```

개발 서버가 시작되면 브라우저에서 `http://127.0.0.1:8000`으로 접속하여 문서를 확인할 수 있습니다.

### 기타 유용한 명령어

```bash
# 문서 빌드 (정적 파일 생성)
uv run mkdocs build

# 문서 구조 확인
uv run mkdocs serve --verbose
```

## 📦 사용된 주요 패키지

이 프로젝트는 다음 패키지들을 사용합니다:

- **mkdocs**: 정적 사이트 생성기
- **mkdocs-material**: Material Design 테마
- **mkdocs-include-markdown-plugin**: 마크다운 파일 include 기능
- **mkdocs-autorefs**: 자동 참조 링크 생성
- **mkdocs-build-plantuml-plugin**: PlantUML 다이어그램 지원
- **markdown-include**: 마크다운 include 확장

전체 의존성은 `pyproject.toml` 파일에서 확인할 수 있습니다.

## 🚀 배포

### GitHub Pages 자동 배포

이 프로젝트는 GitHub Actions를 통한 자동 배포가 설정되어 있습니다:

- **수동 트리거**: `workflow_dispatch` 이벤트로 수동 실행
- **자동 배포**: 필요시 `main` 브랜치 push 시 자동 배포 (현재 비활성화)

배포를 위해 GitHub Actions의 "ci" 워크플로우를 수동으로 실행하세요.

### 수동 배포

왠만하면 실행하지마세요.

```bash
# GitHub Pages에 배포
uv run mkdocs gh-deploy --force
```

## 🎯 주요 기능

- **반응형 디자인**: Material Design 테마
- **다크/라이트 모드**: 테마 전환 기능
- **검색 기능**: 문서 내 통합 검색
- **태그 시스템**: 문서 분류 및 필터링
- **자동 참조**: 문서 간 링크 자동 생성
- **PlantUML 지원**: 다이어그램 렌더링

## 🤝 Contributing

1. 문서 수정은 `docs/` 디렉토리 내 마크다운 파일을 편집
2. 새로운 페이지 추가 시 `mkdocs.yml`의 `nav` 섹션에 등록
3. 로컬에서 `uv run mkdocs serve`로 변경사항 확인
4. Pull Request 생성

## 📄 License

- Educational content and documentation: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Code and scripts: [MIT License](./LICENSE)
