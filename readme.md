## BeautifulSoup

### 특징
- HTML과 XML파일에서 데이터를 뽑아내기 위한 파이썬 라이브러리
- HTML과 XML의 트리 구조를 탐색, 검색, 변경 가능
- 다양한 파서(parser)를 선택하여 이용 가능

### 파서의 종류
- html.parser 
    - 선언: BeautifulSoup(markup, 'html.parser') 
    - 장점: 설치 필요 없음 적절한 속도
- lxml HTML parser
    - 선언: BeautifulSoup(markup, 'lxml')
    - 장점: 매우 빠름
    - 단점: lxml 설치 필요
- lxml XML parser
    - 선언: BeautifulSoup(markup, 'lxml-xml'), BeautifulSoup(markup, 'xml') 
    - 장점: 매우 빠름, 유일한 xml parser
    - 단점: lxml 설치 필요
- html5lib
    - 선언: BeautifulSoup(markup, 'html5lib')
    - 장점: 웹 브라우저와 같은 방식으로 파싱 유용한 html5 생성
    - 단점: html5lib 추가 설치, 매우 느림
    