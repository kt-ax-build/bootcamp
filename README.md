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
├── main.py                           # MkDocs 매크로 플러그인 설정
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

# 문서 구조 확인 (매크로 처리 과정 포함)
uv run mkdocs serve --verbose

# 매크로 처리 상태 확인 (빌드 시 매크로 오류 디버깅)
uv run mkdocs build --verbose

# 특정 포트에서 개발 서버 실행
uv run mkdocs serve -a 127.0.0.1:8080
```

## 📦 사용된 주요 패키지

이 프로젝트는 다음 패키지들을 사용합니다:

- **mkdocs**: 정적 사이트 생성기
- **mkdocs-material**: Material Design 테마
- **mkdocs-awesome-nav**: 네비게이션 자동 생성 및 관리
- **mkdocs-macros-plugin**: 동적 콘텐츠 생성을 위한 매크로 지원
- **mkdocs-include-markdown-plugin**: 마크다운 파일 include 기능
- **mkdocs-autorefs**: 자동 참조 링크 생성
- **mkdocs-puml**: PlantUML 다이어그램 지원
- **markdown-include**: 마크다운 include 확장

전체 의존성은 `pyproject.toml` 파일에서 확인할 수 있습니다.

## 🚀 배포

### GitHub Pages 자동 배포

이 프로젝트는 GitHub Actions를 통한 자동 배포가 설정되어 있습니다:

- **수동 트리거**: `workflow_dispatch` 이벤트로 수동 실행
- **자동 배포**: 필요시 `main` 브랜치 push 시 자동 배포 (현재 비활성화)

배포를 위해 GitHub Actions의 "ci" 워크플로우를 수동으로 실행하세요.

### 수동 배포

> [!CAUTION]
> **왠만하면 실행하지마세요.**


```bash
# GitHub Pages에 배포
uv run mkdocs gh-deploy --force
```

## 🎯 주요 기능

### Material Design 테마 활용

- **반응형 디자인**: Material Design 테마로 모든 디바이스에서 최적화된 UI
- **다크/라이트 모드**: 사용자 선호에 따른 테마 전환 기능
- **커스텀 폰트**: 한글 가독성을 위한 "Hanna" 폰트와 코드용 "Roboto Mono" 적용
- **브랜딩**: 커스텀 로고 및 파비콘 설정

#### mkdocs.yml 설정:
```yaml
theme:
  name: material
  highlightjs: true
  palette:
    - scheme: default
      primary: red
      accent: red
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: red
      accent: red
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  font:
    text: "Hanna"
    code: "Roboto Mono"
  logo: assets/logo.png
  favicon: assets/favicon.png
```

### 네비게이션 기능

- **구조화된 탐색**: `navigation.sections`로 문서 구조 명확화
- **경로 표시**: `navigation.path`로 현재 위치 추적
- **인덱스 페이지**: `navigation.indexes`로 섹션별 랜딩 페이지 제공
- **상단 네비게이션**: `navigation.top`으로 빠른 상단 이동
- **실시간 추적**: `navigation.tracking`으로 URL 자동 업데이트

#### mkdocs.yml 설정:
```yaml
theme:
  features:
    - navigation.indexes
    - navigation.path
    - navigation.sections
    - navigation.top
    - navigation.tracking
    - toc.follow
    - content.code.copy
    - content.code.select
    - content.tooltips
```

### 콘텐츠 기능

- **코드 블록 향상**: 코드 복사(`content.code.copy`) 및 선택(`content.code.select`) 기능
- **툴팁 지원**: `content.tooltips`로 추가 정보 제공
- **목차 연동**: `toc.follow`로 읽기 위치에 따른 목차 하이라이트

### Markdown 확장 기능

- **Admonition**: 주의사항, 팁, 경고 등의 강조 박스
  ```markdown
  !!! note "참고"
      중요한 정보를 강조할 때 사용
  ```

- **Details & Summary**: 접을 수 있는 콘텐츠 섹션
  ```markdown
  ??? info "더 보기"
      숨겨진 내용이 여기에 표시됩니다.
  ```

- **향상된 코드 블록**: `pymdownx.superfences`로 다양한 언어 지원 및 문법 하이라이트
- **목차 생성**: `toc` 확장으로 자동 목차 생성 및 고유 링크 제공

#### mkdocs.yml 설정:
```yaml
markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - toc:
      permalink: true
