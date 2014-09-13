# Vim Notes
Various notes picked up regarding vim, how to effectvely use it, settings and
cool tricks, etc.

## Settings for .vimrc

| Setting | Purpose |
|---------|---------|
| nmap \<leader\>P :set paste!\<cr\> | OsX-specific paste |
| nmap \<leader\>y :.w !pbcopy\<cr\>\<cr\> | OsX-specific copy |
| vmap \<leader\>y :w !pbcopy\<cr\>\<cr\> | OsX-specific copy |
| nmap \<leader\>p :r !pbpaste\<cr\> | OsX-specific paste |
