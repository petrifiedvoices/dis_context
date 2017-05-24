#!/bin/bash


pandoc originals/JanouchovaDisertace.docx -t ConTeXt -o originals/FullDis.tex --wrap=none --smart --normalize --chapters
