## 1. 개요
삼쩜삼 웹 로그인 페이지를 대상으로
Playwright + pytest를 사용한 간단한 자동화 테스트 프로젝트입니다.

---

## 2. 테스트 시나리오
- 로그인 페이지 랜딩 확인
- '예상 환급액 계산 기준' 버튼 클릭 확인
- CI 실패 알림 검증을 위한 의도적 실패 테스트

실제 로그인 인증은 포함하지 않고, UI 노출 및 사용자 인터랙션 시나리오를
자동화 대상으로 선정하였습니다.

--- 

## 3. 실행방법

```bash
pip install -r requirements.txt
python -m playwright install

pytest --html=report.html --self-contained-html
```
---

