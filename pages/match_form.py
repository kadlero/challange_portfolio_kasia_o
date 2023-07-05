from pages.base_page import BasePage


class LoginPage(BasePage):
    add_match_enemy_team_field_xpath = "//*[@name="enemyTeam"]"
    add_match_date_field_xpath = "//*[@name="date" or @type="date"]"
    add_match_match_at_home_checkbox_xpath = "//*[@type="radio" and @name = "matchAtHome"]"
    add_match_clear_button_xpath = "//*[text()="Clear"]"
    # Błąd - 2 checkboxy nazwane tak samo - wyświetlą się 2 wyniki
    add_match_my_team_score_inputBase_xpath = "//*[@name="myTeamScore"]"
    add_match_submit_button_xpath = "//*[@type = "submit"]"
    add_match_web_match_field_xpath = "//*[@name="webMatch"]"
    add_match_number_inputBase_xpath = "//*[contains(@name, "number")]"
    add_match_league_field_xpath = "//*[contains(@name, "league")]"
    add_match_rating_field_xpath = "//*[contains(@name, "rating")]"