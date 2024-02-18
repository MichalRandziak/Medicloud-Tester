from playwright.sync_api import Page, expect
import pytest


def test_01kalendarHappyPath(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-01T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-01-31T00:00:00.000Z")
    page.get_by_role("button", name="Execute").click()
    # checks if execution ends up with HTTP 200 OK
    expect(page.locator('xpath=//tr[@class=\'response\']//td[@class=\'response-col_status\']')).to_contain_text("200")
    page.close()

# pozitivny test hranicne hodnoty ... maximalny
def test_02kalendarMaxRangeSuccess(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-01T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-02-10T00:00:00.000Z")
    page.get_by_role("button", name="Execute").click()
    # checks if execution ends up with HTTP 200 OK
    expect(page.locator('xpath=//tr[@class=\'response\']//td[@class=\'response-col_status\']')).to_contain_text("200")
    page.close()


# Negativny test hranicne hodnoty ... maximalny limit prekroceny
def test_03kalendarMaxRangeFailed(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-01T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-02-11T00:00:00.000Z")
    page.get_by_role("button", name="Execute").click()
    # checks if execution ends up with HTTP 400 Bad Request
    expect(page.locator('xpath=//tr[@class=\'response\']//td[@class=\'response-col_status\']')).to_contain_text("400")
    expect(page.get_by_text("Date range too big max 40 days")).to_be_visible()
    page.close()

# Negativny test nevalidny vstup ... Start date smaller then End date
def test_04kalendarIncorectDateFailed(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-31T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-01-01T00:00:00.000Z")
    page.get_by_role("button", name="Execute").click()
    # checks if execution ends up with HTTP 400 Bad Request
    expect(page.locator('xpath=//tr[@class=\'response\']//td[@class=\'response-col_status\']')).to_contain_text("400")
    expect(page.get_by_text("Start date must be before end date")).to_be_visible()
    page.close()

# Negativny test kontrola validacie
def test_05kalendarValidationFailed(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-01T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-01-32T00:00:00.000Z")
    page.get_by_role("button", name="Execute").click()
    # validation exception exists
    expect(page.get_by_text("Please correct the following")).to_be_visible()
    page.close()

def test_06kalendarTaskTC(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-12T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-01-12T23:59:59.999Z")
    page.get_by_role("button", name="Execute").click()
    # checks if execution ends up with HTTP 200 OK
    expect(page.locator('xpath=//tr[@class=\'response\']//td[@class=\'response-col_status\']')).to_contain_text("200")
    expect(page.get_by_text("[ { \"username\": \"Carla Tapia DDS")).to_be_visible()
    expect(page.get_by_text("\"date\": \"2024-01-12T05:04:37\"")).to_be_visible()
    expect(page.get_by_text("\"description\": \"BmyDzNHzU3pj3QfOk\" } ]")).to_be_visible()
    expect(page.get_by_text("content-length: 95")).to_be_visible()
    page.close()

#  test rozdielnych casovych pasiem
# @pytest.mark.skip(reason="Defect: Def_001")
def test_kalendarDifferentTimeZone(page: Page):

    page.goto("http://pumec.zapto.org:8000/docs#/default/read_orders_orders__get")
    # check page load
    assert page.title() == "FastAPI - Swagger UI"
    page.get_by_role("button", name="Try it out").click()
    # checks the input fields are editable
    expect(page.get_by_placeholder("start_date").first).to_be_editable()
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("start_date").click()
    page.get_by_placeholder("start_date").fill("2024-01-12T00:00:00.000Z")
    expect(page.get_by_placeholder("end_date").first).to_be_editable()
    page.get_by_placeholder("end_date").click()
    page.get_by_placeholder("end_date").fill("2024-01-12T23:59:59.999")
    page.get_by_role("button", name="Execute").click()
    page.wait_for_timeout(1)
    # checks if execution ends up with HTTP 200 OK
    expect(page.locator('xpath=//tr[@class=\'response\']//td[@class=\'response-col_status\']')).to_contain_text("200")
    page.close()