import re

section = re.compile(r'\\((?:subsection)|(?:section)|(?:chapter))(?:\[(.*)\])?{(.*)}')

filename = "thesisBySection/thesis-frontmatter.tex"
with open('originals/FullDis.tex') as dis:
	for line in dis:
		match = section.search(line)
		if match:
			filename = "thesisBySection/thesis-%s-%s.tex" % (match.group(1), match.group(2) or match.group(3))
		with open(filename, 'a+') as file:
			file.seek(0,2)
			file.write(line)