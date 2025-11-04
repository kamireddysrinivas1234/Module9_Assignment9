
import asyncio, os, socket, threading
from contextlib import closing
import uvicorn, pytest
from playwright.sync_api import Page, expect

def _find_free_port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(("", 0))
        return s.getsockname()[1]

@pytest.fixture(scope="session")
def server_url():
    port = int(os.getenv("E2E_PORT", _find_free_port()))
    config = uvicorn.Config("app.main:app", host="127.0.0.1", port=port, log_level="warning")
    server = uvicorn.Server(config)
    thread = threading.Thread(target=server.run, daemon=True); thread.start()
    for _ in range(50):
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.1): break
        except OSError:
            asyncio.sleep(0.1)
    yield f"http://127.0.0.1:{port}"

@pytest.mark.e2e
def test_ui_addition(page: Page, server_url):
    page.goto(server_url)
    page.fill("#a","2"); page.fill("#b","3")
    page.select_option("#op","add"); page.click("#btn")
    expect(page.locator("#result")).to_have_text("5")
