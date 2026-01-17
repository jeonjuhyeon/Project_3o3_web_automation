import os
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    is_ci = os.getenv("CI") == "true"

    with sync_playwright() as p:
        browser = p.chromium.launch(
        headless=is_ci,   
        slow_mo=0 if is_ci else 500
    )
        
        context = browser.new_context()
        page = context.new_page()

        yield page
        browser.close()