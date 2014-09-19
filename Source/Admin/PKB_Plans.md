# Current Plans
## Main Plans
- House everything within this git repository under strict version control
- Take notes in markdown, written in Vim
    - Use github API to convert markdown notes to HTML
    - Create links between documents and table of contents so notes can be
    easily traversed
    - Add authentication to avoid github rate-limiting
- Write script to extract todo list from Todoist, have up to date here
    - Potentially replace use of Todoist with my own todo system?
- Automate updating of todo list and conversion of markdown to HTML
- Transfer over Evernote notes
- Make embedded python system, something like `file.pymd` which compiles into markdown
    - Allow creation of layouts, can extend layouts
    - Dynamic creation of links?
    - Create compiler as a python class
        - In PKB, write 'compile' script which instantiates compiler object and uses it to compile all `*.pymd` files into markdown

- Add in spellchecking feature, runs through all markdown notes and spellchecks them

- Pretty things up (add css)

## Quick Note Functionality
- Create a simple app that saves quick notes into the PKB
    - Add in authentication so only I can access
- Request sent to server which contains note contents
- Server forms markdown note and adds it to the repo
- Automatically re-render the updated PKB
- Automatically pushs to github
    - Need github auth for both.. so need to figure out how to get credentials
    up on heroku safely
        - Look in to setting heroku ENV variables and using those
- Incorporate categories to save notes in specific directories

## Fun Subplans
- Write a live-streaming twitter feed script
