f = open("data_labelings.tex", 'w')
f.write("\\documentclass{article}\n\\usepackage{amsmath, amsfonts, amssymb, tikz}\
        \n\\usepackage[margin=0.5in]{geometry}\n\\title{Graceful Ends}\n\\begin{document}\n")

files = ['1-1-1', '2-1-1', '3-1-1', '2-2-1', '4-1-1', '3-2-1', '2-2-2', '5-1-1',\
        '4-2-1', '3-3-1', '3-2-2', '6-1-1', '5-2-1', '4-3-1', '4-2-2', '3-3-2']
for fn in files:
    f.write("\\section{"+fn+"}\n")
    f.write("\\paragraph{Density}\mbox{}\\\\\n")
    density = open(fn+"density", 'r')
    f.write(density.read())
    density.close()
    f.write("\\paragraph{Lattice Points}\mbox{}\\\\\n")
    lattice_pts = open(fn+"points", 'r')
    f.write(lattice_pts.read())
    f.write("\\begin{figure}\n\t\\center\n\t\input{"+fn+".tikz"+"}\n\
            \\caption{Convex hull for the graceful ends of the tree "+fn+"}\n\\end{figure}\n")
    lattice_pts.close()
    f.write("\\paragraph{Facets of the convex hull "+fn+"}\\\n")
#    f.write("\\begin{itemize}")
    f.write("\\begin{align*}")
    with open(fn+"facets", 'r') as fp:
        for ind, line in enumerate(fp):
            line = list(map(lambda x: int(x), line.split()))
            signs = list(map( lambda x: " + " if x >= 0 else " - ", line))
            final = ""
            exists = []
            for i in range(len(line)):
                if line[i] != 0:
                    exists.append(i)
            for i in exists:
                if i != 0:
                    if exists[0] == i:
                        if signs[i-1] == " - ":
                            final += signs[i-1]
                    else:
                        final += signs[i-1]
                    final += str(abs(line[i]))
                    if i == 1:
                        final += "x"
                    if i == 2:
                        final += "y"
                    if i == 3:
                        final += "z"
                else:
                    final += str(line[i])
            final += " = 0"
            f.write(final + "\\\\")
    f.write("\\end{align*}")
#    f.write("\\end{itemize}")

f.write("\\end{document}")
f.close()
