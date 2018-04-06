# Git operation
1. Git概念&使用：xmind
1. 整理(2)： local開git, remote sync
    1. vs-term:
        1. git config --global user.email "mail"
        1. git config --global user.name "id"
        1. cd local-DIR
        1. git init
        1. git remote add origin github-URL
        1. git pull github-URL master
    1. vs: open folder
        1. do some changes
        2. push
            1. if ask: publish: yes
            1. if ask: id/pass: give
1. 整理： local開git, remote sync
    1. git: new a repo (name:XXX)
    1. vsc: open a dir, 
    1. vsc: 
        1. git/上方git/init commit
        1. add readme.md (this file)
        1. commit it
    1. vsc-term: 
        1. git remote add origin https://github/username/XXX
        1. git -v (verify remote repo exist)
    1. vsc: 
        1. push/sync as usual
1. 細節描述
    3.    github: login, create new project -> get URL (ex.     https://github.com/yuanmark/protfolio)
        *    順便安裝：octotree (chrome store) -> 開啟此plugin後，將原本URL改為上面 我的URL
    2.    vscode console : 只要做一次
        1.    git config --global user.email "yuanmark@gmail.com"
        2.    git config --global user.name "yuanmark"
    1. vscode: open a root-dir folder (repo會裝在root-dir/protfolio)
        1. vscode console:
            1. git clone https://github.com/yuanmark/protfolio
            1. do edit... comit to local
            1. git mode: commit to local
    		1. push: click 左下角的上傳箭號(如果出現輸入帳密，就輸入)
            1. now test => success
    1. outside vscode: new a root-dir/target-folder (repo會裝在 root-dir/target-folder)
        1. vscode: open target-folder
        1. vscode console:
            1. cd ..
            1. git clone https://github.com/yuanmark/folder target-folder
            1. do edit... comit to local
            1. git mode: commit to local
    		1. push: click 左下角的上傳箭號(如果出現輸入帳密，就輸入)
            1. now test => success

