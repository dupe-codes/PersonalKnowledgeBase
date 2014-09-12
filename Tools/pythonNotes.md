# Python Notes
Tips, tricks, and knowledge acquired on my road to becoming a true Pythonista

# Useful Commands
## Style Checks
    for FILE in `git diff --name-only HEAD~1 | grep '.py$'`; do pep8 $FILE; done
    for FILE in `git diff --name-only HEAD~1 | grep '.py$'`; do pylint $file; done

