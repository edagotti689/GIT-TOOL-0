'''
1.using version control tool we can work together in a shared folder on the same set of files.
2. keep historical record of changes in the repository for future purpose.

#  link to know abot version control tool: 

https://www.seguetech.com/a-review-of-software-version-control-systems-benefits-and-why-it-matters/

# link to Download a git -> 

https://git-scm.com/download/win

(git - Disributed Version Control tool )
'''


git clone  url    --> Creates a GIT repository copy from a remote source

git status        --> To know git status

git add filename/directory  --> Adds files changes in your working directory.

git rm filename   --> Removes files from your working directory

git commit --amend --> To know current commit status

git commit -m " commit message " --> To commit local changes

git push      --> Pushes all the modified local objects to the remote repository

git reset --hard origin/master     --> Resets your working directory to the state of your last commit

git pull --> Fetches the files from the remote repository and merges it with your local repository.

git checkout "DataCenter/NXOS/AAA [ NX-OS ].wxml" --> To checkout cental repository file


## Branch 
git branch                  --> To list all branches 
git branch branchname       --> To create a new branch
git checkout -b branchname  --> to create a new branch
git checkout testing        --> Switched to branch "testing"
git branch -D testing       --> Deleted branch testing.
git branch -v               --> To see the last commit on each branch

## Git stash

git stash save " Added new file "     -->  To save all changes
git stash list                        -->  To get all saved list 
git stash apply stash@{0}             -->  To applay changes 

