" Cano's Vim Config Author: Cano
" Email: gcanoxl@gmail.com
"
" This config is lightweight, but smart development environment
" for Web front-end(HTML, CSS, JavaScript), python languages.
"
" You should install all tools of the list before use this config.
" List: git, curl, ctags, jedi, ipykernel, jupyter_client

" Enviroment initialization (compatible with neovim)
let g:VIM_HOME = expand('~/.vim')
if has('nvim')
    let g:VIM_HOME = expand('~/.config/nvim')
endif

" Vim-plug installation
" if vim-plug file (by default, it's VIM_HOME/autoload/plug.vim) is
" not exist, then download and install it from github.
let s:vim_plug_path = g:VIM_HOME.'/autoload/plug.vim'
if !filereadable(s:vim_plug_path)
    echo "Installing Vim-plug ..."
    echo ""
    let s:vim_plug_git = 'https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
    execute "!curl -fLo ".s:vim_plug_path." --create-dirs ".s:vim_plug_git
endif
let s:vim_plugged_path = g:VIM_HOME.'/plugged'

" Plugins Table
call plug#begin(s:vim_plugged_path)

" code browser
Plug 'majutsushi/tagbar'

" file tree browser
Plug 'scrooloose/nerdtree'
Plug 'Xuyuanp/nerdtree-git-plugin'

" fuzzy finder
Plug 'ctrlpvim/ctrlp.vim'

" python code completion
Plug 'davidhalter/jedi-vim', {'for': 'python'}

" ipython for nvim
Plug 'bfredl/nvim-ipy', {'for': 'python'}

" Syntax Checker
Plug 'vim-syntastic/syntastic'

" command fuzzy finder
Plug 'fisadev/vim-ctrlp-cmdpalette'

" colorscheme
Plug 'fisadev/fisa-vim-colorscheme'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

" Automatic installation.
function! s:is_need_install()
    for l:plug_name in g:plugs_order
        let l:plug_path = s:vim_plugged_path.'/'.l:plug_name
        if !isdirectory(l:plug_path)
            return 1
        endif
    endfor
endfunction

if s:is_need_install()
    echom "Found new plugin(s) need to install."
    :PlugInstall
endif

" No vi-compatible
set nocompatible

" Allow plugins by file type
filetype plugin on
filetype indent on

" Use fisa colorscheme
colorscheme fisa

" airline
let g:airline#extensions#tabline#enabled = 1
let g:airline_theme='bubblegum'

" Show line numbers
set nu

" Keep 3 lines when scrolling
set scrolloff=8

" Syntax highlight on
syntax on

" Always show status bar
set ls=2

" Incremental search
set incsearch
set hlsearch

" Tabs and spaces handling
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4

" Tab length for different file type.
autocmd FileType html setlocal shiftwidth=2 tabstop=2 softtabstop=2
autocmd FileType css setlocal shiftwidth=4 tabstop=4 softtabstop=4
autocmd FileType javascript setlocal shiftwidth=4 tabstop=4 softtabstop=4

" Key Mappings {
let mapleader=' '

" set escape to jk
inoremap jk <ESC>

" better command
nnoremap <silent> <leader><leader> :CtrlPCmdPalette<CR>

" general
nnoremap <silent> <leader>gq :xa<CR>
nnoremap <silent> <leader>ge :edit $MYVIMRC<CR>
nnoremap <silent> <leader>gr :source $MYVIMRC<CR>

" file
nnoremap <silent> <leader>fs :w<CR>
nnoremap <silent> <leader>ff :CtrlP<CR>
nnoremap <silent> <leader>fb :NERDTreeToggle<CR>

" buffer
nnoremap <silent> <leader>bf :CtrlPBuffer<CR>

" window
nnoremap <C-h> <C-w><C-h>
nnoremap <C-j> <C-w><C-j>
nnoremap <C-k> <C-w><C-k>
nnoremap <C-l> <C-w><C-l>
nnoremap <C-c> <C-w><C-c>
nnoremap <C-o> <C-w><C-o>

" code
nnoremap <silent> <leader>cb :TagbarToggle<CR>

" }

" NERDTree

" automatic open nerdtree when start up vim with a directory.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif

" automatic close nerdtree when only nerdtree window.
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Jedi
let s:assist_leader = ","

let g:jedi#goto_command = s:assist_leader."g"
let g:jedi#documentation_command = s:assist_leader."d"
let g:jedi#usages_command = s:assist_leader."n"

" Syntastic
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0