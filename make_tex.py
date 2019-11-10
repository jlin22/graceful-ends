f = open("all_graceful_ends.tex", 'w')

def create_header(f):
    f.write("\\documentclass{article}\n \
             \\usepackage{amsmath, amsfonts, amssymb, tikz}\n \
             \\usepackage[margin=0.5in]{geometry}\n \
             \\title{Graceful Ends}\n \
             \\begin{document}\n")

def make_density_table(files):
    f.write("\\paragraph{} Here, the density is computed by the number of \
            graceful ends divided by the number of permutations on the \
            values of the vertices\n")
    f.write("\\begin{center}\n \
             \\begin{tabular}{| l | l | l |}\n \
             \\hline\n \
             Tree & Density Dec & Density Frac \\\\ \n")
    for fn in files:
        string = open(fn+"density", 'r').read().split()
        f.write(fn+" & "+str(string[2])+" & "+str(string[3])+"\\\\\n")
    f.write("\\hline\n \
             \\end{tabular}\n \
             \\end{center}")

def make_graceful_ends_table(files):
    f.write("\\paragraph{} This table shows how many graceful labelings \
            a particular tree has\n")
    f.write("\\begin{center}\n \
             \\begin{tabular}{| l | l | l |}\n \
             \\hline\n \
             Tree & Graceful Ends \\\\ \n")
    for fn in files:
        string = open(fn+"density", 'r').read().split()
        f.write(fn+" & "+str(string[0])+"\\\\\n")
    f.write("\\hline\n \
             \\end{tabular}\n \
             \\end{center}")

def make_lattice_points_table(files):
    f.write("\\paragraph{} This table shows how many lattice points are in \
            the convex hull of the set of graceful ends\n")
    f.write("\\begin{center}\n \
             \\begin{tabular}{| l | l | l |}\n \
             \\hline\n \
             Tree & Lattice Points \\\\ \n")
    for fn in files:
        n_lattice_points = open(fn+"points", 'r').read().split()
        f.write(fn+" & "+str(n_lattice_points[0])+"\\\\\n")
    f.write("\\hline\n \
             \\end{tabular}\n \
             \\end{center}")

files = ['1-1-1', '2-1-1', '3-1-1', '2-2-1', '4-1-1', '3-2-1', '2-2-2', '5-1-1',\
        '4-2-1', '3-3-1', '3-2-2', '6-1-1', '5-2-1', '4-3-1', '4-2-2', '3-3-2']

create_header(f)
make_density_table(files)
make_graceful_ends_table(files)
make_lattice_points_table(files)

for fn in files:
    f.write("\\section{"+fn+"}\n")
    f.write("\\paragraph{Lattice Points}\mbox{}\\\\\n")
    lattice_pts = open(fn+"points", 'r')
    f.write(lattice_pts.read())
    f.write("\\begin{figure}\n\t\\center\n\t\input{"+fn+".tikz"+"}\n\
            \\caption{Convex hull for the graceful ends of the tree "+fn+"}\n\\end{figure}\n")
    lattice_pts.close()
    f.write("\\paragraph{Facets of the convex hull "+fn+"}\\\n")
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

f.write("\\end{document}")
f.close()
