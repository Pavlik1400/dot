" Theme
set termguicolors
set t_Co=256				" iTerm2 supports 256 color mode. 
" set background=light		light background
" colorscheme PaperColor		colorscheme
colorscheme monokai

syntax on					" syntax highlighting
filetype plugin indent on	" use the file type plugin
set ai						" auto indent
set ruler					" show the cursor position

set tabstop=4                   " a tab is four spaces
set softtabstop=4               " when hitting <BS>, pretend like a tab is removed, even if spaces
set noexpandtab                 " don't expand tabs to spaces by default
set shiftwidth=4                " number of spaces to use for autoindenting
set shiftround                  " use multiple of shiftwidth when indenting with '<' and '>'
set backspace=indent,eol,start  " allow backspacing over everything in insert mode
set autoindent                  " always set autoindenting on
set copyindent                  " copy the previous indentation on autoindenting

" lightline config
set laststatus=2
set noshowmode
set nu

" Plugins
call plug#begin('~/.vim/plugged')
Plug 'itchyny/lightline.vim'

Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/preservim/nerdcommenter'
Plug 'https://github.com/airblade/vim-gitgutter'

"Plug 'neoclide/coc.nvim', {'branch': 'release'}
"Plug 'jiangmiao/auto-pairs'

call plug#end()

set splitbelow splitright


" NERDTree config
map <C-n> :NERDTreeToggle<CR>

" NerdCommenter shortcut
map <C-\> <leader>c<space>

vmap <C-c> y:call system("xclip -i -selection clipboard", getreg("\""))<CR>:call system("xclip -i", getreg("\""))<CR>
