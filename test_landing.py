from playwright.sync_api import expect

def test_loginpage_landing(page):

    page.goto("https://app.3o3.co.kr/login")
    page.wait_for_load_state("networkidle")

    expect(page.get_by_role("button", name="카카오 계정으로 계속하기")).to_be_visible()

def test_loginpage_click(page):

    page.goto("https://app.3o3.co.kr/login")
    page.wait_for_load_state("networkidle")

    page.get_by_role("button", name="예상 환급액을 계산하는 기준").click()
    expect(page.get_by_role("heading", name="예상 환급액 계산 기준")).to_be_visible()


def test_loginpage_failcase(page):

    page.goto("https://app.3o3.co.kr/login")
    page.wait_for_load_state("networkidle")

    assert page.get_by_role("heading",name="실패").is_visible(), "기획대로 실패"