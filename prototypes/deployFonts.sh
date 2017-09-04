#!/bin/bash

set -euo pipefail
root=$(git rev-parse --show-toplevel)

# mkdir -p $root/.fonts
# cat > $root/.fonts/toDownload <<HereDoc 
# https://github.com/adachis/Lifehacker.me/raw/master/fonts/HelveticaNeue.ttf
# https://github.com/jackhumbert/kle-image-creator/raw/master/fonts/HelveticaNeueItalic.ttf
# https://github.com/jackhumbert/kle-image-creator/raw/master/fonts/HelveticaNeueLight.ttf
# https://github.com/jackhumbert/kle-image-creator/raw/master/fonts/HelveticaNeueLightItalic.ttf
# https://github.com/adachis/Lifehacker.me/raw/master/fonts/HelveticaNeue-Bold.ttf
# HereDoc
# wget --directory-prefix=$root/.fonts -i $root/.fonts/toDownload -nc

sudo apt-get update
sudo apt install fonts-sil-gentium-basic fonts-sil-gentiumplus

export OSFONTDIR=$HOME/.fonts:/usr/share/fonts/truetype/
# export OSFONTDIR=$HOME/.fonts
echo $OSFONTDIR

mtxrun --script fonts --reload
luatools --generate
# mtxrun --script fonts --list --all --pattern=*
context --reload
mtxrun --script fonts --list --all --pattern=Gent*
