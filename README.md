# The Hellenisation of Ancient Thrace Project
OSF: https://osf.io/fjnw5/ & DOI 10.17605/OSF.IO/FJNW5

## Author: 
**Petra Heřmánková (Janouchová), PhD** (petra.janouchova@gmail.com) 

<a href="https://orcid.org/0000-0002-6349-0540" target="orcid.widget" rel="noopener noreferrer" style="vertical-align:top;"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" style="width:1em;margin-right:.5em;" alt="ORCID iD icon">orcid.org/0000-0002-6349-0540</a>
* PhD, Charles University, Prague, Czech Republic (2011-2017)
* Researcher at Macquarie University, Sydney, Australia @ FAIMS Project (2016- )
* Academia.edu: https://mq.academia.edu/PetraJanouchova
* Twitter: @pettulda

## Author of the technical solution / Sectinator: 
**Brian Ballsun-Stanton, PhD** (https://github.com/Denubis)

## The Aim:
The database has been populated with epigraphic data from a geographic area broadly conceived as falling within Ancient Thrace in a manner that crosses national and linguistic boundaries, and with an emphasis on the spatio-temporal attributes of individual inscriptions. The database makes possible the quantified analysis of more than 4600 inscriptions and their attributes, and is available for use and reuse by other scholars in epigraphy, philology, archaeology and other disciplines.
The data has been primarily collected for the PhD project _Hellenisation of Ancient Thrace_ based at Charles University, conducted by Petra Janouchová.

## Structure of the repository:
* Originals - original of the text as exported from the Google Drive
* Prototypes - prototypes used by the Python Sectionator to parse the Orginal text
* thesisBySection - parsed text of the disseration to chapters and subchapters for easier compiling in ConTeXt
  * the typesetting environment (env_dis.tex)
  * the disertation product (dis_product.tex)
* sectinator.py + sectinator.sh - Python script parsing the text of the dissertation by chapters and subchapters
* convert.sh - script converting .docx to .tex, the format needed to parse the original dissertation document

## Dissertation:
* Link to the data used to write this dissertation can be found at https://github.com/petrajanouchova/hat_project
* Defense 14 Dec 2017 in Czech, English version of the text is scheduled for 2018 
* Preliminary results published in various articles (access via OSF: https://osf.io/fjnw5/) 
