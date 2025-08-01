from pathlib import Path

def define_env(env):
    """
    MkDocs 매크로 플러그인용 환경 정의
    """
    
    @env.macro
    def list_directory_files(directory_path, exclude_index=True, file_extensions=None):
        """
        지정된 디렉토리의 파일들을 리스트로 반환
        
        Args:
            directory_path: 문서 디렉토리를 기준으로 한 상대 경로
            exclude_index: index.md 파일을 제외할지 여부 (기본값: True)
            file_extensions: 포함할 파일 확장자 리스트 (기본값: ['.md'])
        
        Returns:
            마크다운 형식의 파일 리스트
        """
        if file_extensions is None:
            file_extensions = ['.md']
        
        # docs 디렉토리를 기준으로 한 절대 경로 생성
        docs_dir = Path(env.conf['docs_dir'])
        target_dir = docs_dir / directory_path
        
        if not target_dir.exists():
            return f"⚠️ Directory not found: {directory_path}"
        
        files = []
        for file_path in sorted(target_dir.iterdir()):
            if file_path.is_file():
                # 파일 확장자 체크
                if file_path.suffix in file_extensions:
                    # index 파일 제외 옵션 체크
                    if exclude_index and file_path.stem == 'index':
                        continue
                    
                    # 파일명에서 확장자 제거
                    file_title = file_path.stem.replace('-', ' ').replace('_', ' ').title()
                    
                    # 상대 경로 생성
                    relative_path = f"{directory_path}/{file_path.name}"
                    
                    files.append(f"- [{file_title}]({relative_path})")
        
        if not files:
            return "📝 No files found in this directory."
        
        return '\n'.join(files)
    
    @env.macro
    def list_subdirectories(directory_path, max_depth=1):
        """
        지정된 디렉토리의 하위 디렉토리들을 리스트로 반환
        
        Args:
            directory_path: 문서 디렉토리를 기준으로 한 상대 경로
            max_depth: 탐색할 최대 깊이 (기본값: 1)
        
        Returns:
            마크다운 형식의 디렉토리 리스트
        """
        docs_dir = Path(env.conf['docs_dir'])
        target_dir = docs_dir / directory_path
        
        if not target_dir.exists():
            return f"⚠️ Directory not found: {directory_path}"
        
        directories = []
        for dir_path in sorted(target_dir.iterdir()):
            if dir_path.is_dir() and not dir_path.name.startswith('.'):
                # 디렉토리명을 제목으로 변환
                dir_title = dir_path.name.replace('-', ' ').replace('_', ' ').title()
                
                # index.md 파일이 있는지 확인
                index_file = dir_path / 'index.md'
                if index_file.exists():
                    relative_path = f"{directory_path}/{dir_path.name}/"
                    directories.append(f"- [{dir_title}]({relative_path})")
                else:
                    directories.append(f"- **{dir_title}**")
        
        if not directories:
            return "📁 No subdirectories found."
        
        return '\n'.join(directories)
    
    @env.macro
    def auto_nav_current_dir():
        """
        현재 페이지의 디렉토리에 있는 파일들을 자동으로 내비게이션 형태로 생성
        """
        # 현재 페이지의 경로 가져오기
        current_page = env.page
        if not current_page:
            return "⚠️ Page context not available"
        
        # 현재 파일의 디렉토리 경로 추출
        current_file_path = Path(current_page.file.src_path)
        current_dir = current_file_path.parent
        
        # 현재 디렉토리의 파일들 나열
        return list_directory_files(str(current_dir), exclude_index=True)
    
    @env.macro
    def get_current_directory():
        """
        현재 페이지가 위치한 디렉토리 이름을 반환
        """
        current_page = env.page
        if not current_page:
            return "unknown"
        
        current_file_path = Path(current_page.file.src_path)
        return current_file_path.parent.name