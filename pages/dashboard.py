from pages.base_page import BasePage


class Dashboard (BasePage):
    main_page_field_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    main_page_logo_field_xpath = "//*[contains(@title, "Logo")]"
    add_player_button_xpath = "//*[text()="Add player"]"
    add_player_email_field_xpath = "//*[@name="email"]"
    add_player_left_leg_listbox_xpath = "//*[@role="option" and @data-value="left"]"
    add_player_district_mazovia_listbox_xpath = "//*[@role="option" and @data-value="mazowieckie"]"
    players_show_column_club_checkbox_xpath = "//*[@type="checkbox" and @value="club"]"
    players_matches_adding match_date_xpath = "//*[@name="date" and @type="date"]"
    main_page_logo_xpath = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[1]"
    sign_out_button_xpath = "//*[text()="Sign out"]"
    players_print_icon_xpath = "//*[@type="button" and @title="Print"]"