```

### 플러그인 활용

- **자동 참조**: `autorefs` 플러그인으로 문서 간 링크 자동 생성
- **스마트 네비게이션**: `awesome-nav` 플러그인으로 디렉토리 구조 기반 자동 메뉴 생성
- **동적 콘텐츠**: `macros` 플러그인으로 Python 함수를 통한 매크로 기능
- **파일 포함**: `include-markdown` 플러그인으로 재사용 가능한 콘텐츠 관리
- **외부 링크**: `open-in-new-tab` 플러그인으로 외부 링크 새 탭 열기
- **PlantUML 지원**: 다이어그램 및 차트 렌더링
  ```puml
  @startuml
  participant User
  participant System
  User -> System: 요청
  System -> User: 응답
  @enduml
  ```
- **통합 검색**: 한국어 검색 최적화 및 실시간 검색 결과
- **태그 시스템**: 문서 분류 및 필터링으로 체계적인 콘텐츠 관리

#### mkdocs.yml 설정:
```yaml
plugins:
  - autorefs
  - awesome-nav              # 자동 네비게이션 생성
  - include-markdown
  - macros:                  # 매크로 기능
      module_name: main
  - open-in-new-tab
  - plantuml:
      puml_url: https://www.plantuml.com/plantuml/
  - search:
      separator: '[\s\u200b\-,:!=\[\]()"`/]+|\.(?!\d)|&[lg]t;'
  - tags
```

### 자동화된 네비게이션 및 매크로 기능

#### MkDocs Awesome Nav

`mkdocs-awesome-nav` 플러그인을 통해 네비게이션을 자동으로 생성하고 관리할 수 있습니다:

- **자동 네비게이션**: 디렉토리 구조를 기반으로 자동 메뉴 생성
- **섹션별 관리**: `.nav.yml` 파일을 통한 유연한 네비게이션 구성
- **동적 메뉴**: 파일 추가/삭제 시 자동 반영

#### MkDocs Macros Plugin

`mkdocs-macros-plugin`을 통해 동적 콘텐츠 생성이 가능합니다:

**사용 가능한 매크로 함수들:**

- `{{ auto_nav_current_dir() }}`: 현재 디렉토리의 파일들을 자동으로 나열
- `{{ list_directory_files('경로') }}`: 특정 디렉토리의 파일들을 나열
- `{{ list_subdirectories('경로') }}`: 특정 디렉토리의 하위 디렉토리들을 나열
- `{{ get_current_directory() }}`: 현재 페이지가 위치한 디렉토리 이름 반환

**매크로 사용 예시:**

```markdown
# {{ get_current_directory() | title }} 

이 섹션의 내용을 소개합니다.

## 📖 목차
{{ auto_nav_current_dir() }}

## 📁 하위 섹션
{{ list_subdirectories('.') }}

## 특정 디렉토리 파일 목록
{{ list_directory_files('doc-hands-on') }}
```

**고급 옵션:**

```markdown
<!-- .py 파일만 나열 -->
{{ list_directory_files('scripts', file_extensions=['.py']) }}

<!-- index 파일도 포함해서 나열 -->
{{ list_directory_files('.', exclude_index=False) }}
```

**매크로 설정 파일:**

`main.py` 파일에서 매크로 함수들을 정의하고 관리합니다:

```python
def define_env(env):
    @env.macro
    def list_directory_files(directory_path, exclude_index=True, file_extensions=None):
        # 디렉토리 파일 목록 생성 로직
        ...
```

### 추가 커스터마이징

#### 커스텀 CSS:
```yaml
extra_css:
  - extra.css
```

이 설정을 통해 `docs/extra.css` 파일에서 추가적인 스타일 커스터마이징이 가능합니다.

## 🤝 Contributing

1. **문서 수정**: `docs/` 디렉토리 내 마크다운 파일을 편집
2. **새로운 페이지 추가**: 
   - `awesome-nav` 플러그인이 자동으로 메뉴에 반영
   - 필요시 `docs/.nav.yml` 파일에서 네비게이션 구조 조정
3. **매크로 기능 확장**: `main.py` 파일에서 새로운 매크로 함수 추가
4. **동적 콘텐츠 활용**: index 페이지에서 `{{ auto_nav_current_dir() }}` 등의 매크로 사용
5. **로컬 테스트**: `uv run mkdocs serve`로 변경사항 확인
6. **Pull Request 생성**

### 매크로 기능 사용 가이드

- **index.md 파일 생성 시**: `{{ auto_nav_current_dir() }}`로 자동 목차 생성
- **디렉토리 구조 표시**: `{{ list_subdirectories('.') }}`로 하위 폴더 나열
- **특정 파일 타입 필터링**: `{{ list_directory_files('.', file_extensions=['.py']) }}`

## 📄 License

- Educational content and documentation: [CC BY 4.0](./LICENSE)
