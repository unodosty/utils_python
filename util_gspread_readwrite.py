import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from df2gspread import df2gspread as d2g

scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]
json_file_name = 'json file'
credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

spreadsheet_url = 'input your spread sheet url'

# 스프레스시트 문서 가져오기
doc = gc.open_by_url(spreadsheet_url)

# 시트 선택하기
worksheet = doc.worksheet('worksheet name')
data = pd.DataFrame(worksheet.get_all_records())

df = data[['A']].copy()

spreadsheet_key = 'spreadsheet_key'
wks_name = 'new_sheet'
d2g.upload(df, spreadsheet_key, wks_name, credentials=credentials, row_names=True)
