import os
import subprocess

# Create Latex file
latex_path = "../Latex/"
latex_filename = "statistics.tex"

latex_file = open(latex_path+latex_filename,"w+")

# Preamble
latex_file.write('''\\documentclass[a4paper]{article}

\\pagestyle{empty}

\\usepackage[margin=1.5cm]{geometry}
\\usepackage{tabularx}
\\usepackage[table]{xcolor}

\\begin{document}
\\begin{center}
{\\Huge Deck statistics}

\\bigskip
\\begin{Large}
\\rowcolors{2}{gray!25}{white}
\\begin{tabularx}{\\textwidth}{l|X|X|X|X|X|X|X|X}
\\hline
''')

image_path = "../Art/CardImages/"
image_titles = os.listdir(image_path)
for title in image_titles:
    latex_file.write(title[:-4] + ' & & & & & & & & \\\\ \n') #Removes .jpg from title ending

max_decks = 32
for i in range(max_decks-len(image_titles)):
    latex_file.write(' & & & & & & & & \\\\ \n') #Removes .jpg from title ending

# End of file
latex_file.write('''\\hline
\\end{tabularx}
\\end{Large}
\\end{center}
\\end{document}
''')

latex_file.close()

subprocess.check_call('pdflatex -output-directory ' + latex_path + ' ' + latex_path + latex_filename, shell=False)
os.remove(latex_path + latex_filename.split('.')[0] + '.log')
os.remove(latex_path + latex_filename.split('.')[0] + '.aux')