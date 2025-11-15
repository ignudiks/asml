class Latex:

    def __init__(self):
        self.begin_documet = []
        self.begin_documet.append(r"\documentclass[12pt]{extarticle}")
        self.begin_documet.append(r"\usepackage{lmodern}")
        self.begin_documet.append(r"\pagestyle{empty}")
        self.begin_documet.append(
            r"\usepackage[letterpaper, left=0cm, right=0cm, top=0.2cm, bottom=0cm]{geometry}"
        )
        self.begin_documet.append(
            r"\renewcommand\normalsize{\fontsize{30}{30}\selectfont}"
        )
        self.begin_documet.append(r"\extrafloats{100}")
        self.begin_documet.append(r"\begin{document}")

        self.begin_tabular = r"\begin{center}\begin{tabular}{ccccc|ccccc|ccccc}"
        self.hline = r"\hline"
        self.end_tabular = r"\end{tabular}\end{center}"

        self.end_document = r"\end{document}"
   
