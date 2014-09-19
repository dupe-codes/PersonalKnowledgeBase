# Git Notes
## Notes on git and how to best use all of its awesomeness.

Useful Commands
---------------
| Command | Use | Notes |
|---------|-----|-------|
| git rebase | Used to place local commits on top of commits from another branch | With -i, can be used to squash commits |
| git diff --name-only | Shows all files changed in set of commits | Useful when you want to blast through them doing the same thing to each |
| git reflog | | |
| git cherry-pick | Used to bring in a specific commit from another branch | |

Tips and Tricks
---------------

From mentor at work:
> Per recent conversation, @njdup and @SeWonJang, a handy bash alias for gitstuff: gitg is short for 'git get'. You can put the following code into your ~/.bashrc at the end and after you re-source your .bashrc, you should be able to start using it immediately. git get takes two mandatory parameters: a tree-ish (which can be a commit, a branch, a tag...) and a file path (relative to top of repo). The file named like 'bar/foo.sh' will be checked out by default as 'bar/foo.sh.lkg'. (lkg for 'last known good', and it also almost never conflicts with real file extensions....). You can also give a third parameter to specify the filename to write to. Beware, this doesnt check to see if the target file exists first
