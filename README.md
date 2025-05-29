Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql
$ git init
Initialized empty Git repository in C:/Users/Aluno/OneDrive/Área de Trabalho/connectmysql/.git/

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        conectmysql.py

nothing added to commit but untracked files present (use "git add" to track)

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git add .

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   conectmysql.py


Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git commit -m "Meu primeiro commit"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'Aluno@DESKTOP-T2VDKOU.(none)')

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git config --global user.email "caang.2024119tads0019@aluno.ifpi.edu.br"

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git config --global user.email
caang.2024119tads0019@aluno.ifpi.edu.br

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git config --global user.name "josevitor123271"

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git config --global user.name
josevitor123271

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git commit -m "Meu primeiro commit"
[master (root-commit) ad9b033] Meu primeiro commit
 1 file changed, 15 insertions(+)
 create mode 100644 conectmysql.py

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git remote add origin https://github.com/josevitor123271/atividade_warlles.git

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git branch
* master

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
$ git push origin master
info: please complete authentication in your browser...
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 489 bytes | 489.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/josevitor123271/atividade_warlles.git
 * [new branch]      master -> master

Aluno@DESKTOP-T2VDKOU MINGW64 ~/OneDrive/Área de Trabalho/connectmysql (master)
