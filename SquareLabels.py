import os
import subprocess

USE_CIRCLE_SHAPE = False

# Create Latex file
latex_path = "../Latex/"
latex_filename = "labels.tex"

latex_file = open(latex_path+latex_filename,"w+")

# Preamble
latex_file.write('''\documentclass[a4paper]{article}

\\pagestyle{empty}

\\usepackage[left=.75cm, top=1.9cm]{geometry}
\\setlength{\\parindent}{0pt}

\\usepackage{tikz}
\\newcommand{\\squarelabel}[4][]{
\\begin{scope}[xshift=#2,yshift=#3]
\\node [minimum width = 3.2cm,minimum height = 3.2cm,''')

if USE_CIRCLE_SHAPE:
    latex_file.write('circle,') 

latex_file.write('''
	path picture = {
    \\node [#1] at (path picture bounding box.center) {
    \\includegraphics[width=5.2cm]{#4}};
    }] {};
\\end{scope}}
    
\\newlength{\\xspacing}
\\setlength{\\xspacing}{0.28cm}

\\newlength{\\yspacing}
\\setlength{\\yspacing}{-0.25cm}

\\newlength{\\labelswidth}
\\setlength{\\labelswidth}{2.97cm}

\\newlength{\\labelsheight}
\\setlength{\\labelsheight}{-3cm}

\\begin{document}
\\noindent
\\begin{tikzpicture}
''')

# Insert images
art_path = "../Art/"
    
label_selection_filename = "LabelSelection.txt"
label_selection_file = open(art_path + label_selection_filename,"r")
adjustments_raw = label_selection_file.readlines()

adjustment_dict = dict()
for line in adjustments_raw:
    split_line = line.split(',',3)
    card_title = split_line[-1]
    if int(split_line[0].strip()) == 1:
        adjustment_dict[card_title.strip()] = (split_line[1].strip(),split_line[2].strip())
    
card_image_path = art_path + 'CardImages/'
card_image_titles = os.listdir(card_image_path)

for index, card_image_title in enumerate(adjustment_dict):
    latex_file.write('\\squarelabel[xshift=' + adjustment_dict[card_image_title][0] + 'cm,yshift=' + adjustment_dict[card_image_title][1] + 'cm]{' + str(index % 6) + '*(\\xspacing+\\labelswidth)}{' + str(int(index/6)) + '*(\\labelsheight+\\yspacing)}{"' + card_image_path + card_image_title +'"}\n')

label_selection_file.close()   

# End of file
latex_file.write('''
\end{tikzpicture}

\end{document}
''')

latex_file.close()

subprocess.check_call('pdflatex -output-directory ' + latex_path + ' ' + latex_path + latex_filename, shell=False)
os.remove(latex_path + latex_filename.split('.')[0] + '.log')
os.remove(latex_path + latex_filename.split('.')[0] + '.aux')