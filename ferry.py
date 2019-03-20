from selenium import webdriver
from selenium.webdriver.support.ui import Select
import schedule
import time

# ユーザ名
user_name = 'メールアドレス'
# パスワード
password = 'パスワード'
# 出発
port_dep = 'TRG'
# 到着
port_arr = 'TMA'
# ナンバープレート
p1 = "大阪"
p2 = '1'
p3 = "あ"
p4 = '1234'
# 排気量
p5 = '250'

"""
    HOK 北海道（小樽・苫小牧東）
    OTR 小樽
    TMA 苫小牧東
    KAN 関西（舞鶴・敦賀）
    MAI 舞鶴
    TRG 敦賀
    NIG 新潟
    AXT 秋田
"""

def job():
    # 1.新日本海フェリーのサイトを開く
    browser = webdriver.Firefox()
    browser.get('https://frens.snf.co.jp/login')

    # 2.ログイン・メールアドレス
    elem_username = browser.find_element_by_name('mailAddress')
    elem_username.send_keys(user_name)

    # 3.ログイン・パスワード
    elem_password = browser.find_element_by_name('password')
    elem_password.send_keys(password)
    elem_login_btn = browser.find_element_by_class_name('button')
    elem_login_btn.click()

    # 4.検索・日付指定
    departure = Select(browser.find_element_by_name('departureCode'))
    departure.select_by_value(port_dep)

    arrival = Select(browser.find_element_by_name('arrivalCode'))
    arrival.select_by_value('TMA')

    btn_departure_date = browser.find_element_by_id('imgDepartureDate')
    btn_departure_date.click()

    departure_day = browser.find_element_by_xpath('/html/body/div[2]/div[2]/table/tbody/tr[4]/td[5]')
    departure_day.click()

    btn_search = browser.find_element_by_id('serch')
    btn_search.click()

    # 5.便一覧
    funabin = browser.find_element_by_class_name('binSelectSubmit')
    funabin.click()

    # 6.部屋(ツーリストA)
    room = browser.find_element_by_xpath('/html/body/div/div[3]/div[3]/div/div[2]/table/tbody/tr[9]/td[4]/form/button')
    room.click()

    # 7.大人一人
    person = Select(browser.find_element_by_name('adults'))
    person.select_by_value('1')
    btn_select = browser.find_element_by_id('select-button')
    btn_select.click()
    btn_commitAdvance = browser.find_element_by_id('commitAdvance').click()
    btn_commitAdvance = browser.find_element_by_id('commitAdvance').click()

    # 8.車両の追加
    btn_vehicleAdd = browser.find_element_by_id('vehicleAdd').click()

    bikes1 = Select(browser.find_element_by_id('bikes1')).select_by_value('1')
    select_button = browser.find_element_by_id('select-button').click()

    # ナンバープレート入力
    plate1 = browser.find_element_by_id('plate1_0').send_keys(p1)
    plate2 = browser.find_element_by_id('plate2_0').send_keys(p2)
    plate3 = browser.find_element_by_id('plate3_0').send_keys(p3)
    plate4 = browser.find_element_by_id('plate4_0').send_keys(p4)
    numericData = browser.find_element_by_id('numericData_0').send_keys(p5)

    # 確認画面へ
    commitReturn = browser.find_element_by_id('commitReturn').click()

schedule.every().day.at('9:00').do(job)

while True:
    schedule.run_pending()
    time.sleep(1)