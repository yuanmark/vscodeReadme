# Git operation
1.    Git概念&使用：xmind
3.    github: login, create new project -> get URL (ex. https://github.com/yuanmark/protfolio)
    *    順便安裝：octotree (chrome store) -> 開啟此plugin後，將原本URL改為上面我的URL
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
1. outside vscode: new a root-dir/target-folder (repo會裝在root-dir/target-folder)
    1. vscode: open target-folder
    1. vscode console:
        1. cd ..
        1. git clone https://github.com/yuanmark/folder target-folder
        1. do edit... comit to local
        1. git mode: commit to local
		1. push: click 左下角的上傳箭號(如果出現輸入帳密，就輸入)
        1. now test => success
