from playwright.sync_api import expect
import re

def test_redbus(page):
    page.goto("https://www.redbus.in/")
    title = page.title()
    expect(page, "redirected" ).to_have_title("Bus Booking Online and Train Tickets at Lowest Price - redBus")
    assert title == "Bus Booking Online and Train Tickets at Lowest Price - redBus"
    from_tab = page.locator("//div[text()='From']")
    from_tab.click()

    from_input_field = page.locator("//input[@class='inputField___a5ec46']")
    from_input_field.fill("Mumbai")
    mumbai_option = page.locator("//div[@aria-label='Mumbai']")
    mumbai_option.click()

    to_input_field = page.locator("//input[@class='inputField___a5ec46']")
    to_input_field.fill("Pune")
    pune_option = page.locator("//div[@aria-label='Pune']")
    pune_option.click()

    to_date_field = page.locator('//div[@class="dojWrapper___9b2a92"]')
    to_date_field.click()
    date_of_travel = page.locator("//div[@aria-label = 'Sunday, November 30, 2025']")
    date_of_travel.click()

    search_btn = page.locator("//button[@aria-label='Search buses']")

    with page.expect_navigation():
        search_btn.click()

    assert 'bus-ticket' in page.url

