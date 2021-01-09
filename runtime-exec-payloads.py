"""
针对不同环境通过将命令编码成Base64进行伪装，避免因执行命令时受环境的限制而造成麻烦
"""

import base64
import subprocess

instruct = input('Please input your instruction:\n>')
instruct_encode = str(base64.b64encode(instruct.encode('utf-8')))[2:-1]

print('Please choose the mode you want to have:')
print('1.Bash	2.Powershell	3.Python	4.Perl')
choice = int(input())

if choice == 1:
	instruct = 'bash -c {echo, ' + instruct_encode + '}|{base64, -d}|{bash, -i}'
elif choice == 2:
	popen = subprocess.Popen(['powershell', '[Convert]::ToBase64String( [System.Text.UnicodeEncoding]::Unicode.GetBytes(\'' + instruct + '\') )'], stdout=subprocess.PIPE, shell=True)
	out, err = popen.communicate()
	instruct_encode = str(out)[2:-5]
	instruct = 'powershell.exe -NonI -W Hidden -NoP -Exec Bypass -Enc ' + instruct_encode
elif choice == 3:
	instruct = 'python -c exec(\'' + instruct_encode + '\'.decode(\'base64\'))'
elif choice == 4:
	instruct = 'perl -MMIME::Base64 -e eval(decode_base64(\'' + instruct_encode + '\'))'

print(instruct)



