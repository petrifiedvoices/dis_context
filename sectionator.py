#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import os
import shutil
import sys
import codecs

section = re.compile(r'\\((?:section)|(?:chapter))(?:\[(.*)\])?{(.*)}')


try:
	shutil.rmtree('thesisBySection')
except:
	print("ThesisBySection not found, all good.")
	pass

try:
	os.mkdir('thesisBySection')
	os.mkdir('thesisBySection/frontmatter')
except:
	print("Could not make thesis by section. Dying")	
	sys.exit(1)

components = "thesisBySection/disproduct.tex"


with codecs.open(components, 'w', "utf-8") as file:
	file.write(u"""
\environment env_dis


\setupinteraction
  [title=Hellénizace antické Thrákie ve světle epigrafických nálezů,
   subtitle=Hellenisation of Ancient Thrace based on epigraphical evidence,
   author=Petra Janouchová,
   keyword={epigrafika, Thrákie, kulturní kontakt, nápisy, epigrafická produkce, komplexní společnost}]

%% For PDF/A
\setupbackend[
format={pdf/a-1a:2005}, 
profile={default_cmyk.icc,default_rgb.icc,default_gray.icc},
intent=ISO coated v2 300\letterpercent\space (ECI)]

%% Tagged PDF
%% method=auto ==> default tags by Adobe
\setupbackend[export=yes]
\setupstructure[state=start,method=auto]

\startproduct dis_product

\component frontmatter/titlepage.tex

""")


shutil.copyfile('prototypes/titlepage.tex', 'thesisBySection/frontmatter/titlepage.tex')	
shutil.copyfile('prototypes/env_dis.tex', 'thesisBySection/env_dis.tex')	

filename = "thesisBySection/frontmatter/thesis-frontmatter.tex"
texname = "frontmatter/thesis-frontmatter.tex"
chapter = "frontmatter" 

with codecs.open(u'originals/FullDis.tex', "r", "utf-8") as dis:
	for line in dis:
		match = section.search(line)
		if match:
			print(match.group(0), match.group(1), match.group(2), match.group(3))
			if (match.group(1) == "chapter"):
				chapter = u"%s" % (match.group(3))
				os.mkdir('thesisBySection/%s' % chapter)


			with codecs.open(filename, 'a+', "utf-8") as file:
				file.seek(0,2)
				file.write("\stopcomponent")
	
			texname = u"%s/%s-%s.tex" % (chapter, match.group(1), match.group(2) or match.group(3))
			filename = u"thesisBySection/%s" % (texname)
			with codecs.open(filename, 'w', "utf-8") as file:
				file.seek(0,2)
				file.write("""
\environment ../env_dis
\startcomponent %s-%s
""" % (match.group(1), match.group(2) or match.group(3)))


			with codecs.open(components, 'a+', "utf-8") as file:
				file.seek(0,2)
				file.write(u"\component {%s}\n" % (texname))

#		print(texname, filename, chapter)

		


		with codecs.open(filename, 'a+', "utf-8") as file:
			file.seek(0,2)
			file.write(line)


with open(components, 'a+') as file:
	file.write("""
\stopproduct	           
	           """)