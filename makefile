run:
	polymake --script polytope_graceful.pl
	python3 calculate_lattice_density.py
	python3 make_tex.py
	latexmk --pdf 

clean:
	python3 graph_label.py

