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

## 4. CI/CD 파이프라인
```
- https://github.com/jeonjuhyeon/Project_3o3_web_automation
```

- 위의 Github Repository에는 GitHub Actions를 통한 CI 실행 기록이 포함되어 있으며,
  push 또는 수동 실행(workflow_dispatch)으로도 테스트를 실행할 수 있습니다.
- Ubuntu 기반 Github Runner에서 python 및 playwright 환경을 구성한 후, pytest를 통해 자동화 테스트를 수행합니다.
- 테스트 결과는 pytest-html을 통해 HTML 리포트로도 생성됩니다.
- 테스트 실패 시 GitHub Actions의 기본 이메일 알림을 사용하여 결과가 메일로 전달됩니다.

---

## 5. 추가 개선사항

- 현재 생성되는 HTML 리포트를 아티팩트로 업로드하여 CI 실행 이력별로 테스트 결과를 확인할 수 있도록 개선할 수 있습니다.
- CI 결과를 메일 뿐 아니라 실무에서는 슬렉 또는 팀즈와 연동하여 실패 상황을 빠르게 공유할 수 있도록 개선 할 수 있습니다.

---
