#this will install the following tools

#Set-ExecutionPolicy Unrestricted -Scope LocalMachine

#install choco
#Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

#install tools
#choco install magic-wormhole -y
#choco install docker-desktop -y
#choco install gpg4win -y
#choco install nodejs -y
#choco install mattermost-desktop -y
#choco install vscode.install -y
#choco install git.install -y
#choco install oh-my-posh -y

#configure oh-my-posh terminal
#oh-my-posh install font meslo

COPY '.\BloodUnicorn.omp.json' 'C:\Users\Administrator\Documents\WindowsPowerShell'
COPY '.\Microsoft.PowerShell_profile.ps1' 'C:\Users\Administrator\Documents\WindowsPowerShell\'

#import edge bookmarks for Platform One, OSA, and FlankSpeed
COPY .\Bookmarks 'C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data\Default'