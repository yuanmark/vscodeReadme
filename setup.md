# vscode 安裝

1. window: git -> anaconda -> vscode
    1. gitbash.exe (路徑設為放在path)
    1. anaconda (路徑設為放在path)
    1. vscode
    
1. ubuntu
    * 不用裝bash, vscode, 直接裝anaconda:
	1. sudo apt-get update	
	2. sudo apt install curl (for download anaconda)
	    * //search: https://www.anaconda.com/download/#linux (python3.6, 64bit installer)最新版的link
	3. curl -O https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh
	4. bash Anaconda3-5.1.0-Linux-x86_64.sh
	5. 會直接問是否要裝vscode，yes
	    * //if not: search: https://code.visualstudio.com/download for newest version
	    * //do vscode install: https://code.visualstudio.com/docs/?dv=linux64_deb
1. call vscode
    1. windows: click vscode
	2. ubuntu: code & (enter vscode)
    
1. 安裝 plugins: python, code runner, git history
