FLNM=twolaypod
INPFILE=${FLNM}.md

pandoc ${FLNM}.md -o index.html \
    --citeproc \
    --mathjax  \
    -t revealjs --slide-level=2 -s \
    # -V revealjs-url=/home/heiland/software/gits/reveal.js \
    -V theme=solarized \
    -V NavigationMode=linear \
    -V viewDistance=15 -V width=1280 -V height=880 -V margin=0.05
