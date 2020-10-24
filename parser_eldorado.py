import requests
from bs4 import BeautifulSoup as BS
from dicttoxml import dicttoxml
# from xml.dom.minidom import parseString
import json
base_url = "https://www.eldorado.ru/c/smartfony/?page="
headers = {
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'max-age=0',
'cookie': 'reuserid=5475ebe8-4d5c-4683-8004-75290b916392; ABT_test=B; AUTORIZZ=0; AC=1; lv_user_org=0; el_group_user_org=0; bonus_cobrand_showed=0; __utmz=267034714.1600103161.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _dy_c_exps=; _gcl_au=1.1.2003485482.1600103162; rrpvid=923673875144958; rcuid=5e806ecd86040900013e94cb; _dycnst=dg; flocktory-uuid=cef9f9f8-2b14-4c13-937f-9589f9b30f7c-6; advcake_session_id=103ab805-a4be-57a2-2865-bdb03b523737; clickcake_id=9d855a3c-36d0-75fd-1524-b8259c66d407; _ga=GA1.2.1675587629.1600103161; tmr_lvid=6305655fd8445c1fdb094e22727ca351; tmr_lvidTS=1600103167552; uxs_uid=95043470-f6ac-11ea-8930-e17489101701; uxs_mig=1; _ym_uid=16001031691069000740; _ym_d=1600103169; __zzatgib-w-eldorado=MDA0dBA=Fz2+aQ==; _dyid=630504207108940707; _dycst=dk.l.c.ws.; _dy_geo=RU.EU.RU_SPE.RU_SPE_St%20Petersburg; _dy_df_geo=Russia..St%20Petersburg; _userGUID=0:kf2s46u5:kMSCmNxFFAnVYkrPRaLfgeR1SDnqatCS; _fbp=fb.1.1600103174549.1249084471; iRegionSectionId=11279; userSplit=B; rete_session=true; __utma=267034714.1675587629.1600103161.1600103161.1600446146.2; __utmc=267034714; dt=1; PHPSESSID=ulcf2paprp7n7p8ljb2acf955d; BITRIX_SM_SALE_UID=8375191499; show_region_popup=0; _dy_csc_ses=t; _dy_c_att_exps=; _gid=GA1.2.440652946.1600446150; clickcake_sid=e0c1a66b-3fb3-d630-1d76-635957de96f7; _ym_visorc_1937671=w; _dyjsession=5e3812fa2b3c549b9a756f43c06b8ada; dy_fs_page=www.eldorado.ru%2Fd%2Fsmartfony-i-gadzhety; dSesn=ff963a02-a24f-77b5-0e99-8075f61c08c3; _ym_isad=2; _dvs=0:kf8gbfb3:2M3KYxuovtmMaC77i3oqF1wljQi52Dko; _dy_toffset=-5; __utmb=267034714.7.10.1600446146; _dy_ses_load_seq=42853%3A1600446548659; _dy_lu_ses=5e3812fa2b3c549b9a756f43c06b8ada%3A1600446553721; _dy_soct=1007167.1011280.1600446148*1009413.1015421.1600446148*1025826.1047956.1600446148*1020255.1036211.1600446152*1024759.1045344.1600446548*1024887.1045767.1600446548*1003181.1004426.1600446548*1007065.1045386.1600446549*1007087.1011176.1600446549*1016756.1028814.1600446549*1027516.1052205.1600446561*1027515.1052204.1600446561; tmr_detect=0%7C1600446577811; cfidsgib-w-eldorado=lLSyuxopk13Y3Ekbc3MC7tyOIljQx4eDn6mb7Dc4H9stObN1myzSyyl9Tudj377rTye71IlQzH7YY99+n7QuP1c6QPzMO+4frUjAdlGlrDnLDWs24WtXJe4w7w8SPalhNp26Qo8cdgdlPnoeBATQjFXVBAlfV+5r4EMi8A==; tmr_reqNum=134; ADRUM=s=1600448068939&r=https%3A%2F%2Fwww.eldorado.ru%2Fc%2Fsmartfony%2F%3F0',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
# Запуск скрипта

# Скрипт парсит сайт эльдорадо
smartfones = []
i = 1
while True:
    resp = requests.get(base_url + str(i), headers=headers)
    i += 1
    if resp.status_code == 404:
        break
    html = resp.text
    bs_html = BS(html, "html.parser")
    products = bs_html.find_all("li", {"data-dy": "product"})
    for product in products:
        try:
            name = product.find("a", {"data-dy": "title"}).contents[0]
            href = "https://www.eldorado.ru" + product.find("a", {"data-dy": "title"}).attrs["href"]
            price = product.find("span", {"class": "sc-1xca1up-1 sc-3lsqu-1 kQIWtq"}).contents[0]
            actionprice = None if product.find("span", {"class": "sc-1gca38j-2 liWzlg"}) is None else \
            product.find("span", {"class": "sc-1gca38j-2 liWzlg"}).contents[0]
            smartfones.append({'name': str(name), "href": str(href), "price": str(price), "actionprice": str(actionprice)})
        except AttributeError:
            pass

# Записывает данные xml в файл eldorado.xml
xml = dicttoxml(smartfones)

with open('templates/eldorado.xml', 'wb') as file_output:
    file_output.write(xml)
