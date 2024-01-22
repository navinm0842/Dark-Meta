from pywinauto.application import Application
import pywinauto.keyboard as kb
import pywinauto.mouse as ms
from time import sleep
from bs4 import BeautifulSoup
import csv

app=Application(backend='uia').start('C:\\Users\\Navin Prasath\\Desktop\\Tor Browser\\Browser\\firefox.exe')
app=Application(backend='uia').connect(title='Connect to Tor — Tor Browser',timeout=10)
#app.ConnecttoTorTorBrowser.print_control_identifiers()
connect = app.ConnecttoTorTorBrowser.child_window(title="Connect", auto_id="connectButton", control_type="Button")
connect.click_input()
sleep(10)
search = app.ConnecttoTorTorBrowser.child_window(title="Search with DuckDuckGo or enter address", auto_id="urlbar-input", control_type="Edit")
search.type_keys("https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion/")
kb.send_keys("{ENTER}")
sleep(10)
tor_window = app.window(title_re='.*Tor Browser.*')
sleep(25)
#app.ConnecttoTorTorBrowser.print_control_identifiers
tor_window.Edit.type_keys("^u")
# Send Ctrl+U to open page source
sleep(15)  # Wait for the page source to open (adjust as needed)
ms.double_click(button='left', coords=(250, 350))
# Copy the entire page source
tor_window.type_keys('^a')  # Send Ctrl+A (select all) and Ctrl+C (copy)
tor_window.type_keys('^c')
# Get the clipboard content
import win32clipboard
win32clipboard.OpenClipboard()
html_code = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
soup = BeautifulSoup(html_code,'html.parser')
print(soup.title)
# Print or process the HTML code
meta = soup.find_all('meta')
# Print or process the HTML content as needed
meta_info_list = []
# Append meta information to the list
for tag in meta:
    name = tag.get('name', '')
    content = tag.get('content', '')
    meta_info_list.append({'Name': name, 'Content': content})
# Save the meta information into a CSV file
csv_file_path = 'meta_info.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Name', 'Content']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # Write the header
    writer.writeheader()
    # Write the rows
    writer.writerows(meta_info_list)

print(f"Meta information has been saved to '{csv_file_path}'.")

